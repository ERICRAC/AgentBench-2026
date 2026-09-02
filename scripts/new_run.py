#!/usr/bin/env python3
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "challenges" / "calculator" / "SPEC.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Crée une tentative AgentBench vierge.")
    parser.add_argument("run_id", help="Identifiant, par exemple codex-single-001")
    args = parser.parse_args()

    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,63}", args.run_id):
        parser.error("L'identifiant doit contenir uniquement a-z, 0-9 et des tirets.")

    run_dir = ROOT / "runs" / args.run_id
    if run_dir.exists():
        parser.error(f"La tentative existe déjà : {run_dir}")

    solution_dir = run_dir / "solution"
    solution_dir.mkdir(parents=True)
    (run_dir / "CHALLENGE.md").write_text(SPEC.read_text(encoding="utf-8"), encoding="utf-8")
    metadata = {
        "run_id": args.run_id,
        "mode": "codex-single",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "created",
    }
    (run_dir / "run.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
