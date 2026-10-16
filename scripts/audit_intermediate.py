#!/usr/bin/env python3
"""Read-only intermediate audit: recorded costs and common post-hoc probes.

No model calls or writes. Probe archived candidates with bytecode disabled.
These known probes are exploratory and must never change official scores.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
RUNS = (
    "astra-medium-core-v1-001", "astra-medium-core-v2-001",
    "astra-medium-core-v2-2-supervised-002", "astra-medium-core-v2-2-lean-001",
    "astra-medium-scientific-v1-001", "astra-medium-scientific-v2-001",
    "astra-medium-scientific-v2-2-lean-002",
)


def audit():
    costs = []
    for run in RUNS:
        path = ROOT / "runs" / run / "run.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        usage = data.get("usage")
        if usage is None:
            usage = {k: sum(s["usage"][k] for s in data["sessions"])
                     for k in ("input_tokens", "output_tokens", "cached_input_tokens")}
        costs.append({"run": run, "metadata_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                      "wall_seconds": data["wall_duration_seconds"],
                      "input_tokens": usage["input_tokens"],
                      "output_tokens": usage["output_tokens"],
                      "cached_input_tokens": usage["cached_input_tokens"],
                      "total_tokens": usage["input_tokens"] + usage["output_tokens"],
                      "uncached_input_plus_output": usage["input_tokens"] - usage["cached_input_tokens"] + usage["output_tokens"]})
    probes = []
    for number, run in enumerate((RUNS[4], RUNS[5], RUNS[6])):
        path = ROOT / "runs" / run / "solution/scientific_calculator.py"
        name = "audit_candidate_" + str(number)
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        previous = sys.modules.get(name)
        sys.modules[name] = module
        try:
            spec.loader.exec_module(module)
            for probe, expression, expected in (
                    ("P1_trailing_spaces", "1" + " " * 10000, 1.0),
                    ("P2_long_sum", "+".join(["1"] * 1500), 1500.0)):
                record = {"run": run, "probe": probe, "expected": expected,
                          "solution_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                try:
                    value = module.evaluate(expression)
                    record.update(outcome="value", value=value, matches_expected=math.isclose(value, expected))
                except Exception as error:
                    record.update(outcome=type(error).__name__, message=str(error), matches_expected=False)
                probes.append(record)
        finally:
            if previous is None:
                del sys.modules[name]
            else:
                sys.modules[name] = previous
    return {"scope": "Intermediate audit, no candidate launched; candidate costs exclude audit costs",
            "python": sys.version.split()[0], "costs": costs,
            "uncached_metric_note": "Diagnostic only, not monetary cost or subscription quota",
            "probe_classification": "Post-hoc, previously known cases, common to three archived solutions; not official scores or unseen validation",
            "probe_definitions": {"P1_trailing_spaces": "'1' + ' ' * 10000",
                                  "P2_long_sum": "'+'.join(['1'] * 1500)"},
            "probes": probes}


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    print(json.dumps(audit(), ensure_ascii=False, indent=2))
