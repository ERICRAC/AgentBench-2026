# Calculatrice Python

Solution du défi Calculator en mode V1, réalisée par le candidat Codex seul,
sans consultant ni sous-agent. Python 3 et sa bibliothèque standard suffisent.

## Lancement

Depuis le dossier de la tentative :

```bash
python3 solution/calculator.py
```

Depuis `solution/`, utiliser `python3 calculator.py`.

## Utilisation

Saisir une expression par ligne, avec des espaces entre les deux nombres et
l'opérateur. Les opérateurs acceptés sont exactement `+`, `-`, `*` et `/`.
Les nombres peuvent être entiers, décimaux (séparateur `.`) ou négatifs.
Il ne s'agit pas d'un analyseur d'expressions composées : les parenthèses et
les chaînes d'opérations ne sont pas prises en charge.

```text
> 2 + 3
5.0
> -2.5 * 4
-10.0
> 7 / 2
3.5
> 8 - 10
-2.0
> 1 / 0
Erreur : Division par zéro interdite.
> quit
```

`quit` ou `exit` termine le programme. La fin de l'entrée et Ctrl+C terminent
également proprement la boucle. Une expression invalide, un opérateur inconnu
ou une division par zéro affiche une erreur sans traceback ; la saisie peut
ensuite continuer.

## API Python

Depuis `solution/` :

```python
from calculator import calculate

assert calculate(-2.5, "+", 3) == 0.5
```

`calculate(left: float, operator: str, right: float) -> float` renvoie un
flottant. Elle accepte les arguments numériques `int` et `float`, lève
`ValueError` pour un opérateur inconnu et `ZeroDivisionError` pour un diviseur
nul. Importer le module ne lance pas l'interface interactive.
Les calculs utilisent les flottants Python et leur précision habituelle.
Aucune évaluation dynamique de code n'est utilisée.

## Vérification indépendante

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/astra-medium-core-v1-001/solution
```

Commande équivalente depuis le dossier de la tentative :

```bash
python3 ../../scripts/verify.py --solution solution
```
