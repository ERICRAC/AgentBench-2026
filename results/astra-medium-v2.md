# V2 Astra moyen — résultats Core et Scientific

**Français** · [English (UK)](astra-medium-v2.en.md) · [Español](astra-medium-v2.es.md) · [Português](astra-medium-v2.pt.md)

Mise à jour de navigation : ce rapport conserve son état de publication initial. V1 Astra moyen est désormais terminée sur les deux exercices ; voir le bilan actuel. [Bilan complet et preuves](astra-medium-v1-v2.md)

[Conclusions — quand le collectif devient-il rentable ?](CONCLUSIONS.md)

Les deux runs sont terminés et confirmés indépendamment : **15/15 groupes, 71/71 contrôles**, dès le premier passage officiel. Total : **1 023.177 s et 978 998 tokens entrée + sortie**. Aucune interruption dans cette série. Ces mesures excluent maintenance, publication et anciennes tentatives.

## Verdicts

| Run | Premier passage | Verdict final | Temps mural | Tokens |
| --- | ---: | ---: | ---: | ---: |
| Core | 6/6 | 6/6 · 14/14 | 375.169 s | 408 616 |
| Scientific | 9/9 | 9/9 · 57/57 | 648.008 s | 570 382 |
| **Total** | **15/15** | **15/15 · 71/71** | **1 023.177 s** | **978 998** |

[Tests](../docs/acceptance-tests.md) · [Guide](../docs/reading-guide.md)

## Lecture sociale

Core : SA-01 retire sa préférence pour les nombres finis après les réponses croisées. MAIN consigne 21 décisions initiales, puis 11 arbitrages de critique. SA-03 provoque seulement des précisions documentaires ; aucune correction fonctionnelle.

Scientific : les réponses croisées corrigent deux propositions initiales (compositions de fonctions et expression constante indéfinie partout). MAIN produit 22 arbitrages. Après SA-03, il traite 13 points : 10 retenus, 2 écartés, 1 non vérifiable dans son dossier. Trois groupes de corrections suivent : supprimer les limites de longueur/récursion, échapper l'affichage du terminal et gérer les canaux CLI défaillants. Quatre tests candidats reproductibles passent ; ils ne s'ajoutent pas aux 71 contrôles officiels.

Les 131 assertions initiales restent des contrôles candidats. Leur script est observable dans la commande enregistrée de la trace MAIN initiale, mais n'était pas fourni à SA-03 ni à MAIN final : leur réserve « non vérifiable » concerne leur dossier, pas l'absence de capture par le relais. Aucune correction après le premier verdict officiel.

## Métriques et limites

| Metric | Core | Scientific | Total |
| --- | ---: | ---: | ---: |
| Input | 395 814 | 548 369 | 944 183 |
| Cache (included) | 302 080 | 409 216 | 711 296 |
| Output | 12 802 | 22 013 | 34 815 |
| Reasoning (included) | 122 | 955 | 1 077 |
| Session time sum | 451.039 s | 730.595 s | 1 181.634 s |

Les cinq réponses consultantes font 3 480 mots Core et 3 625 Scientific, toutes sous plafond ; tous les messages visibles font respectivement 3 818 et 4 061 mots. Sept threads neufs par run ; consultants sans outils, un écrivain, aucune aide humaine fonctionnelle. Configurations : Astra/medium, contexte 200k, compaction 180k, CLI 0.153.4 ; mêmes runner, prompts et vérificateurs. Core a été publié dans 5c143cd avant le lancement Scientific.

La somme des temps-sessions dépasse le temps mural car certaines consultations sont parallèles. Cache inclus dans l'entrée, raisonnement inclus dans la sortie : ne pas les additionner deux fois. Compteurs et textes détaillés par session dans les PV et JSON.

## Comparaison recevable

Face à V2 Sol/high, cette série prend 57,1 % de temps et 33,7 % de tokens en moins, avec le même verdict final. Le premier passage total est 15/15 contre 9/15 pour Sol, dont Scientific rencontrait un défaut de chargement Python 3.13 documenté. Le modèle **et** l'effort changent : ce n'est pas une preuve causale de supériorité d'Astra ou de medium.

Core medium prend 46,5 % de temps et 28,6 % de tokens en moins que Core high, à verdict officiel égal. Core high, entièrement terminé, est rétabli. Scientific high avait atteint 9/9 avant sa coupure finale, mais ses coûts sont incomplets : aucune comparaison de coûts totaux high/medium n'est calculée.

Aucune V1 Astra/medium n'existe : pas de dominance V1/V2 à effort constant démontrée ici. Une observation par cellule ne permet pas de généralisation statistique. Sol reste la campagne complète du tableau de bord (4/6) ; la série V2 medium est terminée à 2/2.

[Sol V2](sol-v2.md) · [Core high](astra-v2-core.md) · [Scientific high](astra-v2-retired.md)

## Reprise du code et suite

Les modules actuels contiennent 4 docstrings Core et 10 Scientific, avec respectivement 0 et 1 commentaire lexical ; dire « aucun commentaire » ne décrit donc pas toute leur documentation. Cela ne mesure pas leur maintenabilité. Le module Scientific fait 348 lignes, son README 127 ; les décisions et contrôles sont reliés ci-dessous. La Vx de reprise reste une proposition à figer, pas un nouveau score appliqué rétroactivement.

## Preuves

- Core : [PV](../runs/astra-medium-core-v2-001/PV.md) · [trace](../runs/astra-medium-core-v2-001/trace.json) · [metadata](../runs/astra-medium-core-v2-001/run.json) · [DECISIONS](../runs/astra-medium-core-v2-001/solution/DECISIONS.md).
- Scientific : [PV](../runs/astra-medium-scientific-v2-001/PV.md) · [trace](../runs/astra-medium-scientific-v2-001/trace.json) · [metadata](../runs/astra-medium-scientific-v2-001/run.json) · [README](../runs/astra-medium-scientific-v2-001/solution/README.md) · [DECISIONS](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md) · [CONTROLES](../runs/astra-medium-scientific-v2-001/solution/CONTROLES.md) · [controle_final.py](../runs/astra-medium-scientific-v2-001/solution/controle_final.py).
