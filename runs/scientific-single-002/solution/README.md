# Calculatrice scientifique sûre

Cette solution fournit un moteur d'expressions à grammaire fermée, un
échantillonneur de fonctions et un exporteur SVG autonome. Elle utilise
exclusivement la bibliothèque standard de Python et interprète les expressions
avec son propre lexer et son propre parseur : une saisie n'est jamais exécutée
comme du code Python.

## Lancement

Python 3.10 ou une version ultérieure est requis. Depuis la racine du dépôt :

```bash
python3 solution/scientific_calculator.py
```

La boucle interactive accepte une expression par ligne. `quit` ou `exit`
termine la session, `help` affiche l'aide, `history` affiche uniquement les
commandes réussies et `clear` vide cet historique.

```text
> sqrt(2) ^ 2
2.0
> sin(pi / 2)
1.0
> history
1: sqrt(2) ^ 2
2: sin(pi / 2)
```

Une erreur est affichée sans traceback et la boucle reste disponible.

## Syntaxe des expressions

Les nombres peuvent être entiers (`12`), décimaux (`.5`, `2.`, `3.14`) ou en
notation scientifique (`1.2e-3`). Les opérateurs disponibles sont `+`, `-`,
`*`, `/` et `^`. Les parenthèses et les signes unaires `+` et `-` sont pris en
charge.

La puissance est associative à droite et prévaut sur le signe unaire :

- `2 ^ 3 ^ 2` donne `512.0` ;
- `-2 ^ 2` donne `-4.0` ;
- `2 ^ -2` donne `0.25`.

Les constantes sont `pi` et `e`. Les fonctions, à un seul argument exprimé
entre parenthèses, sont :

- trigonométrie en radians : `sin`, `cos`, `tan`, `asin`, `acos`, `atan` ;
- autres fonctions : `sqrt`, `ln`, `log10`, `exp`, `abs`.

La variable `x` n'est disponible que lors de l'échantillonnage ou lorsqu'une
valeur est passée explicitement à l'API Python. Tout autre nom, attribut,
caractère ou forme d'appel est refusé.

## Tracé SVG

La commande de tracé sépare ses quatre champs par des points-virgules :

```text
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

Les bornes sont elles-mêmes des expressions sans `x`. Le fichier contient un
fond, deux axes et une ou plusieurs polylignes. Les valeurs hors domaine ou
non finies séparent les segments au lieu d'annuler le tracé. Le titre est
échappé et le document ne contient ni script, ni ressource externe, ni contenu
actif.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

value = evaluate("cos(x) + 1", {"x": 0.5})
points = sample_curve("1 / x", -1.0, 1.0, samples=201)
write_svg(points, "inverse.svg", title="1 / x")
```

- `evaluate(expression, variables=None)` retourne toujours un `float` réel
  fini. Une syntaxe invalide, un nom inconnu ou une erreur de domaine lève
  `ValueError`; une division par zéro lève `ZeroDivisionError`.
- `sample_curve(expression, x_min, x_max, samples=201)` inclut exactement les
  deux bornes et remplace une valeur isolée invalide par `None`.
- `write_svg(points, output_path, title="")` écrit un SVG UTF-8 autonome et
  lève `ValueError` si aucun point fini n'est disponible.

## Limites

- Le langage ne propose ni affectation, ni fonctions à plusieurs arguments,
  ni nombres complexes, ni calcul symbolique.
- L'échantillonnage est uniforme. Une discontinuité située entre deux points
  échantillonnés ne peut donc pas toujours être détectée automatiquement ; une
  valeur invalide effectivement échantillonnée coupe bien la courbe.
- Les fonctions suivent la précision et les domaines réels du module `math`
  de Python. Les résultats non finis et les débordements sont refusés.
