#!/usr/bin/env python3
"""Real local command-sandbox probes with disposable canaries; zero model calls."""

import argparse
import json
from pathlib import Path
import subprocess
import socket
import tempfile

from v2_2_transport import capture_process, isolated_command, local_cli, permissions
import run_v2_2 as relay


def exercise_relay(root):
    """Six actual isolated processes, synthetic replies, no calculator scores."""
    summaries = []
    for challenge in relay.DELIVERABLES:
        workspace = root / challenge
        (workspace / "solution").mkdir(parents=True)
        (workspace / "CHALLENGE.md").write_text((relay.ROOT / "challenges" / challenge / "SPEC.md").read_text())

        def fixture(request):
            phase = request["phase"]
            events = [{"type": "thread.started", "thread_id": "process-fixture-" + phase},
                      {"type": "turn.started"},
                      {"type": "item.completed", "item": {"type": "agent_message", "text": "Synthetic process fixture only"}},
                      {"type": "turn.completed"}]
            code = "import sys, pathlib\nassert sys.stdin.read()\n"
            if request["role"] == "MAIN":
                for name in sorted(relay.DELIVERABLES[challenge]):
                    code += f"pathlib.Path({name!r}).write_text('SIMULATION ONLY')\n"
            code += "print(" + repr("\n".join(json.dumps(e) for e in events)) + ")\n"
            capture = root / (challenge + "-" + phase)
            argv = isolated_command(request["role"], workspace, ["/usr/bin/python3", "-B", "-c", code])
            state = capture_process(argv, request["prompt"], capture, cwd=request["cwd"], timeout=30)
            return {"exit_code": state["exit_code"], "jsonl": (capture / "stdout.jsonl").read_text()}

        state = relay.run_relay(workspace, root / (challenge + "-relay"), challenge, fixture, simulation=True)
        summaries.append({"challenge": challenge, "status": state["status"],
                          "processes": len(state["sessions"]), "model_calls": 0,
                          "official_verdict": None, "usage": None})
    return summaries


def check(backend="native") -> dict:
    cli = local_cli()
    checks = {}
    observations = {}
    simulations = []
    # Match the real home-backed run location: denied /tmp cannot host read roots.
    with tempfile.TemporaryDirectory(prefix=".agentbench-os-probe-", dir=Path(__file__).resolve().parents[1]) as folder:
        root = Path(folder)
        workspace = root / "workspace"
        solution = workspace / "solution"
        solution.mkdir(parents=True)
        protected = workspace / "CHALLENGE.md"
        protected.write_text("synthetic contract")
        outside = root / "outside.txt"
        outside.write_text("synthetic private canary")
        (solution / "existing.txt").write_text("existing")
        (solution / "escape").symlink_to(outside)
        # Unsandboxed control establishes that host permissions allow access.
        checks["host_can_read_write_canary"] = outside.read_text() == "synthetic private canary"
        outside.write_text("synthetic private canary")
        server = socket.socket()
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        port = server.getsockname()[1]
        with socket.create_connection(("127.0.0.1", port), timeout=1):
            checks["host_loopback_access"] = True
        for role in ("MAIN", "REV-01"):
            # This script handles only generated canaries, never user files.
            script = '''import json, pathlib, socket
def allowed(action):
    try:
        action()
        return True
    except OSError:
        return False
w = pathlib.Path(WORKSPACE)
s = w / "solution"
o = pathlib.Path(OUTSIDE)
r = {
 "contract_read": allowed(lambda: (w / "CHALLENGE.md").read_text()),
 "solution_read": allowed(lambda: (s / "existing.txt").read_text()),
 "outside_read": allowed(o.read_text),
 "symlink_escape_read": allowed(lambda: (s / "escape").read_text()),
 "outside_write": allowed(lambda: o.write_text("changed")),
 "symlink_escape_write": allowed(lambda: (s / "escape").write_text("changed")),
 "contract_write": allowed(lambda: (w / "CHALLENGE.md").write_text("changed")),
 "solution_create": allowed(lambda: (s / "created.txt").write_text("created")),
 "solution_overwrite": allowed(lambda: (s / "existing.txt").write_text("new")),
 "solution_rename": allowed(lambda: (s / "rename.txt").rename(s / "renamed.txt")),
 "solution_delete": allowed(lambda: (s / "delete.txt").unlink()),
 "host_network_connect": allowed(lambda: socket.create_connection(("127.0.0.1", PORT), timeout=0.2)),
}
print(json.dumps(r))
'''.replace("WORKSPACE", repr(str(workspace))).replace("OUTSIDE", repr(str(outside))).replace("PORT", str(port))
            for name in ("rename.txt", "delete.txt"):
                (solution / name).write_text("fixture")
            payload = ["/usr/bin/python3", "-B", "-c", script]
            argv = ([str(cli), "sandbox", *permissions(role, workspace, cli), "--", *payload]
                    if backend == "native" else isolated_command(role, workspace, payload))
            capture = root / ("capture-" + role)
            state = capture_process(argv, "", capture, cwd=solution, timeout=30)
            if state["exit_code"] != 0:
                raise RuntimeError((capture / "stderr.txt").read_text())
            observed = json.loads((capture / "stdout.jsonl").read_text())
            observations[role] = observed
            expected = {key: (key in {"contract_read", "solution_read"} or
                        (role == "MAIN" and key.startswith("solution_") and key != "solution_read"))
                        for key in observed}
            for key, value in observed.items():
                checks[f"{role}.{key}"] = value == expected[key]
            checks[f"{role}.private_canary_intact"] = outside.read_text() == "synthetic private canary"
            checks[f"{role}.contract_intact"] = protected.read_text() == "synthetic contract"
        server.close()
        if backend == "bwrap" and all(checks.values()):
            simulations = exercise_relay(root)
    return {"kind": backend + "_command_sandbox_canaries", "model_calls": 0,
            "status": "passed" if all(checks.values()) else "failed",
            "checks": checks, "allowed_operations": observations,
            "process_simulations": simulations,
            "cli_version": subprocess.check_output([str(cli), "--version"], text=True).strip(),
            "scope": "Local command tool sandbox only; not a live model session or every tool surface",
            "live_authorized": False, "protocol_frozen": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("native", "bwrap"), default="native")
    args = parser.parse_args()
    result = check(args.backend)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "passed" else 1)
