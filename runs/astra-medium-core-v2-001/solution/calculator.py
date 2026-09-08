"""Calculatrice à deux opérandes, utilisable en Python ou en mode interactif."""


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
            raise ZeroDivisionError("Division par zéro impossible.")
        return float(left / right)
    raise ValueError("Opérateur inconnu : utilisez +, -, * ou /.")


def _parse_expression(line: str) -> tuple[float, str, float]:
    """Lit exactement deux nombres et un opérateur séparés par des blancs."""
    parts = line.split()
    if len(parts) != 3:
        raise ValueError("Expression invalide : saisissez nombre opérateur nombre (ex. 2 + 3).")
    left, operator, right = parts
    try:
        return float(left), operator, float(right)
    except ValueError:
        raise ValueError("Nombre invalide : utilisez un point pour les décimales.") from None


def main() -> None:
    """Lit les expressions jusqu'à quit, exit, EOF ou une interruption clavier."""
    try:
        while True:
            line = input("> ").strip()
            if line.lower() in ("quit", "exit"):
                return
            try:
                left, operator, right = _parse_expression(line)
                result = calculate(left, operator, right)
            except (ValueError, ZeroDivisionError) as error:
                print(f"Erreur : {error}")
            else:
                print(result)
    except (EOFError, KeyboardInterrupt):
        print()


if __name__ == "__main__":
    main()
