"""Calculatrice binaire : API indépendante et boucle interactive."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calculer avec +, -, * ou / sur des arguments numériques.

    Lever ValueError pour un opérateur inconnu et ZeroDivisionError pour
    une division par zéro, y compris -0.0. Ne réaliser aucune entrée-sortie.
    """
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Division par zéro impossible.")
        return left / right
    raise ValueError("Opérateur inconnu : utilisez +, -, * ou /.")


def parse_expression(line: str) -> tuple[float, str, float]:
    """Lire exactement deux nombres et un opérateur séparés par des blancs.

    Les nombres suivent la syntaxe de float ; calculate valide l'opérateur.
    Lever ValueError si le format ou un nombre est invalide.
    """
    parts = line.split()
    if len(parts) != 3:
        raise ValueError(
            "Expression invalide : saisissez nombre opérateur nombre "
            "avec des espaces, par exemple 2 + 3."
        )
    left_text, operator, right_text = parts
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        raise ValueError(
            "Nombre invalide : utilisez des nombres avec un point décimal "
            "si nécessaire, par exemple -2.5."
        ) from None
    return left, operator, right


def main() -> None:
    """Lire les expressions jusqu'à quit, exit, EOF ou une interruption."""
    try:
        while True:
            try:
                line = input("> ")
            except EOFError:
                return
            if line.strip().lower() in ("quit", "exit"):
                return
            try:
                left, operator, right = parse_expression(line)
                result = calculate(left, operator, right)
            except (ValueError, ZeroDivisionError) as error:
                print(f"Erreur : {error}")
            else:
                print(result)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
