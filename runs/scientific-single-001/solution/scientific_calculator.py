#!/usr/bin/env python3
"""Safe scientific expression evaluator and dependency-free SVG plotter."""

from __future__ import annotations

import html
import math
import re
from typing import Callable


_FUNCTIONS: dict[str, Callable[[float], float]] = {
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
_NUMBER = re.compile(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?")
_NAME = re.compile(r"[A-Za-z][A-Za-z0-9]*")


class _Token:
    """Small token container independent of module-loader registration."""

    __slots__ = ("kind", "text", "position")

    def __init__(self, kind: str, text: str, position: int):
        self.kind = kind
        self.text = text
        self.position = position


def _tokenize(expression: str) -> list[_Token]:
    tokens: list[_Token] = []
    position = 0
    while position < len(expression):
        if expression[position].isspace():
            position += 1
            continue
        number = _NUMBER.match(expression, position)
        if number:
            tokens.append(_Token("number", number.group(), position))
            position = number.end()
            continue
        name = _NAME.match(expression, position)
        if name:
            tokens.append(_Token("name", name.group(), position))
            position = name.end()
            continue
        character = expression[position]
        if character in "+-*/^()":
            tokens.append(_Token(character, character, position))
            position += 1
            continue
        raise ValueError(f"caractère interdit à la position {position + 1}")
    tokens.append(_Token("end", "", len(expression)))
    return tokens


class _Parser:
    def __init__(self, tokens: list[_Token], variables: dict[str, float]):
        self.tokens = tokens
        self.variables = variables
        self.index = 0

    @property
    def current(self) -> _Token:
        return self.tokens[self.index]

    def accept(self, kind: str) -> bool:
        if self.current.kind == kind:
            self.index += 1
            return True
        return False

    def parse(self) -> float:
        value = self.additive()
        if self.current.kind != "end":
            raise ValueError(
                f"élément inattendu '{self.current.text}' à la position "
                f"{self.current.position + 1}"
            )
        return value

    def additive(self) -> float:
        value = self.multiplicative()
        while self.current.kind in ("+", "-"):
            operator = self.current.kind
            self.index += 1
            operand = self.multiplicative()
            value = value + operand if operator == "+" else value - operand
        return value

    def multiplicative(self) -> float:
        value = self.unary()
        while self.current.kind in ("*", "/"):
            operator = self.current.kind
            self.index += 1
            operand = self.unary()
            if operator == "/":
                if operand == 0:
                    raise ZeroDivisionError("division par zéro")
                value /= operand
            else:
                value *= operand
        return value

    def unary(self) -> float:
        if self.accept("+"):
            return self.unary()
        if self.accept("-"):
            return -self.unary()
        return self.power()

    def power(self) -> float:
        value = self.primary()
        if self.accept("^"):
            exponent = self.unary()
            value = value**exponent
            if isinstance(value, complex):
                raise ValueError("résultat hors du domaine réel")
        return value

    def primary(self) -> float:
        token = self.current
        if self.accept("number"):
            return float(token.text)
        if self.accept("("):
            value = self.additive()
            if not self.accept(")"):
                raise ValueError(f"parenthèse fermante attendue à la position {self.current.position + 1}")
            return value
        if self.accept("name"):
            name = token.text
            if name in _FUNCTIONS:
                if not self.accept("("):
                    raise ValueError(f"la fonction '{name}' doit être appelée avec des parenthèses")
                argument = self.additive()
                if not self.accept(")"):
                    raise ValueError(f"parenthèse fermante attendue après '{name}'")
                return _FUNCTIONS[name](argument)
            if name in _CONSTANTS:
                return _CONSTANTS[name]
            if name == "x" and name in self.variables:
                return self.variables[name]
            raise ValueError(f"nom inconnu ou indisponible : '{name}'")
        if token.kind == "end":
            raise ValueError("expression incomplète")
        raise ValueError(f"expression attendue à la position {token.position + 1}")


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Evaluate an expression without executing Python code.

    ``variables`` may provide the value of ``x``. All syntax and domain errors
    become :class:`ValueError`, except division by zero.
    """
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("l'expression est vide")
    supplied = {} if variables is None else variables
    if not isinstance(supplied, dict):
        raise ValueError("variables doit être un dictionnaire")
    if any(name != "x" for name in supplied):
        raise ValueError("seule la variable 'x' est autorisée")
    converted: dict[str, float] = {}
    if "x" in supplied:
        try:
            converted["x"] = float(supplied["x"])
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("la variable 'x' doit être un nombre fini") from error
        if not math.isfinite(converted["x"]):
            raise ValueError("la variable 'x' doit être un nombre fini")
    try:
        result = _Parser(_tokenize(expression), converted).parse()
    except ZeroDivisionError:
        raise
    except (ValueError, OverflowError) as error:
        if isinstance(error, ValueError) and str(error):
            raise ValueError(str(error)) from error
        raise ValueError("expression hors du domaine réel") from error
    try:
        result = float(result)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("résultat hors du domaine réel") from error
    if not math.isfinite(result):
        raise ValueError("le résultat n'est pas fini")
    return result


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Sample an expression on an inclusive, evenly-spaced interval."""
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("samples doit être un entier au moins égal à 2")
    try:
        start, stop = float(x_min), float(x_max)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("les bornes doivent être des nombres finis") from error
    if not math.isfinite(start) or not math.isfinite(stop) or start >= stop:
        raise ValueError("les bornes doivent être finies et vérifier x_min < x_max")
    step = (stop - start) / (samples - 1)
    points: list[tuple[float, float | None]] = []
    for index in range(samples):
        x = stop if index == samples - 1 else start + index * step
        try:
            y: float | None = evaluate(expression, {"x": x})
        except (ValueError, ZeroDivisionError, OverflowError):
            y = None
        points.append((x, y))
    return points


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Write sampled points to a standalone, inert UTF-8 SVG document."""
    finite: list[tuple[float, float]] = []
    normalized: list[tuple[float, float] | None] = []
    for point in points:
        try:
            x, y = point
            x = float(x)
            y = None if y is None else float(y)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("chaque point doit contenir deux coordonnées numériques") from error
        if not math.isfinite(x) or y is None or not math.isfinite(y):
            normalized.append(None)
        else:
            pair = (x, y)
            normalized.append(pair)
            finite.append(pair)
    if not finite:
        raise ValueError("aucun point fini à tracer")

    width, height, margin = 800.0, 500.0, 40.0
    x_low = min(x for x, _ in finite)
    x_high = max(x for x, _ in finite)
    y_low = min(y for _, y in finite)
    y_high = max(y for _, y in finite)
    if x_low == x_high:
        x_low -= 0.5
        x_high += 0.5
    if y_low == y_high:
        padding = max(0.5, abs(y_low) * 0.05)
        y_low -= padding
        y_high += padding

    def screen(point: tuple[float, float]) -> tuple[float, float]:
        x, y = point
        sx = margin + (x - x_low) * (width - 2 * margin) / (x_high - x_low)
        sy = height - margin - (y - y_low) * (height - 2 * margin) / (y_high - y_low)
        return sx, sy

    axis_x = min(max(0.0, x_low), x_high)
    axis_y = min(max(0.0, y_low), y_high)
    vertical_x, _ = screen((axis_x, y_low))
    _, horizontal_y = screen((x_low, axis_y))
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:g}" height="{height:g}" viewBox="0 0 {width:g} {height:g}">',
        f"  <title>{html.escape(str(title), quote=True)}</title>",
        f'  <rect width="{width:g}" height="{height:g}" fill="white"/>',
        f'  <line x1="{margin:g}" y1="{horizontal_y:.3f}" x2="{width-margin:g}" y2="{horizontal_y:.3f}" stroke="#777"/>',
        f'  <line x1="{vertical_x:.3f}" y1="{margin:g}" x2="{vertical_x:.3f}" y2="{height-margin:g}" stroke="#777"/>',
    ]
    segment: list[str] = []
    for point in normalized + [None]:
        if point is not None:
            sx, sy = screen(point)
            segment.append(f"{sx:.3f},{sy:.3f}")
        elif segment:
            lines.append(f'  <polyline points="{" ".join(segment)}" fill="none" stroke="#1769aa" stroke-width="2"/>')
            segment = []
    lines.append("</svg>")
    with open(output_path, "w", encoding="utf-8", newline="\n") as svg_file:
        svg_file.write("\n".join(lines) + "\n")


_HELP = """Commandes :
  expression                         évaluer une expression
  plot expression; x_min; x_max; fichier.svg
                                     tracer une expression de x
  history                            afficher l'historique réussi
  clear                              vider l'historique
  help                               afficher cette aide
  quit | exit                        quitter
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs
Constantes : pi e    Opérateurs : + - * / ^"""


def _run_cli() -> None:
    history: list[str] = []
    while True:
        try:
            command = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not command:
            continue
        lowered = command.lower()
        if lowered in ("quit", "exit"):
            break
        if lowered == "help":
            print(_HELP)
            continue
        if lowered == "history":
            if history:
                for number, entry in enumerate(history, 1):
                    print(f"{number}: {entry}")
            else:
                print("Historique vide.")
            continue
        if lowered == "clear":
            history.clear()
            print("Historique vidé.")
            continue
        try:
            if lowered.startswith("plot "):
                fields = command[5:].split(";")
                if len(fields) != 4 or any(not field.strip() for field in fields):
                    raise ValueError("syntaxe : plot expression; x_min; x_max; fichier.svg")
                expression, raw_min, raw_max, output_path = (field.strip() for field in fields)
                x_min = evaluate(raw_min)
                x_max = evaluate(raw_max)
                points = sample_curve(expression, x_min, x_max)
                write_svg(points, output_path, expression)
                history.append(command)
                print(f"Courbe enregistrée dans {output_path}")
            else:
                print(evaluate(command))
                history.append(command)
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur : {error}")


if __name__ == "__main__":
    _run_cli()
