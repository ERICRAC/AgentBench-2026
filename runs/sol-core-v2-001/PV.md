# PV multi-agent — sol-core-v2-001

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
| 01-sa01-initial | MSG-001 · analyse indépendante (max 1200) | 62.931 s | 13559 | 8064 | 1566 | 75 | 999 |
| 02-sa02-initial | MSG-002 · analyse indépendante (max 1200) | 72.214 s | 13561 | 8064 | 1840 | 296 | 995 |
| 03-sa01-cross | MSG-003 · contradiction croisée (max 600) | 48.026 s | 16242 | 8064 | 1143 | 475 | 428 |
| 04-sa02-cross | MSG-004 · contradiction croisée (max 600) | 38.788 s | 16244 | 8064 | 898 | 167 | 471 |
| 05-main-first | MSG-005 · arbitrage et première solution | 236.374 s | 153193 | 122880 | 6106 | 1647 | 350 |
| 06-sa03-critic | MSG-006 · critique adversariale (max 1200) | 118.418 s | 20440 | 8064 | 3116 | 2070 | 614 |
| 07-main-final | MSG-007 · arbitrage final et vérification | 321.478 s | 302774 | 272000 | 8406 | 4174 | 490 |

Temps mural : **796.534 s**. Somme des temps-sessions : **898.229 s**.

Tokens : **536013 entrée + 23075 sortie = 559088**. Le cache (435200) est inclus dans
l'entrée et le raisonnement (8904) dans la sortie.

## Messages visibles — verbatim filtré

### MSG-001 — analyse indépendante

Direction : `RELAY → SA-01 → MAIN`. Réponse visible : 999 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Analyse indépendamment le challenge ci-dessous en 1 200 mots maximum. Tu es consultant en lecture seule : n'utilise aucun outil, ne délègue rien, ne consulte aucun dépôt et ne fournis qu'un avis visible. Structure les recommandations pour permettre un arbitrage explicite.
--- BEGIN CHALLENGE ---
# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```

--- END CHALLENGE ---
````

</details>

#### Texte retourné pour MSG-001, mot pour mot

````text
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
````

### MSG-002 — analyse indépendante

Direction : `RELAY → SA-02 → MAIN`. Réponse visible : 995 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Analyse indépendamment le challenge ci-dessous en 1 200 mots maximum. Tu es consultant en lecture seule : n'utilise aucun outil, ne délègue rien, ne consulte aucun dépôt et ne fournis qu'un avis visible. Structure les recommandations pour permettre un arbitrage explicite.
--- BEGIN CHALLENGE ---
# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```

--- END CHALLENGE ---
````

</details>

#### Texte retourné pour MSG-002, mot pour mot

````text
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
````

### MSG-003 — contradiction croisée

Direction : `MAIN/RELAY → SA-01 → MAIN`. Réponse visible : 428 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-01. Analyste exigences et sécurité : obligations, ambiguïtés, erreurs et surfaces d'attaque.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-01 ---
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
--- END YOUR INITIAL SA-01 ---

--- BEGIN PEER INITIAL SA-02 ---
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
--- END PEER INITIAL SA-02 ---
````

</details>

#### Texte retourné pour MSG-003, mot pour mot

````text
## Révision SA-01 après avis SA-02

Les deux avis convergent largement. Ils confirment les mêmes invariants essentiels : `calculate` doit rester pure, n’accepter que quatre opérateurs, préserver `ValueError` et `ZeroDivisionError`, et être séparée du parsing et de la boucle interactive. Ils s’accordent aussi sur le garde d’exécution, la reprise après erreur, l’absence de traceback, la liste blanche stricte, l’interdiction d’`eval()`/`exec()`, le traitement propre d’EOF et l’usage d’exceptions ciblées.

Le principal désaccord utile concerne la grammaire CLI. Mon avis initial recommandait des « espaces souples » et envisageait les formes compactes si elles restaient simples. SA-02 recommande exactement trois éléments séparés par des espaces. Je révise ma recommandation en faveur de SA-02 : accepter les espaces périphériques et multiples, mais exiger trois éléments après découpage — opérande, opérateur, opérande. Ainsi, `-2 * -3.5` est valide et `2+3` ne l’est pas. Cette règle est déterministe, documentable et évite de transformer le défi en problème d’analyse lexicale des signes et opérateurs. L’absence de prise en charge de `2+3` doit être cohérente entre code et README.

Un second point mérite précision : « opérateur inconnu » et « syntaxe invalide » restent deux niveaux distincts. `2 % 3`, composé de trois éléments valides structurellement, devrait atteindre `calculate` et produire son `ValueError`, ensuite traduit par la CLI. `2+3` ou `2 +` relève du parseur. La CLI peut présenter un diagnostic commun si aucun texte exact n’est imposé, mais l’API doit conserver les exceptions contractuelles.

Les doublons entre avis sont nombreux et renforcent leur priorité : ne pas lancer la CLI à l’import, ne pas capturer `Exception`, ne pas quitter après une erreur, ne pas ajouter d’opérateurs, ne pas imprimer depuis `calculate`, ne pas documenter de capacités absentes et ne pas introduire d’effets externes. Les propositions sur EOF, `nan`/`inf`, la casse des commandes et Ctrl-C sont également concordantes : EOF est une robustesse utile ; les autres extensions sont facultatives et ne doivent pas devenir des politiques non demandées.

Priorités finales :

1. Préserver exactement le contrat observable de `calculate` et ses exceptions.
2. Employer une grammaire CLI stricte à trois éléments séparés par des espaces.
3. Isoler parsing, calcul, boucle interactive et garde d’exécution.
4. Capturer uniquement les erreurs utilisateur attendues et poursuivre la boucle.
5. Exclure toute interprétation dynamique, effet système ou fuite de détails internes.
6. Aligner strictement le README sur le comportement réellement fourni.
7. Valider import, quatre opérations, nombres négatifs, erreurs, reprise et sortie propre avec la commande imposée.

La surface d’attaque demeure faible si l’entrée reste structurellement bornée et traitée uniquement par découpage, conversion numérique et liste blanche.
````

### MSG-004 — contradiction croisée

Direction : `MAIN/RELAY → SA-02 → MAIN`. Réponse visible : 471 mots sur 600 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-02. Architecte logiciel et testabilité : structure, invariants, stratégie de validation et cas sensibles.
Voici mot pour mot ton avis initial et celui de l'autre consultant. Produis une seule contradiction, confirmation ou révision de 600 mots maximum. Identifie accords, désaccords utiles, doublons et priorité des recommandations. N'utilise aucun outil et ne délègue rien.
--- BEGIN YOUR INITIAL SA-02 ---
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
--- END YOUR INITIAL SA-02 ---

--- BEGIN PEER INITIAL SA-01 ---
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
--- END PEER INITIAL SA-01 ---
````

</details>

#### Texte retourné pour MSG-004, mot pour mot

````text
## Avis consolidé SA-02 — confirmation avec révision mineure

Je confirme l’architecture initiale et l’essentiel de l’avis SA-01. Les deux analyses convergent sur les invariants déterminants :

- `calculate(left, operator, right)` reste pure, reçoit des nombres et ne réalise ni parsing, ni affichage ;
- seuls `+`, `-`, `*` et `/` sont admis ;
- `ValueError` et `ZeroDivisionError` restent observables lors des appels directs ;
- la CLI traduit uniquement les erreurs utilisateur attendues en messages compréhensibles, puis poursuit la boucle ;
- l’import du module reste sans effet grâce au garde d’exécution ;
- aucune évaluation dynamique, dépendance externe ou capture générale avec `except Exception` ;
- `quit`, `exit` et EOF provoquent une sortie propre.

### Désaccord utile et révision

Le seul désaccord réel concerne la formulation de la grammaire. Mon avis initial recommandait « exactement trois éléments séparés par des espaces ». SA-01 recommande des « espaces souples » et avertit contre une séparation naïve.

Je révise la formulation, mais pas le périmètre fonctionnel : utiliser une décomposition structurelle équivalente à `line.strip().split()` et exiger exactement trois éléments. Cela accepte naturellement les espaces périphériques, plusieurs espaces et les tabulations, tout en rejetant `2+3`, les expressions incomplètes et les éléments surnuméraires.

Ainsi, « espaces souples » ne doit pas être interprété comme l’obligation d’accepter les formes compactes. Étendre le parseur à `-2*-3` créerait une complexité inutile autour des signes et des opérateurs sans exigence explicite. Le README doit annoncer précisément la forme effectivement acceptée.

### Doublons à fusionner

Les recommandations suivantes sont identiques dans les deux avis et ne nécessitent qu’une seule décision :

- séparation calcul/parsing/CLI ;
- liste blanche des opérateurs ;
- opérateur exact dans l’API, normalisation uniquement dans la CLI ;
- acceptation naturelle des `int` par `calculate`, sans conversion de chaînes ;
- gestion de `0.0` et `-0.0` par comparaison exacte à zéro ;
- sortie propre sur EOF ;
- absence de traceback et reprise après erreur ;
- non-promesse des cas non spécifiés (`nan`, `inf`, casse des commandes, syntaxe compacte).

La surface d’attaque décrite par SA-01 confirme l’architecture proposée : un parseur structurellement borné et une sélection explicite des opérateurs suffisent. Une limite arbitraire de longueur d’entrée ajouterait une politique non demandée et reste secondaire.

### Priorités recommandées

1. Respect exact du contrat public de `calculate` et de ses exceptions.
2. Import sans effet interactif.
3. Boucle CLI résiliente avec captures ciblées.
4. Parseur à exactement trois éléments, avec espaces blancs souples.
5. Validation unitaire et intégrée, notamment continuité après deux erreurs successives.
6. Cohérence stricte entre README et comportement.
7. Conforts facultatifs — Ctrl-C, commandes insensibles à la casse, valeurs non finies — seulement après réussite des contrôles obligatoires.

Le cas d’intégration le plus discriminant reste : succès, saisie invalide, division par zéro, nouveau succès, sortie, avec absence de `Traceback` et terminaison normale.
````

### MSG-005 — arbitrage et première solution

Direction : `RELAY → MAIN`. Réponse visible : 350 mots.

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
# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```

--- END CHALLENGE ---

--- BEGIN SA-01 INITIAL ---
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
--- END SA-01 INITIAL ---

--- BEGIN SA-02 INITIAL ---
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
--- END SA-02 INITIAL ---

--- BEGIN SA-01 CONTRADICTION ---
## Révision SA-01 après avis SA-02

Les deux avis convergent largement. Ils confirment les mêmes invariants essentiels : `calculate` doit rester pure, n’accepter que quatre opérateurs, préserver `ValueError` et `ZeroDivisionError`, et être séparée du parsing et de la boucle interactive. Ils s’accordent aussi sur le garde d’exécution, la reprise après erreur, l’absence de traceback, la liste blanche stricte, l’interdiction d’`eval()`/`exec()`, le traitement propre d’EOF et l’usage d’exceptions ciblées.

Le principal désaccord utile concerne la grammaire CLI. Mon avis initial recommandait des « espaces souples » et envisageait les formes compactes si elles restaient simples. SA-02 recommande exactement trois éléments séparés par des espaces. Je révise ma recommandation en faveur de SA-02 : accepter les espaces périphériques et multiples, mais exiger trois éléments après découpage — opérande, opérateur, opérande. Ainsi, `-2 * -3.5` est valide et `2+3` ne l’est pas. Cette règle est déterministe, documentable et évite de transformer le défi en problème d’analyse lexicale des signes et opérateurs. L’absence de prise en charge de `2+3` doit être cohérente entre code et README.

Un second point mérite précision : « opérateur inconnu » et « syntaxe invalide » restent deux niveaux distincts. `2 % 3`, composé de trois éléments valides structurellement, devrait atteindre `calculate` et produire son `ValueError`, ensuite traduit par la CLI. `2+3` ou `2 +` relève du parseur. La CLI peut présenter un diagnostic commun si aucun texte exact n’est imposé, mais l’API doit conserver les exceptions contractuelles.

Les doublons entre avis sont nombreux et renforcent leur priorité : ne pas lancer la CLI à l’import, ne pas capturer `Exception`, ne pas quitter après une erreur, ne pas ajouter d’opérateurs, ne pas imprimer depuis `calculate`, ne pas documenter de capacités absentes et ne pas introduire d’effets externes. Les propositions sur EOF, `nan`/`inf`, la casse des commandes et Ctrl-C sont également concordantes : EOF est une robustesse utile ; les autres extensions sont facultatives et ne doivent pas devenir des politiques non demandées.

Priorités finales :

1. Préserver exactement le contrat observable de `calculate` et ses exceptions.
2. Employer une grammaire CLI stricte à trois éléments séparés par des espaces.
3. Isoler parsing, calcul, boucle interactive et garde d’exécution.
4. Capturer uniquement les erreurs utilisateur attendues et poursuivre la boucle.
5. Exclure toute interprétation dynamique, effet système ou fuite de détails internes.
6. Aligner strictement le README sur le comportement réellement fourni.
7. Valider import, quatre opérations, nombres négatifs, erreurs, reprise et sortie propre avec la commande imposée.

La surface d’attaque demeure faible si l’entrée reste structurellement bornée et traitée uniquement par découpage, conversion numérique et liste blanche.
--- END SA-01 CONTRADICTION ---

--- BEGIN SA-02 CONTRADICTION ---
## Avis consolidé SA-02 — confirmation avec révision mineure

Je confirme l’architecture initiale et l’essentiel de l’avis SA-01. Les deux analyses convergent sur les invariants déterminants :

- `calculate(left, operator, right)` reste pure, reçoit des nombres et ne réalise ni parsing, ni affichage ;
- seuls `+`, `-`, `*` et `/` sont admis ;
- `ValueError` et `ZeroDivisionError` restent observables lors des appels directs ;
- la CLI traduit uniquement les erreurs utilisateur attendues en messages compréhensibles, puis poursuit la boucle ;
- l’import du module reste sans effet grâce au garde d’exécution ;
- aucune évaluation dynamique, dépendance externe ou capture générale avec `except Exception` ;
- `quit`, `exit` et EOF provoquent une sortie propre.

### Désaccord utile et révision

Le seul désaccord réel concerne la formulation de la grammaire. Mon avis initial recommandait « exactement trois éléments séparés par des espaces ». SA-01 recommande des « espaces souples » et avertit contre une séparation naïve.

Je révise la formulation, mais pas le périmètre fonctionnel : utiliser une décomposition structurelle équivalente à `line.strip().split()` et exiger exactement trois éléments. Cela accepte naturellement les espaces périphériques, plusieurs espaces et les tabulations, tout en rejetant `2+3`, les expressions incomplètes et les éléments surnuméraires.

Ainsi, « espaces souples » ne doit pas être interprété comme l’obligation d’accepter les formes compactes. Étendre le parseur à `-2*-3` créerait une complexité inutile autour des signes et des opérateurs sans exigence explicite. Le README doit annoncer précisément la forme effectivement acceptée.

### Doublons à fusionner

Les recommandations suivantes sont identiques dans les deux avis et ne nécessitent qu’une seule décision :

- séparation calcul/parsing/CLI ;
- liste blanche des opérateurs ;
- opérateur exact dans l’API, normalisation uniquement dans la CLI ;
- acceptation naturelle des `int` par `calculate`, sans conversion de chaînes ;
- gestion de `0.0` et `-0.0` par comparaison exacte à zéro ;
- sortie propre sur EOF ;
- absence de traceback et reprise après erreur ;
- non-promesse des cas non spécifiés (`nan`, `inf`, casse des commandes, syntaxe compacte).

La surface d’attaque décrite par SA-01 confirme l’architecture proposée : un parseur structurellement borné et une sélection explicite des opérateurs suffisent. Une limite arbitraire de longueur d’entrée ajouterait une politique non demandée et reste secondaire.

### Priorités recommandées

1. Respect exact du contrat public de `calculate` et de ses exceptions.
2. Import sans effet interactif.
3. Boucle CLI résiliente avec captures ciblées.
4. Parseur à exactement trois éléments, avec espaces blancs souples.
5. Validation unitaire et intégrée, notamment continuité après deux erreurs successives.
6. Cohérence stricte entre README et comportement.
7. Conforts facultatifs — Ctrl-C, commandes insensibles à la casse, valeurs non finies — seulement après réussite des contrôles obligatoires.

Le cas d’intégration le plus discriminant reste : succès, saisie invalide, division par zéro, nouveau succès, sortie, avec absence de `Traceback` et terminaison normale.
--- END SA-02 CONTRADICTION ---
````

</details>

#### Texte retourné pour MSG-005, mot pour mot

````text
Je vais d’abord relire le `CHALLENGE.md` de cette tentative, puis créer la table d’arbitrage avant tout code. Je resterai strictement dans `solution/`, sans agent supplémentaire, sans Git et sans lancer le vérificateur officiel pendant cette phase.

Les avis convergent sur presque tout. Le seul arbitrage substantiel est la grammaire CLI : je retiens trois éléments séparés par des espaces blancs souples (`strip().split()`), ce qui accepte les nombres négatifs mais rejette volontairement `2+3`. Je consigne maintenant chaque recommandation consolidée, y compris les options écartées.

La table d’arbitrage est bien créée avant l’implémentation. Je passe à une solution minimale en trois couches (`calculate`, parseur interne, `main`) et à un README aligné sur la grammaire réellement acceptée.

L’implémentation et la documentation sont en place. Je fais uniquement des contrôles ciblés autorisés : API et exceptions, import sans interaction, puis une session CLI avec succès, syntaxe invalide, division par zéro, reprise et sortie. Je ne lance pas `scripts/verify.py`.

## Objectif

Première solution complète du défi Calculator réalisée, prête pour la critique SA-03.

## Travail réalisé

- [DECISIONS.md](<repo>/runs/sol-core-v2-001/solution/DECISIONS.md) : recommandations de SA-01 et SA-02 arbitrées individuellement, dans l’ordre des quatre avis reçus.
- [calculator.py](<repo>/runs/sol-core-v2-001/solution/calculator.py) : API `calculate`, parseur strict, boucle interactive résiliente et sortie propre.
- [README.md](<repo>/runs/sol-core-v2-001/solution/README.md) : lancement, syntaxe, exemples, erreurs et utilisation comme module.

L’arbitrage principal retient trois éléments séparés par des espaces blancs souples. Les formes compactes comme `2+3` sont donc volontairement rejetées.

## Contrôles ciblés

- Quatre opérations, décimaux et nombres négatifs : OK.
- `ValueError` pour les opérateurs inconnus : OK.
- `ZeroDivisionError` pour `0`, `0.0` et `-0.0` : OK.
- Import sans lancement de la CLI : OK.
- Reprise après syntaxe invalide et division par zéro : OK.
- Sortie par `exit` : OK.
- Aucun traceback observé.
- Aucune utilisation d’`eval()`, `exec()` ou `compile()` détectée.

Le vérificateur officiel n’a pas été lancé, conformément à la frontière de phase.

## Suite

SA-03 doit maintenant examiner cette première solution et la table d’arbitrage. Après sa critique, les défauts confirmés pourront être corrigés, puis la commande officielle exacte sera exécutée pendant la phase finale.

Aucune opération Git n’a été effectuée.
````

### MSG-006 — critique adversariale

Direction : `MAIN/RELAY → SA-03 → MAIN`. Réponse visible : 614 mots sur 1200 maximum.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2. Tu es SA-03, critique QA adversarial en lecture seule. Examine le challenge, les avis transmis, la table de décisions et la première solution ci-dessous. En 1 200 mots maximum, cherche omissions, failles de sécurité, erreurs de contrat, cas limites et régressions. Distingue défaut confirmé, risque et préférence. N'utilise aucun outil, ne délègue rien et ne réécris pas la solution.
--- BEGIN CHALLENGE ---
# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```

--- END CHALLENGE ---

--- BEGIN CONSULTATIONS ---

--- BEGIN SA01_INITIAL ---
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
## Révision SA-01 après avis SA-02

Les deux avis convergent largement. Ils confirment les mêmes invariants essentiels : `calculate` doit rester pure, n’accepter que quatre opérateurs, préserver `ValueError` et `ZeroDivisionError`, et être séparée du parsing et de la boucle interactive. Ils s’accordent aussi sur le garde d’exécution, la reprise après erreur, l’absence de traceback, la liste blanche stricte, l’interdiction d’`eval()`/`exec()`, le traitement propre d’EOF et l’usage d’exceptions ciblées.

Le principal désaccord utile concerne la grammaire CLI. Mon avis initial recommandait des « espaces souples » et envisageait les formes compactes si elles restaient simples. SA-02 recommande exactement trois éléments séparés par des espaces. Je révise ma recommandation en faveur de SA-02 : accepter les espaces périphériques et multiples, mais exiger trois éléments après découpage — opérande, opérateur, opérande. Ainsi, `-2 * -3.5` est valide et `2+3` ne l’est pas. Cette règle est déterministe, documentable et évite de transformer le défi en problème d’analyse lexicale des signes et opérateurs. L’absence de prise en charge de `2+3` doit être cohérente entre code et README.

Un second point mérite précision : « opérateur inconnu » et « syntaxe invalide » restent deux niveaux distincts. `2 % 3`, composé de trois éléments valides structurellement, devrait atteindre `calculate` et produire son `ValueError`, ensuite traduit par la CLI. `2+3` ou `2 +` relève du parseur. La CLI peut présenter un diagnostic commun si aucun texte exact n’est imposé, mais l’API doit conserver les exceptions contractuelles.

Les doublons entre avis sont nombreux et renforcent leur priorité : ne pas lancer la CLI à l’import, ne pas capturer `Exception`, ne pas quitter après une erreur, ne pas ajouter d’opérateurs, ne pas imprimer depuis `calculate`, ne pas documenter de capacités absentes et ne pas introduire d’effets externes. Les propositions sur EOF, `nan`/`inf`, la casse des commandes et Ctrl-C sont également concordantes : EOF est une robustesse utile ; les autres extensions sont facultatives et ne doivent pas devenir des politiques non demandées.

Priorités finales :

1. Préserver exactement le contrat observable de `calculate` et ses exceptions.
2. Employer une grammaire CLI stricte à trois éléments séparés par des espaces.
3. Isoler parsing, calcul, boucle interactive et garde d’exécution.
4. Capturer uniquement les erreurs utilisateur attendues et poursuivre la boucle.
5. Exclure toute interprétation dynamique, effet système ou fuite de détails internes.
6. Aligner strictement le README sur le comportement réellement fourni.
7. Valider import, quatre opérations, nombres négatifs, erreurs, reprise et sortie propre avec la commande imposée.

La surface d’attaque demeure faible si l’entrée reste structurellement bornée et traitée uniquement par découpage, conversion numérique et liste blanche.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
## Avis consolidé SA-02 — confirmation avec révision mineure

Je confirme l’architecture initiale et l’essentiel de l’avis SA-01. Les deux analyses convergent sur les invariants déterminants :

- `calculate(left, operator, right)` reste pure, reçoit des nombres et ne réalise ni parsing, ni affichage ;
- seuls `+`, `-`, `*` et `/` sont admis ;
- `ValueError` et `ZeroDivisionError` restent observables lors des appels directs ;
- la CLI traduit uniquement les erreurs utilisateur attendues en messages compréhensibles, puis poursuit la boucle ;
- l’import du module reste sans effet grâce au garde d’exécution ;
- aucune évaluation dynamique, dépendance externe ou capture générale avec `except Exception` ;
- `quit`, `exit` et EOF provoquent une sortie propre.

### Désaccord utile et révision

Le seul désaccord réel concerne la formulation de la grammaire. Mon avis initial recommandait « exactement trois éléments séparés par des espaces ». SA-01 recommande des « espaces souples » et avertit contre une séparation naïve.

Je révise la formulation, mais pas le périmètre fonctionnel : utiliser une décomposition structurelle équivalente à `line.strip().split()` et exiger exactement trois éléments. Cela accepte naturellement les espaces périphériques, plusieurs espaces et les tabulations, tout en rejetant `2+3`, les expressions incomplètes et les éléments surnuméraires.

Ainsi, « espaces souples » ne doit pas être interprété comme l’obligation d’accepter les formes compactes. Étendre le parseur à `-2*-3` créerait une complexité inutile autour des signes et des opérateurs sans exigence explicite. Le README doit annoncer précisément la forme effectivement acceptée.

### Doublons à fusionner

Les recommandations suivantes sont identiques dans les deux avis et ne nécessitent qu’une seule décision :

- séparation calcul/parsing/CLI ;
- liste blanche des opérateurs ;
- opérateur exact dans l’API, normalisation uniquement dans la CLI ;
- acceptation naturelle des `int` par `calculate`, sans conversion de chaînes ;
- gestion de `0.0` et `-0.0` par comparaison exacte à zéro ;
- sortie propre sur EOF ;
- absence de traceback et reprise après erreur ;
- non-promesse des cas non spécifiés (`nan`, `inf`, casse des commandes, syntaxe compacte).

La surface d’attaque décrite par SA-01 confirme l’architecture proposée : un parseur structurellement borné et une sélection explicite des opérateurs suffisent. Une limite arbitraire de longueur d’entrée ajouterait une politique non demandée et reste secondaire.

### Priorités recommandées

1. Respect exact du contrat public de `calculate` et de ses exceptions.
2. Import sans effet interactif.
3. Boucle CLI résiliente avec captures ciblées.
4. Parseur à exactement trois éléments, avec espaces blancs souples.
5. Validation unitaire et intégrée, notamment continuité après deux erreurs successives.
6. Cohérence stricte entre README et comportement.
7. Conforts facultatifs — Ctrl-C, commandes insensibles à la casse, valeurs non finies — seulement après réussite des contrôles obligatoires.

Le cas d’intégration le plus discriminant reste : succès, saisie invalide, division par zéro, nouveau succès, sortie, avec absence de `Traceback` et terminaison normale.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION ---

--- BEGIN FILE solution/DECISIONS.md ---
# Arbitrages de conception

Ce document synthétise les quatre avis consultatifs reçus avant
l'implémentation : avis initial de SA-01, avis initial de SA-02, contradiction
de SA-01, puis contradiction de SA-02. Le candidat principal reste seul
décideur et seul écrivain.

| Recommandation consolidée | Source(s) | Décision | Motivation et conséquence observable |
|---|---|---|---|
| Garder `calculate(left, operator, right)` pure, sans parsing, lecture ni affichage | SA-01, SA-02, deux contradictions | Retenue | Sépare le contrat Python de l'interface et rend l'import/test direct sans effet de bord. |
| Accepter exactement `+`, `-`, `*` et `/` par branchement explicite | SA-01, SA-02 | Retenue | Une liste blanche minimale préserve `ValueError` pour tout autre opérateur et évite tout mécanisme dynamique. |
| Accepter naturellement les `int` et `float`, sans convertir des chaînes dans `calculate` | SA-01, contradictions | Retenue | Le parsing appartient à la CLI ; les opérations Python prennent déjà en charge entiers, décimaux et négatifs. |
| Exiger l'opérateur exact dans l'API | SA-01, contradictions | Retenue | `" + "` reste un opérateur inconnu lors d'un appel direct ; seuls les espaces de la ligne CLI sont structurants. |
| Laisser `calculate` lever `ZeroDivisionError` pour `0`, `0.0` et `-0.0` | SA-01, SA-02 | Retenue | Le test numérique exact `right == 0` correspond au contrat, sans tolérance arbitraire. |
| Utiliser une fonction interne de parsing et une fonction `main()` distincte | SA-02, contradictions | Retenue | Cette architecture minimale isole calcul, syntaxe et orchestration interactive. |
| Exiger exactement trois éléments, séparés par des espaces blancs souples | SA-01 révisé, SA-02 révisé | Retenue | `line.strip().split()` accepte espaces multiples, tabulations et bords ; `-2 * -3.5` est valide, tandis que `2+3` et les expressions composées sont rejetées sans ambiguïté. |
| Accepter la forme compacte `2+3` ou `-2*-3` | SA-01 initial, option ensuite révisée | Écartée | Elle n'est pas exigée et nécessiterait une analyse lexicale plus complexe pour distinguer signes et opérateurs. |
| Convertir les opérandes CLI avec `float` | SA-02 | Retenue | Cela couvre entiers, décimaux, signes et notation scientifique avec la bibliothèque standard. |
| Rejeter explicitement `nan` et `inf` | SA-01 et SA-02, option discutée | Écartée | Le contrat ne définit pas cette politique ; la conversion standard `float` est conservée et ces formes ne sont pas promises dans la documentation. |
| Afficher la représentation Python du résultat, sans convertir `5.0` en `5` | SA-02 | Retenue | Aucun format exact n'est imposé ; cette sortie est simple, stable et fidèle au calcul flottant. |
| Reconnaître `quit` et `exit` après retrait des espaces périphériques | SA-01, SA-02 | Retenue | Les commandes contractuelles terminent proprement, y compris avec des espaces accidentels. |
| Rendre les commandes de sortie insensibles à la casse | SA-01 et SA-02, confort facultatif | Écartée | La casse n'est pas spécifiée ; le comportement reste limité aux commandes exactes documentées. |
| Traiter EOF comme une sortie propre | SA-01, SA-02, contradictions | Retenue | Évite un traceback en entrée redirigée ou avec Ctrl-D et facilite les tests d'intégration. |
| Traiter aussi `KeyboardInterrupt` comme une sortie propre | SA-01, SA-02, confort facultatif | Retenue | Ctrl-C est une interruption utilisateur attendue ; sa capture au bord de la CLI n'altère pas le contrat métier. |
| Capturer uniquement les erreurs utilisateur attendues | SA-01, SA-02 | Retenue | La boucle traite `ValueError` et `ZeroDivisionError`, poursuit après erreur et ne masque pas les défauts de programmation par un `except Exception`. |
| Distinguer syntaxe CLI invalide et opérateur API inconnu | SA-01 révisé | Retenue | Le parseur vérifie la structure et les nombres ; un opérateur occupant le bon emplacement atteint `calculate`, qui conserve son `ValueError` contractuel. |
| Fournir des messages compréhensibles, stables et sans détails internes | SA-01, SA-02 | Retenue | Les erreurs sont préfixées par `Erreur :`, aucun traceback ni contenu intégral potentiellement démesuré n'est affiché. |
| Ajouter une limite arbitraire de longueur d'entrée | SA-01, option de durcissement | Écartée | Le cahier des charges ne fixe aucune limite ; le parsing retenu est structurellement simple et n'ajoute pas de politique imprévisible. |
| Protéger l'exécution par `if __name__ == "__main__"` | SA-01, SA-02 | Retenue | Importer le module expose `calculate` sans démarrer la boucle interactive. |
| N'utiliser ni évaluation dynamique, ni sous-processus, ni effet système | SA-01, SA-02 | Retenue | Le programme repose uniquement sur découpage, `float` et branchements explicites ; `eval`, `exec` et mécanismes équivalents sont absents. |
| Documenter les quatre opérations, un négatif, une erreur et les sorties | SA-01 | Retenue | Le README décrira uniquement la syntaxe et les capacités réellement implémentées. |
| Tester calcul, import, parsing et séquence CLI avec reprise après erreurs | SA-02, contradictions | Retenue pour les contrôles ciblés | Ces contrôles seront effectués sans lancer le vérificateur officiel avant la critique SA-03. |

## Périmètre de cette première phase

`DECISIONS.md` est exigé par le protocole V2 comme trace d'arbitrage, en plus
des deux livrables fonctionnels du défi. La première solution sera complète,
mais le vérificateur officiel restera réservé à la phase suivant la critique
SA-03.

--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Calculator

Cette calculatrice Python exécute une opération binaire parmi l'addition, la
soustraction, la multiplication et la division. Elle n'utilise que la
bibliothèque standard.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/calculator.py
```

La calculatrice reste active jusqu'à la saisie de `quit` ou `exit`. Une fin de
flux (Ctrl-D) ou une interruption (Ctrl-C) la termine également proprement.

## Utilisation

Saisir exactement deux nombres et un opérateur, séparés par un ou plusieurs
espaces :

```text
2 + 3
10 - 4
-2 * -3.5
7 / 2
```

Les opérateurs disponibles sont uniquement `+`, `-`, `*` et `/`. Les entiers,
les nombres décimaux et les nombres négatifs sont acceptés. Les formes sans
espaces, comme `2+3`, et les expressions composées ne font pas partie de la
syntaxe prise en charge.

Exemple de session :

```text
Expression (ou 'quit'/'exit') : 2 + 3
5.0
Expression (ou 'quit'/'exit') : -2 * -3.5
7.0
Expression (ou 'quit'/'exit') : 4 / 0
Erreur : division par zéro impossible
Expression (ou 'quit'/'exit') : 2+3
Erreur : format attendu : nombre opérateur nombre
Expression (ou 'quit'/'exit') : quit
```

Une saisie incorrecte ou une division par zéro produit un message d'erreur,
sans traceback, puis la calculatrice attend l'expression suivante.

## Utilisation comme module

La logique métier peut être importée sans démarrer l'interface interactive :

```python
from calculator import calculate

result = calculate(6, "/", 4)
print(result)  # 1.5
```

`calculate(left, operator, right)` lève `ValueError` pour un opérateur inconnu
et `ZeroDivisionError` pour une division par zéro.

--- END FILE solution/README.md ---

--- BEGIN FILE solution/calculator.py ---
"""Calculatrice binaire simple et interface en ligne de commande."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération arithmétique binaire.

    Args:
        left: Opérande de gauche.
        operator: L'un des opérateurs ``+``, ``-``, ``*`` ou ``/``.
        right: Opérande de droite.

    Returns:
        Le résultat de l'opération.

    Raises:
        ValueError: Si l'opérateur n'est pas pris en charge.
        ZeroDivisionError: Si une division par zéro est demandée.
    """
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro impossible")
        return left / right
    raise ValueError("opérateur inconnu (utilisez +, -, * ou /)")


def _parse_expression(line: str) -> tuple[float, str, float]:
    """Analyse une expression composée de deux nombres et d'un opérateur."""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("format attendu : nombre opérateur nombre")

    left_text, operator, right_text = parts
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        raise ValueError("les opérandes doivent être des nombres") from None

    return left, operator, right


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""
    while True:
        try:
            line = input("Expression (ou 'quit'/'exit') : ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if line.strip() in {"quit", "exit"}:
            break

        try:
            left, operator, right = _parse_expression(line)
            result = calculate(left, operator, right)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}")
            continue

        print(result)


if __name__ == "__main__":
    main()

--- END FILE solution/calculator.py ---

--- END FIRST SOLUTION ---
````

</details>

#### Texte retourné pour MSG-006, mot pour mot

````text
## Défauts confirmés

1. **Livrable supplémentaire contraire au challenge — sévérité élevée.**  
   Le défi demande de créer « exclusivement » `calculator.py` et `README.md` dans `solution/`. La présence de `DECISIONS.md` viole littéralement cette contrainte. L’affirmation selon laquelle ce fichier serait exigé par le protocole V2 n’est étayée par aucune exigence du challenge fourni. Un vérificateur qui contrôle la liste des fichiers peut donc rejeter la solution.

2. **Exemple d’import incohérent avec le répertoire de lancement — sévérité moyenne.**  
   Le README se place « depuis la racine du dépôt », mais montre ensuite :

   ```python
   from calculator import calculate
   ```

   Depuis cette racine, `calculator.py` se trouve dans `solution/` et n’est normalement pas un module de premier niveau. L’exemple peut donc produire `ModuleNotFoundError` sans changement de répertoire ou adaptation du chemin d’import. La documentation ne fournit pas le contexte nécessaire pour rendre cet exemple reproductible.

3. **Garantie Ctrl-C trop large dans le README — sévérité faible.**  
   Le texte affirme qu’une interruption Ctrl-C termine proprement le programme. Or `KeyboardInterrupt` n’est capturée qu’autour de `input()`. Si elle survient pendant le parsing, le calcul ou l’affichage, elle peut produire un traceback. Le comportement habituel au repos sera propre, mais la garantie documentaire est plus forte que l’implémentation.

## Risques

1. **Type de retour de l’API.**  
   Avec des arguments `int`, `+`, `-` et `*` retournent un `int`, malgré l’annotation `-> float`. Le challenge peut être interprété comme exigeant seulement un résultat numérique, auquel cas cela convient. Un contrôle strict de `type(result) is float` échouerait néanmoins.

2. **Valeurs non finies acceptées implicitement.**  
   `float()` accepte notamment `nan`, `inf` et des exposants débordant vers l’infini. La CLI peut donc afficher `nan` ou `inf`, alors que le README parle de nombres entiers et décimaux ordinaires. Ce n’est pas une faille d’exécution de code, mais cela élargit silencieusement le domaine et peut donner des résultats arithmétiques surprenants, notamment `inf * 0 -> nan`.

3. **Consommation de ressources sur entrée démesurée.**  
   Aucune limite de longueur n’est appliquée avant `split()` et `float()`. Une entrée gigantesque peut consommer mémoire et CPU, et éventuellement déclencher une exception non capturée telle que `MemoryError`. La surface reste limitée à une CLI locale, donc ce risque est faible dans le contexte attendu.

4. **Compatibilité Python non déclarée.**  
   L’annotation `tuple[float, str, float]` nécessite Python 3.9 ou ultérieur. Le challenge ne fixe pas de version minimale au-delà de `python3`. Sur un environnement Python 3.8, le module échouerait dès l’import.

5. **Validation encore non démontrée.**  
   `DECISIONS.md` annonce des contrôles ciblés et reporte le vérificateur officiel, mais aucun résultat de test n’est fourni dans les éléments examinés. Il subsiste donc un risque de régression d’intégration, notamment sur la continuité après plusieurs erreurs, EOF, absence de traceback et import sans effet. Ce n’est pas encore une non-conformité puisque cette critique intervient avant la phase de vérification annoncée.

6. **API permissive hors annotations.**  
   `calculate` ne vérifie pas les types. Par exemple, certains appels avec des chaînes peuvent effectuer concaténation ou répétition au lieu d’échouer immédiatement. Les paramètres étant contractuellement typés `float`, ce comportement hors contrat n’est pas un défaut certain, mais il contredit partiellement la décision affirmant que l’API accepte des `int` et `float` sans préciser qu’elle accepte aussi, accidentellement, d’autres objets.

## Préférences, pas défauts

- Rejeter `2+3` est compatible avec la forme espacée explicitement donnée et avec l’arbitrage documenté.
- Garder `quit` et `exit` sensibles à la casse est acceptable.
- Afficher `5.0` plutôt que `5` est acceptable puisqu’aucun format exact n’est imposé.
- Un message commun préfixé par `Erreur :` est suffisamment compréhensible.
- L’acceptation d’espaces multiples et de tabulations est une extension raisonnable.
- Le cœur nominal est correctement séparé, protégé à l’import, sans `eval()`/`exec()`, et préserve bien `ValueError` et `ZeroDivisionError` pour les appels contractuels.
````

### MSG-007 — arbitrage final et vérification

Direction : `RELAY → MAIN`. Réponse visible : 490 mots.

<details>
<summary>Texte envoyé, mot pour mot</summary>

````text
AgentBench V2 — phase MAIN finale. Tu représentes le même rôle MAIN, orchestrateur candidat et unique écrivain, dans une nouvelle session éphémère mesurée. Aucun nouveau consultant n'est autorisé. Reprends la première solution présente dans `solution/`. Qualifie chaque point de SA-03 comme retenu, écarté ou non vérifiable et complète `solution/DECISIONS.md` avec la justification et la preuve. Applique uniquement les corrections retenues. Exécute ensuite le vérificateur officiel exactement ainsi : `python3 scripts/verify.py --solution runs/sol-core-v2-001/solution`. Corrige les défauts confirmés jusqu'au verdict final. Écris uniquement dans `solution/`, n'effectue aucune opération Git et restitue rôles, arbitrages, premier passage, verdict final, corrections et limites.
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
# Défi 001 — Calculator

## Objectif

Développer une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.

## Livrables

Créer exclusivement dans le dossier `solution/` :

- `calculator.py` : logique métier et interface CLI ;
- `README.md` : lancement, utilisation et exemples.

## Contrat Python

`calculator.py` doit exposer :

```python
def calculate(left: float, operator: str, right: float) -> float:
    ...
```

Comportements attendus :

- accepter entiers, décimaux et nombres négatifs ;
- prendre en charge exactement `+`, `-`, `*` et `/` ;
- lever `ValueError` pour une opération inconnue ;
- lever `ZeroDivisionError` pour une division par zéro ;
- ne jamais utiliser `eval()` ou `exec()`.

## Contrat CLI

La commande suivante doit lancer une boucle interactive :

```bash
python3 solution/calculator.py
```

Chaque ligne saisie contient une expression sous la forme :

```text
2 + 3
```

Les commandes `quit` et `exit` terminent proprement le programme.

En cas d'expression invalide ou de division par zéro :

- afficher un message d'erreur compréhensible ;
- ne jamais afficher de traceback ;
- poursuivre la boucle jusqu'à une commande de sortie.

## Contraintes

- bibliothèque standard Python uniquement ;
- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;
- ne pas modifier le cahier des charges ni les tests.

## Vérification

Depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/<identifiant>/solution
```

--- END CHALLENGE ---

--- BEGIN CONSULTATIONS ---

--- BEGIN SA01_INITIAL ---
## Avis SA-01 — exigences et sécurité

### 1. Obligations certaines

Le livrable doit être limité à deux fichiers dans `solution/` :

- `calculator.py`, contenant la logique métier et la boucle interactive ;
- `README.md`, décrivant lancement, utilisation et exemples.

L’API publique exigée est exactement :

```python
calculate(left: float, operator: str, right: float) -> float
```

Le comportement métier obligatoire est le suivant :

- reconnaître uniquement `+`, `-`, `*` et `/` ;
- accepter des opérandes positifs, négatifs, entiers ou décimaux ;
- lever `ValueError` pour tout opérateur non reconnu ;
- lever `ZeroDivisionError` lorsque le diviseur est nul ;
- ne jamais employer `eval()` ni `exec()`.

La CLI doit :

- être lancée par `python3 solution/calculator.py` ;
- traiter plusieurs expressions successives ;
- reconnaître `quit` et `exit` ;
- intercepter les saisies invalides et divisions par zéro ;
- afficher un diagnostic compréhensible sans traceback ;
- rester active après l’erreur.

Seule la bibliothèque standard est autorisée. Le cahier des charges et les tests sont immuables.

### 2. Ambiguïtés à arbitrer

| Sujet | Ambiguïté | Recommandation prudente |
|---|---|---|
| Grammaire | « sous la forme `2 + 3` » ne précise pas si les espaces sont obligatoires | Accepter toute séparation raisonnable, notamment espaces multiples et espaces périphériques, sans élargir la grammaire à des expressions composées |
| Nombres signés | Les nombres négatifs sont requis, mais `-2*-3` sans espaces n’est pas explicitement exigé | Garantir au minimum `-2 * -3`; accepter la forme compacte seulement si le parseur reste simple et non ambigu |
| Arithmétique | L’annotation `float` ne dit pas si les appels directs avec des `int` doivent fonctionner | Les accepter naturellement, puisque le contrat mentionne les entiers |
| Conversion API | Le contrat ne précise pas si `calculate("2", "+", "3")` doit convertir les chaînes | Ne pas promettre cette conversion : le parsing appartient à la CLI, l’API reçoit des nombres |
| Espaces opérateur | Le traitement de `" + "` par l’API n’est pas défini | Exiger l’opérateur exact dans `calculate`; normaliser seulement au niveau CLI |
| Casse des sorties | `QUIT`, `Exit` et espaces autour des commandes ne sont pas spécifiés | Accepter au moins les commandes exactes après suppression des espaces périphériques; l’insensibilité à la casse est un confort facultatif |
| Fin de fichier | Le comportement sur EOF/Ctrl-D n’est pas défini | Le traiter comme une sortie propre, sans traceback |
| Interruption | Ctrl-C n’est pas couvert | Une sortie propre est souhaitable, mais ne doit pas compromettre les obligations centrales |
| Valeurs spéciales | `nan`, `inf`, notation scientifique, virgule décimale et dépassements ne sont pas définis | Ne pas les revendiquer dans le README; accepter la notation Python seulement si cela découle du mécanisme de conversion retenu |
| Texte exact | Aucun message, invite ou format de résultat précis n’est imposé | Employer des libellés stables et compréhensibles; éviter de supposer une correspondance textuelle non annoncée |

### 3. Erreurs de conception à éviter

- Confondre erreur de syntaxe CLI et opérateur inconnu de l’API. `calculate` doit conserver son exception contractuelle, tandis que la boucle traduit les exceptions en messages.
- Intercepter toutes les exceptions avec un `except` trop large : cela cacherait les défauts de programmation et compliquerait le diagnostic.
- Tester la division par zéro au moyen d’une approximation. Le contrat porte sur zéro ; `0.0` et `-0.0` doivent être reconnus par la sémantique numérique normale.
- Utiliser une séparation naïve sur les espaces si elle rejette des variantes raisonnables ou produit des diagnostics incohérents.
- Accepter plusieurs opérateurs ou des expressions imbriquées : le défi demande une seule opération binaire, pas un interpréteur arithmétique général.
- Exécuter la boucle lors de l’import du module. Les vérificateurs doivent pouvoir importer `calculate` sans bloquer sur une saisie.
- Retourner une chaîne depuis `calculate` ou y imprimer le résultat : la fonction doit rester une logique métier retournant une valeur numérique.
- Documenter des capacités absentes ou des formats non garantis.

### 4. Surfaces d’attaque

La principale surface est l’entrée utilisateur arbitraire. Toute interprétation dynamique est injustifiée : `eval`, `exec`, compilation de code, lancement de sous-processus, import construit depuis l’entrée ou accès au système de fichiers doivent être exclus. Une liste blanche stricte des quatre opérateurs réduit fortement le risque.

Une entrée extrêmement longue peut provoquer une consommation excessive de mémoire ou de CPU pendant le parsing numérique. Le cahier des charges n’impose pas de limite ; une protection explicite serait défendable, mais risque d’introduire un comportement non testé. Pour ce défi local, privilégier un parseur borné en structure et sans algorithme complexe.

Les messages d’erreur ne doivent pas inclure de traceback, de détails internes, de chemins locaux ou de représentation intégrale d’une entrée démesurée. Aucun secret ni journal persistant n’est nécessaire.

Les valeurs flottantes spéciales peuvent produire des résultats surprenants, mais elles ne créent pas ici d’exécution de code. Leur exclusion éventuelle constituerait une politique supplémentaire non demandée.

### 5. Arbitrages proposés au candidat principal

1. **Grammaire recommandée :** une expression binaire composée de deux littéraux numériques et d’un opérateur autorisé, avec espaces souples.
2. **Séparation des responsabilités :** conversion et validation syntaxique dans la CLI ; calcul et exceptions contractuelles dans `calculate`.
3. **Robustesse :** sortie propre sur `quit`, `exit` et EOF ; reprise après les seules erreurs utilisateur anticipées.
4. **Sécurité :** liste blanche explicite, aucune évaluation dynamique, aucun effet externe.
5. **Compatibilité vérificateur :** protéger le point d’entrée afin que l’import soit sans effet interactif.
6. **Documentation :** montrer les quatre opérations, un nombre négatif, une erreur et les commandes de sortie, sans promettre les cas ambigus.

### Conclusion

Le challenge est cohérent et réalisable. Son principal risque n’est pas l’arithmétique, mais un parseur trop permissif ou trop dépendant d’un format d’espacement, ainsi qu’une mauvaise séparation entre exceptions de l’API et présentation CLI. L’arbitrage le plus sûr est une grammaire binaire limitée, une liste blanche stricte et une gestion ciblée des erreurs utilisateur.
--- END SA01_INITIAL ---

--- BEGIN SA02_INITIAL ---
## Objectif de l’avis

Proposer une architecture minimale, testable et conforme, puis identifier les décisions que l’agent principal doit arbitrer explicitement. Aucun comportement du vérificateur non fourni ne doit être présumé.

## Architecture recommandée

Séparer quatre responsabilités dans `calculator.py` :

1. `calculate(left, operator, right)`  
   Fonction métier pure, sans entrée/sortie ni conversion de chaînes.

2. Une fonction interne d’analyse d’expression  
   Transforme une ligne en deux nombres et un opérateur, ou lève `ValueError`.

3. Une fonction de boucle interactive, idéalement `main()`  
   Lit les lignes, traite les commandes de sortie, appelle l’analyseur puis `calculate`, et affiche résultat ou erreur.

4. Un garde d’exécution  
   La boucle ne doit démarrer que lors de l’exécution directe. Importer `calculator` pour tester `calculate` ne doit produire ni affichage ni attente interactive.

Cette séparation permet de tester indépendamment calcul, syntaxe et comportement CLI, sans surarchitecture.

## Invariants à préserver

### Fonction métier

- Seuls les opérateurs `+`, `-`, `*` et `/` sont reconnus.
- Tout autre opérateur entraîne `ValueError`, sans substitution implicite.
- La division par toute valeur égale à zéro, notamment `0`, `0.0` et `-0.0`, entraîne `ZeroDivisionError`.
- Les quatre opérations suivent directement la sémantique numérique Python.
- La fonction ne capture pas les erreurs qu’elle doit contractuellement exposer.
- Aucun `eval()`, `exec()` ou mécanisme équivalent n’est nécessaire.
- Aucun affichage ni lecture interactive ne doit se trouver dans `calculate`.

Un branchement explicite (`if`/`elif`) ou une table locale d’opérations convient. Le branchement explicite réduit ici les risques de comportement indirect.

### CLI

Pour chaque ligne :

- supprimer les espaces périphériques ;
- reconnaître `quit` et `exit` avant l’analyse de l’expression ;
- exiger une expression complète et non ambiguë ;
- convertir les deux opérandes en nombres ;
- afficher un résultat pour une expression valide ;
- pour une syntaxe invalide, un nombre invalide, un opérateur inconnu ou une division par zéro, afficher un message compréhensible puis recommencer ;
- ne laisser aucun traceback atteindre l’utilisateur pour ces erreurs attendues.

Les exceptions devraient être capturées au niveau de la boucle, au plus près de la frontière CLI. Éviter `except Exception`, qui masquerait des défauts de programmation.

## Arbitrages proposés

### A1 — Grammaire d’entrée

**Recommandation :** accepter exactement trois éléments séparés par des espaces, conformément à la forme documentée `2 + 3`.

Conséquences :

- `-2 * -3.5` fonctionne naturellement ;
- `2+3`, `2 +`, `2 + 3 4` et une ligne vide sont invalides ;
- le parseur reste déterministe et facile à expliquer.

Accepter aussi les expressions sans espaces demanderait un véritable analyseur, surtout pour distinguer opérateurs et signes négatifs. Ce surcroît de complexité n’est pas exigé.

### A2 — Format numérique

**Recommandation :** utiliser la conversion standard vers `float`, cohérente avec la signature publiée.

Elle couvre entiers, décimaux, signes négatifs et notation scientifique. Le contrat ne précise pas si `nan` et `inf` doivent être acceptés. Deux choix sont défendables :

- accepter toute syntaxe comprise par `float` : solution minimale et idiomatique ;
- refuser explicitement les valeurs non finies : grammaire utilisateur plus étroite, mais règle supplémentaire absente du contrat.

Arbitrage conseillé : ne pas ajouter de rejet des valeurs non finies sans exigence du vérificateur.

### A3 — Présentation du résultat

**Recommandation :** afficher directement le résultat numérique selon sa représentation Python.

Ne pas transformer automatiquement `5.0` en `5` : le format exact n’est pas spécifié, et une normalisation introduirait une politique supplémentaire.

### A4 — Fin de flux

**Recommandation :** traiter également EOF comme une sortie propre. C’est utile pour les tests par sous-processus et les entrées redirigées. La gestion de `KeyboardInterrupt` est facultative ; si elle est ajoutée, elle doit terminer sans traceback.

Les commandes de sortie devraient probablement être reconnues après suppression des espaces. La casse n’est pas spécifiée : rester strictement sur `quit` et `exit` évite d’étendre silencieusement le contrat.

## Stratégie de validation

### Tests unitaires de `calculate`

Couvrir au minimum :

- addition, soustraction, multiplication et division ;
- entiers, décimaux et nombres négatifs ;
- ordre des opérandes, par exemple une soustraction non commutative ;
- résultat négatif ;
- division donnant un décimal ;
- opérateurs invalides : chaîne vide, `%`, `//`, `**`, variante entourée d’espaces ;
- division par `0`, `0.0` et `-0.0` ;
- type exact des exceptions contractuelles.

Vérifier aussi que l’import du module ne lance pas la CLI.

### Tests du parseur

Couvrir :

- `2 + 3`, espaces périphériques et espaces multiples ;
- opérandes négatifs ;
- ligne vide ;
- opérande non numérique ;
- opérateur manquant ;
- opérande manquante ou surnuméraire ;
- expression accolée `2+3`, selon l’arbitrage A1.

### Tests d’intégration CLI

Piloter le programme avec une séquence d’entrée contenant :

1. une expression valide ;
2. une expression invalide ;
3. une division par zéro ;
4. une autre expression valide ;
5. `quit` ou `exit`.

Les assertions essentielles sont :

- les deux résultats valides apparaissent ;
- les erreurs sont compréhensibles ;
- aucun texte `Traceback` n’apparaît ;
- la boucle continue après chaque erreur ;
- le processus termine normalement après la commande de sortie.

Effectuer le contrôle imposé depuis la racine avec la commande exacte du challenge.

## Cas sensibles

- Confondre le signe négatif avec l’opérateur.
- Autoriser accidentellement des opérateurs supplémentaires.
- Capturer `ZeroDivisionError` dans `calculate`, ce qui violerait son contrat.
- Démarrer la boucle lors de l’import.
- Quitter la boucle après la première erreur.
- Afficher l’objet exception sans préfixe explicatif, potentiellement peu clair.
- Documenter dans le README une syntaxe que le parseur n’accepte pas.
- Placer d’autres livrables dans `solution/`, alors que seuls les deux fichiers demandés sont annoncés.

## Conclusion d’arbitrage

Retenir une solution volontairement étroite : fonction métier pure, parseur à trois éléments espacés, boucle `main()` résiliente, exceptions contractuelles préservées et tests CLI par séquences. Le principal point à consigner est le choix de ne pas prendre en charge `2+3`, puisque cette extension n’est pas requise et complexifie surtout la gestion fiable des nombres négatifs.
--- END SA02_INITIAL ---

--- BEGIN SA01_CROSS ---
## Révision SA-01 après avis SA-02

Les deux avis convergent largement. Ils confirment les mêmes invariants essentiels : `calculate` doit rester pure, n’accepter que quatre opérateurs, préserver `ValueError` et `ZeroDivisionError`, et être séparée du parsing et de la boucle interactive. Ils s’accordent aussi sur le garde d’exécution, la reprise après erreur, l’absence de traceback, la liste blanche stricte, l’interdiction d’`eval()`/`exec()`, le traitement propre d’EOF et l’usage d’exceptions ciblées.

Le principal désaccord utile concerne la grammaire CLI. Mon avis initial recommandait des « espaces souples » et envisageait les formes compactes si elles restaient simples. SA-02 recommande exactement trois éléments séparés par des espaces. Je révise ma recommandation en faveur de SA-02 : accepter les espaces périphériques et multiples, mais exiger trois éléments après découpage — opérande, opérateur, opérande. Ainsi, `-2 * -3.5` est valide et `2+3` ne l’est pas. Cette règle est déterministe, documentable et évite de transformer le défi en problème d’analyse lexicale des signes et opérateurs. L’absence de prise en charge de `2+3` doit être cohérente entre code et README.

Un second point mérite précision : « opérateur inconnu » et « syntaxe invalide » restent deux niveaux distincts. `2 % 3`, composé de trois éléments valides structurellement, devrait atteindre `calculate` et produire son `ValueError`, ensuite traduit par la CLI. `2+3` ou `2 +` relève du parseur. La CLI peut présenter un diagnostic commun si aucun texte exact n’est imposé, mais l’API doit conserver les exceptions contractuelles.

Les doublons entre avis sont nombreux et renforcent leur priorité : ne pas lancer la CLI à l’import, ne pas capturer `Exception`, ne pas quitter après une erreur, ne pas ajouter d’opérateurs, ne pas imprimer depuis `calculate`, ne pas documenter de capacités absentes et ne pas introduire d’effets externes. Les propositions sur EOF, `nan`/`inf`, la casse des commandes et Ctrl-C sont également concordantes : EOF est une robustesse utile ; les autres extensions sont facultatives et ne doivent pas devenir des politiques non demandées.

Priorités finales :

1. Préserver exactement le contrat observable de `calculate` et ses exceptions.
2. Employer une grammaire CLI stricte à trois éléments séparés par des espaces.
3. Isoler parsing, calcul, boucle interactive et garde d’exécution.
4. Capturer uniquement les erreurs utilisateur attendues et poursuivre la boucle.
5. Exclure toute interprétation dynamique, effet système ou fuite de détails internes.
6. Aligner strictement le README sur le comportement réellement fourni.
7. Valider import, quatre opérations, nombres négatifs, erreurs, reprise et sortie propre avec la commande imposée.

La surface d’attaque demeure faible si l’entrée reste structurellement bornée et traitée uniquement par découpage, conversion numérique et liste blanche.
--- END SA01_CROSS ---

--- BEGIN SA02_CROSS ---
## Avis consolidé SA-02 — confirmation avec révision mineure

Je confirme l’architecture initiale et l’essentiel de l’avis SA-01. Les deux analyses convergent sur les invariants déterminants :

- `calculate(left, operator, right)` reste pure, reçoit des nombres et ne réalise ni parsing, ni affichage ;
- seuls `+`, `-`, `*` et `/` sont admis ;
- `ValueError` et `ZeroDivisionError` restent observables lors des appels directs ;
- la CLI traduit uniquement les erreurs utilisateur attendues en messages compréhensibles, puis poursuit la boucle ;
- l’import du module reste sans effet grâce au garde d’exécution ;
- aucune évaluation dynamique, dépendance externe ou capture générale avec `except Exception` ;
- `quit`, `exit` et EOF provoquent une sortie propre.

### Désaccord utile et révision

Le seul désaccord réel concerne la formulation de la grammaire. Mon avis initial recommandait « exactement trois éléments séparés par des espaces ». SA-01 recommande des « espaces souples » et avertit contre une séparation naïve.

Je révise la formulation, mais pas le périmètre fonctionnel : utiliser une décomposition structurelle équivalente à `line.strip().split()` et exiger exactement trois éléments. Cela accepte naturellement les espaces périphériques, plusieurs espaces et les tabulations, tout en rejetant `2+3`, les expressions incomplètes et les éléments surnuméraires.

Ainsi, « espaces souples » ne doit pas être interprété comme l’obligation d’accepter les formes compactes. Étendre le parseur à `-2*-3` créerait une complexité inutile autour des signes et des opérateurs sans exigence explicite. Le README doit annoncer précisément la forme effectivement acceptée.

### Doublons à fusionner

Les recommandations suivantes sont identiques dans les deux avis et ne nécessitent qu’une seule décision :

- séparation calcul/parsing/CLI ;
- liste blanche des opérateurs ;
- opérateur exact dans l’API, normalisation uniquement dans la CLI ;
- acceptation naturelle des `int` par `calculate`, sans conversion de chaînes ;
- gestion de `0.0` et `-0.0` par comparaison exacte à zéro ;
- sortie propre sur EOF ;
- absence de traceback et reprise après erreur ;
- non-promesse des cas non spécifiés (`nan`, `inf`, casse des commandes, syntaxe compacte).

La surface d’attaque décrite par SA-01 confirme l’architecture proposée : un parseur structurellement borné et une sélection explicite des opérateurs suffisent. Une limite arbitraire de longueur d’entrée ajouterait une politique non demandée et reste secondaire.

### Priorités recommandées

1. Respect exact du contrat public de `calculate` et de ses exceptions.
2. Import sans effet interactif.
3. Boucle CLI résiliente avec captures ciblées.
4. Parseur à exactement trois éléments, avec espaces blancs souples.
5. Validation unitaire et intégrée, notamment continuité après deux erreurs successives.
6. Cohérence stricte entre README et comportement.
7. Conforts facultatifs — Ctrl-C, commandes insensibles à la casse, valeurs non finies — seulement après réussite des contrôles obligatoires.

Le cas d’intégration le plus discriminant reste : succès, saisie invalide, division par zéro, nouveau succès, sortie, avec absence de `Traceback` et terminaison normale.
--- END SA02_CROSS ---

--- END CONSULTATIONS ---

--- BEGIN FIRST SOLUTION SNAPSHOT ---

--- BEGIN FILE solution/DECISIONS.md ---
# Arbitrages de conception

Ce document synthétise les quatre avis consultatifs reçus avant
l'implémentation : avis initial de SA-01, avis initial de SA-02, contradiction
de SA-01, puis contradiction de SA-02. Le candidat principal reste seul
décideur et seul écrivain.

| Recommandation consolidée | Source(s) | Décision | Motivation et conséquence observable |
|---|---|---|---|
| Garder `calculate(left, operator, right)` pure, sans parsing, lecture ni affichage | SA-01, SA-02, deux contradictions | Retenue | Sépare le contrat Python de l'interface et rend l'import/test direct sans effet de bord. |
| Accepter exactement `+`, `-`, `*` et `/` par branchement explicite | SA-01, SA-02 | Retenue | Une liste blanche minimale préserve `ValueError` pour tout autre opérateur et évite tout mécanisme dynamique. |
| Accepter naturellement les `int` et `float`, sans convertir des chaînes dans `calculate` | SA-01, contradictions | Retenue | Le parsing appartient à la CLI ; les opérations Python prennent déjà en charge entiers, décimaux et négatifs. |
| Exiger l'opérateur exact dans l'API | SA-01, contradictions | Retenue | `" + "` reste un opérateur inconnu lors d'un appel direct ; seuls les espaces de la ligne CLI sont structurants. |
| Laisser `calculate` lever `ZeroDivisionError` pour `0`, `0.0` et `-0.0` | SA-01, SA-02 | Retenue | Le test numérique exact `right == 0` correspond au contrat, sans tolérance arbitraire. |
| Utiliser une fonction interne de parsing et une fonction `main()` distincte | SA-02, contradictions | Retenue | Cette architecture minimale isole calcul, syntaxe et orchestration interactive. |
| Exiger exactement trois éléments, séparés par des espaces blancs souples | SA-01 révisé, SA-02 révisé | Retenue | `line.strip().split()` accepte espaces multiples, tabulations et bords ; `-2 * -3.5` est valide, tandis que `2+3` et les expressions composées sont rejetées sans ambiguïté. |
| Accepter la forme compacte `2+3` ou `-2*-3` | SA-01 initial, option ensuite révisée | Écartée | Elle n'est pas exigée et nécessiterait une analyse lexicale plus complexe pour distinguer signes et opérateurs. |
| Convertir les opérandes CLI avec `float` | SA-02 | Retenue | Cela couvre entiers, décimaux, signes et notation scientifique avec la bibliothèque standard. |
| Rejeter explicitement `nan` et `inf` | SA-01 et SA-02, option discutée | Écartée | Le contrat ne définit pas cette politique ; la conversion standard `float` est conservée et ces formes ne sont pas promises dans la documentation. |
| Afficher la représentation Python du résultat, sans convertir `5.0` en `5` | SA-02 | Retenue | Aucun format exact n'est imposé ; cette sortie est simple, stable et fidèle au calcul flottant. |
| Reconnaître `quit` et `exit` après retrait des espaces périphériques | SA-01, SA-02 | Retenue | Les commandes contractuelles terminent proprement, y compris avec des espaces accidentels. |
| Rendre les commandes de sortie insensibles à la casse | SA-01 et SA-02, confort facultatif | Écartée | La casse n'est pas spécifiée ; le comportement reste limité aux commandes exactes documentées. |
| Traiter EOF comme une sortie propre | SA-01, SA-02, contradictions | Retenue | Évite un traceback en entrée redirigée ou avec Ctrl-D et facilite les tests d'intégration. |
| Traiter aussi `KeyboardInterrupt` comme une sortie propre | SA-01, SA-02, confort facultatif | Retenue | Ctrl-C est une interruption utilisateur attendue ; sa capture au bord de la CLI n'altère pas le contrat métier. |
| Capturer uniquement les erreurs utilisateur attendues | SA-01, SA-02 | Retenue | La boucle traite `ValueError` et `ZeroDivisionError`, poursuit après erreur et ne masque pas les défauts de programmation par un `except Exception`. |
| Distinguer syntaxe CLI invalide et opérateur API inconnu | SA-01 révisé | Retenue | Le parseur vérifie la structure et les nombres ; un opérateur occupant le bon emplacement atteint `calculate`, qui conserve son `ValueError` contractuel. |
| Fournir des messages compréhensibles, stables et sans détails internes | SA-01, SA-02 | Retenue | Les erreurs sont préfixées par `Erreur :`, aucun traceback ni contenu intégral potentiellement démesuré n'est affiché. |
| Ajouter une limite arbitraire de longueur d'entrée | SA-01, option de durcissement | Écartée | Le cahier des charges ne fixe aucune limite ; le parsing retenu est structurellement simple et n'ajoute pas de politique imprévisible. |
| Protéger l'exécution par `if __name__ == "__main__"` | SA-01, SA-02 | Retenue | Importer le module expose `calculate` sans démarrer la boucle interactive. |
| N'utiliser ni évaluation dynamique, ni sous-processus, ni effet système | SA-01, SA-02 | Retenue | Le programme repose uniquement sur découpage, `float` et branchements explicites ; `eval`, `exec` et mécanismes équivalents sont absents. |
| Documenter les quatre opérations, un négatif, une erreur et les sorties | SA-01 | Retenue | Le README décrira uniquement la syntaxe et les capacités réellement implémentées. |
| Tester calcul, import, parsing et séquence CLI avec reprise après erreurs | SA-02, contradictions | Retenue pour les contrôles ciblés | Ces contrôles seront effectués sans lancer le vérificateur officiel avant la critique SA-03. |

## Périmètre de cette première phase

`DECISIONS.md` est exigé par le protocole V2 comme trace d'arbitrage, en plus
des deux livrables fonctionnels du défi. La première solution sera complète,
mais le vérificateur officiel restera réservé à la phase suivant la critique
SA-03.

--- END FILE solution/DECISIONS.md ---

--- BEGIN FILE solution/README.md ---
# Calculator

Cette calculatrice Python exécute une opération binaire parmi l'addition, la
soustraction, la multiplication et la division. Elle n'utilise que la
bibliothèque standard.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/calculator.py
```

La calculatrice reste active jusqu'à la saisie de `quit` ou `exit`. Une fin de
flux (Ctrl-D) ou une interruption (Ctrl-C) la termine également proprement.

## Utilisation

Saisir exactement deux nombres et un opérateur, séparés par un ou plusieurs
espaces :

```text
2 + 3
10 - 4
-2 * -3.5
7 / 2
```

Les opérateurs disponibles sont uniquement `+`, `-`, `*` et `/`. Les entiers,
les nombres décimaux et les nombres négatifs sont acceptés. Les formes sans
espaces, comme `2+3`, et les expressions composées ne font pas partie de la
syntaxe prise en charge.

Exemple de session :

```text
Expression (ou 'quit'/'exit') : 2 + 3
5.0
Expression (ou 'quit'/'exit') : -2 * -3.5
7.0
Expression (ou 'quit'/'exit') : 4 / 0
Erreur : division par zéro impossible
Expression (ou 'quit'/'exit') : 2+3
Erreur : format attendu : nombre opérateur nombre
Expression (ou 'quit'/'exit') : quit
```

Une saisie incorrecte ou une division par zéro produit un message d'erreur,
sans traceback, puis la calculatrice attend l'expression suivante.

## Utilisation comme module

La logique métier peut être importée sans démarrer l'interface interactive :

```python
from calculator import calculate

result = calculate(6, "/", 4)
print(result)  # 1.5
```

`calculate(left, operator, right)` lève `ValueError` pour un opérateur inconnu
et `ZeroDivisionError` pour une division par zéro.

--- END FILE solution/README.md ---

--- BEGIN FILE solution/calculator.py ---
"""Calculatrice binaire simple et interface en ligne de commande."""


def calculate(left: float, operator: str, right: float) -> float:
    """Calcule une opération arithmétique binaire.

    Args:
        left: Opérande de gauche.
        operator: L'un des opérateurs ``+``, ``-``, ``*`` ou ``/``.
        right: Opérande de droite.

    Returns:
        Le résultat de l'opération.

    Raises:
        ValueError: Si l'opérateur n'est pas pris en charge.
        ZeroDivisionError: Si une division par zéro est demandée.
    """
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division par zéro impossible")
        return left / right
    raise ValueError("opérateur inconnu (utilisez +, -, * ou /)")


def _parse_expression(line: str) -> tuple[float, str, float]:
    """Analyse une expression composée de deux nombres et d'un opérateur."""
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError("format attendu : nombre opérateur nombre")

    left_text, operator, right_text = parts
    try:
        left = float(left_text)
        right = float(right_text)
    except ValueError:
        raise ValueError("les opérandes doivent être des nombres") from None

    return left, operator, right


def main() -> None:
    """Lance la boucle interactive de la calculatrice."""
    while True:
        try:
            line = input("Expression (ou 'quit'/'exit') : ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if line.strip() in {"quit", "exit"}:
            break

        try:
            left, operator, right = _parse_expression(line)
            result = calculate(left, operator, right)
        except (ValueError, ZeroDivisionError) as error:
            print(f"Erreur : {error}")
            continue

        print(result)


if __name__ == "__main__":
    main()

--- END FILE solution/calculator.py ---

--- END FIRST SOLUTION SNAPSHOT ---

--- BEGIN SA-03 CRITIQUE ---
## Défauts confirmés

1. **Livrable supplémentaire contraire au challenge — sévérité élevée.**  
   Le défi demande de créer « exclusivement » `calculator.py` et `README.md` dans `solution/`. La présence de `DECISIONS.md` viole littéralement cette contrainte. L’affirmation selon laquelle ce fichier serait exigé par le protocole V2 n’est étayée par aucune exigence du challenge fourni. Un vérificateur qui contrôle la liste des fichiers peut donc rejeter la solution.

2. **Exemple d’import incohérent avec le répertoire de lancement — sévérité moyenne.**  
   Le README se place « depuis la racine du dépôt », mais montre ensuite :

   ```python
   from calculator import calculate
   ```

   Depuis cette racine, `calculator.py` se trouve dans `solution/` et n’est normalement pas un module de premier niveau. L’exemple peut donc produire `ModuleNotFoundError` sans changement de répertoire ou adaptation du chemin d’import. La documentation ne fournit pas le contexte nécessaire pour rendre cet exemple reproductible.

3. **Garantie Ctrl-C trop large dans le README — sévérité faible.**  
   Le texte affirme qu’une interruption Ctrl-C termine proprement le programme. Or `KeyboardInterrupt` n’est capturée qu’autour de `input()`. Si elle survient pendant le parsing, le calcul ou l’affichage, elle peut produire un traceback. Le comportement habituel au repos sera propre, mais la garantie documentaire est plus forte que l’implémentation.

## Risques

1. **Type de retour de l’API.**  
   Avec des arguments `int`, `+`, `-` et `*` retournent un `int`, malgré l’annotation `-> float`. Le challenge peut être interprété comme exigeant seulement un résultat numérique, auquel cas cela convient. Un contrôle strict de `type(result) is float` échouerait néanmoins.

2. **Valeurs non finies acceptées implicitement.**  
   `float()` accepte notamment `nan`, `inf` et des exposants débordant vers l’infini. La CLI peut donc afficher `nan` ou `inf`, alors que le README parle de nombres entiers et décimaux ordinaires. Ce n’est pas une faille d’exécution de code, mais cela élargit silencieusement le domaine et peut donner des résultats arithmétiques surprenants, notamment `inf * 0 -> nan`.

3. **Consommation de ressources sur entrée démesurée.**  
   Aucune limite de longueur n’est appliquée avant `split()` et `float()`. Une entrée gigantesque peut consommer mémoire et CPU, et éventuellement déclencher une exception non capturée telle que `MemoryError`. La surface reste limitée à une CLI locale, donc ce risque est faible dans le contexte attendu.

4. **Compatibilité Python non déclarée.**  
   L’annotation `tuple[float, str, float]` nécessite Python 3.9 ou ultérieur. Le challenge ne fixe pas de version minimale au-delà de `python3`. Sur un environnement Python 3.8, le module échouerait dès l’import.

5. **Validation encore non démontrée.**  
   `DECISIONS.md` annonce des contrôles ciblés et reporte le vérificateur officiel, mais aucun résultat de test n’est fourni dans les éléments examinés. Il subsiste donc un risque de régression d’intégration, notamment sur la continuité après plusieurs erreurs, EOF, absence de traceback et import sans effet. Ce n’est pas encore une non-conformité puisque cette critique intervient avant la phase de vérification annoncée.

6. **API permissive hors annotations.**  
   `calculate` ne vérifie pas les types. Par exemple, certains appels avec des chaînes peuvent effectuer concaténation ou répétition au lieu d’échouer immédiatement. Les paramètres étant contractuellement typés `float`, ce comportement hors contrat n’est pas un défaut certain, mais il contredit partiellement la décision affirmant que l’API accepte des `int` et `float` sans préciser qu’elle accepte aussi, accidentellement, d’autres objets.

## Préférences, pas défauts

- Rejeter `2+3` est compatible avec la forme espacée explicitement donnée et avec l’arbitrage documenté.
- Garder `quit` et `exit` sensibles à la casse est acceptable.
- Afficher `5.0` plutôt que `5` est acceptable puisqu’aucun format exact n’est imposé.
- Un message commun préfixé par `Erreur :` est suffisamment compréhensible.
- L’acceptation d’espaces multiples et de tabulations est une extension raisonnable.
- Le cœur nominal est correctement séparé, protégé à l’import, sans `eval()`/`exec()`, et préserve bien `ValueError` et `ZeroDivisionError` pour les appels contractuels.
--- END SA-03 CRITIQUE ---
````

</details>

#### Texte retourné pour MSG-007, mot pour mot

````text
Je reprends la solution existante sans nouveau consultant. Je vais d’abord confronter chaque point SA-03 au contrat et au protocole explicite, consigner les preuves dans `DECISIONS.md`, puis n’appliquer que les corrections retenues avant de lancer la commande officielle exactement telle qu’indiquée.

L’arbitrage conduit à trois ajustements avant vérification : rendre l’exemple d’import réellement reproductible, étendre la capture de Ctrl-C à toute la boucle, et éviter la syntaxe d’annotation interne propre à Python 3.9+. Les demandes d’élargissement hors contrat (types arbitraires, valeurs non finies, limite de taille) sont écartées ; `DECISIONS.md` est conservé car la phase finale ordonne explicitement de le compléter.

Les corrections retenues et la table exhaustive SA-03 sont maintenant en place. Je lance à présent le premier passage du vérificateur officiel, depuis la racine du dépôt et avec la commande prescrite inchangée.

Le premier passage est intégralement réussi : 6 tests sur 6, code de sortie 0, verdict `OK`. Aucun défaut fonctionnel n’est confirmé et aucune correction post-vérification n’est nécessaire ; je consigne cette preuve, puis je revaliderai l’état final après cette seule mise à jour documentaire.

La seconde exécution confirme le même résultat final : 6/6 tests réussis, `OK`, code 0. Je termine par un contrôle de cohérence des trois fichiers de la solution afin de restituer précisément les corrections, arbitrages et limites, sans nouvelle modification fonctionnelle.

## Objectif et verdict

Solution finalisée. Le vérificateur officiel rend **`OK`**, avec **6 tests réussis sur 6** et un code de sortie **0**.

## Rôles et échanges

1. Orchestrateur expérimental : fourniture du challenge et des consultations autorisées.
2. SA-01 : analyse du contrat et de la sécurité.
3. SA-02 : analyse de conception et de testabilité.
4. SA-01 puis SA-02 : contradictions croisées.
5. MAIN : première implémentation, décideur et unique écrivain.
6. SA-03 : critique finale des défauts, risques et préférences.
7. MAIN finale : arbitrage SA-03, corrections et vérification. Aucun nouveau consultant ni sous-agent.

## Arbitrages et corrections

Les 15 points SA-03 sont qualifiés et justifiés dans [DECISIONS.md](<repo>/runs/sol-core-v2-001/solution/DECISIONS.md:34) :

- 10 retenus ;
- 5 écartés ;
- aucun point restant non vérifiable après le contrôle officiel.

Corrections retenues :

- exemple d’import rendu reproductible dans [README.md](<repo>/runs/sol-core-v2-001/solution/README.md:54) ;
- capture de Ctrl-C étendue à toute la boucle dans [calculator.py](<repo>/runs/sol-core-v2-001/solution/calculator.py:50) ;
- annotation interne compatible avec les anciennes versions de Python 3 via `typing.Tuple`.

`DECISIONS.md` a été conservé malgré SA-03 D1, car la phase finale demandait explicitement de le compléter. Le vérificateur officiel ne l’a pas rejeté.

## Vérifications

Commande exacte exécutée :

```bash
python3 scripts/verify.py --solution runs/sol-core-v2-001/solution
```

- Premier passage : **6/6, OK**, aucune correction fonctionnelle postérieure.
- Confirmations finales après mise à jour documentaire : **6/6, OK**.
- Verdict final : **réussi**, code 0.

## Limites assumées

Les choix hors contrat restent inchangés : syntaxe compacte rejetée, commandes sensibles à la casse, valeurs `nan`/`inf` non filtrées, aucune limite arbitraire de saisie et aucune validation des objets hors annotations.

Aucun TODO bloquant. Aucune opération Git effectuée.
````

## Lecture sociale synthétique

SA-01 et SA-02 commencent sans voir l'avis de l'autre. Leurs réponses
croisées rendent ensuite visibles accords, désaccords et doublons. MAIN
arbitre avant d'écrire. SA-03 critique l'instantané obtenu ; MAIN qualifie
alors chaque point avant le vérificateur. Le rapport de résultat chiffre
les recommandations retenues, écartées et non vérifiables.

Les prompts dynamiques répètent volontairement le challenge et les textes
antérieurs : cette duplication fait partie du coût de coordination mesuré.
