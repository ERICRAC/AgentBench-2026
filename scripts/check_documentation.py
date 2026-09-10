#!/usr/bin/env python3
"""Read-only editorial links, language navigation and recorded V2 hash checks.

This is not a Markdown parser, external URL checker, or GitHub anchor renderer.
Historical canonical artefacts are excluded from editorial language rules.
"""

import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
HISTORICAL_PUBLISHERS = {
    "98b7163dbf0c1c882a7d0fe3353dfe3ec3135f92395733576b9efd2bfa1dd275": "ad7e234",
    "d8458855862caeb9ec295bd593635974d0d91d6bd097e5f20a0aa2da948f648c": "63f9b92",
}


def check():
    errors = []
    files = list(ROOT.glob("README*.md"))
    for folder in ("docs", "results", "logs", "governance"):
        files.extend((ROOT / folder).rglob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"^(`{3,}|~{3,}).*?^\1\s*$", "", text, flags=re.M | re.S)
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            relative = unquote(target.split("#", 1)[0].strip("<>"))
            if relative and not (path.parent / relative).exists():
                errors.append(f"{path.relative_to(ROOT)}: missing {relative}")
    stems = ["docs/reading-guide", "docs/observability", "docs/documentation-audit"]
    stems += [str(p.relative_to(ROOT)).removesuffix(".md") for p in
              (ROOT / "results/run-summaries").glob("*.md")
              if not p.stem.endswith((".en", ".es", ".pt"))]
    for stem in stems:
        for suffix in ("", ".en", ".es", ".pt"):
            path = ROOT / (stem + suffix + ".md")
            if not path.exists():
                errors.append(f"Missing translation: {path.relative_to(ROOT)}")
                continue
            heading = "\n".join(path.read_text().splitlines()[:4])
            if not all(name in heading for name in ("Français", "English (UK)", "Español", "Português")):
                errors.append(f"Missing language navigation: {path.relative_to(ROOT)}")
            if re.search(r"\b\d{1,2}:\d{2}(?::\d{2})?\b", path.read_text()):
                errors.append(f"Clock-like timestamp: {path.relative_to(ROOT)}")
    annotations = json.loads((ROOT / "docs/run-interpretations.json").read_text())
    checks = 0
    for name in annotations:
        run = ROOT / "runs" / name
        meta = json.loads((run / "run.json").read_text())
        targets = {
            "challenge_sha256": run / "CHALLENGE.md",
            "acceptance_tests_sha256": ROOT / "challenges" / meta["challenge"] / "tests/test_acceptance.py",
            "base_prompt_sha256": ROOT / meta["base_prompt"],
            "runner_sha256": ROOT / meta["runner"],
        }
        for key in ("minutes", "trace", "publisher"):
            if key in meta and key + "_sha256" in meta:
                targets[key + "_sha256"] = ROOT / meta[key]
        for key, path in targets.items():
            checks += 1
            if hashlib.sha256(path.read_bytes()).hexdigest() != meta[key]:
                reference = HISTORICAL_PUBLISHERS.get(meta[key]) if key == "publisher_sha256" else None
                if reference:
                    # Publisher evolved before this maintenance task. Verify the
                    # recorded historical bytes, never rewrite a run's hash.
                    try:
                        historical = subprocess.check_output(
                            ["git", "show", f"{reference}:scripts/publish_v2.py"], cwd=ROOT)
                        if hashlib.sha256(historical).hexdigest() != meta[key]:
                            errors.append(f"{name}: historical publisher hash mismatch")
                    except subprocess.CalledProcessError:
                        errors.append(f"{name}: historical publisher unavailable in Git history")
                else:
                    errors.append(f"{name}: hash mismatch {key}")
        for item in meta.get("files", []):
            checks += 1
            if hashlib.sha256((run / item["path"]).read_bytes()).hexdigest() != item["sha256"]:
                errors.append(f"{name}: hash mismatch {item['path']}")
        for role, expected in meta["config_sha256"].items():
            checks += 1
            if hashlib.sha256((run / f"config-{role.lower()}.toml").read_bytes()).hexdigest() != expected:
                errors.append(f"{name}: config mismatch {role}")
    print(f"Editorial documents: {len(files)}; historical hash checks: {checks}")
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(check())
