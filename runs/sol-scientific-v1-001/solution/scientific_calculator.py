#!/usr/bin/env python3
"""Calculatrice scientifique sûre et export de courbes en SVG.

Le langage d'expressions est analysé par un petit lexer et un parseur récursif.
Il n'exécute jamais l'expression comme du code Python.
"""

from __future__ import annotations

import math
from typing import Callable
import xml.etree.ElementTree as ET


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
    "abs": math.fabs,
}

_CONSTANTS = {"pi": math.pi, "e": math.e}


class _Token:
    """Jeton minimal, indépendant des particularités du chargeur de module."""

    __slots__ = ("kind", "value", "position")

    def __init__(self, kind: str, value: str, position: int) -> None:
        self.kind = kind
        self.value = value
        self.position = position


class _Lexer:
    """Transforme une expression dans le petit ensemble de jetons autorisés."""

    def __init__(self, source: str) -> None:
        self.source = source
        self.length = len(source)
        self.position = 0

    def tokens(self) -> list[_Token]:
        result: list[_Token] = []
        while self.position < self.length:
            char = self.source[self.position]
            if char.isspace():
                self.position += 1
            elif char in "+-*/^()":
                result.append(_Token(char, char, self.position))
                self.position += 1
            elif self._is_ascii_digit(char) or char == ".":
                result.append(self._number())
            elif self._is_ascii_letter(char):
                result.append(self._identifier())
            else:
                raise ValueError(
                    f"Caractère interdit {char!r} à la position {self.position}."
                )
        result.append(_Token("EOF", "", self.length))
        return result

    @staticmethod
    def _is_ascii_digit(char: str) -> bool:
        return "0" <= char <= "9"

    @staticmethod
    def _is_ascii_letter(char: str) -> bool:
        return ("a" <= char <= "z") or ("A" <= char <= "Z")

    def _number(self) -> _Token:
        start = self.position
        digits_before = 0
        while (
            self.position < self.length
            and self._is_ascii_digit(self.source[self.position])
        ):
            self.position += 1
            digits_before += 1

        digits_after = 0
        if self.position < self.length and self.source[self.position] == ".":
            self.position += 1
            while (
                self.position < self.length
                and self._is_ascii_digit(self.source[self.position])
            ):
                self.position += 1
                digits_after += 1

        if digits_before == 0 and digits_after == 0:
            raise ValueError(f"Nombre mal formé à la position {start}.")

        if self.position < self.length and self.source[self.position] in "eE":
            exponent_mark = self.position
            self.position += 1
            if (
                self.position < self.length
                and self.source[self.position] in "+-"
            ):
                self.position += 1
            exponent_start = self.position
            while (
                self.position < self.length
                and self._is_ascii_digit(self.source[self.position])
            ):
                self.position += 1
            if self.position == exponent_start:
                raise ValueError(
                    f"Exposant mal formé à la position {exponent_mark}."
                )

        return _Token("NUMBER", self.source[start : self.position], start)

    def _identifier(self) -> _Token:
        start = self.position
        while self.position < self.length:
            char = self.source[self.position]
            if not (self._is_ascii_letter(char) or self._is_ascii_digit(char)):
                break
            self.position += 1
        return _Token("IDENTIFIER", self.source[start : self.position], start)


class _Parser:
    """Parseur descendant qui calcule en même temps l'expression."""

    def __init__(self, tokens: list[_Token], x_value: float | None) -> None:
        self.tokens = tokens
        self.index = 0
        self.x_value = x_value

    @property
    def current(self) -> _Token:
        return self.tokens[self.index]

    def parse(self) -> float:
        value = self._additive()
        if self.current.kind != "EOF":
            raise ValueError(
                f"Élément inattendu {self.current.value!r} "
                f"à la position {self.current.position}."
            )
        return value

    def _accept(self, kind: str) -> bool:
        if self.current.kind == kind:
            self.index += 1
            return True
        return False

    def _additive(self) -> float:
        value = self._multiplicative()
        while self.current.kind in {"+", "-"}:
            operator = self.current.kind
            self.index += 1
            right = self._multiplicative()
            value = value + right if operator == "+" else value - right
            self._require_finite(value)
        return value

    def _multiplicative(self) -> float:
        value = self._unary()
        while self.current.kind in {"*", "/"}:
            operator = self.current.kind
            self.index += 1
            right = self._unary()
            if operator == "*":
                value *= right
            else:
                if right == 0.0:
                    raise ZeroDivisionError("Division par zéro.")
                value /= right
            self._require_finite(value)
        return value

    def _unary(self) -> float:
        if self._accept("+"):
            return self._unary()
        if self._accept("-"):
            return -self._unary()
        return self._power()

    def _power(self) -> float:
        # L'exposant est un unaire : cela rend ^ associatif à droite, autorise
        # 2^-2, et conserve à ^ une priorité supérieure au signe de -2^2.
        base = self._primary()
        if self._accept("^"):
            exponent = self._unary()
            try:
                value = base**exponent
            except ZeroDivisionError as error:
                raise ZeroDivisionError("Puissance indéfinie avec une base nulle.") from error
            except (OverflowError, ValueError) as error:
                raise ValueError("Puissance hors du domaine réel.") from error
            if isinstance(value, complex):
                raise ValueError("Puissance hors du domaine réel.")
            self._require_finite(value)
            return value
        return base

    def _primary(self) -> float:
        token = self.current
        if self._accept("NUMBER"):
            try:
                value = float(token.value)
            except ValueError as error:
                raise ValueError(f"Nombre invalide {token.value!r}.") from error
            self._require_finite(value)
            return value

        if self._accept("("):
            value = self._additive()
            if not self._accept(")"):
                raise ValueError(
                    f"Parenthèse fermante attendue à la position "
                    f"{self.current.position}."
                )
            return value

        if self._accept("IDENTIFIER"):
            name = token.value
            if name in _CONSTANTS:
                return _CONSTANTS[name]
            if name == "x":
                if self.x_value is None:
                    raise ValueError("La variable x n'a pas de valeur.")
                return self.x_value
            if name not in _FUNCTIONS:
                raise ValueError(f"Nom inconnu ou interdit : {name!r}.")
            if not self._accept("("):
                raise ValueError(f"La fonction {name} doit être appelée avec (...).")
            argument = self._additive()
            if not self._accept(")"):
                raise ValueError(
                    f"Parenthèse fermante attendue après la fonction {name}."
                )
            try:
                value = _FUNCTIONS[name](argument)
            except (ValueError, OverflowError) as error:
                raise ValueError(f"Argument hors du domaine réel pour {name}.") from error
            self._require_finite(value)
            return value

        if token.kind == "EOF":
            raise ValueError("Expression incomplète.")
        raise ValueError(
            f"Élément inattendu {token.value!r} à la position {token.position}."
        )

    @staticmethod
    def _require_finite(value: float) -> None:
        if not math.isfinite(value):
            raise ValueError("Le calcul produit une valeur non finie.")


def evaluate(
    expression: str, variables: dict[str, float] | None = None
) -> float:
    """Évalue une expression autorisée et renvoie un flottant réel fini.

    ``x`` est le seul nom de variable admis et doit être présent dans
    ``variables`` lorsqu'il apparaît. Les erreurs de syntaxe, de domaine et les
    noms interdits produisent ``ValueError`` ; une division par zéro produit
    ``ZeroDivisionError``.
    """

    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("L'expression est vide.")

    x_value: float | None = None
    if variables is not None and "x" in variables:
        try:
            x_value = float(variables["x"])
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("La valeur de x doit être un nombre réel fini.") from error
        if not math.isfinite(x_value):
            raise ValueError("La valeur de x doit être un nombre réel fini.")

    tokens = _Lexer(expression).tokens()
    try:
        result = _Parser(tokens, x_value).parse()
    except ZeroDivisionError:
        raise
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée.") from error
    except (OverflowError, ArithmeticError) as error:
        raise ValueError("Calcul hors du domaine réel.") from error

    if isinstance(result, complex) or not math.isfinite(result):
        raise ValueError("Le résultat n'est pas un nombre réel fini.")
    return float(result)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne ``expression`` sur l'intervalle fermé demandé.

    Un point où l'expression n'est pas définie est conservé avec une ordonnée
    ``None`` afin qu'un tracé ne relie pas les deux côtés d'une discontinuité.
    """

    try:
        lower = float(x_min)
        upper = float(x_max)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Les bornes doivent être des nombres réels finis.") from error
    if not math.isfinite(lower) or not math.isfinite(upper) or lower >= upper:
        raise ValueError("Il faut des bornes finies telles que x_min < x_max.")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("Le nombre d'échantillons doit être un entier au moins égal à 2.")

    span = upper - lower
    denominator = samples - 1
    points: list[tuple[float, float | None]] = []
    for index in range(samples):
        if index == 0:
            x_value = lower
        elif index == denominator:
            x_value = upper
        else:
            x_value = lower + span * index / denominator
        try:
            y_value: float | None = evaluate(expression, {"x": x_value})
        except (ValueError, ZeroDivisionError):
            y_value = None
        points.append((x_value, y_value))
    return points


def _valid_xml_text(value: object) -> str:
    """Remplace les caractères que XML 1.0 ne permet pas dans du texte."""

    text = str(value)
    return "".join(
        character
        if (
            character in "\t\n\r"
            or "\u0020" <= character <= "\ud7ff"
            or "\ue000" <= character <= "\ufffd"
            or "\U00010000" <= character <= "\U0010ffff"
        )
        else "\ufffd"
        for character in text
    )


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Écrit une représentation SVG autonome des points fournis.

    Les points non finis ou dont l'ordonnée vaut ``None`` interrompent le
    segment courant. Le titre est ajouté comme texte XML, jamais comme balise.
    """

    normalized: list[tuple[float, float] | None] = []
    finite_points: list[tuple[float, float]] = []
    for point in points:
        try:
            x_raw, y_raw = point
            if y_raw is None:
                normalized.append(None)
                continue
            x_value = float(x_raw)
            y_value = float(y_raw)
        except (TypeError, ValueError, OverflowError):
            normalized.append(None)
            continue
        if not math.isfinite(x_value) or not math.isfinite(y_value):
            normalized.append(None)
            continue
        clean_point = (x_value, y_value)
        normalized.append(clean_point)
        finite_points.append(clean_point)

    if not finite_points:
        raise ValueError("Aucun point fini ne peut être tracé.")

    x_values = [point[0] for point in finite_points]
    y_values = [point[1] for point in finite_points]
    data_x_min, data_x_max = min(x_values), max(x_values)
    data_y_min, data_y_max = min(y_values), max(y_values)
    if data_x_min == data_x_max:
        data_x_min -= 0.5
        data_x_max += 0.5
    if data_y_min == data_y_max:
        padding = max(0.5, abs(data_y_min) * 0.05)
        data_y_min -= padding
        data_y_max += padding

    x_padding = (data_x_max - data_x_min) * 0.04
    y_padding = (data_y_max - data_y_min) * 0.06
    x_low, x_high = data_x_min - x_padding, data_x_max + x_padding
    y_low, y_high = data_y_min - y_padding, data_y_max + y_padding

    width, height = 800.0, 500.0
    left, right, top, bottom = 60.0, 20.0, 35.0, 45.0
    plot_width = width - left - right
    plot_height = height - top - bottom

    def screen_x(value: float) -> float:
        return left + (value - x_low) / (x_high - x_low) * plot_width

    def screen_y(value: float) -> float:
        return top + (y_high - value) / (y_high - y_low) * plot_height

    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)

    def tag(name: str) -> str:
        return f"{{{namespace}}}{name}"

    root = ET.Element(
        tag("svg"),
        {
            "width": str(int(width)),
            "height": str(int(height)),
            "viewBox": f"0 0 {int(width)} {int(height)}",
            "role": "img",
        },
    )
    title_element = ET.SubElement(root, tag("title"))
    title_element.text = _valid_xml_text(title)
    ET.SubElement(
        root,
        tag("rect"),
        {
            "x": "0",
            "y": "0",
            "width": "100%",
            "height": "100%",
            "fill": "#ffffff",
        },
    )

    axes = ET.SubElement(root, tag("g"), {"stroke": "#68707a", "stroke-width": "1"})
    horizontal_axis = min(max(0.0, y_low), y_high)
    vertical_axis = min(max(0.0, x_low), x_high)
    ET.SubElement(
        axes,
        tag("line"),
        {
            "x1": f"{left:.3f}",
            "y1": f"{screen_y(horizontal_axis):.3f}",
            "x2": f"{width - right:.3f}",
            "y2": f"{screen_y(horizontal_axis):.3f}",
            "aria-label": "axe des abscisses",
        },
    )
    ET.SubElement(
        axes,
        tag("line"),
        {
            "x1": f"{screen_x(vertical_axis):.3f}",
            "y1": f"{top:.3f}",
            "x2": f"{screen_x(vertical_axis):.3f}",
            "y2": f"{height - bottom:.3f}",
            "aria-label": "axe des ordonnées",
        },
    )

    curves = ET.SubElement(
        root,
        tag("g"),
        {"fill": "none", "stroke": "#1769aa", "stroke-width": "2"},
    )

    def draw_segment(segment: list[tuple[float, float]]) -> None:
        if not segment:
            return
        if len(segment) == 1:
            x_value, y_value = segment[0]
            ET.SubElement(
                curves,
                tag("circle"),
                {
                    "cx": f"{screen_x(x_value):.3f}",
                    "cy": f"{screen_y(y_value):.3f}",
                    "r": "2",
                    "fill": "#1769aa",
                    "stroke": "none",
                },
            )
            return
        coordinates = " ".join(
            f"{screen_x(x_value):.3f},{screen_y(y_value):.3f}"
            for x_value, y_value in segment
        )
        ET.SubElement(curves, tag("polyline"), {"points": coordinates})

    segment: list[tuple[float, float]] = []
    for point in normalized:
        if point is None:
            draw_segment(segment)
            segment = []
        else:
            segment.append(point)
    draw_segment(segment)

    ET.indent(root, space="  ")
    tree = ET.ElementTree(root)
    try:
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
    except (OSError, TypeError, ValueError) as error:
        raise ValueError(f"Impossible d'écrire le SVG : {error}") from error


_HELP = """Commandes :
  <expression>                         évaluer une expression
  plot <expression>; <min>; <max>; <fichier.svg>
                                       tracer une courbe (201 points)
  history                              afficher l'historique réussi
  clear                                vider l'historique
  help                                 afficher cette aide
  quit | exit                          quitter

Fonctions : sin, cos, tan, asin, acos, atan, sqrt, ln, log10, exp, abs
Constantes : pi, e. Les angles sont en radians et ^ désigne la puissance.
"""


def _run_cli() -> None:
    history: list[str] = []
    print("Calculatrice scientifique — tapez help pour l'aide.")
    while True:
        try:
            raw_line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        line = raw_line.strip()
        if not line:
            continue
        command = line.lower()
        if command in {"quit", "exit"}:
            break
        if command == "help":
            print(_HELP)
            continue
        if command == "history":
            if history:
                for index, entry in enumerate(history, start=1):
                    print(f"{index}. {entry}")
            else:
                print("Historique vide.")
            continue
        if command == "clear":
            history.clear()
            print("Historique effacé.")
            continue

        try:
            if command == "plot" or command.startswith("plot "):
                arguments = line[4:].strip().split(";")
                if len(arguments) != 4 or any(not item.strip() for item in arguments):
                    raise ValueError(
                        "Syntaxe : plot expression; x_min; x_max; fichier.svg"
                    )
                expression, lower_text, upper_text, output_path = (
                    item.strip() for item in arguments
                )
                lower = evaluate(lower_text)
                upper = evaluate(upper_text)
                points = sample_curve(expression, lower, upper)
                write_svg(points, output_path, expression)
                history.append(line)
                print(f"Courbe enregistrée dans {output_path}")
            else:
                result = evaluate(line)
                history.append(line)
                print(result)
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur : {error}")


if __name__ == "__main__":
    _run_cli()
