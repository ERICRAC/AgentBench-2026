#!/usr/bin/env python3
"""Merge screened timing into a NEW trace copy; never overwrite evidence.

Run the historical publisher in the usual way, review its output, then use
--trace path/trace.json --observations private/observations.json
--output path/trace-observed.json. Repoint future metadata only after review.
"""

import argparse
import json
import math
from pathlib import Path


def merge(trace, observations):
    """Validate identifiers and measurements; export an explicit allowlist."""
    sessions = trace["sessions"]
    ids = [s.get("session_id", s.get("phase")) for s in sessions]
    events = observations["sessions"]
    event_ids = [e["session_id"] for e in events]
    if len(set(ids)) != len(ids) or len(set(event_ids)) != len(event_ids):
        raise ValueError("Duplicate session identifiers")
    if set(ids) != set(event_ids):
        raise ValueError("Trace and observation sessions differ; partial capture requires review")
    mapping = {e["session_id"]: e for e in events}
    result = json.loads(json.dumps(trace))
    for session, identifier in zip(result["sessions"], ids):
        event = mapping[identifier]
        start, end, duration = (event[k] for k in
                               ("started_at_seconds", "ended_at_seconds", "duration_seconds"))
        if not all(isinstance(v, (int, float)) and not isinstance(v, bool)
                   and math.isfinite(v) for v in (start, end, duration)):
            raise ValueError("Invalid timing value")
        if start < 0 or end < start or not math.isclose(end-start, duration, abs_tol=1e-6):
            raise ValueError("Inconsistent timing")
        for dependency in event["depends_on"]:
            if dependency not in mapping or mapping[dependency]["ended_at_seconds"] > start:
                raise ValueError("Dependency barrier violated")
        if any(source not in mapping for source in event["receives_from"]):
            raise ValueError("Unknown information source")
        if session.get("role") != event["role"]:
            raise ValueError("Role mismatch")
        session["observation"] = {key: event[key] for key in (
            "session_id", "role", "parallel_group", "depends_on", "receives_from",
            "writes_solution", "started_at_seconds", "ended_at_seconds",
            "duration_seconds", "outcome")}
    result["observation_schema_version"] = 1
    result["observation_origin"] = "instrumented runner entry; monotonic clock"
    result["observation_boundary"] = "whole run_session invocation; excludes observation write"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("trace", "observations", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    result = merge(json.loads(args.trace.read_text()), json.loads(args.observations.read_text()))
    with args.output.open("x", encoding="utf-8") as output:
        output.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
