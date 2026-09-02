#!/usr/bin/env python3
"""Calculatrice élémentaire et interface interactive en ligne de commande."""


SUPPORTED_OPERATORS = {"+", "-", "*", "/"}


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule ``left operator right``.

    Args:
        left: Opérande de gauche.
        operator: L'un des quatre opérateurs pris en charge : +, -, * ou /.
        right: Opérande de droite.

    Raises:
        ValueError: Si l'opérateur n'est pas pris en charge.
        ZeroDivisionError: En cas de division par zéro.
    """
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro")
        return left / right
    raise ValueError(f"opérateur inconnu : {operator!r}")


def parse_expression(expression: str) -> tuple[float, str, float]:
    """Analyse une expression composée de deux nombres et d'un opérateur."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("format attendu : nombre opérateur nombre (ex. 2 + 3)")

    left_text, operator, right_text = parts
    if operator not in SUPPORTED_OPERATORS:
        raise ValueError(f"opérateur inconnu : {operator!r}")

    try:
        return float(left_text), operator, float(right_text)
    except ValueError as error:
        raise ValueError("les deux opérandes doivent être des nombres") from error


def main() -> int:
    """Lance la boucle interactive jusqu'à ``quit``, ``exit`` ou la fin du flux."""
    print("Calculatrice (+, -, *, /). Tapez 'quit' ou 'exit' pour quitter.")

    while True:
        try:
            expression = input("> ").strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\nAu revoir.")
            break

        if expression.lower() in {"quit", "exit"}:
            break
        if not expression:
            print("Erreur : expression vide.")
            continue

        try:
            left, operator, right = parse_expression(expression)
            print(calculate(left, operator, right))
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
