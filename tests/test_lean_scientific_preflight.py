"""Offline preparation only: never call a candidate."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import preflight_lean_scientific as preflight


class ScientificSizeTests(unittest.TestCase):
    def test_full_contract_and_files(self):
        payloads = preflight.payloads(8000)
        for payload in payloads:
            self.assertEqual(payload["challenge"], preflight.SPEC.read_text())
        self.assertIsNone(payloads[0]["first_solution"])
        self.assertEqual(len(payloads[1]["first_solution"]["scientific_calculator.py"]["text"]), 8000)
        self.assertEqual(payloads[1]["first_solution"], payloads[2]["first_solution"])

    def test_caps_and_boundary(self):
        for case in preflight.audit()["cases"]:
            limit = case["max_synthetic_code_characters"]
            if limit is None:
                self.assertFalse(preflight.measure(0, case["cap"])["fits_all_phases"])
                continue
            self.assertTrue(preflight.measure(limit, case["cap"])["fits_all_phases"])
            self.assertFalse(preflight.measure(limit + 1, case["cap"])["fits_all_phases"])

    def test_no_authority_and_no_tokens_claim(self):
        report = preflight.audit()
        self.assertFalse(report["launch_authorized"])
        self.assertEqual(report["model_calls"], 0)
        self.assertIn("not tokens", report["unit"])

    def test_review_evidence_retained(self):
        payload = preflight.payloads(4000)[2]
        self.assertTrue(payload["prior_sessions"][1]["commands"])
        self.assertEqual(len(payload["prior_sessions"][1]["messages"][0].split()), 300)
