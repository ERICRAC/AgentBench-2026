#!/usr/bin/env python3
"""Calculatrice arithmétique simple et interface en ligne de commande."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule ``left operator right``.

    Les seuls opérateurs acceptés sont ``+``, ``-``, ``*`` et ``/``.

    Raises:
        ValueError: si l'opérateur n'est pas pris en charge.
        ZeroDivisionError: en cas de division par zéro.
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
    """Convertit une expression ``nombre opérateur nombre`` en ses éléments."""
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("format attendu : nombre opérateur nombre")

    left_text, operator, right_text = parts
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError as error:
        raise ValueError("les deux opérandes doivent être des nombres") from error

    return left, operator, right


def format_result(result: float) -> str:
    """Affiche les résultats entiers sans partie décimale superflue."""
    if result.is_integer():
        return str(int(result))
    return str(result)


def main() -> int:
    """Lance la boucle interactive jusqu'à ``quit``, ``exit`` ou la fin de saisie."""
    print("Calculatrice (+, -, *, /). Saisissez 'quit' ou 'exit' pour quitter.")

    while True:
        try:
            expression = input(">>> ").strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\nArrêt de la calculatrice.")
            break

        if expression.lower() in {"quit", "exit"}:
            break
        if not expression:
            print("Erreur : saisissez une expression, par exemple 2 + 3.")
            continue

        try:
            left, operator, right = parse_expression(expression)
            result = calculate(left, operator, right)
        except ZeroDivisionError:
            print("Erreur : division par zéro impossible.")
        except ValueError as error:
            print(f"Erreur : expression invalide ({error}).")
        else:
            print(format_result(result))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
