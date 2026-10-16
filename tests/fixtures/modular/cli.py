"""Calibration CLI only; not visible to future candidates."""

import argparse
import json
from pathlib import Path
import sys
import engine
import presentation


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='command', required=True)
    batch = sub.add_parser('batch')
    batch.add_argument('input')
    batch.add_argument('output')
    plot = sub.add_parser('plot')
    plot.add_argument('expression')
    plot.add_argument('output')
    plot.add_argument('--min', type=float, required=True)
    plot.add_argument('--max', type=float, required=True)
    plot.add_argument('--samples', type=int, default=201)
    args = parser.parse_args()
    try:
        if args.command == 'batch':
            results = presentation.run_batch(json.loads(Path(args.input).read_text()))
            Path(args.output).write_text(json.dumps(results, allow_nan=False))
        else:
            points = engine.sample_curve(args.expression, args.min, args.max, args.samples)
            presentation.write_svg(points, args.output, args.expression)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
