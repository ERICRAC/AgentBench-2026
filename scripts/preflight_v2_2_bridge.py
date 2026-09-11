#!/usr/bin/env python3
"""Exercise real MCP stdio and inspect CLI tool advertisement on a local stub.

No account, credentials or real model provider is used. The local HTTP stub
always rejects inference. It records tool names only, never headers/prompts.
"""

import json
from pathlib import Path
import subprocess
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from v2_2_transport import local_cli

ROOT = Path(__file__).resolve().parents[1]


def check():
    with tempfile.TemporaryDirectory(prefix="agentbench-bridge-") as directory:
        root = Path(directory)
        workspace = root / "workspace"
        (workspace / "solution").mkdir(parents=True)
        (workspace / "CHALLENGE.md").write_text("Synthetic contract, not a benchmark")
        checks = {}
        for role in ("MAIN", "REV-01"):
            requests = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26"}},
                        {"jsonrpc": "2.0", "method": "notifications/initialized"},
                        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
                        {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "confined_command", "arguments": {"command": "printf bridge-output; printf bridge-error >&2"}}},
                        {"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "confined_command", "arguments": {"command": "printf fixture > bridge.txt"}}}]
            result = subprocess.run(["/usr/bin/python3", "-B", str(ROOT / "scripts/v2_2_tool_bridge.py"), "--role", role,
                                     "--workspace", str(workspace), "--capture", str(root / ("capture-" + role))],
                                    input="\n".join(json.dumps(r) for r in requests) + "\n", text=True,
                                    capture_output=True, timeout=30, check=True)
            responses = [json.loads(line) for line in result.stdout.splitlines()]
            checks[role + ".handshake_and_list"] = len(responses) == 4 and responses[1]["result"]["tools"][0]["name"] == "confined_command"
            output = json.loads(responses[2]["result"]["content"][0]["text"])
            checks[role + ".complete_streams"] = output == {"exit_code": 0, "stdout": "bridge-output", "stderr": "bridge-error"}
            write = json.loads(responses[3]["result"]["content"][0]["text"])
            checks[role + ".write_policy"] = (write["exit_code"] == 0) == (role == "MAIN")

        observed = []
        envelopes = []

        class Stub(BaseHTTPRequestHandler):
            def do_POST(self):
                payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                envelopes.append({"path": self.path, "keys": sorted(payload), "model": payload.get("model"), "tool_choice": payload.get("tool_choice"), "metadata_keys": list(payload.get("client_metadata", {})), "input_types": [x.get("type") for x in payload.get("input", [])]})
                # Retain ONLY the advertised tool names/types.
                advertised = list(payload.get("tools", []))
                for item in payload.get("input", []):
                    if item.get("type") == "additional_tools":
                        advertised.extend(item.get("tools", []))
                def names(items, prefix=""):
                    result = []
                    for item in items:
                        name = prefix + item.get("name", item.get("type", "unknown"))
                        if item.get("type") == "namespace":
                            result.extend(names(item.get("tools", []), name + "."))
                        else:
                            result.append(name)
                    return result
                observed.append(names(advertised))
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error":{"message":"LOCAL PREFLIGHT STOP: no inference","type":"invalid_request_error"}}')

            def log_message(self, *args):
                pass

        server = HTTPServer(("127.0.0.1", 0), Stub)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        cli_home = root / "cli-home"
        cli_home.mkdir()
        # Empty, disposable home; no inherited API key, token or auth file.
        env = {"PATH": "/usr/bin:/bin", "HOME": str(cli_home), "CODEX_HOME": str(cli_home), "LANG": "C.UTF-8"}
        config = {
            "model": '"gpt-6-astra"', "model_reasoning_effort": '"medium"',
            "model_provider": '"local-preflight"', "approval_policy": '"never"',
            "sandbox_mode": '"read-only"', "web_search": '"disabled"',
            "model_providers.local-preflight": '{name="Local preflight", base_url="http://127.0.0.1:' + str(server.server_port) + '", wire_api="responses", requires_openai_auth=false, request_max_retries=0, stream_max_retries=0}',
            "mcp_servers.agentbench": '{enabled=true, required=true, command="/usr/bin/python3", args=' + json.dumps(["-B", str(ROOT / "scripts/v2_2_tool_bridge.py"), "--role", "REV-01", "--workspace", str(workspace), "--capture", str(root / "cli-capture")]) + '}',
        }
        disabled = ("shell_tool", "unified_exec", "multi_agent", "apps", "plugins", "hooks", "browser_use",
                    "computer_use", "image_generation", "view_image", "memories", "shell_snapshot", "skill_search", "code_mode", "code_mode_host")
        for feature in disabled:
            config["features." + feature] = "false"
        argv = [str(local_cli()), "exec", "--strict-config", "--ignore-user-config", "--ignore-rules",
                "--ephemeral", "--json", "--skip-git-repo-check", "-C", str(workspace / "solution")]
        for key, value in config.items():
            argv += ["-c", key + "=" + value]
        try:
            result = subprocess.run(argv + ["-"], input="Local infrastructure probe. Do not execute tools.",
                                    text=True, capture_output=True, env=env, timeout=40)
        finally:
            server.shutdown()
            server.server_close()
            worker.join()
        checks["local_stub_reached"] = len(observed) == 1
        checks["candidate_tool_allowlist"] = observed == [["mcp__agentbench__confined_command"]]
        return {"kind": "stdio_bridge_and_local_cli_catalog", "model_calls": 0,
                "status": "passed" if all(checks.values()) else "blocked_tool_catalog",
                "real_authentication_checked": False, "checks": checks,
                "advertised_tools": observed, "cli_exit_code": result.returncode,
                "request_envelopes": envelopes,
                "cli_configuration_accepted": bool(observed),
                "bridge_started_by_cli": (root / "cli-capture").exists(),
                "negotiation": json.loads((root / "cli-capture/negotiation.json").read_text()) if (root / "cli-capture/negotiation.json").exists() else None,
                "mcp_methods": [json.loads(line) for line in (root / "cli-capture/methods.jsonl").read_text().splitlines()] if (root / "cli-capture/methods.jsonl").exists() else [],
                "live_authorized": False, "protocol_frozen": False}


if __name__ == "__main__":
    report = check()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["status"] == "passed" else 1)
