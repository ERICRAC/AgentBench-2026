"""Calculatrice interactive utilisant uniquement la bibliothèque standard."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération ; propage les erreurs d'opérateur et de division."""
    if operator == "+":
        return float(left + right)
    if operator == "-":
        return float(left - right)
    if operator == "*":
        return float(left * right)
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Division par zéro impossible.")
        return float(left / right)
    raise ValueError(f"Opération inconnue : {operator!r}. Utilisez +, -, * ou /.")


def main() -> None:
    """Lit les expressions jusqu'à quit, exit ou la fin de l'entrée."""
    print("Calculatrice : saisissez une expression (2 + 3), quit ou exit.")
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if line.lower() in ("quit", "exit"):
            return

        parts = line.split()
        if len(parts) != 3:
            print("Erreur : saisissez deux nombres et un opérateur séparés par des espaces (2 + 3).")
            continue

        left_text, operator, right_text = parts
        try:
            left = float(left_text)
            right = float(right_text)
        except ValueError:
            print("Erreur : les deux opérandes doivent être des nombres (exemple : -2.5).")
            continue

        try:
            result = calculate(left, operator, right)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}")
            continue
        print(result)


if __name__ == "__main__":
    main()
