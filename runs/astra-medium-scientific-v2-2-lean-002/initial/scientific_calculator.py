"""Safe real expression calculator and standalone SVG plotting (Python 3.10+)."""

import math
import re
from html import escape


_FUNCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sqrt": math.sqrt, "ln": math.log, "log10": math.log10,
    "exp": math.exp, "abs": abs,
}
_CONSTANTS = {"pi": math.pi, "e": math.e}
_TOKEN = re.compile(
    r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
    r"|[A-Za-z_][A-Za-z_0-9]*|[+*/^()\-]"
)


def _finite(value):
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Une valeur réelle finie est requise") from error
    if not math.isfinite(result):
        raise ValueError("Résultat non fini")
    return result


class _Parser:
    """Recursive descent: sum -> product -> unary -> power -> atom."""

    def __init__(self, expression):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError("Expression vide ou invalide")
        self.tokens = []
        position = 0
        while position < len(expression):
            if expression[position].isspace():
                position += 1
                continue
            match = _TOKEN.match(expression, position)
            if match is None:
                raise ValueError(f"Caractère interdit à la position {position + 1}")
            self.tokens.append(match.group())
            position = match.end()
        self.tokens.append("")
        self.index = 0

    def take(self):
        token = self.tokens[self.index]
        if token:
            self.index += 1
        return token

    def peek(self):
        return self.tokens[self.index]

    def parse(self):
        node = self.sum()
        if self.peek():
            raise ValueError(f"Symbole inattendu : {self.peek()}")
        return node

    def sum(self):
        node = self.product()
        while self.peek() in ("+", "-"):
            operator = self.take()
            node = (operator, node, self.product())
        return node

    def product(self):
        node = self.unary()
        while self.peek() in ("*", "/"):
            operator = self.take()
            node = (operator, node, self.unary())
        return node

    def unary(self):
        if self.peek() in ("+", "-"):
            return ("unary", self.take(), self.unary())
        return self.power()

    def power(self):
        node = self.atom()
        if self.peek() == "^":
            self.take()
            node = ("^", node, self.unary())
        return node

    def atom(self):
        token = self.take()
        if token == "(":
            node = self.sum()
            if self.take() != ")":
                raise ValueError("Parenthèse fermante attendue")
            return node
        if token in _FUNCTIONS:
            if self.take() != "(":
                raise ValueError("Une fonction exige des parenthèses")
            node = self.sum()
            if self.take() != ")":
                raise ValueError("Parenthèse fermante attendue")
            return ("call", token, node)
        if token in _CONSTANTS:
            return ("number", _CONSTANTS[token])
        if token == "x":
            return ("variable",)
        if token and (token[0].isdigit() or token[0] == "."):
            return ("number", _finite(token))
        raise ValueError(f"Nombre, fonction ou variable attendu : {token!r}")


def _parse(expression):
    try:
        return _Parser(expression).parse()
    except RecursionError as error:
        raise ValueError("Expression trop complexe") from error


def _calculate(node, variables):
    kind = node[0]
    if kind == "number":
        return node[1]
    if kind == "variable":
        if variables is None or "x" not in variables:
            raise ValueError("La variable x nécessite une valeur")
        return _finite(variables["x"])
    if kind == "unary":
        value = _calculate(node[2], variables)
        return -value if node[1] == "-" else value
    if kind == "call":
        return _finite(_FUNCTIONS[node[1]](_calculate(node[2], variables)))
    left = _calculate(node[1], variables)
    right = _calculate(node[2], variables)
    if kind == "+":
        result = left + right
    elif kind == "-":
        result = left - right
    elif kind == "*":
        result = left * right
    elif kind == "/":
        result = left / right
    else:
        result = math.pow(left, right)
    return _finite(result)


def _run(node, variables):
    try:
        return _calculate(node, variables)
    except (OverflowError, RecursionError) as error:
        raise ValueError("Résultat hors domaine ou expression trop complexe") from error


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Evaluate only the documented grammar; never execute Python input."""
    return _run(_parse(expression), variables)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Include both endpoints, marking undefined samples with None."""
    x_min, x_max = _finite(x_min), _finite(x_max)
    if x_min >= x_max:
        raise ValueError("Les bornes doivent vérifier x_min < x_max")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("Il faut au moins deux échantillons entiers")
    node = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        # Convex interpolation avoids overflow in x_max - x_min.
        x = x_min * (1 - fraction) + x_max * fraction
        if index == 0:
            x = x_min
        elif index == samples - 1:
            x = x_max
        try:
            y = _run(node, {"x": x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Write a passive SVG; missing/nonfinite coordinates split polylines."""
    cleaned = []
    for x, y in points:
        try:
            cleaned.append((_finite(x), _finite(y)))
        except ValueError:
            cleaned.append(None)
    valid = [point for point in cleaned if point is not None]
    if not valid:
        raise ValueError("Aucun point fini à tracer")
    x_low = min(point[0] for point in valid)
    x_high = max(point[0] for point in valid)
    y_low = min(point[1] for point in valid)
    y_high = max(point[1] for point in valid)

    def fraction(value, low, high):
        if low == high:
            return 0.5
        scale = max(abs(low), abs(high))
        return (value / scale - low / scale) / (high / scale - low / scale)

    def px(x):
        return 60 + 700 * fraction(x, x_low, x_high)

    def py(y):
        return 440 - 380 * fraction(y, y_low, y_high)

    # If zero is outside the data range, place that axis at the nearest edge.
    axis_x = px(min(max(0.0, x_low), x_high))
    axis_y = py(min(max(0.0, y_low), y_high))
    safe_title = escape(str(title), quote=True)
    # XML 1.0 does not permit most control characters, even in escaped text.
    safe_title = "".join(c for c in safe_title if c in "\t\n\r" or
                         0x20 <= ord(c) <= 0xD7FF or
                         0xE000 <= ord(c) <= 0xFFFD or
                         0x10000 <= ord(c) <= 0x10FFFF)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">',
        f'<title>{safe_title}</title>',
        '<rect width="800" height="500" fill="white"/>',
        f'<text x="400" y="30" text-anchor="middle" font-family="sans-serif" font-size="18">{safe_title}</text>',
        f'<line x1="60" y1="{axis_y:.6f}" x2="760" y2="{axis_y:.6f}" stroke="#555"/>',
        f'<line x1="{axis_x:.6f}" y1="60" x2="{axis_x:.6f}" y2="440" stroke="#555"/>',
    ]
    segment = []

    def flush():
        if len(segment) == 1:
            x, y = segment[0]
            lines.append(f'<circle cx="{x:.6f}" cy="{y:.6f}" r="2" fill="#1565c0"/>')
        elif segment:
            coordinates = " ".join(f"{x:.6f},{y:.6f}" for x, y in segment)
            lines.append(f'<polyline points="{coordinates}" fill="none" stroke="#1565c0" stroke-width="2"/>')
        segment.clear()

    for point in cleaned:
        if point is None:
            flush()
        else:
            segment.append((px(point[0]), py(point[1])))
    flush()
    lines.append('</svg>')
    with open(output_path, "w", encoding="utf-8") as output:
        output.write("\n".join(lines) + "\n")


_HELP = """Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Tracé : plot expression; borne_min; borne_max; fichier.svg
Exemple : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit."""


def main() -> None:
    """Interactive session with successful operations only in history."""
    history = []
    while True:
        try:
            command = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not command:
            continue
        if command in ("quit", "exit"):
            break
        if command == "help":
            print(_HELP)
            continue
        if command == "history":
            print("\n".join(history) if history else "Historique vide")
            continue
        if command == "clear":
            history.clear()
            print("Historique effacé")
            continue
        try:
            if command.split(maxsplit=1)[0] == "plot":
                parts = command[4:].split(";")
                if len(parts) != 4 or not all(part.strip() for part in parts):
                    raise ValueError("Syntaxe : plot expression; borne_min; borne_max; fichier.svg")
                expression, lower, upper, path = (part.strip() for part in parts)
                points = sample_curve(expression, evaluate(lower), evaluate(upper))
                write_svg(points, path, expression)
                print(f"Courbe enregistrée dans {path}")
            else:
                print(evaluate(command))
            history.append(command)
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur : {error}")
        except KeyboardInterrupt:
            print("Opération interrompue")


if __name__ == "__main__":
    main()
