# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```
