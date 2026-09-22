# Calculatrice Python

Python 3 suffit ; aucune dépendance à installer.

Depuis le dossier parent de `solution/`, lancer :

```bash
python3 solution/calculator.py
```

Depuis `solution/`, utiliser `python3 calculator.py`.

Saisir une expression par ligne avec des espaces entre le nombre de gauche,
l'opérateur et le nombre de droite. Les opérateurs disponibles sont `+`, `-`,
`*` et `/`. Les nombres peuvent être entiers, décimaux (avec un point) ou
négatifs. Les résultats sont affichés sous forme de nombres flottants.

Exemple de session, après le message d'accueil :

```text
> 2 + 3
5.0
> -2.5 * 4
-10.0
> 7 - 10
-3.0
> 9 / 2
4.5
> 1 / 0
Erreur : division par zéro impossible
> quit
```

`quit` et `exit` terminent la boucle. Une fin d'entrée (EOF) ou Ctrl+C au
moment de la saisie termine également le programme proprement. Une expression
invalide affiche une erreur et permet une nouvelle saisie. `2+3` sans espaces,
les parenthèses et les expressions composées ne sont pas pris en charge.

La fonction métier peut être importée depuis le dossier `solution/` :

```python
from calculator import calculate

result = calculate(-2.5, "*", 4)  # -10.0
```

`calculate(left: float, operator: str, right: float) -> float` lève
`ValueError` pour un opérateur inconnu et `ZeroDivisionError` pour une division
par zéro. L'import ne lance pas la boucle interactive. Les calculs utilisent
l'arithmétique flottante de Python, avec ses limites de précision habituelles
(par exemple, `0.1 + 0.2` peut afficher `0.30000000000000004`).
