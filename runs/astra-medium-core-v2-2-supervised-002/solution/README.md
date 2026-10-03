# Calculatrice Python

Python 3 uniquement, sans dépendance externe.

Depuis le dossier parent de `solution/` :

```bash
python3 solution/calculator.py
```

Depuis `solution/`, utilisez `python3 calculator.py`.

Saisissez une expression par ligne, avec des espaces entre les deux nombres
et l'opérateur. Les opérations disponibles sont `+`, `-`, `*` et `/`.
Les nombres peuvent être entiers, décimaux (avec un point) ou négatifs.

Exemple de session (après le message d'accueil) :

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
Erreur : division par zéro impossible.
> quit
```

`quit` et `exit` terminent le programme. La fin de l'entrée (EOF) et Ctrl+C
sont également gérés proprement. Une expression invalide affiche une erreur
sans traceback et permet de saisir la suivante.

Les expressions doivent avoir exactement trois éléments : `2+3`, les
parenthèses et les enchaînements d'opérations ne sont pas pris en charge.
Le calcul utilise les flottants Python, avec leurs limites de précision
habituelles ; par exemple, `0.1 + 0.2` affiche `0.30000000000000004`.
La conversion des entrées utilise `float()`, qui accepte aussi la notation
scientifique et les valeurs spéciales `inf` et `nan`.

## Utilisation depuis Python

Depuis `solution/` :

```python
from calculator import calculate

result = calculate(-2.5, "*", 4)  # -10.0
```

`calculate(left: float, operator: str, right: float) -> float` accepte des
opérandes entiers ou flottants et renvoie un flottant. Une opération inconnue
lève `ValueError` ; une division par zéro (y compris `-0.0`) lève
`ZeroDivisionError`. L'importation ne lance pas la boucle interactive.
Aucune expression n'est exécutée comme du code Python.
