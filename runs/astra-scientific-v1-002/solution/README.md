# Calculatrice scientifique

Calculatrice réelle et tracés SVG autonomes, compatible avec Python 3.10 ou
supérieur. Aucune installation, dépendance tierce ou connexion réseau requise.

## Lancement

Depuis le dossier de la tentative :

```bash
python3 solution/scientific_calculator.py
```

La boucle accepte une expression par ligne, `help`, `history`, `clear`, puis
`quit` ou `exit`. Une fin de fichier termine également la session. Une erreur
est affichée sans traceback et permet de continuer. L'historique, conservé
uniquement en mémoire, contient les calculs et tracés réussis ; `clear` le vide.

```text
> sqrt(2) ^ 2
2.0000000000000004
> -2 ^ 2
-4.0
> 2 ^ 3 ^ 2
512.0
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

Les quatre champs de `plot` sont séparés par des points-virgules : expression,
borne inférieure, borne supérieure, chemin du fichier. Les bornes sont des
expressions constantes. Les chemins peuvent contenir des espaces, mais pas de
point-virgule ; ils sont utilisés sans guillemets et relativement au répertoire
courant. Le dossier parent doit exister. Un fichier existant est écrasé.

## Syntaxe et fonctions

Nombres : `12`, `1.25`, `.5`, `2.`, `1e-3`, `2E+4`. Les noms sont sensibles à la
casse. Constantes : `pi` et `e`. La seule variable est `x`.

| Priorité croissante | Opérateurs | Associativité |
| --- | --- | --- |
| Somme | `+`, `-` | Gauche |
| Produit | `*`, `/` | Gauche |
| Signes unaires | `+`, `-` | Droite |
| Puissance | `^` | Droite |

Les parenthèses modifient la priorité. Ainsi `(-2)^2 = 4`, `-2^2 = -4`,
`2^-2 = 0.25`. La multiplication doit être explicite : écrire `2*pi`, pas `2pi`.
Chaque fonction reçoit exactement un argument entre parenthèses.

| Fonctions | Sens et domaine |
| --- | --- |
| `sin`, `cos`, `tan` | Trigonométrie, angles en radians |
| `asin`, `acos` | Inverses sur [-1, 1], résultats en radians |
| `atan` | Tangente inverse, résultat en radians |
| `sqrt` | Racine carrée, argument positif ou nul |
| `ln`, `log10` | Logarithmes naturel et décimal, argument strictement positif |
| `exp` | Exponentielle naturelle, limitée par les flottants |
| `abs` | Valeur absolue |

## API Python

Depuis `solution/` :

```python
from scientific_calculator import evaluate, sample_curve, write_svg

assert evaluate("sin(pi / 2)") == 1.0
assert evaluate("x^2 + 1", {"x": 3}) == 10.0
points = sample_curve("1/x", -1, 1, samples=201)
assert points[100] == (0.0, None)
write_svg(points, "inverse.svg", title="Fonction 1/x")
```

- `evaluate(expression, variables=None) -> float` renvoie un flottant fini.
  Les expressions vides, inconnues, mal formées, hors domaine réel ou avec
  débordement lèvent `ValueError`. Une division par zéro lève
  `ZeroDivisionError`. La valeur de `x` doit être un `int` ou `float` fini,
  hors booléens. Les autres clés du dictionnaire ne créent pas de noms.
- `sample_curve(expression, x_min, x_max, samples=201)` renvoie une liste de
  couples `(x, y)`. Les bornes doivent être finies et strictement croissantes ;
  le nombre d'échantillons doit être un entier supérieur ou égal à deux.
  Les deux bornes sont incluses. L'expression est analysée une seule fois ;
  une syntaxe invalide est rejetée. Une erreur numérique locale devient `None`.
- `write_svg(points, output_path, title="")` adapte l'échelle aux points finis,
  dessine le fond, deux axes et les segments séparés par les valeurs invalides.
  Un point isolé devient un cercle. Les données non finies coupent la courbe.
  Sans point fini, la fonction lève `ValueError`. Les erreurs d'écriture sont
  des `OSError`. Le fichier est en UTF-8, sans ressources externes ni script.

## Sécurité et limites

Un analyseur dédié vérifie entièrement les caractères et la grammaire ; un
interpréteur de ses instructions arithmétiques calcule le résultat. Il n'y a
aucune exécution dynamique Python ni commande système. Les attributs, chaînes,
indexations, imports, affectations et noms arbitraires sont refusés. L'analyse
est bornée à 10000 caractères, 2048 jetons et 100 niveaux d'imbrication ; une
expression trop complexe lève `ValueError`. Le titre est sérialisé comme texte
XML et les caractères interdits par XML 1.0 sont remplacés.

Les calculs utilisent les flottants binaires de Python et `math`, sans calcul
symbolique : arrondis, sous-flux vers zéro et perte de précision sont possibles.
Les résultats intermédiaires doivent être finis. `0^0` vaut `1`, comme dans
`math.pow`. Les puissances de base négative suivent le domaine de `math.pow`.
`tan(pi/2)` peut donner un grand nombre fini, car `pi/2` est une approximation.

L'échantillonnage est uniforme, sans recherche adaptative d'asymptotes : une
singularité entre deux échantillons peut ne pas être détectée. Augmenter
`samples` améliore la résolution sans garantir cette détection. De très petites
distances entre bornes peuvent produire des abscisses identiques par arrondi.
Le coût mémoire et le temps croissent avec le nombre de points ; l'appelant
doit choisir un nombre raisonnable d'échantillons.

Le SVG a une taille de 800 × 500, un fond blanc et des traits sombres pour un
contraste indépendant du thème du lecteur. Si zéro est hors du domaine visible,
l'axe correspondant est placé au bord du cadre ; les étiquettes précisent les
bornes réelles. Une dimension constante est centrée. Les valeurs extrêmes
peuvent comprimer les variations plus petites. Le tracé reste une approximation
numérique et non une preuve de continuité ou de domaine mathématique.

## Vérification indépendante

Depuis le dossier de la tentative active :

```bash
python3 ../../scripts/verify.py --challenge scientific-calculator --solution solution
```

Le candidat V1 travaille seul. La publication et les opérations Git relèvent
de l'orchestrateur expérimental, distinct du candidat.

Les contrôles complémentaires du candidat sont reproductibles depuis
`solution/` avec `python3 -B verify_additional.py`. Ils vérifient notamment
l'interpolation aux limites des flottants, la complexité maximale et les
caractères interdits en XML. Le [procès-verbal](PV.md) consigne les résultats et
la correction observée. La validation finale comprend 9 tests indépendants et
4 tests complémentaires réussis.
