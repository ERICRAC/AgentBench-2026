"""Scientific live wiring, exclusively fake processes and temporary fixtures."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_v2_2_lean_scientific_live_002 as live


class ScientificLive002Tests(unittest.TestCase):
    def test_frozen_complete_inputs(self):
        data = live.validate()
        self.assertFalse(data["launch_authorized"])
        self.assertEqual(data["payload_character_cap"], 24000)

    def test_approval_missing_before_writes_or_capture(self):
        with tempfile.TemporaryDirectory() as d, patch.object(live, "transport") as transport:
            root = Path(d) / "capture"
            for approval in (None, "wrong-run"):
                with self.assertRaises(PermissionError):
                    live.launch(root, approve_run=approval)
            self.assertFalse(root.exists())
            transport.assert_not_called()

    def test_exact_capture(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            request = {"config": {}, "cwd": root, "capture": root, "prompt": "fixture"}
            def fake(argv, prompt, directory, *, cwd):
                self.assertEqual(argv, ["synthetic"])
                self.assertEqual(prompt, "fixture")
                self.assertEqual(cwd, root)
                directory.mkdir()
                (directory / "stdout.jsonl").write_text("exact fixture\n")
                return {"exit_code": 7}
            with patch.object(live, "command", return_value=["synthetic"]):
                self.assertEqual(live.transport(request, capture=fake)["jsonl"], "exact fixture\n")

    def test_hash_and_missing_input_rejected(self):
        original = live.validate()
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "manifest.json"
            for mutation in ("missing", "changed"):
                data = json.loads(json.dumps(original))
                key = live.INPUTS[0]
                if mutation == "missing":
                    del data["inputs_sha256"][key]
                else:
                    data["inputs_sha256"][key] = "wrong"
                path.write_text(json.dumps(data))
                with patch.object(live, "MANIFEST", path), self.assertRaises(ValueError):
                    live.validate()

    def test_changed_condition_rejected(self):
        data = live.validate()
        data["payload_character_cap"] = 24001
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "manifest.json"
            path.write_text(json.dumps(data))
            with patch.object(live, "MANIFEST", path), self.assertRaises(PermissionError):
                live.validate()

    def test_whole_launch_wiring_fake_capture_and_one_shot(self):
        data = live.validate()
        original_root = live.lean.relay.ROOT
        calls = []
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d) / "repo"
            (repo / "runs").mkdir(parents=True)
            for name in live.INPUTS:
                destination = repo / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(original_root / name, destination)
            def fake_capture(argv, prompt, directory, *, cwd):
                phase = directory.parent.name
                calls.append(phase)
                label = {"main_initial": "MAIN initial", "review": "REV-01", "main_final": "MAIN final"}[phase]
                self.assertIn("autorise maintenant la phase " + label + ".", prompt)
                self.assertIn(live.RUN_ID, prompt)
                self.assertIn("Commence le travail demandé", prompt)
                self.assertNotIn("Lors d'un lancement explicitement autorisé", prompt)
                self.assertNotIn("le gel seul n'autorise aucun lancement", prompt)
                self.assertEqual((directory.parent / "prompt.txt").read_text(), prompt)
                response = live.lean.relay.fake_transport({"phase": phase, "cwd": cwd,
                                                          "challenge": "scientific-calculator"})
                directory.mkdir()
                (directory / "stdout.jsonl").write_text(response["jsonl"])
                return {"exit_code": 0, "duration_seconds": 0}
            real_adapter = live.transport
            def fake_adapter(request):
                return real_adapter(request, capture=fake_capture)
            with patch.object(live.lean.relay, "ROOT", repo), \
                    patch.object(live, "validate", return_value=data), \
                    patch.object(live, "command", return_value=["synthetic-only"]), \
                    patch.object(live, "transport", side_effect=fake_adapter):
                result = live.launch(Path(d) / "capture", approve_run=live.RUN_ID)
                self.assertEqual(result["status"], "candidate_sessions_completed_pending_independent_verification")
                self.assertEqual(result["known_tokens"], 39)  # Synthetic, never a model measurement.
                self.assertIsNone(result["quality_verdict"])
                with self.assertRaises(FileExistsError):
                    live.launch(Path(d) / "second", approve_run=live.RUN_ID)
            self.assertEqual(calls, ["main_initial", "review", "main_final"])
            self.assertTrue((repo / "runs" / live.RUN_ID / "CHALLENGE.md").exists())
