#!/usr/bin/env python3
"""Calculatrice scientifique sûre et générateur de courbes SVG.

Le langage d'expressions est analysé par un lexer et un parseur dédiés. Il
n'utilise aucun mécanisme d'exécution dynamique de code Python.
"""

from __future__ import annotations

import math
import numbers
import os
import re
from typing import Callable, Sequence
import xml.etree.ElementTree as ET


_NUMBER_PATTERN = r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
_NAME_PATTERN = r"[A-Za-z][A-Za-z0-9]*"
_CONSTANTS = {"pi": math.pi, "e": math.e}
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
_SINGLE_CHAR_TOKENS = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "^": "CARET",
    "(": "LPAREN",
    ")": "RPAREN",
}
_ASCII_WHITESPACE = " \t\r\n\f\v"


class _Token:
    """Jeton lexical indépendant des mécanismes d'introspection du chargeur."""

    __slots__ = ("kind", "value", "position")

    def __init__(self, kind: str, value: str, position: int) -> None:
        self.kind = kind
        self.value = value
        self.position = position


_Ast = tuple


def _tokenize(expression: str) -> list[_Token]:
    if not isinstance(expression, str):
        raise ValueError("L'expression doit être une chaîne de caractères")
    if not expression.strip(_ASCII_WHITESPACE):
        raise ValueError("L'expression est vide")

    tokens: list[_Token] = []
    position = 0
    while position < len(expression):
        character = expression[position]
        if character in _ASCII_WHITESPACE:
            position += 1
            continue

        remaining = expression[position:]
        number_match = re.match(_NUMBER_PATTERN, remaining, re.ASCII)
        if number_match is not None:
            value = number_match.group(0)
            tokens.append(_Token("NUMBER", value, position))
            position += number_match.end()
            continue

        name_match = re.match(_NAME_PATTERN, remaining, re.ASCII)
        if name_match is not None:
            value = name_match.group(0)
            tokens.append(_Token("NAME", value, position))
            position += name_match.end()
            continue

        kind = _SINGLE_CHAR_TOKENS.get(character)
        if kind is None:
            raise ValueError(
                f"Caractère interdit à la position {position + 1}: {character!r}"
            )
        tokens.append(_Token(kind, character, position))
        position += 1

    tokens.append(_Token("EOF", "", len(expression)))
    return tokens


class _Parser:
    """Parseur descendant récursif du petit langage arithmétique."""

    def __init__(self, tokens: Sequence[_Token]) -> None:
        self._tokens = tokens
        self._index = 0

    @property
    def _current(self) -> _Token:
        return self._tokens[self._index]

    def _accept(self, kind: str) -> _Token | None:
        if self._current.kind != kind:
            return None
        token = self._current
        self._index += 1
        return token

    def _expect(self, kind: str, message: str) -> _Token:
        token = self._accept(kind)
        if token is None:
            raise ValueError(
                f"{message} à la position {self._current.position + 1}"
            )
        return token

    def parse(self) -> _Ast:
        node = self._sum()
        if self._current.kind != "EOF":
            raise ValueError(
                f"Élément inattendu à la position {self._current.position + 1}"
            )
        return node

    def _sum(self) -> _Ast:
        node = self._product()
        while self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._product())
        return node

    def _product(self) -> _Ast:
        node = self._unary()
        while self._current.kind in ("STAR", "SLASH"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._unary())
        return node

    def _unary(self) -> _Ast:
        if self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            return ("unary", operator, self._unary())
        return self._power()

    def _power(self) -> _Ast:
        node = self._primary()
        if self._accept("CARET") is not None:
            # L'exposant passe par _unary : la puissance reste associative à
            # droite tout en autorisant 2^-2.
            node = ("binary", "^", node, self._unary())
        return node

    def _primary(self) -> _Ast:
        number = self._accept("NUMBER")
        if number is not None:
            try:
                value = float(number.value)
            except (ValueError, OverflowError) as error:
                raise ValueError("Littéral numérique invalide") from error
            if not math.isfinite(value):
                raise ValueError("Le littéral numérique n'est pas fini")
            return ("number", value)

        name_token = self._accept("NAME")
        if name_token is not None:
            name = name_token.value
            if self._accept("LPAREN") is not None:
                if name not in _FUNCTIONS:
                    raise ValueError(f"Fonction inconnue: {name}")
                argument = self._sum()
                self._expect("RPAREN", "Parenthèse fermante attendue")
                return ("call", name, argument)
            if name in _CONSTANTS:
                return ("number", _CONSTANTS[name])
            if name == "x":
                return ("variable", "x")
            if name in _FUNCTIONS:
                raise ValueError(f"La fonction {name} doit être appelée")
            raise ValueError(f"Nom inconnu: {name}")

        if self._accept("LPAREN") is not None:
            node = self._sum()
            self._expect("RPAREN", "Parenthèse fermante attendue")
            return node

        raise ValueError(
            f"Nombre, nom ou parenthèse attendu à la position "
            f"{self._current.position + 1}"
        )


def _parse_expression(expression: str) -> _Ast:
    try:
        return _Parser(_tokenize(expression)).parse()
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée") from error


def _finite_float(value: object, description: str) -> float:
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{description} doit être un nombre réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{description} doit être un nombre réel fini") from error
    if not math.isfinite(result):
        raise ValueError(f"{description} doit être fini")
    return result


def _checked_result(value: object) -> float:
    if isinstance(value, complex):
        raise ValueError("Le résultat sort du domaine réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Résultat numérique invalide") from error
    if not math.isfinite(result):
        raise ValueError("Le résultat n'est pas fini")
    return result


def _apply_function(name: str, argument: float) -> float:
    try:
        return _checked_result(_FUNCTIONS[name](argument))
    except (ValueError, OverflowError) as error:
        raise ValueError(f"Argument hors domaine pour {name}") from error


def _apply_binary(operator: str, left: float, right: float) -> float:
    try:
        if operator == "+":
            value = left + right
        elif operator == "-":
            value = left - right
        elif operator == "*":
            value = left * right
        elif operator == "/":
            value = left / right
        else:
            value = left**right
    except ZeroDivisionError as error:
        if operator == "/":
            raise
        raise ValueError("Opération hors du domaine réel") from error
    except (ValueError, OverflowError) as error:
        raise ValueError("Opération hors du domaine réel") from error
    return _checked_result(value)


def _evaluate_ast(node: _Ast, variables: dict[str, float]) -> float:
    """Évalue l'AST avec des piles explicites, sans récursion Python."""

    pending: list[tuple[_Ast, bool]] = [(node, False)]
    values: list[float] = []
    while pending:
        current, ready = pending.pop()
        kind = current[0]
        if kind == "number":
            values.append(current[1])
            continue
        if kind == "variable":
            if "x" not in variables:
                raise ValueError("La variable x n'a pas de valeur")
            values.append(variables["x"])
            continue

        if not ready:
            pending.append((current, True))
            if kind in ("unary", "call"):
                pending.append((current[2], False))
            else:
                # Empiler la droite avant la gauche conserve l'ordre
                # d'évaluation naturel lorsque la pile est dépilée.
                pending.append((current[3], False))
                pending.append((current[2], False))
            continue

        if kind == "unary":
            value = values.pop()
            values.append(_checked_result(value if current[1] == "+" else -value))
        elif kind == "call":
            values.append(_apply_function(current[1], values.pop()))
        else:
            right = values.pop()
            left = values.pop()
            values.append(_apply_binary(current[1], left, right))

    return values[0]


def _validated_variables(
    variables: dict[str, float] | None,
) -> dict[str, float]:
    if variables is None:
        return {}
    if not isinstance(variables, dict):
        raise ValueError("variables doit être un dictionnaire")
    extra_names = set(variables) - {"x"}
    if extra_names:
        raise ValueError("Seule la variable x est autorisée")
    if "x" not in variables:
        return {}
    return {"x": _finite_float(variables["x"], "La variable x")}


def evaluate(
    expression: str,
    variables: dict[str, float] | None = None,
) -> float:
    """Évalue *expression* dans le langage sûr et retourne un float fini.

    ``ValueError`` signale une syntaxe, un nom, un domaine réel ou une valeur
    non finie invalide. Une division par zéro conserve ``ZeroDivisionError``.
    """

    parsed = _parse_expression(expression)
    validated_variables = _validated_variables(variables)
    return _checked_result(_evaluate_ast(parsed, validated_variables))


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne une expression et marque les valeurs indéfinies par None."""

    minimum = _finite_float(x_min, "x_min")
    maximum = _finite_float(x_max, "x_max")
    if minimum >= maximum:
        raise ValueError("x_min doit être strictement inférieur à x_max")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("samples doit être un entier au moins égal à 2")

    # Le parsing préalable fait remonter les erreurs structurelles une seule
    # fois. Seules les erreurs numériques propres à un point deviennent None.
    parsed = _parse_expression(expression)
    points: list[tuple[float, float | None]] = []
    denominator = samples - 1
    for index in range(samples):
        if index == 0:
            x_value = minimum
        elif index == denominator:
            x_value = maximum
        else:
            ratio = index / denominator
            x_value = (1.0 - ratio) * minimum + ratio * maximum
        try:
            y_value = _checked_result(_evaluate_ast(parsed, {"x": x_value}))
        except (ValueError, ZeroDivisionError):
            y_value = None
        points.append((x_value, y_value))
    return points


def _is_valid_xml_text(text: str) -> bool:
    for character in text:
        codepoint = ord(character)
        if not (
            codepoint in (0x09, 0x0A, 0x0D)
            or 0x20 <= codepoint <= 0xD7FF
            or 0xE000 <= codepoint <= 0xFFFD
            or 0x10000 <= codepoint <= 0x10FFFF
        ):
            return False
    return True


def _svg_number(value: float) -> str:
    if not math.isfinite(value):
        raise ValueError("Coordonnée SVG non finie")
    return format(value, ".12g")


def _expanded_bounds(value: float) -> tuple[float, float]:
    """Crée une étendue finie autour d'une coordonnée unique."""

    expansion = max(1.0, abs(value) * 0.05)
    low = value - expansion
    high = value + expansion
    if not math.isfinite(low):
        low = value
    if not math.isfinite(high):
        high = value
    if low == high:
        low = math.nextafter(value, -math.inf)
        high = math.nextafter(value, math.inf)
        if not math.isfinite(low):
            low = value
        if not math.isfinite(high):
            high = value
    if low == high:
        raise ValueError("Étendue graphique impossible à représenter")
    return low, high


def _relative_position(value: float, low: float, high: float) -> float:
    """Calcule une position relative sans faire déborder high - low."""

    scale = max(abs(low), abs(high), 1.0)
    low_scaled = low / scale
    high_scaled = high / scale
    value_scaled = value / scale
    return (value_scaled - low_scaled) / (high_scaled - low_scaled)


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Écrit une représentation SVG autonome des points fournis.

    Les valeurs ``None`` ou non finies séparent les segments. Un fichier
    existant à *output_path* est remplacé.
    """

    if not isinstance(title, str) or not _is_valid_xml_text(title):
        raise ValueError("Le titre contient des caractères XML invalides")
    try:
        path = os.fspath(output_path)
    except TypeError as error:
        raise ValueError("Chemin de sortie invalide") from error
    if not isinstance(path, (str, bytes)) or not path:
        raise ValueError("Le chemin de sortie est vide")
    if not isinstance(points, list):
        raise ValueError("points doit être une liste")

    normalized: list[tuple[float, float] | None] = []
    finite_points: list[tuple[float, float]] = []
    for point in points:
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            raise ValueError("Chaque point doit contenir exactement x et y")
        x_raw, y_raw = point
        if y_raw is None:
            normalized.append(None)
            continue
        if (
            isinstance(x_raw, bool)
            or isinstance(y_raw, bool)
            or not isinstance(x_raw, numbers.Real)
            or not isinstance(y_raw, numbers.Real)
        ):
            raise ValueError("Les coordonnées doivent être des nombres réels")
        try:
            x_value = float(x_raw)
            y_value = float(y_raw)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("Coordonnée invalide") from error
        if not math.isfinite(x_value) or not math.isfinite(y_value):
            normalized.append(None)
            continue
        finite_point = (x_value, y_value)
        normalized.append(finite_point)
        finite_points.append(finite_point)

    if not finite_points:
        raise ValueError("Aucun point fini ne peut être tracé")

    x_values = [point[0] for point in finite_points]
    y_values = [point[1] for point in finite_points]
    x_low, x_high = min(x_values), max(x_values)
    y_low, y_high = min(y_values), max(y_values)
    if x_low == x_high:
        x_low, x_high = _expanded_bounds(x_low)
    if y_low == y_high:
        y_low, y_high = _expanded_bounds(y_low)

    width, height, margin = 800.0, 500.0, 55.0
    plot_width = width - 2.0 * margin
    plot_height = height - 2.0 * margin

    def project_x(value: float) -> float:
        return margin + _relative_position(value, x_low, x_high) * plot_width

    def project_y(value: float) -> float:
        return height - margin - _relative_position(value, y_low, y_high) * plot_height

    axis_x = min(max(project_x(0.0), margin), width - margin)
    axis_y = min(max(project_y(0.0), margin), height - margin)

    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    root = ET.Element(
        f"{{{namespace}}}svg",
        {
            "viewBox": "0 0 800 500",
            "width": "800",
            "height": "500",
            "role": "img",
        },
    )
    if title:
        title_element = ET.SubElement(root, f"{{{namespace}}}title")
        title_element.text = title
    ET.SubElement(
        root,
        f"{{{namespace}}}rect",
        {"width": "800", "height": "500", "fill": "#ffffff"},
    )
    axis_style = {"stroke": "#666666", "stroke-width": "1"}
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(margin),
            "y1": _svg_number(axis_y),
            "x2": _svg_number(width - margin),
            "y2": _svg_number(axis_y),
            **axis_style,
        },
    )
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(axis_x),
            "y1": _svg_number(margin),
            "x2": _svg_number(axis_x),
            "y2": _svg_number(height - margin),
            **axis_style,
        },
    )

    def append_segment(segment: list[tuple[float, float]]) -> None:
        projected = [
            (project_x(x_value), project_y(y_value))
            for x_value, y_value in segment
        ]
        if len(projected) == 1:
            x_screen, y_screen = projected[0]
            ET.SubElement(
                root,
                f"{{{namespace}}}circle",
                {
                    "cx": _svg_number(x_screen),
                    "cy": _svg_number(y_screen),
                    "r": "2.5",
                    "fill": "#1769aa",
                },
            )
            return
        coordinates = " ".join(
            f"{_svg_number(x_screen)},{_svg_number(y_screen)}"
            for x_screen, y_screen in projected
        )
        ET.SubElement(
            root,
            f"{{{namespace}}}polyline",
            {
                "points": coordinates,
                "fill": "none",
                "stroke": "#1769aa",
                "stroke-width": "2",
                "stroke-linejoin": "round",
                "stroke-linecap": "round",
            },
        )

    current_segment: list[tuple[float, float]] = []
    for point in normalized:
        if point is None:
            if current_segment:
                append_segment(current_segment)
                current_segment = []
        else:
            current_segment.append(point)
    if current_segment:
        append_segment(current_segment)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)


_HELP = """Commandes :
  <expression>                         évaluer une expression
  plot <expression>; <min>; <max>; <fichier.svg>
                                       tracer une courbe
  history                              afficher l'historique réussi
  clear                                vider l'historique
  help                                 afficher cette aide
  quit | exit                          quitter

Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs
Constantes : pi e    Variable de tracé : x    Angles : radians"""


def _terminal_text(text: str) -> str:
    """Neutralise les contrôles lors du réaffichage d'une entrée utilisateur."""

    return "".join(
        character if character.isprintable() else ascii(character)[1:-1]
        for character in text
    )


def _handle_line(line: str, history: list[str]) -> bool:
    """Traite une ligne de CLI. Retourne False lorsqu'il faut quitter."""

    command = line.strip()
    if command in ("quit", "exit"):
        return False
    if command == "help":
        print(_HELP)
        return True
    if command == "history":
        if not history:
            print("Historique vide.")
        else:
            for index, entry in enumerate(history, start=1):
                print(f"{index}: {_terminal_text(entry)}")
        return True
    if command == "clear":
        history.clear()
        print("Historique effacé.")
        return True

    if command == "plot" or command.startswith("plot "):
        fields = command[4:].strip().split(";")
        if len(fields) != 4 or any(not field.strip() for field in fields):
            raise ValueError(
                "Syntaxe: plot <expression>; <min>; <max>; <fichier.svg>"
            )
        expression, minimum_text, maximum_text, output_path = (
            field.strip() for field in fields
        )
        minimum = evaluate(minimum_text)
        maximum = evaluate(maximum_text)
        curve = sample_curve(expression, minimum, maximum)
        write_svg(curve, output_path, expression)
        history.append(command)
        print(f"Courbe enregistrée dans {_terminal_text(output_path)}")
        return True

    result = evaluate(command)
    history.append(command)
    print(result)
    return True


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""

    history: list[str] = []
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        try:
            if not _handle_line(line, history):
                break
        except KeyboardInterrupt:
            print()
            break
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur: {error}")


if __name__ == "__main__":
    main()
