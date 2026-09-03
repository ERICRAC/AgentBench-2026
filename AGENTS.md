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

## Format des restitutions

Les réponses de fin de tâche suivent
[`governance/RESPONSE_FORMAT.md`](governance/RESPONSE_FORMAT.md). Elles commencent
par le résultat, décrivent les changements et les vérifications, exposent les
limites, puis indiquent la suite utile. Les titres remplacent une numérotation
rigide et les affirmations importantes s'appuient sur des preuves observables.
