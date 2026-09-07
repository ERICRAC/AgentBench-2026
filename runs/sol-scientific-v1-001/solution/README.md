# Calculatrice scientifique

Cette solution fournit un moteur d'expressions scientifiques sûr, un
échantillonneur de courbes et un export SVG autonome. Elle utilise uniquement
la bibliothèque standard de Python 3.10 ou supérieur.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/scientific_calculator.py
```

Dans une tentative AgentBench, adapter le chemin au dossier `solution/` de la
tentative. La boucle interactive accepte `help`, `history`, `clear`, `quit` et
`exit`. Après une erreur, elle affiche un message puis attend la commande
suivante. Seules les évaluations et les créations de courbes réussies entrent
dans l'historique de la session.

Exemples :

```text
> sqrt(2) ^ 2
2.0
> sin(pi / 2) + 1e-3
1.001
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

## Langage d'expressions

Les littéraux peuvent être entiers (`12`), décimaux (`.5`, `2.`, `3.14`) ou
en notation scientifique (`6.02e23`). Les opérateurs disponibles sont `+`,
`-`, `*`, `/` et `^`, ainsi que les parenthèses et les signes unaires. La
puissance est associative à droite et plus prioritaire que les signes :
`2^3^2` donne `512.0`, tandis que `-2^2` donne `-4.0`.

Les constantes sont `pi` et `e`. Les fonctions à un argument sont :

- `sin`, `cos`, `tan`, `asin`, `acos`, `atan` (angles en radians) ;
- `sqrt`, `ln`, `log10`, `exp` et `abs`.

La variable `x` est disponible quand l'appel Python lui fournit une valeur,
notamment pendant un tracé. Aucun autre identifiant, attribut, appel ou
caractère de programmation n'est accepté. Le moteur analyse directement cette
grammaire restreinte et ne transforme pas l'entrée en code Python.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

value = evaluate("sin(x) + 2", {"x": 0.5})
points = sample_curve("1 / x", -1.0, 1.0, samples=201)
write_svg(points, "inverse.svg", "Fonction 1 / x")
```

`evaluate` renvoie toujours un `float` réel fini. Une expression vide,
inconnue, mal formée, non réelle ou hors domaine lève `ValueError`; une
division par zéro lève `ZeroDivisionError`.

`sample_curve` inclut exactement les deux bornes. Une singularité ponctuelle
devient `(x, None)` et coupe donc le tracé sans annuler les autres points.
Il exige des bornes finies strictement croissantes et au moins deux points.

`write_svg` ajuste automatiquement les deux échelles aux points finis,
dessine un fond, les axes et une polyligne par segment continu. Il échappe le
titre, ne produit ni script ni ressource externe, et refuse un jeu sans aucun
point fini.

## Syntaxe de tracé

La commande interactive possède quatre champs séparés par des points-virgules :

```text
plot <expression en x>; <borne minimale>; <borne maximale>; <fichier SVG>
```

Les bornes sont elles-mêmes des expressions, ce qui autorise par exemple
`-pi`, `pi / 2` ou `1e2`. Le nom de fichier ne doit pas contenir de
point-virgule.

## Limites

- Le calcul est numérique en double précision, sans simplification symbolique.
- Une discontinuité n'est coupée que si elle coïncide avec un point
  échantillonné (ou si ce point produit une erreur/non-finitude).
- `tan` près d'un multiple impair de `pi/2` peut donner une très grande valeur
  finie en raison des approximations en virgule flottante.
- Chaque fonction accepte exactement un argument et les multiplications
  implicites, telles que `2pi`, ne sont pas prises en charge.
