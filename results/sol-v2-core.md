# V2 Sol — rapport Calculatrice Core

**Français** · [English (UK)](sol-v2-core.en.md) · [Español](sol-v2-core.es.md) · [Português](sol-v2-core.pt.md)

## Verdict lisible

Le run `sol-core-v2-001` réussit **6/6 groupes `unittest` et 14/14 contrôles
élémentaires**, dès le premier passage officiel puis lors de la relance
indépendante. Le [catalogue](../docs/acceptance-tests.md) nomme chaque contrôle.

La qualité officielle égale la référence V1 Sol, mais V2 coûte 4,19 fois plus
de temps mural et 3,54 fois plus de tokens. Selon la règle de Pareto
préenregistrée, **V1 domine V2 sur Core** : même conformité mesurée, coûts
inférieurs. Aucun gain multi-agent n'est démontré sur ce petit défi.

## Comparaison V1/V2

| Mesure | V1 Sol seul | V2 Sol multi-agent | Écart V2 |
| --- | ---: | ---: | ---: |
| Premier passage | 6/6 groupes · 14/14 contrôles | 6/6 groupes · 14/14 contrôles | égalité |
| Verdict indépendant | 6/6 · 14/14 | 6/6 · 14/14 | égalité |
| Temps mural | 189,964 s | 796,534 s | ×4,19 · +319,3 % |
| Entrée + sortie | 158 101 | 559 088 | ×3,54 · +253,6 % |
| Corrections après premier vérificateur | 0 | 0 | égalité |
| Consultants | 0 | 3 métiers, 5 sessions | coût V2 |

Le temps V2 est le temps mural du lanceur. La somme des sept temps-sessions
atteint 898,229 s, car les analyses et contradictions sont partiellement
parallèles. Le cache est inclus dans l'entrée et le raisonnement dans la sortie.

## Coût par phase

| Phase | Durée session | Entrée | Sortie | Mots visibles |
| --- | ---: | ---: | ---: | ---: |
| SA-01 · analyse | 62,931 s | 13 559 | 1 566 | 999 / 1 200 max |
| SA-02 · analyse | 72,214 s | 13 561 | 1 840 | 995 / 1 200 max |
| SA-01 · contradiction | 48,026 s | 16 242 | 1 143 | 428 / 600 max |
| SA-02 · contradiction | 38,788 s | 16 244 | 898 | 471 / 600 max |
| MAIN · première solution | 236,374 s | 153 193 | 6 106 | 350 |
| SA-03 · critique | 118,418 s | 20 440 | 3 116 | 614 / 1 200 max |
| MAIN · arbitrage final | 321,478 s | 302 774 | 8 406 | 490 |
| **Total** | **898,229 s-agents** | **536 013** | **23 075** | **4 347** |

## Relation sociale observée

SA-01 privilégie le contrat et la surface d'attaque ; SA-02 propose la
séparation `calculate` / parsing / CLI / point d'entrée. Leurs analyses sont
largement redondantes. Leur contradiction utile porte sur la grammaire : ils
convergent vers exactement trois éléments séparés par des espaces blancs
souples, en rejetant `2+3`.

MAIN arbitre 23 recommandations initiales : 19 retenues et 4 écartées. Il crée
ensuite la première solution sans lancer l'arbitre officiel. SA-03 formule
3 défauts, 6 risques et 6 préférences. MAIN qualifie les 15 points : 10 retenus,
5 écartés, aucun laissé non vérifiable après les tests.

Trois changements sont réalisés avant le premier passage officiel : exemple
d'import README reproductible, capture de Ctrl-C étendue à toute la boucle et
annotation interne compatible avec d'anciennes versions Python 3. La suite
officielle ne mesure pas ces améliorations ; elles ne créent donc pas un gain
quantifié face à V1.

## Tension de protocole conservée

SA-03 estime que `DECISIONS.md` est un troisième livrable contraire à la liste
du challenge. MAIN le conserve parce que le protocole V2 exige une table
d'arbitrage dans `solution/`. Le vérificateur accepte ce fichier, mais ne tranche
pas l'ambiguïté textuelle. L'incident est publié sans réécrire le challenge ni
la suite.

## Preuves

- [PV verbatim filtré](../runs/sol-core-v2-001/PV.md) : les sept prompts et
  réponses visibles, dans l'ordre.
- [Trace JSON](../runs/sol-core-v2-001/trace.json) : threads, événements et
  compteurs.
- [Métadonnées](../runs/sol-core-v2-001/run.json) : empreintes, paramètres et
  résultats.
- [Solution et arbitrages](../runs/sol-core-v2-001/solution/DECISIONS.md).

Une seule observation V1 et V2 est disponible. Le résultat établit l'absence
de gain sur cette cellule, pas l'inefficacité générale du multi-agent.
