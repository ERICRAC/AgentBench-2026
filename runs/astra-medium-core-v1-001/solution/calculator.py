"""Calculatrice interactive, sans dépendance externe ni évaluation de code."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération arithmétique sur deux nombres.

    Lève ValueError pour un opérateur inconnu et ZeroDivisionError lorsque
    le diviseur est nul. Les arguments numériques peuvent être int ou float.
    """
    if operator == "+":
        return float(left + right)
    if operator == "-":
        return float(left - right)
    if operator == "*":
        return float(left * right)
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Division par zéro interdite.")
        return float(left / right)
    raise ValueError(f"Opérateur inconnu : {operator!r}. Utilisez +, -, * ou /.")


def main() -> None:
    """Lit les expressions jusqu'à quit, exit ou la fin de l'entrée."""
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if line.lower() in {"quit", "exit"}:
            return

        try:
            parts = line.split()
            if len(parts) != 3:
                raise ValueError("Format attendu : nombre opérateur nombre (exemple : 2 + 3).")
            left_text, operator, right_text = parts
            try:
                left = float(left_text)
                right = float(right_text)
            except ValueError:
                raise ValueError("Les deux opérandes doivent être des nombres (exemple : -2.5).") from None
            print(calculate(left, operator, right))
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}")


if __name__ == "__main__":
    main()
