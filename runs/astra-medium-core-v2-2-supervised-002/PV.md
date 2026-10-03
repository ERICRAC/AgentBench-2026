# PV — V2.2 simple supervisée 002

## Identification et équipe

Run `astra-medium-core-v2-2-supervised-002`, campagne `astra-medium-supervised-001`.
Commanditaire : Éric Racineux. RELAY : orchestrateur expérimental hors candidat,
responsable du transport, des captures et de la publication. Vérificateur :
suite indépendante figée, [checklist des 6 groupes / 14 contrôles](../../docs/acceptance-tests.md).

| Rôle et métier | Mission et entrées | Écriture | Modèle / effort |
| --- | --- | --- | --- |
| MAIN — développeur et arbitre, deux sessions distinctes | Défi puis code, traces visibles et revue | Livrables dans solution uniquement | gpt-6-astra / medium |
| REV-01 — relecteur critique, une session | Défi, instantané initial et compte rendu MAIN | Aucune | gpt-6-astra / medium |

REV-01 est l'identifiant du relecteur, **pas un défaut numéroté**.
Trois threads distincts ; leurs identifiants, configurations effectives demandées,
empreintes des prompts et métriques sont dans [run.json](run.json).
Contexte configuré à 200 000 tokens, compaction à 180 000 (portée total) ;
ce n'est pas un plafond cumulatif de consommation. Isolation supervisée, pas
confinement complet en lecture. Aucune déviation enregistrée par le pilote.

## Messages visibles et mandats

Les trois textes envoyés sont intégraux dans [prompts.json](prompts.json),
champs `main_initial.text`, `review.text`, `main_final.text`.
Ils incluent le défi et, selon la phase, les instantanés et transmissions.
La [trace publique](trace.json) contient événements, commandes et sorties.
Le chemin temporaire est remplacé par `<private-run-root>` ; les événements
de raisonnement interne sont exclus. Empreintes des captures originales
conservées. Les messages ci-dessous ne subissent que cette normalisation.

### MSG-001 — RELAY → MAIN, mandat main_initial

Texte envoyé : [prompts.json](prompts.json), champ `main_initial.text`.
Réponse de phase : 104.812 s ; entrée 49294,
cache 34816, sortie 2255,
dont raisonnement 48 tokens.
Ces métriques portent sur toute la session, pas chaque message séparément.

### MSG-002 — MAIN → RELAY, main_initial

> Je vais lire le contrat actif, puis créer les deux livrables et effectuer des contrôles locaux sans lancer le vérificateur officiel.

### MSG-003 — MAIN → RELAY, main_initial

> Livrables créés :
>
> - [calculator.py](<private-run-root>/workspace/solution/calculator.py) : fonction `calculate`, quatre opérations explicites, exceptions attendues et boucle interactive avec messages d’erreur en français. Aucun `eval()` ni `exec()`.
> - [README.md](<private-run-root>/workspace/solution/README.md) : lancement, exemples, API Python et limites documentées.
>
> Contrôles locaux exécutés avec `python3 -B`, sans cache : quatre opérations, entiers et décimaux négatifs, opération inconnue, division par `0` et `-0.0`, import silencieux, expressions invalides, poursuite après erreur, commandes `quit` et `exit`, fin d’entrée.
>
> Résultat : tous les contrôles ont réussi ; les processus CLI ont terminé avec le code `0`, sans sortie d’erreur ni traceback. Commande, entrées et sorties sont visibles dans la trace d’exécution.
>
> Aucun défaut identifié lors de ces contrôles. Les calculs conservent les limites de précision des flottants Python ; `inf` et `nan` sont acceptés et documentés. Ctrl+C est pris en charge mais n’a pas été testé.
>
> Le vérificateur officiel n’a pas été lancé, conformément au mandat. La conformité à ses contrôles reste à confirmer après revue.

### MSG-004 — RELAY → REV-01, mandat review

Texte envoyé : [prompts.json](prompts.json), champ `review.text`.
Réponse de phase : 29.177 s ; entrée 13893,
cache 0, sortie 596,
dont raisonnement 117 tokens.
Ces métriques portent sur toute la session, pas chaque message séparément.

### MSG-005 — REV-01 → RELAY, review

> Aucun défaut confirmé trouvé dans l’instantané fourni. La solution paraît conforme au défi ; aucune correction bloquante ou majeure n’est justifiée par les éléments examinés.
>
> Le contrat a été examiné avant la solution. Cette revue repose uniquement sur le défi, les deux fichiers fournis et les commandes/sorties visibles de MAIN. Aucun contrôle supplémentaire n’a été exécuté, aucun fichier modifié et le vérificateur officiel n’a pas été lancé.
>
> - **Contrat Python :** `calculate` possède la signature demandée, implémente les quatre opérations et renvoie un flottant. Toute opération inconnue déclenche `ValueError`. La division par zéro, y compris `-0.0`, déclenche `ZeroDivisionError`.
> - **Contrat CLI :** la boucle interprète les expressions à trois éléments séparés par des espaces. Les erreurs de format, de conversion numérique, d’opérateur et de division par zéro produisent des messages compréhensibles, puis permettent de poursuivre. `quit` et `exit` terminent le programme.
> - **Sécurité et dépendances :** aucun usage de `eval()` ou `exec()`, aucune dépendance externe et aucune exécution des expressions comme code. L’importation est protégée contre le lancement de la CLI.
> - **Documentation :** le README explique le lancement, l’utilisation, les exceptions et les limites numériques. Ses exemples correspondent au comportement du code.
>
> Les sorties fournies montrent la réussite des contrôles sur les quatre opérations, les nombres négatifs et décimaux, les exceptions attendues, plusieurs expressions invalides, la reprise après erreur, les commandes de sortie et EOF. Elles montrent également une sortie d’erreur vide et un code de retour nul pour les sessions CLI testées.
>
> Les valeurs `inf` et `nan` sont acceptées par `float()` et documentées ; le défi ne les interdit pas. Leur acceptation ne constitue donc pas un défaut. L’exigence d’espaces correspond au format d’expression prescrit.
>
> **Limites de vérification :** Ctrl+C est traité dans le code, mais son comportement n’a pas été testé dans les traces fournies. La réussite du vérificateur officiel demeure inconnue. Ces limites ne démontrent aucune non-conformité et ne motivent pas de constat REV.

### MSG-006 — RELAY → MAIN, mandat main_final

Texte envoyé : [prompts.json](prompts.json), champ `main_final.text`.
Réponse de phase : 25.969 s ; entrée 47324,
cache 30464, sortie 412,
dont raisonnement 0 tokens.
Ces métriques portent sur toute la session, pas chaque message séparément.

### MSG-007 — MAIN → RELAY, main_final

> Je vais lire le contrat actif et les livrables, puis lancer le vérificateur officiel. La revue fournie ne contient aucun constat identifié à corriger ; je confronterai sa conclusion aux résultats obtenus.

### MSG-008 — MAIN → RELAY, main_final

> Le vérificateur officiel réussit dès le premier passage : **6 tests réussis, code de sortie 0**. Aucun défaut confirmé ne nécessite de correction.
>
> | ID reçu | Arbitrage | Motif et preuve |
> |---|---|---|
> | REV-01 — conclusion générale, aucun constat numéroté | Retenu | La lecture du contrat et des livrables concorde avec la revue. Les tests officiels confirment les opérations, les variantes numériques, les exceptions, la reprise de la CLI après erreur et l’absence d’exécution dynamique interdite. |
>
> Commandes exécutées dans cette session :
>
> - `cat ../CHALLENGE.md README.md calculator.py` — réussite ; contrat actif lu avant toute modification.
> - `python3 -B ../scripts/verify.py --solution .` — un seul passage : `Ran 6 tests in 0.012s`, puis `OK`. Sortie intégrale visible dans la trace.
>
> **Changements :** aucun. `calculator.py` et `README.md` sont conservés. Aucune modification spontanée, donc aucun ID MAIN ajouté.
>
> **Limites restantes :** Ctrl+C n’a pas fait l’objet d’un contrôle supplémentaire dans cette session. Les limites de précision des flottants et l’acceptation de `inf` et `nan` restent documentées ; elles ne contreviennent pas au contrat.

## Arbitrage et analyse sociale

| Décision | Source | Avis | Arbitrage MAIN | Effet observé |
| --- | --- | --- | --- | --- |
| DEC-001 | MSG-005, REV-01 relecteur | Aucun défaut confirmé ; conserver la solution | Retenu dans MSG-008, concordance avec contrat et vérificateur | Aucun changement de fichier |
| DEC-002 | MSG-005 | Ctrl+C non testé ; inf/nan acceptés sans violation du contrat | Limites conservées dans MSG-008, pas de correction requise | Aucun gain de couverture revendiqué |

Huit messages visibles numérotés ici : trois mandats et cinq messages retournés.
RELAY transmet la revue à MAIN sans ajouter un avis technique candidat.
Un accord explicite sur la conclusion générale, aucun désaccord observé,
aucun constat correctif numéroté et aucune correction après revue.
Le relecteur n'exécute pas de test ; il examine les éléments transmis.
Sa revue recoupe les contrôles déjà rapportés. Le nombre de doublons précis
et une mesure objective du « bruit » ne sont pas enregistrés.
L'absence de contradiction ne prouve pas un consensus social général.

La revue retourne 318 mots ; les finales MAIN comptent 157 puis 175 mots,
les messages intermédiaires 21 puis 32. Le coût direct REV-01 est
14 489 tokens et 29,177 s. Le coût complet de coordination n'est pas isolé :
les prompts suivants retransmettent des éléments, tandis que MAIN final
inclut lecture, arbitrage et vérification. Ne pas assimiler toute cette phase
à une pure surcharge sociale.

## Vérifications et mesures

| Phase | Durée (s) | Entrée | Sortie | Total |
| --- | ---: | ---: | ---: | ---: |
| MAIN initial | 104,812 | 49 294 | 2 255 | 51 549 |
| REV-01 relecteur | 29,177 | 13 893 | 596 | 14 489 |
| MAIN final | 25,969 | 47 324 | 412 | 47 736 |
| Total sessions | 159,958 | 110 511 | 3 263 | 113 774 |

Temps mural : **159,977 s**. Cache : 65 280 tokens déjà inclus dans l'entrée ;
raisonnement : 165 déjà inclus dans la sortie. Ne pas les additionner à nouveau.
Les coûts de maintenance et publication sont hors périmètre.
Nombre de requêtes modèle et soldes de quota non enregistrés.

Premier passage officiel final : **6/6 groupes, 14 contrôles**, code 0.
Vérification indépendante après run : même verdict. Contrôle rétrospectif de
l'initial : même verdict, jamais transmis au candidat. [Sorties complètes](verifications.json).
[Initial](initial/calculator.py) et [final](solution/calculator.py) identiques
octet pour octet, README compris ; [empreintes et contenus](snapshots.json).
Empreintes des sources gelées et protection du workspace contrôlées inchangées.
Le premier `rg --files` retourne 1 parce que la solution est vide ; la lecture
du défi a réussi. Ce n'est ni une erreur de quota ni un défaut de calculatrice.

## Conclusion expérimentale

La relecture confirme la conformité mais ne corrige aucun défaut et n'améliore
pas le score mesuré. Aucun gain qualitatif démontré sur cette tâche.
Le binôme se termine sans interruption de quota : cela établit la faisabilité
de cet essai, pas une garantie de tenir dans toute fenêtre d'abonnement.
L'essai interrompu 001 reste conservé et son coût ne disparaît pas.

[Rapport comparatif synthétique](../../results/v2-2-supervised-core-002.md) :
comparaison historique exploratoire, pas effet causal isolé de l'organisation.
Aucune scientifique ni relance automatique autorisée.
