#!/usr/bin/env python3
"""Safe scientific expression evaluator and self-contained SVG plotter.

The expression language is deliberately small.  It is tokenised and parsed by
this module; input is never interpreted as Python code.
"""

from __future__ import annotations

from html import escape
import math
from pathlib import Path
import re


_NUMBER_RE = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")
_NAME_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


class _Token:
    """Small token record, independent of module-loader registration details."""

    __slots__ = ("kind", "text", "position")

    def __init__(self, kind: str, text: str, position: int) -> None:
        self.kind = kind
        self.text = text
        self.position = position


def _tokenize(expression: str) -> list[_Token]:
    """Turn an expression into tokens from the calculator's closed grammar."""
    tokens: list[_Token] = []
    position = 0
    single_char_tokens = {
        "+": "PLUS",
        "-": "MINUS",
        "*": "STAR",
        "/": "SLASH",
        "^": "CARET",
        "(": "LPAREN",
        ")": "RPAREN",
    }

    while position < len(expression):
        character = expression[position]
        if character.isspace():
            position += 1
            continue

        kind = single_char_tokens.get(character)
        if kind is not None:
            tokens.append(_Token(kind, character, position))
            position += 1
            continue

        number_match = _NUMBER_RE.match(expression, position)
        if number_match is not None:
            text = number_match.group(0)
            tokens.append(_Token("NUMBER", text, position))
            position = number_match.end()
            continue

        name_match = _NAME_RE.match(expression, position)
        if name_match is not None:
            text = name_match.group(0)
            tokens.append(_Token("NAME", text, position))
            position = name_match.end()
            continue

        raise ValueError(
            f"caractère interdit {character!r} à la position {position + 1}"
        )

    tokens.append(_Token("END", "", len(expression)))
    return tokens


_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "abs": abs,
}

_CONSTANTS = {"pi": math.pi, "e": math.e}


def _require_finite(value: float) -> float:
    if not math.isfinite(value):
        raise ValueError("le résultat n'est pas un nombre réel fini")
    return value


class _Parser:
    """Recursive-descent parser which evaluates while parsing."""

    def __init__(self, tokens: list[_Token], variables: dict[str, float] | None):
        self._tokens = tokens
        self._index = 0
        self._variables = variables

    @property
    def _current(self) -> _Token:
        return self._tokens[self._index]

    def _accept(self, kind: str) -> bool:
        if self._current.kind == kind:
            self._index += 1
            return True
        return False

    def _expect(self, kind: str, message: str) -> None:
        if not self._accept(kind):
            raise ValueError(message)

    def parse(self) -> float:
        result = self._expression()
        if self._current.kind != "END":
            token = self._current
            raise ValueError(
                f"élément inattendu {token.text!r} à la position {token.position + 1}"
            )
        return _require_finite(float(result))

    def _expression(self) -> float:
        value = self._term()
        while self._current.kind in ("PLUS", "MINUS"):
            operation = self._current.kind
            self._index += 1
            right = self._term()
            if operation == "PLUS":
                value = value + right
            else:
                value = value - right
            value = _require_finite(value)
        return value

    def _term(self) -> float:
        value = self._unary()
        while self._current.kind in ("STAR", "SLASH"):
            operation = self._current.kind
            self._index += 1
            right = self._unary()
            if operation == "STAR":
                value = value * right
            else:
                if right == 0.0:
                    raise ZeroDivisionError("division par zéro")
                value = value / right
            value = _require_finite(value)
        return value

    def _unary(self) -> float:
        if self._accept("PLUS"):
            return _require_finite(+self._unary())
        if self._accept("MINUS"):
            return _require_finite(-self._unary())
        return self._power()

    def _power(self) -> float:
        # Parsing the exponent as a unary expression gives both right
        # associativity and support for signed exponents.  The base is parsed
        # first, so exponentiation binds more tightly than a leading sign.
        value = self._primary()
        if self._accept("CARET"):
            exponent = self._unary()
            try:
                value = math.pow(value, exponent)
            except (OverflowError, ValueError) as error:
                raise ValueError("puissance hors du domaine réel") from error
            value = _require_finite(value)
        return value

    def _primary(self) -> float:
        token = self._current

        if self._accept("NUMBER"):
            return _require_finite(float(token.text))

        if self._accept("LPAREN"):
            value = self._expression()
            self._expect("RPAREN", "parenthèse fermante manquante")
            return value

        if token.kind == "NAME":
            self._index += 1
            name = token.text

            if name in _CONSTANTS:
                return _CONSTANTS[name]

            if name == "x":
                if self._variables is None or "x" not in self._variables:
                    raise ValueError("la variable x n'a pas de valeur")
                try:
                    value = float(self._variables["x"])
                except (TypeError, ValueError, OverflowError) as error:
                    raise ValueError("la valeur de x doit être un nombre réel") from error
                return _require_finite(value)

            function = _FUNCTIONS.get(name)
            if function is None:
                raise ValueError(f"nom inconnu ou interdit : {name!r}")
            self._expect("LPAREN", f"la fonction {name} exige des parenthèses")
            argument = self._expression()
            self._expect("RPAREN", f"parenthèse fermante manquante après {name}")
            try:
                return _require_finite(float(function(argument)))
            except (OverflowError, ValueError) as error:
                raise ValueError(f"argument hors domaine pour {name}") from error

        if token.kind == "END":
            raise ValueError("expression incomplète")
        raise ValueError(
            f"élément inattendu {token.text!r} à la position {token.position + 1}"
        )


def evaluate(
    expression: str, variables: dict[str, float] | None = None
) -> float:
    """Evaluate a safe calculator expression and return a finite float.

    ``x`` is the only variable in the language and is available only when the
    caller supplies it in *variables*.  Syntax errors, unknown names and real
    domain errors raise :class:`ValueError`; division by zero raises
    :class:`ZeroDivisionError`.
    """
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("l'expression est vide")
    if variables is not None and not isinstance(variables, dict):
        raise ValueError("variables doit être un dictionnaire ou None")

    try:
        return _Parser(_tokenize(expression), variables).parse()
    except RecursionError as error:
        raise ValueError("expression trop profondément imbriquée") from error


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Sample *expression* over an inclusive interval.

    A point whose expression is undefined or non-finite has ``None`` as its
    ordinate.  This makes such points explicit separators for SVG segments.
    """
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("samples doit être un entier supérieur ou égal à 2")
    try:
        lower = float(x_min)
        upper = float(x_max)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("les bornes doivent être des nombres réels finis") from error
    if not math.isfinite(lower) or not math.isfinite(upper):
        raise ValueError("les bornes doivent être des nombres réels finis")
    if lower >= upper:
        raise ValueError("x_min doit être strictement inférieur à x_max")

    points: list[tuple[float, float | None]] = []
    interval = upper - lower
    for index in range(samples):
        if index == 0:
            x_value = lower
        elif index == samples - 1:
            x_value = upper
        else:
            # This form limits loss of significance around large endpoints.
            fraction = index / (samples - 1)
            x_value = lower * (1.0 - fraction) + upper * fraction
        try:
            y_value: float | None = evaluate(expression, {"x": x_value})
        except (ValueError, ZeroDivisionError, OverflowError):
            y_value = None
        points.append((x_value, y_value))
    return points


def _normalise(value: float, minimum: float, maximum: float) -> float:
    """Return a stable [0, 1] position, including very large finite ranges."""
    if minimum == maximum:
        return 0.5
    if value <= minimum:
        return 0.0
    if value >= maximum:
        return 1.0
    midpoint = minimum / 2.0 + maximum / 2.0
    half_span = maximum / 2.0 - minimum / 2.0
    return 0.5 + 0.5 * ((value - midpoint) / half_span)


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Write finite point segments to a passive, standalone UTF-8 SVG."""
    clean_points: list[tuple[float, float] | None] = []
    finite_points: list[tuple[float, float]] = []

    try:
        iterator = iter(points)
    except TypeError as error:
        raise ValueError("points doit être une séquence de couples (x, y)") from error

    for point in iterator:
        try:
            x_raw, y_raw = point
        except (TypeError, ValueError) as error:
            raise ValueError("chaque point doit contenir exactement x et y") from error
        if y_raw is None:
            clean_points.append(None)
            continue
        try:
            x_value = float(x_raw)
            y_value = float(y_raw)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("les coordonnées doivent être des nombres réels") from error
        if not math.isfinite(x_value) or not math.isfinite(y_value):
            clean_points.append(None)
            continue
        pair = (x_value, y_value)
        clean_points.append(pair)
        finite_points.append(pair)

    if not finite_points:
        raise ValueError("aucun point fini ne peut être tracé")

    x_values = [point[0] for point in finite_points]
    y_values = [point[1] for point in finite_points]
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)

    width, height = 800.0, 500.0
    left, right, top, bottom = 70.0, 770.0, 50.0, 450.0

    def map_x(value: float) -> float:
        return left + (right - left) * _normalise(value, x_min, x_max)

    def map_y(value: float) -> float:
        return bottom - (bottom - top) * _normalise(value, y_min, y_max)

    x_axis_y = map_y(0.0)
    y_axis_x = map_x(0.0)

    segments: list[list[tuple[float, float]]] = []
    current_segment: list[tuple[float, float]] = []
    for point in clean_points:
        if point is None:
            if current_segment:
                segments.append(current_segment)
                current_segment = []
            continue
        current_segment.append(point)
    if current_segment:
        segments.append(current_segment)

    safe_title = escape(str(title), quote=True)
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        (
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'width="800" height="500" viewBox="0 0 800 500" role="img">'
        ),
        f"  <title>{safe_title or 'Courbe scientifique'}</title>",
        '  <rect x="0" y="0" width="800" height="500" fill="#ffffff"/>',
        (
            f'  <line id="x-axis" x1="{left:.3f}" y1="{x_axis_y:.3f}" '
            f'x2="{right:.3f}" y2="{x_axis_y:.3f}" stroke="#5b6470"/>'
        ),
        (
            f'  <line id="y-axis" x1="{y_axis_x:.3f}" y1="{top:.3f}" '
            f'x2="{y_axis_x:.3f}" y2="{bottom:.3f}" stroke="#5b6470"/>'
        ),
    ]
    for segment in segments:
        coordinates = " ".join(
            f"{map_x(x_value):.3f},{map_y(y_value):.3f}"
            for x_value, y_value in segment
        )
        lines.append(
            f'  <polyline points="{coordinates}" fill="none" '
            'stroke="#1769aa" stroke-width="2" stroke-linejoin="round"/>'
        )
    lines.append("</svg>")

    try:
        Path(output_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    except (OSError, TypeError, ValueError) as error:
        raise ValueError(f"impossible d'écrire le SVG : {error}") from error


_HELP = """Commandes :
  <expression>                         évaluer une expression
  plot <expression>; <min>; <max>; <fichier.svg>
                                       tracer une fonction de x
  history                              afficher l'historique réussi
  clear                                vider l'historique
  help                                 afficher cette aide
  quit | exit                          quitter

Opérateurs : + - * / ^, parenthèses et signes unaires.
Constantes : pi, e. Variable de tracé : x.
Fonctions : sin, cos, tan, asin, acos, atan, sqrt, ln, log10, exp, abs.
Les angles sont exprimés en radians."""


def _format_result(value: float) -> str:
    text = format(value, ".15g")
    if "." not in text and "e" not in text.lower():
        text += ".0"
    return text


def _run_plot(command: str) -> str:
    fields = command[5:].split(";")
    if len(fields) != 4:
        raise ValueError(
            "syntaxe : plot <expression>; <min>; <max>; <fichier.svg>"
        )
    expression, lower_text, upper_text, output_path = (
        field.strip() for field in fields
    )
    if not expression or not lower_text or not upper_text or not output_path:
        raise ValueError("tous les paramètres de plot sont obligatoires")
    lower = evaluate(lower_text)
    upper = evaluate(upper_text)
    points = sample_curve(expression, lower, upper)
    write_svg(points, output_path, expression)
    return output_path


def main() -> None:
    """Run the resilient interactive command-line interface."""
    history: list[str] = []
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
            if history:
                for number, entry in enumerate(history, start=1):
                    print(f"{number}: {entry}")
            else:
                print("Historique vide.")
            continue
        if command == "clear":
            history.clear()
            print("Historique effacé.")
            continue

        try:
            if command.startswith("plot "):
                output_path = _run_plot(command)
                history.append(command)
                print(f"Courbe enregistrée dans {output_path}")
            else:
                result = evaluate(command)
                history.append(command)
                print(_format_result(result))
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur : {error}")


if __name__ == "__main__":
    main()
