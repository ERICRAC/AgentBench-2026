"""Calculatrice à quatre opérations, utilisable en Python ou en CLI."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération ou lève ValueError/ZeroDivisionError.

    Les opérandes doivent être des entiers ou des flottants Python.
    """
    if operator == "+":
        return float(left + right)
    if operator == "-":
        return float(left - right)
    if operator == "*":
        return float(left * right)
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro impossible")
        return float(left / right)
    raise ValueError("opération inconnue : utilisez +, -, * ou /")


def main() -> None:
    """Lit des expressions jusqu'à quit, exit ou la fin de l'entrée."""
    print("Calculatrice : nombre opérateur nombre (exemple : 2 + 3).")
    print("Tapez quit ou exit pour quitter.")
    while True:
        try:
            line = input("> ").strip()
            if line in ("quit", "exit"):
                return
            parts = line.split()
            if len(parts) != 3:
                print("Erreur : saisissez nombre opérateur nombre, séparés par des espaces.")
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
                print(f"Erreur : {error}.")
                continue
            print(result)
        except (EOFError, KeyboardInterrupt):
            print()
            return


if __name__ == "__main__":
    main()
