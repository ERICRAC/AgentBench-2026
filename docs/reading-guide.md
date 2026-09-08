# Comprendre AgentBench

**Français** · [English (UK)](reading-guide.en.md) · [Español](reading-guide.es.md) · [Português](reading-guide.pt.md)

Laboratoire R&D sur la collaboration des agents : les calculatrices sont les exercices communs. V1 = un candidat seul ; V2 = un écrivain et trois consultants ; V3 = futurs consultants locaux. On mesure qualité, temps et tokens : V2 n'est pas promise meilleure.

| ID | Role |
| --- | --- |
| RELAY | Orchestrateur expérimental |
| MAIN | Développeur principal, seul écrivain et décideur |
| SA-01 | Sous-agent 1 — exigences et sécurité |
| SA-02 | Sous-agent 2 — architecture et testabilité |
| SA-03 | Sous-agent 3 — relecteur qualité critique, défauts et cas limites |

Dans les PV, ouvrir « Texte envoyé, mot pour mot » et lire « Texte retourné ». MSG-003/004 : réponses croisées ; MSG-006 : critique SA-03 ; MSG-007 : arbitrage final. Sept sessions représentent quatre rôles candidats. Le vérificateur est un programme indépendant. `trace.json` décrit commandes et compteurs ; `DECISIONS.md` les arbitrages. Textes visibles filtrés, sans raisonnement interne.

[Sol Core PV](../runs/sol-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Sol Scientific PV](../runs/sol-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium](../results/astra-medium-v2.md)

Vx future, non activée : confier une évolution figée à un repreneur neuf avec seulement code et documentation ; mesurer succès, régressions, temps, tokens et clarifications. Les tests actuels ne mesurent pas la maintenabilité (Scientific vérifie cinq mots-clés documentaires). Évaluer les explications utiles, pas le nombre de commentaires. Reprendre une solution dans une nouvelle branche ou un nouveau dossier pour conserver la preuve.

[README](../README.md) → [Tests](acceptance-tests.md) → [Results](../results/README.md)
