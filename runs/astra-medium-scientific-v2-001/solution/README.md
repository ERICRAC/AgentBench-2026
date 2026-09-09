# Calculatrice scientifique — solution finale V2

Python 3.10 ou supérieur, bibliothèque standard uniquement. Depuis ce dossier :

```bash
python3 scientific_calculator.py
```

Depuis la racine du dépôt :

```bash
python3 runs/astra-medium-scientific-v2-001/solution/scientific_calculator.py
```

## Syntaxe et exemples

Nombres entiers, décimaux (`.5`, `5.`, `0.25`) et scientifiques (`1.2e-3`),
chiffres ASCII, espaces, `+ - * / ^`, parenthèses, signes unaires et constantes
`pi`, `e`. La puissance est associative à droite et prioritaire sur les signes :
`2^3^2` donne `512.0`, `-2^2` donne `-4.0`, `2^-2` donne `0.25`.

Fonctions à un argument entre parenthèses : `sin`, `cos`, `tan`, `asin`, `acos`,
`atan`, `sqrt`, `ln` (logarithme naturel), `log10`, `exp`, `abs`. Les angles sont
en radians. Les compositions comme `sin(cos(0))` sont permises. La multiplication
doit être explicite (`2*pi`). Aucun attribut, chaîne, indexation, argument nommé,
appel indirect ou nom supplémentaire n'est accepté ; `**` et `%` sont refusés.

```text
> sqrt(2) ^ 2
2.0000000000000004
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
> history
1. sqrt(2) ^ 2
2. plot sin(x); -pi; pi; sinus.svg
> clear
Historique effacé.
> quit
```

Les quatre champs de `plot` sont séparés par trois points-virgules ; le chemin
peut contenir des espaces mais pas de point-virgule. Les bornes sont elles-mêmes
des expressions constantes. Le fichier est écrit relativement au répertoire
courant ; un fichier existant est remplacé. Son dossier doit déjà exister.
`help` rappelle la syntaxe, `exit` équivaut à `quit`. Fin d'entrée et interruption
au prompt terminent proprement. Une erreur de calcul ou d'écriture affiche un
message et permet de continuer. L'historique garde uniquement les expressions
et tracés réussis dans l'ordre, sans les commandes de contrôle.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

assert evaluate('x^2 + 1', {'x': 3}) == 10.0
points = sample_curve('1/x', -1, 1, samples=201)
write_svg(points, 'inverse.svg', title='Inverse : 1/x')
```

- `evaluate(expression, variables=None) -> float` : résultat réel fini ;
  `ValueError` pour syntaxe, nom, domaine ou débordement ; `ZeroDivisionError`
  pour `/` par zéro. Seul `x` est substituable. Les autres clés sont ignorées,
  notamment celles nommées `pi` ou `e`. Une valeur de `x` utilisée doit être finie.
- `sample_curve(expression, x_min, x_max, samples=201)` : liste de couples
  `(x, y)` avec bornes finies strictement croissantes, entier `samples >= 2`
  (booléens refusés). Bornes incluses exactement. Syntaxe analysée une seule
  fois ; toute erreur numérique d'un point produit `None`, y compris lorsque
  toute la fonction est indéfinie (`sqrt(-1)`). Une syntaxe invalide lève une erreur.
- `write_svg(points, output_path, title='')` : SVG UTF-8 autonome de 800 × 500,
  fond blanc, deux axes, courbe bleue et légende des plages. Chaque point
  non traçable coupe la courbe ; les points isolés sont des cercles. Aucun point
  fini entraîne `ValueError`. Les erreurs d'écriture restent des `OSError`.

## Conventions et limites

Calcul flottant standard : arrondis usuels, `0^0 = 1`, `0^-1` et puissances de
base négative à exposant non entier en `ValueError`. `tan` suit `math.tan` :
aucun seuil artificiel ne déclare un pôle. Chaque résultat intermédiaire doit
être fini ; une expression qui déborde avant une éventuelle compensation échoue.

L'échantillonnage uniforme coupe seulement les points réellement indéfinis ou
non finis rencontrés. Il ne détecte pas toutes les asymptotes ni les oscillations
entre points. Augmenter `samples` améliore la résolution sans garantir cette
 détection. Des abscisses peuvent coïncider aux limites de précision flottante.

L'échelle suit les seuls points finis avec marges en pixels. Une coordonnée
constante est centrée. Si zéro est hors plage, l'axe correspondant est ramené
au bord et une légende l'indique : ce bord n'est pas la coordonnée zéro.
La normalisation évite les dépassements de calcul des grandes étendues.

Le titre est du texte XML échappé ; les caractères interdits par XML 1.0 sont
remplacés par U+FFFD. Aucun script, lien externe ou contenu actif n'est généré.
Le document est construit avant ouverture du fichier ; l'écriture n'est pas
transactionnelle en cas de panne du système de fichiers.

L'analyse syntaxique et le calcul utilisent des piles explicites, sans plafond
de longueur ni dépendance à la profondeur de récursion Python. Aucun plafond de `samples` supplémentaire n'est
imposé ; mémoire et temps croissent avec le nombre de points et la taille de
l'expression. L'import du module ne lance pas la CLI et ne crée aucun fichier.

## Validation et protocole

Les arbitrages consultatifs, dont chaque point de SA-03, figurent dans
`DECISIONS.md`. Les contrôles candidats sont décrits dans
`CONTROLES.md` ; ils ne constituent pas le verdict indépendant.

La commande officielle de la phase finale, depuis la racine du dépôt, est :

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-001/solution
```

Les caractères non imprimables des chemins, historiques et diagnostics sont
réaffichés sous forme échappée ; le chemin réellement écrit reste inchangé.
En cas de défaillance de lecture ou d'affichage d'une commande de contrôle,
la session termine sans traceback, avec diagnostic sur stderr si ce canal
fonctionne. La récupération n'est pas garantie si les canaux ou la mémoire
sont indisponibles. L'écho des touches effectué par le terminal lui-même
n'est pas contrôlé par la calculatrice.

Résultat final : premier passage officiel réussi, 9 tests sur 9 (`OK`, code 0),
après corrections SA-03. Aucun correctif après ce passage. Quatre contrôles
candidats supplémentaires réussissent ; leur source reproductible est
`controle_final.py` (lancement : `python3 controle_final.py`). La trace officielle
et les limites de couverture sont conservées dans `CONTROLES.md`.
