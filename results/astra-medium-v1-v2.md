# Astra moyen — bilan V1/V2 et run scientifique V1

**Français** · [English (UK)](astra-medium-v1-v2.en.md) · [Español](astra-medium-v1-v2.es.md) · [Português](astra-medium-v1-v2.pt.md)

## Conclusion en une minute

**Sur les deux calculatrices, V1 solo atteint le même score officiel que V2 consultative, avec moins de temps et de tokens.** Au total, V2 utilise **×3,56 le temps et ×4,49 les tokens**. Aucun point de bascule en faveur du collectif n’est observé sur ces mesures.

Nuance essentielle : même score ne signifie pas même robustesse. La relecture scientifique V2 a corrigé des limites de longueur/profondeur que la nouvelle V1 conserve. La coordination a donc une contribution technique observable, mais son bénéfice n’est pas valorisé par les tests officiels actuels. Ne pas conclure « les consultants ne servent à rien ».

## Comparaison à modèle et effort demandés identiques

gpt-6-astra / medium ; contexte 200000, compaction 180000, portée total. V1 = un développeur dans une session. V2 = un écrivain, trois consultants, sept sessions par défi ; pas plusieurs développeurs en parallèle.

| Calculatrice | Score final V1 = V2 | Temps V1 | Temps V2 | V2/V1 | Tokens V1 | Tokens V2 | V2/V1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Simple | 6/6 groupes · 14/14 contrôles | 98.572 s | 375.169 s | ×3,81 | 98496 | 408616 | ×4,15 |
| Scientifique | 9/9 groupes · 57/57 contrôles | 188.560 s | 648.008 s | ×3,44 | 119388 | 570382 | ×4,78 |
| Total des deux défis | 15/15 groupes · 71/71 contrôles | 287.132 s | 1023.177 s | ×3,56 | 217884 | 978998 | ×4,49 |

Tous ces premiers passages officiels réussissent ; en V2 ils interviennent après la critique obligatoire. Totaux = somme des deux runs terminés de chaque organisation, pas coût de toute la campagne ni de l’abonnement. Tokens = entrée + sortie, cache et raisonnement déjà inclus. V2 scientifique ajoute 459,448 s et 450 994 tokens à V1.

En passant de simple à scientifique, le rapport de temps diminue légèrement (3,81 → 3,44), mais celui des tokens augmente (4,15 → 4,78). La difficulté supplémentaire ne suffit donc pas à rendre cette organisation rentable selon les indicateurs officiels. Deux exercices et une observation par cellule ne permettent aucune extrapolation de seuil.

## Nouvelle V1 scientifique — traitement réalisé

Tentative astra-medium-scientific-v1-001, autorisée après publication de Core. Dossier vierge, prompt historique, aucune lecture d’une solution antérieure par le candidat, aucun consultant ni conseil V2 transmis. Le candidat lit le contrat, construit un analyseur récursif avec grammaire limitée, réutilise l’arbre pour échantillonner, génère un SVG échappé et segmenté, puis ajoute CLI, historique et documentation.

Un contrôle manuel de la CLI précède l’unique passage officiel : puissances 512, -4 et 0,25 ; récupération après division par zéro ; historique des seuls succès. **9/9 puis confirmation indépendante 9/9, sans correctif fonctionnel après verdict.** Code conservé sans retouche dans aaa83de. Fichiers : 295 lignes Python, README 83 lignes, PV candidat 51 lignes ; ce comptage ne mesure pas la maintenabilité.

Durée : 188,560 s. Entrée : 113 746, dont cache 98 944 ; sortie : 5 642, dont raisonnement 164. Total : 119 388. Cinq messages visibles, six commandes terminées, aucune délégation. Recherche rg sans résultat dans le dossier vide ; PV supplémentaire au-delà des deux livrables ; créations par redirections shell plutôt que apply_patch : faits conservés, non sanctionnés par l’arbitre technique.

## Checklist scientifique — neuf groupes, 57 contrôles

- [x] S01 · Livrables et documentation — 7 contrôles.
- [x] S02 · Bibliothèque standard et absence d’exécution dynamique interdite — 2.
- [x] S03 · Priorités, parenthèses, puissances, signes — 10.
- [x] S04 · Fonctions, constantes, notation scientifique — 6.
- [x] S05 · Variable x et noms interdits — 5.
- [x] S06 · Syntaxe, domaines, division par zéro — 6.
- [x] S07 · Échantillonnage, bornes, discontinuités — 8.
- [x] S08 · SVG valide, axes, courbe, titre échappé, contenu inerte — 7.
- [x] S09 · CLI, tracé, historique, récupération, sortie — 6.

[Chaque cas et résultat attendu](../docs/acceptance-tests.md) · [Les six groupes simples](astra-medium-v1-core.md). Aucun contrôle exploratoire ni test candidat n’est ajouté aux 71 contrôles officiels.

## Ce que le collectif apporte malgré son surcoût

En simple, les avis V2 ont surtout précisé la documentation, sans correction fonctionnelle. En scientifique, **SA-03 = sous-agent 3, relecteur critique** : après son avis, MAIN retire les limites de longueur/récursion, protège l’affichage terminal et gère les canaux CLI défaillants. Les revues croisées avaient aussi rectifié des propositions sur les fonctions composées et les expressions indéfinies partout. [Analyse V2 et preuves](astra-medium-v2.md).

Après clôture de la nouvelle V1, deux sondes exploratoires de l’orchestrateur confirment ses limites : `"1" + " " * 10000` devrait mathématiquement donner 1, et `"+".join(["1"] * 1500)` devrait donner 1500 ; toutes deux produisent ValueError. Résultats conservés dans la trace. **Ces sondes sont postérieures, V1 seulement, non préenregistrées et hors score.** L’évidence V2 provient de son rapport et de ses contrôles enregistrés ; aucun rejeu identique V2 ici. Elles montrent un angle mort du score, pas une estimation exhaustive de supériorité V2.

## Limites et prochaine décision

Une observation par cellule ; V1 collectée après V2 ; alias identique sans garantie de snapshot serveur ; charge/cache variables. La durée V1 inclut lancement/clôture CLI, V2 inclut aussi le relais ; préparation, vérification après run et publication sont exclues. Le contexte configuré n’est pas un plafond de consommation totale, ni son application une propriété démontrée par ces runs. Aucun coût monétaire fiable enregistré.

La référence Astra moyen est maintenant complète pour V1/V2 sur les deux exercices. Prochaine proposition : préenregistrer V2.2 (binôme sobre), puis V2.1 (développement parallèle), avec budgets, répétitions et mesures de robustesse explicites. Pour tester réellement le parallélisme, prévoir ensuite un défi divisible. Aucun lancement supplémentaire ni évolution de gouvernance ici. [Conclusion centrale](CONCLUSIONS.md).

## Audit — du résumé aux preuves

[PV scientifique : rôles, chronologie et textes visibles](../runs/astra-medium-scientific-v1-001/PV.md) · [Trace et sondes](../runs/astra-medium-scientific-v1-001/trace.json) · [Métadonnées](../runs/astra-medium-scientific-v1-001/run.json) · [Code](../runs/astra-medium-scientific-v1-001/solution/scientific_calculator.py) · [README candidat](../runs/astra-medium-scientific-v1-001/solution/README.md)

[V1 simple et preuves](astra-medium-v1-core.md) · [V2 et deux PV](astra-medium-v2.md) · [Préflight historique](astra-medium-v1-preflight.md) · [Index](README.md) · [Projet](../README.md)

## Vérification de la publication

Contrôles de maintenance séparés du benchmark : 12 tests unitaires sans appel modèle ; liens de 152 documents éditoriaux et 64 empreintes historiques ; reproductibilité des cinq résumés V2 ; linter Markdown et git diff --check. Audit des 11 empreintes de cette tentative et des compteurs contre la capture privée. Solutions antérieures, défis, scripts, prompts et gouvernance inchangés. Quatre doubles lignes vides signalées par le linter ont été retirées ; aucune correction du candidat.
