"""End-to-end lean preparation with injected synthetic sessions only."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_v2_2_lean as lean


class LeanTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "capture"
        self.calls = []
        self.settings = lean.policy()

    def fake(self, request):
        self.calls.append(request)
        return lean.relay.fake_transport(request)

    def run_fixture(self, callback=None):
        with patch.object(lean, "policy", return_value=self.settings):
            return lean.run(self.root, transport=callback or self.fake)

    def altered(self, change):
        def callback(request):
            response = self.fake(request)
            events = [json.loads(line) for line in response["jsonl"].splitlines()]
            change(events, response, request)
            response["jsonl"] = "\n".join(json.dumps(e) for e in events)
            return response
        return callback

    def test_preparation_defaults(self):
        self.assertEqual(self.settings["between_session_token_stop"], 150000)
        self.assertEqual(self.settings["target_tokens"], 100000)
        self.assertEqual(self.settings["payload_character_cap"], 12000)
        self.assertFalse(self.settings["launch_authorized"])
        self.assertEqual(self.settings["model"], "gpt-6-astra")
        self.assertEqual(self.settings["reasoning_effort"], "medium")

    def test_three_sessions_and_compact_handover_full_capture(self):
        state = self.run_fixture()
        self.assertEqual(state["status"], "simulation_completed")
        self.assertEqual(state["known_tokens"], 39)  # cache and reasoning not added twice
        self.assertIsNone(state["quality_verdict"])
        self.assertEqual(len(self.calls), 3)
        for request in self.calls[1:]:
            payload = json.loads(request["prompt"].split(lean.SEPARATOR)[1])
            self.assertEqual(payload["prior_sessions"][0]["commands"], [])
            self.assertEqual(set(payload["first_solution"]), {"README.md", "calculator.py"})
        final = json.loads(self.calls[2]["prompt"].split(lean.SEPARATOR)[1])
        self.assertTrue(final["prior_sessions"][1]["commands"])
        self.assertIn("SIMULATED output", (self.root / "main_initial/stdout.jsonl").read_text())
        self.assertEqual(self.calls[1]["config"]["sandbox_mode"], "read-only")
        self.assertFalse(self.calls[0]["config"]["features.multi_agent"])

    def test_no_retry_or_overwrite(self):
        self.run_fixture()
        with self.assertRaises(FileExistsError):
            self.run_fixture()
        self.assertEqual(len(self.calls), 3)

    def test_live_refused_before_any_write(self):
        with self.assertRaises(PermissionError):
            lean.run(self.root, simulation=False, transport=self.fake)
        self.assertFalse(self.root.exists())
        self.assertEqual(self.calls, [])

    def test_oversized_payload_never_starts(self):
        self.settings["payload_character_cap"] = 1
        self.assertEqual(self.run_fixture()["status"], "stopped_payload_size")
        self.assertEqual(self.calls, [])

    def test_exact_threshold_and_overshoot(self):
        for stop in (13, 12):
            with self.subTest(stop=stop):
                self.root = self.root.parent / str(stop)
                self.calls = []
                self.settings["between_session_token_stop"] = stop
                state = self.run_fixture()
                self.assertEqual(state["status"], "stopped_token_threshold")
                self.assertEqual(state["overshoot"], 13 - stop)
                self.assertEqual(len(self.calls), 1)

    def test_final_phase_threshold_preserves_completed_status(self):
        self.settings["between_session_token_stop"] = 30
        state = self.run_fixture()
        self.assertEqual(state["status"], "simulation_completed")
        self.assertTrue(state["threshold_reached"])
        self.assertEqual(state["overshoot"], 9)

    def test_failed_process_keeps_available_usage(self):
        def change(events, response, request):
            response["exit_code"] = 7
        state = self.run_fixture(self.altered(change))
        self.assertEqual(state["status"], "stopped_failure")
        self.assertEqual(state["known_tokens"], 13)
        self.assertEqual(len(self.calls), 1)

    def test_missing_usage_stops_not_zero(self):
        def change(events, response, request):
            events[-1]["usage"] = None
        state = self.run_fixture(self.altered(change))
        self.assertEqual(state["status"], "stopped_missing_usage")
        self.assertFalse(state["usage_complete"])
        self.assertIsNone(state["target_met"])
        self.assertEqual(len(self.calls), 1)

    def test_invalid_usage_stops(self):
        def change(events, response, request):
            events[-1]["usage"]["input_tokens"] = True
        self.assertEqual(self.run_fixture(self.altered(change))["status"], "stopped_missing_usage")

    def test_reviewer_write_is_rejected_and_checkpointed(self):
        def change(events, response, request):
            if request["phase"] == "review":
                (request["cwd"] / "calculator.py").write_text("forbidden")
        with self.assertRaises(PermissionError):
            self.run_fixture(self.altered(change))
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(json.loads((self.root / "state.json").read_text())["status"], "interrupted")

    def test_protected_contract_write_is_rejected(self):
        def change(events, response, request):
            (request["cwd"].parent / "CHALLENGE.md").write_text("forbidden")
        with self.assertRaises(PermissionError):
            self.run_fixture(self.altered(change))
        self.assertEqual(len(self.calls), 1)

    def test_reused_thread_is_rejected(self):
        def change(events, response, request):
            events[0]["thread_id"] = "same"
        with self.assertRaises(ValueError):
            self.run_fixture(self.altered(change))
        self.assertEqual(len(self.calls), 2)

    def test_truncated_output_is_rejected(self):
        def change(events, response, request):
            events[2]["item"]["truncated"] = True
        with self.assertRaises(ValueError):
            self.run_fixture(self.altered(change))
        self.assertEqual(len(self.calls), 1)

    def test_word_limit_recorded_not_truncated(self):
        def change(events, response, request):
            events[3]["item"]["text"] = "word " * 301
        state = self.run_fixture(self.altered(change))
        self.assertEqual(len(state["deviations"]), 3)
        self.assertEqual(state["sessions"][0]["final_words"], 301)

    def test_policy_cannot_enable_live(self):
        manifest = self.root.parent / "policy.json"
        self.settings["launch_authorized"] = True
        manifest.write_text(json.dumps(self.settings))
        with patch.object(lean, "MANIFEST", manifest), self.assertRaises(PermissionError):
            lean.run(self.root)
        self.assertFalse(self.root.exists())

    def test_150000_boundary_prevents_third_session(self):
        def change(events, response, request):
            events[-1]["usage"].update(input_tokens=74000, output_tokens=1000)
        state = self.run_fixture(self.altered(change))
        self.assertEqual(state["known_tokens"], 150000)
        self.assertEqual(state["status"], "stopped_token_threshold")
        self.assertEqual(len(self.calls), 2)

    def test_historical_counts_as_fixture_finish_but_miss_target(self):
        counts = {"main_initial": (49294, 2255), "review": (13893, 596),
                  "main_final": (47324, 412)}
        def change(events, response, request):
            entry, output = counts[request["phase"]]
            events[-1]["usage"].update(input_tokens=entry, output_tokens=output)
        state = self.run_fixture(self.altered(change))
        self.assertEqual(state["known_tokens"], 113774)
        self.assertEqual(state["status"], "simulation_completed")
        self.assertFalse(state["target_met"])


if __name__ == "__main__":
    unittest.main()
