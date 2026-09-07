"""Calculatrice élémentaire et interface en ligne de commande.

Le module expose :func:`calculate` pour un usage depuis Python. Lorsqu'il est
exécuté directement, il lit une expression par ligne jusqu'à ``quit`` ou
``exit``.
"""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule ``left operator right`` avec une des quatre opérations admises.

    Args:
        left: Opérande situé à gauche de l'opérateur.
        operator: Un des opérateurs ``+``, ``-``, ``*`` ou ``/``.
        right: Opérande situé à droite de l'opérateur.

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


def _parse_expression(expression: str) -> tuple[float, str, float]:
    """Convertit une expression ``nombre opérateur nombre`` en opérandes."""
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


def main() -> int:
    """Lance la boucle interactive et renvoie un code de sortie réussi."""
    print("Calculatrice (+, -, *, /). Saisissez 'quit' ou 'exit' pour quitter.")

    while True:
        try:
            expression = input("> ").strip()
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print("\nArrêt de la calculatrice.")
            break

        if expression.lower() in {"quit", "exit"}:
            break
        if not expression:
            print("Erreur : expression vide.")
            continue

        try:
            left, operator, right = _parse_expression(expression)
            result = calculate(left, operator, right)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}.")
            continue

        print(f"Résultat : {result:g}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
