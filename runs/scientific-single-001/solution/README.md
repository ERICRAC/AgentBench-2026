# Calculatrice scientifique sûre

Cette solution Python 3.10+ évalue des expressions scientifiques sans
`eval`, sans exécution de code et sans dépendance externe. Elle peut aussi
échantillonner une fonction réelle et produire un SVG autonome.

## Lancement

Depuis la racine de la tentative :

```bash
python3 solution/scientific_calculator.py
```

Dans la boucle interactive, saisir une expression, `help`, `history`, `clear`,
`quit` ou `exit`. Un tracé suit la forme :

```text
plot sin(x); -pi; pi; sinus.svg
```

Les tracés et évaluations réussis sont conservés dans l'historique de la
session. Une erreur affiche un message et laisse la boucle utilisable.

## Syntaxe prise en charge

- nombres entiers, décimaux (`.5`, `2.`) et notation scientifique (`1.2e-3`) ;
- opérateurs `+`, `-`, `*`, `/`, `^` et parenthèses ;
- constantes `pi` et `e` ;
- fonctions à un argument `sin`, `cos`, `tan`, `asin`, `acos`, `atan`,
  `sqrt`, `ln`, `log10`, `exp`, `abs` ;
- variable `x` lorsqu'elle est fournie à `evaluate`, notamment par le tracé.

La puissance est associative à droite et plus prioritaire que les signes :
`2^3^2` produit `512.0`, `-2^2` produit `-4.0`. Les angles sont en radians.

Exemples :

```text
sqrt(2)^2
sin(pi/2)
1e3 + 2.5
plot 1/x; -2; 2; inverse.svg
```

## API Python

Le module expose `evaluate(expression, variables=None)`,
`sample_curve(expression, x_min, x_max, samples=201)` et
`write_svg(points, output_path, title="")`. Les points non définis sont
représentés par `None` et séparent les segments SVG.

## Sécurité et limites

La grammaire est analysée caractère par caractère : attributs, chaînes,
crochets, appels arbitraires et identifiants inconnus sont refusés. Les
résultats complexes ou non finis et les erreurs de domaine réel sont rejetés.
La division par zéro utilise `ZeroDivisionError`; les autres erreurs
d'expression utilisent `ValueError`.

Le tracé est un échantillonnage numérique uniforme, pas un calcul symbolique :
une discontinuité située entre deux échantillons peut donc ne pas être détectée
et les asymptotes très proches d'un point échantillonné peuvent étirer
l'échelle. Le SVG ne contient ni script, ni lien, ni ressource externe.
