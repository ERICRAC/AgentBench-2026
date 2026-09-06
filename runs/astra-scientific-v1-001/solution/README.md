# Calculatrice scientifique — V1

Python 3.10 ou supérieur ; bibliothèque standard uniquement, sans installation,
réseau ni exécution dynamique de code. Le module est importable sans lancer la
CLI. Les modifications de cette tentative sont limitées à `solution/`.

## Lancement

Depuis le dossier de la tentative active :

```sh
python3 solution/scientific_calculator.py
```

```text
> sqrt(2) ^ 2
2.0000000000000004
> -2 ^ 2
-4.0
> 2 ^ 3 ^ 2
512.0
> plot sin(x); -pi; pi; solution/sinus.svg
Courbe enregistrée dans solution/sinus.svg
> history
> clear
> help
> quit
```

`exit` termine également la session ; fin de fichier et Ctrl-C à l'invite
terminent proprement. L'historique en mémoire contient les expressions et
tracés réussis, sans les erreurs ni les commandes de gestion. Toute erreur
de calcul, de syntaxe ou d'écriture est affichée sans traceback, puis la CLI
redonne la main. Un fichier de sortie existant est remplacé ; son répertoire
doit déjà exister. Le chemin est relatif au répertoire courant du processus.

## Syntaxe et fonctions

Les nombres acceptent les formes `12`, `0.5`, `.5`, `2.`, `1e-3`, `2E+4`.
Les espaces sont permis entre les jetons. Les noms sont sensibles à la casse.
Les constantes sont `pi` et `e`. Seule la variable `x` est prévue, et sa valeur
doit être fournie par l'appelant ou par l'échantillonnage.

Priorité croissante : `+ -` binaires, `* /`, signes unaires, puissance `^`.
La puissance est associative à droite : `2^3^2 = 512`, `-2^2 = -4`,
`(-2)^2 = 4` et `2^-2 = 0.25`. Les autres opérateurs sont associatifs à gauche.
Les parenthèses modifient le groupement ; la multiplication doit être explicite.
`**`, `%`, attributs, indexations, chaînes, affectations et noms inconnus sont
refusés. Une fonction exige exactement un argument entre parenthèses.

| Fonction | Interprétation et domaine réel |
| --- | --- |
| `sin`, `cos`, `tan` | Trigonométrie en radians |
| `asin`, `acos` | Arc sinus/cosinus sur [-1, 1], résultat en radians |
| `atan` | Arc tangente, résultat en radians |
| `sqrt` | Racine carrée, argument ≥ 0 |
| `ln`, `log10` | Logarithmes naturel et décimal, argument > 0 |
| `exp` | Exponentielle, résultat dans les limites des flottants |
| `abs` | Valeur absolue |

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

assert evaluate("x^2 + 1", {"x": 3}) == 10.0
points = sample_curve("1/x", -1, 1, samples=201)
assert points[100] == (0.0, None)
write_svg(points, "inverse.svg", title="Courbe de 1/x")
```

- `evaluate(expression, variables=None) -> float` retourne un flottant fini.
  Une division par zéro lève `ZeroDivisionError`. Syntaxe, noms interdits,
  domaine réel, données non finies et débordements lèvent `ValueError`.
  Les valeurs de `x` doivent être des `int` ou `float` finis, hors booléens.
  Les autres clés du dictionnaire ne rendent aucun nom disponible.
- `sample_curve(expression, x_min, x_max, samples=201)` retourne des couples
  `(x, y)` avec les deux bornes incluses, finies et strictement croissantes.
  `samples` doit être un entier ≥ 2, hors booléens. L'expression est analysée
  une fois ; une syntaxe invalide lève `ValueError`. Un défaut numérique local
  produit `None`, sans interrompre les autres évaluations.
- `write_svg(points, output_path, title="")` crée un SVG UTF-8 autonome,
  de 800 × 500 pixels, avec fond, deux axes et segments séparés par les valeurs
  invalides. Un point isolé est un disque. L'échelle utilise les points finis ;
  un axe hors plage est affiché au bord, une plage constante au centre.
  Les bornes numériques figurent sous le graphique. Aucun point traçable
  entraîne `ValueError` avant l'écriture ; les erreurs de fichier sont des
  `OSError`. Le titre est échappé, les caractères XML interdits remplacés ;
  aucun script, lien externe, police distante ou contenu actif n'est généré.

## Choix et limites

Un analyseur descendant construit un arbre inerte avec une liste fermée de
fonctions. Il n'utilise ni `eval`, ni `exec`, ni `compile`. Les expressions
sont limitées à 10000 caractères et 512 jetons ; une imbrication excessive
est rejetée par `ValueError`. Le nombre d'échantillons est choisi par l'appelant
et détermine la mémoire et le temps nécessaires, linéaires à expression fixe.

Les calculs suivent les flottants Python, avec leurs arrondis et sous-flux
possibles vers zéro. Les résultats intermédiaires doivent rester finis.
Les puissances utilisent `math.pow` : aucun nombre complexe, `0^0 = 1`,
`0^-1` est hors domaine. Il n'y a ni calcul symbolique ni précision arbitraire.

L'échantillonnage uniforme ne prouve pas la continuité : une singularité située
entre deux échantillons peut être reliée. `tan(pi/2)` peut donner une grande
valeur finie, car l'argument flottant n'est pas le pôle mathématique exact.
Augmenter `samples` améliore la résolution sans garantir la détection de tous
les pôles. À des échelles extrêmes, des abscisses peuvent se confondre par
arrondi. Les valeurs extrêmes finies influencent l'échelle ; aucun filtrage
statistique ni détection heuristique de discontinuité n'est appliqué.

## Vérification indépendante

Depuis le dossier de la tentative active :

```sh
PYTHONDONTWRITEBYTECODE=1 python3 ../../scripts/verify.py \
  --challenge scientific-calculator --solution solution
```

La variable d'environnement évite d'écrire des caches Python dans les dossiers
du vérificateur. Son verdict et les contrôles complémentaires sont consignés
dans `PV.md` après exécution.
