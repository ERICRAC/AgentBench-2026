# Calculatrice en ligne de commande

Cette solution fournit les quatre opérations arithmétiques demandées :
addition (`+`), soustraction (`-`), multiplication (`*`) et division (`/`).
Elle utilise uniquement la bibliothèque standard de Python.

## Lancement

Depuis le dossier de cette tentative :

```bash
python3 solution/calculator.py
```

Saisir une expression composée de deux nombres et d'un opérateur, séparés
par des espaces. Les entiers, les nombres décimaux et les nombres négatifs
sont acceptés.

```text
>>> 2 + 3
5
>>> -4 * 2.5
-10
>>> 7 / 2
3.5
```

Les commandes `quit` et `exit` ferment la calculatrice. Une expression mal
formée, un opérateur inconnu ou une division par zéro affiche une erreur sans
interrompre la session.

## Utilisation comme module

La fonction publique `calculate(left, operator, right)` peut être importée :

```python
from calculator import calculate

result = calculate(12, "/", 4)
print(result)  # 3.0
```

Elle lève `ValueError` pour un opérateur non pris en charge et
`ZeroDivisionError` pour une division par zéro.
