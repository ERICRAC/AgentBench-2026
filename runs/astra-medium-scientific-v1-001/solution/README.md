# Calculatrice scientifique

Python 3.10 ou supérieur, bibliothèque standard uniquement. Depuis le dossier
actif de la tentative :

```bash
python3 solution/scientific_calculator.py
```

Depuis `solution/`, utiliser `python3 scientific_calculator.py`.

## Syntaxe et commandes

Les nombres acceptent les formes `42`, `2.5`, `.5`, `1.` et `1.2e-3`.
Les opérateurs sont `+`, `-`, `*`, `/`, `^`, avec parenthèses et signes
unaires. La puissance est associative à droite : `2^3^2 = 512`.
Elle précède le signe : `-2^2 = -4`, tandis que `2^-2 = 0.25`.
La multiplication doit être explicite : `2*pi`, pas `2pi`.

Constantes : `pi`, `e`. Fonctions à un argument entre parenthèses :
`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sqrt`, `ln` (logarithme naturel),
`log10`, `exp`, `abs`. Les angles sont en radians. Les noms sont sensibles à
la casse. Seule la variable `x` est autorisée, avec une valeur fournie par
l'appelant ou l'échantillonneur.

```text
> sqrt(2)^2
2.0000000000000004
> sin(pi/2)
1.0
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

`plot expression; borne_min; borne_max; fichier.svg` accepte des expressions
constantes pour les bornes et produit 201 échantillons. Le chemin est relatif
au dossier courant ; un fichier existant est remplacé. Les points-virgules
sont des séparateurs et ne peuvent figurer dans le chemin.

`help` rappelle la syntaxe ; `history` affiche les expressions et tracés
réussis ; `clear` vide cet historique ; `quit`, `exit` ou la fin de l'entrée
terminent la session. Les erreurs sont affichées sans traceback et la boucle
continue. L'historique est conservé uniquement en mémoire durant la session.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

assert evaluate('x^2 + 1', {'x': 3}) == 10.0
points = sample_curve('1/x', -1, 1, samples=201)
write_svg(points, 'inverse.svg', title='Inverse : 1/x')
```

`evaluate(expression, variables=None)` retourne un flottant fini. Une erreur de
syntaxe, un nom interdit, un domaine non réel ou un dépassement donne
`ValueError`. Une division par zéro donne `ZeroDivisionError`.
L'analyseur dédié ne peut accéder à Python, à des attributs, à des commandes
système ou au réseau. Il limite les expressions à 10000 caractères et
convertit les dépassements de profondeur en `ValueError`.

`sample_curve(expression, x_min, x_max, samples=201)` exige deux bornes finies
strictement croissantes et un entier d'au moins deux échantillons. Les bornes
sont incluses. La syntaxe est validée avant la boucle ; les erreurs numériques
locales deviennent `None` et n'interrompent pas l'échantillonnage.

`write_svg(points, output_path, title='')` écrit un SVG UTF-8 autonome, avec
fond blanc, axes et segments séparés aux valeurs absentes ou non finies.
L'échelle suit les points finis, avec marge ; une série constante reste
visible. Si zéro sort du domaine, l'axe correspondant est placé au bord.
Le titre est échappé et ses caractères interdits en XML sont retirés ; aucun
contenu actif ni lien externe n'est généré. Sans point fini : `ValueError`.
Les erreurs d'accès au fichier sont des `OSError` (traitées par la CLI).

## Limites

Calcul en virgule flottante : les arrondis usuels restent visibles. Aucun
calcul symbolique ni nombre complexe. `tan(pi/2)` peut être un grand nombre
fini à cause de l'approximation de pi. Un échantillonnage uniforme ne détecte
pas une singularité située entre deux points : aucune détection analytique
ou adaptative des asymptotes n'est prétendue. Les valeurs extrêmes peuvent
comprimer le reste de la courbe. L'API laisse le nombre d'échantillons à la
charge de l'appelant ; son coût en temps et mémoire est linéaire en ce nombre.
