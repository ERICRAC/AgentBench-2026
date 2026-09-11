"""Bridge request contract tests, without a model or real sandbox invocation."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from v2_2_tool_bridge import Bridge


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.workspace = self.root / "workspace"
        (self.workspace / "solution").mkdir(parents=True)
        self.bridge = Bridge("REV-01", self.workspace, self.root / "capture")

    def call(self, method, params=None):
        return self.bridge.handle({"jsonrpc": "2.0", "id": 1, "method": method, "params": params or {}})

    def initialize(self):
        return self.call("initialize", {"protocolVersion": "2025-03-26"})

    def test_initialization_required_and_only_one_tool(self):
        self.assertIn("error", self.call("tools/list"))
        self.assertIn("result", self.initialize())
        self.assertEqual([x["name"] for x in self.call("tools/list")["result"]["tools"]], ["confined_command"])

    def test_no_role_path_or_permission_override(self):
        self.initialize()
        with patch("v2_2_tool_bridge.capture_process", side_effect=AssertionError("Must not execute")):
            for key in ("role", "cwd", "workspace", "capture", "sandbox_permissions", "env"):
                self.assertIn("error", self.call("tools/call", {"name": "confined_command", "arguments": {"command": "true", key: "override"}}))

    def test_unknown_tool_empty_and_invalid_commands(self):
        self.initialize()
        for command in ("", " ", None, 1, "a\x00b"):
            self.assertIn("error", self.call("tools/call", {"name": "confined_command", "arguments": {"command": command}}))
        self.assertIn("error", self.call("tools/call", {"name": "shell", "arguments": {"command": "true"}}))

    def test_capture_separation_and_reuse(self):
        with self.assertRaises(ValueError):
            Bridge("MAIN", self.workspace, self.workspace / "private")
        with self.assertRaises(FileExistsError):
            Bridge("MAIN", self.workspace, self.root / "capture")

    def test_notifications_cannot_execute(self):
        self.initialize()
        self.assertIsNone(self.bridge.handle({"jsonrpc": "2.0", "method": "tools/call", "params": {"name": "confined_command", "arguments": {"command": "true"}}}))

    def test_protocol_and_malformed_requests(self):
        self.assertIn("error", self.call("initialize", {"protocolVersion": "unknown"}))
        self.assertIn("error", self.bridge.handle([]))
        self.initialize()
        self.assertIn("error", self.initialize())
        self.assertIn("error", self.call("unknown"))


if __name__ == "__main__":
    unittest.main()
