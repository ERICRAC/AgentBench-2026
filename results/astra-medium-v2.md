# V2 Astra medium — série exploratoire

**Français** · [English (UK)](astra-medium-v2.en.md) · [Español](astra-medium-v2.es.md) · [Português](astra-medium-v2.pt.md)

Core terminé : 6/6 groupes et 14/14 contrôles dès le premier passage, confirmés indépendamment. Scientific reste à lancer.

`astra-medium-001` · `gpt-6-astra` · `medium` (MAIN, SA-01, SA-02, SA-03).

- Core : `astra-medium-core-v2-001`.
- Scientific : `astra-medium-scientific-v2-001`.

| Core | Value |
| --- | ---: |
| Wall time | 375.169 s |
| Session time sum | 451.039 s |
| Input | 395 814 |
| Cached input (included) | 302 080 |
| Output | 12 802 |
| Reasoning (included) | 122 |
| Input + output | **408 616** |

SA-01 révise sa préférence pour les nombres finis après les échanges croisés. MAIN consigne 21 arbitrages initiaux ; SA-03 conduit seulement à préciser les limites numériques du README, sans correction fonctionnelle. 3 480 mots consultants, tous sous plafond ; 3 818 mots visibles au total. Sept threads distincts, aucune utilisation d'outil par les consultants. Le code comporte 50 lignes, le README 83 et les décisions 148.

Core medium consomme 46,5 % de temps et 28,6 % de tokens de moins que Core high (700.994 s, 572 168 tokens), à verdict officiel égal. Observation unique : pas de preuve générale qu'un effort inférieur soit meilleur. Les coûts de Scientific high interrompu restent incomplets.

[Core PV](../runs/astra-medium-core-v2-001/PV.md) · [Trace](../runs/astra-medium-core-v2-001/trace.json) · [Metadata](../runs/astra-medium-core-v2-001/run.json) · [Decisions](../runs/astra-medium-core-v2-001/solution/DECISIONS.md) · [Core high](astra-v2-core.md)

Pas de V1 Astra/medium : aucune comparaison causale V1/V2 à effort constant. Sol/high reste la campagne complète affichée (4/6). Pas de V1 supplémentaire sans demande.

[Guide](../docs/reading-guide.md) · [Astra/high](astra-v2-retired.md) · [Sol V2](sol-v2.md)
