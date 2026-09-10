# Le run en 2 minutes — astra-medium-scientific-v2-001

**Français** · [English (UK)](astra-medium-scientific-v2-001.en.md) · [Español](astra-medium-scientific-v2-001.es.md) · [Português](astra-medium-scientific-v2-001.pt.md)

Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.

Calculatrice scientifique · codex-multi · completed

## Faits observés

| | |
| --- | --- |
| Modèle / effort | gpt-6-astra / medium |
| Premier passage officiel | 9/9 groups; 57/57 checks |
| Résultat candidat final | 9/9 groups; 57/57 checks |
| Verdict indépendant | 9/9 groups; 57/57 checks |
| Temps mural (s) | 648.008 |
| Tokens entrée + sortie | 570382 |
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
| sa01_initial | SA-01 | P1 | — | — | Non | 55.127 | 16718 | Non enregistré | Non enregistré |
| sa02_initial | SA-02 | P1 | — | — | Non | 54.314 | 16698 | Non enregistré | Non enregistré |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 28.439 | 17845 | Non enregistré | Non enregistré |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 28.315 | 17903 | Non enregistré | Non enregistré |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Oui | 311.551 | 198505 | Non enregistré | Non enregistré |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Non | 48.689 | 27934 | Non enregistré | Non enregistré |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Oui | 204.160 | 274779 | Non enregistré | Non enregistré |

Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation.

</details>

## Analyse interprétative

[CONTESTÉ → RETENU] Les revues croisées corrigent les avis sur sin(cos(x)) et sqrt(-1) lors de l’échantillonnage. [IMPACT] SA-03 signale les limites de longueur/profondeur → RELAY transmet MSG-006 → MAIN accepte dans la table finale → retire le plafond et remplace la récursion par une pile explicite → test candidat des expressions longues réussi. Deux autres groupes corrigent l’affichage terminal et les canaux CLI. [REJETÉ] Plafond arbitraire d’échantillons et écriture atomique non exigés. Dix points retenus, deux rejetés, un non vérifiable dans le dossier reçu. Le script des 131 assertions initiales figure dans la trace MAIN, pas dans le dossier transmis à SA-03 : sa réserve n’est pas une absence globale de preuve. Voir DECISIONS, « Arbitrage final SA-03 » et « Preuves finales ». Contribution observable, mais aucun gain de score isolé : le premier vérificateur intervient après ces changements. Nouveauté absolue et [BRUIT] non établis.

## Preuves et suite

[PV / verbatim](../../runs/astra-medium-scientific-v2-001/PV.md) · [trace.json](../../runs/astra-medium-scientific-v2-001/trace.json) · [run.json](../../runs/astra-medium-scientific-v2-001/run.json) · [Décisions](../../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md)

[Guide de lecture](../../docs/reading-guide.md) · [Tests](../../docs/acceptance-tests.md) · [Conclusions](../CONCLUSIONS.md) · [Index](index.md)
