# Le run en 2 minutes — astra-core-v2-001

**Français** · [English (UK)](astra-core-v2-001.en.md) · [Español](astra-core-v2-001.es.md) · [Português](astra-core-v2-001.pt.md)

Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.

Calculatrice simple · codex-multi · completed

## Faits observés

| | |
| --- | --- |
| Modèle / effort | gpt-6-astra / high |
| Premier passage officiel | 6/6 unittest groups; 14/14 elementary checks |
| Résultat candidat final | 6/6 unittest groups; 14/14 elementary checks |
| Verdict indépendant | 6/6 unittest groups; 14/14 elementary checks |
| Temps mural (s) | 700.994 |
| Tokens entrée + sortie | 572168 |
| Sessions enregistrées (pas appels API) | 7 |
| Corrections fonctionnelles après premier passage | 0 |

Le cache est inclus dans l’entrée ; le raisonnement est inclus dans la sortie. Ne pas les additionner de nouveau. Une session CLI peut contenir plusieurs appels modèle. Le premier passage officiel vient après la critique, pas avant.

## Équipe et chronologie

MAIN : arbitre et seul écrivain ; SA-01 : exigences/sécurité ; SA-02 : architecture/testabilité ; SA-03 : relecture critique. RELAY est le superviseur mécanique externe, pas un candidat.

P1 : analyses indépendantes, puis barrière. P2 : revues croisées, puis barrière. Ensuite MAIN → SA-03 → MAIN et vérificateur. Le parallélisme historique est spécifié, pas un chevauchement mesuré.

<details>
<summary>Sessions enregistrées (pas appels API)</summary>

| Session | Rôle | Groupe parallèle spécifié | Dépend de | receives_from | Écrivain | Durée CLI (s) | Tokens entrée + sortie | Début / fin mesurés (s) | Durée d’invocation mesurée (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | Non enregistré | P1 | — | — | Non | 48.093 | 15602 | Non enregistré | Non enregistré |
| sa02_initial | Non enregistré | P1 | — | — | Non | 46.555 | 15491 | Non enregistré | Non enregistré |
| sa01_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 27.954 | 16949 | Non enregistré | Non enregistré |
| sa02_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 33.817 | 16980 | Non enregistré | Non enregistré |
| main_first | Non enregistré | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Oui | 393.690 | 213048 | Non enregistré | Non enregistré |
| sa03_critic | Non enregistré | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Non | 44.659 | 27115 | Non enregistré | Non enregistré |
| main_final | Non enregistré | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Oui | 180.712 | 266983 | Non enregistré | Non enregistré |

Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation.

</details>

## Analyse interprétative

[CONFIRMÉ] Consensus et clarification du contrat : 17 décisions initiales. Après MSG-006, MAIN arbitre 14 points (7 retenus, 3 rejetés, 4 non vérifiables) et modifie seulement la documentation. Aucun défaut fonctionnel confirmé ni interaction ayant changé le score. La répétition des consultations dans DECISIONS agrandit les prompts suivants : coût observable de transmission, pas preuve que chaque répétition est inutile. Voir le rapport [Core élevé](../astra-v2-core.md), puis DECISIONS et MSG-007. Aucun [NOUVEAU] ou [BRUIT] forcé.

## Preuves et suite

[PV / verbatim](../../runs/astra-core-v2-001/PV.md) · [trace.json](../../runs/astra-core-v2-001/trace.json) · [run.json](../../runs/astra-core-v2-001/run.json) · [Décisions](../../runs/astra-core-v2-001/solution/DECISIONS.md)

[Guide de lecture](../../docs/reading-guide.md) · [Tests](../../docs/acceptance-tests.md) · [Conclusions](../CONCLUSIONS.md) · [Index](index.md)
