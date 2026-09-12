"""Fake responses are fixed and evidence interpretation is fail-closed."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import v2_2_dispatch_fixtures as fixtures
from preflight_v2_2_bridge import check


class DispatchTests(unittest.TestCase):
    def test_sse_call_and_completion_match(self):
        for name in fixtures.FIXTURES:
            events = [json.loads(line[6:]) for line in fixtures.stream(name).decode().splitlines() if line.startswith("data: ")]
            self.assertEqual(events[2]["item"], fixtures.call_item(name))
            self.assertEqual(events[3]["response"]["output"], [fixtures.call_item(name)])
            self.assertNotEqual(fixtures.call_item(name)["name"], "spawn_agent")

    def test_arbitrary_fixture_and_approval_expansion_refused(self):
        for args in ((None, "arbitrary"), (None, None, True), (None, "inventory", True, True)):
            with self.assertRaises(ValueError):
                check(*args)

    def test_capture_only_known_call_output(self):
        payload = {"input": [{"type": "message", "output": "private surrounding input"},
                             {"type": "custom_tool_call_output", "call_id": "other", "output": "other"},
                             {"type": "custom_tool_call_output", "call_id": "agentbench-dispatch-probe", "output": "fixture"}]}
        self.assertEqual(fixtures.outputs(payload), ["fixture"])

    def test_missing_or_duplicate_output_not_success(self):
        for output in ([], ["a", "a"], [None], ["unexpected"]):
            self.assertTrue(fixtures.assess("bridge_echo", output)["outcome"].startswith("unverified"))

    def test_echo_requires_exact_result_not_marker_alone(self):
        self.assertEqual(fixtures.assess("bridge_echo", ["AGENTBENCH_BRIDGE_DISPATCH"])["outcome"], "unverified_response")
        output = json.dumps({"exit_code": 0, "stdout": "AGENTBENCH_BRIDGE_DISPATCH", "stderr": ""})
        self.assertEqual(fixtures.assess("bridge_echo", [output])["outcome"], "confined_echo_executed")

    def test_distinguish_refusal_inventory_and_collaboration(self):
        self.assertEqual(fixtures.assess("inventory", ["code-mode host is disabled"])["outcome"], "host_disabled_refusal")
        self.assertEqual(fixtures.assess("inventory", ['["apply_patch"]'])["tool_names"], ["apply_patch"])
        self.assertEqual(fixtures.assess("collaboration_list", ['{"agents":[]}'])["outcome"], "collaboration_list_executed")


if __name__ == "__main__":
    unittest.main()
