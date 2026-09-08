# PV multi-agent — sol-scientific-v2-001

## Identification et périmètre

Le commanditaire lance V2 Sol/high. L'orchestrateur expérimental
exécute le relais mécanique et publie après clôture. MAIN est le seul
rôle écrivain. SA-01, SA-02 et SA-03 sont consultants en lecture seule,
sans sous-délégation. Les sept sessions sont neuves et éphémères.

Les textes ci-dessous sont conservés dans l'ordre des phases. Seuls le
préfixe local du dépôt et d'éventuels secrets reconnus sont remplacés ;
aucun raisonnement interne n'est publié.

## Équipe et métriques

| Session | Rôle / phase | Durée | Entrée | Cache inclus | Sortie | Raisonnement inclus | Mots visibles |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 01-sa01-initial | MSG-001 · analyse indépendante (max 1200) | 78.281 s | 14402 | 8064 | 2015 | 516 | 915 |
| 02-sa02-initial | MSG-002 · analyse indépendante (max 1200) | 73.029 s | 14404 | 8064 | 1860 | 85 | 1065 |
| 03-sa01-cross | MSG-003 · contradiction croisée (max 600) | 41.247 s | 16295 | 8064 | 996 | 346 | 413 |
| 04-sa02-cross | MSG-004 · contradiction croisée (max 600) | 38.271 s | 16297 | 8064 | 917 | 202 | 466 |
| 05-main-first | MSG-005 · arbitrage et première solution | 810.863 s | 394075 | 351616 | 21975 | 7564 | 429 |
| 06-sa03-critic | MSG-006 · critique adversariale (max 1200) | 226.117 s | 26664 | 8064 | 6122 | 5035 | 666 |
| 07-main-final | MSG-007 · arbitrage final et vérification | 431.056 s | 389108 | 344704 | 11408 | 5755 | 555 |

Temps mural : **1587.605 s**. Somme des temps-sessions : **1698.864 s**.

Tokens : **871245 entrée + 45293 sortie = 916538**. Le cache (736640) est inclus dans
l'entrée et le raisonnement (19503) dans la sortie.

## Messages visibles — verbatim filtré

### MSG-001 — analyse indépendante

Direction : `RELAY → SA-01 → MAIN`. Réponse visible : 915 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Analyse indépendamment le challenge ci-dessous en 1 200 mots maximum. Tu es consultant en lecture seule : n'utilise aucun outil, ne délègue rien, ne consulte aucun dépôt et ne fournis qu'un avis visible. Structure les recommandations pour permettre un arbitrage explicite.
--- BEGIN CHALLENGE ---
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

--- END CHALLENGE ---
````

</details>

#### Texte retourné pour MSG-001, mot pour mot

````text
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
````

### MSG-002 — analyse indépendante

Direction : `RELAY → SA-02 → MAIN`. Réponse visible : 1065 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Analyse indépendamment le challenge ci-dessous en 1 200 mots maximum. Tu es consultant en lecture seule : n'utilise aucun outil, ne délègue rien, ne consulte aucun dépôt et ne fournis qu'un avis visible. Structure les recommandations pour permettre un arbitrage explicite.
--- BEGIN CHALLENGE ---
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

--- END CHALLENGE ---
````

</details>

#### Texte retourné pour MSG-002, mot pour mot

````text
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
````

### MSG-003 — contradiction croisée

Direction : `MAIN/RELAY → SA-01 → MAIN`. Réponse visible : 413 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-01 ---
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
--- END YOUR INITIAL SA-01 ---

--- BEGIN PEER INITIAL SA-02 ---
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
--- END PEER INITIAL SA-02 ---
````

</details>

#### Texte retourné pour MSG-003, mot pour mot

````text
## Révision SA-01 après avis SA-02

Les deux avis convergent fortement. SA-02 confirme les priorités essentielles : pipeline lexer–parseur–évaluateur, consommation intégrale de l’entrée, grammaire fermée, puissance associative à droite, exposant signé, table blanche, résultats finis, conservation de `ZeroDivisionError`, segmentation aux `None`, titre SVG assaini et historique limité aux opérations réussies. Les listes de cas critiques et de tests sont complémentaires, mais largement redondantes avec les risques déjà identifiés par SA-01.

Deux recommandations doivent toutefois être reclassées.

Premièrement, rejeter toutes les clés de `variables` autres que `x` est un choix de durcissement, pas nécessairement une obligation du contrat. L’exigence de sécurité est qu’aucune clé ne crée un nom accessible dans l’expression. Ignorer les clés surnuméraires peut être tout aussi sûr et davantage compatible avec un appelant fournissant un contexte plus large. Le candidat doit choisir selon le texte exact ou les tests, sans présenter le rejet comme imposé. En revanche, la valeur effectivement utilisée pour `x` doit être numérique réelle et finie; `bool` devrait être explicitement refusé malgré son héritage de `int`.

Deuxièmement, les plafonds de longueur, profondeur, jetons ou échantillons sont pertinents contre le déni de service, mais restent des extensions non contractuelles. Des seuils arbitraires risquent de rejeter des entrées valides du vérificateur. Ils sont donc secondaires tant qu’aucune limite n’est spécifiée, et doivent être documentés s’ils sont ajoutés.

Le principal accord d’architecture appelle une précision : parser une seule fois dans `sample_curve` est préférable, mais ne suffit pas à distinguer toutes les erreurs « globales » des erreurs « locales ». Syntaxe, nom inconnu et mauvais usage d’une fonction sont structurels et doivent être levés avant la boucle. Domaine, division, débordement et non-finitude dépendent de chaque valeur de `x` et deviennent `None`. Cette classification doit reposer sur les phases du moteur, pas sur une capture générale répétée.

Pour le SVG, `ElementTree` ou `html.escape` empêche l’injection de balises, mais ne règle pas automatiquement tous les caractères interdits par XML. La validation ou neutralisation des contrôles illégaux demeure nécessaire. Les axes au bord lorsque zéro est hors domaine, comme la politique d’écrasement, sont des décisions de rendu ou d’I/O et non des priorités de sécurité.

Priorités consolidées :

1. Grammaire exacte et consommation intégrale.
2. Résolution fermée des noms et appels.
3. Typage, finitude et classification stable des exceptions.
4. Séparation des erreurs structurelles et ponctuelles dans l’échantillonnage.
5. SVG XML valide, inerte et segmenté.
6. Résilience CLI et historique transactionnel.
7. Durcissement anti-DoS et politiques de fichiers, uniquement après conformité au contrat.
````

### MSG-004 — contradiction croisée

Direction : `MAIN/RELAY → SA-02 → MAIN`. Réponse visible : 466 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-02 ---
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
--- END YOUR INITIAL SA-02 ---

--- BEGIN PEER INITIAL SA-01 ---
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
--- END PEER INITIAL SA-01 ---
````

</details>

#### Texte retourné pour MSG-004, mot pour mot

````text
## Révision consolidée SA-02

Les deux avis convergent fortement et se confirment sur l’architecture centrale : lexer à consommation totale, parseur dédié, AST, évaluateur par tables blanches, échantillonnage séparé, rendu SVG déterministe et CLI limitée à l’orchestration. Ils s’accordent également sur les priorités sémantiques : puissance associative à droite, priorité sur le signe unaire, exposant signé, résultats finis, maintien de `ZeroDivisionError`, conversion des autres erreurs attendues en `ValueError`, segmentation aux discontinuités et historique réservé aux opérations réussies.

Les recommandations suivantes sont donc des doublons à fusionner, non des décisions indépendantes :

- consommation intégrale de l’entrée et rejet des constructions hors grammaire ;
- distinction entre erreurs globales d’expression et erreurs numériques ponctuelles dans `sample_curve` ;
- échappement XML et interdiction de contenu actif ;
- rejet de `bool` pour `samples`, bornes finies et inclusion des extrémités ;
- ajout à l’historique seulement après écriture effective du SVG.

SA-01 complète utilement mon avis sur quatre cas sensibles : caractères Unicode ressemblants, caractères de contrôle XML, profondeur syntaxique excessive et volume d’échantillonnage pathologique. Je révise donc la stratégie de validation pour inclure explicitement ces familles. Toutefois, des plafonds de longueur, profondeur, jetons ou échantillons ne doivent pas être inventés arbitrairement s’ils ne figurent pas dans le contrat : ils risqueraient de rejeter des entrées valides et de créer une incompatibilité avec le vérificateur. La bonne priorité est d’abord d’éviter les comportements explosifs évidents ; toute limite supplémentaire doit être déterministe, documentée et justifiée comme décision d’implémentation.

Je précise aussi deux arbitrages où nos formulations pourraient être trop prescriptives :

1. Pour `variables`, l’invariant obligatoire est que seul `x` soit résolvable par le langage. Rejeter les clés supplémentaires est une politique défendable, mais les ignorer sans les rendre accessibles peut également respecter cet invariant. Il faut choisir selon le texte exact du contrat et tester la décision.
2. Pour le SVG, l’absence de points finis doit lever `ValueError`, mais un segment contenant un seul point mérite un traitement explicite : un chemin composé uniquement d’un déplacement peut être invisible. Un élément `circle`, ou une convention de rendu stable, doit être prévu si le contrat exige que tout point valide soit représenté.

Ordre de priorité consolidé :

1. Grammaire et précédence exactes, avec consommation totale.
2. Surface d’évaluation fermée et absence de mécanisme dynamique.
3. Taxonomie stable des exceptions et garantie de finitude.
4. Parsing unique de la courbe, puis tolérance limitée aux erreurs dépendant de `x`.
5. SVG analysable, segmenté, sans injection ni coordonnées non finies.
6. CLI résiliente et historique transactionnel.
7. Limites de ressources et cas dégénérés, sans durcir arbitrairement l’API.

La meilleure structure de test reste modulaire : tests du lexer, du parseur/AST, de l’évaluateur, de l’échantillonnage, du rendu XML puis tests d’intégration CLI. Cette séparation permettra d’attribuer immédiatement chaque échec à un invariant précis.
````

### MSG-005 — arbitrage et première solution

Direction : `RELAY → MAIN`. Réponse visible : 429 mots.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2 — phase MAIN première solution. Tu es l'orchestrateur candidat et l'unique écrivain. L'orchestrateur expérimental a déjà exécuté exactement les consultants SA-01 et SA-02 selon le protocole ; ne lance aucun autre agent. Lis leurs quatre textes comme des avis non contraignants. Avant de coder, crée `solution/DECISIONS.md` avec une table reliant chaque recommandation à une décision motivée. Implémente ensuite une première solution complète et documentée, uniquement dans `solution/`. Tu peux effectuer des contrôles ciblés, mais ne lance pas encore le vérificateur officiel : la critique SA-03 doit examiner cette première solution. Ne fais aucune opération Git. Termine par une synthèse visible.
--- BEGIN BASE MULTI-AGENT PROMPT ---
Réalise le défi décrit dans CHALLENGE.md en mode V2 multi-agent gouverné.

Contraintes particulières pour cette tentative :

- ne lis aucune autre tentative, solution ou résultat du dépôt ;
- utilise exactement trois consultants sans délégation imbriquée :
  1. analyste du contrat et de la sécurité,
  2. analyste de conception et de testabilité,
  3. critique final des cas limites ;
- les deux premiers interviennent avant l'implémentation et le critique après
  une première solution ;
- demande d'abord aux deux analystes une réponse indépendante de 1 200 mots
  maximum, sans leur montrer l'avis de l'autre ;
- relaie ensuite à chacun le texte visible intégral de l'autre et autorise une
  seule réponse contradictoire ou révision de 600 mots maximum ;
- synthétise leurs propositions dans une table d'arbitrage avant d'écrire ;
- transmets au critique le challenge, la première solution et cette table ; sa
  critique finale est limitée à 1 200 mots ;
- leurs missions sont consultatives et en lecture seule ; toi seul écris ;
- écris exclusivement dans `solution/` et ne modifie ni spécification, ni
  tests, ni scripts, ni gouvernance ;
- ne lance aucune opération Git (`git add`, `git commit`, `git push`) ;
- utilise uniquement la bibliothèque standard Python ;
- n'utilise jamais `eval()`, `exec()` ou `compile()` ;
- arbitre explicitement les recommandations retenues ou écartées ;
- lance le vérificateur indiqué dans CHALLENGE.md, corrige les défauts
  confirmés et termine avec une solution complète, documentée et sans
  placeholder ;
- résume les rôles, avis, arbitrages, tests, corrections et limites sans
  exposer de raisonnement interne brut.
- conserve dans ta restitution l'ordre et le texte visible des échanges afin
  que l'orchestrateur expérimental puisse produire le `PV.md` du run.

--- END BASE MULTI-AGENT PROMPT ---

--- BEGIN CHALLENGE ---
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

--- END CHALLENGE ---

--- BEGIN SA-01 INITIAL ---
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
--- END SA-01 INITIAL ---

--- BEGIN SA-02 INITIAL ---
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
--- END SA-02 INITIAL ---

--- BEGIN SA-01 CONTRADICTION ---
## Révision SA-01 après avis SA-02

Les deux avis convergent fortement. SA-02 confirme les priorités essentielles : pipeline lexer–parseur–évaluateur, consommation intégrale de l’entrée, grammaire fermée, puissance associative à droite, exposant signé, table blanche, résultats finis, conservation de `ZeroDivisionError`, segmentation aux `None`, titre SVG assaini et historique limité aux opérations réussies. Les listes de cas critiques et de tests sont complémentaires, mais largement redondantes avec les risques déjà identifiés par SA-01.

Deux recommandations doivent toutefois être reclassées.

Premièrement, rejeter toutes les clés de `variables` autres que `x` est un choix de durcissement, pas nécessairement une obligation du contrat. L’exigence de sécurité est qu’aucune clé ne crée un nom accessible dans l’expression. Ignorer les clés surnuméraires peut être tout aussi sûr et davantage compatible avec un appelant fournissant un contexte plus large. Le candidat doit choisir selon le texte exact ou les tests, sans présenter le rejet comme imposé. En revanche, la valeur effectivement utilisée pour `x` doit être numérique réelle et finie; `bool` devrait être explicitement refusé malgré son héritage de `int`.

Deuxièmement, les plafonds de longueur, profondeur, jetons ou échantillons sont pertinents contre le déni de service, mais restent des extensions non contractuelles. Des seuils arbitraires risquent de rejeter des entrées valides du vérificateur. Ils sont donc secondaires tant qu’aucune limite n’est spécifiée, et doivent être documentés s’ils sont ajoutés.

Le principal accord d’architecture appelle une précision : parser une seule fois dans `sample_curve` est préférable, mais ne suffit pas à distinguer toutes les erreurs « globales » des erreurs « locales ». Syntaxe, nom inconnu et mauvais usage d’une fonction sont structurels et doivent être levés avant la boucle. Domaine, division, débordement et non-finitude dépendent de chaque valeur de `x` et deviennent `None`. Cette classification doit reposer sur les phases du moteur, pas sur une capture générale répétée.

Pour le SVG, `ElementTree` ou `html.escape` empêche l’injection de balises, mais ne règle pas automatiquement tous les caractères interdits par XML. La validation ou neutralisation des contrôles illégaux demeure nécessaire. Les axes au bord lorsque zéro est hors domaine, comme la politique d’écrasement, sont des décisions de rendu ou d’I/O et non des priorités de sécurité.

Priorités consolidées :

1. Grammaire exacte et consommation intégrale.
2. Résolution fermée des noms et appels.
3. Typage, finitude et classification stable des exceptions.
4. Séparation des erreurs structurelles et ponctuelles dans l’échantillonnage.
5. SVG XML valide, inerte et segmenté.
6. Résilience CLI et historique transactionnel.
7. Durcissement anti-DoS et politiques de fichiers, uniquement après conformité au contrat.
--- END SA-01 CONTRADICTION ---

--- BEGIN SA-02 CONTRADICTION ---
## Révision consolidée SA-02

Les deux avis convergent fortement et se confirment sur l’architecture centrale : lexer à consommation totale, parseur dédié, AST, évaluateur par tables blanches, échantillonnage séparé, rendu SVG déterministe et CLI limitée à l’orchestration. Ils s’accordent également sur les priorités sémantiques : puissance associative à droite, priorité sur le signe unaire, exposant signé, résultats finis, maintien de `ZeroDivisionError`, conversion des autres erreurs attendues en `ValueError`, segmentation aux discontinuités et historique réservé aux opérations réussies.

Les recommandations suivantes sont donc des doublons à fusionner, non des décisions indépendantes :

- consommation intégrale de l’entrée et rejet des constructions hors grammaire ;
- distinction entre erreurs globales d’expression et erreurs numériques ponctuelles dans `sample_curve` ;
- échappement XML et interdiction de contenu actif ;
- rejet de `bool` pour `samples`, bornes finies et inclusion des extrémités ;
- ajout à l’historique seulement après écriture effective du SVG.

SA-01 complète utilement mon avis sur quatre cas sensibles : caractères Unicode ressemblants, caractères de contrôle XML, profondeur syntaxique excessive et volume d’échantillonnage pathologique. Je révise donc la stratégie de validation pour inclure explicitement ces familles. Toutefois, des plafonds de longueur, profondeur, jetons ou échantillons ne doivent pas être inventés arbitrairement s’ils ne figurent pas dans le contrat : ils risqueraient de rejeter des entrées valides et de créer une incompatibilité avec le vérificateur. La bonne priorité est d’abord d’éviter les comportements explosifs évidents ; toute limite supplémentaire doit être déterministe, documentée et justifiée comme décision d’implémentation.

Je précise aussi deux arbitrages où nos formulations pourraient être trop prescriptives :

1. Pour `variables`, l’invariant obligatoire est que seul `x` soit résolvable par le langage. Rejeter les clés supplémentaires est une politique défendable, mais les ignorer sans les rendre accessibles peut également respecter cet invariant. Il faut choisir selon le texte exact du contrat et tester la décision.
2. Pour le SVG, l’absence de points finis doit lever `ValueError`, mais un segment contenant un seul point mérite un traitement explicite : un chemin composé uniquement d’un déplacement peut être invisible. Un élément `circle`, ou une convention de rendu stable, doit être prévu si le contrat exige que tout point valide soit représenté.

Ordre de priorité consolidé :

1. Grammaire et précédence exactes, avec consommation totale.
2. Surface d’évaluation fermée et absence de mécanisme dynamique.
3. Taxonomie stable des exceptions et garantie de finitude.
4. Parsing unique de la courbe, puis tolérance limitée aux erreurs dépendant de `x`.
5. SVG analysable, segmenté, sans injection ni coordonnées non finies.
6. CLI résiliente et historique transactionnel.
7. Limites de ressources et cas dégénérés, sans durcir arbitrairement l’API.

La meilleure structure de test reste modulaire : tests du lexer, du parseur/AST, de l’évaluateur, de l’échantillonnage, du rendu XML puis tests d’intégration CLI. Cette séparation permettra d’attribuer immédiatement chaque échec à un invariant précis.
--- END SA-02 CONTRADICTION ---
````

</details>

#### Texte retourné pour MSG-005, mot pour mot

````text
Je vais d’abord relire le défi figé dans son fichier source, puis matérialiser l’arbitrage des quatre avis dans `DECISIONS.md` avant toute implémentation. Je resterai dans cette tentative, sans agent supplémentaire, sans Git et sans lancer le vérificateur officiel durant cette phase.

Le fichier canonique confirme mot pour mot le contrat transmis. Les deux analystes convergent sur l’essentiel ; les seuls vrais arbitrages portent sur les clés supplémentaires de `variables`, les limites anti-déni de service, le traitement des erreurs structurelles lors d’un tracé et quelques conventions de rendu/I/O. Je consigne maintenant ces choix avant d’écrire le moteur.

La première implémentation et sa documentation sont en place. Je passe à des contrôles ciblés indépendants du vérificateur officiel : précédence et sécurité lexicale, classification des erreurs, discontinuités, XML hostile et reprise de la CLI après erreur. Ces contrôles peuvent encore conduire à corriger cette première solution avant sa remise à SA-03.

Les contrôles étendus passent, y compris les coordonnées proches des limites des flottants et l’affichage CLI conforme à l’exemple (`sqrt(2)^2` → `2.0`). J’ai aussi corrigé une coquille documentaire et renforcé la projection SVG pour qu’aucun débordement de plage finie ne produise `nan`/`inf` dans le XML. Il reste un contrôle statique à relancer : ma première commande de recherche était mal échappée, donc son résultat n’est pas exploitable.

## Objectif

Première solution V2 complète du défi Scientific Calculator, écrite exclusivement dans le dossier actif par l’orchestrateur candidat unique.

## Réalisé

- [DECISIONS.md](<repo>/runs/sol-scientific-v2-001/solution/DECISIONS.md) arbitre chaque recommandation.
- [scientific_calculator.py](<repo>/runs/sol-scientific-v2-001/solution/scientific_calculator.py) implémente lexer, parseur, évaluation sûre, échantillonnage, SVG autonome et CLI résiliente.
- [README.md](<repo>/runs/sol-scientific-v2-001/solution/README.md) documente syntaxe, API, exemples, sécurité et limites.

Échanges consultants conservés dans l’ordre reçu : SA-01 initial → SA-02 initial → SA-01 contradiction → SA-02 contradiction. Leurs convergences ont été retenues ; les plafonds de ressources arbitraires ont été écartés car non contractuels.

## Vérifications

Les contrôles ciblés passent :

- précédence, puissance à droite et exposants signés ;
- fonctions, domaines, finitude et division par zéro ;
- refus des syntaxes et caractères interdits ;
- bornes et discontinuités de courbes ;
- SVG XML sûr, segmenté et robuste aux flottants extrêmes ;
- historique, reprise après erreur et commande CLI `plot` ;
- aucune invocation de `eval`, `exec` ou `compile`.

Le vérificateur officiel n’a volontairement pas été lancé, conformément à la frontière de cette phase.

## TODO

- [x] Première solution complète et documentée.
- [ ] Faire examiner cette version par SA-03.
- [ ] En phase finale, intégrer les corrections confirmées puis lancer exactement le vérificateur officiel.

## Livraison Git

Aucune opération Git n’a été effectuée, conformément au protocole.
````

### MSG-006 — critique adversariale

Direction : `MAIN/RELAY → SA-03 → MAIN`. Réponse visible : 666 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-03, critique QA adversarial en lecture seule. Examine le challenge, les avis transmis, la table de décisions et la première solution ci-dessous. En 1 200 mots maximum, cherche omissions, failles de sécurité, erreurs de contrat, cas limites et régressions. Distingue défaut confirmé, risque et préférence. N'utilise aucun outil, ne délègue rien et ne réécris pas la solution.
--- BEGIN CHALLENGE ---
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

--- END CHALLENGE ---

--- BEGIN CONSULTATIONS ---

--- BEGIN SA01_INITIAL ---
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
## Révision SA-01 après avis SA-02

Les deux avis convergent fortement. SA-02 confirme les priorités essentielles : pipeline lexer–parseur–évaluateur, consommation intégrale de l’entrée, grammaire fermée, puissance associative à droite, exposant signé, table blanche, résultats finis, conservation de `ZeroDivisionError`, segmentation aux `None`, titre SVG assaini et historique limité aux opérations réussies. Les listes de cas critiques et de tests sont complémentaires, mais largement redondantes avec les risques déjà identifiés par SA-01.

Deux recommandations doivent toutefois être reclassées.

Premièrement, rejeter toutes les clés de `variables` autres que `x` est un choix de durcissement, pas nécessairement une obligation du contrat. L’exigence de sécurité est qu’aucune clé ne crée un nom accessible dans l’expression. Ignorer les clés surnuméraires peut être tout aussi sûr et davantage compatible avec un appelant fournissant un contexte plus large. Le candidat doit choisir selon le texte exact ou les tests, sans présenter le rejet comme imposé. En revanche, la valeur effectivement utilisée pour `x` doit être numérique réelle et finie; `bool` devrait être explicitement refusé malgré son héritage de `int`.

Deuxièmement, les plafonds de longueur, profondeur, jetons ou échantillons sont pertinents contre le déni de service, mais restent des extensions non contractuelles. Des seuils arbitraires risquent de rejeter des entrées valides du vérificateur. Ils sont donc secondaires tant qu’aucune limite n’est spécifiée, et doivent être documentés s’ils sont ajoutés.

Le principal accord d’architecture appelle une précision : parser une seule fois dans `sample_curve` est préférable, mais ne suffit pas à distinguer toutes les erreurs « globales » des erreurs « locales ». Syntaxe, nom inconnu et mauvais usage d’une fonction sont structurels et doivent être levés avant la boucle. Domaine, division, débordement et non-finitude dépendent de chaque valeur de `x` et deviennent `None`. Cette classification doit reposer sur les phases du moteur, pas sur une capture générale répétée.

Pour le SVG, `ElementTree` ou `html.escape` empêche l’injection de balises, mais ne règle pas automatiquement tous les caractères interdits par XML. La validation ou neutralisation des contrôles illégaux demeure nécessaire. Les axes au bord lorsque zéro est hors domaine, comme la politique d’écrasement, sont des décisions de rendu ou d’I/O et non des priorités de sécurité.

Priorités consolidées :

1. Grammaire exacte et consommation intégrale.
2. Résolution fermée des noms et appels.
3. Typage, finitude et classification stable des exceptions.
4. Séparation des erreurs structurelles et ponctuelles dans l’échantillonnage.
5. SVG XML valide, inerte et segmenté.
6. Résilience CLI et historique transactionnel.
7. Durcissement anti-DoS et politiques de fichiers, uniquement après conformité au contrat.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
## Révision consolidée SA-02

Les deux avis convergent fortement et se confirment sur l’architecture centrale : lexer à consommation totale, parseur dédié, AST, évaluateur par tables blanches, échantillonnage séparé, rendu SVG déterministe et CLI limitée à l’orchestration. Ils s’accordent également sur les priorités sémantiques : puissance associative à droite, priorité sur le signe unaire, exposant signé, résultats finis, maintien de `ZeroDivisionError`, conversion des autres erreurs attendues en `ValueError`, segmentation aux discontinuités et historique réservé aux opérations réussies.

Les recommandations suivantes sont donc des doublons à fusionner, non des décisions indépendantes :

- consommation intégrale de l’entrée et rejet des constructions hors grammaire ;
- distinction entre erreurs globales d’expression et erreurs numériques ponctuelles dans `sample_curve` ;
- échappement XML et interdiction de contenu actif ;
- rejet de `bool` pour `samples`, bornes finies et inclusion des extrémités ;
- ajout à l’historique seulement après écriture effective du SVG.

SA-01 complète utilement mon avis sur quatre cas sensibles : caractères Unicode ressemblants, caractères de contrôle XML, profondeur syntaxique excessive et volume d’échantillonnage pathologique. Je révise donc la stratégie de validation pour inclure explicitement ces familles. Toutefois, des plafonds de longueur, profondeur, jetons ou échantillons ne doivent pas être inventés arbitrairement s’ils ne figurent pas dans le contrat : ils risqueraient de rejeter des entrées valides et de créer une incompatibilité avec le vérificateur. La bonne priorité est d’abord d’éviter les comportements explosifs évidents ; toute limite supplémentaire doit être déterministe, documentée et justifiée comme décision d’implémentation.

Je précise aussi deux arbitrages où nos formulations pourraient être trop prescriptives :

1. Pour `variables`, l’invariant obligatoire est que seul `x` soit résolvable par le langage. Rejeter les clés supplémentaires est une politique défendable, mais les ignorer sans les rendre accessibles peut également respecter cet invariant. Il faut choisir selon le texte exact du contrat et tester la décision.
2. Pour le SVG, l’absence de points finis doit lever `ValueError`, mais un segment contenant un seul point mérite un traitement explicite : un chemin composé uniquement d’un déplacement peut être invisible. Un élément `circle`, ou une convention de rendu stable, doit être prévu si le contrat exige que tout point valide soit représenté.

Ordre de priorité consolidé :

1. Grammaire et précédence exactes, avec consommation totale.
2. Surface d’évaluation fermée et absence de mécanisme dynamique.
3. Taxonomie stable des exceptions et garantie de finitude.
4. Parsing unique de la courbe, puis tolérance limitée aux erreurs dépendant de `x`.
5. SVG analysable, segmenté, sans injection ni coordonnées non finies.
6. CLI résiliente et historique transactionnel.
7. Limites de ressources et cas dégénérés, sans durcir arbitrairement l’API.

La meilleure structure de test reste modulaire : tests du lexer, du parseur/AST, de l’évaluateur, de l’échantillonnage, du rendu XML puis tests d’intégration CLI. Cette séparation permettra d’attribuer immédiatement chaque échec à un invariant précis.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION ---

--- BEGIN FILE solution/DECISIONS.md ---
# Table d'arbitrage — première solution

Cette table synthétise les quatre textes autorisés de SA-01 et SA-02. Les
recommandations répétées ont été regroupées, mais chaque avis est relié à une
décision explicite. Les consultants sont en lecture seule et leurs avis restent
non contraignants ; l'orchestrateur candidat demeure l'unique décideur et
écrivain.

| Sources | Recommandation | Décision | Motivation et conséquence vérifiable |
|---|---|---|---|
| SA-01 initial, SA-02 initial, deux révisions | Séparer lexer, parseur, AST, évaluateur, API, SVG et CLI ; consommer toute l'entrée. | **Retenue.** | Une grammaire fermée et des phases distinctes rendent la précédence testable et empêchent l'accès à des constructions Python. |
| SA-01 initial, SA-02 initial, deux révisions | Interdire toute évaluation dynamique et résoudre constantes/fonctions par listes blanches. | **Retenue.** | Aucun `eval`, `exec`, `compile`, attribut, index, chaîne, import ou appel arbitraire ne sera utilisé ou accepté. |
| SA-01 initial, SA-02 initial, deux révisions | Implémenter `^` à droite, plus prioritaire que les signes, tout en acceptant un exposant signé. | **Retenue.** | La grammaire visera simultanément `2^3^2 == 512`, `-2^2 == -4` et `2^-2 == 0.25`. |
| SA-01 initial, SA-02 initial | Accepter les littéraux décimaux/scientifiques usuels, une fonction unaire avec parenthèses, et refuser virgule, `**`, multiplication implicite et suffixe résiduel. | **Retenue.** | Cela suit exactement la surface du langage spécifié et évite les reconnaissances partielles. Les espaces ASCII sont ignorés ; les autres caractères, notamment les ressemblants Unicode, sont rejetés. |
| SA-01 initial, SA-02 initial, deux révisions | Garantir un `float` fini ; préserver `ZeroDivisionError` et convertir domaine réel, complexe, débordement et non-finitude en `ValueError`. | **Retenue.** | La taxonomie d'erreurs fait partie du contrat public et ne doit pas laisser fuir des exceptions arithmétiques internes attendues. |
| SA-01 initial, SA-02 initial, deux révisions | Seul `x` est résolvable ; décider si les autres clés de `variables` sont rejetées ou ignorées ; refuser les valeurs invalides et les booléens. | **Retenue avec arbitrage : clés supplémentaires rejetées.** | Le dictionnaire est validé strictement : seulement `x`, valeur réelle finie, non booléenne. Cette politique simple rend les fautes d'appel visibles sans élargir le langage. |
| SA-01 initial, SA-02 initial, deux révisions | Valider des bornes finies, `x_min < x_max`, un entier véritable `samples >= 2`, inclure exactement les deux bornes. | **Retenue.** | Le dernier `x` sera forcé à `x_max`; `bool` sera refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Parser une seule fois ; lever les erreurs structurelles de `sample_curve`, convertir seulement les erreurs numériques dépendant de `x` en `None`. | **Retenue.** | Syntaxe, noms et mauvais appels seront validés avant la boucle. Division, domaine, dépassement et résultat non fini à un échantillon couperont localement la courbe. |
| SA-01 initial, SA-02 initial, deux révisions | Ajouter des plafonds de longueur, profondeur, jetons ou nombre d'échantillons contre le déni de service. | **Écartée pour cette version.** | Les révisions reconnaissent qu'aucun seuil n'est contractuel et qu'un plafond arbitraire pourrait rejeter une entrée d'acceptation valide. Les erreurs de récursion seront néanmoins normalisées, sans promettre la prise en charge d'entrées pathologiques. |
| SA-01 initial, SA-02 initial, deux révisions | Produire un SVG déterministe, autonome, analysable et inerte ; valider les nombres, échapper le titre et traiter les contrôles XML interdits. | **Retenue.** | Le document sera construit avec `xml.etree.ElementTree`, sans script, lien ni attribut actif. Le titre sera vérifié selon XML 1.0 avant sérialisation. |
| SA-01 initial, SA-02 initial, deux révisions | Chaque `None` coupe la courbe ; gérer les domaines dégénérés et les séquences d'un seul point ; lever si aucun point fini. | **Retenue.** | Chaque série contiguë aura son propre `polyline`; un singleton sera rendu par `circle`. Les étendues nulles seront élargies de façon déterministe. |
| SA-02 initial | Décider où placer un axe lorsque zéro est hors domaine. | **Retenue avec arbitrage : projection bornée au bord.** | Chaque axe reste un élément `line`; sa position est la projection de zéro limitée à la zone de tracé. |
| SA-01 initial, SA-02 initial | Autoriser ou refuser l'écrasement d'un SVG existant et ne pas inventer de bac à sable de chemins. | **Retenue avec arbitrage : écrasement autorisé.** | `output_path` est honoré comme fourni et l'écriture UTF-8 remplace un fichier existant, comportement standard documenté. Le nom CLI vide est refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Rendre la CLI résiliente ; évaluer les bornes de `plot` avec le moteur ; exiger quatre champs et enregistrer seulement les succès complets. | **Retenue.** | Les erreurs sont affichées sans traceback et la boucle continue. `help`, `history`, `clear`, erreurs et sorties ne sont pas historisés ; un tracé l'est seulement après l'écriture. |
| SA-02 initial | Définir le comportement sur EOF et interruption clavier. | **Retenue : sortie propre.** | EOF et `KeyboardInterrupt` terminent la boucle avec une ligne de séparation, sans traceback. |
| SA-01 initial, SA-02 initial, deux révisions | Documenter syntaxe, radians, erreurs, discontinuités, absence de multiplication implicite, écrasement et limites ; effectuer des contrôles modulaires ciblés. | **Retenue.** | Le README couvrira l'API et la CLI. Cette phase exécutera des tests ciblés du moteur, SVG et CLI, mais pas le vérificateur officiel réservé à la phase suivant SA-03. |


--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Scientific Calculator

Cette solution fournit un moteur d'expressions fermé, un échantillonneur de
courbes, un export SVG autonome et une interface interactive. Elle utilise
uniquement la bibliothèque standard de Python 3.10 ou supérieur.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/scientific_calculator.py
```

La boucle affiche l'invite `>`. Une expression est calculée immédiatement :

```text
> sqrt(2) ^ 2
2.0000000000000004
```

Les commandes disponibles sont `help`, `history`, `clear`, `quit` et `exit`.
Seules les évaluations et écritures de courbes entièrement réussies figurent
dans l'historique de la session.

## Langage accepté

- Littéraux entiers, décimaux et scientifiques : `2`, `.5`, `1.`, `6.02e23`.
- Opérateurs : `+`, `-`, `*`, `/`, `^` et parenthèses.
- Constantes : `pi`, `e`.
- Fonctions à un argument : `sin`, `cos`, `tan`, `asin`, `acos`, `atan`,
  `sqrt`, `ln`, `log10`, `exp`, `abs`.
- Variable `x`, seulement lorsqu'une valeur est fournie par l'API ou pendant
  l'échantillonnage d'une courbe.

Les angles sont en radians. La puissance est associative à droite et plus
prioritaire que les signes : `2^3^2` vaut `512.0`, `-2^2` vaut `-4.0`, et
`2^-2` vaut `0.25`.

Le langage n'accepte pas la multiplication implicite (`2pi`, `2(x)`), les
virgules, chaînes, crochets, attributs, mots-clés Python, opérateur `**` ou
appel d'une fonction non listée. Une fonction exige exactement un argument
entre parenthèses.

## Tracer une courbe

La commande `plot` contient exactement quatre champs séparés par des
points-virgules. Les bornes sont elles-mêmes des expressions sûres :

```text
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

Le fichier UTF-8 obtenu ne dépend d'aucune ressource externe et ne contient
aucun contenu actif. Une valeur hors domaine ou non finie devient une coupure
dans la courbe au lieu de faire échouer tout le tracé. Un fichier existant au
chemin demandé est remplacé ; les répertoires parents ne sont pas créés.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

value = evaluate("sin(pi / 2)")
value_at_two = evaluate("x^2 + 1", {"x": 2.0})
points = sample_curve("1 / x", -1.0, 1.0, samples=201)
write_svg(points, "inverse.svg", title="1 / x")
```

`evaluate` retourne toujours un `float` fini. Une expression vide, mal formée,
un nom inconnu, une valeur non réelle ou hors domaine lève `ValueError`; une
division par zéro lève `ZeroDivisionError`. Le dictionnaire `variables`, s'il
est fourni, ne peut contenir que `x`, associé à un réel fini non booléen.

`sample_curve` exige des bornes finies strictement croissantes et un entier
`samples >= 2`; les deux bornes sont incluses. Les erreurs de syntaxe et de nom
sont levées avant l'échantillonnage. Les erreurs numériques ponctuelles sont
représentées par `None`.

`write_svg` exige au moins un couple de coordonnées finies. Chaque `None` ou
coordonnée non finie coupe le segment. Les titres sont sérialisés comme texte
XML et les caractères interdits par XML 1.0 sont refusés.

## Sécurité et limites

Le lexer consomme toute l'entrée et le parseur n'expose qu'une liste blanche
d'opérations mathématiques. Aucun code, commande système, accès réseau,
attribut ou import issu d'une expression n'est exécuté.

La solution n'impose pas de plafond arbitraire à la longueur d'une expression
ou au nombre d'échantillons. L'appelant doit donc choisir des tailles adaptées
à ses ressources. Une imbrication qui dépasse les capacités récursives de
Python est signalée comme expression trop profonde. Le calcul utilise les
flottants binaires de Python : les arrondis usuels sont visibles et les
résultats infinis sont refusés.

--- END FILE solution/README.md ---

--- BEGIN FILE solution/scientific_calculator.py ---
#!/usr/bin/env python3
"""Calculatrice scientifique sûre et générateur de courbes SVG.

Le langage d'expressions est analysé par un lexer et un parseur dédiés. Il
n'utilise aucun mécanisme d'exécution dynamique de code Python.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numbers
import os
import re
from typing import Callable, Sequence
import xml.etree.ElementTree as ET


_NUMBER_PATTERN = r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
_NAME_PATTERN = r"[A-Za-z][A-Za-z0-9]*"
_CONSTANTS = {"pi": math.pi, "e": math.e}
_FUNCTIONS: dict[str, Callable[[float], float]] = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "abs": abs,
}
_SINGLE_CHAR_TOKENS = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "^": "CARET",
    "(": "LPAREN",
    ")": "RPAREN",
}
_ASCII_WHITESPACE = " \t\r\n\f\v"


@dataclass(frozen=True)
class _Token:
    kind: str
    value: str
    position: int


_Ast = tuple


def _tokenize(expression: str) -> list[_Token]:
    if not isinstance(expression, str):
        raise ValueError("L'expression doit être une chaîne de caractères")
    if not expression.strip(_ASCII_WHITESPACE):
        raise ValueError("L'expression est vide")

    tokens: list[_Token] = []
    position = 0
    while position < len(expression):
        character = expression[position]
        if character in _ASCII_WHITESPACE:
            position += 1
            continue

        remaining = expression[position:]
        number_match = re.match(_NUMBER_PATTERN, remaining, re.ASCII)
        if number_match is not None:
            value = number_match.group(0)
            tokens.append(_Token("NUMBER", value, position))
            position += number_match.end()
            continue

        name_match = re.match(_NAME_PATTERN, remaining, re.ASCII)
        if name_match is not None:
            value = name_match.group(0)
            tokens.append(_Token("NAME", value, position))
            position += name_match.end()
            continue

        kind = _SINGLE_CHAR_TOKENS.get(character)
        if kind is None:
            raise ValueError(
                f"Caractère interdit à la position {position + 1}: {character!r}"
            )
        tokens.append(_Token(kind, character, position))
        position += 1

    tokens.append(_Token("EOF", "", len(expression)))
    return tokens


class _Parser:
    """Parseur descendant récursif du petit langage arithmétique."""

    def __init__(self, tokens: Sequence[_Token]) -> None:
        self._tokens = tokens
        self._index = 0

    @property
    def _current(self) -> _Token:
        return self._tokens[self._index]

    def _accept(self, kind: str) -> _Token | None:
        if self._current.kind != kind:
            return None
        token = self._current
        self._index += 1
        return token

    def _expect(self, kind: str, message: str) -> _Token:
        token = self._accept(kind)
        if token is None:
            raise ValueError(
                f"{message} à la position {self._current.position + 1}"
            )
        return token

    def parse(self) -> _Ast:
        node = self._sum()
        if self._current.kind != "EOF":
            raise ValueError(
                f"Élément inattendu à la position {self._current.position + 1}"
            )
        return node

    def _sum(self) -> _Ast:
        node = self._product()
        while self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._product())
        return node

    def _product(self) -> _Ast:
        node = self._unary()
        while self._current.kind in ("STAR", "SLASH"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._unary())
        return node

    def _unary(self) -> _Ast:
        if self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            return ("unary", operator, self._unary())
        return self._power()

    def _power(self) -> _Ast:
        node = self._primary()
        if self._accept("CARET") is not None:
            # L'exposant passe par _unary : la puissance reste associative à
            # droite tout en autorisant 2^-2.
            node = ("binary", "^", node, self._unary())
        return node

    def _primary(self) -> _Ast:
        number = self._accept("NUMBER")
        if number is not None:
            try:
                value = float(number.value)
            except (ValueError, OverflowError) as error:
                raise ValueError("Littéral numérique invalide") from error
            if not math.isfinite(value):
                raise ValueError("Le littéral numérique n'est pas fini")
            return ("number", value)

        name_token = self._accept("NAME")
        if name_token is not None:
            name = name_token.value
            if self._accept("LPAREN") is not None:
                if name not in _FUNCTIONS:
                    raise ValueError(f"Fonction inconnue: {name}")
                argument = self._sum()
                self._expect("RPAREN", "Parenthèse fermante attendue")
                return ("call", name, argument)
            if name in _CONSTANTS:
                return ("number", _CONSTANTS[name])
            if name == "x":
                return ("variable", "x")
            if name in _FUNCTIONS:
                raise ValueError(f"La fonction {name} doit être appelée")
            raise ValueError(f"Nom inconnu: {name}")

        if self._accept("LPAREN") is not None:
            node = self._sum()
            self._expect("RPAREN", "Parenthèse fermante attendue")
            return node

        raise ValueError(
            f"Nombre, nom ou parenthèse attendu à la position "
            f"{self._current.position + 1}"
        )


def _parse_expression(expression: str) -> _Ast:
    try:
        return _Parser(_tokenize(expression)).parse()
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée") from error


def _finite_float(value: object, description: str) -> float:
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{description} doit être un nombre réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{description} doit être un nombre réel fini") from error
    if not math.isfinite(result):
        raise ValueError(f"{description} doit être fini")
    return result


def _checked_result(value: object) -> float:
    if isinstance(value, complex):
        raise ValueError("Le résultat sort du domaine réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Résultat numérique invalide") from error
    if not math.isfinite(result):
        raise ValueError("Le résultat n'est pas fini")
    return result


def _evaluate_ast(node: _Ast, variables: dict[str, float]) -> float:
    kind = node[0]
    if kind == "number":
        return node[1]
    if kind == "variable":
        if "x" not in variables:
            raise ValueError("La variable x n'a pas de valeur")
        return variables["x"]
    if kind == "unary":
        value = _evaluate_ast(node[2], variables)
        return _checked_result(value if node[1] == "+" else -value)
    if kind == "call":
        argument = _evaluate_ast(node[2], variables)
        try:
            return _checked_result(_FUNCTIONS[node[1]](argument))
        except (ValueError, OverflowError) as error:
            raise ValueError(f"Argument hors domaine pour {node[1]}") from error

    left = _evaluate_ast(node[2], variables)
    right = _evaluate_ast(node[3], variables)
    operator = node[1]
    try:
        if operator == "+":
            value = left + right
        elif operator == "-":
            value = left - right
        elif operator == "*":
            value = left * right
        elif operator == "/":
            value = left / right
        else:
            value = left**right
    except ZeroDivisionError:
        raise
    except (ValueError, OverflowError) as error:
        raise ValueError("Opération hors du domaine réel") from error
    return _checked_result(value)


def _validated_variables(
    variables: dict[str, float] | None,
) -> dict[str, float]:
    if variables is None:
        return {}
    if not isinstance(variables, dict):
        raise ValueError("variables doit être un dictionnaire")
    extra_names = set(variables) - {"x"}
    if extra_names:
        raise ValueError("Seule la variable x est autorisée")
    if "x" not in variables:
        return {}
    return {"x": _finite_float(variables["x"], "La variable x")}


def evaluate(
    expression: str,
    variables: dict[str, float] | None = None,
) -> float:
    """Évalue *expression* dans le langage sûr et retourne un float fini.

    ``ValueError`` signale une syntaxe, un nom, un domaine réel ou une valeur
    non finie invalide. Une division par zéro conserve ``ZeroDivisionError``.
    """

    parsed = _parse_expression(expression)
    validated_variables = _validated_variables(variables)
    try:
        return _checked_result(_evaluate_ast(parsed, validated_variables))
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée") from error


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne une expression et marque les valeurs indéfinies par None."""

    minimum = _finite_float(x_min, "x_min")
    maximum = _finite_float(x_max, "x_max")
    if minimum >= maximum:
        raise ValueError("x_min doit être strictement inférieur à x_max")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("samples doit être un entier au moins égal à 2")

    # Le parsing préalable fait remonter les erreurs structurelles une seule
    # fois. Seules les erreurs numériques propres à un point deviennent None.
    parsed = _parse_expression(expression)
    points: list[tuple[float, float | None]] = []
    denominator = samples - 1
    for index in range(samples):
        if index == 0:
            x_value = minimum
        elif index == denominator:
            x_value = maximum
        else:
            ratio = index / denominator
            x_value = (1.0 - ratio) * minimum + ratio * maximum
        try:
            y_value = _checked_result(_evaluate_ast(parsed, {"x": x_value}))
        except (ValueError, ZeroDivisionError, OverflowError, RecursionError):
            y_value = None
        points.append((x_value, y_value))
    return points


def _is_valid_xml_text(text: str) -> bool:
    for character in text:
        codepoint = ord(character)
        if not (
            codepoint in (0x09, 0x0A, 0x0D)
            or 0x20 <= codepoint <= 0xD7FF
            or 0xE000 <= codepoint <= 0xFFFD
            or 0x10000 <= codepoint <= 0x10FFFF
        ):
            return False
    return True


def _svg_number(value: float) -> str:
    if not math.isfinite(value):
        raise ValueError("Coordonnée SVG non finie")
    return format(value, ".12g")


def _expanded_bounds(value: float) -> tuple[float, float]:
    """Crée une étendue finie autour d'une coordonnée unique."""

    expansion = max(1.0, abs(value) * 0.05)
    low = value - expansion
    high = value + expansion
    if not math.isfinite(low):
        low = value
    if not math.isfinite(high):
        high = value
    if low == high:
        low = math.nextafter(value, -math.inf)
        high = math.nextafter(value, math.inf)
        if not math.isfinite(low):
            low = value
        if not math.isfinite(high):
            high = value
    if low == high:
        raise ValueError("Étendue graphique impossible à représenter")
    return low, high


def _relative_position(value: float, low: float, high: float) -> float:
    """Calcule une position relative sans faire déborder high - low."""

    scale = max(abs(low), abs(high), 1.0)
    low_scaled = low / scale
    high_scaled = high / scale
    value_scaled = value / scale
    return (value_scaled - low_scaled) / (high_scaled - low_scaled)


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Écrit une représentation SVG autonome des points fournis.

    Les valeurs ``None`` ou non finies séparent les segments. Un fichier
    existant à *output_path* est remplacé.
    """

    if not isinstance(title, str) or not _is_valid_xml_text(title):
        raise ValueError("Le titre contient des caractères XML invalides")
    try:
        path = os.fspath(output_path)
    except TypeError as error:
        raise ValueError("Chemin de sortie invalide") from error
    if not isinstance(path, (str, bytes)) or not path:
        raise ValueError("Le chemin de sortie est vide")
    if not isinstance(points, list):
        raise ValueError("points doit être une liste")

    normalized: list[tuple[float, float] | None] = []
    finite_points: list[tuple[float, float]] = []
    for point in points:
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            raise ValueError("Chaque point doit contenir exactement x et y")
        x_raw, y_raw = point
        if y_raw is None:
            normalized.append(None)
            continue
        if (
            isinstance(x_raw, bool)
            or isinstance(y_raw, bool)
            or not isinstance(x_raw, numbers.Real)
            or not isinstance(y_raw, numbers.Real)
        ):
            raise ValueError("Les coordonnées doivent être des nombres réels")
        try:
            x_value = float(x_raw)
            y_value = float(y_raw)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("Coordonnée invalide") from error
        if not math.isfinite(x_value) or not math.isfinite(y_value):
            normalized.append(None)
            continue
        finite_point = (x_value, y_value)
        normalized.append(finite_point)
        finite_points.append(finite_point)

    if not finite_points:
        raise ValueError("Aucun point fini ne peut être tracé")

    x_values = [point[0] for point in finite_points]
    y_values = [point[1] for point in finite_points]
    x_low, x_high = min(x_values), max(x_values)
    y_low, y_high = min(y_values), max(y_values)
    if x_low == x_high:
        x_low, x_high = _expanded_bounds(x_low)
    if y_low == y_high:
        y_low, y_high = _expanded_bounds(y_low)

    width, height, margin = 800.0, 500.0, 55.0
    plot_width = width - 2.0 * margin
    plot_height = height - 2.0 * margin

    def project_x(value: float) -> float:
        return margin + _relative_position(value, x_low, x_high) * plot_width

    def project_y(value: float) -> float:
        return height - margin - _relative_position(value, y_low, y_high) * plot_height

    axis_x = min(max(project_x(0.0), margin), width - margin)
    axis_y = min(max(project_y(0.0), margin), height - margin)

    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    root = ET.Element(
        f"{{{namespace}}}svg",
        {
            "viewBox": "0 0 800 500",
            "width": "800",
            "height": "500",
            "role": "img",
        },
    )
    if title:
        title_element = ET.SubElement(root, f"{{{namespace}}}title")
        title_element.text = title
    ET.SubElement(
        root,
        f"{{{namespace}}}rect",
        {"width": "800", "height": "500", "fill": "#ffffff"},
    )
    axis_style = {"stroke": "#666666", "stroke-width": "1"}
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(margin),
            "y1": _svg_number(axis_y),
            "x2": _svg_number(width - margin),
            "y2": _svg_number(axis_y),
            **axis_style,
        },
    )
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(axis_x),
            "y1": _svg_number(margin),
            "x2": _svg_number(axis_x),
            "y2": _svg_number(height - margin),
            **axis_style,
        },
    )

    def append_segment(segment: list[tuple[float, float]]) -> None:
        projected = [
            (project_x(x_value), project_y(y_value))
            for x_value, y_value in segment
        ]
        if len(projected) == 1:
            x_screen, y_screen = projected[0]
            ET.SubElement(
                root,
                f"{{{namespace}}}circle",
                {
                    "cx": _svg_number(x_screen),
                    "cy": _svg_number(y_screen),
                    "r": "2.5",
                    "fill": "#1769aa",
                },
            )
            return
        coordinates = " ".join(
            f"{_svg_number(x_screen)},{_svg_number(y_screen)}"
            for x_screen, y_screen in projected
        )
        ET.SubElement(
            root,
            f"{{{namespace}}}polyline",
            {
                "points": coordinates,
                "fill": "none",
                "stroke": "#1769aa",
                "stroke-width": "2",
                "stroke-linejoin": "round",
                "stroke-linecap": "round",
            },
        )

    current_segment: list[tuple[float, float]] = []
    for point in normalized:
        if point is None:
            if current_segment:
                append_segment(current_segment)
                current_segment = []
        else:
            current_segment.append(point)
    if current_segment:
        append_segment(current_segment)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)


_HELP = """Commandes :
  <expression>                         évaluer une expression
  plot <expression>; <min>; <max>; <fichier.svg>
                                       tracer une courbe
  history                              afficher l'historique réussi
  clear                                vider l'historique
  help                                 afficher cette aide
  quit | exit                          quitter

Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs
Constantes : pi e    Variable de tracé : x    Angles : radians"""


def _handle_line(line: str, history: list[str]) -> bool:
    """Traite une ligne de CLI. Retourne False lorsqu'il faut quitter."""

    command = line.strip()
    if command in ("quit", "exit"):
        return False
    if command == "help":
        print(_HELP)
        return True
    if command == "history":
        if not history:
            print("Historique vide.")
        else:
            for index, entry in enumerate(history, start=1):
                print(f"{index}: {entry}")
        return True
    if command == "clear":
        history.clear()
        print("Historique effacé.")
        return True

    if command == "plot" or command.startswith("plot "):
        fields = command[4:].strip().split(";")
        if len(fields) != 4 or any(not field.strip() for field in fields):
            raise ValueError(
                "Syntaxe: plot <expression>; <min>; <max>; <fichier.svg>"
            )
        expression, minimum_text, maximum_text, output_path = (
            field.strip() for field in fields
        )
        minimum = evaluate(minimum_text)
        maximum = evaluate(maximum_text)
        curve = sample_curve(expression, minimum, maximum)
        write_svg(curve, output_path, expression)
        history.append(command)
        print(f"Courbe enregistrée dans {output_path}")
        return True

    result = evaluate(command)
    history.append(command)
    # Quinze chiffres significatifs masquent les artefacts d'arrondi les plus
    # triviaux dans l'interface (sqrt(2)^2 s'affiche 2.0) sans modifier l'API.
    print(float(format(result, ".15g")))
    return True


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""

    history: list[str] = []
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        try:
            if not _handle_line(line, history):
                break
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur: {error}")


if __name__ == "__main__":
    main()

--- END FILE solution/scientific_calculator.py ---

--- END FIRST SOLUTION ---
````

</details>

#### Texte retourné pour MSG-006, mot pour mot

````text
## Défauts confirmés

- **Interruption clavier incomplètement gérée.** `KeyboardInterrupt` n’est intercepté qu’autour de `input()`. Un Ctrl-C pendant l’évaluation, l’échantillonnage, l’écriture SVG ou l’affichage produit donc potentiellement un traceback. Cela contredit la décision « EOF et `KeyboardInterrupt` terminent la boucle […] sans traceback » et fragilise l’exigence de résilience de la CLI.

- **La CLI peut afficher un résultat numériquement différent de celui calculé.** `print(float(format(result, ".15g")))` arrondit à quinze chiffres significatifs puis reconvertit. Par exemple, `1 + 1e-15` peut être affiché comme `1.0`, alors que `evaluate` renvoie approximativement `1.000000000000001`. Il ne s’agit pas seulement d’une présentation plus courte : une variation représentable disparaît.

- **Classification incorrecte d’une limite globale dans `sample_curve`.** Un long enchaînement associatif à gauche, tel qu’une somme de milliers de termes, est parsé itérativement mais produit un AST profond. Sa récursion d’évaluation peut lever `RecursionError`; `sample_curve` transforme alors cette erreur en `None` à chaque point. Une limite structurelle globale est donc présentée comme une discontinuité numérique locale, contrairement à la table de décisions (« seulement les erreurs numériques dépendant de `x` »).

- **Exemple README faux pour la CLI livrée.** La section « Lancement » montre `sqrt(2) ^ 2` donnant `2.0000000000000004`, alors que le formatage de `_handle_line` affiche `2.0`. L’API et la CLI ont effectivement des rendus différents, mais l’exemple est explicitement présenté comme une session interactive.

## Risques

- **Déni de service assumé mais réel.** L’absence de plafonds autorise des expressions, titres, listes de points ou nombres d’échantillons démesurés. `sample_curve` alloue toute la liste et évalue chaque point; une valeur massive peut bloquer durablement ou épuiser la mémoire. L’absence de limite n’est pas une violation explicite du contrat, mais elle affaiblit la promesse d’évaluation « sûre ».

- **Distinction global/local encore imparfaite.** Le parsing préalable détecte syntaxe et noms inconnus, mais une erreur numérique indépendante de `x`, par exemple `sqrt(-1)`, devient une liste entière de `None`. Le challenge permet raisonnablement cette lecture, mais le discours des décisions suggère une séparation plus sémantique que celle réellement obtenue.

- **Politique stricte de `variables` potentiellement incompatible.** Rejeter toute clé autre que `x` est documenté et sûr, mais non imposé par le contrat. Un vérificateur ou appelant peut raisonnablement fournir un contexte plus large en attendant que les clés inaccessibles soient simplement ignorées. Les consultations avaient précisément identifié cette divergence possible.

- **Écrasement de fichiers arbitraires.** La CLI honore chemins absolus, traversées et liens symboliques, puis remplace la cible directement. Cette politique est explicitement arbitrée et le contrat ne prescrit aucun bac à sable; elle reste néanmoins une surface dangereuse, surtout si la CLI est intégrée à un service ou lancée avec des privilèges élevés.

- **Écriture non transactionnelle.** `ElementTree.write` écrit directement dans la cible existante. Une erreur d’E/S en cours d’écriture peut laisser un fichier antérieur tronqué ou un SVG partiel, bien que le tracé ne soit ensuite pas ajouté à l’historique.

- **Injection de contrôle dans le terminal.** Le chemin de sortie est réaffiché brut et conservé dans l’historique. Un nom contenant des séquences de contrôle ou ANSI peut altérer l’affichage du terminal. Cela ne compromet pas le SVG, mais constitue une surface d’injection de présentation.

- **Taxonomie ambiguë pour les puissances de zéro négatives.** Python lève `ZeroDivisionError` pour certaines formes telles que `0^-1`. Le contrat réserve explicitement cette exception à « une division par zéro », sans préciser si une puissance équivalant à une réciproque doit suivre la même classification. Un test strict pourrait attendre `ValueError` comme opération hors domaine.

## Préférences, non défauts

- Exiger exactement une `list` dans `write_svg`, plutôt qu’un itérable, suit la signature publique et reste défendable.
- Transformer une coordonnée non finie en coupure est cohérent avec l’objectif, même si le contrat ne fixe pas précisément la validation des points fournis directement.
- Les axes projetés au bord, les singletons rendus par `circle` et l’écrasement autorisé sont des choix de rendu ou d’I/O documentés, pas des erreurs contractuelles.
- Le rejet des espaces Unicode, des booléens et de la multiplication implicite constitue un durcissement cohérent avec la grammaire fermée.
````

### MSG-007 — arbitrage final et vérification

Direction : `RELAY → MAIN`. Réponse visible : 555 mots.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2 — phase MAIN finale. Tu représentes le même rôle MAIN, orchestrateur candidat et unique écrivain, dans une nouvelle session éphémère mesurée. Aucun nouveau consultant n'est autorisé. Reprends la première solution présente dans `solution/`. Qualifie chaque point de SA-03 comme retenu, écarté ou non vérifiable et complète `solution/DECISIONS.md` avec la justification et la preuve. Applique uniquement les corrections retenues. Exécute ensuite le vérificateur officiel exactement ainsi : `python3 scripts/verify.py --challenge scientific-calculator --solution runs/sol-scientific-v2-001/solution`. Corrige les défauts confirmés jusqu'au verdict final. Écris uniquement dans `solution/`, n'effectue aucune opération Git et restitue rôles, arbitrages, premier passage, verdict final, corrections et limites.
--- BEGIN BASE MULTI-AGENT PROMPT ---
Réalise le défi décrit dans CHALLENGE.md en mode V2 multi-agent gouverné.

Contraintes particulières pour cette tentative :

- ne lis aucune autre tentative, solution ou résultat du dépôt ;
- utilise exactement trois consultants sans délégation imbriquée :
  1. analyste du contrat et de la sécurité,
  2. analyste de conception et de testabilité,
  3. critique final des cas limites ;
- les deux premiers interviennent avant l'implémentation et le critique après
  une première solution ;
- demande d'abord aux deux analystes une réponse indépendante de 1 200 mots
  maximum, sans leur montrer l'avis de l'autre ;
- relaie ensuite à chacun le texte visible intégral de l'autre et autorise une
  seule réponse contradictoire ou révision de 600 mots maximum ;
- synthétise leurs propositions dans une table d'arbitrage avant d'écrire ;
- transmets au critique le challenge, la première solution et cette table ; sa
  critique finale est limitée à 1 200 mots ;
- leurs missions sont consultatives et en lecture seule ; toi seul écris ;
- écris exclusivement dans `solution/` et ne modifie ni spécification, ni
  tests, ni scripts, ni gouvernance ;
- ne lance aucune opération Git (`git add`, `git commit`, `git push`) ;
- utilise uniquement la bibliothèque standard Python ;
- n'utilise jamais `eval()`, `exec()` ou `compile()` ;
- arbitre explicitement les recommandations retenues ou écartées ;
- lance le vérificateur indiqué dans CHALLENGE.md, corrige les défauts
  confirmés et termine avec une solution complète, documentée et sans
  placeholder ;
- résume les rôles, avis, arbitrages, tests, corrections et limites sans
  exposer de raisonnement interne brut.
- conserve dans ta restitution l'ordre et le texte visible des échanges afin
  que l'orchestrateur expérimental puisse produire le `PV.md` du run.

--- END BASE MULTI-AGENT PROMPT ---

--- BEGIN CHALLENGE ---
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

--- END CHALLENGE ---

--- BEGIN CONSULTATIONS ---

--- BEGIN SA01_INITIAL ---
## Avis SA-01 — exigences et sécurité

### Conclusion

Le contrat est réalisable avec la bibliothèque standard et suffisamment précis pour guider l’architecture générale : analyseur lexical et syntaxique dédié, évaluation par liste blanche, échantillonnage tolérant aux erreurs ponctuelles et génération XML/SVG sans contenu actif.

Quelques ambiguïtés peuvent toutefois produire des solutions raisonnables mais incompatibles entre elles. Elles doivent être arbitrées par le candidat de façon explicite et documentée, sans supposer que les tests couvrent uniquement les exemples.

### Obligations non négociables

1. **Aucune évaluation dynamique.** `eval`, `exec` et `compile` sont interdits. Les expressions doivent être analysées par une grammaire fermée. Aucun accès aux attributs, indexations, chaînes, imports, appels arbitraires ou opérateurs supplémentaires ne doit être possible.

2. **Sémantique exacte des puissances.** `^` signifie puissance, est associative à droite et lie plus fortement que le signe unaire : `2^3^2 = 512`, `-2^2 = -4`. L’analyseur doit néanmoins permettre un exposant signé, notamment `2^-2`, vraisemblablement égal à `0.25`.

3. **Classification des erreurs.** Une division par zéro doit conserver `ZeroDivisionError`. Les autres erreurs de syntaxe, nom, domaine réel ou résultat non fini doivent devenir `ValueError`, sans fuite accidentelle de `OverflowError` ou d’exceptions internes.

4. **Résultats strictement finis.** `evaluate` ne peut renvoyer ni `nan` ni `inf`, y compris si ceux-ci arrivent par `variables`.

5. **SVG sûr.** Tout texte utilisateur doit être échappé pour XML. Aucun script, gestionnaire d’évènement, lien externe, inclusion de ressource ou fragment XML brut ne doit être injecté. Les coordonnées doivent provenir uniquement de nombres finis contrôlés.

6. **CLI résiliente.** Toutes les erreurs attendues doivent être interceptées à la frontière interactive, affichées sans traceback, puis la boucle doit continuer. Seules les opérations entièrement réussies entrent dans l’historique.

### Arbitrages recommandés

| Sujet ambigu | Arbitrage recommandé |
|---|---|
| Contenu de `variables` | N’accepter que le nom `x`; rejeter les autres clés et les valeurs non numériques ou non finies. Le contrat du langage n’autorise aucune autre variable. |
| Arity des fonctions | Exiger exactement un argument pour toutes les fonctions listées. Rejeter virgules et appels multiples. |
| Littéraux | Accepter les formes Python usuelles décimales et scientifiques (`1`, `1.`, `.5`, `1e-3`), mais pas hexadécimal, underscore, `nan` ou `inf`. |
| Espaces et caractères | Autoriser les espaces ASCII autour des jetons; rejeter explicitement tout caractère ou identifiant hors grammaire, y compris les variantes Unicode ressemblantes. |
| Opérations hors domaine | Traiter racine négative, logarithme non positif, puissance produisant un complexe et dépassement comme `ValueError`. |
| `sample_curve` face à une expression invalide | Faire remonter les défauts globaux de syntaxe ou de nom. Convertir en `None` uniquement les erreurs dépendant du point (`ZeroDivisionError`, domaine, dépassement ou non-finitude). Cela évite de masquer une faute de saisie en « courbe vide ». |
| Paramètres d’échantillonnage | Exiger des bornes numériques finies, `x_min < x_max`, et un entier `samples >= 2`; refuser `bool`. |
| Paramètres CLI de `plot` | Évaluer `-pi` et `pi` avec le même moteur sûr, puis exiger des résultats finis. La forme doit comporter exactement expression, minimum, maximum et fichier. |
| Segmentation SVG | Construire une séquence distincte pour chaque série contiguë de points finis; chaque `None` coupe obligatoirement la courbe. |
| Étendue graphique nulle | Ajouter une marge déterministe lorsqu’une seule abscisse/ordonnée distincte est présente afin d’éviter une division par zéro. |
| Historique | Conserver l’entrée réussie sous une représentation stable; exclure erreurs, `help`, `history`, `clear`, `quit` et `exit`. N’ajouter un tracé qu’après écriture réussie. |

### Principales surfaces d’attaque

- **Contournement lexical :** identifiants préfixés, notation numérique mal formée, caractères Unicode, points, crochets, guillemets, virgules et suites comme `__class__`. La tokenisation doit consommer toute l’entrée; aucun caractère résiduel ne peut être ignoré.
- **Déni de service arithmétique :** puissances ou expressions profondément imbriquées peuvent consommer beaucoup de temps ou provoquer une récursion excessive. Des limites déterministes de longueur, nombre de jetons et profondeur sont recommandées, avec `ValueError`.
- **Déni de service par tracé :** un nombre d’échantillons gigantesque peut épuiser mémoire et CPU. Même si la CLI n’expose pas ce paramètre, l’API le fait; une borne maximale documentée est souhaitable.
- **Écriture de fichier :** le nom fourni permet potentiellement écrasement, chemin absolu ou traversée de répertoires. Le contrat exige un chemin arbitraire dans l’API et ne définit pas de bac à sable; ne pas inventer une restriction incompatible. En revanche, refuser un nom CLI vide et présenter clairement les erreurs d’E/S.
- **Injection XML :** l’échappement de `<`, `>`, `&` et des guillemets ne suffit pas si des caractères de contrôle interdits par XML sont conservés. Ils doivent être rejetés ou neutralisés.
- **Masquage excessif d’exceptions :** un `except Exception` dans le moteur pourrait cacher un défaut de programmation. Les conversions en erreurs métier doivent viser des exceptions identifiées; une interception plus large n’est acceptable qu’à la frontière CLI pour garantir l’absence de traceback.

### Risques de conformité

Les erreurs les plus probables sont une puissance rendue associative à gauche, une mauvaise priorité de `-2^2`, l’acceptation implicite de noms du dictionnaire, la propagation de `nan`/`inf`, la capture de toutes les erreurs de `sample_curve` en `None`, une courbe reliant les deux côtés d’une discontinuité, ou un titre SVG insuffisamment assaini.

La documentation devrait enfin distinguer syntaxe acceptée, erreurs, radians, absence de multiplication implicite, comportement aux discontinuités, politique d’écrasement des fichiers et limites de ressources. Aucun défaut manifeste du contrat ne rend le défi insoluble, mais les arbitrages ci-dessus méritent d’être consignés comme décisions d’implémentation plutôt que présentés comme exigences explicitement garanties par le texte.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
## Avis SA-02 — Architecture et testabilité

### Recommandation principale

Adopter une architecture en pipeline explicite :

```text
expression → lexer → parseur → AST → évaluateur
                                     ↓
                              échantillonnage
                                     ↓
                               rendu SVG
                                     ↓
                                    CLI
```

Cette séparation réduit les risques de sécurité, rend les règles de précédence vérifiables isolément et empêche la CLI ou le SVG de contaminer le moteur d’expression.

### 1. Structure proposée

Un seul fichier est imposé, mais il peut contenir des composants internes clairement délimités :

- **Lexer** : transforme exclusivement les caractères autorisés en jetons (`NUMBER`, `NAME`, opérateurs, parenthèses, fin).
- **Parseur descendant récursif** : construit un petit AST interne.
- **Évaluateur** : interprète cet AST au moyen de tables fermées de constantes et fonctions.
- **API publique** : `evaluate`, `sample_curve`, `write_svg`.
- **CLI** : parsing des commandes, historique et présentation des erreurs, sous garde `if __name__ == "__main__"`.

Le lexer doit consommer toute l’entrée. Aucun caractère inattendu, suffixe résiduel ou nom partiellement reconnu ne doit être ignoré.

### 2. Arbitrages de grammaire

Le point le plus sensible est l’interaction entre puissance et signes unaires. Il faut garantir simultanément :

- `2 ^ 3 ^ 2 == 512` : puissance associative à droite ;
- `-2 ^ 2 == -4` : puissance plus prioritaire que le signe ;
- `2 ^ -2 == 0.25` : exposant signé, comportement normalement attendu.

Une grammaire adaptée est conceptuellement :

```text
expression  := somme
somme       := produit (("+" | "-") produit)*
produit     := unaire (("*" | "/") unaire)*
unaire      := ("+" | "-") unaire | puissance
puissance   := primaire ("^" unaire)?
primaire    := NUMBER | NAME | NAME "(" expression ")" | "(" expression ")"
```

Le recours à `**` dans l’entrée doit être refusé : seul `^` appartient au langage.

Décision recommandée pour les appels : exactement un argument et exactement une paire de parenthèses syntaxiques par appel. Les virgules, appels implicites (`sin x`) et multiplications implicites (`2pi`, `2(x)`) sont hors contrat et doivent échouer.

### 3. Invariants du moteur

`evaluate` doit maintenir les invariants suivants :

- `variables` ne donne accès qu’à `x`; les autres clés ne créent pas de nouveaux noms.
- `x` sans valeur fournie produit `ValueError`.
- Toute réussite retourne un `float` fini.
- Tout résultat `NaN` ou infini, y compris après débordement, devient `ValueError`.
- Une division par zéro conserve spécifiquement `ZeroDivisionError`.
- Les erreurs de domaine réel (`sqrt(-1)`, `ln(0)`, `acos(2)`) deviennent `ValueError`.
- Aucun objet Python, attribut, indexation, mot-clé ou appel arbitraire n’est accessible.

Les fonctions doivent être résolues par une table blanche fermée. Il faut distinguer une constante utilisée comme fonction (`pi(2)`), une fonction utilisée sans appel (`sin`) et un nom inconnu : les trois sont invalides.

Pour la puissance, rester dans le domaine réel. Les résultats complexes doivent être refusés. Une base négative avec exposant non entier est un cas critique à normaliser en `ValueError`.

### 4. Échantillonnage

Valider d’abord :

- bornes finies ;
- `x_min < x_max` ;
- `samples` entier véritable, au moins égal à 2.

Les abscisses doivent suivre `x_min + i * (x_max - x_min) / (samples - 1)`, en forçant idéalement le dernier point à `x_max` afin d’assurer l’inclusion exacte des bornes.

À chaque point, `ValueError`, `ZeroDivisionError`, débordement ou résultat non fini donne `(x, None)`. Les défauts structurels de l’expression pourraient ainsi être répétés à chaque point ; une validation ou un parsing unique préalable est préférable pour la performance et la testabilité, sans toutefois modifier le contrat visible.

Arbitrage important : `sample_curve("nom_inconnu", ...)` pourrait produire uniquement des `None`. La spécification exige la tolérance aux points isolés, mais ne dit pas explicitement si une expression globalement invalide doit lever une erreur. Recommandation : distinguer les erreurs syntaxiques/noms inconnus, qui doivent être levées, des erreurs numériques dépendant de `x`, qui deviennent `None`.

### 5. Rendu SVG

`write_svg` doit être un rendu déterministe à partir des données, sans réévaluer l’expression.

Invariants :

- seuls les couples numériques finis sont traçables ;
- `None` coupe obligatoirement le chemin ;
- une nouvelle séquence commence après chaque interruption ;
- aucune liaison ne traverse une discontinuité explicite ;
- absence totale de point fini → `ValueError`.

Prévoir des marges fixes, un `viewBox` fixe et une transformation affine vers l’espace écran. Les domaines dégénérés (`tous les x identiques`, `tous les y identiques`) nécessitent un élargissement artificiel non nul. Les axes doivent toujours être des éléments `line`; si zéro est hors domaine, ils peuvent être placés au bord ou par projection bornée, à documenter.

Construire le XML avec `xml.etree.ElementTree` ou échapper systématiquement le titre avec `html.escape(..., quote=True)`. Le titre ne doit jamais être interpolé brut. Le SVG ne doit contenir ni `script`, ni gestionnaire `on*`, ni `href`, ni ressource externe.

### 6. CLI et historique

Séparer le traitement d’une ligne de la boucle d’entrée facilite les tests. Pour `plot`, découper sur `;`, puis retirer le préfixe `plot` uniquement au début. Exiger exactement quatre champs : expression, minimum, maximum, chemin.

Les bornes de tracé sont elles-mêmes des expressions (`-pi`, `pi`) et doivent donc passer par `evaluate`, pas par `float`.

L’historique ne doit enregistrer que les opérations entièrement réussies, notamment après écriture effective du SVG. `clear`, `help` et les erreurs ne devraient pas être enregistrés. Toutes les exceptions attendues doivent être converties en messages courts; `EOFError` et `KeyboardInterrupt` méritent une sortie propre.

### 7. Stratégie de validation prioritaire

Tests unitaires à forte valeur :

1. Grammaire : `-2^2`, `(-2)^2`, `2^-2`, `2^3^2`, `1--2`.
2. Lexique : notation scientifique valide et formes incomplètes (`1e`, `.`, `1..2`).
3. Sécurité : attributs, crochets, chaînes, virgules, `_`, `__import__`, `**`.
4. Numérique : division par `0` et `-0.0`, domaines, débordements, non-finis.
5. Courbes : deux échantillons, bornes exactes, `1/x` autour de zéro, séries de `None`.
6. SVG : XML analysable, titre hostile échappé, plusieurs segments, aucun contenu actif.
7. CLI : erreur suivie d’une commande valide, historique réussi uniquement, `clear`, sortie.

### Arbitrages à figer

Avant implémentation, le candidat principal devrait consigner ces décisions :

- erreurs globales de `sample_curve` levées, erreurs locales converties en `None`;
- axes hors domaine placés au bord ou projetés;
- politique envers `bool` pour `samples` et valeurs de variables;
- écrasement autorisé ou non d’un SVG existant;
- comportement précis sur EOF et interruption clavier.

La priorité absolue est le triptyque **grammaire exacte, table blanche fermée, normalisation cohérente des erreurs** : c’est là que se concentrent à la fois les risques fonctionnels, sécuritaires et de vérification indépendante.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
## Révision SA-01 après avis SA-02

Les deux avis convergent fortement. SA-02 confirme les priorités essentielles : pipeline lexer–parseur–évaluateur, consommation intégrale de l’entrée, grammaire fermée, puissance associative à droite, exposant signé, table blanche, résultats finis, conservation de `ZeroDivisionError`, segmentation aux `None`, titre SVG assaini et historique limité aux opérations réussies. Les listes de cas critiques et de tests sont complémentaires, mais largement redondantes avec les risques déjà identifiés par SA-01.

Deux recommandations doivent toutefois être reclassées.

Premièrement, rejeter toutes les clés de `variables` autres que `x` est un choix de durcissement, pas nécessairement une obligation du contrat. L’exigence de sécurité est qu’aucune clé ne crée un nom accessible dans l’expression. Ignorer les clés surnuméraires peut être tout aussi sûr et davantage compatible avec un appelant fournissant un contexte plus large. Le candidat doit choisir selon le texte exact ou les tests, sans présenter le rejet comme imposé. En revanche, la valeur effectivement utilisée pour `x` doit être numérique réelle et finie; `bool` devrait être explicitement refusé malgré son héritage de `int`.

Deuxièmement, les plafonds de longueur, profondeur, jetons ou échantillons sont pertinents contre le déni de service, mais restent des extensions non contractuelles. Des seuils arbitraires risquent de rejeter des entrées valides du vérificateur. Ils sont donc secondaires tant qu’aucune limite n’est spécifiée, et doivent être documentés s’ils sont ajoutés.

Le principal accord d’architecture appelle une précision : parser une seule fois dans `sample_curve` est préférable, mais ne suffit pas à distinguer toutes les erreurs « globales » des erreurs « locales ». Syntaxe, nom inconnu et mauvais usage d’une fonction sont structurels et doivent être levés avant la boucle. Domaine, division, débordement et non-finitude dépendent de chaque valeur de `x` et deviennent `None`. Cette classification doit reposer sur les phases du moteur, pas sur une capture générale répétée.

Pour le SVG, `ElementTree` ou `html.escape` empêche l’injection de balises, mais ne règle pas automatiquement tous les caractères interdits par XML. La validation ou neutralisation des contrôles illégaux demeure nécessaire. Les axes au bord lorsque zéro est hors domaine, comme la politique d’écrasement, sont des décisions de rendu ou d’I/O et non des priorités de sécurité.

Priorités consolidées :

1. Grammaire exacte et consommation intégrale.
2. Résolution fermée des noms et appels.
3. Typage, finitude et classification stable des exceptions.
4. Séparation des erreurs structurelles et ponctuelles dans l’échantillonnage.
5. SVG XML valide, inerte et segmenté.
6. Résilience CLI et historique transactionnel.
7. Durcissement anti-DoS et politiques de fichiers, uniquement après conformité au contrat.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
## Révision consolidée SA-02

Les deux avis convergent fortement et se confirment sur l’architecture centrale : lexer à consommation totale, parseur dédié, AST, évaluateur par tables blanches, échantillonnage séparé, rendu SVG déterministe et CLI limitée à l’orchestration. Ils s’accordent également sur les priorités sémantiques : puissance associative à droite, priorité sur le signe unaire, exposant signé, résultats finis, maintien de `ZeroDivisionError`, conversion des autres erreurs attendues en `ValueError`, segmentation aux discontinuités et historique réservé aux opérations réussies.

Les recommandations suivantes sont donc des doublons à fusionner, non des décisions indépendantes :

- consommation intégrale de l’entrée et rejet des constructions hors grammaire ;
- distinction entre erreurs globales d’expression et erreurs numériques ponctuelles dans `sample_curve` ;
- échappement XML et interdiction de contenu actif ;
- rejet de `bool` pour `samples`, bornes finies et inclusion des extrémités ;
- ajout à l’historique seulement après écriture effective du SVG.

SA-01 complète utilement mon avis sur quatre cas sensibles : caractères Unicode ressemblants, caractères de contrôle XML, profondeur syntaxique excessive et volume d’échantillonnage pathologique. Je révise donc la stratégie de validation pour inclure explicitement ces familles. Toutefois, des plafonds de longueur, profondeur, jetons ou échantillons ne doivent pas être inventés arbitrairement s’ils ne figurent pas dans le contrat : ils risqueraient de rejeter des entrées valides et de créer une incompatibilité avec le vérificateur. La bonne priorité est d’abord d’éviter les comportements explosifs évidents ; toute limite supplémentaire doit être déterministe, documentée et justifiée comme décision d’implémentation.

Je précise aussi deux arbitrages où nos formulations pourraient être trop prescriptives :

1. Pour `variables`, l’invariant obligatoire est que seul `x` soit résolvable par le langage. Rejeter les clés supplémentaires est une politique défendable, mais les ignorer sans les rendre accessibles peut également respecter cet invariant. Il faut choisir selon le texte exact du contrat et tester la décision.
2. Pour le SVG, l’absence de points finis doit lever `ValueError`, mais un segment contenant un seul point mérite un traitement explicite : un chemin composé uniquement d’un déplacement peut être invisible. Un élément `circle`, ou une convention de rendu stable, doit être prévu si le contrat exige que tout point valide soit représenté.

Ordre de priorité consolidé :

1. Grammaire et précédence exactes, avec consommation totale.
2. Surface d’évaluation fermée et absence de mécanisme dynamique.
3. Taxonomie stable des exceptions et garantie de finitude.
4. Parsing unique de la courbe, puis tolérance limitée aux erreurs dépendant de `x`.
5. SVG analysable, segmenté, sans injection ni coordonnées non finies.
6. CLI résiliente et historique transactionnel.
7. Limites de ressources et cas dégénérés, sans durcir arbitrairement l’API.

La meilleure structure de test reste modulaire : tests du lexer, du parseur/AST, de l’évaluateur, de l’échantillonnage, du rendu XML puis tests d’intégration CLI. Cette séparation permettra d’attribuer immédiatement chaque échec à un invariant précis.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION SNAPSHOT ---

--- BEGIN FILE solution/DECISIONS.md ---
# Table d'arbitrage — première solution

Cette table synthétise les quatre textes autorisés de SA-01 et SA-02. Les
recommandations répétées ont été regroupées, mais chaque avis est relié à une
décision explicite. Les consultants sont en lecture seule et leurs avis restent
non contraignants ; l'orchestrateur candidat demeure l'unique décideur et
écrivain.

| Sources | Recommandation | Décision | Motivation et conséquence vérifiable |
|---|---|---|---|
| SA-01 initial, SA-02 initial, deux révisions | Séparer lexer, parseur, AST, évaluateur, API, SVG et CLI ; consommer toute l'entrée. | **Retenue.** | Une grammaire fermée et des phases distinctes rendent la précédence testable et empêchent l'accès à des constructions Python. |
| SA-01 initial, SA-02 initial, deux révisions | Interdire toute évaluation dynamique et résoudre constantes/fonctions par listes blanches. | **Retenue.** | Aucun `eval`, `exec`, `compile`, attribut, index, chaîne, import ou appel arbitraire ne sera utilisé ou accepté. |
| SA-01 initial, SA-02 initial, deux révisions | Implémenter `^` à droite, plus prioritaire que les signes, tout en acceptant un exposant signé. | **Retenue.** | La grammaire visera simultanément `2^3^2 == 512`, `-2^2 == -4` et `2^-2 == 0.25`. |
| SA-01 initial, SA-02 initial | Accepter les littéraux décimaux/scientifiques usuels, une fonction unaire avec parenthèses, et refuser virgule, `**`, multiplication implicite et suffixe résiduel. | **Retenue.** | Cela suit exactement la surface du langage spécifié et évite les reconnaissances partielles. Les espaces ASCII sont ignorés ; les autres caractères, notamment les ressemblants Unicode, sont rejetés. |
| SA-01 initial, SA-02 initial, deux révisions | Garantir un `float` fini ; préserver `ZeroDivisionError` et convertir domaine réel, complexe, débordement et non-finitude en `ValueError`. | **Retenue.** | La taxonomie d'erreurs fait partie du contrat public et ne doit pas laisser fuir des exceptions arithmétiques internes attendues. |
| SA-01 initial, SA-02 initial, deux révisions | Seul `x` est résolvable ; décider si les autres clés de `variables` sont rejetées ou ignorées ; refuser les valeurs invalides et les booléens. | **Retenue avec arbitrage : clés supplémentaires rejetées.** | Le dictionnaire est validé strictement : seulement `x`, valeur réelle finie, non booléenne. Cette politique simple rend les fautes d'appel visibles sans élargir le langage. |
| SA-01 initial, SA-02 initial, deux révisions | Valider des bornes finies, `x_min < x_max`, un entier véritable `samples >= 2`, inclure exactement les deux bornes. | **Retenue.** | Le dernier `x` sera forcé à `x_max`; `bool` sera refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Parser une seule fois ; lever les erreurs structurelles de `sample_curve`, convertir seulement les erreurs numériques dépendant de `x` en `None`. | **Retenue.** | Syntaxe, noms et mauvais appels seront validés avant la boucle. Division, domaine, dépassement et résultat non fini à un échantillon couperont localement la courbe. |
| SA-01 initial, SA-02 initial, deux révisions | Ajouter des plafonds de longueur, profondeur, jetons ou nombre d'échantillons contre le déni de service. | **Écartée pour cette version.** | Les révisions reconnaissent qu'aucun seuil n'est contractuel et qu'un plafond arbitraire pourrait rejeter une entrée d'acceptation valide. Les erreurs de récursion seront néanmoins normalisées, sans promettre la prise en charge d'entrées pathologiques. |
| SA-01 initial, SA-02 initial, deux révisions | Produire un SVG déterministe, autonome, analysable et inerte ; valider les nombres, échapper le titre et traiter les contrôles XML interdits. | **Retenue.** | Le document sera construit avec `xml.etree.ElementTree`, sans script, lien ni attribut actif. Le titre sera vérifié selon XML 1.0 avant sérialisation. |
| SA-01 initial, SA-02 initial, deux révisions | Chaque `None` coupe la courbe ; gérer les domaines dégénérés et les séquences d'un seul point ; lever si aucun point fini. | **Retenue.** | Chaque série contiguë aura son propre `polyline`; un singleton sera rendu par `circle`. Les étendues nulles seront élargies de façon déterministe. |
| SA-02 initial | Décider où placer un axe lorsque zéro est hors domaine. | **Retenue avec arbitrage : projection bornée au bord.** | Chaque axe reste un élément `line`; sa position est la projection de zéro limitée à la zone de tracé. |
| SA-01 initial, SA-02 initial | Autoriser ou refuser l'écrasement d'un SVG existant et ne pas inventer de bac à sable de chemins. | **Retenue avec arbitrage : écrasement autorisé.** | `output_path` est honoré comme fourni et l'écriture UTF-8 remplace un fichier existant, comportement standard documenté. Le nom CLI vide est refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Rendre la CLI résiliente ; évaluer les bornes de `plot` avec le moteur ; exiger quatre champs et enregistrer seulement les succès complets. | **Retenue.** | Les erreurs sont affichées sans traceback et la boucle continue. `help`, `history`, `clear`, erreurs et sorties ne sont pas historisés ; un tracé l'est seulement après l'écriture. |
| SA-02 initial | Définir le comportement sur EOF et interruption clavier. | **Retenue : sortie propre.** | EOF et `KeyboardInterrupt` terminent la boucle avec une ligne de séparation, sans traceback. |
| SA-01 initial, SA-02 initial, deux révisions | Documenter syntaxe, radians, erreurs, discontinuités, absence de multiplication implicite, écrasement et limites ; effectuer des contrôles modulaires ciblés. | **Retenue.** | Le README couvrira l'API et la CLI. Cette phase exécutera des tests ciblés du moteur, SVG et CLI, mais pas le vérificateur officiel réservé à la phase suivant SA-03. |


--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Scientific Calculator

Cette solution fournit un moteur d'expressions fermé, un échantillonneur de
courbes, un export SVG autonome et une interface interactive. Elle utilise
uniquement la bibliothèque standard de Python 3.10 ou supérieur.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/scientific_calculator.py
```

La boucle affiche l'invite `>`. Une expression est calculée immédiatement :

```text
> sqrt(2) ^ 2
2.0000000000000004
```

Les commandes disponibles sont `help`, `history`, `clear`, `quit` et `exit`.
Seules les évaluations et écritures de courbes entièrement réussies figurent
dans l'historique de la session.

## Langage accepté

- Littéraux entiers, décimaux et scientifiques : `2`, `.5`, `1.`, `6.02e23`.
- Opérateurs : `+`, `-`, `*`, `/`, `^` et parenthèses.
- Constantes : `pi`, `e`.
- Fonctions à un argument : `sin`, `cos`, `tan`, `asin`, `acos`, `atan`,
  `sqrt`, `ln`, `log10`, `exp`, `abs`.
- Variable `x`, seulement lorsqu'une valeur est fournie par l'API ou pendant
  l'échantillonnage d'une courbe.

Les angles sont en radians. La puissance est associative à droite et plus
prioritaire que les signes : `2^3^2` vaut `512.0`, `-2^2` vaut `-4.0`, et
`2^-2` vaut `0.25`.

Le langage n'accepte pas la multiplication implicite (`2pi`, `2(x)`), les
virgules, chaînes, crochets, attributs, mots-clés Python, opérateur `**` ou
appel d'une fonction non listée. Une fonction exige exactement un argument
entre parenthèses.

## Tracer une courbe

La commande `plot` contient exactement quatre champs séparés par des
points-virgules. Les bornes sont elles-mêmes des expressions sûres :

```text
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

Le fichier UTF-8 obtenu ne dépend d'aucune ressource externe et ne contient
aucun contenu actif. Une valeur hors domaine ou non finie devient une coupure
dans la courbe au lieu de faire échouer tout le tracé. Un fichier existant au
chemin demandé est remplacé ; les répertoires parents ne sont pas créés.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

value = evaluate("sin(pi / 2)")
value_at_two = evaluate("x^2 + 1", {"x": 2.0})
points = sample_curve("1 / x", -1.0, 1.0, samples=201)
write_svg(points, "inverse.svg", title="1 / x")
```

`evaluate` retourne toujours un `float` fini. Une expression vide, mal formée,
un nom inconnu, une valeur non réelle ou hors domaine lève `ValueError`; une
division par zéro lève `ZeroDivisionError`. Le dictionnaire `variables`, s'il
est fourni, ne peut contenir que `x`, associé à un réel fini non booléen.

`sample_curve` exige des bornes finies strictement croissantes et un entier
`samples >= 2`; les deux bornes sont incluses. Les erreurs de syntaxe et de nom
sont levées avant l'échantillonnage. Les erreurs numériques ponctuelles sont
représentées par `None`.

`write_svg` exige au moins un couple de coordonnées finies. Chaque `None` ou
coordonnée non finie coupe le segment. Les titres sont sérialisés comme texte
XML et les caractères interdits par XML 1.0 sont refusés.

## Sécurité et limites

Le lexer consomme toute l'entrée et le parseur n'expose qu'une liste blanche
d'opérations mathématiques. Aucun code, commande système, accès réseau,
attribut ou import issu d'une expression n'est exécuté.

La solution n'impose pas de plafond arbitraire à la longueur d'une expression
ou au nombre d'échantillons. L'appelant doit donc choisir des tailles adaptées
à ses ressources. Une imbrication qui dépasse les capacités récursives de
Python est signalée comme expression trop profonde. Le calcul utilise les
flottants binaires de Python : les arrondis usuels sont visibles et les
résultats infinis sont refusés.

--- END FILE solution/README.md ---

--- BEGIN FILE solution/scientific_calculator.py ---
#!/usr/bin/env python3
"""Calculatrice scientifique sûre et générateur de courbes SVG.

Le langage d'expressions est analysé par un lexer et un parseur dédiés. Il
n'utilise aucun mécanisme d'exécution dynamique de code Python.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numbers
import os
import re
from typing import Callable, Sequence
import xml.etree.ElementTree as ET


_NUMBER_PATTERN = r"(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?"
_NAME_PATTERN = r"[A-Za-z][A-Za-z0-9]*"
_CONSTANTS = {"pi": math.pi, "e": math.e}
_FUNCTIONS: dict[str, Callable[[float], float]] = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "ln": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "abs": abs,
}
_SINGLE_CHAR_TOKENS = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "STAR",
    "/": "SLASH",
    "^": "CARET",
    "(": "LPAREN",
    ")": "RPAREN",
}
_ASCII_WHITESPACE = " \t\r\n\f\v"


@dataclass(frozen=True)
class _Token:
    kind: str
    value: str
    position: int


_Ast = tuple


def _tokenize(expression: str) -> list[_Token]:
    if not isinstance(expression, str):
        raise ValueError("L'expression doit être une chaîne de caractères")
    if not expression.strip(_ASCII_WHITESPACE):
        raise ValueError("L'expression est vide")

    tokens: list[_Token] = []
    position = 0
    while position < len(expression):
        character = expression[position]
        if character in _ASCII_WHITESPACE:
            position += 1
            continue

        remaining = expression[position:]
        number_match = re.match(_NUMBER_PATTERN, remaining, re.ASCII)
        if number_match is not None:
            value = number_match.group(0)
            tokens.append(_Token("NUMBER", value, position))
            position += number_match.end()
            continue

        name_match = re.match(_NAME_PATTERN, remaining, re.ASCII)
        if name_match is not None:
            value = name_match.group(0)
            tokens.append(_Token("NAME", value, position))
            position += name_match.end()
            continue

        kind = _SINGLE_CHAR_TOKENS.get(character)
        if kind is None:
            raise ValueError(
                f"Caractère interdit à la position {position + 1}: {character!r}"
            )
        tokens.append(_Token(kind, character, position))
        position += 1

    tokens.append(_Token("EOF", "", len(expression)))
    return tokens


class _Parser:
    """Parseur descendant récursif du petit langage arithmétique."""

    def __init__(self, tokens: Sequence[_Token]) -> None:
        self._tokens = tokens
        self._index = 0

    @property
    def _current(self) -> _Token:
        return self._tokens[self._index]

    def _accept(self, kind: str) -> _Token | None:
        if self._current.kind != kind:
            return None
        token = self._current
        self._index += 1
        return token

    def _expect(self, kind: str, message: str) -> _Token:
        token = self._accept(kind)
        if token is None:
            raise ValueError(
                f"{message} à la position {self._current.position + 1}"
            )
        return token

    def parse(self) -> _Ast:
        node = self._sum()
        if self._current.kind != "EOF":
            raise ValueError(
                f"Élément inattendu à la position {self._current.position + 1}"
            )
        return node

    def _sum(self) -> _Ast:
        node = self._product()
        while self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._product())
        return node

    def _product(self) -> _Ast:
        node = self._unary()
        while self._current.kind in ("STAR", "SLASH"):
            operator = self._current.value
            self._index += 1
            node = ("binary", operator, node, self._unary())
        return node

    def _unary(self) -> _Ast:
        if self._current.kind in ("PLUS", "MINUS"):
            operator = self._current.value
            self._index += 1
            return ("unary", operator, self._unary())
        return self._power()

    def _power(self) -> _Ast:
        node = self._primary()
        if self._accept("CARET") is not None:
            # L'exposant passe par _unary : la puissance reste associative à
            # droite tout en autorisant 2^-2.
            node = ("binary", "^", node, self._unary())
        return node

    def _primary(self) -> _Ast:
        number = self._accept("NUMBER")
        if number is not None:
            try:
                value = float(number.value)
            except (ValueError, OverflowError) as error:
                raise ValueError("Littéral numérique invalide") from error
            if not math.isfinite(value):
                raise ValueError("Le littéral numérique n'est pas fini")
            return ("number", value)

        name_token = self._accept("NAME")
        if name_token is not None:
            name = name_token.value
            if self._accept("LPAREN") is not None:
                if name not in _FUNCTIONS:
                    raise ValueError(f"Fonction inconnue: {name}")
                argument = self._sum()
                self._expect("RPAREN", "Parenthèse fermante attendue")
                return ("call", name, argument)
            if name in _CONSTANTS:
                return ("number", _CONSTANTS[name])
            if name == "x":
                return ("variable", "x")
            if name in _FUNCTIONS:
                raise ValueError(f"La fonction {name} doit être appelée")
            raise ValueError(f"Nom inconnu: {name}")

        if self._accept("LPAREN") is not None:
            node = self._sum()
            self._expect("RPAREN", "Parenthèse fermante attendue")
            return node

        raise ValueError(
            f"Nombre, nom ou parenthèse attendu à la position "
            f"{self._current.position + 1}"
        )


def _parse_expression(expression: str) -> _Ast:
    try:
        return _Parser(_tokenize(expression)).parse()
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée") from error


def _finite_float(value: object, description: str) -> float:
    if isinstance(value, bool) or not isinstance(value, numbers.Real):
        raise ValueError(f"{description} doit être un nombre réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError(f"{description} doit être un nombre réel fini") from error
    if not math.isfinite(result):
        raise ValueError(f"{description} doit être fini")
    return result


def _checked_result(value: object) -> float:
    if isinstance(value, complex):
        raise ValueError("Le résultat sort du domaine réel")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("Résultat numérique invalide") from error
    if not math.isfinite(result):
        raise ValueError("Le résultat n'est pas fini")
    return result


def _evaluate_ast(node: _Ast, variables: dict[str, float]) -> float:
    kind = node[0]
    if kind == "number":
        return node[1]
    if kind == "variable":
        if "x" not in variables:
            raise ValueError("La variable x n'a pas de valeur")
        return variables["x"]
    if kind == "unary":
        value = _evaluate_ast(node[2], variables)
        return _checked_result(value if node[1] == "+" else -value)
    if kind == "call":
        argument = _evaluate_ast(node[2], variables)
        try:
            return _checked_result(_FUNCTIONS[node[1]](argument))
        except (ValueError, OverflowError) as error:
            raise ValueError(f"Argument hors domaine pour {node[1]}") from error

    left = _evaluate_ast(node[2], variables)
    right = _evaluate_ast(node[3], variables)
    operator = node[1]
    try:
        if operator == "+":
            value = left + right
        elif operator == "-":
            value = left - right
        elif operator == "*":
            value = left * right
        elif operator == "/":
            value = left / right
        else:
            value = left**right
    except ZeroDivisionError:
        raise
    except (ValueError, OverflowError) as error:
        raise ValueError("Opération hors du domaine réel") from error
    return _checked_result(value)


def _validated_variables(
    variables: dict[str, float] | None,
) -> dict[str, float]:
    if variables is None:
        return {}
    if not isinstance(variables, dict):
        raise ValueError("variables doit être un dictionnaire")
    extra_names = set(variables) - {"x"}
    if extra_names:
        raise ValueError("Seule la variable x est autorisée")
    if "x" not in variables:
        return {}
    return {"x": _finite_float(variables["x"], "La variable x")}


def evaluate(
    expression: str,
    variables: dict[str, float] | None = None,
) -> float:
    """Évalue *expression* dans le langage sûr et retourne un float fini.

    ``ValueError`` signale une syntaxe, un nom, un domaine réel ou une valeur
    non finie invalide. Une division par zéro conserve ``ZeroDivisionError``.
    """

    parsed = _parse_expression(expression)
    validated_variables = _validated_variables(variables)
    try:
        return _checked_result(_evaluate_ast(parsed, validated_variables))
    except RecursionError as error:
        raise ValueError("Expression trop profondément imbriquée") from error


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Échantillonne une expression et marque les valeurs indéfinies par None."""

    minimum = _finite_float(x_min, "x_min")
    maximum = _finite_float(x_max, "x_max")
    if minimum >= maximum:
        raise ValueError("x_min doit être strictement inférieur à x_max")
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError("samples doit être un entier au moins égal à 2")

    # Le parsing préalable fait remonter les erreurs structurelles une seule
    # fois. Seules les erreurs numériques propres à un point deviennent None.
    parsed = _parse_expression(expression)
    points: list[tuple[float, float | None]] = []
    denominator = samples - 1
    for index in range(samples):
        if index == 0:
            x_value = minimum
        elif index == denominator:
            x_value = maximum
        else:
            ratio = index / denominator
            x_value = (1.0 - ratio) * minimum + ratio * maximum
        try:
            y_value = _checked_result(_evaluate_ast(parsed, {"x": x_value}))
        except (ValueError, ZeroDivisionError, OverflowError, RecursionError):
            y_value = None
        points.append((x_value, y_value))
    return points


def _is_valid_xml_text(text: str) -> bool:
    for character in text:
        codepoint = ord(character)
        if not (
            codepoint in (0x09, 0x0A, 0x0D)
            or 0x20 <= codepoint <= 0xD7FF
            or 0xE000 <= codepoint <= 0xFFFD
            or 0x10000 <= codepoint <= 0x10FFFF
        ):
            return False
    return True


def _svg_number(value: float) -> str:
    if not math.isfinite(value):
        raise ValueError("Coordonnée SVG non finie")
    return format(value, ".12g")


def _expanded_bounds(value: float) -> tuple[float, float]:
    """Crée une étendue finie autour d'une coordonnée unique."""

    expansion = max(1.0, abs(value) * 0.05)
    low = value - expansion
    high = value + expansion
    if not math.isfinite(low):
        low = value
    if not math.isfinite(high):
        high = value
    if low == high:
        low = math.nextafter(value, -math.inf)
        high = math.nextafter(value, math.inf)
        if not math.isfinite(low):
            low = value
        if not math.isfinite(high):
            high = value
    if low == high:
        raise ValueError("Étendue graphique impossible à représenter")
    return low, high


def _relative_position(value: float, low: float, high: float) -> float:
    """Calcule une position relative sans faire déborder high - low."""

    scale = max(abs(low), abs(high), 1.0)
    low_scaled = low / scale
    high_scaled = high / scale
    value_scaled = value / scale
    return (value_scaled - low_scaled) / (high_scaled - low_scaled)


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = "",
) -> None:
    """Écrit une représentation SVG autonome des points fournis.

    Les valeurs ``None`` ou non finies séparent les segments. Un fichier
    existant à *output_path* est remplacé.
    """

    if not isinstance(title, str) or not _is_valid_xml_text(title):
        raise ValueError("Le titre contient des caractères XML invalides")
    try:
        path = os.fspath(output_path)
    except TypeError as error:
        raise ValueError("Chemin de sortie invalide") from error
    if not isinstance(path, (str, bytes)) or not path:
        raise ValueError("Le chemin de sortie est vide")
    if not isinstance(points, list):
        raise ValueError("points doit être une liste")

    normalized: list[tuple[float, float] | None] = []
    finite_points: list[tuple[float, float]] = []
    for point in points:
        if not isinstance(point, (tuple, list)) or len(point) != 2:
            raise ValueError("Chaque point doit contenir exactement x et y")
        x_raw, y_raw = point
        if y_raw is None:
            normalized.append(None)
            continue
        if (
            isinstance(x_raw, bool)
            or isinstance(y_raw, bool)
            or not isinstance(x_raw, numbers.Real)
            or not isinstance(y_raw, numbers.Real)
        ):
            raise ValueError("Les coordonnées doivent être des nombres réels")
        try:
            x_value = float(x_raw)
            y_value = float(y_raw)
        except (TypeError, ValueError, OverflowError) as error:
            raise ValueError("Coordonnée invalide") from error
        if not math.isfinite(x_value) or not math.isfinite(y_value):
            normalized.append(None)
            continue
        finite_point = (x_value, y_value)
        normalized.append(finite_point)
        finite_points.append(finite_point)

    if not finite_points:
        raise ValueError("Aucun point fini ne peut être tracé")

    x_values = [point[0] for point in finite_points]
    y_values = [point[1] for point in finite_points]
    x_low, x_high = min(x_values), max(x_values)
    y_low, y_high = min(y_values), max(y_values)
    if x_low == x_high:
        x_low, x_high = _expanded_bounds(x_low)
    if y_low == y_high:
        y_low, y_high = _expanded_bounds(y_low)

    width, height, margin = 800.0, 500.0, 55.0
    plot_width = width - 2.0 * margin
    plot_height = height - 2.0 * margin

    def project_x(value: float) -> float:
        return margin + _relative_position(value, x_low, x_high) * plot_width

    def project_y(value: float) -> float:
        return height - margin - _relative_position(value, y_low, y_high) * plot_height

    axis_x = min(max(project_x(0.0), margin), width - margin)
    axis_y = min(max(project_y(0.0), margin), height - margin)

    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)
    root = ET.Element(
        f"{{{namespace}}}svg",
        {
            "viewBox": "0 0 800 500",
            "width": "800",
            "height": "500",
            "role": "img",
        },
    )
    if title:
        title_element = ET.SubElement(root, f"{{{namespace}}}title")
        title_element.text = title
    ET.SubElement(
        root,
        f"{{{namespace}}}rect",
        {"width": "800", "height": "500", "fill": "#ffffff"},
    )
    axis_style = {"stroke": "#666666", "stroke-width": "1"}
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(margin),
            "y1": _svg_number(axis_y),
            "x2": _svg_number(width - margin),
            "y2": _svg_number(axis_y),
            **axis_style,
        },
    )
    ET.SubElement(
        root,
        f"{{{namespace}}}line",
        {
            "x1": _svg_number(axis_x),
            "y1": _svg_number(margin),
            "x2": _svg_number(axis_x),
            "y2": _svg_number(height - margin),
            **axis_style,
        },
    )

    def append_segment(segment: list[tuple[float, float]]) -> None:
        projected = [
            (project_x(x_value), project_y(y_value))
            for x_value, y_value in segment
        ]
        if len(projected) == 1:
            x_screen, y_screen = projected[0]
            ET.SubElement(
                root,
                f"{{{namespace}}}circle",
                {
                    "cx": _svg_number(x_screen),
                    "cy": _svg_number(y_screen),
                    "r": "2.5",
                    "fill": "#1769aa",
                },
            )
            return
        coordinates = " ".join(
            f"{_svg_number(x_screen)},{_svg_number(y_screen)}"
            for x_screen, y_screen in projected
        )
        ET.SubElement(
            root,
            f"{{{namespace}}}polyline",
            {
                "points": coordinates,
                "fill": "none",
                "stroke": "#1769aa",
                "stroke-width": "2",
                "stroke-linejoin": "round",
                "stroke-linecap": "round",
            },
        )

    current_segment: list[tuple[float, float]] = []
    for point in normalized:
        if point is None:
            if current_segment:
                append_segment(current_segment)
                current_segment = []
        else:
            current_segment.append(point)
    if current_segment:
        append_segment(current_segment)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(path, encoding="utf-8", xml_declaration=True)


_HELP = """Commandes :
  <expression>                         évaluer une expression
  plot <expression>; <min>; <max>; <fichier.svg>
                                       tracer une courbe
  history                              afficher l'historique réussi
  clear                                vider l'historique
  help                                 afficher cette aide
  quit | exit                          quitter

Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs
Constantes : pi e    Variable de tracé : x    Angles : radians"""


def _handle_line(line: str, history: list[str]) -> bool:
    """Traite une ligne de CLI. Retourne False lorsqu'il faut quitter."""

    command = line.strip()
    if command in ("quit", "exit"):
        return False
    if command == "help":
        print(_HELP)
        return True
    if command == "history":
        if not history:
            print("Historique vide.")
        else:
            for index, entry in enumerate(history, start=1):
                print(f"{index}: {entry}")
        return True
    if command == "clear":
        history.clear()
        print("Historique effacé.")
        return True

    if command == "plot" or command.startswith("plot "):
        fields = command[4:].strip().split(";")
        if len(fields) != 4 or any(not field.strip() for field in fields):
            raise ValueError(
                "Syntaxe: plot <expression>; <min>; <max>; <fichier.svg>"
            )
        expression, minimum_text, maximum_text, output_path = (
            field.strip() for field in fields
        )
        minimum = evaluate(minimum_text)
        maximum = evaluate(maximum_text)
        curve = sample_curve(expression, minimum, maximum)
        write_svg(curve, output_path, expression)
        history.append(command)
        print(f"Courbe enregistrée dans {output_path}")
        return True

    result = evaluate(command)
    history.append(command)
    # Quinze chiffres significatifs masquent les artefacts d'arrondi les plus
    # triviaux dans l'interface (sqrt(2)^2 s'affiche 2.0) sans modifier l'API.
    print(float(format(result, ".15g")))
    return True


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""

    history: list[str] = []
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        try:
            if not _handle_line(line, history):
                break
        except (ValueError, ZeroDivisionError, OSError) as error:
            print(f"Erreur: {error}")


if __name__ == "__main__":
    main()

--- END FILE solution/scientific_calculator.py ---

--- END FIRST SOLUTION SNAPSHOT ---

--- BEGIN SA-03 CRITIQUE ---
## Défauts confirmés

- **Interruption clavier incomplètement gérée.** `KeyboardInterrupt` n’est intercepté qu’autour de `input()`. Un Ctrl-C pendant l’évaluation, l’échantillonnage, l’écriture SVG ou l’affichage produit donc potentiellement un traceback. Cela contredit la décision « EOF et `KeyboardInterrupt` terminent la boucle […] sans traceback » et fragilise l’exigence de résilience de la CLI.

- **La CLI peut afficher un résultat numériquement différent de celui calculé.** `print(float(format(result, ".15g")))` arrondit à quinze chiffres significatifs puis reconvertit. Par exemple, `1 + 1e-15` peut être affiché comme `1.0`, alors que `evaluate` renvoie approximativement `1.000000000000001`. Il ne s’agit pas seulement d’une présentation plus courte : une variation représentable disparaît.

- **Classification incorrecte d’une limite globale dans `sample_curve`.** Un long enchaînement associatif à gauche, tel qu’une somme de milliers de termes, est parsé itérativement mais produit un AST profond. Sa récursion d’évaluation peut lever `RecursionError`; `sample_curve` transforme alors cette erreur en `None` à chaque point. Une limite structurelle globale est donc présentée comme une discontinuité numérique locale, contrairement à la table de décisions (« seulement les erreurs numériques dépendant de `x` »).

- **Exemple README faux pour la CLI livrée.** La section « Lancement » montre `sqrt(2) ^ 2` donnant `2.0000000000000004`, alors que le formatage de `_handle_line` affiche `2.0`. L’API et la CLI ont effectivement des rendus différents, mais l’exemple est explicitement présenté comme une session interactive.

## Risques

- **Déni de service assumé mais réel.** L’absence de plafonds autorise des expressions, titres, listes de points ou nombres d’échantillons démesurés. `sample_curve` alloue toute la liste et évalue chaque point; une valeur massive peut bloquer durablement ou épuiser la mémoire. L’absence de limite n’est pas une violation explicite du contrat, mais elle affaiblit la promesse d’évaluation « sûre ».

- **Distinction global/local encore imparfaite.** Le parsing préalable détecte syntaxe et noms inconnus, mais une erreur numérique indépendante de `x`, par exemple `sqrt(-1)`, devient une liste entière de `None`. Le challenge permet raisonnablement cette lecture, mais le discours des décisions suggère une séparation plus sémantique que celle réellement obtenue.

- **Politique stricte de `variables` potentiellement incompatible.** Rejeter toute clé autre que `x` est documenté et sûr, mais non imposé par le contrat. Un vérificateur ou appelant peut raisonnablement fournir un contexte plus large en attendant que les clés inaccessibles soient simplement ignorées. Les consultations avaient précisément identifié cette divergence possible.

- **Écrasement de fichiers arbitraires.** La CLI honore chemins absolus, traversées et liens symboliques, puis remplace la cible directement. Cette politique est explicitement arbitrée et le contrat ne prescrit aucun bac à sable; elle reste néanmoins une surface dangereuse, surtout si la CLI est intégrée à un service ou lancée avec des privilèges élevés.

- **Écriture non transactionnelle.** `ElementTree.write` écrit directement dans la cible existante. Une erreur d’E/S en cours d’écriture peut laisser un fichier antérieur tronqué ou un SVG partiel, bien que le tracé ne soit ensuite pas ajouté à l’historique.

- **Injection de contrôle dans le terminal.** Le chemin de sortie est réaffiché brut et conservé dans l’historique. Un nom contenant des séquences de contrôle ou ANSI peut altérer l’affichage du terminal. Cela ne compromet pas le SVG, mais constitue une surface d’injection de présentation.

- **Taxonomie ambiguë pour les puissances de zéro négatives.** Python lève `ZeroDivisionError` pour certaines formes telles que `0^-1`. Le contrat réserve explicitement cette exception à « une division par zéro », sans préciser si une puissance équivalant à une réciproque doit suivre la même classification. Un test strict pourrait attendre `ValueError` comme opération hors domaine.

## Préférences, non défauts

- Exiger exactement une `list` dans `write_svg`, plutôt qu’un itérable, suit la signature publique et reste défendable.
- Transformer une coordonnée non finie en coupure est cohérent avec l’objectif, même si le contrat ne fixe pas précisément la validation des points fournis directement.
- Les axes projetés au bord, les singletons rendus par `circle` et l’écrasement autorisé sont des choix de rendu ou d’I/O documentés, pas des erreurs contractuelles.
- Le rejet des espaces Unicode, des booléens et de la multiplication implicite constitue un durcissement cohérent avec la grammaire fermée.
--- END SA-03 CRITIQUE ---
````

</details>

#### Texte retourné pour MSG-007, mot pour mot

````text
Je reprends strictement le rôle MAIN, sans nouveau consultant. Je vais d’abord confronter les 16 points de SA‑03 à l’état réel des trois fichiers, compléter l’arbitrage, appliquer seulement les points retenus, puis lancer une première fois le vérificateur officiel avec la commande exacte.

L’arbitrage retient les quatre défauts confirmés. Deux risques justifient aussi une correction ciblée : neutraliser les caractères de contrôle lors du réaffichage du chemin et réserver `ZeroDivisionError` à l’opérateur `/` (donc `0^-1` devient `ValueError`). Les plafonds arbitraires, le bac à sable de chemins et l’écriture transactionnelle restent écartés car ils ne sont pas imposés par le contrat et changeraient l’API ou la sémantique d’E/S.

Les corrections retenues sont maintenant appliquées et les 15 puces de SA‑03 sont qualifiées dans `DECISIONS.md`. Je lance à présent le premier passage officiel, sans prétest intermédiaire, depuis la racine du dépôt et avec la commande prescrite mot pour mot.

Premier passage : 9 tests exécutés, 3 réussis et 6 en erreur. Tous les échecs ont une cause unique, confirmée par les six traces : le chargeur indépendant n’insère pas le module dans `sys.modules`, ce qui fait échouer le décorateur `dataclass` sous Python 3.13 avant même les tests fonctionnels. Je remplace ce simple conteneur de jeton par une classe standard équivalente, sans toucher au vérificateur, puis je relance exactement la même commande.

Le second passage est entièrement vert : 9/9 tests, verdict `OK`, code retour 0. Je consigne maintenant dans `DECISIONS.md` le premier passage, sa cause unique, la correction issue du vérificateur et le verdict final ; aucune autre correction n’est nécessaire.

## Résultat

Solution finalisée et conforme. Le vérificateur officiel conclut :

```text
Ran 9 tests in 0.057s
OK
```

Code retour : `0`.

## Rôles et échanges

Ordre conservé : SA‑01 initial → SA‑02 initial → réponses croisées SA‑01/SA‑02 → première solution MAIN → critique SA‑03 → arbitrage final MAIN.

- Orchestrateur expérimental : fourniture des textes autorisés.
- MAIN : orchestrateur candidat, décideur et unique écrivain.
- SA‑01 : contrat et sécurité.
- SA‑02 : conception et testabilité.
- SA‑03 : critique finale des cas limites.
- Aucun nouveau consultant ou sous-agent pendant cette phase.

## Arbitrages SA‑03

Les 15 points sont qualifiés dans [DECISIONS.md](<repo>/runs/sol-scientific-v2-001/solution/DECISIONS.md:28) :

- 10 retenus, dont les comportements déjà conformes maintenus.
- 5 écartés.
- Aucun point non vérifiable.

Corrections retenues :

- interception de `KeyboardInterrupt` pendant toute opération CLI ;
- affichage fidèle du `float`, sans arrondi destructeur ;
- évaluation itérative des AST profonds ;
- cohérence de l’exemple README ;
- neutralisation des contrôles lors du réaffichage terminal ;
- `ZeroDivisionError` réservé à `/`, tandis que `0^-1` lève `ValueError`.

## Premier passage et correction

Premier passage officiel : 9 tests, 3 succès, 6 erreurs. Toutes provenaient du même défaut d’import sous Python 3.13 : le décorateur `dataclass` dépendait d’une inscription du module dans `sys.modules` que le chargeur indépendant n’effectuait pas.

Le jeton lexical a été remplacé par une classe simple à `__slots__` dans [scientific_calculator.py](<repo>/runs/sol-scientific-v2-001/solution/scientific_calculator.py:46).

Passage final, avec la même commande exacte :

```bash
python3 scripts/verify.py --challenge scientific-calculator --solution runs/sol-scientific-v2-001/solution
```

Résultat : 9/9 tests réussis.

## Limites assumées

Aucun plafond arbitraire de taille ou d’échantillonnage ; chemins de sortie arbitraires et écrasement autorisés ; écriture non transactionnelle ; clés de variables autres que `x` rejetées. Ces choix sont documentés dans [README.md](<repo>/runs/sol-scientific-v2-001/solution/README.md:1).

TODO : aucun. Aucune opération Git effectuée.
````

## Lecture sociale synthétique

SA-01 et SA-02 commencent sans voir l'avis de l'autre. Leurs réponses
croisées rendent ensuite visibles accords, désaccords et doublons. MAIN
arbitre avant d'écrire. SA-03 critique l'instantané obtenu ; MAIN qualifie
alors chaque point avant le vérificateur. Le rapport de résultat chiffre
les recommandations retenues, écartées et non vérifiables.

Les prompts dynamiques répètent volontairement le challenge et les textes
antérieurs : cette duplication fait partie du coût de coordination mesuré.
