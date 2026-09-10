"""Safe scientific expressions, finite sampling and standalone SVG (Python 3.10+)."""

import math
import re
from html import escape
from pathlib import Path


_FUNCTIONS = {
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
    'sqrt': math.sqrt, 'ln': math.log, 'log10': math.log10,
    'exp': math.exp, 'abs': abs,
}
_CONSTANTS = {'pi': math.pi, 'e': math.e}
_TOKEN = re.compile(r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?|[A-Za-z_][A-Za-z_0-9]*|[+*/^()\-]')


def _finite(value):
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError('Nombre réel fini requis') from error
    if not math.isfinite(number):
        raise ValueError('Résultat ou paramètre non fini')
    return number


class _Parser:
    """Recursive descent: power := atom ['^' unary], unary := sign unary | power."""

    def __init__(self, expression):
        if not isinstance(expression, str) or not expression.strip():
            raise ValueError('Expression vide ou invalide')
        if len(expression) > 10000:
            raise ValueError('Expression trop longue (maximum 10000 caractères)')
        self.tokens = []
        pos = 0
        while pos < len(expression):
            if expression[pos].isspace():
                pos += 1
                continue
            match = _TOKEN.match(expression, pos)
            if match is None:
                raise ValueError(f'Caractère interdit à la position {pos + 1}')
            self.tokens.append(match.group())
            pos = match.end()
        self.tokens.append('')
        self.index = 0

    def peek(self):
        return self.tokens[self.index]

    def take(self):
        token = self.peek()
        self.index += 1
        return token

    def parse(self):
        node = self.sum()
        if self.peek():
            raise ValueError(f'Élément inattendu : {self.peek()}')
        return node

    def sum(self):
        node = self.product()
        while self.peek() in ('+', '-'):
            node = (self.take(), node, self.product())
        return node

    def product(self):
        node = self.unary()
        while self.peek() in ('*', '/'):
            node = (self.take(), node, self.unary())
        return node

    def unary(self):
        if self.peek() in ('+', '-'):
            return ('unary', self.take(), self.unary())
        node = self.atom()
        if self.peek() == '^':
            self.take()
            node = ('^', node, self.unary())
        return node

    def atom(self):
        token = self.peek()
        if not token:
            raise ValueError('Expression incomplète')
        self.take()
        if token == '(':
            node = self.sum()
            self.close()
            return node
        if token in _FUNCTIONS:
            if self.peek() != '(':
                raise ValueError('Une fonction exige des parenthèses')
            self.take()
            node = ('call', token, self.sum())
            self.close()
            return node
        if token in _CONSTANTS:
            return ('number', _CONSTANTS[token])
        if token == 'x':
            return ('variable',)
        if token[0].isdigit() or token[0] == '.':
            return ('number', _finite(token))
        raise ValueError(f'Nom ou élément interdit : {token}')

    def close(self):
        if self.peek() != ')':
            raise ValueError('Parenthèse fermante attendue')
        self.take()


def _parse(expression):
    try:
        return _Parser(expression).parse()
    except RecursionError as error:
        raise ValueError('Expression trop complexe') from error


def _compute(node, variables):
    kind = node[0]
    if kind == 'number':
        return node[1]
    if kind == 'variable':
        if variables is None or 'x' not in variables:
            raise ValueError('Valeur de x manquante')
        return _finite(variables['x'])
    if kind == 'unary':
        value = _compute(node[2], variables)
        return value if node[1] == '+' else -value
    if kind == 'call':
        return _finite(_FUNCTIONS[node[1]](_compute(node[2], variables)))
    left, right = _compute(node[1], variables), _compute(node[2], variables)
    if kind == '+':
        value = left + right
    elif kind == '-':
        value = left - right
    elif kind == '*':
        value = left * right
    elif kind == '/':
        value = left / right
    else:
        value = math.pow(left, right)
    return _finite(value)


def _evaluate_tree(tree, variables):
    try:
        return _finite(_compute(tree, variables))
    except (OverflowError, RecursionError) as error:
        raise ValueError('Résultat hors limites ou expression trop complexe') from error


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Evaluate the allowed real grammar; division by zero remains a distinct error."""
    if variables is not None and not isinstance(variables, dict):
        raise ValueError('Les variables doivent être un dictionnaire')
    return _evaluate_tree(_parse(expression), variables)


def sample_curve(expression: str, x_min: float, x_max: float,
                 samples: int = 201) -> list[tuple[float, float | None]]:
    """Include endpoints and use None for domain errors at individual samples."""
    low, high = _finite(x_min), _finite(x_max)
    if low >= high:
        raise ValueError('Il faut x_min < x_max')
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError('Il faut au moins deux échantillons (entier)')
    tree = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        x = low if index == 0 else high if index == samples - 1 else low * (1 - fraction) + high * fraction
        try:
            y = _evaluate_tree(tree, {'x': x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def write_svg(points: list[tuple[float, float | None]], output_path: str,
              title: str = '') -> None:
    """Write inert XML with independent polylines separated by undefined points."""
    clean = []
    for x, y in points:
        try:
            clean.append((_finite(x), _finite(y)))
        except ValueError:
            clean.append(None)
    finite = [point for point in clean if point is not None]
    if not finite:
        raise ValueError('Aucun point fini à tracer')

    def projection(values, start, end):
        # Normalize before subtraction to avoid overflow for very large ranges.
        scale = max(1.0, max(abs(value) for value in values))
        low, high = min(values) / scale, max(values) / scale
        if low == high:
            low -= 0.5
            high += 0.5
        padding = (high - low) * 0.05
        low, high = low - padding, high + padding

        def project(value):
            fraction = (value / scale - low) / (high - low)
            return start + min(1.0, max(0.0, fraction)) * (end - start)
        return project

    px = projection([p[0] for p in finite], 60, 760)
    py = projection([p[1] for p in finite], 440, 60)
    safe_title = escape(str(title), quote=True)
    # XML 1.0 forbids control characters even in escaped text.
    safe_title = ''.join(c for c in safe_title if c in '\t\n\r' or
                         0x20 <= ord(c) <= 0xD7FF or
                         0xE000 <= ord(c) <= 0xFFFD or
                         0x10000 <= ord(c) <= 0x10FFFF)
    svg = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="500" viewBox="0 0 800 500">',
           f'<title>{safe_title}</title>',
           '<rect width="800" height="500" fill="white"/>',
           f'<text x="400" y="30" text-anchor="middle" fill="black">{safe_title}</text>',
           f'<line x1="60" y1="{py(0):.6f}" x2="760" y2="{py(0):.6f}" stroke="#555"/>',
           f'<line x1="{px(0):.6f}" y1="60" x2="{px(0):.6f}" y2="440" stroke="#555"/>']
    segment = []

    def flush():
        if segment:
            svg.append('<polyline fill="none" stroke="#1565c0" stroke-width="2" points="' + ' '.join(segment) + '"/>')
            if len(segment) == 1:
                cx, cy = segment[0].split(',')
                svg.append(f'<circle cx="{cx}" cy="{cy}" r="2" fill="#1565c0"/>')
            segment.clear()

    for point in clean:
        if point is None:
            flush()
        else:
            segment.append(f'{px(point[0]):.6f},{py(point[1]):.6f}')
    flush()
    svg.append('</svg>')
    Path(output_path).write_text('\n'.join(svg) + '\n', encoding='utf-8')


_HELP = '''Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Tracé : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit.'''


def main():
    """Interactive session; only successful evaluations and plots enter history."""
    history = []
    while True:
        try:
            command = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not command:
            continue
        if command in ('quit', 'exit'):
            break
        try:
            if command == 'help':
                print(_HELP)
            elif command == 'history':
                print('\n'.join(history) if history else 'Historique vide')
            elif command == 'clear':
                history.clear()
                print('Historique effacé')
            elif command == 'plot' or command.startswith(('plot ', 'plot\t')):
                fields = [part.strip() for part in command[4:].split(';')]
                if len(fields) != 4 or not all(fields):
                    raise ValueError('Syntaxe : plot expression; x_min; x_max; fichier.svg')
                expression, low, high, path = fields
                points = sample_curve(expression, evaluate(low), evaluate(high))
                write_svg(points, path, title=expression)
                print(f'Courbe enregistrée dans {path}')
                history.append(command)
            else:
                result = evaluate(command)
                print(result)
                history.append(f'{command} = {result}')
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f'Erreur : {error}')
        except KeyboardInterrupt:
            print('Opération interrompue')


if __name__ == '__main__':
    main()
