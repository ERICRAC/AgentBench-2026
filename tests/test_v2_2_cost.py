"""Offline-only cost audit: no subprocess, model, network or historical writes."""
import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_v2_2_cost import audit, compact_payload, simulate_fake_candidates


class CostDraftTests(unittest.TestCase):
    def setUp(self):
        self.payloads = [{"challenge": "synthetic"}] * 3
        self.replies = [{"exit_code": 0, "usage": {"input_tokens": 10, "output_tokens": 2}} for _ in range(3)]

    def simulate(self, **kwargs):
        return simulate_fake_candidates(self.payloads, self.replies,
                                        **({"character_cap": 1000, "token_stop": 100} | kwargs))

    def test_three_fake_phases(self):
        result = self.simulate()
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["observed_fake_tokens"], 36)
        self.assertEqual(len(result["completed_phases"]), 3)

    def test_size_stops_before_first_candidate_without_truncation(self):
        before = copy.deepcopy(self.payloads)
        result = self.simulate(character_cap=1)
        self.assertEqual(result["status"], "stopped_payload_size")
        self.assertEqual(result["completed_phases"], [])
        self.assertEqual(before, self.payloads)

    def test_budget_boundary_stops_without_retry(self):
        result = self.simulate(token_stop=12)
        self.assertEqual(result["status"], "stopped_token_threshold")
        self.assertEqual(result["completed_phases"], ["main_initial"])
        self.assertEqual(result["overshoot"], 0)

    def test_budget_overshoot_is_visible_not_prevented(self):
        result = self.simulate(token_stop=5)
        self.assertEqual(result["overshoot"], 7)
        self.assertEqual(len(result["completed_phases"]), 1)

    def test_missing_usage_stops(self):
        self.replies[0]["usage"] = {}
        self.assertEqual(self.simulate()["status"], "stopped_missing_usage")

    def test_failure_stops(self):
        self.replies[0]["exit_code"] = 1
        self.assertEqual(self.simulate()["status"], "stopped_failure")

    def test_live_forbidden(self):
        with self.assertRaises(PermissionError):
            self.simulate(live=True)

    def test_invalid_limits(self):
        for limit in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                self.simulate(token_stop=limit)

    def test_keep_contract_files_review_and_final_handover(self):
        payload = {"challenge": "contract", "first_solution": {"file": "entire file"},
                   "prior_sessions": [
                       {"phase": "main_initial", "role": "MAIN", "messages": ["progress", "final"], "commands": ["long log"]},
                       {"phase": "review", "role": "REV-01", "messages": ["review"], "commands": ["reproduction"]}]}
        before = copy.deepcopy(payload)
        compact = compact_payload(payload)
        self.assertEqual(payload, before)
        self.assertEqual(compact["challenge"], "contract")
        self.assertEqual(compact["first_solution"], payload["first_solution"])
        self.assertEqual(compact["prior_sessions"][0]["messages"], ["final"])
        self.assertEqual(compact["prior_sessions"][0]["commands"], [])
        self.assertEqual(compact["prior_sessions"][1], payload["prior_sessions"][1])

    def test_audit_is_character_accounting_not_token_estimation(self):
        data = audit()
        self.assertEqual(len(data["phases"]), 3)
        self.assertEqual(sum(r["input_tokens"] for r in data["phases"]), 110511)
        for row in data["phases"]:
            self.assertEqual(row["removed_payload_characters"],
                             row["payload_characters"] - row["proposed_payload_characters"])


if __name__ == "__main__":
    unittest.main()
