#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CHALLENGES = {
    "calculator": ROOT / "challenges" / "calculator" / "tests",
    "scientific-calculator": ROOT / "challenges" / "scientific-calculator" / "tests",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Vérifie une solution AgentBench.")
    parser.add_argument("--solution", required=True, type=Path)
    parser.add_argument(
        "--challenge",
        choices=sorted(CHALLENGES),
        default="calculator",
        help="Suite de tests à utiliser (calculator par défaut).",
    )
    args = parser.parse_args()

    solution_dir = args.solution.resolve()
    if not solution_dir.is_dir():
        parser.error(f"Dossier de solution absent : {solution_dir}")

    environment = os.environ.copy()
    environment["AGENTBENCH_SOLUTION_DIR"] = str(solution_dir)
    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(CHALLENGES[args.challenge]),
            "-v",
        ],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
