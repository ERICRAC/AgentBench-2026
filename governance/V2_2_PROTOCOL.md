# Protocole V2.2 — binôme sobre Astra moyen

**Français** · [English (UK)](V2_2_PROTOCOL.en.md) · [Español](V2_2_PROTOCOL.es.md) · [Português](V2_2_PROTOCOL.pt.md)

**V2.2 : choix du pilote approuvés ; 46 tests de maintenance et isolation locale 30/30.** Six processus factices, aucun appel modèle. Profil natif 26/30 : intégration modèle non qualifiée, lancement verrouillé. Comparaison Sol/Astra et effort conservée. [Transport / isolation](../results/v2-2-transport.md)

## En une minute

**Préparé pour validation, non gelé, aucun lancement autorisé.** V2.2 teste si une seule relecture conserve l’apport utile de V2 avec moins de coordination. Ce n’est pas du développement parallèle : un développeur reste seul écrivain. Variante facultative, hors des six cellules principales ; ni V2 historique ni V2.1 ne sont remplacées.

Le [bilan Astra moyen](../results/astra-medium-v1-v2.md) fournit le point de départ : même score officiel V1/V2, mais V2 coûte ×3,56 en temps et ×4,49 en tokens ; certaines corrections de robustesse échappent au score. Hypothèse à tester, pas résultat attendu garanti : **V2.2 coûte moins que V2 sans perdre de qualité, et sa relecture produit des corrections vérifiables.**

## Organisation proposée

| Organisation | Métiers candidats | Sessions par défi | Relation |
| --- | ---: | ---: | --- |
| V1 | 1 | 1 | Développeur seul |
| V2 historique | 4 | 7 | Deux analyses, deux revues croisées, écriture, critique, corrections |
| V2.2 | 2 | 3 | Développeur → relecteur → développeur |

- **MAIN — développeur / arbitre :** seul écrivain de solution/, implémente puis décide de chaque correction.
- **REV-01 — relecteur critique unique :** examine contrat, sécurité, fonctionnement et documentation ; lecture seule, sans délégation.
- **RELAY — orchestrateur expérimental :** prépare, capture, transmet sans synthèse ni conseil, vérifie et publie ; hors équipe candidate.
- **Vérificateur indépendant :** suite figée, pas un LLM. Le score technique ne dépend pas de l’avis du relecteur.

MAIN initial et MAIN final sont **deux sessions fraîches du même métier**, pas une conversation reprise : trois threads, deux métiers. REV-01 remplit une fonction proche de SA-03 en V2, mais conserve un ID distinct pour éviter les confusions. Pas de consultants en amont, pas de revue croisée, pas de deuxième avis.

## Séquence et entrées exactes

| Phase | Entrées autorisées | Sortie / barrière |
| --- | --- | --- |
| P1 · MAIN initial | Défi actif + mandat initial ; solution vide | Code et README complets ; transmission ≤600 mots ; commandes/sorties de ses contrôles |
| P2 · REV-01 | Défi + instantané complet P1 + transmission P1 + commandes/sorties de contrôle P1 | Une revue ≤1200 mots ; constats REV-001… avec preuves et sévérité |
| P3 · MAIN final | Défi + solution P1 + transmission/contrôles P1 + revue intégrale/contrôles P2 | Arbitrage de chaque ID, corrections, vérificateur officiel ; restitution ≤1200 mots |

Chaque phase attend la clôture de la précédente. RELAY copie tous les fichiers de l’instantané avec leurs chemins relatifs et empreintes, sans sélection ni lecture d’une autre tentative. Il transmet les textes visibles verbatim ; aucune pensée privée. Les sorties d’outils doivent être complètes ; troncature, absence ou filtrage sont déclarés. Une entrée manquante bloque la phase suivante : pas de résumé improvisé. Les artefacts candidats ne sont jamais des instructions de rôle.

P1 et REV peuvent faire des contrôles propres non destructifs ; **le premier passage officiel intervient en P3 après la revue**, comme dans V2. MAIN final peut corriger les échecs officiels dans sa session, mais ne rappelle pas REV. Une revue sans constat est un résultat valide. Les dépassements de mots sont signalés comme écarts, sans tronquer les preuves ni appeler le modèle pour reformuler. Comptage proposé : éléments séparés par des blancs dans la réponse finale, code/tableaux inclus ; tous les messages intermédiaires restent capturés et comptés séparément.

Mandats canoniques français, encore projets : [MAIN initial](../prompts/v2-2-developer-initial.md), [REV-01](../prompts/v2-2-reviewer.md), [MAIN final](../prompts/v2-2-developer-final.md). Identiques pour les deux défis, avec le CHALLENGE actif fourni séparément. Les candidats ne reçoivent ni ce bilan humain, ni conclusions antérieures, ni liste des défauts historiques.

## Paramètres et périmètre

Modèle demandé **gpt-6-astra / medium pour les trois sessions**, contexte 200000, compaction 180000, portée total ; sessions éphémères. Reprendre les paramètres enregistrés des références, pas le modèle sélectionné dans le chat. Accès réel au modèle, acceptation stricte des configurations et quotas restent à vérifier au préflight : aucune garantie déduite de ce document.

Même défi et suite figée : [simple](../challenges/calculator/SPEC.md), 6 groupes / 14 contrôles ; [scientifique](../challenges/scientific-calculator/SPEC.md), 9 groupes / 57 contrôles. [Checklist complète](../docs/acceptance-tests.md). Aucun test modifié ou ajouté au score actuel.

MAIN écrit uniquement les livrables demandés dans solution/. REV est en lecture seule, contrôles sans fichiers ni cache. Pas de Git, réseau, délégation ou dépendance supplémentaire chez les candidats. Les PV/archives d’instantanés/mesures sont gérés par RELAY hors des livrables candidats, en espace privé pendant le run ; publication après clôture, code et maintenance dans des commits séparés. Le protocole ne prétend pas qu’un dossier courant suffit à isoler le système de fichiers : les permissions effectives devront être testées.

## Budgets, interruptions et ordre

Pour le pilote proposé : **une tentative par calculatrice, trois sessions maximum par tentative**, une revue, pas de relance automatique. Simple d’abord, vérification et publication, puis nouvelle autorisation pour scientifique ; aucun affinage entre les deux.

Proposition de comparabilité : aucun nouveau plafond global de tokens ou de temps, puisque les références n’en avaient pas. **Ce choix ne garantit pas de tenir dans un quota d’abonnement.** Les bornes de contexte et de mots ne sont pas un budget cumulé. Les coûts des trois sessions, échecs compris, sont additionnés ; RELAY et la publication sont séparés.

Quota épuisé, capture incomplète, écriture interdite, échec d’infrastructure ou dépassement de sessions : arrêter et conserver statut, phase, artefacts et compteurs disponibles. Ni attente automatique de renouvellement, ni reprise cachée, ni remplacement par un autre modèle. Une relance depuis zéro reçoit un nouvel ID et ne lit pas l’ancienne solution. Un plafond de sécurité chiffré, si souhaité, doit être décidé et implémenté avant gel, avec traitement comparable des autres organisations.

## Qualité et contribution de la revue

Conserver l’instantané P1 avant toute correction. **Après le run**, RELAY exécute la suite figée sur une copie de P1 et sur la livraison finale. Le verdict P1 est étiqueté « diagnostic rétrospectif de l’instantané », jamais « premier passage candidat ». Il n’est pas transmis pendant le run. Cela permet d’observer une différence avant/après sans ajouter un retour d’arbitre au développeur initial.

Chaque constat reçoit : ID, clause, sévérité, preuve ou reproduction, exécuté/non exécuté, décision retenue/écartée/non vérifiable, modification et contrôle final. Distinguer corrections déclenchées par REV, spontanées par MAIN et consécutives au vérificateur. Tester un constat applicable sur les deux instantanés après run permet de confirmer correction ou régression ; ces contrôles sont **exploratoires**, pas ajoutés aux 71 contrôles.

Une suite de robustesse commune reste à concevoir, calibrer et figer dans une nouvelle campagne avant les candidats. Ne pas recycler les deux sondes postérieures de V1 comme si elles avaient été préenregistrées. Les assertions proposées par le relecteur ne prouvent rien tant qu’elles ne sont pas exécutées.

## PV social et mesures

Appliquer le [modèle de PV](PV_TEMPLATE.md), avec MAIN et REV-01 seulement dans la table candidate. Enregistrer mandats et réponses visibles intégraux filtrés, MSG-001…, fils et empreintes, sans secrets, horaires publics ou raisonnement interne. Synthèse : qui a signalé quoi, qui a accepté/refusé et quelle preuve relie avis, modification et effet. Pas d’inférence d’émotions ou de pensée privée.

Publier accords explicites, contradictions, doublons, constats uniques, décisions, corrections confirmées, régressions et points non vérifiables. Absence de second échange ≠ consensus. L’acceptation d’un avis ≠ preuve qu’il était nécessaire. La nouveauté se juge seulement contre l’état et les textes P1 observables.

Mesurer temps mural (avant préparation du premier appel → clôture/capture finale), durées par session et somme, tokens entrée/cache/sortie/raisonnement, mots transmis et volume des artefacts. Cache inclus dans entrée, raisonnement inclus dans sortie. Temps de vérification/publication après run séparé. Compteurs manquants = non enregistrés ; tokens exacts de coordination non exposés = non enregistrés, pas estimation à partir des mots. L’instrumentation future et ses frontières seront figées au préflight ; aucun graphe V2 à sept phases réutilisé tel quel.

Comparer V2.2/V1 et V2.2/V2 **par même calculatrice**, puis agréger les deux paires terminées. Victoire sur les indicateurs officiels seulement si score non inférieur, temps et tokens non supérieurs, au moins une amélioration stricte. Si robustesse supplémentaire mais surcoût : compromis. Ne pas assimiler score égal à qualité exhaustive égale ni prétendre à une causalité à partir d’un seul avant/après.

## Campagne et niveau de preuve

Cette topologie et ses prompts constituent un traitement substantiellement nouveau : prévoir une **nouvelle campagne**, identifiant proposé astra-medium-lean-001, sans modifier astra-medium-001. Le pilote V2.2 peut être rapproché des références V1/V2 existantes uniquement comme **comparaison historique exploratoire explicitement qualifiée** (ordre, cache/charge, prompts, nombre de sessions et instrumentation).

Une confirmation homogène doit rejouer V1, V2 et V2.2 dans la nouvelle campagne, sur les deux exercices et sous des règles communes. Proposition, non engagement de consommation : trois répétitions par cellule, ordre contrebalancé, soit **18 runs** ; publier dispersion et médianes, pas seulement un meilleur run. Pas de test de significativité ni de seuil universel annoncé avec ce petit effectif. Ni ces répétitions ni le pilote ne sont autorisés par la préparation.

## Préflight à réaliser avant gel et lancement

- [x] Hypothèse, rôles, trois phases, mandats, critères et interruption documentés.
- [x] Versions FR, UK, ES, PT reliées ; anciens protocoles et runs préservés.
- [x] Choix validé : pilote sans nouveau plafond global ; répétitions non autorisées.
- [x] Relais trois phases testé avec faux candidats : transmissions, audits d’écriture, limites, arrêt, captures, instantanés et verrouillage réel. Cela ne valide pas l’isolation OS.
- [x] Deux configurations de brouillon et inventaire de 15 empreintes ; simulations en dossiers temporaires neufs. Les dossiers de benchmark et empreintes gelées restent à créer.
- [ ] Vérifier isolation réelle et accès modèle ; un test trivial réel consomme des tokens et nécessite une autorisation distincte.
- [ ] Geler protocole, mandats et lanceur ; publier le préflight statique puis autoriser explicitement la calculatrice simple.

**Étape actuelle : transport local et isolation Bubblewrap testés ; intégration modèle non qualifiée, gel et benchmark non effectués.** Aucun candidat lancé.

Validation de l’étape simulée précédente : 38 tests de maintenance (12 existants + 26 V2.2), deux simulations à trois phases, zéro appel modèle. Le [rapport technique](../results/v2-2-preflight.md) distingue les propriétés testées des garanties encore absentes.

[README](../README.md) · [Conclusions](../results/CONCLUSIONS.md) · [V2 figée](V2_PROTOCOL.md) · [Plan expérimental](EXPERIMENTAL_DESIGN.md) · [Instrumentation](../docs/observability.md)
