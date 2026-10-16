# Calculatrice scientifique

Python 3.10 ou supérieur, bibliothèque standard uniquement. Depuis le dossier
contenant `solution/` :

```bash
python3 -B solution/scientific_calculator.py
```

Depuis `solution/`, utiliser `python3 -B scientific_calculator.py`.
La boucle affiche un résultat flottant ou une erreur puis accepte une nouvelle
commande. `quit`, `exit` ou la fin de l'entrée terminent la session.

## Syntaxe et fonctions

Entiers, décimaux (`.5`, `2.0`) et notation scientifique (`1e-3`) sont acceptés.
Les opérateurs sont `+`, `-`, `*`, `/`, `^`, avec parenthèses et signes unaires.
La puissance est associative à droite et précède le signe unaire :
`2^3^2` donne `512.0`, `-2^2` donne `-4.0`, `2^-2` donne `0.25`.
Les constantes sont `pi` et `e`.

Fonctions à un argument entre parenthèses : `sin`, `cos`, `tan`, `asin`,
`acos`, `atan`, `sqrt`, `ln` (logarithme naturel), `log10`, `exp`, `abs`.
Les angles sont en radians. La casse est significative. La multiplication doit
être explicite ; `2pi`, les attributs, listes, chaînes, appels inconnus et la
syntaxe Python `**` sont refusés. Aucun code saisi n'est exécuté.

```text
> sqrt(2)^2
2.0000000000000004
> sin(pi/2) + ln(e)
2.0
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

`plot expression; borne_min; borne_max; fichier.svg` évalue les bornes comme
expressions constantes et utilise 201 points, bornes incluses. Les quatre champs
sont séparés par des points-virgules ; un nom de fichier ne peut donc pas en
contenir. Le chemin est relatif au dossier courant ; un fichier existant est
remplacé. `help` rappelle la syntaxe, `history` affiche seulement les évaluations
et tracés réussis, et `clear` efface cet historique en mémoire.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

result = evaluate("x^2 + 1", {"x": 3})  # 10.0
points = sample_curve("1/x", -1, 1, samples=201)
write_svg(points, "inverse.svg", title="Courbe de 1/x")
```

`evaluate(expression, variables=None)` renvoie un flottant fini. Seule `x`
peut être fournie comme variable ; les autres clés ne créent pas de noms dans
le langage. Une expression invalide, un domaine non réel, un résultat infini
ou une complexité excessive lève `ValueError`. Une division par zéro lève
`ZeroDivisionError`.

`sample_curve(expression, x_min, x_max, samples=201)` exige des bornes finies
strictement croissantes et un entier d'au moins deux points. Une syntaxe invalide
est rejetée avant échantillonnage. Chaque valeur hors domaine ou non finie est
remplacée par `None` sans arrêter les autres évaluations.

`write_svg(points, output_path, title="")` produit un SVG UTF-8 autonome, sans
contenu actif, avec fond, axes et segments séparés aux points manquants.
Les titres sont échappés et les caractères incompatibles avec XML retirés.
Les points non finis coupent aussi les segments ; aucun point fini entraîne
`ValueError`. Les erreurs d'écriture sont des exceptions `OSError`.

## Limites numériques et graphiques

Les calculs utilisent les flottants binaires de Python, avec leurs arrondis et
limites de précision. Il n'y a ni calcul symbolique ni détection analytique
des singularités : une discontinuité entre deux échantillons peut être reliée.
Ainsi `tan(pi/2)` peut être un grand nombre fini dû à l'approximation de pi.
Augmenter `samples` dans l'API améliore la résolution sans garantir la détection
de toutes les singularités. Les valeurs extrêmes peuvent écraser visuellement
le reste de la courbe. Les axes hors plage sont placés au bord le plus proche ;
une dimension constante est centrée. Le SVG a une taille de 800 × 500, sans
graduations. L'historique n'est pas conservé après la session.
