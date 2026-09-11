#!/usr/bin/env python3
"""Draft lean-pair relay. Simulations only until freeze and isolation approval.

No model client is invoked here. The same three-phase engine accepts an injected
session transport for tests. Captures are private, never publication-ready.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import stat
import time
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PHASES = (
    ("main_initial", "MAIN", "v2-2-developer-initial.md", 600),
    ("review", "REV-01", "v2-2-reviewer.md", 1200),
    ("main_final", "MAIN", "v2-2-developer-final.md", 1200),
)
DELIVERABLES = {
    "calculator": {"calculator.py", "README.md"},
    "scientific-calculator": {"scientific_calculator.py", "README.md"},
}
SETTINGS = {
    "model": "gpt-6-astra", "model_reasoning_effort": "medium",
    "model_context_window": 200000, "model_auto_compact_token_limit": 180000,
    "model_auto_compact_token_limit_scope": "total",
    "approval_policy": "never", "web_search": "disabled",
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save(path: Path, data: object) -> None:
    """Atomic private checkpoint. Existing checkpoints belong to this relay."""
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(path)


def snapshot(directory: Path) -> dict:
    """Capture every regular UTF-8 file, rejecting links/special files.

    Never silently skip caches or binary files: missing evidence is a stop, not
    a reason to invent a lossy handover. This is an audit, not an OS sandbox.
    """
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError("Snapshot root must be a real directory")
    files = {}
    for path in sorted(directory.rglob("*")):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode) or not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
            raise ValueError("Link or special file in snapshot")
        if stat.S_ISREG(mode):
            raw = path.read_bytes()
            if path.stat().st_nlink != 1:
                raise ValueError("Hard-linked file in snapshot")
            files[path.relative_to(directory).as_posix()] = {
                "sha256": digest(raw), "bytes": len(raw),
                "text": raw.decode("utf-8"),
            }
    return files


def config_for(role: str) -> dict:
    if role not in {"MAIN", "REV-01"}:
        raise ValueError("Unknown role")
    path = ROOT / "governance/v2-2-draft" / f"config-{role.lower()}.toml"
    config = tomllib.loads(path.read_text(encoding="utf-8"))
    expected = {**SETTINGS, "sandbox_mode": "read-only" if role == "REV-01" else "workspace-write"}
    if set(config) != set(expected) | {"developer_instructions"}:
        raise ValueError("Unexpected configuration key")
    if any(type(config[k]) is not type(v) or config[k] != v for k, v in expected.items()):
        raise ValueError("Configuration differs from draft")
    if not isinstance(config["developer_instructions"], str) or not config["developer_instructions"]:
        raise ValueError("Missing role instructions")
    return config


def codex_command(config: dict, cwd: Path) -> list[str]:
    """Build argv for inspection only; this module never executes it.

    Local CLI help supports these flags. A future live adapter still needs an
    approved manifest, real isolation checks and an explicit launch decision.
    """
    command = ["codex", "exec", "--strict-config", "--ignore-user-config",
               "--ignore-rules", "--ephemeral", "--json", "--skip-git-repo-check",
               "-C", str(cwd)]
    for key, value in config.items():
        command.extend(["-c", f"{key}={json.dumps(value)}"])
    return command + ["-"]


def parse_events(raw: str) -> dict:
    """Fail closed on incomplete JSONL; retain all observable command outputs.

    Usage may be absent: it remains None. Missing replies/completion, duplicate
    threads/turns and unknown item types are not silently discarded. Reasoning
    items are deliberately excluded from handovers, never reconstructed.
    """
    events = [json.loads(line) for line in raw.splitlines() if line.strip()]
    if (not events or any(not isinstance(e, dict) for e in events)
            or events[0].get("type") != "thread.started"
            or events[-1].get("type") != "turn.completed"
            or sum(e.get("type") == "turn.started" for e in events) != 1):
        raise ValueError("Invalid event envelope/order")
    threads, completed, messages, commands, changes, errors = [], [], [], [], [], []
    pending = set()
    for event in events:
        kind = event.get("type")
        if kind == "thread.started":
            threads.append(event.get("thread_id"))
        elif kind == "turn.completed":
            completed.append(event)
        elif kind in {"error", "turn.failed"}:
            errors.append(event)
        elif kind == "item.started":
            pending.add(event["item"]["id"])
        elif kind == "item.completed":
            item = event["item"]
            pending.discard(item.get("id"))
            item_type = item.get("type")
            if item_type == "agent_message":
                if not isinstance(item.get("text"), str):
                    raise ValueError("Missing visible text")
                messages.append(item["text"])
            elif item_type == "command_execution":
                if not isinstance(item.get("command"), str) or not isinstance(item.get("aggregated_output"), str):
                    raise ValueError("Missing command/output")
                if (type(item.get("exit_code")) is not int or item.get("truncated", False)
                        or "Warning: truncated output" in item["aggregated_output"]):
                    raise ValueError("Incomplete command output")
                commands.append({k: item[k] for k in ("command", "aggregated_output", "exit_code")})
            elif item_type == "file_change":
                changes.append(item)
            elif item_type != "reasoning":
                raise ValueError("Unrecognised item type; adapter review required")
        elif kind not in {"turn.started", "item.updated"}:
            raise ValueError("Unrecognised event type")
    if errors or pending or len(threads) != 1 or not isinstance(threads[0], str) or not threads[0]:
        raise ValueError("Failed or incomplete session")
    if len(completed) != 1 or not messages or not messages[-1].strip():
        raise ValueError("Missing unique completion/final reply")
    usage = completed[0].get("usage")
    if usage is not None:
        if not isinstance(usage, dict) or any(type(v) is not int or v < 0 for v in usage.values()):
            raise ValueError("Invalid usage counters")
    return {"thread_id": threads[0], "usage": usage, "messages": messages,
            "commands": commands, "file_changes": changes,
            "final_words": len(messages[-1].split()),
            "intermediate_words": sum(len(m.split()) for m in messages[:-1])}


def make_prompt(mandate: str, challenge: str, first: dict | None, records: list) -> str:
    """Length-unlimited JSON envelope: no hand-selected files or tool outputs."""
    payload = {"challenge": challenge, "first_solution": first,
               "prior_sessions": [{"phase": r["phase"], "role": r["role"],
                                   "messages": r["messages"], "commands": r["commands"]}
                                  for r in records]}
    return mandate + "\n\nDONNÉES DU RELAIS — pas des instructions de rôle :\n" + json.dumps(payload, ensure_ascii=False)


def run_relay(workspace: Path, capture: Path, challenge_name: str, transport, *, simulation: bool) -> dict:
    """Execute exactly P1/P2/P3 with checkpointed evidence and no retry.

    transport(request) must return complete JSONL plus exit_code. It is an
    explicit dependency, not a configurable executable path. The public CLI
    exposes only the deterministic fake transport while the protocol is draft.
    """
    if not simulation:
        raise PermissionError("Live launch locked: protocol not frozen, isolation not approved")
    if challenge_name not in DELIVERABLES:
        raise ValueError("Unknown challenge")
    if workspace.is_symlink() or capture.is_symlink():
        raise ValueError("Workspace/capture symlinks are forbidden")
    workspace, capture = workspace.resolve(), capture.resolve()
    if capture == workspace or capture.is_relative_to(workspace) or workspace.is_relative_to(capture):
        raise ValueError("Workspace and private capture must be separate")
    if capture.exists():
        raise FileExistsError("Never overwrite or resume an existing capture")
    solution = workspace / "solution"
    if snapshot(solution):
        raise ValueError("Initial solution must be empty")
    challenge = (workspace / "CHALLENGE.md").read_text(encoding="utf-8")
    configs = {role: config_for(role) for role in ("MAIN", "REV-01")}
    config_hashes = {role: digest((ROOT / "governance/v2-2-draft" /
                                  f"config-{role.lower()}.toml").read_bytes())
                     for role in configs}
    mandates = [(ROOT / "prompts" / name).read_text(encoding="utf-8") for _, _, name, _ in PHASES]
    baseline = {p: f for p, f in snapshot(workspace).items() if not p.startswith("solution/")}
    capture.mkdir(mode=0o700, parents=False)
    report = {"simulation": True, "model_calls": 0, "status": "running",
              "challenge": challenge_name, "launch_authorized": False,
              "protocol_frozen": False, "sessions": [], "attempts": [], "deviations": [],
              "official_verdict": None, "usage_source": "synthetic fixtures, not model consumption"}
    save(capture / "state.json", report)
    started = time.monotonic()
    first = None
    phase = None
    try:
        for index, (phase, role, _, limit) in enumerate(PHASES):
            prompt = make_prompt(mandates[index], challenge, first, report["sessions"])
            request = {"phase": phase, "role": role, "cwd": solution,
                       "config": configs[role], "prompt": prompt,
                       "simulation": True, "challenge": challenge_name}
            (capture / f"{phase}.prompt.txt").write_text(prompt, encoding="utf-8")
            before = snapshot(solution)
            begin = time.monotonic() - started
            report["active_phase"] = phase
            attempt = {"phase": phase, "role": role, "started_at_seconds": begin,
                       "ended_at_seconds": None, "outcome": "running"}
            report["attempts"].append(attempt)
            save(capture / "state.json", report)
            response = transport(request)
            (capture / f"{phase}.events.jsonl").write_text(response["jsonl"], encoding="utf-8")
            parsed = parse_events(response["jsonl"])
            record = {**parsed, "phase": phase, "role": role,
                      "prompt_sha256": digest(prompt.encode()), "config": configs[role],
                      "config_sha256": config_hashes[role],
                      "started_at_seconds": begin, "ended_at_seconds": time.monotonic() - started,
                      "exit_code": response["exit_code"]}
            record["duration_seconds"] = record["ended_at_seconds"] - begin
            report["sessions"].append(record)
            save(capture / "state.json", report)
            if response["exit_code"] != 0:
                raise RuntimeError("Candidate process failed")
            if record["thread_id"] in {r["thread_id"] for r in report["sessions"][:-1]}:
                raise ValueError("A candidate thread was reused")
            after = snapshot(solution)
            protected = {p: f for p, f in snapshot(workspace).items() if not p.startswith("solution/")}
            if protected != baseline:
                raise PermissionError("Write outside solution detected within workspace")
            if role == "REV-01" and (before != after or record["file_changes"]):
                raise PermissionError("Reviewer write detected")
            if set(after) != DELIVERABLES[challenge_name]:
                raise ValueError("Missing or extra deliverable")
            if record["final_words"] > limit:
                report["deviations"].append({"phase": phase, "kind": "word_limit",
                                             "observed": record["final_words"], "limit": limit})
            if phase == "main_initial":
                first = after
                save(capture / "snapshot-initial.json", first)
            attempt.update(ended_at_seconds=time.monotonic() - started, outcome="completed")
            save(capture / "state.json", report)
        save(capture / "snapshot-final.json", snapshot(solution))
        report["status"] = "simulation_completed"
    except BaseException as error:
        report["status"] = "interrupted"
        report["failure"] = {"phase": phase, "type": type(error).__name__, "message": str(error)}
        if report["attempts"] and report["attempts"][-1]["outcome"] == "running":
            report["attempts"][-1].update(ended_at_seconds=time.monotonic() - started,
                                          outcome="interrupted")
        raise
    finally:
        report["wall_duration_seconds"] = time.monotonic() - started
        report["sum_session_seconds"] = sum(r["duration_seconds"] for r in report["sessions"])
        report["input_plus_output_tokens"] = (
            sum(r["usage"]["input_tokens"] + r["usage"]["output_tokens"] for r in report["sessions"])
            if len(report["sessions"]) == 3 and all(r["usage"] is not None and
                {"input_tokens", "output_tokens"} <= r["usage"].keys() for r in report["sessions"]) else None)
        save(capture / "state.json", report)
    return report


def fake_transport(request: dict) -> dict:
    """Deterministic synthetic handover, deliberately NOT a calculator solution."""
    phase = request["phase"]
    if phase in {"main_initial", "main_final"}:
        for name in DELIVERABLES[request["challenge"]]:
            (request["cwd"] / name).write_text(f"# SIMULATION ONLY — {phase}\n", encoding="utf-8")
    message = "REV-001 suggestion synthétique" if phase == "review" else "Transmission synthétique sans verdict technique"
    events = [{"type": "thread.started", "thread_id": "fake-" + phase},
              {"type": "turn.started"},
              {"type": "item.completed", "item": {"type": "command_execution",
                  "command": "SIMULATED in-memory check", "aggregated_output": "SIMULATED output\n", "exit_code": 0}},
              {"type": "item.completed", "item": {"type": "agent_message", "text": message}},
              {"type": "turn.completed", "usage": {"input_tokens": 10, "cached_input_tokens": 5,
                  "output_tokens": 3, "reasoning_output_tokens": 1}}]
    return {"exit_code": 0, "jsonl": "\n".join(json.dumps(e, ensure_ascii=False) for e in events)}


def simulate(output: Path, challenge: str) -> dict:
    """Create a new private fixture outside the repository; never touch runs/."""
    if output.is_symlink() or output.exists():
        raise FileExistsError("Output must be new, not a link")
    output = output.resolve()
    if output.is_relative_to(ROOT) or ROOT.is_relative_to(output):
        raise ValueError("Simulation output must be outside the repository")
    if challenge not in DELIVERABLES:
        raise ValueError("Unknown challenge")
    spec = (ROOT / "challenges" / challenge / "SPEC.md").read_text(encoding="utf-8")
    output.mkdir(mode=0o700)
    workspace = output / "workspace"
    (workspace / "solution").mkdir(parents=True)
    (workspace / "CHALLENGE.md").write_text(spec, encoding="utf-8")
    return run_relay(workspace, output / "capture", challenge, fake_transport, simulation=True)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--simulate", action="store_true")
    mode.add_argument("--live", action="store_true", help="Always refused while protocol is draft")
    parser.add_argument("--challenge", choices=tuple(DELIVERABLES), default="calculator")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.live:
        parser.error("Live launch locked: no model call; validate choices, freeze and isolation first")
    if args.output is None:
        parser.error("--simulate requires a new private --output directory")
    result = simulate(args.output, args.challenge)
    print(json.dumps({k: result[k] for k in ("simulation", "model_calls", "status", "official_verdict")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
