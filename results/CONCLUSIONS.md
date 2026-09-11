# Conclusions — quand le collectif devient-il rentable ?

**Français** · [English (UK)](CONCLUSIONS.en.md) · [Español](CONCLUSIONS.es.md) · [Português](CONCLUSIONS.pt.md)

[Les cinq runs V2 en 2 minutes chacun](run-summaries/index.md) · [📖 Comment lire et interpréter un run AgentBench](../docs/reading-guide.md)

> Sur les tâches actuellement étudiées, le coût de coordination dépasse le bénéfice mesuré. AgentBench cherche désormais à identifier les conditions où ce rapport s’inverse : difficulté, spécialisation, parallélisme et coût des erreurs.

Ce constat concerne les comparaisons disponibles à modèle et effort identiques, avec la V2 consultative actuelle. Il ne condamne pas toutes les équipes d’agents. Les corrections supplémentaires observées ne sont pas entièrement mesurées par les tests officiels.

**V1 contre V2, Astra moyen : même score officiel sur les deux défis.** V2 utilise ×3,56 le temps et ×4,49 les tokens au total. La relecture apporte toutefois des corrections de robustesse hors score. [Bilan complet et preuves](astra-medium-v1-v2.md)

## Ce que montrent les expériences

| Comparaison | Temps V2 / V1 | Tokens V2 / V1 |
| --- | ---: | ---: |
| Sol élevé · calculatrice simple | ×4,19 | ×3,54 |
| Sol élevé · calculatrice scientifique | ×1,57 | ×3,09 |
| Astra élevé · calculatrice simple | ×7,00 | ×4,75 |
| Astra moyen · calculatrice simple | ×3,81 | ×4,15 |
| Astra moyen · calculatrice scientifique | ×3,44 | ×4,78 |

Dans ces cinq comparaisons, le score final officiel est identique : V1 est moins coûteuse en temps et en tokens. Pour Sol, le surcoût relatif diminue sur la calculatrice scientifique, sans devenir un gain. Deux difficultés et une observation par cellule ne permettent ni de situer ni d’extrapoler un seuil de bascule.

[Sol V1/V2](sol-v2.md) · [Astra Core V1/V2](astra-v2-core.md)

Les mots V1/V2 désignent des organisations, jamais des générations de calculatrice. **Calculatrice simple** = identifiant historique Core ; **calculatrice scientifique** = Scientific. On compare V1 et V2 sur chaque même exercice, puis leurs écarts entre exercices. Comparer directement V1 simple à V2 scientifique mélangerait difficulté et organisation.

En Astra moyen, le rapport de temps diminue de 3,81 à 3,44 entre simple et scientifique, mais celui des tokens augmente de 4,15 à 4,78. Aucun seuil observé. La nouvelle V1 scientifique conserve des limites d’expressions longues corrigées après SA-03 (sous-agent 3, relecteur critique) en V2 : contribution réelle, non valorisée par le score officiel ; sondes V1 postérieures et non préenregistrées.

## Organisations — références et variantes proposées

| Organisation | Répartition du travail | Hypothèse |
| --- | --- | --- |
| Solo (V1) | Un candidat réalise tout. | Deux calculatrices terminées. |
| Conseil (V2 actuelle) | Un écrivain et trois consultants. | Des avis et une relecture évitent des erreurs. |
| **V2.1** — Développement parallèle | Deux développeurs, un intégrateur et un relecteur ; contributions isolées, interfaces fixées avant développement. | Le travail simultané compense les échanges et l’intégration. |
| **V2.2** — Binôme sobre | Un développeur et un relecteur, une revue bornée. | Conserver la critique utile avec moins de coordination. |

**Nomenclature validée : V2** reste le collectif consultatif historique ; **V2.1** désigne le développement parallèle ; **V2.2** le binôme sobre ; **V2.x** la famille de variantes futures, pas un run supplémentaire. V1 reste la référence solo. Les comparaisons futures sont en Astra moyen, sur calculatrice simple et scientifique. Les noms sont validés ; protocoles détaillés et lancements restent à valider.

**V2.2 : lanceur de simulation et préflight statique réussis, sans appel modèle.** 26 nouveaux tests, 38 tests de maintenance au total ; lancement réel verrouillé, choix et isolation à valider avant gel. [Préflight et checklist](v2-2-preflight.md)

Toutes les variantes proposées utilisent Astra en effort moyen. Même modèle ne signifie pas contexte identique, expertise réellement identique ou coût total égal : les rôles, informations reçues et budgets sont enregistrés. Le binôme teste aussi un changement d’effectif ; ce n’est pas une comparaison de topologie seule.

Les variantes sont distinctes de la V2 figée : aucun benchmark existant n’est réécrit. L’écriture parallèle n’est pas autorisée par le protocole actuel. Il faudra préenregistrer un nouveau protocole, les droits par fichier ou branche, les interfaces, l’intégration et le traitement des conflits avant tout lancement.

## Comment chercher la bascule

La référence solo Astra moyen est complète. Préenregistrer maintenant les variantes, puis tester les organisations sur les deux exercices identiques. Les calculatrices monofichier constituent un premier témoin, mais offrent peu de travail réellement divisible. Étendre ensuite à un défi modulaire ou à une évolution de code existant avec davantage d’interactions ; figer les nouveaux tests avant les runs.

Mesurer séparément qualité, délai total jusqu’à validation, tokens de tous les agents, reprises d’intégration et échanges. Répéter les cellules avec ordre de passage équilibré ; fixer à l’avance budgets, arrêt et traitement des quotas. Distinguer les temps d’attente imposés des temps d’exécution. Le nombre de répétitions et le nouveau défi restent à arbitrer.

Le seuil peut être différent pour le délai, les tokens et la qualité. Une équipe plus rapide mais plus coûteuse est un compromis, pas une victoire universelle. La bascule sera un intervalle observé de conditions, pas un nombre magique de lignes de code. Si aucune bascule n’apparaît, cela reste un résultat utile.

## Limites et preuves

Les références V1 et V2 Astra moyen sont terminées sur les deux calculatrices. Les résultats V2 Astra moyen / Sol élevé changent modèle et effort ; Scientific Astra élevé a des coûts incomplets. Ils ne démontrent pas isolément l’effet de l’organisation. Les PV révèlent des corrections utiles, mais 71/71 ne mesure pas toute la qualité ni la maintenabilité.

[Astra medium](astra-medium-v2.md) · [Guide](../docs/reading-guide.md) · [README](../README.md) · [Tests](../docs/acceptance-tests.md)
