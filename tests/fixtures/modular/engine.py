"""Calibration implementation only: never distribute to benchmark candidates."""

import ast
from dataclasses import dataclass
import math
import operator

FUNCTIONS = {name: getattr(math, name) for name in ('sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'log10', 'exp')}
FUNCTIONS.update(ln=math.log, abs=abs)
OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
       ast.Div: operator.truediv, ast.Pow: operator.pow}


def variables_checked(variables):
    if variables is None:
        return {}
    if not isinstance(variables, dict) or set(variables) - {'x'}:
        raise ValueError('invalid variables')
    for value in variables.values():
        if type(value) not in (int, float) or not math.isfinite(value):
            raise ValueError('invalid variable value')
    return variables


@dataclass
class Expression:
    """Dataclass intentionally exercises correct sys.modules registration."""

    root: ast.AST

    @classmethod
    def parse(cls, text):
        if not isinstance(text, str) or not text.strip() or len(text) > 4096:
            raise ValueError('invalid expression size')
        depth = 0
        for character in text:
            depth += (character == '(') - (character == ')')
            if depth > 64:
                raise ValueError('parenthesis limit')
        try:
            root = ast.parse(text.strip().replace('^', '**'), mode='eval').body
        except (SyntaxError, RecursionError) as error:
            raise ValueError('syntax') from error
        for node in ast.walk(root):
            if not isinstance(node, (ast.Constant, ast.BinOp, ast.UnaryOp, ast.Name, ast.Call,
                                     ast.Load, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.UAdd, ast.USub)):
                raise ValueError('forbidden syntax')
            if isinstance(node, ast.Name) and node.id not in {*FUNCTIONS, 'x', 'pi', 'e'}:
                raise ValueError('forbidden name')
            if isinstance(node, ast.Call) and (not isinstance(node.func, ast.Name)
                                              or node.func.id not in FUNCTIONS or len(node.args) != 1 or node.keywords):
                raise ValueError('invalid function')
        return cls(root)

    def value(self, variables):
        def walk(node):
            if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                return node.value
            if isinstance(node, ast.Name):
                return {'pi': math.pi, 'e': math.e, **variables}[node.id]
            if isinstance(node, ast.UnaryOp):
                return (-1 if isinstance(node.op, ast.USub) else 1) * walk(node.operand)
            if isinstance(node, ast.BinOp):
                return OPS[type(node.op)](walk(node.left), walk(node.right))
            if isinstance(node, ast.Call):
                return FUNCTIONS[node.func.id](walk(node.args[0]))
            raise ValueError('invalid value')
        try:
            result = float(walk(self.root))
            if not math.isfinite(result):
                raise ValueError('non-finite result')
            return result
        except (ArithmeticError, TypeError, KeyError, RecursionError) as error:
            raise ValueError('domain or complexity') from error


def evaluate(expression, variables=None):
    """Return finite expression value; invalid input or domain raises ValueError."""
    variables = variables_checked(variables)
    return Expression.parse(expression).value(variables)


def sample_curve(expression, x_min, x_max, samples=201):
    """Return regular (x,y) pairs; invalid parameters raise ValueError, gaps use None."""
    if (any(type(v) not in (int, float) or not math.isfinite(v) for v in (x_min, x_max))
            or x_min >= x_max or type(samples) is not int or not 2 <= samples <= 1001):
        raise ValueError('invalid sampling')
    parsed = Expression.parse(expression)
    points = []
    for index in range(samples):
        x = x_min + (x_max-x_min)*index/(samples-1)
        try:
            y = parsed.value({'x': x})
        except ValueError:
            y = None
        points.append((x, y))
    return points
