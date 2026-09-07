# Calculatrice en ligne de commande

Cette solution fournit les quatre opérations arithmétiques élémentaires :
addition (`+`), soustraction (`-`), multiplication (`*`) et division (`/`).
Elle utilise uniquement la bibliothèque standard de Python et n'évalue jamais
les expressions comme du code.

## Prérequis et lancement

Python 3.9 ou une version plus récente est nécessaire. Depuis le répertoire de
la tentative (`runs/sol-core-v1-001`), lancer :

```bash
python3 solution/calculator.py
```

Depuis le dossier `solution/` lui-même, la commande équivalente est :

```bash
python3 calculator.py
```

Depuis la racine du dépôt AgentBench, utiliser le chemin complet de la
tentative :

```bash
python3 runs/sol-core-v1-001/solution/calculator.py
```

## Utilisation

Saisir une expression par ligne sous la forme `nombre opérateur nombre`. Les
espaces séparent les trois éléments. Les entiers, les décimaux et les nombres
négatifs sont acceptés.

```text
> 2 + 3
Résultat : 5
> -4 * 2.5
Résultat : -10
> 7 / 2
Résultat : 3.5
> exit
```

Les commandes `quit` et `exit` arrêtent le programme. Une expression mal
formée, un opérateur inconnu ou une division par zéro affiche une erreur, puis
la calculatrice demande une nouvelle expression.

## Utilisation comme module Python

La fonction publique `calculate(left, operator, right)` peut aussi être
importée :

```python
from calculator import calculate

result = calculate(6, "/", 4)
print(result)  # 1.5
```

Elle lève `ValueError` si l'opérateur n'est pas l'un de `+`, `-`, `*`, `/`, et
`ZeroDivisionError` lors d'une division par zéro.
