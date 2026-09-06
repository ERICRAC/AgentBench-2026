"""Calculatrice réelle sûre et tracé SVG, uniquement en bibliothèque standard.

Grammaire : sum -> product -> unary -> power -> primary.
power = primary ['^' unary] assure l'associativité à droite et -2^2 == -4.
Aucun texte utilisateur n'est exécuté comme du code Python.
"""

from __future__ import annotations

import html
import math
import re
from pathlib import Path


_FUNCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sqrt": math.sqrt, "ln": math.log, "log10": math.log10,
    "exp": math.exp, "abs": abs,
}
_CONSTANTS = {"pi": math.pi, "e": math.e}
_TOKEN = r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?|[A-Za-z_][A-Za-z_0-9]*|[^\s]"
_MAX_LENGTH = 10000
_MAX_TOKENS = 512


def _finite(value: object) -> float:
    """Convertit une donnée numérique réelle, sans accepter chaînes ou booléens."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Une valeur numérique réelle est requise.")
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError("Valeur numérique hors limites.") from error
    if not math.isfinite(result):
        raise ValueError("Le résultat doit être un nombre fini.")
    return result


class _Parser:
    """Analyse descendante vers un arbre constitué de tuples inertes."""

    def __init__(self, expression: str):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError("Expression vide ou non textuelle.")
        if len(expression) > _MAX_LENGTH:
            raise ValueError("Expression trop longue (10000 caractères maximum).")
        self.tokens = re.findall(_TOKEN, expression)
        if len(self.tokens) > _MAX_TOKENS:
            raise ValueError("Expression trop complexe (512 jetons maximum).")
        self.position = 0

    def peek(self) -> str:
        return self.tokens[self.position] if self.position < len(self.tokens) else ""

    def take(self) -> str:
        token = self.peek()
        if not token:
            raise ValueError("Expression incomplète.")
        self.position += 1
        return token

    def parse(self) -> tuple:
        node = self.sum()
        if self.peek():
            raise ValueError(f"Jeton inattendu : {self.peek()!r}.")
        return node

    def sum(self) -> tuple:
        node = self.product()
        while self.peek() in ("+", "-"):
            operator = self.take()
            node = (operator, node, self.product())
        return node

    def product(self) -> tuple:
        node = self.unary()
        while self.peek() in ("*", "/"):
            operator = self.take()
            node = (operator, node, self.unary())
        return node

    def unary(self) -> tuple:
        if self.peek() in ("+", "-"):
            return ("unary", self.take(), self.unary())
        return self.power()

    def power(self) -> tuple:
        node = self.primary()
        if self.peek() == "^":
            self.take()
            node = ("^", node, self.unary())
        return node

    def primary(self) -> tuple:
        token = self.take()
        if token == "(":
            node = self.sum()
            if self.take() != ")":
                raise ValueError("Parenthèse fermante attendue.")
            return node
        if token in _FUNCTIONS:
            if self.take() != "(":
                raise ValueError(f"La fonction {token} exige des parenthèses.")
            argument = self.sum()
            if self.take() != ")":
                raise ValueError("Parenthèse fermante attendue après l'argument.")
            return ("call", token, argument)
        if token in _CONSTANTS:
            return ("number", _CONSTANTS[token])
        if token == "x":
            return ("variable",)
        if token[0] in "0123456789.":
            try:
                return ("number", _finite(float(token)))
            except ValueError as error:
                raise ValueError(f"Nombre invalide : {token!r}.") from error
        raise ValueError(f"Nom ou caractère interdit : {token!r}.")


def _parse(expression: str) -> tuple:
    try:
        return _Parser(expression).parse()
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée.") from error


def _calculate(node: tuple, variables: dict[str, float]) -> float:
    kind = node[0]
    if kind == "number":
        return node[1]
    if kind == "variable":
        if "x" not in variables:
            raise ValueError("La variable x n'a pas de valeur.")
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
        if right == 0:
            raise ZeroDivisionError("Division par zéro.")
        result = left / right
    else:
        result = math.pow(left, right)
    return _finite(result)


def _run(node: tuple, variables: dict[str, float]) -> float:
    try:
        return _calculate(node, variables)
    except OverflowError as error:
        raise ValueError("Résultat hors des limites des flottants.") from error
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée.") from error
    except ValueError as error:
        raise ValueError(f"Expression non définie dans les réels : {error}") from error


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Évalue une expression réelle finie ; seule la variable x est autorisée.

    Syntaxe, domaine et débordement lèvent ValueError ; une division par zéro
    lève ZeroDivisionError. Les autres clés de variables ne créent aucun nom.
    """
    if variables is not None and not isinstance(variables, dict):
        raise ValueError("Les variables doivent être fournies dans un dictionnaire.")
    return _run(_parse(expression), {} if variables is None else variables)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne uniformément, bornes incluses ; None marque un point invalide.

    Les erreurs de syntaxe sont signalées avant l'échantillonnage. Les erreurs
    numériques locales sont converties en ruptures, même si toutes le sont.
    """
    lower, upper = _finite(x_min), _finite(x_max)
    if lower >= upper:
        raise ValueError("Il faut x_min < x_max.")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("Il faut un nombre entier d'échantillons, au moins 2.")
    node = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        # Une combinaison convexe évite le débordement de upper - lower.
        x = lower if index == 0 else upper if index == samples - 1 else (
            (1 - fraction) * lower + fraction * upper
        )
        try:
            y = _run(node, {"x": x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def _xml_text(value: str) -> str:
    # L'échappement seul ne rend pas valides les contrôles interdits en XML 1.0.
    cleaned = "".join(
        character if character in "\t\n\r" or 0x20 <= ord(character) <= 0xD7FF
        or 0xE000 <= ord(character) <= 0xFFFD
        or 0x10000 <= ord(character) <= 0x10FFFF else "\ufffd"
        for character in str(value)
    )
    return html.escape(cleaned, quote=True)


def _projection(values: list[float], start: float, end: float):
    """Construit une projection affine sans soustraire de grands flottants."""
    minimum, maximum = min(values), max(values)
    magnitude = max(abs(minimum), abs(maximum)) or 1.0
    low, high = minimum / magnitude, maximum / magnitude

    def project(value: float) -> float:
        if low == high:
            return (start + end) / 2
        ratio = (value / magnitude - low) / (high - low)
        return start + min(1.0, max(0.0, ratio)) * (end - start)

    return project


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Écrit un SVG autonome. Les points non finis interrompent les segments.

    Les axes hors plage sont rabattus sur le bord du cadre. Un point isolé est
    représenté par un disque. Aucun fichier n'est écrit sans point traçable.
    """
    cleaned = []
    finite_points = []
    for point in points:
        try:
            x, y = point
            pair = (_finite(x), _finite(y))
        except (ValueError, TypeError):
            cleaned.append(None)
        else:
            cleaned.append(pair)
            finite_points.append(pair)
    if not finite_points:
        raise ValueError("Aucun point fini à tracer.")
    px = _projection([point[0] for point in finite_points], 60, 760)
    py = _projection([point[1] for point in finite_points], 440, 60)
    caption = _xml_text(title)
    svg = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500" role="img">',
        f'<title>{caption}</title>',
        '<rect width="800" height="500" fill="#ffffff"/>',
        f'<text x="400" y="30" text-anchor="middle" font-family="sans-serif" fill="#172033">{caption}</text>',
        f'<line x1="60" y1="{py(0):.6f}" x2="760" y2="{py(0):.6f}" stroke="#64748b"/>',
        f'<line x1="{px(0):.6f}" y1="60" x2="{px(0):.6f}" y2="440" stroke="#64748b"/>',
    ]

    def flush(segment: list[str]) -> None:
        if len(segment) == 1:
            x, y = segment[0].split(",")
            svg.append(f'<circle cx="{x}" cy="{y}" r="2" fill="#2563eb"/>')
        elif segment:
            svg.append('<polyline points="' + " ".join(segment)
                       + '" fill="none" stroke="#2563eb" stroke-width="2"/>')

    segment = []
    for point in cleaned:
        if point is None:
            flush(segment)
            segment = []
        else:
            segment.append(f"{px(point[0]):.6f},{py(point[1]):.6f}")
    flush(segment)
    xs, ys = zip(*finite_points)
    for x, y, label, anchor in (
        (60, 465, f"x min: {min(xs):.6g}", "start"),
        (760, 465, f"x max: {max(xs):.6g}", "end"),
        (60, 485, f"y min: {min(ys):.6g}   y max: {max(ys):.6g}", "start"),
    ):
        svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="12" fill="#172033">{label}</text>')
    svg.append("</svg>")
    Path(output_path).write_text("\n".join(svg) + "\n", encoding="utf-8")


_HELP = """Expressions : + - * / ^, parenthèses ; constantes pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Tracé : plot expression; borne_min; borne_max; fichier.svg
Exemple : plot sin(x); -pi; pi; sinus.svg
help : aide ; history : réussites ; clear : vider l'historique ; quit/exit : quitter.
"""


def main() -> None:
    """Boucle interactive avec historique des seules commandes réussies."""
    history: list[str] = []
    while True:
        try:
            command = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not command:
            continue
        keyword = command.lower()
        if keyword in ("quit", "exit"):
            return
        if keyword == "help":
            print(_HELP)
        elif keyword == "history":
            print("\n".join(f"{i}. {item}" for i, item in enumerate(history, 1))
                  or "Historique vide.")
        elif keyword == "clear":
            history.clear()
            print("Historique effacé.")
        else:
            try:
                if command.split(maxsplit=1)[0].lower() == "plot":
                    fields = [field.strip() for field in command[4:].split(";")]
                    if len(fields) != 4 or not all(fields):
                        raise ValueError("Syntaxe : plot expression; min; max; fichier.svg")
                    expression, lower, upper, path = fields
                    points = sample_curve(expression, evaluate(lower), evaluate(upper))
                    write_svg(points, path, title=expression)
                    print(f"Courbe enregistrée dans {path}")
                else:
                    print(evaluate(command))
                history.append(command)
            except (ValueError, ZeroDivisionError, OSError) as error:
                print(f"Erreur : {error}")
            except KeyboardInterrupt:
                print("\nOpération interrompue.")


if __name__ == "__main__":
    main()
