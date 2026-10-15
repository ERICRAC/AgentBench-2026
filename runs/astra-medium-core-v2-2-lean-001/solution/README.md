# Calculatrice

Calculatrice interactive Python 3, sans dépendance externe.

Depuis le dossier parent de `solution/`, lancez :

```bash
python3 solution/calculator.py
```

Depuis `solution/`, utilisez `python3 calculator.py`.

Saisissez un nombre, un opérateur et un nombre, séparés par des espaces.
Les opérateurs disponibles sont `+`, `-`, `*` et `/`. Les nombres peuvent
être entiers, décimaux (avec un point) ou négatifs.

Exemple de session :

```text
Calculatrice : saisissez une expression (2 + 3), quit ou exit.
> 2 + 3
5.0
> -2.5 * 4
-10.0
> 7 - 10
-3.0
> 9 / 2
4.5
> 1 / 0
Erreur : Division par zéro impossible.
> quit
```

Une expression invalide affiche une erreur et permet une nouvelle saisie.
`quit` ou `exit` termine le programme. La fin de l'entrée (Ctrl+D sous Unix)
et Ctrl+C terminent également proprement la boucle.

La fonction importable `calculate(left: float, operator: str, right: float)`
renvoie un `float`. Elle lève `ValueError` pour un opérateur inconnu et
`ZeroDivisionError` pour une division par zéro. L'import du module ne lance
pas la boucle interactive. Les calculs utilisent la précision usuelle des
flottants Python ; certains résultats décimaux peuvent être approximatifs.
