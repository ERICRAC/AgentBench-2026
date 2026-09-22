"""Calculatrice arithmétique et interface interactive, sans dépendance externe."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération ; lève ValueError ou ZeroDivisionError si nécessaire."""
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
    """Lit une expression par ligne et continue après les erreurs de saisie."""
    print("Calculatrice : nombre opérateur nombre (exemple : 2 + 3).")
    print("Tapez quit ou exit pour terminer.")
    while True:
        try:
            expression = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if expression in ("quit", "exit"):
            return
        try:
            parts = expression.split()
            if len(parts) != 3:
                raise ValueError("format attendu : nombre opérateur nombre, séparés par des espaces")
            left_text, operator, right_text = parts
            try:
                left, right = float(left_text), float(right_text)
            except ValueError:
                raise ValueError("nombres invalides : utilisez un point pour les décimales") from None
            print(calculate(left, operator, right))
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print(f"Erreur : {error}")


if __name__ == "__main__":
    main()
