"""Pure catalogue checks: no CLI, networking, model or credentials."""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from preflight_v2_2_bridge import allowed_catalog, tool_names


class CatalogTests(unittest.TestCase):
    def test_legacy_location(self):
        self.assertEqual(tool_names({"tools": [{"name": "shell", "type": "function"}]}), ["shell"])

    def test_additional_tools_namespaces(self):
        payload = {"input": [{"type": "message"}, {"type": "additional_tools", "tools": [
            {"type": "namespace", "name": "collaboration", "tools": [{"type": "function", "name": "spawn_agent"}]}]}]}
        self.assertEqual(tool_names(payload), ["collaboration.spawn_agent"])

    def test_both_locations_must_be_checked(self):
        payload = {"tools": [{"name": "mcp__agentbench__confined_command"}],
                   "input": [{"type": "additional_tools", "tools": [{"name": "shell"}]}]}
        self.assertFalse(allowed_catalog([tool_names(payload)]))

    def test_empty_duplicate_and_multiple_requests_fail(self):
        approved = ["mcp__agentbench__confined_command"]
        for observed in ([], [[]], [approved + approved], [approved, approved]):
            self.assertFalse(allowed_catalog(observed))
        self.assertTrue(allowed_catalog([approved]))

    def test_unknown_tool_fails_closed(self):
        self.assertFalse(allowed_catalog([tool_names({"tools": [{"type": "new_tool_type"}]})]))


if __name__ == "__main__":
    unittest.main()
