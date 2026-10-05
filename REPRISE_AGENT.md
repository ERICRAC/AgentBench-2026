# Reprise opérationnelle — AgentBench 2026

**Mise à jour après l'échange 045 :** l'audit hors modèle et le prototype allégé
sont désormais réalisés, avec 82 tests de maintenance réussis. Lire le
[bilan de coût](results/v2-2-cost-audit.md) avant les propositions historiques
ci-dessous. Aucun lancement autorisé, aucune économie de tokens démontrée ;
mandats et seuils restent à arbitrer. Le reste décrit l'instantané de reprise initial.

Instruction de reprise destinée au prochain agent, langue canonique française.
Ce fichier n'est ni un nouveau protocole ni un mandat candidat. Il relève de
l'exception « instructions agent » d'AGENTS.md : il n'est pas traduit en quatre
versions susceptibles de diverger. Les rapports éditoriaux liés sont multilingues.

## À lire en premier : ne rien relancer

**La V2.2 simple Astra moyen est terminée, vérifiée, documentée et poussée.**
Une interruption de conversation ne signifie pas que le benchmark a échoué.
Ne pas recommencer le run, sa publication ou une qualification historique.
La prochaine priorité proposée est de réduire le coût du dispositif, sans appel
modèle candidat. Cette proposition n'est pas un accord de lancement.

L'utilisateur demande maintenant une migration de conversation parce que son
interface semble n'accepter qu'un prompt entre deux lancements de VS Code et
que cette conversation n'apparaît pas dans son nouveau projet local.
Ce document conserve le contexte opérationnel disponible et pointe vers les
preuves du dépôt. **Ce n'est pas une exportation intégrale de la conversation** :
les anciens messages de l'assistant non disponibles, les pièces jointes privées,
l'état interne du client et les métriques non enregistrées ne sont pas recréés.
Ne pas promettre une migration native du chat ni une mémoire absolument sans perte.

Instantané de reprise : après `ecdac58`, avant le commit qui ajoute ce document.
À l'ouverture, vérifier `git status --short` et `git log -5 --oneline` : l'état
du dépôt peut avoir changé depuis cette rédaction.

### Premier message conseillé au nouvel agent

```text
Reprends AgentBench-2026. Lis REPRISE_AGENT.md et AGENTS.md, puis uniquement
les références nécessaires. Vérifie le répertoire, la distribution et Git.
La V2.2 simple supervisée 002 est terminée et publiée : ne la rejoue pas.
Ne lance aucun candidat, sous-agent ou benchmark ; ne modifie pas la
gouvernance ni les preuves historiques. Commence par un bilan très court
de la reprise et distingue le problème d'interface du coût expérimental.
Propose ensuite un travail borné pour alléger le dispositif sans appel modèle
candidat. Préserve tous les résultats. Toute nouvelle campagne ou exécution
réelle devra être explicitement approuvée. Évite de charger toutes les traces.
```

## Mission et vocabulaire

AgentBench est un laboratoire R&D public sur le comportement social des agents :
qui influence qui, quels conseils changent réellement le résultat, à quel coût
en qualité, temps, tokens et coordination ? La calculatrice est un support
expérimental, pas l'objectif ultime du projet.

Question centrale validée par l'utilisateur : à partir de quelle difficulté,
spécialisation, parallélisation ou réduction d'erreurs le collectif devient-il
plus efficace qu'un agent seul ? Le seuil n'est pas établi.

> Sur les tâches actuellement étudiées, le coût de coordination dépasse le bénéfice mesuré. AgentBench cherche désormais à identifier les conditions où ce rapport s'inverse : difficulté, spécialisation, parallélisme et coût des erreurs.

Cette conclusion ne condamne pas tous les collectifs. La V2 historique possède
un seul écrivain : elle ne mesure pas plusieurs développeurs parallèles.
Le score officiel ne couvre pas toute la robustesse ni la maintenabilité.
La formule qualité / (temps + tokens + coordination) du README est illustrative,
pas un indicateur numérique additionnant des unités incompatibles.

| Terme | Sens |
| --- | --- |
| Core / simple | Calculatrice à quatre opérations, défi indépendant |
| Scientific / scientifique | Expressions, fonctions, variable, courbes SVG, CLI et historique |
| V1 | Un candidat solo, mandaté par un orchestrateur expérimental extérieur |
| V2 historique | MAIN écrivain, trois consultants, sept sessions avec certaines phases parallèles |
| V2.1 | Développement parallèle envisagé ; aucun lancement implicite |
| V2.2 | Binôme sobre : développeur, relecteur, développeur final |
| V2.x | Famille de variantes facultatives, pas un résultat supplémentaire |
| V3 | Codex avec consultants locaux Ollama, à préparer |
| V4 | Témoin historique facultatif, ne remplace aucune cellule principale |

Ne pas appeler les deux calculatrices V1 et V2. La campagne principale compte
six cellules : trois organisations V1/V2/V3 × deux difficultés. V2.x n'augmente
pas ce compteur. Plusieurs modèles et campagnes existent : ne pas les fusionner.

## Ce que souhaite l'utilisateur

- Des résultats concrets, pas une succession indéfinie de petits préflights.
- Une lecture synthétique d'abord, puis des liens vers les preuves et détails.
- Des métiers explicités : SA-03 signifie sous-agent critique qualité, pas un code opaque.
- Les textes visibles des échanges entre agents, les arbitrages et leur analyse sociale.
- Une distinction entre modèle, effort et organisation ; ne pas attribuer un gain à la mauvaise variable.
- Conserver Sol élevé, Astra élevé et Astra moyen dans les comparaisons historiques.
- Ne plus lancer Astra élevé : consommation jugée trop importante. Astra moyen était le dernier choix candidat ; ne pas déduire le modèle actuel du nouveau chat de ce choix historique.
- Ne pas garantir qu'un run tiendra dans une fenêtre de quota. Ne pas convertir sans preuve les tokens en quota d'abonnement.
- Ne pas faire évoluer la gouvernance générale pendant ce chantier de reprise.
- Chaque échange qui modifie des fichiers suivis : commit avec titre et corps, puis push, sauf instruction contraire.
- Garder `Passphrase.sh` local, hors Git ; ne pas le supprimer et ne pas publier son contenu.
- Documents publics sans heures de travail, jamais d'heures fictives ; numéros d'échanges dans le journal.
- Éditorial FR, anglais britannique, espagnol et portugais avec navigation ; instructions et preuves canoniques restent dans leur langue.
- Le projet a été conçu au microphone avec Codex par Éric Racineux. Profil public et bio déjà dans le README ; ne pas inventer de détails personnels.

## État des travaux et jalons

| Étape | État / référence |
| --- | --- |
| Premières V1 | Conservées et archivées ; voir [archives](results/ARCHIVE_V1.md) |
| V1 Sol élevé et Astra élevé | Comparaisons publiées ; voir [Sol/Astra](results/sol-vs-astra-v1.md) |
| V2 Sol | Simple et scientifique publiées ; [rapport](results/sol-v2.md) |
| V2 Astra élevé | Simple rétablie ; scientifiques interrompues ne sont pas des références complètes ; [retraits](results/astra-v2-retired.md) |
| V1/V2 Astra moyen | Deux difficultés terminées, [bilan](results/astra-medium-v1-v2.md) |
| V2.2 renforcée, transport MCP | Qualification NON-GO conservée, [diagnostic](results/v2-2-dispatch.md) |
| V2.2 pilote supervisé 001 | Quota après 48,641 s ; revue non lancée ; [rapport](results/v2-2-supervised-core.md) |
| V2.2 pilote supervisé 002 | Trois sessions terminées ; [rapport actuel](results/v2-2-supervised-core-002.md) |
| Allègement du protocole | Proposition suite aux coûts, non implémentée |
| Nouvelle scientifique supervisée | Non autorisée, ne pas lancer |
| V2.1, V3, V4 | Ne pas lancer à partir de cette reprise |

Les anciens documents de qualification gardent des « prochaines étapes »
historiques. Ils ne remplacent pas l'état le plus récent. En particulier,
`results/v2-2-dispatch.md` décrit le dispositif renforcé, pas l'échec du pilote
supervisé 002. Le rapport 002 propose une scientifique, mais l'échange utilisateur
suivant a remis la réduction des coûts au premier plan : pas de lancement.

Commits utiles, déjà publiés avant cette reprise :

- `3587167` : arrêt du pilote 001 pour quota.
- `eecd56d` : autorisation et réservation du pilote 002, avant lancement.
- `064c3c5` : code candidat 002, séparé des rapports.
- `ecdac58` : bilan, preuves et publication 002.

## Dernier run : vérité opérationnelle détaillée

Identifiant : `astra-medium-core-v2-2-supervised-002`.
Campagne : `astra-medium-supervised-001`. Modèle demandé `gpt-6-astra`, effort
`medium`. Trois sessions fraîches, deux métiers ; MAIN final n'est pas une
reprise du thread MAIN initial. RELAY transporte les données et publie, hors
périmètre candidat. Aucun autre consultant.

| Phase | Métier | Durée s | Entrée | Sortie | Total |
| --- | --- | ---: | ---: | ---: | ---: |
| MAIN initial | Développeur | 104,812 | 49 294 | 2 255 | 51 549 |
| REV-01 | Relecteur critique | 29,177 | 13 893 | 596 | 14 489 |
| MAIN final | Arbitre, vérification | 25,969 | 47 324 | 412 | 47 736 |
| Total | Trois sessions | 159,958 | 110 511 | 3 263 | 113 774 |

Temps mural : 159,977 s. Cache : 65 280 tokens inclus dans l'entrée ; raisonnement :
165 inclus dans la sortie. Ne pas doubler ces compteurs. Nombre de requêtes modèle
non enregistré : trois sessions ne veulent pas dire trois requêtes.
Les frais de maintenance, d'orchestration hors candidat, de publication et de
vérification indépendante ne sont pas inclus dans le coût candidat.

Résultat officiel premier passage final : 6/6 groupes, 14 contrôles.
Confirmation indépendante après run : même verdict.
Diagnostic rétrospectif initial : même verdict, non transmis au candidat.
Les fichiers initial et final sont identiques octet pour octet.
Le relecteur n'a exécuté aucun test et n'a identifié aucun défaut confirmé.
MAIN a retenu sa conclusion générale sans modifier le code.
Les limites Ctrl+C non testé et valeurs inf/nan acceptées ne constituent pas
des violations confirmées du contrat.

Conclusion sociale : un accord explicite, aucune correction et aucun gain de
score attribuable à la revue. Pas de preuve d'inutilité universelle des revues.
Le coût direct de REV-01 est connu ; le coût total de coordination n'est pas isolé.

Les soldes initial/final de quota ne sont pas mesurés. Cet essai a terminé sans
interruption ; ne pas prétendre qu'il a consommé un quota plein, ni qu'un autre
essai terminera forcément. Le coût du 001 interrompu reste séparé, avec ses
tokens manquants : aucun total complet de campagne ne peut être annoncé.

### Preuves à ouvrir seulement selon le besoin

Dossier [run 002](runs/astra-medium-core-v2-2-supervised-002/) :

- [PV.md](runs/astra-medium-core-v2-2-supervised-002/PV.md) : métiers, huit messages numérotés, analyse et décisions.
- [run.json](runs/astra-medium-core-v2-2-supervised-002/run.json) : sessions, threads, configurations, empreintes, durées et usages.
- [prompts.json](runs/astra-medium-core-v2-2-supervised-002/prompts.json) : trois mandats intégraux, avec données transmises.
- [trace.json](runs/astra-medium-core-v2-2-supervised-002/trace.json) : événements visibles, commandes et sorties, sans raisonnement interne.
- [verifications.json](runs/astra-medium-core-v2-2-supervised-002/verifications.json) : sorties exactes des trois contrôles officiels/indépendants.
- [snapshots.json](runs/astra-medium-core-v2-2-supervised-002/snapshots.json) : instantanés initial et final.
- `initial/` et `solution/` : fichiers candidats conservés, à ne pas transmettre à un futur candidat.
- [CHALLENGE.md](runs/astra-medium-core-v2-2-supervised-002/CHALLENGE.md) : contrat applicable.

Les captures brutes privées étaient dans un répertoire temporaire hors Git :
ne pas en faire une dépendance de reprise ou supposer qu'elles sont toujours là.
Les preuves publiques normalisent le chemin temporaire et excluent le
raisonnement privé. Ni une trace ni ce document ne certifient des événements
qui n'ont pas été observés.

## Comparaison et coût : ce qui est établi

| Calculatrice simple, Astra moyen | Temps s | Tokens | Verdict |
| --- | ---: | ---: | --- |
| V1 historique | 98,572 | 98 496 | 6/6 groupes, 14 contrôles |
| V2 historique | 375,169 | 408 616 | Même score |
| V2.2 supervisée 002 | 159,977 | 113 774 | Même score |

V2.2 / V1 : +62,3 % de temps, +15,5 % de tokens.
V2.2 / V2 : −57,4 % de temps, −72,2 % de tokens.
Comparaison **exploratoire historique**, pas effet causal contrôlé : CLI,
instantané modèle servi, cache, charge, prompts et instrumentation peuvent varier.
Une référence V1 sous le même nouveau dispositif serait nécessaire pour une
comparaison homogène ; sa nécessité scientifique n'est pas une autorisation de dépense.

V1/V2 historiques sur les DEUX difficultés : même score, V2 utilise environ
3,56 fois le temps et 4,49 fois les tokens. Ne pas comparer ces totaux aux seuls
113 774 tokens de la calculatrice simple V2.2.

Le dernier échange utilisateur constate que le coût est disproportionné et
demande de poursuivre sans refaire. La réponse a proposé de réduire le dispositif
avant de changer de modèle. **Cette réduction n'a pas été codée.**
110 511 tokens d'entrée indiquent un coût de lecture cumulé dominant, mais ne
mesurent pas seuls la part de chaque source : prompts, outils, contexte fourni
par le client et relectures. Éviter d'attribuer tout ce volume aux seuls transferts
entre agents ou à un prompt unique de cette taille.

Proposition à borner avec l'utilisateur : analyser les captures existantes hors
modèle, identifier les duplications, réduire les transmissions sans supprimer
les preuves utiles, tester localement avec de faux candidats et définir un
budget d'arrêt réellement applicable. Ne pas inventer un paramètre CLI de plafond.
Contexte et compaction ne sont pas des limites cumulatives de consommation.
Un contrôle après une session peut constater un dépassement, pas empêcher à
lui seul le dépassement pendant celle-ci. Modifier prompts ou modèle ouvre une
nouvelle condition expérimentale et conserve intact le protocole ancien.

## Gouvernance et protections

Lire [AGENTS.md](AGENTS.md), [format de réponse](governance/RESPONSE_FORMAT.md),
[journalisation](governance/LOGGING.md) et, pour une modification de protocole,
[plan expérimental](governance/EXPERIMENTAL_DESIGN.md).
Ce fichier ne les remplace pas et ne constitue pas une nouvelle règle générale.

- Aucun run actif à reprendre dans l'état livré. Toute future tentative doit lire son propre CHALLENGE avant modification.
- Pendant un run, le candidat écrit seulement dans sa solution ; pas dans les tests, défis, Git ou rapports.
- Ne pas fournir au candidat les solutions des autres tentatives ni cette synthèse de résultats.
- Ne pas modifier silencieusement une suite figée ou un défaut de vérificateur après les runs.
- Le contrôle scientifique a connu un problème de chargeur avec dataclass/Python 3.13 : se référer aux rapports avant toute comparaison, pas de correction rétroactive.
- Un arrêt quota n'est pas un zéro-token ni un run achevé.
- Les traces visibles et arbitrages sont publics après contrôle de confidentialité ; aucun raisonnement interne brut.
- Ne pas abaisser les protections globales ou utiliser un contournement de sandbox pour terminer coûte que coûte.

## Architecture et points d'entrée du dépôt

| Chemin | Utilité |
| --- | --- |
| [README.md](README.md) | Présentation, tableau de bord, checklist et liens |
| [docs/reading-guide.md](docs/reading-guide.md) | Guide humain, synthèse puis détails |
| [results/CONCLUSIONS.md](results/CONCLUSIONS.md) | Conclusion expérimentale lisible |
| [results/README.md](results/README.md) | Catalogue des rapports |
| [results/run-summaries/index.md](results/run-summaries/index.md) | Synthèses des V2 historiques, pas inventaire exhaustif de V2.2 |
| [docs/acceptance-tests.md](docs/acceptance-tests.md) | Liste explicite des tests et correspondance avec les sources |
| [docs/observability.md](docs/observability.md) | Instrumentation et preuves |
| [logs/history.md](logs/history.md) | Journal numéroté ; 043 publie le dernier run |
| [requirements.txt](requirements.txt) | Pas de dépendance Python externe ; outils séparés |
| [governance/V2_PROTOCOL.md](governance/V2_PROTOCOL.md) | V2 historique |
| [governance/V2_2_PROTOCOL.md](governance/V2_2_PROTOCOL.md) | Binôme, mandats et conditions |
| [governance/V2_2_SUPERVISED.md](governance/V2_2_SUPERVISED.md) | Pilote autorisé, garanties réduites explicites |
| [governance/v2-2-supervised-002.json](governance/v2-2-supervised-002.json) | Identité, autorisation et empreintes figées |
| [scripts/run_v2_2_supervised.py](scripts/run_v2_2_supervised.py) | Moteur du pilote, ne pas lancer pour « vérifier » |
| [scripts/run_v2_2_supervised_002.py](scripts/run_v2_2_supervised_002.py) | Adaptation d'identifiant 002, pas nouvelle logique |
| [scripts/run_v2_2.py](scripts/run_v2_2.py) | Autre voie automatisée, encore verrouillée pour le réel |
| [scripts/verify.py](scripts/verify.py) | Vérification indépendante, pas appel modèle |
| [scripts/summarize_runs.py](scripts/summarize_runs.py) | Cohérence des synthèses historiques |

L'ancienne qualification renforcée comprenait transport, bridge MCP, catalogue
d'outils et isolation. Son NON-GO ne signifie pas que le pilote supervisé
fonctionnel fournit toutes ses garanties. Le pilote utilise MAIN workspace-write,
REV-01 read-only, approval never, web et multi-agent désactivés dans sa configuration.
Il ne démontre pas l'impossibilité de toute lecture externe non observée.
Contexte configuré 200 000, compaction 180 000 total ; aucun plafond cumulé garanti.

## Tests : ne pas confondre les dénominateurs

Simple : 6 groupes unittest / 14 contrôles élémentaires.
Scientifique : 9 groupes / 57 contrôles. Ensemble : 15 groupes / 71 contrôles.
Addition, soustraction, multiplication et division sont bien quatre contrôles
dans un groupe, pas une seule opération. Voir la checklist liée plus haut.
Les 72 tests de maintenance concernent le dispositif, pas la calculatrice.

Vérifications réussies lors de la publication `ecdac58` :

- 72 tests de maintenance.
- Linter Markdown sans erreur.
- Liens de 188 documents éditoriaux ; 64 empreintes historiques.
- `summarize_runs.py --check` et `git diff --check`.
- Empreintes du gel et des configurations ; identité des instantanés initial/final.

Commandes locales sans appel candidat, à exécuter seulement selon la portée
de la prochaine modification, pas automatiquement après chaque lecture :

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/check_documentation.py
python3 -B scripts/summarize_runs.py --check
markdownlint '**/*.md'
git diff --check
```

Python >= 3.11 pour le lanceur (tomllib), solutions >= 3.10 selon requirements.
Node/npm servent au lint Markdown, pas à l'exécution de la calculatrice.
Les artefacts canoniques sous runs sont exclus du lint éditorial : ne pas les
reformater pour satisfaire une préférence de style.

## Environnement et livraison Git

Le terminal inspecté lors de cette reprise annonce Debian GNU/Linux 13 (trixie).
L'utilisateur parle d'Ubuntu dans le nouveau sélecteur : vérifier si c'est la
même distribution WSL ou un autre environnement avant de toucher au dépôt.
Node, npm et Python sont trouvés sous `/usr/bin`. Le linter résout actuellement
vers une installation npm Windows accessible depuis WSL ; ne pas présumer sa
disponibilité dans une autre distribution. Codex est disponible localement.
Versions présentes à vérifier si diagnostic ; ne pas supposer que les versions
historiques des essais de qualification sont celles du client actuel.

Branche livrée : `main`. Remote dédié :
`git@github-agentbench-2026:ERICRAC/AgentBench-2026.git`.
Ne pas remplacer cet alias par une configuration globale de compte GitHub :
l'utilisateur veut éviter les conflits entre plusieurs identités.
SSH a fonctionné pour la livraison précédente ; sa disponibilité dans le prochain
terminal n'est pas garantie. Voir [SSH/VS Code](docs/ssh-vscode.md).
S'il faut déverrouiller la clé, l'utilisateur saisit la passphrase localement,
jamais dans le chat, le dépôt ou les logs. Aucun besoin de lire la clé privée.
`Passphrase.sh` n'est pas suivi lors de ce contrôle ; ne pas le lire pour la reprise.

Avant toute écriture : identifier les modifications existantes et les préserver.
Après une modification : commit ciblé, corps décrivant les contrôles, push.
Si push bloqué par interaction, conserver le commit et donner la commande
minimale. Pas de reset destructif, réécriture d'historique ou suppression de caches.

## Incident client WSL : faits, hypothèses et diagnostic minimal

Signalement utilisateur, non reproduit par l'agent : un prompt fonctionnerait
par lancement VS Code ; cette conversation n'apparaîtrait pas pour association
au nouveau projet local. Deux symptômes à distinguer : envoi du second message
et visibilité/association du chat. Aucune preuve ici d'une conversation corrompue,
d'un bug confirmé OpenAI ou d'une panne générale de WSL.

La documentation officielle distingue le dossier/workspace de l'extension IDE
de la vue Projects web/desktop ; elle ne suffit pas à garantir la migration de
cette conversation particulière. Voir [Projects and chats](https://learn.chatgpt.com/docs/projects).
La [documentation WSL](https://learn.chatgpt.com/docs/windows/wsl) recommande de
confirmer la distribution et d'ouvrir VS Code depuis le dossier Linux avec
`code .`. Ces sources ne documentent pas le symptôme exact « un seul prompt ».

Hypothèses à tester séparément : mauvais dossier/distribution/compte sélectionné,
périmètre différent entre surfaces, état de thread bloqué, processus de l'extension
ou connexion distante défaillante. Ne pas conclure à partir de la seule longueur
du chat. Un problème d'interface n'explique pas à lui seul les compteurs du run.

Procédure proposée, non exécutée sur l'interface utilisateur :

1. Relever l'application exacte (extension VS Code ou application desktop), sa version, le compte/espace sélectionné et la distribution distante affichée. Garder les données de compte privées.
2. Depuis PowerShell, `wsl --list --verbose` pour identifier les distributions ; ne pas lancer `wsl --shutdown` pendant des travaux.
3. Dans le terminal du projet, lire `/etc/os-release`, `pwd`, `git rev-parse --show-toplevel`, `git log -1 --oneline`. Comparer avec le nouveau projet. Ne pas cloner ni déplacer automatiquement.
4. Créer un nouveau chat sur exactement ce dossier, envoyer deux messages minuscules successifs sans outil ni benchmark, par exemple « réponds OK », puis « réponds OK2 ».
5. Si seul l'ancien chat échoue : indice en faveur d'un état propre au thread, pas preuve de corruption. Continuer avec cette reprise sans supprimer l'ancien chat.
6. Si les deux échouent après un message : investiguer le client/extension/connexion plutôt que le benchmark. Noter si un rechargement de fenêtre suffit ; préserver le travail avant tout redémarrage.
7. Relever le message exact et les journaux disponibles du client/extension autour de l'échec ; les garder privés et retirer identifiants, secrets, chemins personnels et contenu de conversation avant partage.

Un signalement support utile décrit versions, distribution, surface, reproduction
en deux messages, résultat attendu/observé et effet du redémarrage. N'ajouter
aucune clé, cookie, jeton, passphrase ou export complet non nettoyé.
Pas d'installation ni de réinitialisation de profil justifiée sans diagnostic.

## Limites de la reprise et prochaine décision

Cette instruction et le dépôt permettent de reprendre le travail documenté.
Ils ne transfèrent pas les autorisations de session, processus en mémoire,
soldes d'abonnement, pièces jointes privées, réglages du client ni mémoire cachée.
Un nouveau chat a un contexte neuf et doit vérifier ses propres accès.
Ne pas demander de recopier toute la conversation ni d'ingérer toutes les traces
par défaut : cela recréerait une partie du coût que l'utilisateur veut réduire.

Ordre conseillé :

- Confirmer que le nouveau chat reçoit bien deux messages et pointe sur le bon dépôt.
- Restituer en quelques lignes : dernier run terminé, coût connu, quota non mesuré, aucune relance.
- Demander seulement l'arbitrage manquant : audit borné d'allègement, ou diagnostic client si toujours bloqué.
- Pour l'allègement, commencer sur les artefacts existants, sans consultant ni appel candidat ; proposer une condition expérimentale nouvelle avant gel.
- Ne lancer la scientifique, un nouveau solo témoin ou une variante qu'après accord explicite sur périmètre et budget vérifiable.

Critère de réussite de la reprise : l'utilisateur n'a pas à réexpliquer le projet,
aucune preuve ancienne n'est modifiée, aucun run n'est refait pour rien et la
prochaine action a un résultat concret et une portée bornée.
