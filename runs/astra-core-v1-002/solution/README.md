# Calculatrice Python

Calculatrice en ligne de commande, sans dépendance externe. Python 3 suffit.

## Lancement

Depuis le dossier de la tentative :

```bash
python3 solution/calculator.py
```

Depuis `solution/`, utiliser `python3 calculator.py`.
Le programme attend une ligne d'entrée, sans afficher d'invite.

## Utilisation

Saisir `nombre opérateur nombre`, en séparant les trois éléments par des
espaces. Les opérateurs disponibles sont `+`, `-`, `*` et `/`.
Les nombres peuvent être entiers, décimaux (avec un point) ou négatifs.
Les résultats sont des flottants Python, avec leur précision habituelle.

Exemple de session, alternant saisies et réponses :

```text
2 + 3
5.0
-2.5 * 4
-10.0
7 / 2
3.5
1 / 0
Erreur : division par zéro.
9 - 12
-3.0
quit
```

Une expression mal formée, un nombre invalide, un opérateur inconnu ou une
division par zéro affiche une erreur compréhensible ; la saisie suivante reste
possible. `quit` et `exit` terminent le programme. La fin de l'entrée et
Ctrl+C terminent également la boucle proprement.

On peut aussi fournir les lignes par un tube :

```bash
printf '%s\n' '2 + 3' '-2.5 * 4' 'exit' | python3 solution/calculator.py
```

## Interface Python

Depuis `solution/` :

```python
from calculator import calculate

result = calculate(-2.5, "*", 4)  # -10.0
```

`calculate(left: float, operator: str, right: float) -> float` accepte des
opérandes entiers ou flottants. Une opération inconnue lève `ValueError` ; une
division par zéro, y compris `-0.0`, lève `ZeroDivisionError`.
Importer le module ne lance pas la boucle interactive.

## Vérification indépendante

Depuis le dossier de la tentative active :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 ../../scripts/verify.py --solution solution
```

Cette commande appelle le vérificateur du dépôt ; la variable d'environnement
évite de créer des caches Python dans les répertoires de tests.

Résultat observé pour cette tentative : **6 tests réussis**, code de sortie 0.
