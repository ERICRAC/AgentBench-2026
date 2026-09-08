# Défi — Scientific Calculator

## Statut

Spécification figée avec sa suite de tests d'acceptation avant la création du
premier run scientifique. Toute évolution ultérieure impose une nouvelle
version du défi et ne peut pas être appliquée aux runs existants.

## Objectif

Développer une calculatrice scientifique Python en ligne de commande capable
d'évaluer des expressions sûres et de produire la courbe d'une fonction dans
un fichier SVG autonome.

Le défi doit rester exécutable avec la bibliothèque standard. L'absence de
bibliothèque de calcul symbolique ou de tracé fait partie de la difficulté.

## Livrables

Créer exclusivement dans le dossier `solution/` de la tentative :

- `scientific_calculator.py` : moteur d'expressions, échantillonnage, export
  SVG et interface CLI ;
- `README.md` : lancement, syntaxe, fonctions, exemples et limites.

## Langage d'expressions

Le moteur doit accepter :

- les nombres entiers, décimaux et la notation scientifique ;
- les opérateurs `+`, `-`, `*`, `/` et `^` avec leurs priorités usuelles ;
- les parenthèses et les signes unaires `+` et `-` ;
- les constantes `pi` et `e` ;
- les fonctions `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `sqrt`, `ln`,
  `log10`, `exp` et `abs` ;
- la variable `x` lorsqu'une valeur est fournie par l'appelant.

Les angles des fonctions trigonométriques sont exprimés en radians.
La puissance est associative à droite et prioritaire sur les signes unaires :
`2 ^ 3 ^ 2` vaut `512` et `-2 ^ 2` vaut `-4`.

## Contrat Python

Le module doit exposer :

```python
def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    ...

def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    ...

def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    ...
```

`evaluate` doit :

- respecter la priorité et l'associativité des opérateurs ;
- retourner un nombre flottant fini ;
- lever `ValueError` pour une expression vide, mal formée, inconnue ou hors du
  domaine réel ;
- lever `ZeroDivisionError` pour une division par zéro ;
- refuser les noms, attributs, appels ou caractères non prévus par la
  grammaire.

`sample_curve` doit :

- exiger `x_min < x_max` et au moins deux échantillons ;
- inclure les deux bornes ;
- évaluer l'expression avec la variable `x` ;
- représenter par `None` une valeur non définie ou non finie afin de couper la
  courbe au niveau des discontinuités ;
- ne pas interrompre tout le tracé à cause d'un point isolé hors domaine.

`write_svg` doit :

- produire un SVG UTF-8 autonome et valide ;
- dessiner un fond, les deux axes avec des éléments SVG `line` et la courbe en
  segments discontinus ;
- adapter l'échelle aux points finis disponibles ;
- échapper tout titre ou contenu provenant de l'utilisateur ;
- n'inclure aucun script, lien externe ou contenu actif ;
- lever `ValueError` si aucun point fini ne peut être tracé.

## Interface CLI

La commande suivante lance une boucle interactive :

```bash
python3 solution/scientific_calculator.py
```

Une expression ordinaire est évaluée immédiatement :

```text
> sqrt(2) ^ 2
2.0
```

La commande de tracé utilise des points-virgules pour séparer sans ambiguïté
l'expression et les paramètres :

```text
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

La CLI doit également accepter :

- `help` pour rappeler la syntaxe ;
- `history` pour afficher les expressions et tracés réussis de la session ;
- `clear` pour vider cet historique ;
- `quit` et `exit` pour terminer.

Toute erreur doit produire un message compréhensible, sans traceback, puis
rendre la main à l'utilisateur.

## Contraintes de sécurité et de portabilité

- bibliothèque standard Python uniquement ;
- interdiction de `eval()`, `exec()` et `compile()` ;
- aucune exécution de commande système ou de code provenant de l'expression ;
- aucune dépendance réseau ;
- résultat déterministe pour les mêmes entrées ;
- compatibilité Python 3.10 ou supérieur.

## Vérification attendue

La suite d'acceptation indépendante devra couvrir au minimum :

- précédence, parenthèses, puissance et signes unaires ;
- constantes, fonctions et notation scientifique ;
- variable `x` et noms interdits ;
- erreurs de syntaxe, domaines réels et division par zéro ;
- échantillonnage des bornes et discontinuités ;
- validité et innocuité du SVG produit ;
- historique et récupération de la CLI après erreur ;
- absence d'exécution dynamique interdite ;
- présence et qualité minimale de la documentation.

Commande de vérification depuis la racine du dépôt :

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/<identifiant>/solution
```
