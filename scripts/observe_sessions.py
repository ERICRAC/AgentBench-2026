"""Opt-in, content-free timing of session invocations; no orchestration logic."""

from __future__ import annotations

import json
from pathlib import Path
import threading
import time


class SessionObserver:
    """Record monotonic offsets around a callable, including failures.

    The origin is entry into the instrumented runner, not the historical
    runner's wall-duration origin. The interval includes preparation and record
    parsing; it is deliberately separate from the historical CLI duration.
    No prompt, reply, error text, absolute path or wall-clock timestamp is saved.
    """

    def __init__(self, clock=time.monotonic):
        self.clock = clock
        self.origin = clock()
        self.lock = threading.Lock()
        self.events = []

    def invoke(self, function, metadata, **kwargs):
        start = self.clock() - self.origin
        outcome = "failed"
        try:
            result = function(**kwargs)
            outcome = "returned"
            return result
        finally:
            end = self.clock() - self.origin
            event = dict(metadata)
            event.update(
                started_at_seconds=start,
                ended_at_seconds=end,
                duration_seconds=end - start,
                outcome=outcome,
            )
            with self.lock:
                self.events.append(event)
                payload = {
                    "schema_version": 1,
                    "origin": "instrumented runner entry; monotonic clock",
                    "boundary": "whole run_session invocation; excludes observation write",
                    "metadata_kind": "specified topology; measured timing",
                    "sessions": sorted(self.events, key=lambda item: item["started_at_seconds"]),
                }
                # Private capture only. Persist each completion, including failure.
                target = Path(kwargs["private_root"]) / "observations.json"
                temporary = target.with_suffix(".tmp")
                temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
                temporary.replace(target)


def v2_topology():
    """Describe the frozen V2 graph, not a scheduling implementation."""
    phases = ["sa01_initial", "sa02_initial", "sa01_cross", "sa02_cross",
              "main_first", "sa03_critic", "main_final"]
    roles = ["SA-01", "SA-02", "SA-01", "SA-02", "MAIN", "SA-03", "MAIN"]
    labels = ["01-sa01-initial", "02-sa02-initial", "03-sa01-cross",
              "04-sa02-cross", "05-main-first", "06-sa03-critic", "07-main-final"]
    dependencies = [[], [], phases[:2], phases[:2], phases[:4],
                    ["main_first"], ["sa03_critic"]]
    received = [[], [], phases[:2], phases[:2], phases[:4],
                phases[:4] + ["main_first"], phases[:6]]
    return {
        label: {"session_id": phase, "role": role,
                "parallel_group": "P1" if index < 2 else "P2" if index < 4 else None,
                "depends_on": dependencies[index], "receives_from": received[index],
                "writes_solution": role == "MAIN"}
        for index, (label, phase, role) in enumerate(zip(labels, phases, roles))
    }
