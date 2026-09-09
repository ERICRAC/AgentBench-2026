# PV multi-agent — astra-medium-scientific-v2-001

## Identification et périmètre

Le commanditaire lance V2 gpt-6-astra/medium. L'orchestrateur expérimental
exécute le relais mécanique et publie après clôture. MAIN est le seul
rôle écrivain. SA-01, SA-02 et SA-03 sont consultants en lecture seule,
sans sous-délégation. Les sept sessions sont neuves et éphémères.

Les textes ci-dessous sont conservés dans l'ordre des phases. Seuls le
préfixe local du dépôt et d'éventuels secrets reconnus sont remplacés ;
aucun raisonnement interne n'est publié.

## Qui est qui ?

- **RELAY** : Orchestrateur expérimental : lance, relaie, mesure et publie.
- **MAIN** : Développeur principal : arbitre et reste le seul écrivain.
- **SA-01** : Sous-agent 1 — analyste exigences et sécurité.
- **SA-02** : Sous-agent 2 — architecte logiciel et testabilité.
- **SA-03** : Sous-agent 3 — relecteur qualité critique, défauts et cas limites.

Sept sessions représentent quatre rôles candidats, pas sept métiers.
Le vérificateur est un programme indépendant, pas un consultant LLM.

## Équipe et métriques

| Session | Rôle / phase | Durée | Entrée | Cache inclus | Sortie | Raisonnement inclus | Mots visibles |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 01-sa01-initial | MSG-001 · analyse indépendante (max 1200) | 55.127 s | 15106 | 0 | 1612 | 0 | 1000 |
| 02-sa02-initial | MSG-002 · analyse indépendante (max 1200) | 54.314 s | 15108 | 9088 | 1590 | 0 | 1031 |
| 03-sa01-cross | MSG-003 · contradiction croisée (max 600) | 28.439 s | 17123 | 4992 | 722 | 0 | 473 |
| 04-sa02-cross | MSG-004 · contradiction croisée (max 600) | 28.315 s | 17125 | 0 | 778 | 0 | 497 |
| 05-main-first | MSG-005 · arbitrage et première solution | 311.551 s | 188709 | 163072 | 9796 | 296 | 195 |
| 06-sa03-critic | MSG-006 · critique adversariale (max 1200) | 48.689 s | 26532 | 9088 | 1402 | 451 | 624 |
| 07-main-final | MSG-007 · arbitrage final et vérification | 204.16 s | 268666 | 222976 | 6113 | 208 | 241 |

Temps mural : **648.008 s**. Somme des temps-sessions : **730.595 s**.

Tokens : **548369 entrée + 22013 sortie = 570382**. Le cache (409216) est inclus dans
l'entrée et le raisonnement (955) dans la sortie.

## Messages visibles — verbatim filtré

### MSG-001 — analyse indépendante

Direction : `RELAY → SA-01 → MAIN`. Réponse visible : 1000 mots sur 1200 maximum.

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
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
````

### MSG-002 — analyse indépendante

Direction : `RELAY → SA-02 → MAIN`. Réponse visible : 1031 mots sur 1200 maximum.

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
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
````

### MSG-003 — contradiction croisée

Direction : `MAIN/RELAY → SA-01 → MAIN`. Réponse visible : 473 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-01 ---
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
--- END YOUR INITIAL SA-01 ---

--- BEGIN PEER INITIAL SA-02 ---
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
--- END PEER INITIAL SA-02 ---
````

</details>

#### Texte retourné pour MSG-003, mot pour mot

````text
Je confirme l’accord principal avec SA-02, avec deux corrections de formulation et un désaccord utile sur les axes. Le challenge original n’étant pas reproduit ici, cette confrontation repose uniquement sur les deux avis ; elle ne permet pas de confirmer indépendamment leurs affirmations contractuelles.

**Accords et doublons.** Nos recommandations convergent sur la grammaire fermée, la consommation intégrale de l’entrée, les précédences, les résultats réels finis, la séparation entre erreurs structurelles et numériques, l’échappement XML, les ruptures de courbe et l’historique après réussite effective. Ces éléments doivent former une seule liste de contrôles. La décomposition proposée par SA-02 précise utilement leur mise en œuvre, sans constituer une obligation d’architecture. L’absence d’effets de bord à l’import et la gestion de la fin d’entrée complètent mon avis.

**Correction prioritaire : appels imbriqués.** La formulation de SA-02 « appels imbriqués non autorisés » est ambiguë. Une composition comme `sin(cos(x))` ne doit pas être assimilée à un appel indirect ou à une construction étrangère. La recommandation doit viser les appels vers des fonctions non autorisées et les formes d’appel étrangères à la grammaire. Une interdiction générale de l’imbrication introduirait une restriction que nos avis ne justifient pas.

**Révision commune : erreurs numériques pendant l’échantillonnage.** « Seuls les échecs numériques dépendant de l’abscisse deviennent `None` » est trop restrictif. Une expression syntaxiquement valide telle que `sqrt(-1)` peut être indéfinie à chaque point sans dépendre de `x`. Il faut distinguer la validité structurelle de l’expression de la réussite numérique de chaque évaluation. Selon le contrat rapporté, l’échantillonnage peut alors produire uniquement des `None`, puis le rendu doit lever `ValueError` faute de point fini. Il ne faut pas exiger une dépendance à `x` pour reconnaître un échec numérique local.

**Désaccord utile : axes hors domaine.** Inclure systématiquement zéro, comme le propose SA-02, peut fortement comprimer une courbe située loin de l’origine et affaiblir l’exigence d’échelle adaptée. Je maintiens une préférence pour des axes placés au bord lorsque zéro est hors champ, avec une convention documentée qui évite de présenter ce bord comme la coordonnée zéro. Les deux choix restent des arbitrages tant que le contrat ne tranche pas.

**Priorités consolidées.**

- **P0 :** empêcher toute exécution ou résolution de noms arbitraire ; garantir un SVG valide sans contenu actif ni référence externe.
- **P1 :** vérifier précédences et exceptions, corriger les deux ambiguïtés ci-dessus, préserver les trous, stabiliser interpolation et projection pour les valeurs extrêmes, puis assurer la reprise CLI après échec.
- **P2 :** documenter les conventions numériques, les axes et les limites scientifiques ; encadrer les ressources sans transformer des plafonds arbitraires en exigences du challenge.

La limite sur les asymptotes est un accord complet : les coupures explicites sont requises, une détection exhaustive ne peut être promise.

Aucun outil, contrôle, changement de fichier ou acte Git effectué. Le candidat conserve l’implémentation ; le vérificateur indépendant conserve le verdict.
````

### MSG-004 — contradiction croisée

Direction : `MAIN/RELAY → SA-02 → MAIN`. Réponse visible : 497 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-02 ---
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
--- END YOUR INITIAL SA-02 ---

--- BEGIN PEER INITIAL SA-01 ---
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
--- END PEER INITIAL SA-01 ---
````

</details>

#### Texte retourné pour MSG-004, mot pour mot

````text
Je confirme l’architecture proposée et l’essentiel de l’avis SA-01, avec deux corrections de mon avis initial et un arbitrage révisé sur les axes. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge lui-même n’est pas reproduit dans ce message.

**Accords et doublons.** Nous convergeons sur l’analyseur fermé, la consommation intégrale des jetons, la précédence des puissances, les résultats flottants finis et la distinction entre erreurs structurelles et échecs numériques d’échantillonnage. Même convergence sur l’échappement XML, les ruptures aux points invalides, l’historique après succès effectif et les limites de détection des discontinuités. Ces doublons doivent former une seule liste de critères d’acceptation, sans multiplier les composants ou les contrôles équivalents.

**Corrections de mon avis initial.**

- La formule « appels imbriqués non autorisés » est trop large : une composition telle que `sin(cos(0))` doit rester permise si chaque appel respecte la grammaire des fonctions autorisées. Ce sont les appels indirects et les constructions étrangères qui doivent être rejetés.
- Un domaine entièrement invalide n’est pas une erreur syntaxique : une expression valide comme `sqrt(-1)` peut produire uniquement des `None` pendant l’échantillonnage. Selon l’obligation rapportée par SA-01, le rendu sans aucun point fini doit ensuite lever `ValueError`. Il faut distinguer explicitement ces deux étapes.

**Désaccord utile : position des axes.** Ma recommandation d’inclure systématiquement zéro peut comprimer fortement une courbe éloignée de l’origine et affaiblir l’exigence d’échelle adaptée. Je privilégie désormais une fenêtre fondée sur les données et des axes ramenés au bord lorsque zéro est hors champ, sous réserve du contrat exact. Cette convention doit être documentée pour éviter qu’un bord soit interprété comme la position réelle de zéro.

**Compléments à retenir avec mesure.** SA-01 apporte deux recommandations utiles : rendre visible un point isolé, qu’une ligne brisée peut laisser invisible, et terminer la validation du SVG avant d’ouvrir le fichier de destination. En revanche, les plafonds de longueur, profondeur ou nombre d’échantillons introduisent des restrictions supplémentaires. Les erreurs de ressources doivent être maîtrisées, mais des plafonds arbitraires ne doivent pas devenir des obligations supposées du défi. Les conventions sur `0^0`, `0^-1` et les booléens restent également des arbitrages tant que le texte contractuel ne les tranche pas.

**Priorités consolidées.**

1. **P0 — Contrat et innocuité :** grammaire fermée, exceptions publiques correctes, séparation syntaxe/calcul, titre sans injection XML et coordonnées finales finies.
2. **P1 — Robustesse observable :** bornes exactement incluses, interpolation et transformations stables, rupture à chaque point invalide, rejet du rendu vide, cas constant et point isolé.
3. **P1 — Continuité de session :** reprise après erreur de calcul ou d’écriture, historique uniquement après réussite.
4. **P2 — Conventions documentées :** axes hors champ, puissances particulières et limites scientifiques.

La validation doit cibler ces comportements publics : expressions représentatives, échantillonnages dégénérés, inspection XML et session CLI avec échec suivi d’un succès. Elle ne doit pas imposer la forme de l’arbre syntaxique ni le découpage interne retenu.

Aucun outil utilisé, contrôle exécuté, fichier modifié ou acte Git effectué. Le verdict appartient au vérificateur indépendant.
````

### MSG-005 — arbitrage et première solution

Direction : `RELAY → MAIN`. Réponse visible : 195 mots.

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
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
--- END SA-01 INITIAL ---

--- BEGIN SA-02 INITIAL ---
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
--- END SA-02 INITIAL ---

--- BEGIN SA-01 CONTRADICTION ---
Je confirme l’accord principal avec SA-02, avec deux corrections de formulation et un désaccord utile sur les axes. Le challenge original n’étant pas reproduit ici, cette confrontation repose uniquement sur les deux avis ; elle ne permet pas de confirmer indépendamment leurs affirmations contractuelles.

**Accords et doublons.** Nos recommandations convergent sur la grammaire fermée, la consommation intégrale de l’entrée, les précédences, les résultats réels finis, la séparation entre erreurs structurelles et numériques, l’échappement XML, les ruptures de courbe et l’historique après réussite effective. Ces éléments doivent former une seule liste de contrôles. La décomposition proposée par SA-02 précise utilement leur mise en œuvre, sans constituer une obligation d’architecture. L’absence d’effets de bord à l’import et la gestion de la fin d’entrée complètent mon avis.

**Correction prioritaire : appels imbriqués.** La formulation de SA-02 « appels imbriqués non autorisés » est ambiguë. Une composition comme `sin(cos(x))` ne doit pas être assimilée à un appel indirect ou à une construction étrangère. La recommandation doit viser les appels vers des fonctions non autorisées et les formes d’appel étrangères à la grammaire. Une interdiction générale de l’imbrication introduirait une restriction que nos avis ne justifient pas.

**Révision commune : erreurs numériques pendant l’échantillonnage.** « Seuls les échecs numériques dépendant de l’abscisse deviennent `None` » est trop restrictif. Une expression syntaxiquement valide telle que `sqrt(-1)` peut être indéfinie à chaque point sans dépendre de `x`. Il faut distinguer la validité structurelle de l’expression de la réussite numérique de chaque évaluation. Selon le contrat rapporté, l’échantillonnage peut alors produire uniquement des `None`, puis le rendu doit lever `ValueError` faute de point fini. Il ne faut pas exiger une dépendance à `x` pour reconnaître un échec numérique local.

**Désaccord utile : axes hors domaine.** Inclure systématiquement zéro, comme le propose SA-02, peut fortement comprimer une courbe située loin de l’origine et affaiblir l’exigence d’échelle adaptée. Je maintiens une préférence pour des axes placés au bord lorsque zéro est hors champ, avec une convention documentée qui évite de présenter ce bord comme la coordonnée zéro. Les deux choix restent des arbitrages tant que le contrat ne tranche pas.

**Priorités consolidées.**

- **P0 :** empêcher toute exécution ou résolution de noms arbitraire ; garantir un SVG valide sans contenu actif ni référence externe.
- **P1 :** vérifier précédences et exceptions, corriger les deux ambiguïtés ci-dessus, préserver les trous, stabiliser interpolation et projection pour les valeurs extrêmes, puis assurer la reprise CLI après échec.
- **P2 :** documenter les conventions numériques, les axes et les limites scientifiques ; encadrer les ressources sans transformer des plafonds arbitraires en exigences du challenge.

La limite sur les asymptotes est un accord complet : les coupures explicites sont requises, une détection exhaustive ne peut être promise.

Aucun outil, contrôle, changement de fichier ou acte Git effectué. Le candidat conserve l’implémentation ; le vérificateur indépendant conserve le verdict.
--- END SA-01 CONTRADICTION ---

--- BEGIN SA-02 CONTRADICTION ---
Je confirme l’architecture proposée et l’essentiel de l’avis SA-01, avec deux corrections de mon avis initial et un arbitrage révisé sur les axes. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge lui-même n’est pas reproduit dans ce message.

**Accords et doublons.** Nous convergeons sur l’analyseur fermé, la consommation intégrale des jetons, la précédence des puissances, les résultats flottants finis et la distinction entre erreurs structurelles et échecs numériques d’échantillonnage. Même convergence sur l’échappement XML, les ruptures aux points invalides, l’historique après succès effectif et les limites de détection des discontinuités. Ces doublons doivent former une seule liste de critères d’acceptation, sans multiplier les composants ou les contrôles équivalents.

**Corrections de mon avis initial.**

- La formule « appels imbriqués non autorisés » est trop large : une composition telle que `sin(cos(0))` doit rester permise si chaque appel respecte la grammaire des fonctions autorisées. Ce sont les appels indirects et les constructions étrangères qui doivent être rejetés.
- Un domaine entièrement invalide n’est pas une erreur syntaxique : une expression valide comme `sqrt(-1)` peut produire uniquement des `None` pendant l’échantillonnage. Selon l’obligation rapportée par SA-01, le rendu sans aucun point fini doit ensuite lever `ValueError`. Il faut distinguer explicitement ces deux étapes.

**Désaccord utile : position des axes.** Ma recommandation d’inclure systématiquement zéro peut comprimer fortement une courbe éloignée de l’origine et affaiblir l’exigence d’échelle adaptée. Je privilégie désormais une fenêtre fondée sur les données et des axes ramenés au bord lorsque zéro est hors champ, sous réserve du contrat exact. Cette convention doit être documentée pour éviter qu’un bord soit interprété comme la position réelle de zéro.

**Compléments à retenir avec mesure.** SA-01 apporte deux recommandations utiles : rendre visible un point isolé, qu’une ligne brisée peut laisser invisible, et terminer la validation du SVG avant d’ouvrir le fichier de destination. En revanche, les plafonds de longueur, profondeur ou nombre d’échantillons introduisent des restrictions supplémentaires. Les erreurs de ressources doivent être maîtrisées, mais des plafonds arbitraires ne doivent pas devenir des obligations supposées du défi. Les conventions sur `0^0`, `0^-1` et les booléens restent également des arbitrages tant que le texte contractuel ne les tranche pas.

**Priorités consolidées.**

1. **P0 — Contrat et innocuité :** grammaire fermée, exceptions publiques correctes, séparation syntaxe/calcul, titre sans injection XML et coordonnées finales finies.
2. **P1 — Robustesse observable :** bornes exactement incluses, interpolation et transformations stables, rupture à chaque point invalide, rejet du rendu vide, cas constant et point isolé.
3. **P1 — Continuité de session :** reprise après erreur de calcul ou d’écriture, historique uniquement après réussite.
4. **P2 — Conventions documentées :** axes hors champ, puissances particulières et limites scientifiques.

La validation doit cibler ces comportements publics : expressions représentatives, échantillonnages dégénérés, inspection XML et session CLI avec échec suivi d’un succès. Elle ne doit pas imposer la forme de l’arbre syntaxique ni le découpage interne retenu.

Aucun outil utilisé, contrôle exécuté, fichier modifié ou acte Git effectué. Le verdict appartient au vérificateur indépendant.
--- END SA-02 CONTRADICTION ---
````

</details>

#### Texte retourné pour MSG-005, mot pour mot

````text
Je vais lire le challenge de la tentative, consigner les arbitrages avant de coder, puis réaliser et contrôler la première solution. Le vérificateur officiel restera réservé à la phase finale, après la critique SA-03.


La table d’arbitrage est écrite. Je retiens notamment les compositions de fonctions, les trous numériques même pour une expression constante, et les axes au bord lorsque zéro est hors champ. Le moteur séparera l’analyse syntaxique du calcul pour analyser chaque courbe une seule fois.


Le moteur, le SVG et la CLI sont implémentés et documentés. Je passe aux contrôles ciblés : précédence, erreurs, ruptures de courbe, valeurs extrêmes, titre XML hostile et reprise de session après erreur. Le vérificateur officiel n’a pas été lancé.


Première solution complète, documentée et prête pour SA-03.

- [DECISIONS.md](DECISIONS.md) : arbitrages motivés des quatre avis, écrits avant le code.
- [scientific_calculator.py](scientific_calculator.py) : moteur, échantillonnage, SVG et CLI.
- [README.md](README.md) : utilisation, conventions et limites.
- [CONTROLES.md](CONTROLES.md) : trace des contrôles — **131 assertions ciblées réussies**.

Aucun autre agent lancé, aucune opération Git effectuée. Le vérificateur officiel n’a pas été exécuté, conformément à la frontière de phase. La critique SA-03 et le verdict indépendant restent à venir.
````

### MSG-006 — critique adversariale

Direction : `MAIN/RELAY → SA-03 → MAIN`. Réponse visible : 624 mots sur 1200 maximum.

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
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
Je confirme l’accord principal avec SA-02, avec deux corrections de formulation et un désaccord utile sur les axes. Le challenge original n’étant pas reproduit ici, cette confrontation repose uniquement sur les deux avis ; elle ne permet pas de confirmer indépendamment leurs affirmations contractuelles.

**Accords et doublons.** Nos recommandations convergent sur la grammaire fermée, la consommation intégrale de l’entrée, les précédences, les résultats réels finis, la séparation entre erreurs structurelles et numériques, l’échappement XML, les ruptures de courbe et l’historique après réussite effective. Ces éléments doivent former une seule liste de contrôles. La décomposition proposée par SA-02 précise utilement leur mise en œuvre, sans constituer une obligation d’architecture. L’absence d’effets de bord à l’import et la gestion de la fin d’entrée complètent mon avis.

**Correction prioritaire : appels imbriqués.** La formulation de SA-02 « appels imbriqués non autorisés » est ambiguë. Une composition comme `sin(cos(x))` ne doit pas être assimilée à un appel indirect ou à une construction étrangère. La recommandation doit viser les appels vers des fonctions non autorisées et les formes d’appel étrangères à la grammaire. Une interdiction générale de l’imbrication introduirait une restriction que nos avis ne justifient pas.

**Révision commune : erreurs numériques pendant l’échantillonnage.** « Seuls les échecs numériques dépendant de l’abscisse deviennent `None` » est trop restrictif. Une expression syntaxiquement valide telle que `sqrt(-1)` peut être indéfinie à chaque point sans dépendre de `x`. Il faut distinguer la validité structurelle de l’expression de la réussite numérique de chaque évaluation. Selon le contrat rapporté, l’échantillonnage peut alors produire uniquement des `None`, puis le rendu doit lever `ValueError` faute de point fini. Il ne faut pas exiger une dépendance à `x` pour reconnaître un échec numérique local.

**Désaccord utile : axes hors domaine.** Inclure systématiquement zéro, comme le propose SA-02, peut fortement comprimer une courbe située loin de l’origine et affaiblir l’exigence d’échelle adaptée. Je maintiens une préférence pour des axes placés au bord lorsque zéro est hors champ, avec une convention documentée qui évite de présenter ce bord comme la coordonnée zéro. Les deux choix restent des arbitrages tant que le contrat ne tranche pas.

**Priorités consolidées.**

- **P0 :** empêcher toute exécution ou résolution de noms arbitraire ; garantir un SVG valide sans contenu actif ni référence externe.
- **P1 :** vérifier précédences et exceptions, corriger les deux ambiguïtés ci-dessus, préserver les trous, stabiliser interpolation et projection pour les valeurs extrêmes, puis assurer la reprise CLI après échec.
- **P2 :** documenter les conventions numériques, les axes et les limites scientifiques ; encadrer les ressources sans transformer des plafonds arbitraires en exigences du challenge.

La limite sur les asymptotes est un accord complet : les coupures explicites sont requises, une détection exhaustive ne peut être promise.

Aucun outil, contrôle, changement de fichier ou acte Git effectué. Le candidat conserve l’implémentation ; le vérificateur indépendant conserve le verdict.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
Je confirme l’architecture proposée et l’essentiel de l’avis SA-01, avec deux corrections de mon avis initial et un arbitrage révisé sur les axes. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge lui-même n’est pas reproduit dans ce message.

**Accords et doublons.** Nous convergeons sur l’analyseur fermé, la consommation intégrale des jetons, la précédence des puissances, les résultats flottants finis et la distinction entre erreurs structurelles et échecs numériques d’échantillonnage. Même convergence sur l’échappement XML, les ruptures aux points invalides, l’historique après succès effectif et les limites de détection des discontinuités. Ces doublons doivent former une seule liste de critères d’acceptation, sans multiplier les composants ou les contrôles équivalents.

**Corrections de mon avis initial.**

- La formule « appels imbriqués non autorisés » est trop large : une composition telle que `sin(cos(0))` doit rester permise si chaque appel respecte la grammaire des fonctions autorisées. Ce sont les appels indirects et les constructions étrangères qui doivent être rejetés.
- Un domaine entièrement invalide n’est pas une erreur syntaxique : une expression valide comme `sqrt(-1)` peut produire uniquement des `None` pendant l’échantillonnage. Selon l’obligation rapportée par SA-01, le rendu sans aucun point fini doit ensuite lever `ValueError`. Il faut distinguer explicitement ces deux étapes.

**Désaccord utile : position des axes.** Ma recommandation d’inclure systématiquement zéro peut comprimer fortement une courbe éloignée de l’origine et affaiblir l’exigence d’échelle adaptée. Je privilégie désormais une fenêtre fondée sur les données et des axes ramenés au bord lorsque zéro est hors champ, sous réserve du contrat exact. Cette convention doit être documentée pour éviter qu’un bord soit interprété comme la position réelle de zéro.

**Compléments à retenir avec mesure.** SA-01 apporte deux recommandations utiles : rendre visible un point isolé, qu’une ligne brisée peut laisser invisible, et terminer la validation du SVG avant d’ouvrir le fichier de destination. En revanche, les plafonds de longueur, profondeur ou nombre d’échantillons introduisent des restrictions supplémentaires. Les erreurs de ressources doivent être maîtrisées, mais des plafonds arbitraires ne doivent pas devenir des obligations supposées du défi. Les conventions sur `0^0`, `0^-1` et les booléens restent également des arbitrages tant que le texte contractuel ne les tranche pas.

**Priorités consolidées.**

1. **P0 — Contrat et innocuité :** grammaire fermée, exceptions publiques correctes, séparation syntaxe/calcul, titre sans injection XML et coordonnées finales finies.
2. **P1 — Robustesse observable :** bornes exactement incluses, interpolation et transformations stables, rupture à chaque point invalide, rejet du rendu vide, cas constant et point isolé.
3. **P1 — Continuité de session :** reprise après erreur de calcul ou d’écriture, historique uniquement après réussite.
4. **P2 — Conventions documentées :** axes hors champ, puissances particulières et limites scientifiques.

La validation doit cibler ces comportements publics : expressions représentatives, échantillonnages dégénérés, inspection XML et session CLI avec échec suivi d’un succès. Elle ne doit pas imposer la forme de l’arbre syntaxique ni le découpage interne retenu.

Aucun outil utilisé, contrôle exécuté, fichier modifié ou acte Git effectué. Le verdict appartient au vérificateur indépendant.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION ---

--- BEGIN FILE solution/CONTROLES.md ---
# Contrôles candidats — première solution

## Échange 001 — mandat et avis

Demande : préparer une première solution complète avant SA-03, en V2 gouvernée.
MAIN, candidat et unique écrivain, a lu le CHALLENGE.md actif et les quatre avis
fournis par l'orchestrateur expérimental. Aucun autre agent n'a été lancé.
L'ordre des messages sources est enregistré dans DECISIONS.md ; leurs textes
visibles intégraux restent dans le message de relais, sans réécriture par MAIN.
L'orchestrateur expérimental conserve la production du PV et de son annexe.

## Échange 002 — réalisation

DECISIONS.md a été créé avant scientific_calculator.py et README.md.
Les désaccords et corrections ont été arbitrés explicitement : compositions
permises, domaines entièrement invalides échantillonnés en None, axes au bord,
limite de longueur documentée, aucune heuristique d'asymptote.

## Échange 003 — contrôles ciblés

Commande candidate exécutée dans solution :
`PYTHONDONTWRITEBYTECODE=1 python3 -` avec un programme de contrôle fourni sur
l'entrée standard (bibliothèque standard, assertions, mock de l'entrée CLI et
parseur XML). Le programme de contrôle n'est pas une suite indépendante figée.

Sortie capturée :

```text
131 assertions ciblées réussies ; aucun vérificateur officiel lancé.
```

Code de sortie : 0.

Couverture observée :

- Précédence, associativité, exposants signés, constantes, toutes les fonctions,
  compositions et notation scientifique ; type float et résultats attendus.
- Rejet de syntaxe étrangère, appels indirects, noms arbitraires, caractères
  numériques non ASCII, entrées vides et suffixes ; domaines, overflow,
  variable absente/non finie et division par zéro.
- Longueur excessive et profondeur excessive converties en ValueError.
- Bornes exactes, point central de 1/x, domaine partiel de sqrt(x), domaine
  entièrement invalide, expression structurellement invalide, paramètres rejetés.
- Interpolation finie de -1.7e308 à 1.7e308.
- SVG parsé en XML, deux axes line, deux segments séparés pour 1/x,
  titre hostile conservé comme texte et contrôles XML remplacés, aucun script.
- Projections extrêmes, sous-normales, plage constante, abscisses constantes,
  points isolés et trous ; attributs de coordonnées contrôlés finis.
- Aucun point fini : ValueError sans altérer le fichier préexistant.
- CLI simulée : succès, erreur numérique, succès, échec d'écriture, tracé réussi,
  historique des seules réussites, effacement, sortie et EOF.
- Inspection syntaxique du source : aucun appel à eval, exec ou compile.

L'artefact temporaire `_controle.svg`, créé exclusivement dans solution, a été
supprimé après les contrôles. Aucun fichier du challenge, des tests, des scripts
ou de la gouvernance n'a été modifié. Aucun défaut n'a été révélé par ces
contrôles ; aucune correction consécutive à un échec n'a été nécessaire.

## Échange 004 — frontière de phase

Première solution prête à être transmise à SA-03 par l'orchestrateur
expérimental. Aucun avis SA-03 reçu et aucune vérification officielle exécutée.
Le verdict indépendant reste ouvert. Après la critique, la phase finale devra
arbitrer ses recommandations, corriger les défauts confirmés et exécuter la
commande exacte documentée dans README.md.

Aucune opération Git effectuée. Tokens et durée globale : non enregistrés.
Les contrôles candidats ne garantissent ni la couverture exhaustive ni le
résultat du vérificateur indépendant. Aucun visuel éditorial public produit ;
le SVG livré est un artefact autonome à fond blanc explicite.

--- END FILE solution/CONTROLES.md ---

--- BEGIN FILE solution/DECISIONS.md ---
# Arbitrages MAIN — première solution

Le candidat MAIN est l'unique écrivain. L'orchestrateur expérimental a fourni
les avis consultatifs en lecture seule ; aucun agent supplémentaire n'est lancé.
Le challenge actif a été lu avant cette table, elle-même écrite avant le code.

Ordre des textes visibles reçus, conservés intégralement dans le message source
pour l'annexe verbatim du PV de l'orchestrateur expérimental :
1. SA-01 INITIAL — contrat et sécurité.
2. SA-02 INITIAL — conception et testabilité.
3. SA-01 CONTRADICTION — confrontation et corrections.
4. SA-02 CONTRADICTION — confrontation et révision.

I = avis initial ; C = contradiction. Les recommandations communes sont regroupées.

| Source | Recommandation | Décision motivée |
|---|---|---|
| SA-01 I, SA-02 I | Bibliothèque standard, grammaire fermée, consommation totale, aucune exécution dynamique | Retenue : lexeur dédié et analyse descendante ; aucune résolution libre de nom. |
| SA-01 I | Livrer uniquement moteur et README | Adaptée : ces livrables plus DECISIONS et traces de contrôles dans solution, demandés par le protocole MAIN. |
| SA-02 I | Séparer syntaxe, calcul, échantillonnage, SVG, CLI ; import sans effet | Retenue : représentation postfixée interne, exécution numérique itérative, garde main. |
| SA-01 I, SA-02 I | Puissance à droite, précédence sur unaire, exposant signé | Retenue : grammaire unary → signe unary ou power ; power → primary [^ unary]. |
| SA-01 I, SA-02 I | Décimaux .5 et 5., exposants signés, chiffres ASCII | Retenue : formes usuelles explicites ; rejet des autres caractères et suffixes. |
| SA-01 I, SA-02 I/C, SA-01 C | Fonctions à un argument, compositions autorisées ; pas d'appel indirect ni multiplication implicite | Retenue avec correction des avis initiaux : sin(cos(x)) est valide. |
| SA-01 I, SA-02 I | Seul x est variable ; constantes non redéfinissables | Retenue : clés inutilisées ignorées, valeur de x contrôlée uniquement si utilisée. |
| SA-01 I, SA-02 I | Float réel fini ; division par zéro distincte ; overflow en ValueError | Retenue : contrôle après chaque opération ; math.pow refuse les complexes. |
| SA-01 I, SA-02 I/C | Conventions 0^0, 0^-1, tan aux pôles | Retenue : 1, ValueError, et comportement math.tan sans seuil artificiel. |
| SA-01 I, SA-02 I/C, SA-01 C | Analyser une fois ; distinguer structure invalide et échec numérique | Retenue avec correction : sqrt(-1) produit tous les points à None, même sans dépendance à x. |
| SA-01 I, SA-02 I | Bornes finies croissantes, entier ≥ 2, booléens rejetés | Retenue : diagnostics explicites et contrat numérique sans ambiguïté. |
| SA-02 I, SA-01 C | Extrémités exactes et interpolation stable | Retenue : interpolation convexe si signes opposés ; différence sinon ; bornes assignées exactement. |
| SA-01 I/C, SA-02 I/C | Ne pas promettre toutes les asymptotes | Retenue : coupures sur points invalides ; heuristique de saut écartée car elle peut couper une fonction continue. |
| SA-01 I, SA-02 I/C | XML échappé, caractères interdits traités, coordonnées finies, aucun contenu actif | Retenue : structure SVG fixe et sérialisation XML standard ; remplacement des caractères XML interdits. |
| SA-01 I, SA-02 I/C | Échelles stables, marges, constantes, points isolés, rendu vide refusé | Retenue : normalisation avant soustraction, plage constante centrée, cercle isolé. |
| SA-02 I | Inclure zéro dans toute fenêtre | Écartée suivant SA-01 I/C et SA-02 C : compression excessive des données éloignées. |
| SA-01 I/C, SA-02 C | Axes ramenés au bord | Retenue : position bornée ; légende explicite si origine hors champ. |
| SA-01 I, SA-02 C | Limites de ressources raisonnables | Adaptée : longueur maximale 10 000 caractères et profondeur de syntaxe limitée par Python, convertie en ValueError ; pas de plafond arbitraire d'échantillons. Calcul float et pile numérique itérative. Limites documentées. |
| SA-01 I, SA-02 I/C | Valider document avant ouverture ; erreurs de chemin récupérables | Retenue : document entièrement construit avant écriture et OSError présenté par CLI. |
| SA-01 I, SA-02 I/C | Historique ordonné des réussites ; EOF et reprise après erreur | Retenue : ajout après succès, commandes de contrôle exclues, EOF propre. |
| Tous | Contrôles publics ciblés et documentation des conventions | Retenue : précédence, refus, domaines, SVG extrême et hostile, CLI ; aucun test de forme interne. |
| SA-01 I, SA-02 I | Vérificateur indépendant et corrections | Différée conformément à la phase : uniquement après SA-03 ; aucun verdict officiel revendiqué ici. |

## Trace synthétique

1. Demande : première solution V2, arbitrages préalables, aucun autre consultant.
2. Avis : quatre textes reçus dans l'ordre ci-dessus ; les consultants déclarent
   n'avoir utilisé aucun outil ni exécuté de contrôle.
3. Arbitrage : table ci-dessus ; code et contrôles candidats viennent ensuite.
4. SA-03 et vérification officielle : non exécutés dans cette phase.

Tokens et durée totale des consultants et du candidat : non enregistrés.
Aucune modification de gouvernance ; aucune opération Git autorisée dans ce run.

--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Calculatrice scientifique — première solution V2

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

Les expressions sont limitées à 10 000 caractères. Une imbrication dépassant
la limite de récursion Python devient `ValueError`. Les calculs utilisent une
pile itérative de flottants. Aucun plafond de `samples` supplémentaire n'est
imposé ; mémoire et temps croissent avec le nombre de points et la taille de
l'expression. L'import du module ne lance pas la CLI et ne crée aucun fichier.

## Validation et protocole

Les arbitrages consultatifs figurent dans `DECISIONS.md`. La première solution
est destinée à la critique SA-03. Les contrôles candidats sont décrits dans
`CONTROLES.md` ; ils ne constituent pas le verdict indépendant.

La commande officielle, **réservée à la phase finale après SA-03**, depuis la
racine du dépôt, est :

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-001/solution
```

--- END FILE solution/README.md ---

--- BEGIN FILE solution/scientific_calculator.py ---
"""Calculatrice scientifique sûre, échantillonnage et SVG (Python >= 3.10)."""

import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path


_FUNCTIONS = {name: getattr(math, name) for name in (
    'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'log10', 'exp'
)}
_FUNCTIONS.update(ln=math.log, abs=abs)
_CONSTANTS = {'pi': math.pi, 'e': math.e}
_NUMBER = r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?'
_MAX_LENGTH = 10_000


def _tokens(expression):
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError('Expression vide ou non textuelle.')
    if len(expression) > _MAX_LENGTH:
        raise ValueError('Expression trop longue (maximum 10 000 caractères).')
    result = []
    position = 0
    while position < len(expression):
        char = expression[position]
        if char.isspace():
            position += 1
            continue
        match = re.match(_NUMBER, expression[position:])
        if match:
            result.append(('number', match.group()))
            position += len(match.group())
            continue
        match = re.match(r'[A-Za-z_][A-Za-z_0-9]*', expression[position:])
        if match:
            result.append(('name', match.group()))
            position += len(match.group())
            continue
        if char in '+-*/^()':
            result.append((char, char))
            position += 1
            continue
        raise ValueError(f'Caractère interdit à la position {position + 1}.')
    return result + [('end', '')]


class _Parser:
    """Analyse descendante émettant des instructions postfixées fermées."""

    def __init__(self, expression):
        self.tokens = _tokens(expression)
        self.index = 0
        self.code = []

    def accept(self, kind):
        if self.tokens[self.index][0] == kind:
            self.index += 1
            return True
        return False

    def require(self, kind):
        if not self.accept(kind):
            raise ValueError(f'Syntaxe incorrecte : {kind} attendu.')

    def expression(self):
        self.term()
        while self.tokens[self.index][0] in ('+', '-'):
            op = self.tokens[self.index][0]
            self.index += 1
            self.term()
            self.code.append(('binary', op))

    def term(self):
        self.unary()
        while self.tokens[self.index][0] in ('*', '/'):
            op = self.tokens[self.index][0]
            self.index += 1
            self.unary()
            self.code.append(('binary', op))

    def unary(self):
        if self.accept('+'):
            self.unary()
        elif self.accept('-'):
            self.unary()
            self.code.append(('negative', None))
        else:
            self.power()

    def power(self):
        self.primary()
        if self.accept('^'):
            self.unary()
            self.code.append(('binary', '^'))

    def primary(self):
        kind, value = self.tokens[self.index]
        if self.accept('number'):
            self.code.append(('number', value))
        elif self.accept('name'):
            if value in _FUNCTIONS:
                self.require('(')
                self.expression()
                self.require(')')
                self.code.append(('function', value))
            elif value in _CONSTANTS:
                self.code.append(('number', _CONSTANTS[value]))
            elif value == 'x':
                self.code.append(('variable', 'x'))
            else:
                raise ValueError(f'Nom inconnu : {value}.')
        elif self.accept('('):
            self.expression()
            self.require(')')
        else:
            raise ValueError('Syntaxe incorrecte : nombre, fonction ou parenthèse attendu.')


def _parse(expression):
    try:
        parser = _Parser(expression)
        parser.expression()
        parser.require('end')
        return parser.code
    except RecursionError:
        raise ValueError('Expression trop profondément imbriquée.') from None


def _finite(value):
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Un nombre réel fini est requis.') from None
    if not math.isfinite(result):
        raise ValueError('Résultat non fini ou dépassement numérique.')
    return result


def _calculate(code, variables):
    stack = []
    try:
        for kind, value in code:
            if kind == 'number':
                result = _finite(value)
            elif kind == 'variable':
                if variables is None or 'x' not in variables:
                    raise ValueError('La variable x nécessite une valeur.')
                result = _finite(variables['x'])
            elif kind == 'negative':
                result = -stack.pop()
            elif kind == 'function':
                result = _FUNCTIONS[value](stack.pop())
            else:
                right, left = stack.pop(), stack.pop()
                if value == '+':
                    result = left + right
                elif value == '-':
                    result = left - right
                elif value == '*':
                    result = left * right
                elif value == '/':
                    if right == 0:
                        raise ZeroDivisionError('Division par zéro.')
                    result = left / right
                else:
                    result = math.pow(left, right)
            stack.append(_finite(result))
    except OverflowError:
        raise ValueError('Dépassement numérique.') from None
    except ValueError as error:
        raise ValueError(f'Calcul invalide dans le domaine réel : {error}') from None
    return stack[0]


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Évalue la grammaire fermée ; retourne un float fini ou une erreur."""
    if variables is not None and not isinstance(variables, dict):
        raise ValueError('Les variables doivent être un dictionnaire.')
    return _calculate(_parse(expression), variables)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Inclut les bornes exactes ; chaque échec numérique devient None."""
    if isinstance(x_min, bool) or isinstance(x_max, bool):
        raise ValueError('Les bornes doivent être des nombres réels, pas des booléens.')
    low, high = _finite(x_min), _finite(x_max)
    if low >= high:
        raise ValueError('Il faut x_min < x_max.')
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError('samples doit être un entier supérieur ou égal à 2.')
    code = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        if index == 0:
            x = low
        elif index == samples - 1:
            x = high
        elif low < 0 < high:
            x = (1 - fraction) * low + fraction * high
        else:
            x = low + fraction * (high - low)
        try:
            y = _calculate(code, {'x': x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def _projection(values, start, end):
    """Normaliser avant soustraction évite les étendues infinies."""
    low, high = min(values), max(values)
    if low == high:
        def constant(value):
            return (start + end) / 2 if value == low else (start if value < low else end)
        return constant, low, high
    scale = max(abs(low), abs(high))
    lo, hi = low / scale, high / scale

    def project(value):
        if value <= low:
            return start
        if value >= high:
            return end
        ratio = (value / scale - lo) / (hi - lo)
        return start + ratio * (end - start)

    return project, low, high


def _xml_text(text):
    """Remplace les caractères interdits en XML 1.0 avant sérialisation."""
    return ''.join(char if (ord(char) in (9, 10, 13)
                           or 0x20 <= ord(char) <= 0xD7FF
                           or 0xE000 <= ord(char) <= 0xFFFD
                           or 0x10000 <= ord(char) <= 0x10FFFF)
                   else '\uFFFD' for char in str(text))


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = '',
) -> None:
    """Écrit un SVG autonome ; une coordonnée invalide coupe le segment."""
    cleaned = []
    for point in points:
        try:
            x, y = point
            cleaned.append((_finite(x), _finite(y)))
        except (ValueError, TypeError):
            cleaned.append(None)
    finite = [point for point in cleaned if point is not None]
    if not finite:
        raise ValueError('Aucun point fini à tracer.')
    px, xmin, xmax = _projection([p[0] for p in finite], 60, 760)
    py, ymin, ymax = _projection([p[1] for p in finite], 440, 60)
    root = ET.Element('svg', xmlns='http://www.w3.org/2000/svg',
                      width='800', height='500', viewBox='0 0 800 500')
    ET.SubElement(root, 'title').text = _xml_text(title)
    ET.SubElement(root, 'rect', x='0', y='0', width='800', height='500', fill='white')
    ET.SubElement(root, 'text', x='60', y='28', fill='#111111').text = _xml_text(title)
    ET.SubElement(root, 'line', x1='60', y1=str(py(0)), x2='760', y2=str(py(0)),
                  stroke='#666666')
    ET.SubElement(root, 'line', x1=str(px(0)), y1='60', x2=str(px(0)), y2='440',
                  stroke='#666666')

    def draw(segment):
        if len(segment) == 1:
            x, y = segment[0]
            ET.SubElement(root, 'circle', cx=f'{px(x):.8f}', cy=f'{py(y):.8f}',
                          r='3', fill='#145aca')
        elif segment:
            coordinates = ' '.join(f'{px(x):.8f},{py(y):.8f}' for x, y in segment)
            ET.SubElement(root, 'polyline', points=coordinates, fill='none',
                          stroke='#145aca', **{'stroke-width': '2'})

    segment = []
    for point in cleaned:
        if point is None:
            draw(segment)
            segment = []
        else:
            segment.append(point)
    draw(segment)
    legend = f'x : [{xmin:.6g}, {xmax:.6g}] ; y : [{ymin:.6g}, {ymax:.6g}]'
    ET.SubElement(root, 'text', x='60', y='468', fill='#111111').text = legend
    if not xmin <= 0 <= xmax or not ymin <= 0 <= ymax:
        ET.SubElement(root, 'text', x='60', y='490', fill='#111111').text = (
            'Origine hors champ : axe correspondant au bord, sans représenter zéro.')
    document = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    Path(output_path).write_bytes(document)


_HELP = """Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Exemple : sqrt(2) ^ 2 ; la variable x est réservée aux tracés dans la CLI.
Tracé : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit."""


def main() -> None:
    """Boucle interactive ; historique des seules opérations réussies."""
    history = []
    while True:
        try:
            line = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line:
            continue
        if line in ('quit', 'exit'):
            return
        if line == 'help':
            print(_HELP)
            continue
        if line == 'history':
            print('\n'.join(f'{i}. {entry}' for i, entry in enumerate(history, 1))
                  or 'Historique vide.')
            continue
        if line == 'clear':
            history.clear()
            print('Historique effacé.')
            continue
        try:
            if line.split(maxsplit=1)[0] == 'plot':
                parts = [part.strip() for part in line[4:].split(';')]
                if len(parts) != 4 or not all(parts):
                    raise ValueError('Syntaxe : plot expression; minimum; maximum; fichier.svg')
                expression, low, high, output = parts
                points = sample_curve(expression, evaluate(low), evaluate(high))
                write_svg(points, output, title=expression)
                print(f'Courbe enregistrée dans {output}')
            else:
                print(evaluate(line))
            history.append(line)
        except (ValueError, ZeroDivisionError, OSError, MemoryError) as error:
            print(f'Erreur : {error or "ressources insuffisantes"}')
        except KeyboardInterrupt:
            print('Opération interrompue.')


if __name__ == '__main__':
    main()

--- END FILE solution/scientific_calculator.py ---

--- END FIRST SOLUTION ---
````

</details>

#### Texte retourné pour MSG-006, mot pour mot

````text
La lecture statique ne révèle pas d’exécution arbitraire, d’injection XML ni d’erreur manifeste de précédence. Les corrections issues des consultations sont effectivement présentes : compositions autorisées, séparation syntaxe/calcul, domaines entièrement invalides convertis en `None`, ruptures explicites et historique ajouté après réussite.

**Défaut confirmé — restriction supplémentaire du langage.** `_tokens` refuse toute expression dépassant 10 000 caractères, même grammaticalement valide. Une somme de 5 001 termes `1`, séparés par `+`, dépasse cette limite alors que son résultat est fini. La profondeur de récursion impose également une restriction sur des parenthèses ou signes unaires valides. Ces restrictions sont arbitrées et documentées, mais le challenge figé ne les prévoit pas : la documentation ne suffit donc pas à établir leur conformité. Leur incidence sur l’acceptation reste inconnue. Il faut conserver explicitement cet écart dans l’arbitrage final, sans le présenter comme une exigence du défi.

**Risques à examiner avant clôture :**

- **Échappement du terminal absent.** Le SVG protège correctement son titre, mais la CLI réaffiche directement le chemin de sortie et les entrées d’historique. Un chemin contenant des séquences de contrôle, accepté notamment sur un système POSIX, peut donc modifier l’affichage du terminal lors du message de réussite ou de `history`. C’est un risque distinct de l’injection SVG ; son exploitation dépend du terminal et de la provenance des commandes. Aucun mécanisme d’exécution système n’est démontré.

- **Récupération CLI partielle.** Le bloc entourant `input()` intercepte seulement `EOFError` et `KeyboardInterrupt`. Une erreur de lecture telle qu’un `OSError`, ou un manque de mémoire pendant la lecture, échappe donc au traitement prévu pour les opérations. Les sorties de `help`, `history` et `clear` sont également hors de ce traitement. Cela fragilise la promesse générale « toute erreur […] sans traceback », même si la récupération après perte du canal d’entrée ou de sortie peut être impossible. Les contrôles rapportés couvrent EOF, mais pas ces défaillances.

- **Ressources non bornées pour l’API de tracé.** `sample_curve` accepte tout entier d’échantillonnage supérieur ou égal à deux ; `write_svg` conserve plusieurs représentations des points et du document. Un appel volumineux peut épuiser temps ou mémoire. C’est un compromis explicitement documenté, pas une vulnérabilité d’exécution de code ni une violation certaine du contrat. La CLI fixe toutefois l’échantillonnage à 201, ce qui réduit cette exposition dans son usage ordinaire.

- **Perte possible du fichier existant pendant l’écriture.** Construire le document avant ouverture protège contre les erreurs de préparation, mais `write_bytes` peut tronquer le fichier puis échouer. La documentation l’annonce correctement. Une écriture transactionnelle serait un durcissement ; elle n’est pas exigée par le challenge.

- **Vérification encore incomplète.** Les « 131 assertions » constituent une trace candidate rapportée. Leur programme n’étant pas reproduit, je ne peux examiner ni leurs assertions exactes ni leur couverture effective. Le vérificateur officiel n’a pas été exécuté, conformément à la frontière de phase annoncée : ce n’est pas un échec technique constaté, mais le verdict reste ouvert. La commande prescrite demeure nécessaire avant conclusion finale.

**Préférences et ambiguïtés à ne pas transformer en défauts :**

- Les axes ramenés au bord, le cercle pour un point isolé et l’absence d’heuristique d’asymptote respectent les arbitrages et sont documentés.
- L’exemple `sqrt(2)^2` affiche `2.0000000000000004`, contre `2.0` dans le challenge. Sans exigence explicite d’arrondi, cet écart flottant ne démontre pas une erreur du moteur.
- Les fichiers de décisions et de contrôles supplémentaires ne constituent pas clairement une violation : le challenge impose une destination exclusive, sans dire sans ambiguïté que seuls deux fichiers peuvent y exister.
- Aucun défaut de projection n’est établi ici ; les cas constants, les points isolés et les grandes étendues ont un traitement explicite.

Cette critique repose exclusivement sur les éléments reproduits. Aucun outil, test, fichier, sous-agent ou acte Git ; le verdict technique appartient au vérificateur indépendant.
````

### MSG-007 — arbitrage final et vérification

Direction : `RELAY → MAIN`. Réponse visible : 241 mots.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2 — phase MAIN finale. Tu représentes le même rôle MAIN, orchestrateur candidat et unique écrivain, dans une nouvelle session éphémère mesurée. Aucun nouveau consultant n'est autorisé. Reprends la première solution présente dans `solution/`. Qualifie chaque point de SA-03 comme retenu, écarté ou non vérifiable et complète `solution/DECISIONS.md` avec la justification et la preuve. Applique uniquement les corrections retenues. Exécute ensuite le vérificateur officiel exactement ainsi : `python3 scripts/verify.py --challenge scientific-calculator --solution runs/astra-medium-scientific-v2-001/solution`. Corrige les défauts confirmés jusqu'au verdict final. Écris uniquement dans `solution/`, n'effectue aucune opération Git et restitue rôles, arbitrages, premier passage, verdict final, corrections et limites.
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
## Objectif et portée

Avis SA-01 fondé exclusivement sur le challenge fourni. Aucune consultation de dépôt, utilisation d’outil, délégation ou vérification exécutée. La spécification et la suite étant figées, les recommandations ci-dessous constituent des arbitrages d’implémentation ; elles ne modifient pas le contrat.

## Obligations à préserver

- **Livraison :** uniquement `scientific_calculator.py` et `README.md` dans `solution/`. Bibliothèque standard, Python ≥ 3.10, sans réseau, `eval()`, `exec()`, `compile()` ni exécution système issue des expressions.
- **Langage :** grammaire fermée couvrant les nombres, opérateurs, parenthèses, signes, constantes, fonctions et `x`. Consommer toute l’expression : accepter un préfixe valide puis ignorer un suffixe serait une faille.
- **Calcul :** puissance associative à droite et prioritaire sur le signe unaire ; résultat de type flottant fini. Distinguer `ValueError` et `ZeroDivisionError` conformément au contrat.
- **Échantillonnage :** au moins deux points, bornes incluses, intervalle strictement croissant, substitution de `x`, et `None` pour chaque résultat local indéfini ou non fini.
- **SVG :** document autonome UTF-8 valide, fond, deux axes en éléments `line`, échelle adaptée, rupture aux points invalides, contenu utilisateur échappé, aucun contenu actif ou externe. Aucun point fini doit entraîner `ValueError`.
- **CLI :** expressions, tracés et commandes de session ; historique des réussites uniquement ; erreurs compréhensibles et reprise de la boucle.
- **Documentation et validation :** syntaxe, fonctions, exemples et limites. Le candidat devra exécuter la commande prescrite ; le verdict reste celui du vérificateur indépendant.

## Arbitrages recommandés

| Sujet | Ambiguïté ou risque | Recommandation à arbitrer |
|---|---|---|
| Puissance et signes | Les exemples ne précisent pas les exposants négatifs. | Accepter `2^-2` et `2^(-2)` ; préserver simultanément `-2^2 = -4`. |
| Syntaxe numérique | `.5`, `5.`, Unicode et espaces ne sont pas détaillés. | Accepter les formes décimales usuelles et les exposants signés ; privilégier les chiffres ASCII et rejeter toute notation supplémentaire non prévue. |
| Fonctions | Arity et syntaxe d’appel implicites. | Un argument entre parenthèses ; refuser arguments multiples, mots-clés, appels indirects et multiplication implicite. |
| Variables | Le dictionnaire semble générique, mais seul `x` est autorisé. | Ne permettre que `x` dans l’expression, même si d’autres clés sont fournies ; ne jamais permettre de redéfinir `pi`, `e` ou une fonction. Documenter le traitement des clés inutilisées. |
| Dépassements numériques | Les bibliothèques peuvent lever `OverflowError` ou produire un infini. | Convertir les dépassements de calcul en `ValueError` pour `evaluate`, puis en `None` lorsqu’ils concernent un point échantillonné. |
| Puissances particulières | `0^0` et `0^-1` ne sont pas spécifiés. | Documenter une convention : `0^0 = 1` suivant le comportement numérique usuel ; `0^-1` en `ValueError` comme puissance indéfinie. Réserver `ZeroDivisionError` à `/` par zéro. |
| Expression invalide dans un tracé | Une faute globale pourrait devenir une courbe entièrement vide. | Valider la syntaxe et les noms une fois ; propager ces erreurs. Seuls les échecs numériques propres aux points deviennent `None`. |
| Paramètres publics | Bornes infinies, `NaN`, nombre d’échantillons non entier. | Exiger des bornes finies et un entier ≥ 2, avec rejet explicite des booléens. |
| Axes hors domaine | L’origine peut être extérieure à la plage tracée. | Choisir et documenter une convention conservant deux axes visibles, par exemple un placement au bord lorsque zéro est hors champ. |
| Historique | Format, contenu des entrées et échecs d’écriture non précisés. | Conserver les expressions et commandes de tracé réussies dans l’ordre ; ajouter le tracé seulement après écriture réussie. Exclure les commandes de contrôle. |

## Surfaces d’attaque et défauts prioritaires

**P0 — Évaluation arbitraire.** Un analyseur qui délègue au langage Python ou résout librement des noms peut exposer attributs, imports et appels imprévus. Recommandation : analyse syntaxique fermée, liste explicite des fonctions et rejet des chaînes, indexations, points d’attribut et caractères résiduels. Une interdiction par recherche de mots dangereux ne suffit pas.

**P0 — Injection SVG.** Le titre peut contenir des balises, guillemets, esperluettes ou caractères interdits par XML. L’échappement des balises doit s’accompagner du traitement des caractères XML invalides. Les coordonnées doivent provenir exclusivement de valeurs numériques finies validées ; aucun texte utilisateur ne doit devenir du balisage, une URL ou un attribut événementiel.

**P1 — Épuisement des ressources.** Imbrication profonde, expressions très longues, puissances gigantesques et échantillonnages excessifs peuvent bloquer ou faire échouer le processus. Recommandation : calcul flottant sans entiers intermédiaires gigantesques, limites raisonnables documentées et erreurs maîtrisées. Ces limites ajoutent une restriction non chiffrée par le contrat : leur adoption doit être explicite.

**P1 — Instabilité de l’échelle.** Des points finis ne garantissent pas que leurs différences ou transformations restent finies. Une plage très grande, une fonction constante ou un unique point valide peuvent provoquer dépassement ou division par zéro. Prévoir des transformations stables, une marge pour les plages nulles et un rendu du point isolé.

**P1 — Écriture et récupération CLI.** Un chemin invalide ou non accessible doit produire un message puis rendre la main. Le chemin de sortie est une destination explicitement fournie, pas une commande à interpréter. Éviter d’ouvrir ou tronquer le fichier avant validation complète du document ; n’enregistrer aucun succès prématuré.

## Limite scientifique à rendre explicite

Un échantillonnage fini ne détecte pas toutes les discontinuités. Pour `1/x`, un intervalle traversant zéro peut ne contenir aucun échantillon exactement nul ; `tan` près d’un pôle peut retourner une très grande valeur finie.

La coupure sur `None` est obligatoire. La garantie de repérer toutes les asymptotes ne découle pas du contrat et ne peut pas être promise. Recommandation : documenter cette limite ; soumettre toute heuristique supplémentaire à un arbitrage, car elle peut aussi couper une fonction continue à forte pente.

## Contrôles et suite

Prioriser les contrôles de précédence, refus des constructions étrangères, classification des erreurs, ruptures SVG, titres hostiles et reprise CLI après échec d’écriture. Vérifier aussi les plages constantes et les extrêmes numériques.

Aucun contrôle exécuté ; aucun fichier modifié ; aucune opération Git. Les ambiguïtés incompatibles avec le vérificateur devront être consignées, sans correction silencieuse de la suite figée.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
Avis SA-02 — Je recommande un analyseur explicite, une séparation nette entre syntaxe et calcul, et un rendu SVG fondé sur les seules données finies. Le risque principal concerne la distinction entre expression invalide et point isolé hors domaine.

**Architecture recommandée**

Conserver les trois fonctions publiques exigées et organiser le module en composants internes distincts :

- **Analyse lexicale** : reconnaître nombres, noms autorisés, opérateurs et parenthèses ; rejeter chaque caractère restant.
- **Analyse syntaxique** : construire une représentation de l’expression et vérifier que tous les jetons sont consommés.
- **Évaluation numérique** : appliquer les opérations et fonctions autorisées, contrôler les domaines et la finitude.
- **Échantillonnage** : produire les abscisses et transformer les erreurs numériques locales en interruptions.
- **Rendu SVG** : calculer les limites, transformer les coordonnées et dessiner les segments.
- **CLI** : interpréter les commandes, gérer l’historique et présenter les erreurs.

Cette séparation facilite les vérifications indépendantes. Importer le module ne doit ni lancer la boucle interactive ni créer de fichier.

**Arbitrage 1 — Analyseur dédié ou transformation d’un langage existant**

Recommandation : analyseur récursif descendant dédié. La grammaire est assez petite pour rester contrôlable, tandis qu’une transformation vers la syntaxe Python ajoute des écarts de langage à surveiller.

Les propriétés décisives sont :

- puissance associative à droite ;
- puissance prioritaire sur le signe placé devant sa base ;
- signe unaire accepté dans l’exposant ;
- fonctions à un argument, avec parenthèses ;
- absence de multiplication implicite.

Les exemples `-2^2 = -4`, `(-2)^2 = 4`, `2^3^2 = 512` et `2^-2 = 0.25` doivent être considérés ensemble : réussir les deux premiers ne garantit pas le traitement correct des exposants signés.

Le lexeur doit reconnaître intégralement la notation scientifique. Une entrée comme `1e+` ne doit pas être récupérée comme plusieurs éléments valides. L’acceptation de `.5` et `5.` constitue une convention raisonnable à documenter, ces formes n’étant pas précisées individuellement.

**Arbitrage 2 — Invariants numériques et exceptions**

Recommandation : toute évaluation réussie produit un `float` fini et réel. Les erreurs de syntaxe, noms inconnus, domaines invalides, débordements et résultats non finis deviennent des `ValueError`. La division par zéro conserve `ZeroDivisionError`.

Points sensibles :

- `sqrt(-1)`, `ln(0)` et `acos(2)` : domaine réel invalide ;
- `(-1)^0.5` : refuser un résultat complexe ;
- `exp(10000)` et les puissances excessives : convertir le débordement en erreur contractuelle ;
- `1/(-0.0)` : division par zéro ;
- `x` absent ou fourni avec une valeur non finie : erreur explicite ;
- `2pi`, `sin x`, attributs, indexations et appels imbriqués non autorisés : rejet syntaxique.

Les variables fournies ne doivent pas élargir la grammaire : une clé arbitraire ne devient pas un nom utilisable, et `pi` ou `e` ne devraient pas être redéfinis par ce dictionnaire.

Deux conventions restent à arbitrer : `0^0` et zéro élevé à une puissance négative. Recommandation : documenter le comportement retenu, en distinguant le second cas de l’opérateur `/` explicitement mentionné dans le contrat.

Pour `tan(pi/2)`, éviter un seuil arbitraire présenté comme une vérité mathématique : la valeur flottante de `pi/2` et l’approximation numérique de la tangente demandent une convention documentée.

**Arbitrage 3 — Expression invalide ou trou dans la courbe**

Recommandation : analyser l’expression une seule fois avant l’échantillonnage. Les erreurs structurelles doivent remonter immédiatement ; seuls les échecs numériques dépendant de l’abscisse deviennent `None`.

Ainsi, `sqrt(x)` sur un intervalle contenant des nombres négatifs produit des trous, tandis que `sqrt(` doit signaler une expression invalide. Des catégories internes d’erreurs peuvent préserver cette distinction tout en respectant les exceptions publiques demandées.

Invariants à contrôler :

- bornes finies, strictement croissantes ;
- nombre entier d’échantillons, au moins égal à deux ;
- longueur du résultat exactement égale à `samples` ;
- première et dernière abscisses égales aux bornes ;
- chaque ordonnée est finie ou vaut `None`.

Une interpolation doit éviter les débordements intermédiaires pour de grandes bornes finies. Fixer explicitement les deux extrémités protège aussi leur inclusion exacte.

Limite importante : un échantillonnage fini ne détecte pas toute discontinuité. Si aucun point ne tombe sur le pôle de `1/x`, aucun `None` n’est nécessairement produit. Recommandation : assurer les coupures explicites et documenter cette limite ; une détection heuristique des sauts dépasserait le contrat et pourrait couper des courbes continues.

**Arbitrage 4 — Échelle et innocuité du SVG**

Recommandation : retenir uniquement les points dont les deux coordonnées sont finies, puis calculer une fenêtre avec marges. Toute donnée non traçable interrompt le segment courant.

Prévoir les cas dégénérés : fonction constante, point fini unique, suite de `None`, abscisses identiques et amplitudes extrêmes. Une étendue nulle nécessite une marge artificielle déterministe. Aucun attribut SVG ne doit contenir `nan` ou `inf`.

Les deux axes doivent être des éléments `line`. Leur position lorsque zéro est hors de la fenêtre n’est pas explicitée. Pour un arbitrage simple, je recommande d’inclure zéro dans les limites affichées, en acceptant la compression possible de certaines courbes.

Le titre doit être inséré uniquement comme texte XML échappé. L’échappement des caractères spéciaux ne suffit pas pour les caractères de contrôle interdits en XML : prévoir leur traitement. Utiliser une structure SVG fixe, sans interprétation du contenu utilisateur, script ni référence externe.

**Stratégie de validation et CLI**

Prioriser des contrôles observables :

- tableau d’expressions couvrant précédence, domaines, noms interdits et exceptions exactes ;
- échantillonnages avec bornes vérifiées, trou central et domaine entièrement invalide ;
- lecture du SVG avec un parseur XML standard, contrôle des axes, coordonnées finies et absence de liaison à travers un trou ;
- titre contenant caractères XML spéciaux et texte ressemblant à une balise ;
- session CLI simulée : succès, erreur, nouveau succès, historique, effacement et sortie.

La CLI doit évaluer ses bornes avec le même moteur, enregistrer seulement les opérations réussies et ajouter un tracé à l’historique après l’écriture effective du fichier. Les erreurs de chemin ou d’écriture doivent permettre de continuer la session. Prévoir également la fin de l’entrée standard.

Le README doit préciser radians, syntaxe, conventions numériques et limites de détection des discontinuités.

Avis fondé exclusivement sur le challenge fourni ; aucun outil ni contrôle exécuté. Le candidat devra lancer la commande de vérification prescrite ; le verdict technique reste celui du vérificateur indépendant.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
Je confirme l’accord principal avec SA-02, avec deux corrections de formulation et un désaccord utile sur les axes. Le challenge original n’étant pas reproduit ici, cette confrontation repose uniquement sur les deux avis ; elle ne permet pas de confirmer indépendamment leurs affirmations contractuelles.

**Accords et doublons.** Nos recommandations convergent sur la grammaire fermée, la consommation intégrale de l’entrée, les précédences, les résultats réels finis, la séparation entre erreurs structurelles et numériques, l’échappement XML, les ruptures de courbe et l’historique après réussite effective. Ces éléments doivent former une seule liste de contrôles. La décomposition proposée par SA-02 précise utilement leur mise en œuvre, sans constituer une obligation d’architecture. L’absence d’effets de bord à l’import et la gestion de la fin d’entrée complètent mon avis.

**Correction prioritaire : appels imbriqués.** La formulation de SA-02 « appels imbriqués non autorisés » est ambiguë. Une composition comme `sin(cos(x))` ne doit pas être assimilée à un appel indirect ou à une construction étrangère. La recommandation doit viser les appels vers des fonctions non autorisées et les formes d’appel étrangères à la grammaire. Une interdiction générale de l’imbrication introduirait une restriction que nos avis ne justifient pas.

**Révision commune : erreurs numériques pendant l’échantillonnage.** « Seuls les échecs numériques dépendant de l’abscisse deviennent `None` » est trop restrictif. Une expression syntaxiquement valide telle que `sqrt(-1)` peut être indéfinie à chaque point sans dépendre de `x`. Il faut distinguer la validité structurelle de l’expression de la réussite numérique de chaque évaluation. Selon le contrat rapporté, l’échantillonnage peut alors produire uniquement des `None`, puis le rendu doit lever `ValueError` faute de point fini. Il ne faut pas exiger une dépendance à `x` pour reconnaître un échec numérique local.

**Désaccord utile : axes hors domaine.** Inclure systématiquement zéro, comme le propose SA-02, peut fortement comprimer une courbe située loin de l’origine et affaiblir l’exigence d’échelle adaptée. Je maintiens une préférence pour des axes placés au bord lorsque zéro est hors champ, avec une convention documentée qui évite de présenter ce bord comme la coordonnée zéro. Les deux choix restent des arbitrages tant que le contrat ne tranche pas.

**Priorités consolidées.**

- **P0 :** empêcher toute exécution ou résolution de noms arbitraire ; garantir un SVG valide sans contenu actif ni référence externe.
- **P1 :** vérifier précédences et exceptions, corriger les deux ambiguïtés ci-dessus, préserver les trous, stabiliser interpolation et projection pour les valeurs extrêmes, puis assurer la reprise CLI après échec.
- **P2 :** documenter les conventions numériques, les axes et les limites scientifiques ; encadrer les ressources sans transformer des plafonds arbitraires en exigences du challenge.

La limite sur les asymptotes est un accord complet : les coupures explicites sont requises, une détection exhaustive ne peut être promise.

Aucun outil, contrôle, changement de fichier ou acte Git effectué. Le candidat conserve l’implémentation ; le vérificateur indépendant conserve le verdict.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
Je confirme l’architecture proposée et l’essentiel de l’avis SA-01, avec deux corrections de mon avis initial et un arbitrage révisé sur les axes. Cette confrontation repose uniquement sur les deux avis reproduits ; le challenge lui-même n’est pas reproduit dans ce message.

**Accords et doublons.** Nous convergeons sur l’analyseur fermé, la consommation intégrale des jetons, la précédence des puissances, les résultats flottants finis et la distinction entre erreurs structurelles et échecs numériques d’échantillonnage. Même convergence sur l’échappement XML, les ruptures aux points invalides, l’historique après succès effectif et les limites de détection des discontinuités. Ces doublons doivent former une seule liste de critères d’acceptation, sans multiplier les composants ou les contrôles équivalents.

**Corrections de mon avis initial.**

- La formule « appels imbriqués non autorisés » est trop large : une composition telle que `sin(cos(0))` doit rester permise si chaque appel respecte la grammaire des fonctions autorisées. Ce sont les appels indirects et les constructions étrangères qui doivent être rejetés.
- Un domaine entièrement invalide n’est pas une erreur syntaxique : une expression valide comme `sqrt(-1)` peut produire uniquement des `None` pendant l’échantillonnage. Selon l’obligation rapportée par SA-01, le rendu sans aucun point fini doit ensuite lever `ValueError`. Il faut distinguer explicitement ces deux étapes.

**Désaccord utile : position des axes.** Ma recommandation d’inclure systématiquement zéro peut comprimer fortement une courbe éloignée de l’origine et affaiblir l’exigence d’échelle adaptée. Je privilégie désormais une fenêtre fondée sur les données et des axes ramenés au bord lorsque zéro est hors champ, sous réserve du contrat exact. Cette convention doit être documentée pour éviter qu’un bord soit interprété comme la position réelle de zéro.

**Compléments à retenir avec mesure.** SA-01 apporte deux recommandations utiles : rendre visible un point isolé, qu’une ligne brisée peut laisser invisible, et terminer la validation du SVG avant d’ouvrir le fichier de destination. En revanche, les plafonds de longueur, profondeur ou nombre d’échantillons introduisent des restrictions supplémentaires. Les erreurs de ressources doivent être maîtrisées, mais des plafonds arbitraires ne doivent pas devenir des obligations supposées du défi. Les conventions sur `0^0`, `0^-1` et les booléens restent également des arbitrages tant que le texte contractuel ne les tranche pas.

**Priorités consolidées.**

1. **P0 — Contrat et innocuité :** grammaire fermée, exceptions publiques correctes, séparation syntaxe/calcul, titre sans injection XML et coordonnées finales finies.
2. **P1 — Robustesse observable :** bornes exactement incluses, interpolation et transformations stables, rupture à chaque point invalide, rejet du rendu vide, cas constant et point isolé.
3. **P1 — Continuité de session :** reprise après erreur de calcul ou d’écriture, historique uniquement après réussite.
4. **P2 — Conventions documentées :** axes hors champ, puissances particulières et limites scientifiques.

La validation doit cibler ces comportements publics : expressions représentatives, échantillonnages dégénérés, inspection XML et session CLI avec échec suivi d’un succès. Elle ne doit pas imposer la forme de l’arbre syntaxique ni le découpage interne retenu.

Aucun outil utilisé, contrôle exécuté, fichier modifié ou acte Git effectué. Le verdict appartient au vérificateur indépendant.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION SNAPSHOT ---

--- BEGIN FILE solution/CONTROLES.md ---
# Contrôles candidats — première solution

## Échange 001 — mandat et avis

Demande : préparer une première solution complète avant SA-03, en V2 gouvernée.
MAIN, candidat et unique écrivain, a lu le CHALLENGE.md actif et les quatre avis
fournis par l'orchestrateur expérimental. Aucun autre agent n'a été lancé.
L'ordre des messages sources est enregistré dans DECISIONS.md ; leurs textes
visibles intégraux restent dans le message de relais, sans réécriture par MAIN.
L'orchestrateur expérimental conserve la production du PV et de son annexe.

## Échange 002 — réalisation

DECISIONS.md a été créé avant scientific_calculator.py et README.md.
Les désaccords et corrections ont été arbitrés explicitement : compositions
permises, domaines entièrement invalides échantillonnés en None, axes au bord,
limite de longueur documentée, aucune heuristique d'asymptote.

## Échange 003 — contrôles ciblés

Commande candidate exécutée dans solution :
`PYTHONDONTWRITEBYTECODE=1 python3 -` avec un programme de contrôle fourni sur
l'entrée standard (bibliothèque standard, assertions, mock de l'entrée CLI et
parseur XML). Le programme de contrôle n'est pas une suite indépendante figée.

Sortie capturée :

```text
131 assertions ciblées réussies ; aucun vérificateur officiel lancé.
```

Code de sortie : 0.

Couverture observée :

- Précédence, associativité, exposants signés, constantes, toutes les fonctions,
  compositions et notation scientifique ; type float et résultats attendus.
- Rejet de syntaxe étrangère, appels indirects, noms arbitraires, caractères
  numériques non ASCII, entrées vides et suffixes ; domaines, overflow,
  variable absente/non finie et division par zéro.
- Longueur excessive et profondeur excessive converties en ValueError.
- Bornes exactes, point central de 1/x, domaine partiel de sqrt(x), domaine
  entièrement invalide, expression structurellement invalide, paramètres rejetés.
- Interpolation finie de -1.7e308 à 1.7e308.
- SVG parsé en XML, deux axes line, deux segments séparés pour 1/x,
  titre hostile conservé comme texte et contrôles XML remplacés, aucun script.
- Projections extrêmes, sous-normales, plage constante, abscisses constantes,
  points isolés et trous ; attributs de coordonnées contrôlés finis.
- Aucun point fini : ValueError sans altérer le fichier préexistant.
- CLI simulée : succès, erreur numérique, succès, échec d'écriture, tracé réussi,
  historique des seules réussites, effacement, sortie et EOF.
- Inspection syntaxique du source : aucun appel à eval, exec ou compile.

L'artefact temporaire `_controle.svg`, créé exclusivement dans solution, a été
supprimé après les contrôles. Aucun fichier du challenge, des tests, des scripts
ou de la gouvernance n'a été modifié. Aucun défaut n'a été révélé par ces
contrôles ; aucune correction consécutive à un échec n'a été nécessaire.

## Échange 004 — frontière de phase

Première solution prête à être transmise à SA-03 par l'orchestrateur
expérimental. Aucun avis SA-03 reçu et aucune vérification officielle exécutée.
Le verdict indépendant reste ouvert. Après la critique, la phase finale devra
arbitrer ses recommandations, corriger les défauts confirmés et exécuter la
commande exacte documentée dans README.md.

Aucune opération Git effectuée. Tokens et durée globale : non enregistrés.
Les contrôles candidats ne garantissent ni la couverture exhaustive ni le
résultat du vérificateur indépendant. Aucun visuel éditorial public produit ;
le SVG livré est un artefact autonome à fond blanc explicite.

--- END FILE solution/CONTROLES.md ---

--- BEGIN FILE solution/DECISIONS.md ---
# Arbitrages MAIN — première solution

Le candidat MAIN est l'unique écrivain. L'orchestrateur expérimental a fourni
les avis consultatifs en lecture seule ; aucun agent supplémentaire n'est lancé.
Le challenge actif a été lu avant cette table, elle-même écrite avant le code.

Ordre des textes visibles reçus, conservés intégralement dans le message source
pour l'annexe verbatim du PV de l'orchestrateur expérimental :
1. SA-01 INITIAL — contrat et sécurité.
2. SA-02 INITIAL — conception et testabilité.
3. SA-01 CONTRADICTION — confrontation et corrections.
4. SA-02 CONTRADICTION — confrontation et révision.

I = avis initial ; C = contradiction. Les recommandations communes sont regroupées.

| Source | Recommandation | Décision motivée |
|---|---|---|
| SA-01 I, SA-02 I | Bibliothèque standard, grammaire fermée, consommation totale, aucune exécution dynamique | Retenue : lexeur dédié et analyse descendante ; aucune résolution libre de nom. |
| SA-01 I | Livrer uniquement moteur et README | Adaptée : ces livrables plus DECISIONS et traces de contrôles dans solution, demandés par le protocole MAIN. |
| SA-02 I | Séparer syntaxe, calcul, échantillonnage, SVG, CLI ; import sans effet | Retenue : représentation postfixée interne, exécution numérique itérative, garde main. |
| SA-01 I, SA-02 I | Puissance à droite, précédence sur unaire, exposant signé | Retenue : grammaire unary → signe unary ou power ; power → primary [^ unary]. |
| SA-01 I, SA-02 I | Décimaux .5 et 5., exposants signés, chiffres ASCII | Retenue : formes usuelles explicites ; rejet des autres caractères et suffixes. |
| SA-01 I, SA-02 I/C, SA-01 C | Fonctions à un argument, compositions autorisées ; pas d'appel indirect ni multiplication implicite | Retenue avec correction des avis initiaux : sin(cos(x)) est valide. |
| SA-01 I, SA-02 I | Seul x est variable ; constantes non redéfinissables | Retenue : clés inutilisées ignorées, valeur de x contrôlée uniquement si utilisée. |
| SA-01 I, SA-02 I | Float réel fini ; division par zéro distincte ; overflow en ValueError | Retenue : contrôle après chaque opération ; math.pow refuse les complexes. |
| SA-01 I, SA-02 I/C | Conventions 0^0, 0^-1, tan aux pôles | Retenue : 1, ValueError, et comportement math.tan sans seuil artificiel. |
| SA-01 I, SA-02 I/C, SA-01 C | Analyser une fois ; distinguer structure invalide et échec numérique | Retenue avec correction : sqrt(-1) produit tous les points à None, même sans dépendance à x. |
| SA-01 I, SA-02 I | Bornes finies croissantes, entier ≥ 2, booléens rejetés | Retenue : diagnostics explicites et contrat numérique sans ambiguïté. |
| SA-02 I, SA-01 C | Extrémités exactes et interpolation stable | Retenue : interpolation convexe si signes opposés ; différence sinon ; bornes assignées exactement. |
| SA-01 I/C, SA-02 I/C | Ne pas promettre toutes les asymptotes | Retenue : coupures sur points invalides ; heuristique de saut écartée car elle peut couper une fonction continue. |
| SA-01 I, SA-02 I/C | XML échappé, caractères interdits traités, coordonnées finies, aucun contenu actif | Retenue : structure SVG fixe et sérialisation XML standard ; remplacement des caractères XML interdits. |
| SA-01 I, SA-02 I/C | Échelles stables, marges, constantes, points isolés, rendu vide refusé | Retenue : normalisation avant soustraction, plage constante centrée, cercle isolé. |
| SA-02 I | Inclure zéro dans toute fenêtre | Écartée suivant SA-01 I/C et SA-02 C : compression excessive des données éloignées. |
| SA-01 I/C, SA-02 C | Axes ramenés au bord | Retenue : position bornée ; légende explicite si origine hors champ. |
| SA-01 I, SA-02 C | Limites de ressources raisonnables | Adaptée : longueur maximale 10 000 caractères et profondeur de syntaxe limitée par Python, convertie en ValueError ; pas de plafond arbitraire d'échantillons. Calcul float et pile numérique itérative. Limites documentées. |
| SA-01 I, SA-02 I/C | Valider document avant ouverture ; erreurs de chemin récupérables | Retenue : document entièrement construit avant écriture et OSError présenté par CLI. |
| SA-01 I, SA-02 I/C | Historique ordonné des réussites ; EOF et reprise après erreur | Retenue : ajout après succès, commandes de contrôle exclues, EOF propre. |
| Tous | Contrôles publics ciblés et documentation des conventions | Retenue : précédence, refus, domaines, SVG extrême et hostile, CLI ; aucun test de forme interne. |
| SA-01 I, SA-02 I | Vérificateur indépendant et corrections | Différée conformément à la phase : uniquement après SA-03 ; aucun verdict officiel revendiqué ici. |

## Trace synthétique

1. Demande : première solution V2, arbitrages préalables, aucun autre consultant.
2. Avis : quatre textes reçus dans l'ordre ci-dessus ; les consultants déclarent
   n'avoir utilisé aucun outil ni exécuté de contrôle.
3. Arbitrage : table ci-dessus ; code et contrôles candidats viennent ensuite.
4. SA-03 et vérification officielle : non exécutés dans cette phase.

Tokens et durée totale des consultants et du candidat : non enregistrés.
Aucune modification de gouvernance ; aucune opération Git autorisée dans ce run.

--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Calculatrice scientifique — première solution V2

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

Les expressions sont limitées à 10 000 caractères. Une imbrication dépassant
la limite de récursion Python devient `ValueError`. Les calculs utilisent une
pile itérative de flottants. Aucun plafond de `samples` supplémentaire n'est
imposé ; mémoire et temps croissent avec le nombre de points et la taille de
l'expression. L'import du module ne lance pas la CLI et ne crée aucun fichier.

## Validation et protocole

Les arbitrages consultatifs figurent dans `DECISIONS.md`. La première solution
est destinée à la critique SA-03. Les contrôles candidats sont décrits dans
`CONTROLES.md` ; ils ne constituent pas le verdict indépendant.

La commande officielle, **réservée à la phase finale après SA-03**, depuis la
racine du dépôt, est :

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-001/solution
```

--- END FILE solution/README.md ---

--- BEGIN FILE solution/scientific_calculator.py ---
"""Calculatrice scientifique sûre, échantillonnage et SVG (Python >= 3.10)."""

import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path


_FUNCTIONS = {name: getattr(math, name) for name in (
    'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sqrt', 'log10', 'exp'
)}
_FUNCTIONS.update(ln=math.log, abs=abs)
_CONSTANTS = {'pi': math.pi, 'e': math.e}
_NUMBER = r'(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?'
_MAX_LENGTH = 10_000


def _tokens(expression):
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError('Expression vide ou non textuelle.')
    if len(expression) > _MAX_LENGTH:
        raise ValueError('Expression trop longue (maximum 10 000 caractères).')
    result = []
    position = 0
    while position < len(expression):
        char = expression[position]
        if char.isspace():
            position += 1
            continue
        match = re.match(_NUMBER, expression[position:])
        if match:
            result.append(('number', match.group()))
            position += len(match.group())
            continue
        match = re.match(r'[A-Za-z_][A-Za-z_0-9]*', expression[position:])
        if match:
            result.append(('name', match.group()))
            position += len(match.group())
            continue
        if char in '+-*/^()':
            result.append((char, char))
            position += 1
            continue
        raise ValueError(f'Caractère interdit à la position {position + 1}.')
    return result + [('end', '')]


class _Parser:
    """Analyse descendante émettant des instructions postfixées fermées."""

    def __init__(self, expression):
        self.tokens = _tokens(expression)
        self.index = 0
        self.code = []

    def accept(self, kind):
        if self.tokens[self.index][0] == kind:
            self.index += 1
            return True
        return False

    def require(self, kind):
        if not self.accept(kind):
            raise ValueError(f'Syntaxe incorrecte : {kind} attendu.')

    def expression(self):
        self.term()
        while self.tokens[self.index][0] in ('+', '-'):
            op = self.tokens[self.index][0]
            self.index += 1
            self.term()
            self.code.append(('binary', op))

    def term(self):
        self.unary()
        while self.tokens[self.index][0] in ('*', '/'):
            op = self.tokens[self.index][0]
            self.index += 1
            self.unary()
            self.code.append(('binary', op))

    def unary(self):
        if self.accept('+'):
            self.unary()
        elif self.accept('-'):
            self.unary()
            self.code.append(('negative', None))
        else:
            self.power()

    def power(self):
        self.primary()
        if self.accept('^'):
            self.unary()
            self.code.append(('binary', '^'))

    def primary(self):
        kind, value = self.tokens[self.index]
        if self.accept('number'):
            self.code.append(('number', value))
        elif self.accept('name'):
            if value in _FUNCTIONS:
                self.require('(')
                self.expression()
                self.require(')')
                self.code.append(('function', value))
            elif value in _CONSTANTS:
                self.code.append(('number', _CONSTANTS[value]))
            elif value == 'x':
                self.code.append(('variable', 'x'))
            else:
                raise ValueError(f'Nom inconnu : {value}.')
        elif self.accept('('):
            self.expression()
            self.require(')')
        else:
            raise ValueError('Syntaxe incorrecte : nombre, fonction ou parenthèse attendu.')


def _parse(expression):
    try:
        parser = _Parser(expression)
        parser.expression()
        parser.require('end')
        return parser.code
    except RecursionError:
        raise ValueError('Expression trop profondément imbriquée.') from None


def _finite(value):
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Un nombre réel fini est requis.') from None
    if not math.isfinite(result):
        raise ValueError('Résultat non fini ou dépassement numérique.')
    return result


def _calculate(code, variables):
    stack = []
    try:
        for kind, value in code:
            if kind == 'number':
                result = _finite(value)
            elif kind == 'variable':
                if variables is None or 'x' not in variables:
                    raise ValueError('La variable x nécessite une valeur.')
                result = _finite(variables['x'])
            elif kind == 'negative':
                result = -stack.pop()
            elif kind == 'function':
                result = _FUNCTIONS[value](stack.pop())
            else:
                right, left = stack.pop(), stack.pop()
                if value == '+':
                    result = left + right
                elif value == '-':
                    result = left - right
                elif value == '*':
                    result = left * right
                elif value == '/':
                    if right == 0:
                        raise ZeroDivisionError('Division par zéro.')
                    result = left / right
                else:
                    result = math.pow(left, right)
            stack.append(_finite(result))
    except OverflowError:
        raise ValueError('Dépassement numérique.') from None
    except ValueError as error:
        raise ValueError(f'Calcul invalide dans le domaine réel : {error}') from None
    return stack[0]


def evaluate(expression: str, variables: dict[str, float] | None = None) -> float:
    """Évalue la grammaire fermée ; retourne un float fini ou une erreur."""
    if variables is not None and not isinstance(variables, dict):
        raise ValueError('Les variables doivent être un dictionnaire.')
    return _calculate(_parse(expression), variables)


def sample_curve(
    expression: str,
    x_min: float,
    x_max: float,
    samples: int = 201,
) -> list[tuple[float, float | None]]:
    """Inclut les bornes exactes ; chaque échec numérique devient None."""
    if isinstance(x_min, bool) or isinstance(x_max, bool):
        raise ValueError('Les bornes doivent être des nombres réels, pas des booléens.')
    low, high = _finite(x_min), _finite(x_max)
    if low >= high:
        raise ValueError('Il faut x_min < x_max.')
    if isinstance(samples, bool) or not isinstance(samples, int) or samples < 2:
        raise ValueError('samples doit être un entier supérieur ou égal à 2.')
    code = _parse(expression)
    points = []
    for index in range(samples):
        fraction = index / (samples - 1)
        if index == 0:
            x = low
        elif index == samples - 1:
            x = high
        elif low < 0 < high:
            x = (1 - fraction) * low + fraction * high
        else:
            x = low + fraction * (high - low)
        try:
            y = _calculate(code, {'x': x})
        except (ValueError, ZeroDivisionError):
            y = None
        points.append((x, y))
    return points


def _projection(values, start, end):
    """Normaliser avant soustraction évite les étendues infinies."""
    low, high = min(values), max(values)
    if low == high:
        def constant(value):
            return (start + end) / 2 if value == low else (start if value < low else end)
        return constant, low, high
    scale = max(abs(low), abs(high))
    lo, hi = low / scale, high / scale

    def project(value):
        if value <= low:
            return start
        if value >= high:
            return end
        ratio = (value / scale - lo) / (hi - lo)
        return start + ratio * (end - start)

    return project, low, high


def _xml_text(text):
    """Remplace les caractères interdits en XML 1.0 avant sérialisation."""
    return ''.join(char if (ord(char) in (9, 10, 13)
                           or 0x20 <= ord(char) <= 0xD7FF
                           or 0xE000 <= ord(char) <= 0xFFFD
                           or 0x10000 <= ord(char) <= 0x10FFFF)
                   else '\uFFFD' for char in str(text))


def write_svg(
    points: list[tuple[float, float | None]],
    output_path: str,
    title: str = '',
) -> None:
    """Écrit un SVG autonome ; une coordonnée invalide coupe le segment."""
    cleaned = []
    for point in points:
        try:
            x, y = point
            cleaned.append((_finite(x), _finite(y)))
        except (ValueError, TypeError):
            cleaned.append(None)
    finite = [point for point in cleaned if point is not None]
    if not finite:
        raise ValueError('Aucun point fini à tracer.')
    px, xmin, xmax = _projection([p[0] for p in finite], 60, 760)
    py, ymin, ymax = _projection([p[1] for p in finite], 440, 60)
    root = ET.Element('svg', xmlns='http://www.w3.org/2000/svg',
                      width='800', height='500', viewBox='0 0 800 500')
    ET.SubElement(root, 'title').text = _xml_text(title)
    ET.SubElement(root, 'rect', x='0', y='0', width='800', height='500', fill='white')
    ET.SubElement(root, 'text', x='60', y='28', fill='#111111').text = _xml_text(title)
    ET.SubElement(root, 'line', x1='60', y1=str(py(0)), x2='760', y2=str(py(0)),
                  stroke='#666666')
    ET.SubElement(root, 'line', x1=str(px(0)), y1='60', x2=str(px(0)), y2='440',
                  stroke='#666666')

    def draw(segment):
        if len(segment) == 1:
            x, y = segment[0]
            ET.SubElement(root, 'circle', cx=f'{px(x):.8f}', cy=f'{py(y):.8f}',
                          r='3', fill='#145aca')
        elif segment:
            coordinates = ' '.join(f'{px(x):.8f},{py(y):.8f}' for x, y in segment)
            ET.SubElement(root, 'polyline', points=coordinates, fill='none',
                          stroke='#145aca', **{'stroke-width': '2'})

    segment = []
    for point in cleaned:
        if point is None:
            draw(segment)
            segment = []
        else:
            segment.append(point)
    draw(segment)
    legend = f'x : [{xmin:.6g}, {xmax:.6g}] ; y : [{ymin:.6g}, {ymax:.6g}]'
    ET.SubElement(root, 'text', x='60', y='468', fill='#111111').text = legend
    if not xmin <= 0 <= xmax or not ymin <= 0 <= ymax:
        ET.SubElement(root, 'text', x='60', y='490', fill='#111111').text = (
            'Origine hors champ : axe correspondant au bord, sans représenter zéro.')
    document = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    Path(output_path).write_bytes(document)


_HELP = """Expressions : + - * / ^, parenthèses, pi, e ; angles en radians.
Fonctions : sin cos tan asin acos atan sqrt ln log10 exp abs.
Exemple : sqrt(2) ^ 2 ; la variable x est réservée aux tracés dans la CLI.
Tracé : plot sin(x); -pi; pi; sinus.svg
Commandes : help, history, clear, quit, exit."""


def main() -> None:
    """Boucle interactive ; historique des seules opérations réussies."""
    history = []
    while True:
        try:
            line = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line:
            continue
        if line in ('quit', 'exit'):
            return
        if line == 'help':
            print(_HELP)
            continue
        if line == 'history':
            print('\n'.join(f'{i}. {entry}' for i, entry in enumerate(history, 1))
                  or 'Historique vide.')
            continue
        if line == 'clear':
            history.clear()
            print('Historique effacé.')
            continue
        try:
            if line.split(maxsplit=1)[0] == 'plot':
                parts = [part.strip() for part in line[4:].split(';')]
                if len(parts) != 4 or not all(parts):
                    raise ValueError('Syntaxe : plot expression; minimum; maximum; fichier.svg')
                expression, low, high, output = parts
                points = sample_curve(expression, evaluate(low), evaluate(high))
                write_svg(points, output, title=expression)
                print(f'Courbe enregistrée dans {output}')
            else:
                print(evaluate(line))
            history.append(line)
        except (ValueError, ZeroDivisionError, OSError, MemoryError) as error:
            print(f'Erreur : {error or "ressources insuffisantes"}')
        except KeyboardInterrupt:
            print('Opération interrompue.')


if __name__ == '__main__':
    main()

--- END FILE solution/scientific_calculator.py ---

--- END FIRST SOLUTION SNAPSHOT ---

--- BEGIN SA-03 CRITIQUE ---
La lecture statique ne révèle pas d’exécution arbitraire, d’injection XML ni d’erreur manifeste de précédence. Les corrections issues des consultations sont effectivement présentes : compositions autorisées, séparation syntaxe/calcul, domaines entièrement invalides convertis en `None`, ruptures explicites et historique ajouté après réussite.

**Défaut confirmé — restriction supplémentaire du langage.** `_tokens` refuse toute expression dépassant 10 000 caractères, même grammaticalement valide. Une somme de 5 001 termes `1`, séparés par `+`, dépasse cette limite alors que son résultat est fini. La profondeur de récursion impose également une restriction sur des parenthèses ou signes unaires valides. Ces restrictions sont arbitrées et documentées, mais le challenge figé ne les prévoit pas : la documentation ne suffit donc pas à établir leur conformité. Leur incidence sur l’acceptation reste inconnue. Il faut conserver explicitement cet écart dans l’arbitrage final, sans le présenter comme une exigence du défi.

**Risques à examiner avant clôture :**

- **Échappement du terminal absent.** Le SVG protège correctement son titre, mais la CLI réaffiche directement le chemin de sortie et les entrées d’historique. Un chemin contenant des séquences de contrôle, accepté notamment sur un système POSIX, peut donc modifier l’affichage du terminal lors du message de réussite ou de `history`. C’est un risque distinct de l’injection SVG ; son exploitation dépend du terminal et de la provenance des commandes. Aucun mécanisme d’exécution système n’est démontré.

- **Récupération CLI partielle.** Le bloc entourant `input()` intercepte seulement `EOFError` et `KeyboardInterrupt`. Une erreur de lecture telle qu’un `OSError`, ou un manque de mémoire pendant la lecture, échappe donc au traitement prévu pour les opérations. Les sorties de `help`, `history` et `clear` sont également hors de ce traitement. Cela fragilise la promesse générale « toute erreur […] sans traceback », même si la récupération après perte du canal d’entrée ou de sortie peut être impossible. Les contrôles rapportés couvrent EOF, mais pas ces défaillances.

- **Ressources non bornées pour l’API de tracé.** `sample_curve` accepte tout entier d’échantillonnage supérieur ou égal à deux ; `write_svg` conserve plusieurs représentations des points et du document. Un appel volumineux peut épuiser temps ou mémoire. C’est un compromis explicitement documenté, pas une vulnérabilité d’exécution de code ni une violation certaine du contrat. La CLI fixe toutefois l’échantillonnage à 201, ce qui réduit cette exposition dans son usage ordinaire.

- **Perte possible du fichier existant pendant l’écriture.** Construire le document avant ouverture protège contre les erreurs de préparation, mais `write_bytes` peut tronquer le fichier puis échouer. La documentation l’annonce correctement. Une écriture transactionnelle serait un durcissement ; elle n’est pas exigée par le challenge.

- **Vérification encore incomplète.** Les « 131 assertions » constituent une trace candidate rapportée. Leur programme n’étant pas reproduit, je ne peux examiner ni leurs assertions exactes ni leur couverture effective. Le vérificateur officiel n’a pas été exécuté, conformément à la frontière de phase annoncée : ce n’est pas un échec technique constaté, mais le verdict reste ouvert. La commande prescrite demeure nécessaire avant conclusion finale.

**Préférences et ambiguïtés à ne pas transformer en défauts :**

- Les axes ramenés au bord, le cercle pour un point isolé et l’absence d’heuristique d’asymptote respectent les arbitrages et sont documentés.
- L’exemple `sqrt(2)^2` affiche `2.0000000000000004`, contre `2.0` dans le challenge. Sans exigence explicite d’arrondi, cet écart flottant ne démontre pas une erreur du moteur.
- Les fichiers de décisions et de contrôles supplémentaires ne constituent pas clairement une violation : le challenge impose une destination exclusive, sans dire sans ambiguïté que seuls deux fichiers peuvent y exister.
- Aucun défaut de projection n’est établi ici ; les cas constants, les points isolés et les grandes étendues ont un traitement explicite.

Cette critique repose exclusivement sur les éléments reproduits. Aucun outil, test, fichier, sous-agent ou acte Git ; le verdict technique appartient au vérificateur indépendant.
--- END SA-03 CRITIQUE ---
````

</details>

#### Texte retourné pour MSG-007, mot pour mot

````text
Je vais examiner la solution présente, arbitrer chaque point de SA-03, puis appliquer les corrections retenues et lancer le vérificateur officiel. Aucun nouveau consultant ne sera sollicité.


Je retiens trois corrections : supprimer les limites de longueur et de récursion du parseur, neutraliser les caractères de contrôle réaffichés par la CLI et traiter les défaillances de ses canaux d’entrée/sortie. L’écriture transactionnelle et un plafond d’échantillonnage restent écartés : ils ne sont pas exigés par le contrat et leurs limites sont documentées.


Le premier passage du vérificateur officiel réussit : 9 tests sur 9, code de sortie 0. Les quatre contrôles candidats des corrections SA-03 réussissent aussi. Je consigne ces résultats et les limites restantes ; aucune correction supplémentaire n’est nécessaire après ce verdict.


### Résultat

Scientific Calculator V2 terminé. **Premier passage officiel : 9/9 tests réussis, code 0. Verdict final identique**, sans correction supplémentaire.

### Réalisé

MAIN est resté unique écrivain, sans nouveau consultant. Chaque point de SA-03 est qualifié et justifié dans [DECISIONS.md](DECISIONS.md).

Corrections retenues : suppression des limites syntaxiques artificielles, neutralisation des contrôles réaffichés au terminal et traitement des défaillances des canaux CLI.

Quatre contrôles candidats supplémentaires réussissent. Commande officielle exacte, sortie et chronologie figurent dans [CONTROLES.md](CONTROLES.md).

### Limites

Écriture non transactionnelle, ressources physiques limitées et détection non exhaustive des discontinuités restent documentées. Les 131 assertions historiques ne sont pas vérifiables rétroactivement. Tokens et durée globale : non enregistrés.

### Livraison Git

Écritures uniquement dans `solution/`. Aucune opération Git.
````

## Lecture sociale synthétique

SA-01 et SA-02 commencent sans voir l'avis de l'autre. Leurs réponses
croisées rendent ensuite visibles accords, désaccords et doublons. MAIN
arbitre avant d'écrire. SA-03 critique l'instantané obtenu ; MAIN qualifie
alors chaque point avant le vérificateur. Le rapport de résultat chiffre
les recommandations retenues, écartées et non vérifiables.

Les prompts dynamiques répètent volontairement le challenge et les textes
antérieurs : cette duplication fait partie du coût de coordination mesuré.
