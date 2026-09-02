# Calculator

Cette solution fournit une calculatrice Python sans dépendance externe. Elle
prend en charge l'addition (`+`), la soustraction (`-`), la multiplication (`*`)
et la division (`/`) sur les entiers, les décimaux et les nombres négatifs.

## Lancement

Depuis la racine de cette tentative :

```bash
python3 solution/calculator.py
```

Saisissez une expression avec des espaces entre les deux opérandes et
l'opérateur. Tapez `quit` ou `exit` pour terminer.

```text
> 2 + 3
5.0
> -4 * 2
-8.0
> 7 / 2
3.5
> quit
```

Une saisie incorrecte ou une division par zéro affiche un message d'erreur,
puis la calculatrice attend une nouvelle expression.

## Utilisation comme module

La fonction `calculate(left, operator, right)` peut aussi être importée :

```python
from calculator import calculate

result = calculate(1.5, "*", 2)
```

Elle lève `ValueError` si l'opérateur est inconnu et `ZeroDivisionError` en cas
de division par zéro.
