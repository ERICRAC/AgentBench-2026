# Le run en 2 minutes — sol-scientific-v2-001

**Français** · [English (UK)](sol-scientific-v2-001.en.md) · [Español](sol-scientific-v2-001.es.md) · [Português](sol-scientific-v2-001.pt.md)

Cette couche précède le PV détaillé dans le parcours de lecture ; le PV original reste inchangé. Les cellules absentes ne valent pas zéro.

Calculatrice scientifique · codex-multi · completed

## Faits observés

| | |
| --- | --- |
| Modèle / effort | gpt-5.6-sol / high |
| Premier passage officiel | 3/9 unittest groups; 6 import errors from one dataclass loader incompatibility |
| Résultat candidat final | 9/9 unittest groups; 57/57 elementary checks |
| Verdict indépendant | 9/9 unittest groups; 57/57 elementary checks |
| Temps mural (s) | 1587.605 |
| Tokens entrée + sortie | 916538 |
| Sessions enregistrées (pas appels API) | 7 |
| Corrections fonctionnelles après premier passage | 1 |

Le cache est inclus dans l’entrée ; le raisonnement est inclus dans la sortie. Ne pas les additionner de nouveau. Une session CLI peut contenir plusieurs appels modèle. Le premier passage officiel vient après la critique, pas avant.

## Équipe et chronologie

MAIN : arbitre et seul écrivain ; SA-01 : exigences/sécurité ; SA-02 : architecture/testabilité ; SA-03 : relecture critique. RELAY est le superviseur mécanique externe, pas un candidat.

P1 : analyses indépendantes, puis barrière. P2 : revues croisées, puis barrière. Ensuite MAIN → SA-03 → MAIN et vérificateur. Le parallélisme historique est spécifié, pas un chevauchement mesuré.

<details>
<summary>Sessions enregistrées (pas appels API)</summary>

| Session | Rôle | Groupe parallèle spécifié | Dépend de | receives_from | Écrivain | Durée CLI (s) | Tokens entrée + sortie | Début / fin mesurés (s) | Durée d’invocation mesurée (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | Non enregistré | P1 | — | — | Non | 78.281 | 16417 | Non enregistré | Non enregistré |
| sa02_initial | Non enregistré | P1 | — | — | Non | 73.029 | 16264 | Non enregistré | Non enregistré |
| sa01_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 41.247 | 17291 | Non enregistré | Non enregistré |
| sa02_cross | Non enregistré | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Non | 38.271 | 17214 | Non enregistré | Non enregistré |
| main_first | Non enregistré | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Oui | 810.863 | 416050 | Non enregistré | Non enregistré |
| sa03_critic | Non enregistré | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Non | 226.117 | 32786 | Non enregistré | Non enregistré |
| main_final | Non enregistré | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Oui | 431.056 | 400516 | Non enregistré | Non enregistré |

Les mesures d’invocation ont une origine distincte du temps mural historique ; voir le guide d’instrumentation.

</details>

## Analyse interprétative

[CONTESTÉ] Revues croisées : plafonds non contractuels, clés de variables supplémentaires et sécurité des chemins. MAIN retient 15 recommandations initiales sur 16. [IMPACT] SA-03 → transmission MSG-006 → arbitrage MAIN (10 retenus, 5 écartés) → six corrections avant vérification : Ctrl-C, affichage numérique, AST profonds, exemple README, terminal, 0^-1. Voir [rapport Sol](../sol-v2.md) et DECISIONS. Le premier score reste 3/9 : le chargeur Python 3.13 échoue avec dataclass. MAIN remplace le conteneur et obtient 9/9. Cette dernière correction vient du vérificateur, pas d’un consultant. V1 Sol avait le même profil : les contributions observables n’améliorent pas la convergence officielle. Nouveauté absolue et volume de [BRUIT] non établis.

## Preuves et suite

[PV / verbatim](../../runs/sol-scientific-v2-001/PV.md) · [trace.json](../../runs/sol-scientific-v2-001/trace.json) · [run.json](../../runs/sol-scientific-v2-001/run.json) · [Décisions](../../runs/sol-scientific-v2-001/solution/DECISIONS.md)

[Guide de lecture](../../docs/reading-guide.md) · [Tests](../../docs/acceptance-tests.md) · [Conclusions](../CONCLUSIONS.md) · [Index](index.md)
