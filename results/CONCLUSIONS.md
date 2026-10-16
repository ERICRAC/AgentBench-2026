# Conclusions — quand le collectif devient-il rentable ?

**Français** · [English (UK)](CONCLUSIONS.en.md) · [Español](CONCLUSIONS.es.md) · [Português](CONCLUSIONS.pt.md)

[Prochain pilote et aide pour les liens WSL](../docs/parallel-pilot.md)

[Expertise intermédiaire](intermediate-review.md) — Le collectif apporte des corrections de robustesse observables, mais aucun avantage net reproductible n'est établi. Six sondes communes confirment un angle mort du score. Prochaine exploration recommandée : deux développeurs parallèles dont un intègre, avec témoin solo contemporain.

## Décision — ce que nous faisons maintenant

**Clore l'exploration V2.2 actuelle.** Les deux niveaux sont réalisés, avec leurs limites documentées. Aucun nouvel essai identique ni nouvelle optimisation du lanceur n'est recommandé à ce stade. Cela ne déclare pas les campagnes homogènes ni la question scientifique résolue.

### Le bilan en une minute

| Organisation | Constat | Décision proposée |
| --- | --- | --- |
| V2 consultative historique | Même score, coût supérieur au solo dans les comparaisons disponibles | Conserver comme référence, ne pas répéter sans nouvelle hypothèse |
| V2.2 binôme allégé | Scientifique : +18,8 % tokens, +10,1 % temps ; aucune correction après revue | Relecture explicite, mais rentabilité non démontrée |
| V2.1 développement parallèle | Pas encore mesuré | Prochaine hypothèse à tester, pas un gain acquis |

### Où le temps et les tokens partent

Sur la scientifique 002, MAIN initial prend 159,910 s ; revue et MAIN final ajoutent 47,711 s, plus environ 0,010 s de relais. Le solo historique prend 188,560 s : l'écart final est 19,070 s. Pour simplement égaler ce témoin, il faudrait retirer **9,2 % du temps total et 15,8 % des tokens du binôme** (22 406 tokens), à qualité identique. Ce sont des seuils arithmétiques par rapport à un témoin historique, pas des gains réalisables démontrés.

La revue seule représente 16 696 tokens. Même sa soustraction comptable laisserait 125 098 tokens, au-dessus des 119 388 du solo. Ce calcul n'est pas un run sans relecteur : enlever la revue changerait aussi le contexte et le comportement de MAIN final. Il montre seulement que le coût n'est pas porté par le seul consultant ; la reprise et la relecture du développeur comptent aussi.

[PV / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md) · [V1/V2](astra-medium-v1-v2.md).

### La bonne expérience suivante

**Proposition : V2.1 sur un défi modulaire, avec un nouveau témoin V1, en Astra moyen.** Exemple de périmètre à approuver : moteur de calcul d'un côté, courbes et interface de l'autre, contrat d'intégration fixé en amont. Deux développeurs en parallèle, dont un assure ensuite l’intégration ; contributions isolées et droits d'écriture bornés. Les deux organisations reçoivent exactement les mêmes exigences, interfaces et tests. Le solo peut utiliser la même décomposition.

Le défi monofichier actuel ne doit pas être changé rétroactivement. Un défi modulaire ouvre une nouvelle campagne ; les anciens résultats servent de contexte, pas de témoin causal. Préparer en un seul lot le contrat, les tests indépendants, les frontières d'écriture, le protocole d'intégration et les mesures, puis exécuter le pilote autorisé. Pas de série de préflights avec appels modèle.

Critères à fixer avant lancement : qualité au moins égale au solo, délai jusqu'au verdict final et tokens cumulés de tous les agents ; inclure l'intégration, les corrections et les essais interrompus séparément. Une baisse du délai avec hausse des tokens sera un compromis explicite. Un pilote unique ne localise pas un seuil : il détermine si des répétitions équilibrées méritent leur budget.

**Point restant à approuver : périmètre du nouveau défi et budget de la paire V1/V2.1.** Aucun plafond fiable de quota Plus n'est déduit des anciens runs. Aucun nouveau candidat ni appel modèle n'a été lancé pour cette synthèse. Ne pas relancer le pilote sans cet accord global.

**Essai scientifique 002 réussi : 9/9 groupes, 57/57 contrôles, 141 794 tokens, 207,630 s.** Aucun changement après revue. Le binôme reste plus coûteux que le solo scientifique historique ; comparaison exploratoire. [V2.2 scientifique allégée — essai 002 terminé](v2-2-lean-scientific-002.md).

Face au solo historique : **+18,8 % de tokens, +10,1 % de temps**, sans gain de score ni correction. Face à V2 historique : **−75,1 % de tokens, −68,0 % de temps**. Le binôme allégé réduit fortement le surcoût du collectif, mais ne dépasse pas le solo sur ce cas.

**Essai réel V2.2 allégé terminé : 6/6 groupes, 14 contrôles, 87 775 tokens, 65,964 s.** Cible < 100 000 atteinte. Baisse observée, mais ambiguïté de mandat OBS-001 : pas de conclusion causale. [Rapport / Report / Informe / Relatório](v2-2-lean-001.md)

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
| **V2.1** — Développement parallèle | Deux développeurs, dont un intègre ensuite (variante légère proposée) ; contributions isolées, interfaces fixées avant développement. | Le travail simultané compense les échanges et l’intégration. |
| **V2.2** — Binôme sobre | Un développeur et un relecteur, une revue bornée. | Conserver la critique utile avec moins de coordination. |

**Nomenclature validée : V2** reste le collectif consultatif historique ; **V2.1** désigne le développement parallèle ; **V2.2** le binôme sobre ; **V2.x** la famille de variantes futures, pas un run supplémentaire. V1 reste la référence solo. Les comparaisons futures sont en Astra moyen, sur calculatrice simple et scientifique. Les noms sont validés ; protocoles détaillés et lancements restent à valider.

**V2.2 simple terminée en Astra moyen : 3 sessions, 6/6 groupes (14 contrôles), 159,977 s et 113 774 tokens.** Aucun changement après revue. Moins coûteux que la V2 historique, mais davantage que le solo historique ; comparaison exploratoire. [Rapport / Report / Informe / Relatório](v2-2-supervised-core-002.md).

Toutes les variantes proposées utilisent Astra en effort moyen. Même modèle ne signifie pas contexte identique, expertise réellement identique ou coût total égal : les rôles, informations reçues et budgets sont enregistrés. Le binôme teste aussi un changement d’effectif ; ce n’est pas une comparaison de topologie seule.

Les variantes sont distinctes de la V2 figée : aucun benchmark existant n’est réécrit. L’écriture parallèle n’est pas autorisée par le protocole actuel. Il faudra préenregistrer un nouveau protocole, les droits par fichier ou branche, les interfaces, l’intégration et le traitement des conflits avant tout lancement.

## Comment chercher la bascule

La référence solo Astra moyen est complète. Préenregistrer maintenant les variantes, puis tester les organisations sur les deux exercices identiques. Les calculatrices monofichier constituent un premier témoin, mais offrent peu de travail réellement divisible. Étendre ensuite à un défi modulaire ou à une évolution de code existant avec davantage d’interactions ; figer les nouveaux tests avant les runs.

Mesurer séparément qualité, délai total jusqu’à validation, tokens de tous les agents, reprises d’intégration et échanges. Répéter les cellules avec ordre de passage équilibré ; fixer à l’avance budgets, arrêt et traitement des quotas. Distinguer les temps d’attente imposés des temps d’exécution. Le nombre de répétitions et le nouveau défi restent à arbitrer.

Le seuil peut être différent pour le délai, les tokens et la qualité. Une équipe plus rapide mais plus coûteuse est un compromis, pas une victoire universelle. La bascule sera un intervalle observé de conditions, pas un nombre magique de lignes de code. Si aucune bascule n’apparaît, cela reste un résultat utile.

## Limites et preuves

Les références V1 et V2 Astra moyen sont terminées sur les deux calculatrices. Les résultats V2 Astra moyen / Sol élevé changent modèle et effort ; Scientific Astra élevé a des coûts incomplets. Ils ne démontrent pas isolément l’effet de l’organisation. Les PV révèlent des corrections utiles, mais 71/71 ne mesure pas toute la qualité ni la maintenabilité.

[Astra medium](astra-medium-v2.md) · [Guide](../docs/reading-guide.md) · [README](../README.md) · [Tests](../docs/acceptance-tests.md)
