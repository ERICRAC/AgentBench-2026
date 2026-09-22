# V2.2 supervisée — essai simple interrompu par quota

**Français** · [English (UK)](v2-2-supervised-core.en.md) · [Español](v2-2-supervised-core.es.md) · [Português](v2-2-supervised-core.pt.md)

**L'essai a réellement démarré en Astra moyen, puis la CLI a signalé une limite d'usage.** MAIN a créé les deux livrables mais n'a pas terminé sa session. REV-01 et MAIN final n'ont pas été lancés. Aucun réessai.

| Mesure | Observation |
| --- | --- |
| Tentative | astra-medium-core-v2-2-supervised-001 |
| Sessions | 1 commencée, 0 terminée sur 3 prévues |
| Temps du processus candidat | 48,639 s |
| Temps mural de l'essai interrompu | 48,641 s |
| Tokens / nombre de requêtes modèle | Non enregistrés, pas zéro |
| Verdict V2.2 complet | Aucun |
| Diagnostic après interruption | 6/6 groupes, 14 contrôles réussis |

Les fichiers sont archivés **sans correction de l'orchestrateur**. Après clôture, le vérificateur indépendant confirme les deux livrables, l'absence d'exécution dynamique, les quatre opérations, les erreurs d'opérateur et de division par zéro, ainsi que la récupération CLI. [Checklist des contrôles](../docs/acceptance-tests.md). Ce diagnostic n'est pas un passage officiel de phase finale et n'a pas été transmis au candidat.

**Enseignement :** le transport réel a permis lecture et écriture. Cet essai s'arrête pour quota, pas pour le précédent blocage MCP. Il ne permet aucune conclusion sur l'efficacité du binôme : aucune revue, aucun arbitrage et aucun total de tokens disponible. Ne pas comparer ces 48,641 s à un run V1/V2 terminé. Les garanties restent celles du pilote supervisé, non d'un confinement complet.

[PV et analyse sociale](../runs/astra-medium-core-v2-2-supervised-001/PV.md) · [Mandat intégral](../runs/astra-medium-core-v2-2-supervised-001/PROMPT.md) · [Événements visibles](../runs/astra-medium-core-v2-2-supervised-001/trace.jsonl) · [Métadonnées](../runs/astra-medium-core-v2-2-supervised-001/run.json) · [Code intact](../runs/astra-medium-core-v2-2-supervised-001/solution/calculator.py) · [Protocole figé](../governance/V2_2_SUPERVISED.md).

Les captures brutes restent privées. La trace publique retire le chemin temporaire et les liens/heure du message de quota ; aucune donnée manquante n'est inventée. Protection des fichiers du workspace et empreintes gelées vérifiées.

**Suite :** si l'utilisateur confirme un quota disponible et une relance, créer une nouvelle tentative simple, nouvel ID et solution vide. Ne pas reprendre ou réutiliser ce code ; scientifique toujours non autorisée.

[README](../README.md) · [Conclusions](CONCLUSIONS.md)
