# Calculator

Cette calculatrice Python exécute une opération binaire parmi l'addition, la
soustraction, la multiplication et la division. Elle n'utilise que la
bibliothèque standard.

## Lancement

Depuis la racine du dépôt, entrer dans le répertoire de la tentative puis
lancer la commande prévue par le contrat :

```bash
cd runs/sol-core-v2-001
python3 solution/calculator.py
```

La calculatrice reste active jusqu'à la saisie de `quit` ou `exit`. Une fin de
flux (Ctrl-D) ou une interruption (Ctrl-C) la termine également proprement.

## Utilisation

Saisir exactement deux nombres et un opérateur, séparés par un ou plusieurs
espaces :

```text
2 + 3
10 - 4
-2 * -3.5
7 / 2
```

Les opérateurs disponibles sont uniquement `+`, `-`, `*` et `/`. Les entiers,
les nombres décimaux et les nombres négatifs sont acceptés. Les formes sans
espaces, comme `2+3`, et les expressions composées ne font pas partie de la
syntaxe prise en charge.

Exemple de session :

```text
Expression (ou 'quit'/'exit') : 2 + 3
5.0
Expression (ou 'quit'/'exit') : -2 * -3.5
7.0
Expression (ou 'quit'/'exit') : 4 / 0
Erreur : division par zéro impossible
Expression (ou 'quit'/'exit') : 2+3
Erreur : format attendu : nombre opérateur nombre
Expression (ou 'quit'/'exit') : quit
```

Une saisie incorrecte ou une division par zéro produit un message d'erreur,
sans traceback, puis la calculatrice attend l'expression suivante.

## Utilisation comme module

La logique métier peut être importée sans démarrer l'interface interactive.
Depuis la racine du dépôt :

```bash
cd runs/sol-core-v2-001/solution
python3
```

Puis, dans l'interpréteur Python :

```python
from calculator import calculate

result = calculate(6, "/", 4)
print(result)  # 1.5
```

`calculate(left, operator, right)` lève `ValueError` pour un opérateur inconnu
et `ZeroDivisionError` pour une division par zéro.
