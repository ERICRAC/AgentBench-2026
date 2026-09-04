# Historique synthétique des échanges

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
