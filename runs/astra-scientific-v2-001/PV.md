# PV — Scientific Astra V2 interrompue

Quota atteint au démarrage de MAIN (écrivain principal). Aucune solution, aucun verdict.
SA-01 : exigences et sécurité ; SA-02 : architecture et testabilité ;
SA-03 : relecteur qualité, non sollicité.
Les compteurs de MAIN et le temps mural total ne sont pas enregistrés.

Tokens partiels observés : **69713**.

## Textes visibles

### MSG-001 — 01-sa01-initial

<details>
<summary>Mandat envoyé</summary>

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

````text
Avis SA-01 — analyse indépendante des exigences et de la sécurité, fondée exclusivement sur le challenge fourni. Aucun outil, dépôt, fichier ou test consulté ; aucune délégation. Le verdict technique reste à la charge du vérificateur indépendant.

**1. Obligations non négociables**

La livraison comprend `scientific_calculator.py` et `README.md`, exclusivement dans `solution/`. Elle doit fonctionner avec la bibliothèque standard sous Python 3.10 ou supérieur, sans réseau ni exécution dynamique (`eval`, `exec`, `compile`).

Les trois fonctions publiques doivent respecter leurs signatures et contrats. Points particulièrement discriminants :

- `evaluate` retourne toujours un flottant fini en cas de réussite ; les résultats complexes, infinis ou indéfinis sont des erreurs.
- La puissance est associative à droite et prioritaire sur les signes unaires.
- Les noms, appels et caractères autorisés forment une liste fermée.
- `sample_curve` inclut exactement les bornes et conserve les points invalides sous forme de couples `(x, None)`.
- Le SVG contient un fond, deux axes constitués d’éléments `line`, une courbe interrompue aux points invalides et aucun contenu actif.
- La CLI reste utilisable après une erreur et n’enregistre que les expressions et tracés réussis.
- Le README explique lancement, syntaxe, fonctions, exemples et limites.

**Arbitrage :** traiter ces éléments comme des critères d’acceptation, sans les assouplir au nom d’une commodité d’implémentation.

**2. Grammaire : préciser les choix sans élargir le langage**

Plusieurs frontières ne sont pas explicites : nombres `.5` ou `5.`, casse des fonctions, chiffres Unicode, multiplication implicite, appel sans parenthèses et alias `**`.

**Recommandation :** accepter les formes décimales usuelles `.5` et `5.`, les exposants scientifiques signés, et les espaces entre jetons ; conserver les noms canoniques et les appels avec parenthèses. Refuser les extensions non prévues telles que `2pi`, `sin x` et `**`. La totalité de l’entrée doit être consommée : accepter un préfixe valide suivi de caractères interdits serait une faille de validation.

Les fonctions listées sont unaires : les appels sans argument ou avec plusieurs arguments doivent échouer. La grammaire doit permettre `2^-2` et interpréter `-2^-2` comme `-(2^(-2))`, conformément aux priorités annoncées.

Le dictionnaire `variables` pourrait laisser croire que tout identifiant est injectable.

**Arbitrage recommandé :** seule `x` peut être résolue comme variable ; les clés supplémentaires ne doivent ni autoriser d’autres noms ni remplacer `pi`, `e` ou les fonctions. Leur rejet explicite ou leur ignorance reste à documenter.

**3. Erreurs numériques : stabiliser les exceptions**

L’obligation de résultat fini implique que dépassements numériques et résultats non finis deviennent des `ValueError`, plutôt que de laisser remonter une exception interne telle qu’`OverflowError`. Une division explicite par zéro doit conserver `ZeroDivisionError`.

Deux cas demandent une décision documentée :

- `0^-1` : recommander `ValueError`, comme puissance hors domaine, puisque l’obligation spécifique de `ZeroDivisionError` vise la division.
- `0^0` : le challenge ne tranche pas ; la convention numérique `1.0` est défendable, mais ne doit pas être présentée comme une exigence explicite.

Pour les puissances négatives à exposant fractionnaire, le comportement réel mérite également une limite claire : une approximation flottante de `1/3` ne fournit pas automatiquement une information rationnelle exacte.

**Arbitrage :** documenter la convention numérique retenue, sans promettre de calcul symbolique. De même, `tan(pi/2)` peut produire un grand flottant fini : imposer une détection mathématique exacte des pôles dépasserait les précisions du contrat.

**4. Échantillonnage : distinguer expression invalide et point invalide**

Le contrat protège le tracé contre un point isolé hors domaine ; il ne dit pas clairement comment traiter une syntaxe globalement invalide.

**Recommandation :** faire échouer une expression mal formée ou inconnue, puis convertir en `None` les erreurs numériques dépendant du point. Une capture indifférenciée des exceptions masquerait aussi des défauts internes.

Exiger des bornes finies et un nombre entier d’échantillons au moins égal à deux. Le seul contrôle `x_min < x_max` ne suffit pas à exclure toutes les entrées problématiques. Les intervalles très larges peuvent également provoquer des dépassements dans les calculs intermédiaires.

Une singularité située entre deux échantillons peut rester invisible.

**Arbitrage :** garantir les coupures aux échantillons invalides. Présenter la détection supplémentaire des asymptotes comme facultative ; un seuil arbitraire risquerait de couper une fonction continue très pentue.

**5. SVG : sécurité et géométrie**

Les surfaces d’attaque principales sont le titre et toute autre chaîne utilisateur insérée dans le XML. L’échappement doit correspondre au contexte, y compris les guillemets dans les attributs. Certains caractères de contrôle restent invalides en XML même après échappement classique.

**Recommandation :** limiter les interpolations utilisateur à du texte correctement traité ; exclure scripts, gestionnaires d’événements, références externes et balisage utilisateur.

Cas géométriques à arbitrer explicitement :

- ordonnées constantes ou abscisses identiques : prévoir une échelle non dégénérée ;
- coordonnées non finies : les exclure du calcul des limites et du dessin ;
- segment réduit à un point : assurer sa visibilité si ce point est le seul tracé possible ;
- origine hors du domaine affiché : choisir une convention pour les axes et la documenter.

Un `None` doit réellement interrompre la courbe : filtrer les points invalides puis relier tous les autres violerait cette exigence.

**6. CLI et robustesse**

Les bornes de `plot` doivent accepter des expressions constantes, puisque l’exemple utilise `-pi` et `pi`. Le comportement des chemins contenant un point-virgule reste indéterminé ; une limitation documentée est acceptable.

L’écriture peut échouer pour des raisons de permissions, de chemin ou de stockage. Le message de réussite et l’entrée d’historique doivent intervenir après l’écriture réussie. La fin d’entrée et l’interruption utilisateur méritent une sortie propre.

La profondeur des expressions, leur longueur et le nombre d’échantillons constituent des surfaces d’épuisement des ressources.

**Arbitrage recommandé :** envisager des limites explicites et compréhensibles, en reconnaissant qu’aucun seuil n’est fixé par le challenge.

**7. Contrôles et points ouverts**

Prioriser les contrôles sur la précédence, le rejet intégral des entrées interdites, les exceptions numériques, les coupures, l’échappement XML et la récupération de la CLI. La vérification prescrite reste à exécuter par le candidat ; aucun résultat n’est établi ici.

Les ambiguïtés ci-dessus appellent des décisions consignées, sans modification rétroactive du challenge ou de sa suite figée. Aucun travail sur fichiers ni aucune opération Git réalisés.
````

### MSG-002 — 02-sa02-initial

<details>
<summary>Mandat envoyé</summary>

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

````text
Avis SA-02 — privilégier une architecture à responsabilités séparées, avec des règles explicites pour les erreurs et les ruptures de courbe. Les risques principaux concernent la priorité des signes, la distinction entre syntaxe invalide et point hors domaine, ainsi que la robustesse de l’échelle SVG.

### 1. Structure recommandée

Conserver le livrable unique `scientific_calculator.py`, mais distinguer en interne :

- l’analyse lexicale et syntaxique ;
- l’évaluation numérique ;
- l’échantillonnage ;
- la transformation des coordonnées et la production SVG ;
- la boucle CLI et son historique.

Les trois fonctions publiques doivent fonctionner indépendamment de la CLI. Importer le module ne doit déclencher ni invite interactive ni écriture.

**Arbitrage recommandé :** un analyseur dédié, simple et fondé sur une liste fermée de constructions autorisées. Une architecture extensible par greffons ou un langage intermédiaire général ajouterait une complexité inutile. Une représentation interne réutilisable de l’expression permet néanmoins de l’analyser une seule fois pour tout un échantillonnage.

### 2. Invariants du moteur d’expressions

**Reconnaissance complète.** Toute l’expression doit être consommée. Une partie valide suivie de caractères interdits doit échouer. Les nombres scientifiques doivent être reconnus sans confondre leur exposant avec un opérateur ou la constante `e`.

**Priorités.** L’associativité à droite de la puissance et sa priorité sur les signes doivent être conçues ensemble. Les exemples imposés ne suffisent pas à éliminer toutes les erreurs : `2^-2`, `(-2)^2` et `-2^-2` sont également discriminants.

**Noms autorisés.** Séparer constantes, fonctions et variable. La présence d’une clé dans `variables` ne doit pas étendre implicitement le langage à des noms arbitraires. Définir clairement le traitement de `x` absent, des clés supplémentaires et des tentatives de redéfinition de `pi` ou `e`.

**Résultats et exceptions.**

- Tout succès de `evaluate` produit un `float` fini.
- Toute syntaxe invalide, tout nom interdit ou tout résultat hors du domaine réel produit `ValueError`.
- Une division explicite par zéro conserve `ZeroDivisionError`.
- Un dépassement numérique doit être normalisé en erreur conforme au contrat ; aucun résultat complexe, `NaN` ou infini ne doit sortir.

**Arbitrage recommandé :** traiter les opérateurs selon leur sémantique réelle, puis vérifier la finitude. Éviter une capture globale qui transformerait une erreur de programmation en erreur utilisateur. Le cas `0^-1` mérite une décision documentée : le contrat distingue division par zéro et puissance hors domaine sans préciser explicitement leur frontière.

### 3. Échantillonnage : préserver les ruptures sans cacher les erreurs

L’échantillonnage devrait garantir :

- exactement le nombre demandé de points, avec des abscisses ordonnées ;
- les deux bornes incluses explicitement ;
- une ordonnée finie ou `None` pour chaque abscisse ;
- aucune interruption provoquée par un point isolé hors domaine.

Valider les paramètres avant le calcul : bornes finies, intervalle strictement croissant, nombre entier d’échantillons au moins égal à deux. Les bornes très grandes peuvent provoquer un dépassement dans des calculs intermédiaires malgré des entrées finies.

**Arbitrage recommandé :** rejeter une expression syntaxiquement invalide avant de parcourir les points ; convertir ensuite les seules erreurs numériques attendues en `None`. Le contrat ne précise pas complètement le comportement de `sample_curve` sur une expression mal formée : cette distinction est utile, mais doit rester identifiée comme un choix d’interprétation.

Une discontinuité située entre deux échantillons peut rester invisible. Ainsi, `1/x` ne produit une coupure certaine que si un point atteint zéro, sauf mécanisme supplémentaire.

**Arbitrage recommandé :** assurer les coupures aux valeurs effectivement invalides et documenter la limite de l’échantillonnage. Une heuristique de grands écarts pourrait couper à tort une fonction continue ; elle ne devrait pas devenir une exigence implicite.

### 4. SVG : géométrie robuste et contenu inerte

Le producteur SVG doit être testable avec des points construits directement, indépendamment du moteur.

Invariants essentiels :

- l’échelle dépend uniquement des couples de coordonnées finis ;
- aucune coordonnée sérialisée ne contient `NaN` ou une infinité ;
- aucun segment ne traverse un point invalide ;
- une courbe constante ou un unique point fini ne provoque aucune division par zéro ;
- fond et deux éléments `line` pour les axes sont présents ;
- tout texte utilisateur est échappé dans son contexte XML.

**Arbitrages à expliciter :**

- Prévoir une marge lorsque l’étendue horizontale ou verticale est nulle.
- Pour une série ne contenant qu’un point fini, préférer un marqueur visible.
- Si zéro est hors des données, préciser comment concilier adaptation de l’échelle et visibilité des deux axes : inclusion de zéro ou représentation aux bords. Le texte ne tranche pas cette présentation.
- Traiter les points fournis directement avec des coordonnées non finies comme invalides et comme ruptures.

Limiter le document aux éléments SVG nécessaires facilite la vérification de son innocuité.

### 5. CLI et historique

Faire dépendre l’ajout à l’historique de la réussite complète : résultat obtenu pour une expression, fichier effectivement écrit pour un tracé. Un échec d’écriture ne doit pas être enregistré comme succès.

Les bornes de `plot` doivent bénéficier du même moteur, notamment pour `-pi` et `pi`. Vérifier le nombre de champs séparés par des points-virgules et les champs vides.

**Arbitrage recommandé :** intercepter les erreurs attendues à la frontière CLI, avec un message contextualisé et une nouvelle invite. Prévoir également une sortie propre à la fin de l’entrée standard. Les commandes de gestion ne devraient pas polluer l’historique des expressions et tracés réussis.

### 6. Validation prioritaire

Organiser les contrôles par contrat observable :

1. **Moteur :** précédence, exposants signés, notation scientifique, arité des fonctions, consommation complète, noms interdits, exceptions et finitude.
2. **Échantillonnage :** bornes exactes, nombre de points, intervalle invalide, `sqrt(x)` sur un intervalle mixte, `1/x` avec zéro échantillonné.
3. **SVG :** analyse XML, éléments attendus, titre contenant `<`, `&` et guillemets, ruptures effectives, courbe constante, absence totale de points finis.
4. **CLI :** session comportant succès, erreur, nouveau succès, historique, effacement et sortie ; ajouter un chemin de sortie inaccessible.
5. **Livraison :** absence d’exécution dynamique interdite, documentation des conventions et lancement de la commande d’acceptation fournie.

Ces contrôles doivent mesurer les comportements, sans imposer une organisation interne particulière. Aucun outil ni dépôt n’a été consulté et aucun test n’a été exécuté ; le verdict technique reste celui du vérificateur indépendant.
````

### MSG-003 — 03-sa01-cross

<details>
<summary>Mandat envoyé</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-01 ---
Avis SA-01 — analyse indépendante des exigences et de la sécurité, fondée exclusivement sur le challenge fourni. Aucun outil, dépôt, fichier ou test consulté ; aucune délégation. Le verdict technique reste à la charge du vérificateur indépendant.

**1. Obligations non négociables**

La livraison comprend `scientific_calculator.py` et `README.md`, exclusivement dans `solution/`. Elle doit fonctionner avec la bibliothèque standard sous Python 3.10 ou supérieur, sans réseau ni exécution dynamique (`eval`, `exec`, `compile`).

Les trois fonctions publiques doivent respecter leurs signatures et contrats. Points particulièrement discriminants :

- `evaluate` retourne toujours un flottant fini en cas de réussite ; les résultats complexes, infinis ou indéfinis sont des erreurs.
- La puissance est associative à droite et prioritaire sur les signes unaires.
- Les noms, appels et caractères autorisés forment une liste fermée.
- `sample_curve` inclut exactement les bornes et conserve les points invalides sous forme de couples `(x, None)`.
- Le SVG contient un fond, deux axes constitués d’éléments `line`, une courbe interrompue aux points invalides et aucun contenu actif.
- La CLI reste utilisable après une erreur et n’enregistre que les expressions et tracés réussis.
- Le README explique lancement, syntaxe, fonctions, exemples et limites.

**Arbitrage :** traiter ces éléments comme des critères d’acceptation, sans les assouplir au nom d’une commodité d’implémentation.

**2. Grammaire : préciser les choix sans élargir le langage**

Plusieurs frontières ne sont pas explicites : nombres `.5` ou `5.`, casse des fonctions, chiffres Unicode, multiplication implicite, appel sans parenthèses et alias `**`.

**Recommandation :** accepter les formes décimales usuelles `.5` et `5.`, les exposants scientifiques signés, et les espaces entre jetons ; conserver les noms canoniques et les appels avec parenthèses. Refuser les extensions non prévues telles que `2pi`, `sin x` et `**`. La totalité de l’entrée doit être consommée : accepter un préfixe valide suivi de caractères interdits serait une faille de validation.

Les fonctions listées sont unaires : les appels sans argument ou avec plusieurs arguments doivent échouer. La grammaire doit permettre `2^-2` et interpréter `-2^-2` comme `-(2^(-2))`, conformément aux priorités annoncées.

Le dictionnaire `variables` pourrait laisser croire que tout identifiant est injectable.

**Arbitrage recommandé :** seule `x` peut être résolue comme variable ; les clés supplémentaires ne doivent ni autoriser d’autres noms ni remplacer `pi`, `e` ou les fonctions. Leur rejet explicite ou leur ignorance reste à documenter.

**3. Erreurs numériques : stabiliser les exceptions**

L’obligation de résultat fini implique que dépassements numériques et résultats non finis deviennent des `ValueError`, plutôt que de laisser remonter une exception interne telle qu’`OverflowError`. Une division explicite par zéro doit conserver `ZeroDivisionError`.

Deux cas demandent une décision documentée :

- `0^-1` : recommander `ValueError`, comme puissance hors domaine, puisque l’obligation spécifique de `ZeroDivisionError` vise la division.
- `0^0` : le challenge ne tranche pas ; la convention numérique `1.0` est défendable, mais ne doit pas être présentée comme une exigence explicite.

Pour les puissances négatives à exposant fractionnaire, le comportement réel mérite également une limite claire : une approximation flottante de `1/3` ne fournit pas automatiquement une information rationnelle exacte.

**Arbitrage :** documenter la convention numérique retenue, sans promettre de calcul symbolique. De même, `tan(pi/2)` peut produire un grand flottant fini : imposer une détection mathématique exacte des pôles dépasserait les précisions du contrat.

**4. Échantillonnage : distinguer expression invalide et point invalide**

Le contrat protège le tracé contre un point isolé hors domaine ; il ne dit pas clairement comment traiter une syntaxe globalement invalide.

**Recommandation :** faire échouer une expression mal formée ou inconnue, puis convertir en `None` les erreurs numériques dépendant du point. Une capture indifférenciée des exceptions masquerait aussi des défauts internes.

Exiger des bornes finies et un nombre entier d’échantillons au moins égal à deux. Le seul contrôle `x_min < x_max` ne suffit pas à exclure toutes les entrées problématiques. Les intervalles très larges peuvent également provoquer des dépassements dans les calculs intermédiaires.

Une singularité située entre deux échantillons peut rester invisible.

**Arbitrage :** garantir les coupures aux échantillons invalides. Présenter la détection supplémentaire des asymptotes comme facultative ; un seuil arbitraire risquerait de couper une fonction continue très pentue.

**5. SVG : sécurité et géométrie**

Les surfaces d’attaque principales sont le titre et toute autre chaîne utilisateur insérée dans le XML. L’échappement doit correspondre au contexte, y compris les guillemets dans les attributs. Certains caractères de contrôle restent invalides en XML même après échappement classique.

**Recommandation :** limiter les interpolations utilisateur à du texte correctement traité ; exclure scripts, gestionnaires d’événements, références externes et balisage utilisateur.

Cas géométriques à arbitrer explicitement :

- ordonnées constantes ou abscisses identiques : prévoir une échelle non dégénérée ;
- coordonnées non finies : les exclure du calcul des limites et du dessin ;
- segment réduit à un point : assurer sa visibilité si ce point est le seul tracé possible ;
- origine hors du domaine affiché : choisir une convention pour les axes et la documenter.

Un `None` doit réellement interrompre la courbe : filtrer les points invalides puis relier tous les autres violerait cette exigence.

**6. CLI et robustesse**

Les bornes de `plot` doivent accepter des expressions constantes, puisque l’exemple utilise `-pi` et `pi`. Le comportement des chemins contenant un point-virgule reste indéterminé ; une limitation documentée est acceptable.

L’écriture peut échouer pour des raisons de permissions, de chemin ou de stockage. Le message de réussite et l’entrée d’historique doivent intervenir après l’écriture réussie. La fin d’entrée et l’interruption utilisateur méritent une sortie propre.

La profondeur des expressions, leur longueur et le nombre d’échantillons constituent des surfaces d’épuisement des ressources.

**Arbitrage recommandé :** envisager des limites explicites et compréhensibles, en reconnaissant qu’aucun seuil n’est fixé par le challenge.

**7. Contrôles et points ouverts**

Prioriser les contrôles sur la précédence, le rejet intégral des entrées interdites, les exceptions numériques, les coupures, l’échappement XML et la récupération de la CLI. La vérification prescrite reste à exécuter par le candidat ; aucun résultat n’est établi ici.

Les ambiguïtés ci-dessus appellent des décisions consignées, sans modification rétroactive du challenge ou de sa suite figée. Aucun travail sur fichiers ni aucune opération Git réalisés.
--- END YOUR INITIAL SA-01 ---

--- BEGIN PEER INITIAL SA-02 ---
Avis SA-02 — privilégier une architecture à responsabilités séparées, avec des règles explicites pour les erreurs et les ruptures de courbe. Les risques principaux concernent la priorité des signes, la distinction entre syntaxe invalide et point hors domaine, ainsi que la robustesse de l’échelle SVG.

### 1. Structure recommandée

Conserver le livrable unique `scientific_calculator.py`, mais distinguer en interne :

- l’analyse lexicale et syntaxique ;
- l’évaluation numérique ;
- l’échantillonnage ;
- la transformation des coordonnées et la production SVG ;
- la boucle CLI et son historique.

Les trois fonctions publiques doivent fonctionner indépendamment de la CLI. Importer le module ne doit déclencher ni invite interactive ni écriture.

**Arbitrage recommandé :** un analyseur dédié, simple et fondé sur une liste fermée de constructions autorisées. Une architecture extensible par greffons ou un langage intermédiaire général ajouterait une complexité inutile. Une représentation interne réutilisable de l’expression permet néanmoins de l’analyser une seule fois pour tout un échantillonnage.

### 2. Invariants du moteur d’expressions

**Reconnaissance complète.** Toute l’expression doit être consommée. Une partie valide suivie de caractères interdits doit échouer. Les nombres scientifiques doivent être reconnus sans confondre leur exposant avec un opérateur ou la constante `e`.

**Priorités.** L’associativité à droite de la puissance et sa priorité sur les signes doivent être conçues ensemble. Les exemples imposés ne suffisent pas à éliminer toutes les erreurs : `2^-2`, `(-2)^2` et `-2^-2` sont également discriminants.

**Noms autorisés.** Séparer constantes, fonctions et variable. La présence d’une clé dans `variables` ne doit pas étendre implicitement le langage à des noms arbitraires. Définir clairement le traitement de `x` absent, des clés supplémentaires et des tentatives de redéfinition de `pi` ou `e`.

**Résultats et exceptions.**

- Tout succès de `evaluate` produit un `float` fini.
- Toute syntaxe invalide, tout nom interdit ou tout résultat hors du domaine réel produit `ValueError`.
- Une division explicite par zéro conserve `ZeroDivisionError`.
- Un dépassement numérique doit être normalisé en erreur conforme au contrat ; aucun résultat complexe, `NaN` ou infini ne doit sortir.

**Arbitrage recommandé :** traiter les opérateurs selon leur sémantique réelle, puis vérifier la finitude. Éviter une capture globale qui transformerait une erreur de programmation en erreur utilisateur. Le cas `0^-1` mérite une décision documentée : le contrat distingue division par zéro et puissance hors domaine sans préciser explicitement leur frontière.

### 3. Échantillonnage : préserver les ruptures sans cacher les erreurs

L’échantillonnage devrait garantir :

- exactement le nombre demandé de points, avec des abscisses ordonnées ;
- les deux bornes incluses explicitement ;
- une ordonnée finie ou `None` pour chaque abscisse ;
- aucune interruption provoquée par un point isolé hors domaine.

Valider les paramètres avant le calcul : bornes finies, intervalle strictement croissant, nombre entier d’échantillons au moins égal à deux. Les bornes très grandes peuvent provoquer un dépassement dans des calculs intermédiaires malgré des entrées finies.

**Arbitrage recommandé :** rejeter une expression syntaxiquement invalide avant de parcourir les points ; convertir ensuite les seules erreurs numériques attendues en `None`. Le contrat ne précise pas complètement le comportement de `sample_curve` sur une expression mal formée : cette distinction est utile, mais doit rester identifiée comme un choix d’interprétation.

Une discontinuité située entre deux échantillons peut rester invisible. Ainsi, `1/x` ne produit une coupure certaine que si un point atteint zéro, sauf mécanisme supplémentaire.

**Arbitrage recommandé :** assurer les coupures aux valeurs effectivement invalides et documenter la limite de l’échantillonnage. Une heuristique de grands écarts pourrait couper à tort une fonction continue ; elle ne devrait pas devenir une exigence implicite.

### 4. SVG : géométrie robuste et contenu inerte

Le producteur SVG doit être testable avec des points construits directement, indépendamment du moteur.

Invariants essentiels :

- l’échelle dépend uniquement des couples de coordonnées finis ;
- aucune coordonnée sérialisée ne contient `NaN` ou une infinité ;
- aucun segment ne traverse un point invalide ;
- une courbe constante ou un unique point fini ne provoque aucune division par zéro ;
- fond et deux éléments `line` pour les axes sont présents ;
- tout texte utilisateur est échappé dans son contexte XML.

**Arbitrages à expliciter :**

- Prévoir une marge lorsque l’étendue horizontale ou verticale est nulle.
- Pour une série ne contenant qu’un point fini, préférer un marqueur visible.
- Si zéro est hors des données, préciser comment concilier adaptation de l’échelle et visibilité des deux axes : inclusion de zéro ou représentation aux bords. Le texte ne tranche pas cette présentation.
- Traiter les points fournis directement avec des coordonnées non finies comme invalides et comme ruptures.

Limiter le document aux éléments SVG nécessaires facilite la vérification de son innocuité.

### 5. CLI et historique

Faire dépendre l’ajout à l’historique de la réussite complète : résultat obtenu pour une expression, fichier effectivement écrit pour un tracé. Un échec d’écriture ne doit pas être enregistré comme succès.

Les bornes de `plot` doivent bénéficier du même moteur, notamment pour `-pi` et `pi`. Vérifier le nombre de champs séparés par des points-virgules et les champs vides.

**Arbitrage recommandé :** intercepter les erreurs attendues à la frontière CLI, avec un message contextualisé et une nouvelle invite. Prévoir également une sortie propre à la fin de l’entrée standard. Les commandes de gestion ne devraient pas polluer l’historique des expressions et tracés réussis.

### 6. Validation prioritaire

Organiser les contrôles par contrat observable :

1. **Moteur :** précédence, exposants signés, notation scientifique, arité des fonctions, consommation complète, noms interdits, exceptions et finitude.
2. **Échantillonnage :** bornes exactes, nombre de points, intervalle invalide, `sqrt(x)` sur un intervalle mixte, `1/x` avec zéro échantillonné.
3. **SVG :** analyse XML, éléments attendus, titre contenant `<`, `&` et guillemets, ruptures effectives, courbe constante, absence totale de points finis.
4. **CLI :** session comportant succès, erreur, nouveau succès, historique, effacement et sortie ; ajouter un chemin de sortie inaccessible.
5. **Livraison :** absence d’exécution dynamique interdite, documentation des conventions et lancement de la commande d’acceptation fournie.

Ces contrôles doivent mesurer les comportements, sans imposer une organisation interne particulière. Aucun outil ni dépôt n’a été consulté et aucun test n’a été exécuté ; le verdict technique reste celui du vérificateur indépendant.
--- END PEER INITIAL SA-02 ---

````

</details>

````text
Avis SA-01 — **confirmation avec révisions ciblées**. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge original n’étant pas joint à cet échange, elle ne constitue pas une vérification indépendante de ses exigences.

**Accords et doublons.** Les analyses convergent sur les risques principaux : consommation intégrale de l’expression, langage fermé, priorité et associativité de la puissance, résultats réels finis, exceptions maîtrisées, distinction entre syntaxe invalide et erreur numérique ponctuelle, ruptures effectives du tracé et historique conditionné à la réussite complète. Ces recommandations se recouvrent largement : les regrouper en une seule liste de critères observables évitera de multiplier artificiellement les obligations.

Même convergence sur les limites : aucune garantie de détection des singularités entre échantillons, aucune obligation implicite de calcul symbolique et aucune heuristique de rupture à imposer sans fondement contractuel.

**Désaccords utiles et révisions.**

- La formulation SA-02 « livrable unique `scientific_calculator.py` » mérite correction : mon avis initial mentionne également `README.md`. Parler de **module Python unique accompagné du README** lève cette ambiguïté.
- La séparation des responsabilités et l’analyse unique de l’expression sont de bonnes recommandations internes. Elles ne doivent pas devenir des critères d’acceptation : plusieurs architectures peuvent respecter les mêmes comportements.
- Je confirme la distinction proposée pour `sample_curve`, mais conserve son statut d’**interprétation à documenter**. Notre accord ne transforme pas le rejet préalable d’une syntaxe invalide en exigence explicitement établie.
- Les conventions relatives à `0^-1`, `0^0`, aux clés supplémentaires de `variables`, aux axes hors origine et aux points isolés restent des arbitrages. Leur documentation doit les distinguer des obligations.
- L’expression « abscisses ordonnées » ne devrait pas être durcie en croissance strictement positive entre chaque paire : la précision flottante peut produire des abscisses identiques sur un intervalle très étroit. Les exigences rapportées sur le nombre de points et les bornes restent prioritaires.

**Compléments à conserver.** SA-02 apporte des contrôles utiles sur l’absence d’effets lors de l’import, l’utilisation indépendante des fonctions publiques et le SVG sans aucun point fini. Mon avis ajoute deux surfaces de sécurité peu développées chez SA-02 : les caractères interdits en XML malgré l’échappement classique, et l’épuisement des ressources. Des limites éventuelles doivent être justifiées et documentées, sans inventer de seuil contractuel.

**Priorité des recommandations.**

1. **Conformité et sécurité :** langage fermé, absence d’exécution dynamique, validation complète, exceptions conformes, finitude, XML valide et contenu SVG inerte.
2. **Comportement observable :** échantillonnage conforme, ruptures préservées, géométrie dégénérée maîtrisée, reprise de la CLI après erreur et historique après écriture réussie.
3. **Arbitrages documentés :** conventions numériques, entrées ambiguës, cas limites du SVG et limites de ressources.
4. **Organisation interne :** séparation des responsabilités et réutilisation de l’analyse, sans imposer ces choix au vérificateur.

Aucun outil, fichier, test, opération Git ou délégation utilisé. Les contrôles restent à exécuter par le candidat ; le verdict appartient au vérificateur indépendant.
````

### MSG-004 — 04-sa02-cross

<details>
<summary>Mandat envoyé</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-02 ---
Avis SA-02 — privilégier une architecture à responsabilités séparées, avec des règles explicites pour les erreurs et les ruptures de courbe. Les risques principaux concernent la priorité des signes, la distinction entre syntaxe invalide et point hors domaine, ainsi que la robustesse de l’échelle SVG.

### 1. Structure recommandée

Conserver le livrable unique `scientific_calculator.py`, mais distinguer en interne :

- l’analyse lexicale et syntaxique ;
- l’évaluation numérique ;
- l’échantillonnage ;
- la transformation des coordonnées et la production SVG ;
- la boucle CLI et son historique.

Les trois fonctions publiques doivent fonctionner indépendamment de la CLI. Importer le module ne doit déclencher ni invite interactive ni écriture.

**Arbitrage recommandé :** un analyseur dédié, simple et fondé sur une liste fermée de constructions autorisées. Une architecture extensible par greffons ou un langage intermédiaire général ajouterait une complexité inutile. Une représentation interne réutilisable de l’expression permet néanmoins de l’analyser une seule fois pour tout un échantillonnage.

### 2. Invariants du moteur d’expressions

**Reconnaissance complète.** Toute l’expression doit être consommée. Une partie valide suivie de caractères interdits doit échouer. Les nombres scientifiques doivent être reconnus sans confondre leur exposant avec un opérateur ou la constante `e`.

**Priorités.** L’associativité à droite de la puissance et sa priorité sur les signes doivent être conçues ensemble. Les exemples imposés ne suffisent pas à éliminer toutes les erreurs : `2^-2`, `(-2)^2` et `-2^-2` sont également discriminants.

**Noms autorisés.** Séparer constantes, fonctions et variable. La présence d’une clé dans `variables` ne doit pas étendre implicitement le langage à des noms arbitraires. Définir clairement le traitement de `x` absent, des clés supplémentaires et des tentatives de redéfinition de `pi` ou `e`.

**Résultats et exceptions.**

- Tout succès de `evaluate` produit un `float` fini.
- Toute syntaxe invalide, tout nom interdit ou tout résultat hors du domaine réel produit `ValueError`.
- Une division explicite par zéro conserve `ZeroDivisionError`.
- Un dépassement numérique doit être normalisé en erreur conforme au contrat ; aucun résultat complexe, `NaN` ou infini ne doit sortir.

**Arbitrage recommandé :** traiter les opérateurs selon leur sémantique réelle, puis vérifier la finitude. Éviter une capture globale qui transformerait une erreur de programmation en erreur utilisateur. Le cas `0^-1` mérite une décision documentée : le contrat distingue division par zéro et puissance hors domaine sans préciser explicitement leur frontière.

### 3. Échantillonnage : préserver les ruptures sans cacher les erreurs

L’échantillonnage devrait garantir :

- exactement le nombre demandé de points, avec des abscisses ordonnées ;
- les deux bornes incluses explicitement ;
- une ordonnée finie ou `None` pour chaque abscisse ;
- aucune interruption provoquée par un point isolé hors domaine.

Valider les paramètres avant le calcul : bornes finies, intervalle strictement croissant, nombre entier d’échantillons au moins égal à deux. Les bornes très grandes peuvent provoquer un dépassement dans des calculs intermédiaires malgré des entrées finies.

**Arbitrage recommandé :** rejeter une expression syntaxiquement invalide avant de parcourir les points ; convertir ensuite les seules erreurs numériques attendues en `None`. Le contrat ne précise pas complètement le comportement de `sample_curve` sur une expression mal formée : cette distinction est utile, mais doit rester identifiée comme un choix d’interprétation.

Une discontinuité située entre deux échantillons peut rester invisible. Ainsi, `1/x` ne produit une coupure certaine que si un point atteint zéro, sauf mécanisme supplémentaire.

**Arbitrage recommandé :** assurer les coupures aux valeurs effectivement invalides et documenter la limite de l’échantillonnage. Une heuristique de grands écarts pourrait couper à tort une fonction continue ; elle ne devrait pas devenir une exigence implicite.

### 4. SVG : géométrie robuste et contenu inerte

Le producteur SVG doit être testable avec des points construits directement, indépendamment du moteur.

Invariants essentiels :

- l’échelle dépend uniquement des couples de coordonnées finis ;
- aucune coordonnée sérialisée ne contient `NaN` ou une infinité ;
- aucun segment ne traverse un point invalide ;
- une courbe constante ou un unique point fini ne provoque aucune division par zéro ;
- fond et deux éléments `line` pour les axes sont présents ;
- tout texte utilisateur est échappé dans son contexte XML.

**Arbitrages à expliciter :**

- Prévoir une marge lorsque l’étendue horizontale ou verticale est nulle.
- Pour une série ne contenant qu’un point fini, préférer un marqueur visible.
- Si zéro est hors des données, préciser comment concilier adaptation de l’échelle et visibilité des deux axes : inclusion de zéro ou représentation aux bords. Le texte ne tranche pas cette présentation.
- Traiter les points fournis directement avec des coordonnées non finies comme invalides et comme ruptures.

Limiter le document aux éléments SVG nécessaires facilite la vérification de son innocuité.

### 5. CLI et historique

Faire dépendre l’ajout à l’historique de la réussite complète : résultat obtenu pour une expression, fichier effectivement écrit pour un tracé. Un échec d’écriture ne doit pas être enregistré comme succès.

Les bornes de `plot` doivent bénéficier du même moteur, notamment pour `-pi` et `pi`. Vérifier le nombre de champs séparés par des points-virgules et les champs vides.

**Arbitrage recommandé :** intercepter les erreurs attendues à la frontière CLI, avec un message contextualisé et une nouvelle invite. Prévoir également une sortie propre à la fin de l’entrée standard. Les commandes de gestion ne devraient pas polluer l’historique des expressions et tracés réussis.

### 6. Validation prioritaire

Organiser les contrôles par contrat observable :

1. **Moteur :** précédence, exposants signés, notation scientifique, arité des fonctions, consommation complète, noms interdits, exceptions et finitude.
2. **Échantillonnage :** bornes exactes, nombre de points, intervalle invalide, `sqrt(x)` sur un intervalle mixte, `1/x` avec zéro échantillonné.
3. **SVG :** analyse XML, éléments attendus, titre contenant `<`, `&` et guillemets, ruptures effectives, courbe constante, absence totale de points finis.
4. **CLI :** session comportant succès, erreur, nouveau succès, historique, effacement et sortie ; ajouter un chemin de sortie inaccessible.
5. **Livraison :** absence d’exécution dynamique interdite, documentation des conventions et lancement de la commande d’acceptation fournie.

Ces contrôles doivent mesurer les comportements, sans imposer une organisation interne particulière. Aucun outil ni dépôt n’a été consulté et aucun test n’a été exécuté ; le verdict technique reste celui du vérificateur indépendant.
--- END YOUR INITIAL SA-02 ---

--- BEGIN PEER INITIAL SA-01 ---
Avis SA-01 — analyse indépendante des exigences et de la sécurité, fondée exclusivement sur le challenge fourni. Aucun outil, dépôt, fichier ou test consulté ; aucune délégation. Le verdict technique reste à la charge du vérificateur indépendant.

**1. Obligations non négociables**

La livraison comprend `scientific_calculator.py` et `README.md`, exclusivement dans `solution/`. Elle doit fonctionner avec la bibliothèque standard sous Python 3.10 ou supérieur, sans réseau ni exécution dynamique (`eval`, `exec`, `compile`).

Les trois fonctions publiques doivent respecter leurs signatures et contrats. Points particulièrement discriminants :

- `evaluate` retourne toujours un flottant fini en cas de réussite ; les résultats complexes, infinis ou indéfinis sont des erreurs.
- La puissance est associative à droite et prioritaire sur les signes unaires.
- Les noms, appels et caractères autorisés forment une liste fermée.
- `sample_curve` inclut exactement les bornes et conserve les points invalides sous forme de couples `(x, None)`.
- Le SVG contient un fond, deux axes constitués d’éléments `line`, une courbe interrompue aux points invalides et aucun contenu actif.
- La CLI reste utilisable après une erreur et n’enregistre que les expressions et tracés réussis.
- Le README explique lancement, syntaxe, fonctions, exemples et limites.

**Arbitrage :** traiter ces éléments comme des critères d’acceptation, sans les assouplir au nom d’une commodité d’implémentation.

**2. Grammaire : préciser les choix sans élargir le langage**

Plusieurs frontières ne sont pas explicites : nombres `.5` ou `5.`, casse des fonctions, chiffres Unicode, multiplication implicite, appel sans parenthèses et alias `**`.

**Recommandation :** accepter les formes décimales usuelles `.5` et `5.`, les exposants scientifiques signés, et les espaces entre jetons ; conserver les noms canoniques et les appels avec parenthèses. Refuser les extensions non prévues telles que `2pi`, `sin x` et `**`. La totalité de l’entrée doit être consommée : accepter un préfixe valide suivi de caractères interdits serait une faille de validation.

Les fonctions listées sont unaires : les appels sans argument ou avec plusieurs arguments doivent échouer. La grammaire doit permettre `2^-2` et interpréter `-2^-2` comme `-(2^(-2))`, conformément aux priorités annoncées.

Le dictionnaire `variables` pourrait laisser croire que tout identifiant est injectable.

**Arbitrage recommandé :** seule `x` peut être résolue comme variable ; les clés supplémentaires ne doivent ni autoriser d’autres noms ni remplacer `pi`, `e` ou les fonctions. Leur rejet explicite ou leur ignorance reste à documenter.

**3. Erreurs numériques : stabiliser les exceptions**

L’obligation de résultat fini implique que dépassements numériques et résultats non finis deviennent des `ValueError`, plutôt que de laisser remonter une exception interne telle qu’`OverflowError`. Une division explicite par zéro doit conserver `ZeroDivisionError`.

Deux cas demandent une décision documentée :

- `0^-1` : recommander `ValueError`, comme puissance hors domaine, puisque l’obligation spécifique de `ZeroDivisionError` vise la division.
- `0^0` : le challenge ne tranche pas ; la convention numérique `1.0` est défendable, mais ne doit pas être présentée comme une exigence explicite.

Pour les puissances négatives à exposant fractionnaire, le comportement réel mérite également une limite claire : une approximation flottante de `1/3` ne fournit pas automatiquement une information rationnelle exacte.

**Arbitrage :** documenter la convention numérique retenue, sans promettre de calcul symbolique. De même, `tan(pi/2)` peut produire un grand flottant fini : imposer une détection mathématique exacte des pôles dépasserait les précisions du contrat.

**4. Échantillonnage : distinguer expression invalide et point invalide**

Le contrat protège le tracé contre un point isolé hors domaine ; il ne dit pas clairement comment traiter une syntaxe globalement invalide.

**Recommandation :** faire échouer une expression mal formée ou inconnue, puis convertir en `None` les erreurs numériques dépendant du point. Une capture indifférenciée des exceptions masquerait aussi des défauts internes.

Exiger des bornes finies et un nombre entier d’échantillons au moins égal à deux. Le seul contrôle `x_min < x_max` ne suffit pas à exclure toutes les entrées problématiques. Les intervalles très larges peuvent également provoquer des dépassements dans les calculs intermédiaires.

Une singularité située entre deux échantillons peut rester invisible.

**Arbitrage :** garantir les coupures aux échantillons invalides. Présenter la détection supplémentaire des asymptotes comme facultative ; un seuil arbitraire risquerait de couper une fonction continue très pentue.

**5. SVG : sécurité et géométrie**

Les surfaces d’attaque principales sont le titre et toute autre chaîne utilisateur insérée dans le XML. L’échappement doit correspondre au contexte, y compris les guillemets dans les attributs. Certains caractères de contrôle restent invalides en XML même après échappement classique.

**Recommandation :** limiter les interpolations utilisateur à du texte correctement traité ; exclure scripts, gestionnaires d’événements, références externes et balisage utilisateur.

Cas géométriques à arbitrer explicitement :

- ordonnées constantes ou abscisses identiques : prévoir une échelle non dégénérée ;
- coordonnées non finies : les exclure du calcul des limites et du dessin ;
- segment réduit à un point : assurer sa visibilité si ce point est le seul tracé possible ;
- origine hors du domaine affiché : choisir une convention pour les axes et la documenter.

Un `None` doit réellement interrompre la courbe : filtrer les points invalides puis relier tous les autres violerait cette exigence.

**6. CLI et robustesse**

Les bornes de `plot` doivent accepter des expressions constantes, puisque l’exemple utilise `-pi` et `pi`. Le comportement des chemins contenant un point-virgule reste indéterminé ; une limitation documentée est acceptable.

L’écriture peut échouer pour des raisons de permissions, de chemin ou de stockage. Le message de réussite et l’entrée d’historique doivent intervenir après l’écriture réussie. La fin d’entrée et l’interruption utilisateur méritent une sortie propre.

La profondeur des expressions, leur longueur et le nombre d’échantillons constituent des surfaces d’épuisement des ressources.

**Arbitrage recommandé :** envisager des limites explicites et compréhensibles, en reconnaissant qu’aucun seuil n’est fixé par le challenge.

**7. Contrôles et points ouverts**

Prioriser les contrôles sur la précédence, le rejet intégral des entrées interdites, les exceptions numériques, les coupures, l’échappement XML et la récupération de la CLI. La vérification prescrite reste à exécuter par le candidat ; aucun résultat n’est établi ici.

Les ambiguïtés ci-dessus appellent des décisions consignées, sans modification rétroactive du challenge ou de sa suite figée. Aucun travail sur fichiers ni aucune opération Git réalisés.
--- END PEER INITIAL SA-01 ---

````

</details>

````text
**Avis SA-02 — confirmation avec révisions ciblées**

Les deux avis convergent sur l’architecture et les risques principaux. Je confirme leurs recommandations communes, avec une réserve : le challenge intégral n’étant pas reproduit dans cet échange, cette confrontation ne vérifie pas indépendamment les obligations qu’ils lui attribuent.

**Accords et doublons**

La séparation entre analyse, évaluation, échantillonnage, SVG et CLI constitue une base cohérente et testable. Elle permet de contrôler chaque fonction publique indépendamment, notamment le SVG avec des points construits directement.

Les recommandations sur la consommation complète de l’expression, la priorité des puissances, les noms autorisés, les résultats finis et les exceptions numériques sont concordantes. Même accord sur les ruptures aux points invalides, l’échappement XML et l’historique alimenté après réussite effective.

Ces sujets représentent des doublons à fusionner dans une seule matrice de validation. Répéter leur justification dans plusieurs documents apporterait peu ; associer chaque invariant à un contrôle observable serait plus utile.

**Révisions et désaccords utiles**

Je corrige ma formulation « livrable unique » : elle devait désigner le module Python unique. SA-01 mentionne également un `README.md` ; la structure interne recommandée ne justifie donc pas de réduire la livraison à un seul fichier.

Je retiens l’apport de SA-01 concernant les caractères interdits en XML : l’échappement de `<`, `&` et des guillemets ne suffit pas à garantir un document valide. La validation doit couvrir cette distinction, avec une convention documentée de rejet ou de traitement.

Je nuance notre formulation commune « erreurs numériques dépendant du point ». Une expression syntaxiquement valide telle que `1/0` peut être invalide à tous les points. La frontière utile sépare les erreurs de langage des erreurs numériques rencontrées pendant l’évaluation ; elle ne doit pas imposer une analyse supplémentaire de dépendance à `x`.

Les propositions concernant `0^-1`, `0^0`, les formes décimales et les axes hors origine restent des conventions à consigner, sous réserve du texte contractuel. Leur accord entre consultants ne les transforme pas en exigences.

Enfin, les limites de ressources et la visibilité d’un point isolé sont des recommandations complémentaires. Des seuils arbitraires pourraient refuser des entrées autrement conformes ; ils ne doivent pas précéder la satisfaction des contrats rapportés.

**Priorité des recommandations**

1. **Conformité centrale :** signatures publiques, import sans effet de bord, langage fermé, précédence, finitude et catégories d’exceptions. Contrôler les comportements sans imposer une représentation interne particulière.
2. **Intégrité du tracé :** nombre de points et bornes, conservation des invalides, ruptures réelles, échelles non dégénérées et coordonnées SVG finies, y compris avec de grandes valeurs.
3. **Validité et interaction :** XML valide et inerte, reprise de la CLI après erreur, absence de succès annoncé ou enregistré après un échec d’écriture.
4. **Conventions et livraison :** documenter les ambiguïtés et les limites de l’échantillonnage, puis exécuter la vérification prescrite. La détection supplémentaire des asymptotes reste facultative selon les deux avis.

Cette réponse est exclusivement consultative : aucun outil, fichier, test, sous-agent ou opération Git mobilisé. Aucun résultat technique n’est établi ; le verdict appartient au vérificateur indépendant.
````

### MSG-005 — 05-main-first

<details>
<summary>Mandat envoyé</summary>

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
Avis SA-01 — analyse indépendante des exigences et de la sécurité, fondée exclusivement sur le challenge fourni. Aucun outil, dépôt, fichier ou test consulté ; aucune délégation. Le verdict technique reste à la charge du vérificateur indépendant.

**1. Obligations non négociables**

La livraison comprend `scientific_calculator.py` et `README.md`, exclusivement dans `solution/`. Elle doit fonctionner avec la bibliothèque standard sous Python 3.10 ou supérieur, sans réseau ni exécution dynamique (`eval`, `exec`, `compile`).

Les trois fonctions publiques doivent respecter leurs signatures et contrats. Points particulièrement discriminants :

- `evaluate` retourne toujours un flottant fini en cas de réussite ; les résultats complexes, infinis ou indéfinis sont des erreurs.
- La puissance est associative à droite et prioritaire sur les signes unaires.
- Les noms, appels et caractères autorisés forment une liste fermée.
- `sample_curve` inclut exactement les bornes et conserve les points invalides sous forme de couples `(x, None)`.
- Le SVG contient un fond, deux axes constitués d’éléments `line`, une courbe interrompue aux points invalides et aucun contenu actif.
- La CLI reste utilisable après une erreur et n’enregistre que les expressions et tracés réussis.
- Le README explique lancement, syntaxe, fonctions, exemples et limites.

**Arbitrage :** traiter ces éléments comme des critères d’acceptation, sans les assouplir au nom d’une commodité d’implémentation.

**2. Grammaire : préciser les choix sans élargir le langage**

Plusieurs frontières ne sont pas explicites : nombres `.5` ou `5.`, casse des fonctions, chiffres Unicode, multiplication implicite, appel sans parenthèses et alias `**`.

**Recommandation :** accepter les formes décimales usuelles `.5` et `5.`, les exposants scientifiques signés, et les espaces entre jetons ; conserver les noms canoniques et les appels avec parenthèses. Refuser les extensions non prévues telles que `2pi`, `sin x` et `**`. La totalité de l’entrée doit être consommée : accepter un préfixe valide suivi de caractères interdits serait une faille de validation.

Les fonctions listées sont unaires : les appels sans argument ou avec plusieurs arguments doivent échouer. La grammaire doit permettre `2^-2` et interpréter `-2^-2` comme `-(2^(-2))`, conformément aux priorités annoncées.

Le dictionnaire `variables` pourrait laisser croire que tout identifiant est injectable.

**Arbitrage recommandé :** seule `x` peut être résolue comme variable ; les clés supplémentaires ne doivent ni autoriser d’autres noms ni remplacer `pi`, `e` ou les fonctions. Leur rejet explicite ou leur ignorance reste à documenter.

**3. Erreurs numériques : stabiliser les exceptions**

L’obligation de résultat fini implique que dépassements numériques et résultats non finis deviennent des `ValueError`, plutôt que de laisser remonter une exception interne telle qu’`OverflowError`. Une division explicite par zéro doit conserver `ZeroDivisionError`.

Deux cas demandent une décision documentée :

- `0^-1` : recommander `ValueError`, comme puissance hors domaine, puisque l’obligation spécifique de `ZeroDivisionError` vise la division.
- `0^0` : le challenge ne tranche pas ; la convention numérique `1.0` est défendable, mais ne doit pas être présentée comme une exigence explicite.

Pour les puissances négatives à exposant fractionnaire, le comportement réel mérite également une limite claire : une approximation flottante de `1/3` ne fournit pas automatiquement une information rationnelle exacte.

**Arbitrage :** documenter la convention numérique retenue, sans promettre de calcul symbolique. De même, `tan(pi/2)` peut produire un grand flottant fini : imposer une détection mathématique exacte des pôles dépasserait les précisions du contrat.

**4. Échantillonnage : distinguer expression invalide et point invalide**

Le contrat protège le tracé contre un point isolé hors domaine ; il ne dit pas clairement comment traiter une syntaxe globalement invalide.

**Recommandation :** faire échouer une expression mal formée ou inconnue, puis convertir en `None` les erreurs numériques dépendant du point. Une capture indifférenciée des exceptions masquerait aussi des défauts internes.

Exiger des bornes finies et un nombre entier d’échantillons au moins égal à deux. Le seul contrôle `x_min < x_max` ne suffit pas à exclure toutes les entrées problématiques. Les intervalles très larges peuvent également provoquer des dépassements dans les calculs intermédiaires.

Une singularité située entre deux échantillons peut rester invisible.

**Arbitrage :** garantir les coupures aux échantillons invalides. Présenter la détection supplémentaire des asymptotes comme facultative ; un seuil arbitraire risquerait de couper une fonction continue très pentue.

**5. SVG : sécurité et géométrie**

Les surfaces d’attaque principales sont le titre et toute autre chaîne utilisateur insérée dans le XML. L’échappement doit correspondre au contexte, y compris les guillemets dans les attributs. Certains caractères de contrôle restent invalides en XML même après échappement classique.

**Recommandation :** limiter les interpolations utilisateur à du texte correctement traité ; exclure scripts, gestionnaires d’événements, références externes et balisage utilisateur.

Cas géométriques à arbitrer explicitement :

- ordonnées constantes ou abscisses identiques : prévoir une échelle non dégénérée ;
- coordonnées non finies : les exclure du calcul des limites et du dessin ;
- segment réduit à un point : assurer sa visibilité si ce point est le seul tracé possible ;
- origine hors du domaine affiché : choisir une convention pour les axes et la documenter.

Un `None` doit réellement interrompre la courbe : filtrer les points invalides puis relier tous les autres violerait cette exigence.

**6. CLI et robustesse**

Les bornes de `plot` doivent accepter des expressions constantes, puisque l’exemple utilise `-pi` et `pi`. Le comportement des chemins contenant un point-virgule reste indéterminé ; une limitation documentée est acceptable.

L’écriture peut échouer pour des raisons de permissions, de chemin ou de stockage. Le message de réussite et l’entrée d’historique doivent intervenir après l’écriture réussie. La fin d’entrée et l’interruption utilisateur méritent une sortie propre.

La profondeur des expressions, leur longueur et le nombre d’échantillons constituent des surfaces d’épuisement des ressources.

**Arbitrage recommandé :** envisager des limites explicites et compréhensibles, en reconnaissant qu’aucun seuil n’est fixé par le challenge.

**7. Contrôles et points ouverts**

Prioriser les contrôles sur la précédence, le rejet intégral des entrées interdites, les exceptions numériques, les coupures, l’échappement XML et la récupération de la CLI. La vérification prescrite reste à exécuter par le candidat ; aucun résultat n’est établi ici.

Les ambiguïtés ci-dessus appellent des décisions consignées, sans modification rétroactive du challenge ou de sa suite figée. Aucun travail sur fichiers ni aucune opération Git réalisés.
--- END SA-01 INITIAL ---

--- BEGIN SA-02 INITIAL ---
Avis SA-02 — privilégier une architecture à responsabilités séparées, avec des règles explicites pour les erreurs et les ruptures de courbe. Les risques principaux concernent la priorité des signes, la distinction entre syntaxe invalide et point hors domaine, ainsi que la robustesse de l’échelle SVG.

### 1. Structure recommandée

Conserver le livrable unique `scientific_calculator.py`, mais distinguer en interne :

- l’analyse lexicale et syntaxique ;
- l’évaluation numérique ;
- l’échantillonnage ;
- la transformation des coordonnées et la production SVG ;
- la boucle CLI et son historique.

Les trois fonctions publiques doivent fonctionner indépendamment de la CLI. Importer le module ne doit déclencher ni invite interactive ni écriture.

**Arbitrage recommandé :** un analyseur dédié, simple et fondé sur une liste fermée de constructions autorisées. Une architecture extensible par greffons ou un langage intermédiaire général ajouterait une complexité inutile. Une représentation interne réutilisable de l’expression permet néanmoins de l’analyser une seule fois pour tout un échantillonnage.

### 2. Invariants du moteur d’expressions

**Reconnaissance complète.** Toute l’expression doit être consommée. Une partie valide suivie de caractères interdits doit échouer. Les nombres scientifiques doivent être reconnus sans confondre leur exposant avec un opérateur ou la constante `e`.

**Priorités.** L’associativité à droite de la puissance et sa priorité sur les signes doivent être conçues ensemble. Les exemples imposés ne suffisent pas à éliminer toutes les erreurs : `2^-2`, `(-2)^2` et `-2^-2` sont également discriminants.

**Noms autorisés.** Séparer constantes, fonctions et variable. La présence d’une clé dans `variables` ne doit pas étendre implicitement le langage à des noms arbitraires. Définir clairement le traitement de `x` absent, des clés supplémentaires et des tentatives de redéfinition de `pi` ou `e`.

**Résultats et exceptions.**

- Tout succès de `evaluate` produit un `float` fini.
- Toute syntaxe invalide, tout nom interdit ou tout résultat hors du domaine réel produit `ValueError`.
- Une division explicite par zéro conserve `ZeroDivisionError`.
- Un dépassement numérique doit être normalisé en erreur conforme au contrat ; aucun résultat complexe, `NaN` ou infini ne doit sortir.

**Arbitrage recommandé :** traiter les opérateurs selon leur sémantique réelle, puis vérifier la finitude. Éviter une capture globale qui transformerait une erreur de programmation en erreur utilisateur. Le cas `0^-1` mérite une décision documentée : le contrat distingue division par zéro et puissance hors domaine sans préciser explicitement leur frontière.

### 3. Échantillonnage : préserver les ruptures sans cacher les erreurs

L’échantillonnage devrait garantir :

- exactement le nombre demandé de points, avec des abscisses ordonnées ;
- les deux bornes incluses explicitement ;
- une ordonnée finie ou `None` pour chaque abscisse ;
- aucune interruption provoquée par un point isolé hors domaine.

Valider les paramètres avant le calcul : bornes finies, intervalle strictement croissant, nombre entier d’échantillons au moins égal à deux. Les bornes très grandes peuvent provoquer un dépassement dans des calculs intermédiaires malgré des entrées finies.

**Arbitrage recommandé :** rejeter une expression syntaxiquement invalide avant de parcourir les points ; convertir ensuite les seules erreurs numériques attendues en `None`. Le contrat ne précise pas complètement le comportement de `sample_curve` sur une expression mal formée : cette distinction est utile, mais doit rester identifiée comme un choix d’interprétation.

Une discontinuité située entre deux échantillons peut rester invisible. Ainsi, `1/x` ne produit une coupure certaine que si un point atteint zéro, sauf mécanisme supplémentaire.

**Arbitrage recommandé :** assurer les coupures aux valeurs effectivement invalides et documenter la limite de l’échantillonnage. Une heuristique de grands écarts pourrait couper à tort une fonction continue ; elle ne devrait pas devenir une exigence implicite.

### 4. SVG : géométrie robuste et contenu inerte

Le producteur SVG doit être testable avec des points construits directement, indépendamment du moteur.

Invariants essentiels :

- l’échelle dépend uniquement des couples de coordonnées finis ;
- aucune coordonnée sérialisée ne contient `NaN` ou une infinité ;
- aucun segment ne traverse un point invalide ;
- une courbe constante ou un unique point fini ne provoque aucune division par zéro ;
- fond et deux éléments `line` pour les axes sont présents ;
- tout texte utilisateur est échappé dans son contexte XML.

**Arbitrages à expliciter :**

- Prévoir une marge lorsque l’étendue horizontale ou verticale est nulle.
- Pour une série ne contenant qu’un point fini, préférer un marqueur visible.
- Si zéro est hors des données, préciser comment concilier adaptation de l’échelle et visibilité des deux axes : inclusion de zéro ou représentation aux bords. Le texte ne tranche pas cette présentation.
- Traiter les points fournis directement avec des coordonnées non finies comme invalides et comme ruptures.

Limiter le document aux éléments SVG nécessaires facilite la vérification de son innocuité.

### 5. CLI et historique

Faire dépendre l’ajout à l’historique de la réussite complète : résultat obtenu pour une expression, fichier effectivement écrit pour un tracé. Un échec d’écriture ne doit pas être enregistré comme succès.

Les bornes de `plot` doivent bénéficier du même moteur, notamment pour `-pi` et `pi`. Vérifier le nombre de champs séparés par des points-virgules et les champs vides.

**Arbitrage recommandé :** intercepter les erreurs attendues à la frontière CLI, avec un message contextualisé et une nouvelle invite. Prévoir également une sortie propre à la fin de l’entrée standard. Les commandes de gestion ne devraient pas polluer l’historique des expressions et tracés réussis.

### 6. Validation prioritaire

Organiser les contrôles par contrat observable :

1. **Moteur :** précédence, exposants signés, notation scientifique, arité des fonctions, consommation complète, noms interdits, exceptions et finitude.
2. **Échantillonnage :** bornes exactes, nombre de points, intervalle invalide, `sqrt(x)` sur un intervalle mixte, `1/x` avec zéro échantillonné.
3. **SVG :** analyse XML, éléments attendus, titre contenant `<`, `&` et guillemets, ruptures effectives, courbe constante, absence totale de points finis.
4. **CLI :** session comportant succès, erreur, nouveau succès, historique, effacement et sortie ; ajouter un chemin de sortie inaccessible.
5. **Livraison :** absence d’exécution dynamique interdite, documentation des conventions et lancement de la commande d’acceptation fournie.

Ces contrôles doivent mesurer les comportements, sans imposer une organisation interne particulière. Aucun outil ni dépôt n’a été consulté et aucun test n’a été exécuté ; le verdict technique reste celui du vérificateur indépendant.
--- END SA-02 INITIAL ---

--- BEGIN SA-01 CONTRADICTION ---
Avis SA-01 — **confirmation avec révisions ciblées**. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge original n’étant pas joint à cet échange, elle ne constitue pas une vérification indépendante de ses exigences.

**Accords et doublons.** Les analyses convergent sur les risques principaux : consommation intégrale de l’expression, langage fermé, priorité et associativité de la puissance, résultats réels finis, exceptions maîtrisées, distinction entre syntaxe invalide et erreur numérique ponctuelle, ruptures effectives du tracé et historique conditionné à la réussite complète. Ces recommandations se recouvrent largement : les regrouper en une seule liste de critères observables évitera de multiplier artificiellement les obligations.

Même convergence sur les limites : aucune garantie de détection des singularités entre échantillons, aucune obligation implicite de calcul symbolique et aucune heuristique de rupture à imposer sans fondement contractuel.

**Désaccords utiles et révisions.**

- La formulation SA-02 « livrable unique `scientific_calculator.py` » mérite correction : mon avis initial mentionne également `README.md`. Parler de **module Python unique accompagné du README** lève cette ambiguïté.
- La séparation des responsabilités et l’analyse unique de l’expression sont de bonnes recommandations internes. Elles ne doivent pas devenir des critères d’acceptation : plusieurs architectures peuvent respecter les mêmes comportements.
- Je confirme la distinction proposée pour `sample_curve`, mais conserve son statut d’**interprétation à documenter**. Notre accord ne transforme pas le rejet préalable d’une syntaxe invalide en exigence explicitement établie.
- Les conventions relatives à `0^-1`, `0^0`, aux clés supplémentaires de `variables`, aux axes hors origine et aux points isolés restent des arbitrages. Leur documentation doit les distinguer des obligations.
- L’expression « abscisses ordonnées » ne devrait pas être durcie en croissance strictement positive entre chaque paire : la précision flottante peut produire des abscisses identiques sur un intervalle très étroit. Les exigences rapportées sur le nombre de points et les bornes restent prioritaires.

**Compléments à conserver.** SA-02 apporte des contrôles utiles sur l’absence d’effets lors de l’import, l’utilisation indépendante des fonctions publiques et le SVG sans aucun point fini. Mon avis ajoute deux surfaces de sécurité peu développées chez SA-02 : les caractères interdits en XML malgré l’échappement classique, et l’épuisement des ressources. Des limites éventuelles doivent être justifiées et documentées, sans inventer de seuil contractuel.

**Priorité des recommandations.**

1. **Conformité et sécurité :** langage fermé, absence d’exécution dynamique, validation complète, exceptions conformes, finitude, XML valide et contenu SVG inerte.
2. **Comportement observable :** échantillonnage conforme, ruptures préservées, géométrie dégénérée maîtrisée, reprise de la CLI après erreur et historique après écriture réussie.
3. **Arbitrages documentés :** conventions numériques, entrées ambiguës, cas limites du SVG et limites de ressources.
4. **Organisation interne :** séparation des responsabilités et réutilisation de l’analyse, sans imposer ces choix au vérificateur.

Aucun outil, fichier, test, opération Git ou délégation utilisé. Les contrôles restent à exécuter par le candidat ; le verdict appartient au vérificateur indépendant.
--- END SA-01 CONTRADICTION ---

--- BEGIN SA-02 CONTRADICTION ---
**Avis SA-02 — confirmation avec révisions ciblées**

Les deux avis convergent sur l’architecture et les risques principaux. Je confirme leurs recommandations communes, avec une réserve : le challenge intégral n’étant pas reproduit dans cet échange, cette confrontation ne vérifie pas indépendamment les obligations qu’ils lui attribuent.

**Accords et doublons**

La séparation entre analyse, évaluation, échantillonnage, SVG et CLI constitue une base cohérente et testable. Elle permet de contrôler chaque fonction publique indépendamment, notamment le SVG avec des points construits directement.

Les recommandations sur la consommation complète de l’expression, la priorité des puissances, les noms autorisés, les résultats finis et les exceptions numériques sont concordantes. Même accord sur les ruptures aux points invalides, l’échappement XML et l’historique alimenté après réussite effective.

Ces sujets représentent des doublons à fusionner dans une seule matrice de validation. Répéter leur justification dans plusieurs documents apporterait peu ; associer chaque invariant à un contrôle observable serait plus utile.

**Révisions et désaccords utiles**

Je corrige ma formulation « livrable unique » : elle devait désigner le module Python unique. SA-01 mentionne également un `README.md` ; la structure interne recommandée ne justifie donc pas de réduire la livraison à un seul fichier.

Je retiens l’apport de SA-01 concernant les caractères interdits en XML : l’échappement de `<`, `&` et des guillemets ne suffit pas à garantir un document valide. La validation doit couvrir cette distinction, avec une convention documentée de rejet ou de traitement.

Je nuance notre formulation commune « erreurs numériques dépendant du point ». Une expression syntaxiquement valide telle que `1/0` peut être invalide à tous les points. La frontière utile sépare les erreurs de langage des erreurs numériques rencontrées pendant l’évaluation ; elle ne doit pas imposer une analyse supplémentaire de dépendance à `x`.

Les propositions concernant `0^-1`, `0^0`, les formes décimales et les axes hors origine restent des conventions à consigner, sous réserve du texte contractuel. Leur accord entre consultants ne les transforme pas en exigences.

Enfin, les limites de ressources et la visibilité d’un point isolé sont des recommandations complémentaires. Des seuils arbitraires pourraient refuser des entrées autrement conformes ; ils ne doivent pas précéder la satisfaction des contrats rapportés.

**Priorité des recommandations**

1. **Conformité centrale :** signatures publiques, import sans effet de bord, langage fermé, précédence, finitude et catégories d’exceptions. Contrôler les comportements sans imposer une représentation interne particulière.
2. **Intégrité du tracé :** nombre de points et bornes, conservation des invalides, ruptures réelles, échelles non dégénérées et coordonnées SVG finies, y compris avec de grandes valeurs.
3. **Validité et interaction :** XML valide et inerte, reprise de la CLI après erreur, absence de succès annoncé ou enregistré après un échec d’écriture.
4. **Conventions et livraison :** documenter les ambiguïtés et les limites de l’échantillonnage, puis exécuter la vérification prescrite. La détection supplémentaire des asymptotes reste facultative selon les deux avis.

Cette réponse est exclusivement consultative : aucun outil, fichier, test, sous-agent ou opération Git mobilisé. Aucun résultat technique n’est établi ; le verdict appartient au vérificateur indépendant.
--- END SA-02 CONTRADICTION ---

````

</details>

````text
Aucune réponse ; interruption par quota.
````
