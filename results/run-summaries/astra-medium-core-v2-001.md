# Le run en 2 minutes — astra-medium-core-v2-001

**Français** · [English (UK)](astra-medium-core-v2-001.en.md) · [Español](astra-medium-core-v2-001.es.md) · [Português](astra-medium-core-v2-001.pt.md)

Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.

Calculatrice simple · codex-multi · completed

## Faits observés

| | |
| --- | --- |
| Modèle / effort | gpt-6-astra / medium |
| Premier passage officiel | 6/6 groups; 14/14 checks |
| Résultat candidat final | 6/6 groups; 14/14 checks |
| Verdict indépendant | 6/6 groups; 14/14 checks |
| Temps mural (s) | 375.169 |
| Tokens entrée + sortie | 408616 |
| Sessions enregistrées (pas appels API) | 7 |
| Corrections fonctionnelles après premier passage | Non enregistré |

Le cache est inclus dans l’entrée ; le raisonnement est inclus dans la sortie. Ne pas les additionner de nouveau. Une session CLI peut contenir plusieurs appels modèle. Le premier passage officiel vient après la critique, pas avant.

## Équipe et chronologie

MAIN : arbitre et seul écrivain ; SA-01 : exigences/sécurité ; SA-02 : architecture/testabilité ; SA-03 : relecture critique. RELAY est le superviseur mécanique externe, pas un candidat.

P1 : analyses indépendantes, puis barrière. P2 : revues croisées, puis barrière. Ensuite MAIN → SA-03 → MAIN et vérificateur. Le parallélisme historique est spécifié, pas un chevauchement mesuré.

<details>
<summary>Sessions enregistrées (pas appels API)</summary>

| Session | Rôle | Groupe parallèle spécifié | Dépend de | receives_from | Écrivain | Durée CLI (s) | Tokens entrée + sortie | Début / fin mesurés (s) | Durée d’invocation mesurée (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | SA-01 | P1 | — | — | Non | 51.054 | 15919 | Non enregistré | Non enregistré |
| sa02_initial | SA-02 | P1 | — | — | Non | 47.764 | 15812 | Non enregistré | Non enregistré |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 28.390 | 17485 | Non enregistré | Non enregistré |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 28.140 | 17483 | Non enregistré | Non enregistré |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Oui | 146.611 | 144301 | Non enregistré | Non enregistré |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Non | 37.223 | 22386 | Non enregistré | Non enregistré |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Oui | 111.857 | 175230 | Non enregistré | Non enregistré |

Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation.

</details>

## Analyse interprétative

[CONTESTÉ → RETENU] SA-01 retire sa préférence pour les nombres finis lors de la revue croisée (MSG-003/004) ; MAIN arbitre 21 points avant le code. [CONFIRMÉ] SA-03 relève des limites numériques ; MAIN les vérifie et précise le README, sans modifier calculator.py. Onze arbitrages finaux, aucun correctif fonctionnel. Interaction déterminante pour le score : aucune démontrée. Les avis retenus ne prouvent pas que MAIN aurait échoué seul ; pas de classement automatique en [BRUIT]. Voir DECISIONS, table finale et points 9–12, et MSG-006/007 du PV.

## Preuves et suite

[PV / verbatim](../../runs/astra-medium-core-v2-001/PV.md) · [trace.json](../../runs/astra-medium-core-v2-001/trace.json) · [run.json](../../runs/astra-medium-core-v2-001/run.json) · [Décisions](../../runs/astra-medium-core-v2-001/solution/DECISIONS.md)

[Guide de lecture](../../docs/reading-guide.md) · [Tests](../../docs/acceptance-tests.md) · [Conclusions](../CONCLUSIONS.md) · [Index](index.md)
