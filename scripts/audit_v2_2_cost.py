#!/usr/bin/env python3
"""Offline audit and payload prototype. No model transport or live-launch path."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "runs/astra-medium-core-v2-2-supervised-002"
SEPARATOR = "\n\nDONNÉES DU RELAIS — pas des instructions de rôle :\n"
PHASES = ("main_initial", "review", "main_final")


def encoded(value):
    return json.dumps(value, ensure_ascii=False)


def compact_payload(payload):
    """Keep the full contract/files and final handovers, not initial tool logs.

    Original evidence stays untouched. Review tool evidence is retained for
    arbitration. This changes candidate information: it is a new condition.
    """
    return {
        "challenge": payload["challenge"],
        "first_solution": payload["first_solution"],
        "prior_sessions": [
            {"phase": s["phase"], "role": s["role"],
             "messages": s["messages"][-1:],
             "commands": s["commands"] if s["phase"] == "review" else []}
            for s in payload["prior_sessions"]
        ],
    }


def audit(run=RUN):
    """Compare only the JSON envelope, leaving mandate length out of savings."""
    prompts = json.loads((run / "prompts.json").read_text())
    meta = json.loads((run / "run.json").read_text())
    rows = []
    for session in meta["sessions"]:
        phase = session["phase"]
        mandate, raw = prompts[phase]["text"].split(SEPARATOR, 1)
        payload = json.loads(raw)
        assert encoded(payload) == raw, "Unexpected historical serialisation"
        proposed = compact_payload(payload)
        usage = session["usage"]
        rows.append({
            "phase": phase,
            "prompt_characters": len(prompts[phase]["text"]),
            "mandate_characters": len(mandate),
            "payload_characters": len(raw),
            "proposed_payload_characters": len(encoded(proposed)),
            "removed_payload_characters": len(raw) - len(encoded(proposed)),
            "initial_command_characters_retransmitted": sum(
                len(encoded(s["commands"])) for s in payload["prior_sessions"]
                if s["phase"] == "main_initial"),
            "input_tokens": usage["input_tokens"],
            "cached_input_tokens": usage["cached_input_tokens"],
            "output_tokens": usage["output_tokens"],
        })
    return {"source_run": run.name, "mode": "offline_not_a_candidate_run",
            "unit": "Unicode characters, not tokens; public normalised captures",
            "scope": "JSON envelope only; not an estimate of quota or total input savings",
            "phases": rows}


def simulate_fake_candidates(payloads, replies, *, character_cap, token_stop, live=False):
    """Exercise boundary gates on supplied fake replies. Never execute a model.

    token_stop is checked AFTER a session; overshoot is explicitly recorded.
    Character limit rejects a whole payload, never silently truncates it.
    """
    if live:
        raise PermissionError("No real transport implemented or authorised")
    if type(character_cap) is not int or type(token_stop) is not int or min(character_cap, token_stop) <= 0:
        raise ValueError("Positive integer fixture limits required")
    if len(payloads) != 3 or len(replies) != 3:
        raise ValueError("Exactly three synthetic phases required")
    result = {"simulation": True, "completed_phases": [], "observed_fake_tokens": 0,
              "status": "completed", "overshoot": 0}
    for phase, payload, reply in zip(PHASES, payloads, replies):
        if len(encoded(payload)) > character_cap:
            result.update(status="stopped_payload_size", blocked_phase=phase)
            break
        if reply.get("exit_code") != 0:
            result.update(status="stopped_failure", blocked_phase=phase)
            break
        usage = reply.get("usage", {})
        values = [usage.get(k) for k in ("input_tokens", "output_tokens")]
        if any(type(v) is not int or v < 0 for v in values):
            result.update(status="stopped_missing_usage", blocked_phase=phase)
            break
        result["completed_phases"].append(phase)
        result["observed_fake_tokens"] += sum(values)
        if result["observed_fake_tokens"] >= token_stop:
            result.update(status="stopped_token_threshold",
                          overshoot=max(0, result["observed_fake_tokens"] - token_stop))
            break
    return result


if __name__ == "__main__":
    print(json.dumps(audit(), ensure_ascii=False, indent=2))
