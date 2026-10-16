"""Calibrate the draft verifier on dataclasses, sibling imports and mutations.

The fixture is not a measured candidate or a claim of exhaustive correctness.
Never expose fixtures or prior submissions to an experimental candidate.
"""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / 'challenges/modular-calculator-draft/tests/test_acceptance.py'
FIXTURE = ROOT / 'tests/fixtures/modular'
DOCUMENTATION = '''Calibration only. engine presentation cli evaluate sample_curve
write_svg run_batch batch plot 4096 64 1001 100 expression variables
'''


class Calibration(unittest.TestCase):
    def verify(self, mutation=None):
        with tempfile.TemporaryDirectory() as folder:
            solution = Path(folder)/'solution'
            shutil.copytree(FIXTURE, solution, ignore=shutil.ignore_patterns('__pycache__'))
            (solution/'README.md').write_text(DOCUMENTATION)
            if mutation:
                name, old, new = mutation
                target = solution/name
                source = target.read_text()
                self.assertIn(old, source)
                target.write_text(source.replace(old, new))
            return subprocess.run([sys.executable, '-B', str(SUITE), '--solution', str(solution)],
                                  cwd=folder, capture_output=True, text=True, timeout=30)

    def test_dataclass_and_sibling_imports_pass(self):
        result = self.verify()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Ran 10 tests', result.stderr)

    def test_equivalent_path_renderer_passes(self):
        result = self.verify(
            ('presentation.py', "'polyline', {'data-series': 'curve', 'fill': 'none', 'stroke': 'blue',\n                                               'points': ' '.join(f'{x},{y}' for x, y in segment)",
             "'path', {'data-series': 'curve', 'fill': 'none', 'stroke': 'blue',\n                                               'd': 'M' + ' L'.join(f'{x} {y}' for x, y in segment)"))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_injected_faults_are_detected(self):
        mutations = [
            ('cli.py', 'import argparse', 'import argparse\n\ndef forbidden():\n    return compile("", "", "exec")', 'M01'),
            ('engine.py', 'ast.Add: operator.add', 'ast.Add: operator.sub', 'M02'),
            ('engine.py', "{'pi': math.pi, 'e': math.e, **variables}", "{'pi': 0, 'e': math.e, **variables}", 'M03'),
            ('engine.py', 'len(text) > 4096', 'len(text) > 99999', 'M04'),
            ('engine.py', 'y = None', 'y = 0.0', 'M05'),
            ('presentation.py', 'segments.append(segment)\n                segment = []', 'pass', 'M06'),
            ('presentation.py', "'ok': False", "'ok': True", 'M07'),
            ('cli.py', 'return 2', 'return 0', 'M08'),
            ('cli.py', 'args.min, args.max, args.samples', 'args.min, args.max, 2', 'M09'),
            ('README.md', 'run_batch', 'removed', 'M10'),
        ]
        for name, old, new, group in mutations:
            with self.subTest(group=group):
                result = self.verify((name, old, new))
                self.assertNotEqual(result.returncode, 0)
                self.assertRegex(result.stderr, rf'FAIL: test_{group}')


if __name__ == '__main__':
    unittest.main()
