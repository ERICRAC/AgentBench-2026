"""Contrôles candidats reproductibles des corrections SA-03, hors suite officielle."""
import contextlib
import io
import math
import unittest
from unittest.mock import patch

import scientific_calculator as calculator


class FinalChecks(unittest.TestCase):
    def test_long_and_deep_valid_expressions(self):
        cases = [('+'.join(['1'] * 5001), 5001.0),
                 ('(' * 3000 + '1' + ')' * 3000, 1.0),
                 ('-' * 3001 + '2^2', -4.0),
                 ('abs(' * 1500 + '-1' + ')' * 1500, 1.0),
                 ('^'.join(['1'] * 3000), 1.0)]
        for expression, expected in cases:
            with self.subTest(length=len(expression)):
                self.assertEqual(calculator.evaluate(expression), expected)

    def test_grammar_preserved(self):
        for expression, expected in [('2^3^2', 512.0), ('-2^2', -4.0),
                                     ('2^-2', 0.25), ('2^-2^2', 0.0625),
                                     ('10-3-2', 5.0), ('8/2/2', 2.0),
                                     ('sin(cos(0))', math.sin(1)),
                                     ('(-2)^2', 4.0), ('.5+5.+1e-2', 5.51)]:
            with self.subTest(expression=expression):
                self.assertAlmostEqual(calculator.evaluate(expression), expected)
        for expression in ['', '1+', 'sin()', '2**3', 'sin(1,2)', '2pi',
                           'x.y', 'sin(0)(1)', '(' * 3000 + '1',
                           '1e+', 'foo(1)', '1 2', '1)', 'sqrt(-1)']:
            with self.subTest(expression=expression[:30]):
                with self.assertRaises(ValueError):
                    calculator.evaluate(expression)
        with self.assertRaises(ZeroDivisionError):
            calculator.evaluate('1/0')
        self.assertEqual(calculator.sample_curve('sqrt(-1)', -1, 1, 3),
                         [(-1.0, None), (0.0, None), (1.0, None)])

    def test_terminal_and_history(self):
        output = io.StringIO()
        path = 'courbe\x1b[31m.svg'
        commands = [f'plot x; 0; 1; {path}', 'history', '1/0', '2+2', 'quit']
        with patch('builtins.input', side_effect=commands), \
                patch.object(calculator, 'write_svg') as writer, \
                contextlib.redirect_stdout(output):
            calculator.main()
        self.assertEqual(writer.call_args.args[1], path)
        self.assertNotIn('\x1b', output.getvalue())
        self.assertIn(r'courbe\x1b[31m.svg', output.getvalue())
        self.assertIn('1. plot x;', output.getvalue())
        self.assertIn('Erreur :', output.getvalue())
        self.assertIn('4.0', output.getvalue())

    def test_failed_channels(self):
        for error in [OSError('lecture indisponible'), MemoryError('mémoire')]:
            stderr = io.StringIO()
            with patch('builtins.input', side_effect=error), \
                    contextlib.redirect_stderr(stderr):
                calculator.main()
            self.assertIn('Erreur :', stderr.getvalue())
        for command in ['help', 'history', 'clear']:
            stderr = io.StringIO()
            with patch('builtins.input', return_value=command), \
                    patch('sys.stdout.write', side_effect=OSError('sortie')), \
                    contextlib.redirect_stderr(stderr):
                calculator.main()
            self.assertIn('Erreur :', stderr.getvalue())
        with patch('builtins.input', side_effect=OSError('lecture')), \
                patch('sys.stderr.write', side_effect=OSError('diagnostic')):
            calculator.main()


if __name__ == '__main__':
    unittest.main()
