"""Live adapter checks without authentication or model calls."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_v2_2_lean_live as live


class LiveAdapterTests(unittest.TestCase):
    def test_frozen_manifest(self):
        data = live.validate()
        self.assertEqual(data["between_session_token_stop"], 150000)

    def test_transport_captures_exact_output_without_model(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            request = {"config": {}, "cwd": root, "capture": root, "prompt": "synthetic"}
            def fake(argv, prompt, directory, *, cwd):
                self.assertEqual(argv, ["not-a-model"])
                self.assertEqual(prompt, "synthetic")
                directory.mkdir()
                (directory / "stdout.jsonl").write_text('fixture\n')
                return {"exit_code": 7, "duration_seconds": 0}
            with patch.object(live, "command", return_value=["not-a-model"]):
                result = live.transport(request, capture=fake)
            self.assertEqual(result["jsonl"], 'fixture\n')
            self.assertEqual(result["exit_code"], 7)

    def test_permission_false_refused(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "manifest.json"
            data = json.loads(live.MANIFEST.read_text())
            data["launch_authorized"] = False
            path.write_text(json.dumps(data))
            with patch.object(live, "MANIFEST", path), self.assertRaises(PermissionError):
                live.validate()

    def test_hash_tampering_refused(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "manifest.json"
            data = json.loads(live.MANIFEST.read_text())
            data["inputs_sha256"]["scripts/run_v2_2_lean.py"] = "bad-hash"
            path.write_text(json.dumps(data))
            with patch.object(live, "MANIFEST", path), self.assertRaises(ValueError):
                live.validate()


if __name__ == "__main__":
    unittest.main()
