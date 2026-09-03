# Gouvernance des agents — AgentBench 2026

## Principes globaux

- Lire le `CHALLENGE.md` de la tentative active avant toute modification.
- Ne jamais modifier `challenges/` ni les tests pendant une tentative.
- Utiliser un répertoire neuf et ne jamais consulter la solution d'une autre
  tentative.
- Ne pas utiliser `eval()` ou `exec()` ni ajouter de dépendance d'exécution au
  défi Calculator.
- Ne jamais écrire de secret, jeton, phrase secrète ou donnée
  d'authentification dans le dépôt ou les journaux publics.
- Le verdict technique appartient au vérificateur indépendant.

## Gouvernance par mode

- **V1 — Codex seul :** aucun sous-agent ni aucune délégation.
- **V2 — Codex multi-agent :** les sous-agents sont autorisés uniquement quand
  le lancement de la V2 le demande explicitement. Leurs missions sont bornées
  et consultatives ; un seul écrivain principal modifie la solution.
- **V3 — Codex avec Ollama :** Codex reste orchestrateur, décideur et écrivain.
  Les modèles locaux analysent ou critiquent dans un contexte limité.

Pendant un run, seules les écritures dans le dossier `solution/` de la
tentative active sont autorisées. La maintenance du protocole, des résultats,
de la gouvernance et des journaux se fait hors run et dans un commit séparé.

## Validation et traçabilité

- Implémenter une solution complète, sans placeholder.
- Exécuter la commande indiquée dans `CHALLENGE.md` avant de conclure.
- Corriger les défauts confirmés jusqu'à réussite ou signaler précisément les
  contrôles restant en échec.
- Enregistrer les rôles, décisions, tests, corrections, tokens et durées quand
  ces données sont effectivement disponibles.
- Ne jamais inventer une donnée manquante ; la marquer comme non enregistrée.
- Publier une synthèse des échanges selon [`governance/LOGGING.md`](governance/LOGGING.md).

## Gouvernance évolutive

- À chaque échange, examiner si une erreur, une ambiguïté, une intervention
  humaine ou une décision réutilisable révèle une règle à améliorer.
- Modifier la gouvernance seulement si la nouvelle règle est générale,
  vérifiable et utile aux prochains runs ; éviter l'accumulation de consignes
  anecdotiques.
- Journaliser synthétiquement toute évolution de gouvernance et sa raison.
- Ne jamais appliquer rétroactivement une nouvelle règle pour embellir ou
  réinterpréter les conditions d'une tentative terminée.
- Protéger les habitudes de travail de l'auteur en retirant les heures des
  Markdown publics, sans jamais les remplacer par des heures fictives.

## Livraison Git

- Après chaque échange qui modifie des fichiers suivis, créer un commit avec un
  titre synthétique et un corps décrivant le résultat, les principaux fichiers
  et les vérifications exécutées.
- Pousser immédiatement ce commit sur la branche distante, sauf instruction
  contraire explicite de l'utilisateur.
- Ne jamais inclure dans un commit un helper local, une clé ou un secret, même
  si l'utilisateur demande de publier les autres changements du même échange.
- Si le push exige une interaction inaccessible à l'agent, conserver le commit
  local, signaler précisément le blocage et donner la commande minimale à
  exécuter.

## Format des restitutions

Les réponses de fin de tâche suivent
[`governance/RESPONSE_FORMAT.md`](governance/RESPONSE_FORMAT.md). Elles sont
structurées autour de l'objectif, de la réponse directe, du travail réalisé,
des vérifications, des points ouverts, du TODO et de la livraison Git. Les
titres remplacent une numérotation rigide et les affirmations importantes
s'appuient sur des preuves observables.
