import ast
import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import unittest


SOLUTION_DIR = Path(os.environ["AGENTBENCH_SOLUTION_DIR"]).resolve()
CALCULATOR_FILE = SOLUTION_DIR / "calculator.py"


def load_calculator():
    spec = importlib.util.spec_from_file_location("candidate_calculator", CALCULATOR_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError("Impossible de charger calculator.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CalculatorAcceptanceTests(unittest.TestCase):
    def test_required_files_exist(self):
        self.assertTrue(CALCULATOR_FILE.is_file(), "calculator.py est absent")
        self.assertTrue((SOLUTION_DIR / "README.md").is_file(), "README.md est absent")

    def test_forbidden_dynamic_execution_is_absent(self):
        tree = ast.parse(CALCULATOR_FILE.read_text(encoding="utf-8"))
        forbidden = {
            node.func.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id in {"eval", "exec"}
        }
        self.assertFalse(forbidden, f"Appels interdits détectés : {sorted(forbidden)}")

    def test_four_operations_and_numeric_variants(self):
        calculator = load_calculator()
        cases = [
            (2, "+", 3, 5),
            (-2, "-", 3, -5),
            (1.5, "*", 2, 3.0),
            (7, "/", 2, 3.5),
        ]
        for left, operator, right, expected in cases:
            with self.subTest(left=left, operator=operator, right=right):
                self.assertEqual(calculator.calculate(left, operator, right), expected)

    def test_invalid_operator(self):
        calculator = load_calculator()
        with self.assertRaises(ValueError):
            calculator.calculate(1, "%", 2)

    def test_division_by_zero(self):
        calculator = load_calculator()
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(1, "/", 0)

    def test_cli_recovers_from_errors_and_exits_cleanly(self):
        session = "2 + 3\n10 / 0\nexpression invalide\n-4 * 2\nquit\n"
        completed = subprocess.run(
            [sys.executable, str(CALCULATOR_FILE)],
            input=session,
            text=True,
            capture_output=True,
            timeout=10,
            cwd=SOLUTION_DIR,
            check=False,
        )
        combined = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0, combined)
        self.assertNotIn("Traceback", combined)
        self.assertIn("5", combined)
        self.assertIn("-8", combined)
        self.assertRegex(combined.lower(), r"erreur|invalide|division")


if __name__ == "__main__":
    unittest.main()
