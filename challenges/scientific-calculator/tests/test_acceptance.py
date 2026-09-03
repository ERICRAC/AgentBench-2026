import ast
import importlib.util
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET


SOLUTION_DIR = Path(os.environ["AGENTBENCH_SOLUTION_DIR"]).resolve()
CALCULATOR_FILE = SOLUTION_DIR / "scientific_calculator.py"


def load_calculator():
    spec = importlib.util.spec_from_file_location(
        "candidate_scientific_calculator", CALCULATOR_FILE
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Impossible de charger scientific_calculator.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScientificCalculatorAcceptanceTests(unittest.TestCase):
    def test_required_files_and_documentation_exist(self):
        self.assertTrue(CALCULATOR_FILE.is_file(), "scientific_calculator.py est absent")
        readme = SOLUTION_DIR / "README.md"
        self.assertTrue(readme.is_file(), "README.md est absent")
        documentation = readme.read_text(encoding="utf-8").lower()
        for expected in ("evaluate", "plot", "svg", "sin", "history"):
            self.assertIn(expected, documentation)

    def test_only_standard_library_and_no_dynamic_execution(self):
        tree = ast.parse(CALCULATOR_FILE.read_text(encoding="utf-8"))
        forbidden_calls = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in {"eval", "exec", "compile"}
        }
        self.assertFalse(forbidden_calls, f"Appels interdits : {sorted(forbidden_calls)}")

        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".", 1)[0])
        external = imported_roots - sys.stdlib_module_names
        self.assertFalse(external, f"Dépendances externes détectées : {sorted(external)}")

    def test_operator_precedence_parentheses_and_unary_signs(self):
        calculator = load_calculator()
        cases = (
            ("2 + 3 * 4", 14.0),
            ("(2 + 3) * 4", 20.0),
            ("2 ^ 3 ^ 2", 512.0),
            ("-2 ^ 2", -4.0),
            ("2 ^ -2", 0.25),
        )
        for expression, expected in cases:
            with self.subTest(expression=expression):
                result = calculator.evaluate(expression)
                self.assertIs(type(result), float)
                self.assertAlmostEqual(result, expected)

    def test_constants_functions_and_scientific_notation(self):
        calculator = load_calculator()
        cases = (
            ("sin(pi / 2)", 1.0),
            ("cos(0) + tan(0)", 1.0),
            ("asin(1) + acos(1) + atan(0)", math.pi / 2),
            ("sqrt(9) + ln(e) + log10(100)", 6.0),
            ("exp(0) + abs(-3)", 4.0),
            ("1e-3 + 2E2", 200.001),
        )
        for expression, expected in cases:
            with self.subTest(expression=expression):
                self.assertAlmostEqual(calculator.evaluate(expression), expected)

    def test_variables_and_unsafe_or_unknown_names(self):
        calculator = load_calculator()
        self.assertEqual(calculator.evaluate("x ^ 2 + 1", {"x": 3}), 10.0)
        for expression in ("x + 1", "unknown(2)", "__import__('os')", "pi.real"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculator.evaluate(expression)

    def test_syntax_domain_and_arithmetic_errors(self):
        calculator = load_calculator()
        for expression in ("", "2 +", "sqrt(-1)", "ln(0)", "exp(10000)"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculator.evaluate(expression)
        with self.assertRaises(ZeroDivisionError):
            calculator.evaluate("1 / 0")

    def test_curve_sampling_and_discontinuities(self):
        calculator = load_calculator()
        points = calculator.sample_curve("x ^ 2", -2, 2, samples=5)
        self.assertEqual(len(points), 5)
        self.assertEqual(points[0], (-2.0, 4.0))
        self.assertEqual(points[-1], (2.0, 4.0))
        self.assertEqual(points[2], (0.0, 0.0))

        discontinuous = calculator.sample_curve("1 / x", -1, 1, samples=3)
        self.assertEqual(discontinuous[1], (0.0, None))

        for arguments in (("x", 1, 1, 3), ("x", 2, 1, 3), ("x", 0, 1, 1)):
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    calculator.sample_curve(*arguments)

    def test_svg_is_valid_safe_and_contains_axes_and_curve(self):
        calculator = load_calculator()
        points = calculator.sample_curve("sin(x)", -math.pi, math.pi, samples=21)
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "curve.svg"
            calculator.write_svg(points, str(output), title="sin(x) < test & trace")
            raw_svg = output.read_text(encoding="utf-8")
            root = ET.fromstring(raw_svg)

        self.assertTrue(root.tag.endswith("svg"))
        tags = [element.tag.rsplit("}", 1)[-1] for element in root.iter()]
        self.assertGreaterEqual(tags.count("line"), 2, "Les axes SVG sont absents")
        self.assertTrue(
            "polyline" in tags or "path" in tags,
            "La courbe SVG est absente",
        )
        self.assertNotIn("<script", raw_svg.lower())
        self.assertNotIn("javascript:", raw_svg.lower())
        self.assertNotIn("< test & trace", raw_svg)

        with self.assertRaises(ValueError):
            calculator.write_svg([(0.0, None)], str(output))

    def test_cli_recovers_plots_tracks_history_and_exits(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            session = (
                "2 + 3 * 4\n"
                "sqrt(-1)\n"
                "plot sin(x); -pi; pi; curve.svg\n"
                "history\n"
                "clear\n"
                "history\n"
                "quit\n"
            )
            completed = subprocess.run(
                [sys.executable, str(CALCULATOR_FILE)],
                input=session,
                text=True,
                capture_output=True,
                timeout=15,
                cwd=temporary_directory,
                check=False,
            )
            curve = Path(temporary_directory) / "curve.svg"
            combined = completed.stdout + completed.stderr
            curve_created = curve.is_file()

        self.assertEqual(completed.returncode, 0, combined)
        self.assertNotIn("Traceback", combined)
        self.assertIn("14", combined)
        self.assertRegex(combined.lower(), r"erreur|error|domaine|domain")
        self.assertIn("sin(x)", combined)
        self.assertTrue(curve_created, "La commande plot n'a pas créé le SVG")


if __name__ == "__main__":
    unittest.main()
