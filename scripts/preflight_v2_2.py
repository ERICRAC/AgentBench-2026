#!/usr/bin/env python3
"""Static draft checks and two deterministic simulations, never a model call."""

import argparse
import json
from pathlib import Path
import tempfile

import run_v2_2 as relay


def check() -> dict:
    choices_path = relay.ROOT / "governance/v2-2-draft/choices.json"
    choices = json.loads(choices_path.read_text(encoding="utf-8"))
    if choices["status"] != "draft_simulation_only" or any(
        choices[key] is not False for key in ("protocol_frozen", "launch_authorized",
                                            "real_isolation_validated", "model_access_checked")
    ):
        raise ValueError("This preflight accepts only an unfrozen, unauthorised draft")
    expected_choices = {
        "organisation": "two_roles_three_fresh_sessions_one_review",
        "model": "gpt-6-astra", "reasoning_effort": "medium",
        "pilot": "one_attempt_per_challenge", "global_token_cap": None,
        "global_time_cap_seconds": None,
        "limits_status": "proposed_no_new_cap_not_approved",
        "review_words": 1200, "initial_handover_words": 600,
        "final_handover_words": 1200,
        "repeat_plan_status": "18_runs_proposed_not_authorized",
        "stop_policy": "stop_no_retry_no_automatic_quota_wait",
        "first_official_pass": "P3_after_review", "snapshot_diagnostic": "after_run_only",
    }
    if choices["choices"] != expected_choices:
        raise ValueError("Draft choices diverge from the implemented simulation")
    for role in ("MAIN", "REV-01"):
        relay.config_for(role)
    files = ["scripts/run_v2_2.py", "scripts/preflight_v2_2.py", "tests/test_v2_2.py",
             "scripts/verify.py", "governance/V2_2_PROTOCOL.md",
             "governance/v2-2-draft/choices.json",
             "governance/v2-2-draft/config-main.toml", "governance/v2-2-draft/config-rev-01.toml"]
    files.extend("prompts/" + row[2] for row in relay.PHASES)
    for challenge in relay.DELIVERABLES:
        files.extend(f"challenges/{challenge}/{tail}" for tail in ("SPEC.md", "tests/test_acceptance.py"))
    hashes = {p: relay.digest((relay.ROOT / p).read_bytes()) for p in files}
    simulations = []
    with tempfile.TemporaryDirectory(prefix="agentbench-v2-2-preflight-") as private:
        for challenge in relay.DELIVERABLES:
            result = relay.simulate(Path(private) / challenge, challenge)
            if result["status"] != "simulation_completed" or len(result["sessions"]) != 3:
                raise ValueError("Incomplete simulated topology")
            simulations.append({"challenge": challenge, "status": result["status"],
                                "sessions": len(result["sessions"]), "model_calls": 0,
                                "official_verdict": None})
    return {"kind": "static_and_synthetic_preflight", "status": "passed",
            "protocol_frozen": False, "launch_authorized": False,
            "model_calls": 0, "model_access_checked": False,
            "runtime_configuration_acceptance_checked": False,
            "os_isolation_checked": False, "quota_checked": False,
            "hashes_kind": "current_draft_inventory_not_frozen_baseline",
            "hashes": hashes, "simulations": simulations,
            "limits": choices["pending_before_freeze"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New JSON file; existing output is refused")
    args = parser.parse_args(argv)
    report = check()
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as stream:
            stream.write(text)
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
