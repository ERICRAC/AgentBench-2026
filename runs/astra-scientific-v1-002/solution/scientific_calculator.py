"""Calculatrice réelle sûre et export SVG, avec la bibliothèque standard.

L'analyseur produit des instructions postfixées, interprétées sans exécution
dynamique. Voir README.md pour la grammaire, les bornes et les exemples.
"""

from __future__ import annotations

import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path


_FUNCTIONS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sqrt": math.sqrt, "ln": math.log, "log10": math.log10,
    "exp": math.exp, "abs": abs,
}
_CONSTANTS = {"pi": math.pi, "e": math.e}
_TOKEN = re.compile(
    r"(?P<number>(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?)"
    r"|(?P<name>[A-Za-z_][A-Za-z_0-9]*)|(?P<symbol>[+*/^()-])"
)
_MAX_LENGTH = 10000
_MAX_TOKENS = 2048
_MAX_DEPTH = 100


def _finite(value: object) -> float:
    """Accepte uniquement les nombres réels Python finis (hors booléens)."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Un nombre réel fini est requis.")
    try:
        result = float(value)
    except (OverflowError, ValueError) as error:
        raise ValueError("Nombre hors des limites flottantes.") from error
    if not math.isfinite(result):
        raise ValueError("Le résultat doit être fini.")
    return result


class _Parser:
    """Descente récursive bornée ; les sommes et produits sont itératifs."""

    def __init__(self, expression: str):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError("Expression vide ou invalide.")
        if len(expression) > _MAX_LENGTH:
            raise ValueError("Expression trop longue (10000 caractères maximum).")
        self.tokens: list[tuple[str, str]] = []
        position = 0
        while position < len(expression):
            if expression[position].isspace():
                position += 1
                continue
            match = _TOKEN.match(expression, position)
            if match is None:
                raise ValueError(f"Caractère interdit à la position {position + 1}.")
            self.tokens.append((match.lastgroup, match.group()))
            if len(self.tokens) > _MAX_TOKENS:
                raise ValueError("Expression trop complexe (2048 jetons maximum).")
            position = match.end()
        self.tokens.append(("end", ""))
        self.index = 0
        self.code: list[tuple[str, object]] = []

    def accept(self, symbol: str) -> bool:
        if self.tokens[self.index][1] == symbol:
            self.index += 1
            return True
        return False

    def require(self, symbol: str) -> None:
        if not self.accept(symbol):
            raise ValueError(f"Symbole attendu : {symbol}")

    def parse(self) -> list[tuple[str, object]]:
        try:
            self.expression(0)
        except RecursionError as error:
            raise ValueError("Expression trop profondément imbriquée.") from error
        if self.tokens[self.index][0] != "end":
            raise ValueError("Expression mal formée : opérateur ou fin attendu.")
        return self.code

    def expression(self, depth: int) -> None:
        self.product(depth)
        while self.tokens[self.index][1] in ("+", "-"):
            operator = self.tokens[self.index][1]
            self.index += 1
            self.product(depth)
            self.code.append(("binary", operator))

    def product(self, depth: int) -> None:
        self.unary(depth)
        while self.tokens[self.index][1] in ("*", "/"):
            operator = self.tokens[self.index][1]
            self.index += 1
            self.unary(depth)
            self.code.append(("binary", operator))

    def unary(self, depth: int) -> None:
        if depth > _MAX_DEPTH:
            raise ValueError("Expression trop profondément imbriquée (limite 100).")
        if self.accept("+"):
            self.unary(depth + 1)
        elif self.accept("-"):
            self.unary(depth + 1)
            self.code.append(("negate", None))
        else:
            self.primary(depth)
            if self.accept("^"):
                self.unary(depth + 1)
                self.code.append(("binary", "^"))

    def primary(self, depth: int) -> None:
        kind, value = self.tokens[self.index]
        if kind == "number":
            self.index += 1
            self.code.append(("number", _finite(float(value))))
        elif self.accept("("):
            self.expression(depth + 1)
            self.require(")")
        elif kind == "name":
            self.index += 1
            if value in _CONSTANTS:
                self.code.append(("number", _CONSTANTS[value]))
            elif value == "x":
                self.code.append(("variable", "x"))
            elif value in _FUNCTIONS:
                self.require("(")
                self.expression(depth + 1)
                self.require(")")
                self.code.append(("function", value))
            else:
                raise ValueError(f"Nom inconnu : {value}")
        else:
            raise ValueError("Nombre, fonction ou parenthèse attendu.")


def _run(code: list[tuple[str, object]], variables: dict[str, float]) -> float:
    stack: list[float] = []
    try:
        for kind, value in code:
            if kind == "number":
                stack.append(value)
            elif kind == "variable":
                if "x" not in variables:
                    raise ValueError("La variable x nécessite une valeur.")
                stack.append(_finite(variables["x"]))
            elif kind == "negate":
                stack[-1] = -stack[-1]
            elif kind == "function":
                stack[-1] = _finite(_FUNCTIONS[value](stack[-1]))
            else:
                right = stack.pop()
                left = stack.pop()
                if value == "+":
                    result = left + right
                elif value == "-":
                    result = left - right
                elif value == "*":
                    result = left * right
                elif value == "/":
                    if right == 0:
                        raise ZeroDivisionError("Division par zéro.")
                    result = left / right
                else:
                    result = math.pow(left, right)
                stack.append(_finite(result))
    except (OverflowError, ValueError) as error:
        raise ValueError(f"Expression hors du domaine réel fini : {error}") from error
    return stack[0]


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Évalue la grammaire autorisée ; erreurs : ValueError ou ZeroDivisionError.

    Seule la clé x est consultée. Les autres clés ne créent aucun nom utilisable.
    Les résultats intermédiaires doivent également rester réels et finis.
    """
    if variables is not None and not isinstance(variables, dict):
        raise ValueError("Les variables doivent être fournies dans un dictionnaire.")
    return _run(_Parser(expression).parse(), {} if variables is None else variables)


def sample_curve(
    expression: str, x_min: float, x_max: float, samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne uniformément, bornes incluses ; les erreurs locales sont None.

    Une erreur de syntaxe est rejetée avant l'échantillonnage. Aucune détection
    symbolique des singularités situées entre deux échantillons n'est effectuée.
    """
    x_min, x_max = _finite(x_min), _finite(x_max)
    if x_min >= x_max:
        raise ValueError("Les bornes doivent vérifier x_min < x_max.")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("Le nombre d'échantillons doit être un entier au moins égal à 2.")
    code = _Parser(expression).parse()
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        # Signes opposés : éviter le débordement de la différence.
        # Même signe : préserver l'intervalle pour des bornes très voisines.
        if x_min < 0 < x_max:
            x = (1 - fraction) * x_min + fraction * x_max
        else:
            x = x_min + fraction * (x_max - x_min)
        if index == 0:
            x = x_min
        elif index == samples - 1:
            x = x_max
        try:
            y = _run(code, {"x": x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def _xml_text(value: str) -> str:
    """Remplace les caractères non représentables en XML 1.0."""
    return "".join(
        char if (char in "\t\n\r" or 0x20 <= ord(char) <= 0xD7FF
                 or 0xE000 <= ord(char) <= 0xFFFD
                 or 0x10000 <= ord(char) <= 0x10FFFF) else "\ufffd"
        for char in value
    )


def _ratio(value: float, lower: float, upper: float) -> float:
    if lower == upper:
        return 0.5
    scale = max(abs(lower), abs(upper))
    return (value / scale - lower / scale) / (upper / scale - lower / scale)


def write_svg(
    points: list[tuple[float, float | None]], output_path: str, title: str = "",
) -> None:
    """Écrit un SVG statique autonome ; chaque point invalide coupe la courbe.

    Les axes sont rabattus sur le bord du cadre si zéro est hors de l'intervalle.
    Les points finis isolés sont représentés par un cercle.
    """
    if not isinstance(title, str):
        raise ValueError("Le titre doit être une chaîne de caractères.")
    normalized: list[tuple[float, float] | None] = []
    for point in points:
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            raise ValueError("Chaque point doit être un couple (x, y).")
        x, y = point
        try:
            normalized.append((_finite(x), _finite(y)))
        except ValueError:
            normalized.append(None)
    finite_points = [point for point in normalized if point is not None]
    if not finite_points:
        raise ValueError("Aucun point fini à tracer.")
    x_min = min(point[0] for point in finite_points)
    x_max = max(point[0] for point in finite_points)
    y_min = min(point[1] for point in finite_points)
    y_max = max(point[1] for point in finite_points)

    def px(x: float) -> float:
        return 65 + 705 * _ratio(x, x_min, x_max)

    def py(y: float) -> float:
        return 445 - 385 * _ratio(y, y_min, y_max)

    root = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg", "width": "800", "height": "500",
        "viewBox": "0 0 800 500", "role": "img",
    })
    ET.SubElement(root, "title").text = _xml_text(title or "Courbe scientifique")
    ET.SubElement(root, "rect", {
        "width": "800", "height": "500", "fill": "#ffffff",
    })
    ET.SubElement(root, "text", {
        "x": "400", "y": "30", "text-anchor": "middle", "fill": "#172033",
        "font-family": "sans-serif", "font-size": "18",
    }).text = _xml_text(title)
    axis_x = px(min(max(0.0, x_min), x_max))
    axis_y = py(min(max(0.0, y_min), y_max))
    for attributes in (
        {"x1": "65", "y1": str(axis_y), "x2": "770", "y2": str(axis_y)},
        {"x1": str(axis_x), "y1": "60", "x2": str(axis_x), "y2": "445"},
    ):
        ET.SubElement(root, "line", {**attributes, "stroke": "#697386", "stroke-width": "1"})
    for x, y, label, anchor in (
        (65, 470, f"x min : {x_min:.6g}", "start"),
        (770, 470, f"x max : {x_max:.6g}", "end"),
        (65, 53, f"y max : {y_max:.6g}", "start"),
        (65, 490, f"y min : {y_min:.6g}", "start"),
    ):
        ET.SubElement(root, "text", {
            "x": str(x), "y": str(y), "text-anchor": anchor,
            "font-family": "sans-serif", "font-size": "12", "fill": "#172033",
        }).text = label

    def add_segment(segment: list[tuple[float, float]]) -> None:
        if len(segment) == 1:
            ET.SubElement(root, "circle", {
                "cx": f"{px(segment[0][0]):.6f}",
                "cy": f"{py(segment[0][1]):.6f}", "r": "2", "fill": "#195dc5",
            })
        elif segment:
            ET.SubElement(root, "polyline", {
                "points": " ".join(f"{px(x):.6f},{py(y):.6f}" for x, y in segment),
                "fill": "none", "stroke": "#195dc5", "stroke-width": "2",
                "stroke-linejoin": "round",
            })

    segment: list[tuple[float, float]] = []
    for point in normalized:
        if point is None:
            add_segment(segment)
            segment = []
        else:
            segment.append(point)
    add_segment(segment)
    document = ET.tostring(root, encoding="unicode", xml_declaration=True)
    Path(output_path).write_text(document, encoding="utf-8")


_HELP = """Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Exemples : -2^2 ; sqrt(2)^2 ; 2^3^2.
Tracé : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit.
La variable x est disponible pour les tracés. Les fichiers existants sont écrasés."""


def main() -> None:
    """Boucle interactive : seules les opérations réussies entrent dans l'historique."""
    history: list[str] = []
    print("Calculatrice scientifique — help pour l'aide.")
    while True:
        try:
            command = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not command:
            continue
        if command in ("quit", "exit"):
            return
        try:
            if command == "help":
                print(_HELP)
            elif command == "history":
                print("\n".join(f"{index}. {entry}" for index, entry in enumerate(history, 1))
                      or "Historique vide.")
            elif command == "clear":
                history.clear()
                print("Historique effacé.")
            elif command.split(maxsplit=1)[0] == "plot":
                parts = [part.strip() for part in command[4:].split(";")]
                if len(parts) != 4 or not all(parts):
                    raise ValueError("Syntaxe : plot expression; x_min; x_max; fichier.svg")
                expression, lower, upper, output_path = parts
                points = sample_curve(expression, evaluate(lower), evaluate(upper))
                write_svg(points, output_path, title=expression)
                print(f"Courbe enregistrée dans {output_path}")
                history.append(command)
            else:
                result = evaluate(command)
                print(result)
                history.append(f"{command} = {result}")
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur : {error}")
        except KeyboardInterrupt:
            print("Opération interrompue.")


if __name__ == "__main__":
    main()
