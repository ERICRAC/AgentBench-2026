#!/usr/bin/env python3
"""Frozen scientific adapter; explicit per-run approval required, no retry."""
import argparse
import json
from pathlib import Path

import run_v2_2_lean_scientific as lean
from run_v2_2_supervised import command
from v2_2_transport import capture_process

RUN_ID = "astra-medium-scientific-v2-2-lean-001"
MANIFEST = lean.relay.ROOT / "governance/v2-2-lean-scientific-001.json"
MANDATES = [f"v2-2-lean-scientific-001-{phase}.md" for phase in ("initial", "review", "final")]
INPUTS = [
    "scripts/run_v2_2_lean_scientific.py", "scripts/run_v2_2_lean_scientific_live.py",
    "scripts/audit_v2_2_cost.py", "scripts/run_v2_2.py", "scripts/run_v2_2_supervised.py",
    "scripts/v2_2_transport.py", "scripts/verify.py",
    "challenges/scientific-calculator/SPEC.md",
    "challenges/scientific-calculator/tests/test_acceptance.py",
    "governance/v2-2-draft/config-main.toml", "governance/v2-2-draft/config-rev-01.toml",
    *["prompts/" + name for name in MANDATES],
]


def validate():
    data = json.loads(MANIFEST.read_text())
    expected = {"run_id": RUN_ID, "campaign": "astra-medium-lean-002",
                "protocol_frozen": True, "launch_authorized": False,
                "challenge": "scientific-calculator", "model": "gpt-6-astra",
                "reasoning_effort": "medium", "max_sessions": 3,
                "payload_character_cap": 24000, "between_session_token_stop": 150000,
                "hard_token_cap": None, "target_tokens": None, "retry_authorized": False,
                "final_word_limits": [150, 300, 300], "mandates": MANDATES}
    if any(type(data.get(k)) is not type(v) or data[k] != v for k, v in expected.items()):
        raise PermissionError("Frozen scientific conditions changed")
    if set(data["inputs_sha256"]) != set(INPUTS):
        raise ValueError("Incomplete or unexpected frozen input set")
    for name in INPUTS:
        if lean.relay.digest((lean.relay.ROOT / name).read_bytes()) != data["inputs_sha256"][name]:
            raise ValueError("Frozen input changed: " + name)
    return data


def transport(request, capture=capture_process):
    """Native CLI with existing per-role permissions; raw captures stay private."""
    process = capture(command(request["config"], request["cwd"]), request["prompt"],
                      request["capture"] / "process", cwd=request["cwd"])
    return {"exit_code": process["exit_code"], "process": process,
            "jsonl": (request["capture"] / "process/stdout.jsonl").read_text()}


def launch(root, *, approve_run=None):
    # A flag is a deliberate operator action, not proof of human consent.
    # The orchestrator may supply it only AFTER explicit user launch approval.
    if approve_run != RUN_ID:
        raise PermissionError("Explicit user approval for this run is required")
    manifest = validate()
    root = Path(root)
    if root.is_symlink():
        raise ValueError("Linked workspace")
    root = root.resolve()
    if root.exists() or root.is_relative_to(lean.relay.ROOT) or lean.relay.ROOT.is_relative_to(root):
        raise ValueError("Fresh external workspace required")
    public = lean.relay.ROOT / "runs" / RUN_ID
    public.mkdir()  # One-shot persistent reservation, also after failure.
    (public / "CHALLENGE.md").write_bytes((lean.relay.ROOT / "challenges/scientific-calculator/SPEC.md").read_bytes())
    lean.relay.save(public / "run.json", {"run_id": RUN_ID, "status": "reserved",
                    "campaign": manifest["campaign"], "exploratory": True,
                    "launch_approval": "explicit_operator_confirmation",
                    "manifest_sha256": lean.relay.digest(MANIFEST.read_bytes())})
    return lean._execute_engine(root, manifest, transport, simulation=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--run", type=Path)
    parser.add_argument("--approve-run", choices=[RUN_ID])
    args = parser.parse_args()
    if args.check:
        if args.approve_run:
            parser.error("--check never authorises a launch")
        validate()
        print("Frozen scientific inputs verified; no model called; launch requires approval")
    else:
        state = launch(args.run, approve_run=args.approve_run)
        print(json.dumps({k: state[k] for k in ("status", "known_tokens", "usage_complete", "wall_duration_seconds")}))
