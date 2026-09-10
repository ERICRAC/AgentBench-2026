# Le run en 2 minutes — sol-core-v2-001

**Français** · [English (UK)](sol-core-v2-001.en.md) · [Español](sol-core-v2-001.es.md) · [Português](sol-core-v2-001.pt.md)

Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.

Calculatrice simple · codex-multi · completed

## Faits observés

| | |
| --- | --- |
| Modèle / effort | gpt-5.6-sol / high |
| Premier passage officiel | 6/6 unittest groups; 14/14 elementary checks |
| Résultat candidat final | 6/6 unittest groups; 14/14 elementary checks |
| Verdict indépendant | 6/6 unittest groups; 14/14 elementary checks |
| Temps mural (s) | 796.534 |
| Tokens entrée + sortie | 559088 |
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
| sa01_initial | Non enregistré | P1 | — | — | Non | 62.931 | 15125 | Non enregistré | Non enregistré |
| sa02_initial | Non enregistré | P1 | — | — | Non | 72.214 | 15401 | Non enregistré | Non enregistré |
| sa01_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 48.026 | 17385 | Non enregistré | Non enregistré |
| sa02_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 38.788 | 17142 | Non enregistré | Non enregistré |
| main_first | Non enregistré | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Oui | 236.374 | 159299 | Non enregistré | Non enregistré |
| sa03_critic | Non enregistré | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Non | 118.418 | 23556 | Non enregistré | Non enregistré |
| main_final | Non enregistré | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Oui | 321.478 | 311180 | Non enregistré | Non enregistré |

Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation.

</details>

## Analyse interprétative

[CONTESTÉ → RETENU] Convergence sur trois éléments séparés par des blancs et refus de 2+3. MAIN arbitre 23 recommandations (19 retenues, 4 écartées). [IMPACT] Après SA-03 : exemple d’import corrigé, Ctrl-C étendu à toute la boucle, annotation interne compatible avec d’anciennes versions Python. [REJETÉ] MAIN conserve DECISIONS malgré l’objection de SA-03 sur les livrables, suivant le protocole. Dix points finaux retenus et cinq écartés. Voir [rapport Core Sol](../sol-v2-core.md), DECISIONS et MSG-006/007. Pas de gain sur le score officiel ; aucune preuve que MAIN aurait échoué seul. Avis souvent redondants, sans quantification fiable du [BRUIT].

## Preuves et suite

[PV / verbatim](../../runs/sol-core-v2-001/PV.md) · [trace.json](../../runs/sol-core-v2-001/trace.json) · [run.json](../../runs/sol-core-v2-001/run.json) · [Décisions](../../runs/sol-core-v2-001/solution/DECISIONS.md)

[Guide de lecture](../../docs/reading-guide.md) · [Tests](../../docs/acceptance-tests.md) · [Conclusions](../CONCLUSIONS.md) · [Index](index.md)
