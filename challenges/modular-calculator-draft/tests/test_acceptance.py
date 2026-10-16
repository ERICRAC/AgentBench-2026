"""Draft independent acceptance suite. No model calls; never a sandbox itself."""

import argparse
import ast
import copy
import importlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

SOLUTION = None


def load_modules(directory):
    """Use normal imports: dataclasses and sibling imports retain their semantics.

    One fresh verifier process per candidate. Never reuse sys.modules between
    solutions; calibration also launches separate processes.
    """
    sys.path.insert(0, str(directory))
    return importlib.import_module('engine'), importlib.import_module('presentation')


class Acceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine, cls.presentation = load_modules(SOLUTION)

    def rejected(self, function, *args):
        with self.assertRaises(ValueError) as caught:
            function(*args)
        self.assertTrue(str(caught.exception).strip())

    def numeric(self, actual, expected):
        self.assertIs(type(actual), float)
        self.assertTrue(math.isfinite(actual))
        self.assertTrue(math.isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9))

    def cli(self, folder, *args):
        return subprocess.run([sys.executable, '-B', str(SOLUTION / 'cli.py'), *map(str, args)],
                              cwd=folder, text=True, capture_output=True, timeout=10)

    def test_M01_deliverables_and_static_constraints(self):
        for name in ('engine.py', 'presentation.py', 'cli.py', 'README.md'):
            with self.subTest(file=name):
                self.assertTrue((SOLUTION / name).is_file())
        for name in ('engine.py', 'presentation.py', 'cli.py'):
            tree = ast.parse((SOLUTION / name).read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    function = node.func
                    called = function.id if isinstance(function, ast.Name) else getattr(function, 'attr', '')
                    self.assertNotIn(called, {'eval', 'exec', 'compile', '__import__'})
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    roots = ([item.name.split('.')[0] for item in node.names] if isinstance(node, ast.Import)
                             else [(node.module or '').split('.')[0]])
                    self.assertFalse(set(roots) - sys.stdlib_module_names - {'engine', 'presentation'})

    def test_M02_arithmetic(self):
        for expression, expected in [('2+3', 5), ('8-3', 5), ('2*3', 6), ('9/2', 4.5),
                                     ('2+3*4', 14), ('(2+3)*4', 20), ('2^3^2', 512),
                                     ('-2^2', -4), ('2^-2', .25), ('+2', 2)]:
            with self.subTest(expression=expression):
                self.numeric(self.engine.evaluate(expression), expected)

    def test_M03_functions_variables(self):
        for expression, expected in [('sin(pi/2)', 1), ('cos(0)+tan(0)', 1),
                                     ('asin(1)+acos(1)+atan(0)', math.pi/2),
                                     ('sqrt(9)+ln(e)+log10(100)', 6),
                                     ('exp(0)+abs(-3)', 4), ('1e-3+2E2', 200.001)]:
            with self.subTest(expression=expression):
                self.numeric(self.engine.evaluate(expression), expected)
        self.numeric(self.engine.evaluate('x^2', {'x': 3}), 9)
        for expression in ['x', 'unknown', 'pi.real', 'sin(1,2)', '__import__("os")', '[1]', '1<2']:
            with self.subTest(rejected=expression):
                self.rejected(self.engine.evaluate, expression)

    def test_M04_errors_and_bounds(self):
        for expression in ['', ' ', '2+', '1/0', 'sqrt(-1)', 'exp(1000)', '(-1)^0.5',
                           '1e999', '1' + ' '*4096, '('*65+'1'+')'*65]:
            with self.subTest(expression=expression[:30]):
                self.rejected(self.engine.evaluate, expression)
        for variables in [{'x': True}, {'x': float('nan')}, {'y': 1}, [], {'x': '2'}]:
            with self.subTest(variables=variables):
                self.rejected(self.engine.evaluate, '1', variables)
        self.rejected(self.engine.evaluate, 1)
        self.numeric(self.engine.evaluate('+'.join(['1']*500)), 500)
        self.numeric(self.engine.evaluate('('*32+'1'+')'*32), 1)

    def test_M05_sampling(self):
        points = self.engine.sample_curve('1/x', -1, 1, 3)
        self.assertEqual(len(points), 3)
        self.assertEqual(points[1], (0, None))
        self.numeric(float(points[0][0]), -1)
        self.numeric(points[0][1], -1)
        self.numeric(float(points[-1][0]), 1)
        self.numeric(points[-1][1], 1)
        self.assertEqual(len(self.engine.sample_curve('x', 0, 1)), 201)
        self.assertTrue(all(y is None for x, y in self.engine.sample_curve('sqrt(-1)', 0, 1, 3)))
        for args in [('x', 1, 1, 3), ('x', 0, 1, 1), ('x', 0, 1, 1002),
                     ('x', 0, 1, True), ('x', 0, float('inf'), 3), ('2+', 0, 1, 3)]:
            with self.subTest(args=args):
                self.rejected(self.engine.sample_curve, *args)

    def svg(self, points, title='A < B & "C"'):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'curve.svg'
            output.write_text('old')
            self.presentation.write_svg(points, output, title)
            root = ET.parse(output).getroot()
        self.assertEqual(root.tag, '{http://www.w3.org/2000/svg}svg')
        self.assertGreater(float(root.attrib['width']), 0)
        self.assertGreater(float(root.attrib['height']), 0)
        self.assertIn(title, ''.join(root.itertext()))
        box = list(map(float, root.attrib['viewBox'].replace(',', ' ').split()))
        self.assertEqual(len(box), 4)
        self.assertTrue(all(math.isfinite(v) for v in box))
        self.assertGreater(box[2], 0)
        self.assertGreater(box[3], 0)
        segments = []
        for element in root.iter():
            self.assertNotIn(element.tag.split('}')[-1].lower(), {'script', 'foreignobject', 'image', 'use'})
            self.assertFalse(any(k.lower().startswith('on') or k.endswith('href') for k in element.attrib))
            if element.get('data-series') != 'curve':
                continue
            tag = element.tag.split('}')[-1]
            self.assertIn(tag, {'polyline', 'path'})
            coordinates = element.get('points') if tag == 'polyline' else element.get('d')
            if tag == 'path':
                self.assertEqual(coordinates.count('M'), 1)
                coordinates = coordinates.replace('M', ' ').replace('L', ' ')
            values = list(map(float, re.split(r'[\s,]+', coordinates.strip())))
            self.assertEqual(len(values) % 2, 0)
            self.assertTrue(all(math.isfinite(v) for v in values))
            segment = list(zip(values[::2], values[1::2]))
            for x, y in segment:
                self.assertTrue(box[0] <= x <= box[0]+box[2])
                self.assertTrue(box[1] <= y <= box[1]+box[3])
            segments.append(segment)
        return segments

    def test_M06_svg(self):
        segments = self.svg([(0, 0), (1, 1), (2, None), (3, 0), (4, 1)])
        self.assertEqual(len(segments), 2)
        self.assertEqual([len(s) for s in segments], [2, 2])
        for segment in segments:
            self.assertLess(segment[0][0], segment[1][0])
            self.assertGreater(segment[0][1], segment[1][1])
        self.assertTrue(self.svg([(0, 1), (1, 1)]))
        self.assertEqual(self.svg([]), [])
        self.assertEqual(self.svg([(0, None), (1, None)]), [])

    def test_M07_batches(self):
        jobs = [{'expression': '2+3'}, {'expression': '1/0'}, {'expression': 'x^2', 'variables': {'x': 3}},
                {'expression': ''}, {'expression': '2+'}, {'expression': '7'}]
        before = copy.deepcopy(jobs)
        result = self.presentation.run_batch(jobs)
        self.assertEqual(jobs, before)
        self.assertEqual(len(result), len(jobs))
        for index, expected in [(0, 5), (2, 9), (5, 7)]:
            self.assertEqual(set(result[index]), {'ok', 'value'})
            self.assertIs(result[index]['ok'], True)
            self.numeric(result[index]['value'], expected)
        for index in (1, 3, 4):
            self.assertEqual(set(result[index]), {'ok', 'error'})
            self.assertIs(result[index]['ok'], False)
            self.assertIsInstance(result[index]['error'], str)
            self.assertTrue(result[index]['error'].strip())
        self.assertEqual(self.presentation.run_batch([]), [])
        for jobs in [None, {}, [{}], [{'expression': 2}], [{'expression': '1', 'extra': 1}],
                     [{'expression': '1', 'variables': {'x': True}}], [{'expression': '1'}]*101]:
            with self.subTest(invalid=str(jobs)[:50]):
                self.rejected(self.presentation.run_batch, jobs)

    def test_M08_cli_errors(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'in.json', Path(folder)/'out.json'
            for contents in ['{', '{}', '[{}]']:
                source.write_text(contents)
                output.write_text('preserve')
                result = self.cli(folder, 'batch', source, output)
                self.assertEqual(result.returncode, 2)
                self.assertTrue(result.stderr.strip())
                self.assertNotIn('Traceback', result.stderr)
                self.assertEqual(output.read_text(), 'preserve')
            for args in [('unknown',), ('batch', 'missing.json', output),
                         ('plot', 'x', output, '--min', '1', '--max', '0')]:
                result = self.cli(folder, *args)
                self.assertEqual(result.returncode, 2)
                self.assertTrue(result.stderr.strip())
                self.assertNotIn('Traceback', result.stderr)
            self.assertEqual(self.cli(folder, '--help').returncode, 0)

    def test_M09_integration(self):
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/'in.json', Path(folder)/'out.json'
            source.write_text(json.dumps([{'expression': 'sin(pi/2)'}, {'expression': '1/0'}, {'expression': 'x+1', 'variables': {'x': 4}}]))
            result = self.cli(folder, 'batch', source, output)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(output.read_text())
            self.numeric(data[0]['value'], 1)
            self.assertIs(data[1]['ok'], False)
            self.numeric(data[2]['value'], 5)
            svg = Path(folder)/'curve.svg'
            result = self.cli(folder, 'plot', '1/x', svg, '--min', '-1', '--max', '1', '--samples', '5')
            self.assertEqual(result.returncode, 0, result.stderr)
            root = ET.parse(svg).getroot()
            self.assertEqual(len([e for e in root.iter() if e.get('data-series') == 'curve']), 2)

    def test_M10_documentation(self):
        text = (SOLUTION/'README.md').read_text().lower()
        for token in ('engine', 'presentation', 'cli', 'evaluate', 'sample_curve', 'write_svg', 'run_batch',
                      'batch', 'plot', '4096', '64', '1001', '100', 'expression', 'variables'):
            with self.subTest(documented=token):
                self.assertIn(token, text)
        for function in (self.engine.evaluate, self.engine.sample_curve,
                         self.presentation.write_svg, self.presentation.run_batch):
            self.assertTrue(function.__doc__ and function.__doc__.strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--solution', type=Path, required=True)
    args = parser.parse_args()
    SOLUTION = args.solution.resolve(strict=True)
    unittest.main(argv=[sys.argv[0]], verbosity=2)
