# Historique synthétique des échanges

**Français** · [English (UK)](history.en.md) · [Español](history.es.md) · [Português](history.pt.md)

Ce journal ne reproduit pas les conversations. Il conserve les demandes,
réponses et décisions utiles à l'audit du projet, dans l'ordre d'exécution et
sans date ni heure.

## Échange 001

**Demande synthétique** — Établir une référence avec un agent Codex unique sur
le défi Calculator, sans délégation et sans modifier les tests.

**Réponse synthétique** — La calculatrice, sa CLI et sa documentation ont été
produites dans une tentative isolée. Le premier passage connu a réussi les six
contrôles.

**Trace utile** — Un agent, deux fichiers livrés, aucune dépendance externe,
6/6, environ 18 086 tokens.

## Échange 002

**Demande synthétique** — Enregistrer proprement la V1 et préparer sa
publication GitHub avant la comparaison multi-agent.

**Réponse synthétique** — Les métadonnées et le rapport ont été ajoutés, les
permissions normalisées et le dépôt publié avec une identité et une clé SSH
dédiées.

**Trace utile** — Résultat V1 publié ; branche locale et distante synchronisées.

## Échange 003

**Demande synthétique** — Conserver le helper SSH local sans le publier.

**Réponse synthétique** — Le helper a été placé sous exclusion Git. À la suite
d'une suppression erronée puis d'une clarification humaine, sa version locale
a été conservée hors du suivi.

**Trace utile** — Intervention humaine de clarification ; aucun secret suivi
par Git.

## Échange 004

**Demande synthétique** — Dépasser le simple score et documenter précisément
ce que l'agent a fait et comment il l'a fait.

**Réponse synthétique** — Le rapport V1 a été enrichi avec gouvernance,
traitement technique, matrice des contrôles, métriques, incidents, analyse
qualitative et limites.

**Trace utile** — Rapport détaillé publié ; vérificateur toujours à 6/6.

## Échange 005

**Demande synthétique** — Donner envie de suivre les V2 et V3, afficher
l'avancement, expliquer l'angle R&D social, créditer l'auteur et formaliser une
gouvernance publique légère.

**Réponse synthétique** — La page d'accueil a été restructurée autour de la
question expérimentale, d'une feuille de route visible et d'un schéma Mermaid.
Une identité visuelle originale, un format de restitution et une politique de
journalisation synthétique ont été ajoutés.

**Trace utile** — README, gouvernance, journal public et bannière du projet.

## Échange 006

**Demande synthétique** — Monter les exigences techniques avec une calculatrice
scientifique capable de produire des courbes.

**Réponse synthétique** — Un second niveau de difficulté a été ajouté à la
feuille de route. Il sera exécuté dans chacun des modes afin de ne pas confondre
la difficulté du défi avec l'effet social de l'organisation des agents.

**Trace utile** — Décision méthodologique : matrice défis × organisations.

## Échange 007

**Demande synthétique** — Formaliser le commit et le push après chaque échange,
ajouter une version anglaise, présenter l'auteur et son CV, adapter le format
des réponses et expliquer l'authentification SSH sous VS Code.

**Réponse synthétique** — La gouvernance impose désormais un commit descriptif
et son push, le README dispose d'une version anglaise liée manuellement, la bio
publique renvoie vers LinkedIn et le CV, et une note explique l'usage sûr de
`ssh-agent`. Pour protéger le rythme de travail sans falsifier l'expérience,
les heures sont retirées des Markdown plutôt que remplacées par des valeurs
fictives.

**Trace utile** — Documentation bilingue, format objectif/réponse/TODO,
politique Git par échange et guide SSH sans stockage de phrase secrète.

## Échange 008

**Demande synthétique** — Retirer les heures des Markdown publics et améliorer
progressivement les règles de gouvernance au fil des enseignements du projet.

**Réponse synthétique** — La confidentialité des horaires est confirmée sans
recours à des données fictives. Une règle d'évolution contrôlée de la
gouvernance est ajoutée pour transformer les apprentissages réutilisables en
consignes futures sans réécrire les runs passés.

**Trace utile** — Gouvernance adaptative, minimale, journalisée et non
rétroactive.

## Échange 009

**Demande synthétique** — Stabiliser le protocole, figer les tests de la
calculatrice scientifique, créer une tentative solo, l'exécuter et présenter
son rapport avant toute variante multi-agent.

**Réponse synthétique** — La spécification scientifique est figée avec son
prompt solo et une suite d'acceptation indépendante. Les scripts de création et
de vérification prennent désormais en charge plusieurs défis sans changer le
comportement historique de Calculator Core.

**Trace utile** — Protocole Scientific Calculator préparé avant la création du
premier run candidat.

## Échange 010

**Demande synthétique** — Exécuter la première référence solo du défi
Scientific Calculator et présenter son rapport complet avant toute variante
multi-agent.

**Réponse synthétique** — Un agent Codex unique a livré le moteur, la CLI et la
documentation en 331 secondes. Après deux corrections autonomes, le résultat
final et sa vérification indépendante atteignent 9/9.

**Trace utile** — Premier passage 3/9 avec six erreurs liées au chargeur de
tests, passe intermédiaire non mesurable, résultat final 9/9, 8 459 tokens de
sortie et aucune intervention humaine fonctionnelle. Le biais `dataclass` du
vérificateur entraîne une nouvelle règle de calibration pré-run.

## Échange 011

**Demande synthétique** — Transformer l'avancement en tableau de bord plus
graphique, planifier V1 à V3 sur les deux difficultés, intégrer des jalons
d'affinage et étudier V2.1, V4 ainsi qu'un rendu STL ludique.

**Réponse synthétique** — Le README bilingue affiche désormais les six cellules
principales, leur progression, la prochaine étape et le TODO complet. Les
règles de campagne distinguent les observations, les affinages et les relances
comparables ; V2.1 reste une optimisation exploratoire et V4 un témoin
historique facultatif.

**Trace utile** — Tableau de bord Mermaid, bannière claire/sombre, plan
expérimental versionné et objet STL octaédrique ; aucun run supplémentaire
lancé.

## Échange 012

**Demande synthétique** — Restaurer la palette sombre du tableau de bord et
éviter le fond blanc du rendu STL lorsque GitHub est utilisé en mode sombre.

**Réponse synthétique** — Le Mermaid retrouve ses fonds bleu nuit, violet et
orange avec texte clair. Un aperçu 3D clair/sombre suit désormais le thème du
visiteur, tandis que le lecteur STL natif au fond imposé par GitHub reste
accessible dans un volet repliable.

**Trace utile** — Deux aperçus PNG thématiques, modèle STL inchangé et nouvelle
règle de contrôle visuel multi-thème ; aucun run expérimental affecté.

## Échange 013

**Demande synthétique** — Nommer explicitement les objectifs Calculatrice Core
et Calculatrice Scientific, examiner le nom des README de dossier et proposer
les documents publics en anglais britannique, espagnol et portugais.

**Réponse synthétique** — Les objectifs sont explicités dans le tableau de bord
et les rapports. Les `README.md` de dossier sont conservés pour leur rôle
d'accueil contextuel sur GitHub ; chaque document éditorial public reçoit des
versions `.en.md`, `.es.md` et `.pt.md` reliées par une navigation réciproque.

**Trace utile** — Localisation quadrilingue de l'accueil, de la gouvernance,
des rapports, du guide SSH et du journal. Les protocoles, prompts, traces et
livrables de runs restent canoniques et immuables.

## Échange 014

**Demande synthétique** — Rejouer toute la V1, remplacer la référence publiée,
préparer le protocole V2 et évaluer une proposition de limiter contexte et
effort afin de mieux mesurer l'organisation multi-agent.

**Réponse synthétique** — Deux tentatives neuves et paramétrées ont reproduit
Core à 6/6 et Scientific à 9/9. Les rapports `002` deviennent les références
courantes sans supprimer les `001`. Le protocole V2 fixe trois consultants, un
seul écrivain, le modèle, l'effort, le contexte, la compaction et les mesures.

**Trace utile** — V1 : 193 s et 556 461 tokens cumulés pour Core ; 541 s et
603 492 pour Scientific, sans aide humaine fonctionnelle. Un biais de chargeur
`dataclass` et une collision entre périmètre du run et règle Git sont conservés.
La gouvernance distingue désormais budget cognitif, effet plafond et futur
défi de grande ampleur.

## Échange 015

**Demande synthétique** — Clarifier qui a réellement exécuté V1, conserver un
procès-verbal des échanges et afficher la valeur expérimentale comme une vraie
formule mathématique dans le README.

**Réponse synthétique** — V1 distingue désormais le commanditaire,
l'orchestrateur expérimental et la session candidate Codex mandatée ; seul le
candidat n'a utilisé aucun consultant ou sous-agent. Chaque run `002` possède
un PV numéroté, rendu obligatoire pour V2 et les modes suivants.

**Trace utile** — Topologie des acteurs ajoutée aux métadonnées et rapports,
politique de journalisation renforcée, formule rendue en notation mathématique
GitHub dans les quatre langues.

## Échange 016

**Demande synthétique** — Définir précisément la validation du contexte par
consultant, rendre les derniers arbitrages V2 explicites et conserver les
textes inter-agents afin d'analyser relation sociale et efficacité.

**Réponse synthétique** — Le protocole distingue capacité active, compaction,
consommation cumulée et dossier transmis. Il préenregistre trois métiers, une
analyse indépendante, une contradiction croisée, une critique adversariale et
un PV verbatim filtré accompagné d'une synthèse analytique.

**Trace utile** — Huit arbitrages identifiés avant gel ; modèle de PV en quatre
langues ; comparaison séparée de la qualité initiale/finale, du temps mural et
des temps-agents, des tokens par rôle et du bruit de coordination.

## Échange 017

**Demande synthétique** — Valider les arbitrages V2 proposés et déterminer si
GPT-6 Astra en effort élevé peut servir au prochain run au regard du solde
Codex disponible.

**Réponse synthétique** — A-01 à A-08 sont gelés avec la référence comparable
`gpt-5.6-sol`/`high`; le préflight V2 devient la prochaine étape. Astra accepte
l'effort `high` et convient techniquement au multi-agent, mais l'utiliser
seulement en V2 confondrait effet du modèle et effet de l'organisation.

**Trace utile** — L'éventuelle variante Astra est classée comme nouvelle
campagne nécessitant de rejouer V1 Core et Scientific. Le solde d'interface
indique une marge positive, sans permettre de garantir le coût d'un run ;
aucun run ni sous-agent n'a été lancé.

## Échange 018

**Demande synthétique** — Analyser et corriger le projet, archiver les V1, rejouer V1 avec Astra high puis effectuer le préflight V2 après un commit/push intermédiaire.

**Réponse synthétique** — Archives à adresses stables avec empreintes SHA-256 ; campagne astra-high-001 et configuration explicite ; capture privée des sessions pour produire des preuves publiques filtrées. Node Windows fonctionne, mais le lanceur WSL ne trouve pas node. Résultats d’exécution ajoutés après clôture.

## Échange 019

**Demande synthétique** — Poursuivre après rétablissement du crédit et fournir les commandes Node.js pour WSL Debian.

**Réponse synthétique** — La Scientific interrompue par quota est conservée sans verdict ni compteurs inventés. Une nouvelle session vierge termine à 9/9, avec une correction numérique découverte après le premier 9/9 et quatre tests complémentaires réussis. Core reste à 6/6. Les rapports V1, PV visibles, métriques et archives sont publiés avant le préflight V2. Un guide Debian explique l'installation nodejs/npm et le lint épinglé.

Contrôles : vérification indépendante Core 6/6, Scientific 9/9 et réexécution des tests complémentaires 4/4 ; intégrité des preuves historiques conservée. Sessions terminées : 499,653 s et 340 988 tokens au total, hors essais interrompus et maintenance.

Clôture du préflight : quatre rôles sur quatre validés après le push V1 `c959216`, avec sessions distinctes, réponses exactes, SHA-256 et compteurs. Coût du diagnostic : 50 019 tokens ; pas de benchmark V2 lancé. La gouvernance précise désormais comment conserver les interruptions et leurs coûts incomplets, pour éviter qu'une relance masque l'incident.

Contrôle final sous WSL : Node.js `20.19.2` dans `/usr/bin/node`, npm `9.2.0` dans `/usr/bin/npm`, et markdownlint `0.47.0`. Le lint de tous les Markdown éditoriaux réussit désormais directement avec le runtime Linux.

## Échange 020

**Demande synthétique** — Confirmer l'installation de Node/npm et reprendre après le rétablissement des crédits.

**Réponse synthétique** — Node 20.19.2 et npm 9.2.0 sont confirmés dans WSL. V1 et préflight sont déjà terminés ; seule la livraison finale avait été refusée par la revue automatique à cause de son quota. Reprise de la publication sans relancer les benchmarks.

## Échange 021

**Demande synthétique** — Ne pas faire évoluer la gouvernance et rejouer V1
avec Sol en effort élevé afin de comparer Sol et Astra sur le même périmètre.

**Réponse synthétique** — Deux runs solo neufs, préenregistrés avant lancement,
reprennent défis, tests, prompts, CLI, contexte, compaction, isolation et
lanceur Astra ; seule la valeur du modèle change. Core termine à 6/6 dès le
premier passage. Scientific passe de 3/9 à 9/9 après une correction autonome du
chargement Python 3.13. Les deux verdicts sont confirmés indépendamment.

**Trace utile** — Sol totalise 1 199,432 s et 454 376 tokens contre 499,653 s
et 340 988 pour Astra, soit +140,1 % de temps et +33,3 % de tokens. Une suite
supplémentaire postérieure favorise Astra 4/4 contre Sol 0/4, mais reste
exploratoire et partiellement couplée à l'implémentation. Aucune règle de
gouvernance n'est modifiée.

## Échange 022

**Demande synthétique** — Rendre les verdicts 6/6, 9/9 et 15/15 réellement
auditables jusqu'au README, améliorer les liens entre documents, puis exécuter
V2 avec Sol en effort élevé.

**Réponse synthétique** — Le catalogue public distingue désormais 15 groupes
`unittest` et 71 contrôles élémentaires, avec une checklist Core 14 et
Scientific 57 dans les quatre README. V2 exécute trois métiers consultants et
un écrivain selon le protocole figé, d'abord sur Core puis sur Scientific sans
affinage intermédiaire. Les deux verdicts finaux indépendants atteignent 71/71.

**Trace utile** — V2 totalise 2 384,139 s et 1 475 626 tokens, soit +98,8 % de
temps et +224,8 % de tokens face à V1 Sol, sans gain sur les contrôles figés.
Core réussit au premier passage ; Scientific passe de 3/9 à 9/9 après une
correction de compatibilité du chargeur Python 3.13. Les 14 sessions, PV
verbatim filtrés, traces, décisions et métriques sont publiés. Aucune règle de
gouvernance n'est modifiée ; le jalon d'observation V2 devient la prochaine
étape.

## Échange 023

**Demande synthétique** — Rejouer V2 avec Astra en effort élevé.

**Réponse synthétique** — Préenregistrement des tentatives vierges `astra-core-v2-001` et `astra-scientific-v2-001` dans `astra-high-001`, comparées aux V1 Astra `002`. Même runner et mêmes paramètres V2 que Sol, sauf le modèle. Publication Core avant Scientific.

## Échange 024

Reprise après quotas : ajouter requirements.txt et un guide des métiers, retirer V2 Astra/high et relancer toute V2 Astra/medium en conservant Sol. Scientific high 002 avait réussi 9/9 avant sa coupure finale, confirmé indépendamment. Retrait récupérable et coûts partiels documentés. Deux dossiers vierges préenregistrés ; aucune V1 medium comparable. Gouvernance et protocole inchangés ; proposition Vx de reprise du code non activée.

Core Astra medium terminé et vérifié : 6/6 groupes, 14/14 contrôles, 375.169 s, 408 616 tokens. Publication avant Scientific. À la demande complémentaire, Core Astra high est rétabli car complet ; Scientific high reste un résultat interrompu à métriques incomplètes.

V2 Astra/medium terminée sans interruption : 15/15 groupes, 71/71 contrôles, 1 023.177 s et 978 998 tokens. Rapports, PV avec métiers, traces et décisions publiés. Scientific : trois groupes de corrections avant le premier verdict officiel. Aucun nouveau run V1, aucune évolution de gouvernance. Core high restauré ; Scientific high conservé comme interruption à coûts incomplets.

## Échange 025

Publier la conclusion sur le coût de coordination et la recherche du point de bascule, accessible dès le README et via une synthèse centrale. Distinguer calculatrice simple/scientifique des organisations V1/V2. Proposer solo, conseil, développement parallèle et binôme en Astra moyen, sans lancer de run ni modifier la gouvernance. Les comparaisons entre difficultés portent sur les écarts V2/V1 de chaque même exercice ; aucun seuil ni gain futur n'est affirmé.

## Échange 026

**Nomenclature validée : V2** reste le collectif consultatif historique ; **V2.1** désigne le développement parallèle ; **V2.2** le binôme sobre ; **V2.x** la famille de variantes futures, pas un run supplémentaire. V1 reste la référence solo. Les comparaisons futures sont en Astra moyen, sur calculatrice simple et scientifique. Les noms sont validés ; protocoles détaillés et lancements restent à valider.

Ces points proviennent du cadrage transmis ; ils ne sont pas déclarés terminés par la validation des noms V2.x. [Chantier documentaire joint — restant à réaliser](../docs/reading-guide.md).

## Échange 027

Réaliser le chantier documentaire joint sans relancer les expériences : README avec flux V2, guide à deux niveaux et séquence parallèle, cinq couvertures de PV générées en quatre langues, analyses sourcées séparées. Instrumentation future optionnelle : intervalles relatifs, dépendances et groupes ; lanceur historique intact. Douze tests de maintenance réussis sans appel modèle ; neuf solutions existantes revérifiées. Les anciens publishers sont vérifiés dans leur version Git, sans réécrire les empreintes. [Bilan complet](../docs/documentation-audit.md). Gouvernance et preuves inchangées. Validation réelle de l’instrumentation et rendu GitHub clair/sombre restent ouverts ; aucun nouveau run autorisé implicitement.

## Échange 028

À la demande de l’auteur, réintroduire le contexte avant les conclusions : pourquoi ce laboratoire R&D, quels exercices, quelle question sur la collaboration et quelle démarche au microphone. Faire descendre les constats après le tableau de bord, le schéma V2 après l’explication expérimentale et la nomenclature dans la feuille de route. Quatre langues synchronisées ; aucune mesure ni preuve modifiée.

## Échange 029

Préparer uniquement V1 Astra moyen sur les deux calculatrices, sans lancer de candidat. Deux dossiers vierges préenregistrés dans la campagne associée astra-medium-001 ; configuration V1 historique modifiée uniquement de high à medium. Capture historique conservée, nouvelle instrumentation désactivée. 44/44 contrôles statiques et 12 tests de maintenance réussis ; aucun appel modèle de test. Comparabilité, limites d’une référence après V2, absence de garantie de quota et commandes de contrôle documentées en quatre langues. Compétence OpenAI Docs utilisée pour les paramètres, sans considérer la documentation comme une preuve d’accès au modèle. Gouvernance et anciens résultats inchangés ; le lancement nécessite une nouvelle autorisation.

## Échange 030

Autorisation de lancer uniquement V1 simple Astra moyen, puis vérifier et publier avant Scientific. Session solo distincte sans consultant : 98,572 s, 98 496 tokens entrée + sortie, 6/6 groupes et 14/14 contrôles dès le premier passage, confirmés indépendamment. Incident de chemins sans correction fonctionnelle ; PV supplémentaire candidat conservé comme tension de livrables. Code figé dans ddf4745, rapport/PV/trace/métadonnées publiés séparément. V2 simple moyen : ×3,81 temps, ×4,15 tokens, score égal ; limites de causalité explicites. Scientific demeure vierge ; gouvernance et arbitres inchangés.

## Échange 031

Autorisation et exécution de V1 scientifique Astra moyen après publication Core. Candidat solo distinct : 188,560 s, 119 388 tokens, 9/9 groupes et 57/57 contrôles au premier passage puis indépendamment ; aucun correctif après verdict. Code inchangé dans aaa83de, autorisation b312fb5 ; PV, verbatim, trace et métriques publiés séparément. Deux sondes après run exposent les limites longueur/récursion, hors score. Comparaison complète : V2 ×3,56 temps et ×4,49 tokens, même score ; apport de robustesse de SA-03 distingué. Quatre langues et navigation actualisées, gouvernance et suites inchangées, aucune variante lancée. [Bilan complet et preuves](../results/astra-medium-v1-v2.md)

## Échange 032

Préparer V2.2 Astra moyen sans lancement : deux métiers (MAIN et REV-01), trois sessions fraîches, une revue de 1200 mots. Trois projets de mandat canoniques et protocole en quatre langues : entrées, droits, PV verbatim/arbitrages, diagnostics avant/après, coûts, interruptions et comparaison exploratoire distincte d’une confirmation répétée. Non gelé ; aucun dossier candidat, configuration ou lanceur V2.2 créé, aucun appel modèle. Règles générales, suites, lanceurs et runs historiques inchangés. Suite : préparation technique et tests à faux candidats avant préflight. [Protocole V2.2](../governance/V2_2_PROTOCOL.md)

## Échange 033

Préparer le relais V2.2 avec transport factice, capture JSONL, transmissions complètes, instantanés, audit des écritures et arrêt sans relance. Ajouter deux configurations de brouillon, choix non validés et inventaire de 15 empreintes. Préflight : deux défis simulés, trois phases chacun, aucun appel modèle ni score ; 26 nouveaux tests, 38 au total. Lancement réel verrouillé ; isolation OS, transport réel et arbitrage des budgets restent ouverts. OpenAI Docs et aide CLI consultées pour les options, sans authentification ni appel modèle. Quatre langues, protocole, index et README actualisés ; anciennes preuves préservées. [Préflight et checklist](../results/v2-2-preflight.md)

## Échange 034

**V2.2 : choix du pilote approuvés ; 46 tests de maintenance et isolation locale 30/30.** Six processus factices, aucun appel modèle. Profil natif 26/30 : intégration modèle non qualifiée, lancement verrouillé. Comparaison Sol/Astra et effort conservée. Choix validé : pilote sans nouveau plafond global ; répétitions non autorisées. [Rapport / Report / Informe / Relatório](../results/v2-2-transport.md). OpenAI Docs ; protocol frozen = false ; model calls = 0.

## Échange 035

Reprise du même traitement après interruption du contrôle automatique d’autorisation Git pour limite d’usage. Aucun run relancé ; 52 tests et 64 empreintes historiques revérifiés. Maintien d’Astra moyen, sans demande de passage à Sol élevé.

**V2.2 : pont confiné testé ; 52 tests de maintenance réussis.** Raccordement bloqué : le CLI annonce encore des outils hors liste autorisée. Aucun appel modèle. **Astra élevé : historique uniquement, aucun nouveau run prévu.** Pont MCP stdio ajouté et testé avec MAIN/REV-01 ; fournisseur factice local sans identifiants. 7/8 contrôles d’intégration réussis : catalogue tools transmis via input/additional_tools, outils de collaboration encore annoncés malgré désactivation. Pas de sonde authentifiée, protocole non gelé. OpenAI Docs utilisé pour préparer puis confronter la configuration au comportement observé. Résultats et gouvernance générale préservés. [MCP / CLI](../results/v2-2-bridge.md)
