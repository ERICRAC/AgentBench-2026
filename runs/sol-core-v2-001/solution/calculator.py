"""Calculatrice binaire simple et interface en ligne de commande."""

from typing import Tuple


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération arithmétique binaire.

    Args:
        left: Opérande de gauche.
        operator: L'un des opérateurs ``+``, ``-``, ``*`` ou ``/``.
        right: Opérande de droite.

    Returns:
        Le résultat de l'opération.

    Raises:
        ValueError: Si l'opérateur n'est pas pris en charge.
        ZeroDivisionError: Si une division par zéro est demandée.
    """
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro impossible")
        return left / right
    raise ValueError("opérateur inconnu (utilisez +, -, * ou /)")


def _parse_expression(line: str) -> Tuple[float, str, float]:
    """Analyse une expression composée de deux nombres et d'un opérateur."""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("format attendu : nombre opérateur nombre")

    left_text, operator, right_text = parts
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        raise ValueError("les opérandes doivent être des nombres") from None

    return left, operator, right


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""
    try:
        while True:
            line = input("Expression (ou 'quit'/'exit') : ")

            if line.strip() in {"quit", "exit"}:
                break

            try:
                left, operator, right = _parse_expression(line)
                result = calculate(left, operator, right)
            except (ValueError, ZeroDivisionError) as error:
                print(f"Erreur : {error}")
                continue

            print(result)
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()
