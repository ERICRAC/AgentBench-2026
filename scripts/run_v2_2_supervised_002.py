#!/usr/bin/env python3
"""Authorised fresh attempt 002; reuse the unchanged frozen pilot engine."""
import argparse
import json
from pathlib import Path
import run_v2_2_supervised as pilot


def main():
    pilot.RUN_ID = "astra-medium-core-v2-2-supervised-002"
    pilot.MANIFEST = pilot.relay.ROOT / "governance/v2-2-supervised-002.json"
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prepare", action="store_true")
    mode.add_argument("--run", type=Path)
    args = parser.parse_args()
    print(pilot.prepare() if args.prepare else json.dumps(pilot.run(args.run), ensure_ascii=False))


if __name__ == "__main__":
    main()
