#!/usr/bin/env python3
"""MCP stdio bridge to the confined command runner; never handles credentials.

The orchestrator fixes workspace, role and private capture directory. Tool
arguments cannot change any of them. This prototype does not authorise a model
launch and does not prove that a Codex client exposes no other tools.
"""

import argparse
import json
from pathlib import Path
import sys

from v2_2_transport import capture_process, isolated_command

TOOL = {"name": "confined_command", "description": "Run a shell command in the role's isolated solution directory. Full stdout/stderr and exit code are returned. No network or host credentials.",
        "inputSchema": {"type": "object", "properties": {"command": {"type": "string", "minLength": 1}},
                        "required": ["command"], "additionalProperties": False}}


class Bridge:
    def __init__(self, role, workspace, capture):
        # Reuse the sandbox builder's validation before accepting requests.
        isolated_command(role, workspace, ["/usr/bin/true"])
        self.workspace = workspace.resolve(strict=True)
        if capture.is_symlink():
            raise ValueError("Capture must not be a link")
        self.capture = capture.resolve()
        if self.capture.is_relative_to(self.workspace) or self.workspace.is_relative_to(self.capture):
            raise ValueError("Capture and workspace must be separate")
        self.capture.mkdir(mode=0o700)
        self.role = role
        self.sequence = 0
        self.initialized = False

    def handle(self, request):
        if not isinstance(request, dict) or request.get("jsonrpc") != "2.0":
            return self.error(None, -32600, "Invalid request")
        ident = request.get("id")
        with (self.capture / "methods.jsonl").open("a", encoding="utf-8") as trace:
            trace.write(json.dumps({"method": request.get("method")}) + "\n")
        if "id" not in request:
            return None  # MCP notifications do not trigger commands.
        method = request.get("method")
        params = request.get("params", {})
        if not isinstance(params, dict):
            return self.error(ident, -32602, "Invalid params")
        if method == "initialize":
            if self.initialized:
                return self.error(ident, -32600, "Already initialized")
            version = params.get("protocolVersion")
            (self.capture / "negotiation.json").write_text(json.dumps({"requested_version": version}), encoding="utf-8")
            if version not in {"2024-11-05", "2025-03-26", "2025-06-18"}:
                return self.error(ident, -32602, "Unsupported protocol version")
            self.initialized = True
            result = {"protocolVersion": version, "capabilities": {"tools": {}},
                      "serverInfo": {"name": "agentbench-confined-tools", "version": "0.1.0"}}
        elif not self.initialized:
            return self.error(ident, -32002, "Initialize first")
        elif method == "ping":
            result = {}
        elif method == "tools/list":
            result = {"tools": [TOOL]}
        elif method == "tools/call":
            arguments = params.get("arguments")
            if (params.get("name") != TOOL["name"] or not isinstance(arguments, dict)
                    or set(arguments) != {"command"} or not isinstance(arguments["command"], str)
                    or not arguments["command"].strip() or "\x00" in arguments["command"]):
                return self.error(ident, -32602, "Only a nonempty command is allowed")
            self.sequence += 1
            directory = self.capture / f"command-{self.sequence:04d}"
            argv = isolated_command(self.role, self.workspace,
                                    ["/bin/bash", "--noprofile", "--norc", "-c", arguments["command"]])
            state = capture_process(argv, "", directory, cwd=self.workspace / "solution")
            output = {"exit_code": state["exit_code"],
                      "stdout": (directory / "stdout.jsonl").read_text(encoding="utf-8"),
                      "stderr": (directory / "stderr.txt").read_text(encoding="utf-8")}
            result = {"content": [{"type": "text", "text": json.dumps(output, ensure_ascii=False)}],
                      "isError": state["exit_code"] != 0}
        else:
            return self.error(ident, -32601, "Unknown method")
        return {"jsonrpc": "2.0", "id": ident, "result": result}

    @staticmethod
    def error(ident, code, message):
        return {"jsonrpc": "2.0", "id": ident, "error": {"code": code, "message": message}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=("MAIN", "REV-01"), required=True)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--capture", type=Path, required=True)
    args = parser.parse_args()
    bridge = Bridge(args.role, args.workspace, args.capture)
    for line in sys.stdin:
        try:
            request = json.loads(line)
        except json.JSONDecodeError:
            response = bridge.error(None, -32700, "Invalid JSON")
        else:
            # Infrastructure/encoding errors terminate instead of silently retrying
            # or replacing evidence. The private process checkpoint is retained.
            response = bridge.handle(request)
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
