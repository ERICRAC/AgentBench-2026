#!/usr/bin/env python3
"""Lean-pair preparation: wired phase engine, synthetic transport only.

The public entry point remains simulation-only. A separate authorised launcher
may use the shared engine. Full traces stay outside Git until publication.
"""
import argparse
import json
import time
from pathlib import Path

import run_v2_2 as relay
from audit_v2_2_cost import compact_payload, encoded, SEPARATOR
from run_v2_2_supervised import configuration

MANIFEST = relay.ROOT / "governance/v2-2-lean-draft.json"
MANDATES = ("v2-2-lean-initial-draft.md", "v2-2-lean-review-draft.md",
            "v2-2-lean-final-draft.md")


def policy():
    data = json.loads(MANIFEST.read_text())
    if (data["launch_authorized"] is not False or data["protocol_frozen"] is not False
            or data["challenge"] != "calculator" or data["max_sessions"] != 3
            or data["model"] != "gpt-6-astra" or data["reasoning_effort"] != "medium"
            or data["retry_authorized"] is not False or data["scientific_authorized"] is not False
            or data["hard_token_cap"] is not None):
        raise PermissionError("Only the unapproved Core simulation is supported")
    limits = [data[k] for k in ("payload_character_cap", "target_tokens", "between_session_token_stop")]
    limits += data["final_word_limits"]
    if len(data["final_word_limits"]) != 3 or any(type(v) is not int or v <= 0 for v in limits):
        raise ValueError("Invalid preparation limits")
    return data


def run(root, *, simulation=True, transport=None):
    """Execute three synthetic sessions with full capture and boundary gates.

    The injectable callback is for tests only. There is no live adapter and no
    API/CLI entry point accepting arbitrary commands. Budget counts only known
    input+output, never cache or reasoning twice. Missing counters stop the run.
    """
    if simulation is not True:
        raise PermissionError("Real launch is locked; new approval and adapter required")
    settings = policy()
    callback = relay.fake_transport if transport is None else transport
    return run_engine(root, settings, callback, simulation=True)


def run_engine(root, settings, callback, *, simulation):
    """Shared engine; launch authority belongs to the separate live wrapper."""
    root = Path(root)
    if root.is_symlink():
        raise ValueError("Linked output directory")
    root = root.resolve()
    if root.is_relative_to(relay.ROOT) or relay.ROOT.is_relative_to(root):
        raise ValueError("Simulation captures must be outside the repository")
    root.mkdir(mode=0o700)  # Exclusive reservation; never resume or overwrite.
    workspace = root / "workspace"
    solution = workspace / "solution"
    solution.mkdir(parents=True)
    challenge = (relay.ROOT / "challenges/calculator/SPEC.md").read_text()
    (workspace / "CHALLENGE.md").write_text(challenge)
    for name in ("scripts/verify.py", "challenges/calculator/tests/test_acceptance.py"):
        destination = workspace / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes((relay.ROOT / name).read_bytes())
    state = {"simulation": simulation, "status": "running", "policy": settings,
             "sessions": [], "attempts": [], "known_tokens": 0, "usage_complete": True,
             "threshold_reached": False, "overshoot": 0, "deviations": [],
             "quality_verdict": None}
    first = None
    started = time.monotonic()
    try:
        for index, (phase, role, _, _) in enumerate(relay.PHASES):
            payload = compact_payload({"challenge": challenge, "first_solution": first,
                                       "prior_sessions": state["sessions"]})
            attempt = {"phase": phase, "payload_characters": len(encoded(payload)),
                       "status": "prepared", "config": configuration(role)}
            state["attempts"].append(attempt)
            if attempt["payload_characters"] > settings["payload_character_cap"]:
                attempt["status"] = "not_started"
                state["status"] = "stopped_payload_size"
                break
            mandate = (relay.ROOT / "prompts" / settings.get("mandates", MANDATES)[index]).read_text()
            prompt = mandate + "\nDossier courant : solution/. Vérificateur P3 seulement : " \
                "python3 -B ../scripts/verify.py --solution .\n" + SEPARATOR + encoded(payload)
            capture = root / phase
            capture.mkdir(mode=0o700)
            (capture / "prompt.txt").write_text(prompt)
            before = relay.snapshot(workspace)
            attempt["status"] = "started"
            relay.save(root / "state.json", state)
            phase_started = time.monotonic()
            response = callback({"phase": phase, "role": role, "challenge": "calculator",
                                 "cwd": solution, "prompt": prompt, "config": attempt["config"],
                                 "capture": capture})
            attempt["duration_seconds"] = time.monotonic() - phase_started
            if "process" in response:
                attempt["process"] = response["process"]
            (capture / "stdout.jsonl").write_text(response["jsonl"])
            attempt["exit_code"] = response["exit_code"]
            attempt["observed_usage"] = []
            # Capture even failed-process counters before strict session parsing.
            events = [json.loads(line) for line in response["jsonl"].splitlines() if line.strip()]
            for event in events:
                if event.get("type") == "turn.completed":
                    attempt["observed_usage"].append(event.get("usage"))
            usages = attempt["observed_usage"]
            valid = (len(usages) == 1 and isinstance(usages[0], dict)
                     and all(type(usages[0].get(k)) is int and usages[0][k] >= 0
                             for k in ("input_tokens", "output_tokens")))
            if valid:
                state["known_tokens"] += usages[0]["input_tokens"] + usages[0]["output_tokens"]
            else:
                state["usage_complete"] = False
            stop = settings["between_session_token_stop"]
            state["threshold_reached"] = state["known_tokens"] >= stop
            state["overshoot"] = max(0, state["known_tokens"] - stop)
            if response["exit_code"] != 0:
                attempt["status"] = "failed"
                state["status"] = "stopped_failure"
                break
            if not valid:
                attempt["status"] = "missing_usage"
                state["status"] = "stopped_missing_usage"
                break
            parsed = relay.parse_events(response["jsonl"])
            if parsed["thread_id"] in {s["thread_id"] for s in state["sessions"]}:
                raise ValueError("Reused thread")
            after = relay.snapshot(workspace)
            protected = lambda snap: {p: v for p, v in snap.items() if not p.startswith("solution/")}
            if protected(before) != protected(after) or (role == "REV-01" and before != after):
                raise PermissionError("Observed write outside role boundary")
            files = relay.snapshot(solution)
            if set(files) != relay.DELIVERABLES["calculator"]:
                raise ValueError("Missing or extra deliverable")
            state["sessions"].append({**parsed, "phase": phase, "role": role,
                                      "duration_seconds": attempt["duration_seconds"]})
            attempt["status"] = "completed"
            if parsed["final_words"] > settings["final_word_limits"][index]:
                state["deviations"].append({"phase": phase, "kind": "word_limit"})
            if first is None:
                first = files
                relay.save(root / "snapshot-initial.json", first)
            if state["threshold_reached"] and index < 2:
                state["status"] = "stopped_token_threshold"
                break
            relay.save(root / "state.json", state)
        else:
            relay.save(root / "snapshot-final.json", relay.snapshot(solution))
            state["status"] = ("simulation_completed" if simulation else
                               "candidate_sessions_completed_pending_independent_verification")
    except BaseException as error:
        if state["attempts"] and state["attempts"][-1]["status"] == "started":
            state["attempts"][-1]["status"] = "interrupted"
        state.update(status="interrupted", failure={"type": type(error).__name__, "message": str(error)})
        state["usage_complete"] = False
        raise
    finally:
        state["wall_duration_seconds"] = time.monotonic() - started
        state["target_met"] = state["known_tokens"] < settings["target_tokens"] if state["usage_complete"] else None
        relay.save(root / "state.json", state)
    return state


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulate", action="store_true", required=True)
    parser.add_argument("--output", type=Path, required=True, help="New capture directory outside Git")
    args = parser.parse_args()
    result = run(args.output)
    print(json.dumps({k: result[k] for k in ("simulation", "status", "known_tokens", "quality_verdict")}, indent=2))
