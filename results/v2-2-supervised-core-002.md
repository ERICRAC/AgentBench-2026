# V2.2 supervisée — binôme simple terminé

**Français** · [English (UK)](v2-2-supervised-core-002.en.md) · [Español](v2-2-supervised-core-002.es.md) · [Português](v2-2-supervised-core-002.pt.md)

**V2.2 simple terminée en Astra moyen : 3 sessions, 6/6 groupes (14 contrôles), 159,977 s et 113 774 tokens.** Aucun changement après revue. Moins coûteux que la V2 historique, mais davantage que le solo historique ; comparaison exploratoire.

Le binôme sobre a terminé sans interruption de quota et sans relance. MAIN développe, REV-01 relit en lecture seule, puis une nouvelle session MAIN arbitre et vérifie. La tentative 001 interrompue reste conservée ; la 002 repartait de zéro.

## Résultats et comparaison

| Organisation | Temps (s) | Tokens entrée + sortie | Qualité |
| --- | ---: | ---: | --- |
| V1 solo historique | 98.572 | 98 496 | 6/6 groupes, 14 contrôles |
| V2 historique, trois consultants | 375.169 | 408 616 | 6/6 groupes, 14 contrôles |
| V2.2 supervisée 002, un relecteur | 159.977 | 113 774 | 6/6 groupes, 14 contrôles |

**Sur cette calculatrice simple, le binôme n'apporte aucun gain de qualité mesuré.** L'initial et le final sont identiques ; tous deux passent les contrôles indépendants. Le relecteur ne relève aucun défaut confirmé. Par rapport au solo historique : **+62,3 % de temps, +15,5 % de tokens**. Par rapport à la V2 historique : **−57,4 % de temps, −72,2 % de tokens**. Le dispositif sobre réduit le coût observé de l'équipe, sans dépasser le solo.

Ces écarts sont exploratoires, pas un effet causal isolé : versions CLI, état du modèle servi, cache, charge, prompts et instrumentation peuvent différer. Les deux références historiques viennent du tableau « Simple » ci-dessous, pas des totaux simple + scientifique. Une observation par organisation ne permet pas de déterminer le seuil où le collectif devient rentable.

[V1 / V2 Astra medium](astra-medium-v1-v2.md)

## Mesures et limites

Entrée : 110 511 tokens ; sortie : 3 263. Les 65 280 tokens en cache sont déjà inclus dans l'entrée et les 165 tokens de raisonnement dans la sortie. Trois sessions ne signifient pas trois requêtes modèle. Somme des temps de sessions : 159,958 s ; temps mural : 159,977 s. Maintenance, publication et contrôles indépendants sont hors coût candidat.

**Quota : cet essai est allé au bout.** Solde initial et final non mesurés ; on ne peut donc pas affirmer quelle fraction d'une fenêtre Plus a été consommée ni garantir le prochain essai. Les 48,641 s et tokens manquants de 001 restent séparés : le coût total de campagne en tokens demeure incomplet.

## Preuves et lecture sociale

Premier vérificateur officiel : 6/6 ; confirmation indépendante finale : 6/6 ; diagnostic rétrospectif initial : 6/6, sans retour au candidat. Les 14 contrôles ne sont pas 14 opérations arithmétiques. La revue coûte directement 29,177 s et 14 489 tokens ; un accord explicite, aucun défaut confirmé et aucune correction. Le coût complet de coordination n'est pas isolé. Le PV nomme les métiers et publie les cinq messages retournés, les trois mandats complets et les arbitrages, sans raisonnement interne.

[PV — MAIN / REV-01](../runs/astra-medium-core-v2-2-supervised-002/PV.md) · [Prompts](../runs/astra-medium-core-v2-2-supervised-002/prompts.json) · [Trace](../runs/astra-medium-core-v2-2-supervised-002/trace.json) · [JSON](../runs/astra-medium-core-v2-2-supervised-002/run.json) · [Tests](../docs/acceptance-tests.md) · [001](v2-2-supervised-core.md) · [Protocol](../governance/V2_2_SUPERVISED.md)

## Suite

La calculatrice scientifique reste non autorisée. Prochaine proposition : décider de son lancement supervisé, neuf, en Astra moyen, sans retry automatique. Aucun autre candidat lancé ici.

[README](../README.md) · [Conclusions](CONCLUSIONS.md)
