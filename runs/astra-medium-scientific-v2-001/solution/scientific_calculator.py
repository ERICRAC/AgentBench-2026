"""Calculatrice scientifique sûre, échantillonnage et SVG (Python >= 3.10)."""

import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


_FUNCTIONS = {name: getattr(math, name) for name in (
    'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'log10', 'exp'
)}
_FUNCTIONS.update(ln=math.log, abs=abs)
_CONSTANTS = {'pi': math.pi, 'e': math.e}
_NUMBER = r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?'


def _tokens(expression):
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError('Expression vide ou non textuelle.')
    result = []
    position = 0
    while position < len(expression):
        char = expression[position]
        if char.isspace():
            position += 1
            continue
        match = re.match(_NUMBER, expression[position:])
        if match:
            result.append(('number', match.group()))
            position += len(match.group())
            continue
        match = re.match(r'[A-Za-z_][A-Za-z_0-9]*', expression[position:])
        if match:
            result.append(('name', match.group()))
            position += len(match.group())
            continue
        if char in '+-*/^()':
            result.append((char, char))
            position += 1
            continue
        raise ValueError(f'Caractère interdit à la position {position + 1}.')
    return result + [('end', '')]


def _parse(expression):
    """Même grammaire descendante, avec pile explicite sans récursion Python."""
    tokens = _tokens(expression)
    index = 0
    code = []
    pending = [('require', 'end'), ('expression', None)]
    while pending:
        action, argument = pending.pop()
        if action == 'emit':
            code.append(argument)
            continue
        kind, value = tokens[index]
        if action == 'require':
            if kind != argument:
                raise ValueError(f'Syntaxe incorrecte : {argument} attendu.')
            index += 1
        elif action == 'expression':
            pending.extend([('sum_tail', None), ('term', None)])
        elif action == 'term':
            pending.extend([('product_tail', None), ('unary', None)])
        elif action in ('sum_tail', 'product_tail'):
            operators = ('+', '-') if action == 'sum_tail' else ('*', '/')
            if kind in operators:
                index += 1
                operand = 'term' if action == 'sum_tail' else 'unary'
                pending.extend([(action, None), ('emit', ('binary', kind)),
                                (operand, None)])
        elif action == 'unary':
            if kind in ('+', '-'):
                index += 1
                if kind == '-':
                    pending.append(('emit', ('negative', None)))
                pending.append(('unary', None))
            else:
                pending.extend([('power_tail', None), ('primary', None)])
        elif action == 'power_tail':
            if kind == '^':
                index += 1
                pending.extend([('emit', ('binary', '^')), ('unary', None)])
        elif action == 'primary':
            if kind == 'number':
                index += 1
                code.append(('number', value))
            elif kind == 'name':
                index += 1
                if value in _FUNCTIONS:
                    pending.extend([('emit', ('function', value)), ('require', ')'),
                                    ('expression', None), ('require', '(')])
                elif value in _CONSTANTS:
                    code.append(('number', _CONSTANTS[value]))
                elif value == 'x':
                    code.append(('variable', 'x'))
                else:
                    raise ValueError(f'Nom inconnu : {value}.')
            elif kind == '(':
                index += 1
                pending.extend([('require', ')'), ('expression', None)])
            else:
                raise ValueError('Syntaxe incorrecte : nombre, fonction ou parenthèse attendu.')
    return code


def _finite(value):
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Un nombre réel fini est requis.') from None
    if not math.isfinite(result):
        raise ValueError('Résultat non fini ou dépassement numérique.')
    return result


def _calculate(code, variables):
    stack = []
    try:
        for kind, value in code:
            if kind == 'number':
                result = _finite(value)
            elif kind == 'variable':
                if variables is None or 'x' not in variables:
                    raise ValueError('La variable x nécessite une valeur.')
                result = _finite(variables['x'])
            elif kind == 'negative':
                result = -stack.pop()
            elif kind == 'function':
                result = _FUNCTIONS[value](stack.pop())
            else:
                right, left = stack.pop(), stack.pop()
                if value == '+':
                    result = left + right
                elif value == '-':
                    result = left - right
                elif value == '*':
                    result = left * right
                elif value == '/':
                    if right == 0:
                        raise ZeroDivisionError('Division par zéro.')
                    result = left / right
                else:
                    result = math.pow(left, right)
            stack.append(_finite(result))
    except OverflowError:
        raise ValueError('Dépassement numérique.') from None
    except ValueError as error:
        raise ValueError(f'Calcul invalide dans le domaine réel : {error}') from None
    return stack[0]


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Évalue la grammaire fermée ; retourne un float fini ou une erreur."""
    if variables is not None and not isinstance(variables, dict):
        raise ValueError('Les variables doivent être un dictionnaire.')
    return _calculate(_parse(expression), variables)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Inclut les bornes exactes ; chaque échec numérique devient None."""
    if isinstance(x_min, bool) or isinstance(x_max, bool):
        raise ValueError('Les bornes doivent être des nombres réels, pas des booléens.')
    low, high = _finite(x_min), _finite(x_max)
    if low >= high:
        raise ValueError('Il faut x_min < x_max.')
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError('samples doit être un entier supérieur ou égal à 2.')
    code = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        if index == 0:
            x = low
        elif index == samples - 1:
            x = high
        elif low < 0 < high:
            x = (1 - fraction) * low + fraction * high
        else:
            x = low + fraction * (high - low)
        try:
            y = _calculate(code, {'x': x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def _projection(values, start, end):
    """Normaliser avant soustraction évite les étendues infinies."""
    low, high = min(values), max(values)
    if low == high:
        def constant(value):
            return (start + end) / 2 if value == low else (start if value < low else end)
        return constant, low, high
    scale = max(abs(low), abs(high))
    lo, hi = low / scale, high / scale

    def project(value):
        if value <= low:
            return start
        if value >= high:
            return end
        ratio = (value / scale - lo) / (hi - lo)
        return start + ratio * (end - start)

    return project, low, high


def _xml_text(text):
    """Remplace les caractères interdits en XML 1.0 avant sérialisation."""
    return ''.join(char if (ord(char) in (9, 10, 13)
                           or 0x20 <= ord(char) <= 0xD7FF
                           or 0xE000 <= ord(char) <= 0xFFFD
                           or 0x10000 <= ord(char) <= 0x10FFFF)
                   else '\uFFFD' for char in str(text))


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = '',
) -> None:
    """Écrit un SVG autonome ; une coordonnée invalide coupe le segment."""
    cleaned = []
    for point in points:
        try:
            x, y = point
            cleaned.append((_finite(x), _finite(y)))
        except (ValueError, TypeError):
            cleaned.append(None)
    finite = [point for point in cleaned if point is not None]
    if not finite:
        raise ValueError('Aucun point fini à tracer.')
    px, xmin, xmax = _projection([p[0] for p in finite], 60, 760)
    py, ymin, ymax = _projection([p[1] for p in finite], 440, 60)
    root = ET.Element('svg', xmlns='http://www.w3.org/2000/svg',
                      width='800', height='500', viewBox='0 0 800 500')
    ET.SubElement(root, 'title').text = _xml_text(title)
    ET.SubElement(root, 'rect', x='0', y='0', width='800', height='500', fill='white')
    ET.SubElement(root, 'text', x='60', y='28', fill='#111111').text = _xml_text(title)
    ET.SubElement(root, 'line', x1='60', y1=str(py(0)), x2='760', y2=str(py(0)),
                  stroke='#666666')
    ET.SubElement(root, 'line', x1=str(px(0)), y1='60', x2=str(px(0)), y2='440',
                  stroke='#666666')

    def draw(segment):
        if len(segment) == 1:
            x, y = segment[0]
            ET.SubElement(root, 'circle', cx=f'{px(x):.8f}', cy=f'{py(y):.8f}',
                          r='3', fill='#145aca')
        elif segment:
            coordinates = ' '.join(f'{px(x):.8f},{py(y):.8f}' for x, y in segment)
            ET.SubElement(root, 'polyline', points=coordinates, fill='none',
                          stroke='#145aca', **{'stroke-width': '2'})

    segment = []
    for point in cleaned:
        if point is None:
            draw(segment)
            segment = []
        else:
            segment.append(point)
    draw(segment)
    legend = f'x : [{xmin:.6g}, {xmax:.6g}] ; y : [{ymin:.6g}, {ymax:.6g}]'
    ET.SubElement(root, 'text', x='60', y='468', fill='#111111').text = legend
    if not xmin <= 0 <= xmax or not ymin <= 0 <= ymax:
        ET.SubElement(root, 'text', x='60', y='490', fill='#111111').text = (
            'Origine hors champ : axe correspondant au bord, sans représenter zéro.')
    document = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    Path(output_path).write_bytes(document)


_HELP = """Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Exemple : sqrt(2) ^ 2 ; la variable x est réservée aux tracés dans la CLI.
Tracé : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit."""


def _terminal_text(value):
    """Affiche les contrôles comme séquences littérales, jamais comme commandes."""
    return ''.join(char if char.isprintable() else ascii(char)[1:-1]
                   for char in str(value))


def _session() -> None:
    """Boucle interactive ; historique des seules opérations réussies."""
    history = []
    while True:
        try:
            line = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line:
            continue
        if line in ('quit', 'exit'):
            return
        if line == 'help':
            print(_HELP)
            continue
        if line == 'history':
            print('\n'.join(f'{i}. {_terminal_text(entry)}' for i, entry in enumerate(history, 1))
                  or 'Historique vide.')
            continue
        if line == 'clear':
            history.clear()
            print('Historique effacé.')
            continue
        try:
            if line.split(maxsplit=1)[0] == 'plot':
                parts = [part.strip() for part in line[4:].split(';')]
                if len(parts) != 4 or not all(parts):
                    raise ValueError('Syntaxe : plot expression; minimum; maximum; fichier.svg')
                expression, low, high, output = parts
                points = sample_curve(expression, evaluate(low), evaluate(high))
                write_svg(points, output, title=expression)
                print(f'Courbe enregistrée dans {_terminal_text(output)}')
            else:
                print(evaluate(line))
            history.append(line)
        except (ValueError, ZeroDivisionError, OSError, MemoryError) as error:
            print(f'Erreur : {_terminal_text(error) or "ressources insuffisantes"}')
        except KeyboardInterrupt:
            print('Opération interrompue.')


def main() -> None:
    """Protège également lecture et commandes de contrôle si un canal échoue."""
    try:
        _session()
    except (OSError, MemoryError) as error:
        try:
            print(f'Erreur : canal ou ressources indisponibles : {_terminal_text(error)}',
                  file=sys.stderr)
        except (OSError, MemoryError):
            pass  # Aucun diagnostic fiable si même le canal d'erreur est perdu.


if __name__ == '__main__':
    main()
