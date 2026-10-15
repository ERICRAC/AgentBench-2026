#!/usr/bin/env python3
"""Read-only envelope sizing with synthetic text; no candidate or transport."""
import hashlib
import json
from pathlib import Path

from audit_v2_2_cost import compact_payload, encoded

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "challenges/scientific-calculator/SPEC.md"


def synthetic_text(size):
    """Escapable dummy text, not code or an estimate of solution size."""
    pattern = '# synthetic "fixture"\n'
    return (pattern * (size // len(pattern) + 1))[:size]


def file_record(text):
    raw = text.encode("utf-8")
    return {"sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw), "text": text}


def payloads(code_characters):
    challenge = SPEC.read_text(encoding="utf-8")
    files = {"scientific_calculator.py": file_record(synthetic_text(code_characters)),
             "README.md": file_record(synthetic_text(1000))}
    main = {"phase": "main_initial", "role": "MAIN",
            "messages": [" ".join(["synthetic"] * 150)], "commands": []}
    review = {"phase": "review", "role": "REV-01",
              "messages": [" ".join(["synthetic"] * 300)],
              "commands": [{"command": "synthetic non-executed check",
                            "output": synthetic_text(1000)}]}
    return [compact_payload({"challenge": challenge, "first_solution": files if i else None,
                             "prior_sessions": [main, review][:i]}) for i in range(3)]


def measure(code_characters, cap):
    sizes = [len(encoded(p)) for p in payloads(code_characters)]
    return {"synthetic_code_characters": code_characters,
            "payload_characters": dict(zip(("main_initial", "review", "main_final"), sizes)),
            "fits_all_phases": all(n <= cap for n in sizes)}


def audit():
    cases = []
    for cap in (12000, 24000):
        low, high = 0, cap
        while low < high:
            middle = (low + high + 1) // 2
            if measure(middle, cap)["fits_all_phases"]:
                low = middle
            else:
                high = middle - 1
        maximum = low if measure(0, cap)["fits_all_phases"] else None
        cases.append({"cap": cap, "max_synthetic_code_characters": maximum,
                      "profiles": [measure(n, cap) for n in (4000, 8000, 16000)]})
    return {"mode": "offline_synthetic_size_audit", "model_calls": 0,
            "launch_authorized": False, "unit": "Unicode characters, not tokens",
            "scope": "JSON envelope only, excludes mandate and client context",
            "challenge_sha256": hashlib.sha256(SPEC.read_bytes()).hexdigest(),
            "fixture": {"readme_characters": 1000, "initial_words": 150,
                        "review_words": 300, "review_output_characters": 1000},
            "cases": cases}


if __name__ == "__main__":
    print(json.dumps(audit(), ensure_ascii=False, indent=2))
