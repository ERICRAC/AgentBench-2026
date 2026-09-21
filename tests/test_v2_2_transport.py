"""Real subprocess fixtures, never a model call or an authenticated CLI exec."""

import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import v2_2_transport as transport


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "workspace"
        (self.workspace / "solution").mkdir(parents=True)
        self.capture = self.root / "capture"

    def run_fixture(self, code, **kwargs):
        return transport.capture_process([sys.executable, "-B", "-c", code], "fixture prompt",
                                         self.capture, cwd=self.workspace, **kwargs)

    def test_streams_and_stdin_preserved(self):
        result = self.run_fixture("import sys; print(sys.stdin.read()); print('stderr evidence', file=sys.stderr)")
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual((self.capture / "stdout.jsonl").read_text(), "fixture prompt\n")
        self.assertEqual((self.capture / "stderr.txt").read_text(), "stderr evidence\n")
        self.assertEqual(self.capture.stat().st_mode & 0o777, 0o700)

    def test_nonzero_preserves_partial_evidence(self):
        result = self.run_fixture("print('partial'); raise SystemExit(7)")
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["exit_code"], 7)
        self.assertEqual((self.capture / "stdout.jsonl").read_text(), "partial\n")

    def test_timeout_kills_and_checkpoints(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            self.run_fixture("import time; print('partial', flush=True); time.sleep(20)", timeout=0.5)
        state = json.loads((self.capture / "process.json").read_text())
        self.assertEqual(state["status"], "interrupted")
        self.assertEqual(state["exit_code"], -9)
        self.assertEqual((self.capture / "stdout.jsonl").read_text(), "partial\n")

    def test_large_output_is_not_truncated(self):
        self.run_fixture("import sys; sys.stdout.write('x' * 2000000)")
        self.assertEqual((self.capture / "stdout.jsonl").stat().st_size, 2000000)

    def test_binary_streams_preserved_without_decoding(self):
        self.run_fixture("import sys; sys.stdout.buffer.write(bytes(range(256)) * 4096); sys.stderr.buffer.write(b'\\xff' * 1048576)")
        self.assertEqual((self.capture / "stdout.jsonl").read_bytes(), bytes(range(256)) * 4096)
        self.assertEqual((self.capture / "stderr.txt").read_bytes(), b'\xff' * 1048576)

    @unittest.skipUnless(os.name == "posix", "POSIX interrupt semantics")
    def test_sigint_preserves_partial_streams_and_stops_child(self):
        child = "import sys,time; print('ready', flush=True); print('partial error', file=sys.stderr, flush=True); time.sleep(30)"
        code = ("import sys; from pathlib import Path; "
                f"sys.path.insert(0, {str(Path(transport.__file__).parent)!r}); "
                "from v2_2_transport import capture_process; "
                f"capture_process({[sys.executable, '-B', '-c', child]!r}, '', Path({str(self.capture)!r}), cwd=Path({str(self.workspace)!r}), timeout=5)")
        runner = subprocess.Popen([sys.executable, "-B", "-c", code],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                  start_new_session=True)
        try:
            deadline = time.monotonic() + 4
            while time.monotonic() < deadline:
                output = self.capture / "stderr.txt"
                if output.exists() and output.read_bytes() == b"partial error\n":
                    break
                time.sleep(0.01)
            else:
                self.fail("Synthetic child did not become ready")
            runner.send_signal(signal.SIGINT)
            runner.wait(timeout=3)
            state = json.loads((self.capture / "process.json").read_text())
            self.assertEqual(state["status"], "interrupted")
            self.assertEqual(state["error_type"], "KeyboardInterrupt")
            self.assertEqual(state["exit_code"], -9)
            self.assertEqual((self.capture / "stdout.jsonl").read_bytes(), b"ready\n")
            self.assertEqual(output.read_bytes(), b"partial error\n")
            with self.assertRaises(ProcessLookupError):
                os.kill(state["pid"], 0)
        finally:
            if runner.poll() is None:
                runner.send_signal(signal.SIGINT)
                runner.wait(timeout=7)

    def test_capture_cannot_be_reused(self):
        self.capture.mkdir()
        with self.assertRaises(FileExistsError):
            self.run_fixture("raise SystemExit(99)")

    def test_spawn_failure_recorded(self):
        with self.assertRaises(FileNotFoundError):
            transport.capture_process(["/nonexistent-agentbench-test"], "", self.capture, cwd=self.workspace)
        self.assertEqual(json.loads((self.capture / "process.json").read_text())["status"], "interrupted")

    def test_prepared_command_removes_legacy_sandbox(self):
        # Build only: this test must never invoke Codex.
        with patch("subprocess.Popen", side_effect=AssertionError("No model calls")):
            command = transport.prepared_command("MAIN", self.workspace, Path(sys.executable))
        self.assertNotIn("sandbox_mode", " ".join(command))
        self.assertNotIn("-P", command)
        self.assertIn('default_permissions="agentbench-v2-2"', command)
        self.assertEqual(command[-1], "-")
        self.assertIn('network.enabled=false', " ".join(command))

    def test_invalid_role_and_linked_solution_refused(self):
        with self.assertRaises(ValueError):
            transport.permissions("OTHER", self.workspace, Path(sys.executable))
        (self.workspace / "solution").rmdir()
        (self.workspace / "solution").symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            transport.isolated_command("MAIN", self.workspace, ["true"])


if __name__ == "__main__":
    unittest.main()
