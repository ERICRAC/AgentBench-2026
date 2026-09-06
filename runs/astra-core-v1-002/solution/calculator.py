"""Calculatrice interactive, utilisant uniquement la bibliothèque standard."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération arithmétique et renvoie un flottant.

    Lève ValueError si l'opérateur est inconnu et ZeroDivisionError si
    une division a un dénominateur nul.
    """
    if operator == "+":
        return float(left + right)
    if operator == "-":
        return float(left - right)
    if operator == "*":
        return float(left * right)
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro")
        return float(left / right)
    raise ValueError(f"opération inconnue : {operator!r} ; utiliser +, -, * ou /")


def main() -> None:
    """Lit une expression par ligne jusqu'à quit, exit ou la fin de l'entrée."""
    while True:
        try:
            line = input().strip()
        except (EOFError, KeyboardInterrupt):
            return

        if line.lower() in ("quit", "exit"):
            return

        parts = line.split()
        if len(parts) != 3:
            print("Erreur : saisir une expression sous la forme 2 + 3 (avec espaces).")
            continue

        left_text, operator, right_text = parts
        try:
            left = float(left_text)
            right = float(right_text)
        except ValueError:
            print("Erreur : les deux opérandes doivent être des nombres, par exemple -2.5.")
            continue

        try:
            result = calculate(left, operator, right)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}.")
        else:
            print(result)


if __name__ == "__main__":
    main()
