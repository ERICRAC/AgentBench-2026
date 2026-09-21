"""Supervised pilot checks with synthetic candidates only."""
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_v2_2_supervised as pilot


class SupervisedTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.manifest = self.root / "manifest.json"
        self.manifest.write_text(json.dumps({"run_id": pilot.RUN_ID, "challenge": "calculator",
            "protocol_frozen": True, "launch_authorized": True, "inputs_sha256": {}}))
        self.patch = patch.object(pilot, "MANIFEST", self.manifest)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        workspace = self.root / "workspace"
        (workspace / "solution").mkdir(parents=True)
        (workspace / "CHALLENGE.md").write_text("Synthetic contract")
        pilot.relay.save(self.root / "preparation.json", {"run_id": pilot.RUN_ID,
            "manifest_sha256": pilot.relay.digest(self.manifest.read_bytes()),
            "baseline": pilot.relay.snapshot(workspace)})
        self.calls = []

    def fake(self, argv, prompt, capture, cwd):
        phase = pilot.relay.PHASES[len(self.calls)][0]
        self.calls.append(phase)
        result = pilot.relay.fake_transport({"phase": phase, "challenge": "calculator", "cwd": cwd})
        capture.mkdir()
        (capture / "stdout.jsonl").write_text(result["jsonl"])
        return {"exit_code": 0, "duration_seconds": 0}

    def test_three_sessions_and_no_reuse(self):
        result = pilot.run(self.root, self.fake)
        self.assertEqual(len(result["sessions"]), 3)
        self.assertEqual(result["status"], "candidate_sessions_completed_pending_independent_verification")
        self.assertTrue((self.root / "capture/snapshot-initial.json").exists())
        with self.assertRaises((ValueError, FileExistsError)):
            pilot.run(self.root, self.fake)
        self.assertEqual(len(self.calls), 3)

    def test_failure_stops_without_second_candidate(self):
        def failed(*args, **kwargs):
            state = self.fake(*args, **kwargs)
            return {**state, "exit_code": 7}
        with self.assertRaises(RuntimeError):
            pilot.run(self.root, failed)
        self.assertEqual(self.calls, ["main_initial"])
        state = json.loads((self.root / "capture/state.json").read_text())
        self.assertEqual(state["status"], "interrupted")
        self.assertEqual(len(state["attempts"][0]["observed_usage"]), 1)

    def test_unapproved_manifest_refused(self):
        data = json.loads(self.manifest.read_text())
        data["launch_authorized"] = False
        self.manifest.write_text(json.dumps(data))
        with self.assertRaises(PermissionError):
            pilot.run(self.root, self.fake)
        self.assertEqual(self.calls, [])

    def test_role_config_and_toml_arguments(self):
        for role, sandbox in (("MAIN", "workspace-write"), ("REV-01", "read-only")):
            config = pilot.configuration(role)
            self.assertEqual(config["sandbox_mode"], sandbox)
            self.assertFalse(config["features.multi_agent"])
            self.assertEqual(config["approval_policy"], "never")
            argv = pilot.command(config, self.root / "workspace/solution")
            for i, arg in enumerate(argv):
                if arg == "-c":
                    tomllib.loads(argv[i + 1])


if __name__ == "__main__":
    unittest.main()
