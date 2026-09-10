#!/usr/bin/env python3
"""Read-only preflight. Never starts Codex, a verifier or a candidate.

Checks are scoped to the two prepared Astra medium V1 attempts. Historical
candidate solutions are deliberately never opened. Re-run before launch;
the expected prepared state is no longer applicable after a real run starts.
"""
import ast
import hashlib
import json
import os
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
RUNS = ("astra-medium-core-v1-001", "astra-medium-scientific-v1-001")
PARAMETERS = ("model", "model_reasoning_effort", "model_context_window",
              "model_auto_compact_token_limit", "model_auto_compact_token_limit_scope",
              "approval_policy", "sandbox_mode", "web_search")


def check(root=ROOT):
    errors, checks = [], 0
    def require(condition, label):
        nonlocal checks
        checks += 1
        if not condition:
            errors.append(label)
    baseline = tomllib.loads((root / "governance/astra-v1.toml").read_text())
    expected = {**baseline, "model_reasoning_effort": "medium"}
    for identifier in RUNS:
        run = root / "runs" / identifier
        data = json.loads((run / "run.json").read_text())
        config = tomllib.loads((run / "config.toml").read_text())
        require(config == expected, f"{identifier}: only high → medium may differ from V1 config")
        require(data["run_id"] == identifier and data["mode"] == "codex-single", f"{identifier}: identity")
        require(data["status"] == "prepared_not_started" and data["launch_authorized"] is False,
                f"{identifier}: preparation only")
        require(all(data.get(key) is None for key in ("verification", "usage", "duration_seconds", "thread_id")),
                f"{identifier}: no invented results")
        solution = run / "solution"
        require(solution.is_dir() and not any(solution.iterdir()), f"{identifier}: solution must exist and be empty")
        require(solution.is_dir() and os.access(solution, os.W_OK), f"{identifier}: writable solution")
        challenge = data["challenge"]
        paths = {"config_sha256": run / "config.toml", "prompt_sha256": root / data["prompt"],
                 "challenge_sha256": run / "CHALLENGE.md",
                 "acceptance_tests_sha256": root / "challenges" / challenge / "tests/test_acceptance.py",
                 "runner_sha256": root / data["runner"], "verifier_sha256": root / data["verifier"]}
        for key, path in paths.items():
            require(hashlib.sha256(path.read_bytes()).hexdigest() == data[key], f"{identifier}: {key}")
        require((run / "CHALLENGE.md").read_bytes() == (root / "challenges" / challenge / "SPEC.md").read_bytes(),
                f"{identifier}: frozen challenge copy")
        v2 = root / "runs" / data["comparison_run"]
        reference = json.loads((v2 / "run.json").read_text())
        require(reference["status"] == "completed" and reference["campaign_id"] == data["campaign_id"],
                f"{identifier}: completed medium V2 reference")
        for key in ("challenge_sha256", "acceptance_tests_sha256"):
            require(data[key] == reference[key], f"{identifier}: V2 {key}")
        for role in ("main", "sa-01", "sa-02", "sa-03"):
            peer = tomllib.loads((v2 / f"config-{role}.toml").read_text())
            keys = PARAMETERS if role == "main" else tuple(k for k in PARAMETERS if k != "sandbox_mode")
            require(all(config[k] == peer[k] for k in keys)
                    and (role == "main" or peer["sandbox_mode"] == "read-only"),
                    f"{identifier}: shared parameters and role-specific permissions vs V2 {role}")
        tree = ast.parse(paths["acceptance_tests_sha256"].read_text())
        methods = [node.name for node in ast.walk(tree)
                   if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")]
        require(len(methods) == (6 if challenge == "calculator" else 9), f"{identifier}: frozen group count")
        require(data["preflight_environment"]["codex_cli"] == reference["codex_cli"], f"{identifier}: recorded CLI")
    return checks, errors


if __name__ == "__main__":
    count, errors = check()
    print(f"Static preflight: {count - len(errors)}/{count} checks passed; no candidate launched")
    for error in errors:
        print(error)
    raise SystemExit(bool(errors))
