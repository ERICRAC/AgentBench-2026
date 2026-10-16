# Expertise intermédiaire — ce que montre AgentBench

[Français](intermediate-review.md) · [English (UK)](intermediate-review.en.md) · [Español](intermediate-review.es.md) · [Português](intermediate-review.pt.md)

## Réponse à la question

> À quelles conditions une équipe d'agents devient-elle plus efficace qu'un agent seul, à modèle et effort demandés identiques, une fois comptés la qualité, le temps, les tokens et la coordination ?

**Le projet démontre une collaboration observable et des corrections utiles dans certains runs. Il n'a pas encore démontré un avantage net et reproductible du collectif.** Les calculatrices servent aujourd'hui surtout à calibrer l'expérience. Le point de bascule reste à rechercher.

La V2 consultative historique réussit les mêmes tests que le solo, à un coût supérieur. Le binôme réduit fortement ce surcoût. Son dernier essai scientifique reste à +18,8 % de tokens et +10,1 % de temps face au solo historique, sans correction après revue. Le simple allégé est plus rapide et moins consommateur en tokens bruts que le solo historique, mais OBS-001 modifie le travail accompli ; il ne valide pas une victoire du binôme.

Cette expertise porte sur les artefacts existants. Elle comprend deux relectures indépendantes de méthode et d'observation sociale, hors candidats. Aucun benchmark ni nouvelle campagne modèle n'est lancé. Les coûts de cette expertise ne sont pas inclus dans les coûts candidats ; ils ne sont pas enregistrés.

## Mesures vérifiées

| Défi, Astra moyen | Organisation | Temps (s) | Tokens entrée + sortie |
| --- | --- | ---: | ---: |
| Simple | Solo V1 | 98,572 | 98 496 |
| Simple | V2 consultative | 375,169 | 408 616 |
| Simple | Binôme supervisé | 159,977 | 113 774 |
| Simple | Binôme allégé, OBS-001 | 65,964 | 87 775 |
| Scientifique | Solo V1 | 188,560 | 119 388 |
| Scientifique | V2 consultative | 648,008 | 570 382 |
| Scientifique | Binôme allégé | 207,630 | 141 794 |

Tous ces résultats finaux passent leur suite : simple 6 groupes / 14 contrôles, scientifique 9 groupes / 57 contrôles. Les rapports historiques détaillent les conditions et les écarts. Les lignes ne constituent pas une seule campagne contrôlée ; une observation par condition ne mesure pas la variabilité.

[Données recalculées et empreintes](intermediate-review-data.json) · [Bilan V1/V2](astra-medium-v1-v2.md) · [Simple allégé et OBS-001](v2-2-lean-001.md) · [Scientifique 002](v2-2-lean-scientific-002.md).

## Le score masque des différences de qualité

Deux sondes déjà connues ont été appliquées de manière identique aux trois solutions scientifiques archivées sous Python 3.13.5, en lecture seule :

| Sonde | Résultat attendu | Solo V1 | V2 consultative | Binôme allégé |
| --- | ---: | --- | --- | --- |
| P1 : 1 suivi de 10 000 espaces | 1 | Rejet, limite de longueur | 1 | 1 |
| P2 : somme de 1 500 termes égaux à 1 | 1 500 | Rejet, complexité | 1 500 | Rejet, complexité |

**La V2 historique traite ces deux cas, contrairement aux autres solutions sur au moins un cas.** Sa trace relie une critique SA-03 aux corrections de longueur/profondeur. C'est une contribution technique vérifiable sur des cas précis, pas une estimation de son effet moyen.

Ces sondes sont postérieures aux runs, choisies en connaissance des défauts et non tenues à l'écart. Elles ne forment pas un nouveau score officiel, une évaluation exhaustive ni une obligation de ressources illimitées. Un rejet révèle ici une limite d'usage ; il ne suffit pas, seul, à prononcer une violation générale du contrat.

Amélioration prioritaire : pour une nouvelle campagne, figer des contrôles plus discriminants de robustesse, intégration et reprise du code ; prévoir des cas d'évaluation indépendants inconnus des candidats. Ne pas modifier rétroactivement la suite actuelle. Les 71 contrôles ne sont ni 71 répétitions expérimentales ni une note complète de qualité.

## Ce que les échanges prouvent sur la collaboration

En V2 scientifique, des avis se contredisent, MAIN les arbitre et des corrections ciblées suivent la critique QA. Cela établit une circulation d'information et une influence observable. Cela ne prouve pas que le même développeur, avec davantage de temps ou une auto-relecture, n'aurait pas corrigé ces défauts.

Dans le dernier binôme, le relecteur ne relève aucun défaut confirmé, ne lance aucun contrôle et le code reste identique. Il distingue correctement « MAIN annonce 78 contrôles » de « j'ai consulté leur preuve ». C'est une bonne discipline de preuve, sans gain de qualité observé sur ce run. L'absence de correction ne prouve ni inutilité générale de la revue ni prévention d'une erreur invisible.

Le collectif peut aussi ajouter des contraintes discutables : MAIN avait adopté une limite de 10 000 caractères avant de la retirer après SA-03. Compter seulement les corrections finales masquerait cette trajectoire. Il faut suivre aussi les restrictions introduites puis retirées. [Décision initiale et arbitrages](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md).

Les PV permettent d'étudier accords, contradictions, adoption et corrections. Le nombre d'avis acceptés mesure des décisions, pas une efficacité. Un consensus entre instances du même modèle ne garantit pas une expertise indépendante ; ces traces ne permettent pas d'inférer à elles seules une complaisance ou une psychologie humaine.

Pour la suite, chaque constat utile devrait relier : **clause → preuve → décision → modification → contrôle avant/après**. Mesurer séparément défauts confirmés, fausses alertes, régressions, duplications et points non vérifiables. Une calibration de revue sur défauts injectés connus peut mesurer détection et précision dans une étude distincte.

[PV V2 scientifique](../runs/astra-medium-scientific-v2-001/PV.md) · [PV binôme](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).

## Les principaux biais à corriger

| Priorité | Problème | Conséquence / amélioration |
| --- | --- | --- |
| Haute | Une observation par condition, ordre et environnement variables | Décrire les écarts ; prévoir répétitions équilibrées avant une conclusion générale |
| Haute | Score déjà maximal chez le solo | Distinguer conformité minimale, robustesse, intégration et maintenabilité |
| Haute | Solo en une session, binôme en trois sessions fraîches | Le rôle social, le redémarrage et le calcul supplémentaire changent ensemble ; prévoir un contrôle solo segmenté |
| Haute | OBS-001 et nouvelles campagnes | Ne pas attribuer l'écart du simple allégé à la seule coordination |
| Moyenne | Modèle désigné par alias, effort variable entre certaines séries | Enregistrer ce que la CLI expose ; ne pas classer isolément Sol, Astra et niveaux d'effort |
| Moyenne | Tests officiels après revue pour V2 | Distinguer premier jet rétrospectif et premier passage officiel, qui n'ont pas la même place dans le parcours |
| Moyenne | Coûts exclus et interruptions incomplètement mesurées | Publier coûts candidats, essais interrompus et maintenance dans des périmètres explicites |

Deux questions doivent rester distinctes : quelle organisation complète livre le meilleur compromis pratique ? Et quel effet apporte précisément le consultant, à nombre de sessions et budget comparables ? Un essai unique ne répond pas aux deux.

## Optimisations recommandées

Le dernier scientifique dépense 65 015 tokens pour MAIN initial, 16 696 pour REV-01 et 60 083 pour MAIN final. La reprise finale représente environ 42,4 % du total. Elle inclut lecture et vérification : ce n'est pas un volume mesuré de coordination pure.

La revue et la reprise ajoutent environ 47,72 s à l'écriture initiale. Les supprimer arithmétiquement ne simule pas une autre organisation. Reprendre le thread du développeur ou maintenir un contexte plus compact est une hypothèse d'optimisation à comparer dans une nouvelle condition, pas un correctif à appliquer aux anciens runs.

Sur le simple, les tokens bruts diminuent de 98 496 à 87 775 entre solo et binôme allégé, mais entrée non cachée + sortie passe de 21 696 à 39 647. Cette seconde mesure reste un diagnostic, pas un prix ni une mesure du quota Plus. Cache, sortie, total et temps doivent être publiés séparément.

Le seuil 150 000 est contrôlé entre sessions ; il ne borne pas une session en cours. L'enveloppe de 24 000 caractères ne borne pas non plus les tokens consommés avec les outils. En cas d'échec, conserver aussi l'état des fichiers et distinguer « tous les compteurs présents » de « protocole terminé » : le moteur marque actuellement usage_complete=false à toute exception.

Enfin, regrouper la préparation et réserver un point d'entrée éditorial actuel. Les rapports et la reprise accumulent des instructions historiques ; le tableau de bord mêle références Sol et Astra. Cela coûte de l'attention et favorise les relances inutiles. Ce sont des améliorations de lisibilité, sans retoucher les preuves.

## Stratégie proposée pour chercher la bascule

**Je nuance la proposition précédente à quatre rôles : commencer par une variante parallèle légère.** Deux développeurs travaillent sur des composants isolés ; l'un assure ensuite l'intégration dans une session distincte. Trois sessions, deux métiers, puis vérification indépendante. L'intégration a un coût enregistré. Le relecteur dédié pourra être ajouté ensuite si une hypothèse le justifie. C'est une nouvelle variante proposée, pas une redéfinition rétroactive de V2.1.

Préparer en un lot un défi modulaire et son témoin V1 contemporain, mêmes interfaces et mêmes exigences. Le solo peut employer la même décomposition. Les interfaces comprennent des tests d'intégration : un découpage artificiellement sans interaction favoriserait le collectif sans tester son coût réel. Inversement, tout rendre dépendant retirerait son potentiel de parallélisme.

Le temps d'équipe dépend du chemin critique : préparation, plus le maximum des travaux parallèles, puis intégration et validation. Mesurer début/fin relatifs, chevauchement réel, temps mural, somme des temps-agents, tokens de chacun et reprises d'intégration. Un gain de délai avec davantage de tokens reste un compromis à annoncer.

Si la priorité est d'expliquer le binôme actuel, le contrôle le plus ciblé est un solo en trois sessions avec auto-relecture, avant toute nouvelle topologie. Si la priorité est d'explorer la vitesse collaborative, le pilote parallèle léger est le prochain test recommandé. Ces deux questions sont complémentaires ; lancer simultanément toutes les variantes disperserait le budget.

Un pilote renseigne sur la faisabilité, pas sur la reproductibilité. Avant la campagne, choisir la contrainte principale — délai, tokens ou qualité —, les règles d'arrêt et le budget global. Répéter ensuite les conditions prometteuses dans un ordre équilibré. Le point de bascule sera un domaine de tâches et de contraintes, pas un nombre universel de lignes de code.

## Questions encore ouvertes et expertise de jalon

- Quelle priorité domine : réduire le délai, économiser les tokens ou éviter des défauts coûteux ?
- Les défauts d'intégration et la difficulté du nouveau défi départagent-ils vraiment les organisations ?
- La critique d'un autre agent apporte-t-elle plus qu'une auto-relecture à ressources comparables ?
- Le bénéfice se maintient-il sur plusieurs essais et après prise en compte des interruptions ?

Ces questions peuvent guider les choix techniques sans multiplier les confirmations humaines. Un lancement de nouvelle campagne engage néanmoins un périmètre et un budget à fixer ensemble.

Les deux relectures d'audit ont été retenues ainsi : la revue méthodologique demande un contrôle des sessions et des mesures séparées du cache ; la revue sociale demande de compter aussi les restrictions introduites et de commencer par deux développeurs dont un intègre. Leur divergence porte sur l'ordre des expériences : expliquer le binôme par un solo segmenté, ou explorer le parallélisme. La priorité recommandée ici est le pilote parallèle léger, cohérent avec la question encore non testée ; le contrôle segmenté reste nécessaire pour isoler ultérieurement l'effet du consultant. Aucun des deux relecteurs n'est un candidat des runs étudiés.

**Rappel demandé : faire expertiser le protocole arrêté par le modèle le plus puissant disponible avant les nouveaux runs, puis relire les résultats au jalon.** La présente expertise est réalisée par la session courante avec deux relectures ; elle ne certifie pas un classement des modèles disponibles. Les métriques de coût des relectures d'audit ne sont pas exposées.

## Vérifications et accès aux preuves

Coûts de sept runs recalculés depuis leurs métadonnées ; empreintes des sources conservées ; six exécutions de sondes communes sur trois solutions ; aucun candidat ni fichier de run modifié. Le script diagnostic écrit seulement sur sa sortie standard et désactive le bytecode à son lancement.

```bash
python3 -B scripts/audit_intermediate.py
```

[Script](../scripts/audit_intermediate.py) · [Données et résultats](intermediate-review-data.json) · [Conclusion centrale](CONCLUSIONS.md) · [Catalogue des tests](../docs/acceptance-tests.md).
