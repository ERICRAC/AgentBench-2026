#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
TEST_DIR = ROOT / "challenges" / "calculator" / "tests"


def main() -> int:
    parser = argparse.ArgumentParser(description="Vérifie une solution Calculator.")
    parser.add_argument("--solution", required=True, type=Path)
    args = parser.parse_args()

    solution_dir = args.solution.resolve()
    if not solution_dir.is_dir():
        parser.error(f"Dossier de solution absent : {solution_dir}")

    environment = os.environ.copy()
    environment["AGENTBENCH_SOLUTION_DIR"] = str(solution_dir)
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(TEST_DIR), "-v"],
        cwd=ROOT,
        env=environment,
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
