# V2.2 — routage réel après mise à jour

**Français** · [English (UK)](v2-2-dispatch.en.md) · [Español](v2-2-dispatch.es.md) · [Português](v2-2-dispatch.pt.md)

**V2.2 supervisée : essai simple interrompu par quota après 48,641 s.** Deux livrables conservés ; diagnostic après arrêt 6/6 groupes, 14 contrôles. Relecteur non lancé, tokens non enregistrés : aucune conclusion sur l'efficacité du binôme. [Rapport / Report / Informe / Relatório](v2-2-supervised-core.md).

## Verdict final de qualification — non prêt au gel

**La qualification est close avec un verdict NON-GO pour le dispositif automatisé actuel. Aucun benchmark n'a été lancé.** Ce n'est pas un échec de la calculatrice ou d'Astra : le raccordement du lanceur et les garanties d'isolation ne sont pas complets. Nous arrêtons la succession de petites qualifications ; la prochaine décision porte sur le dispositif à retenir.

| Exigence | Verdict et preuve |
| --- | --- |
| Développeur → relecteur → développeur | Deux simulations rejouées, trois sessions chacune ; aucun score candidat |
| Capture locale des sorties | Réussie : stdin, stdout, stderr, sortie non nulle, 2 Mo sans troncature et octets non UTF-8 conservés |
| Interruption du transport local | Réussie : délai dépassé et SIGINT réel ; traces partielles conservées, enfant arrêté, état interrupted |
| Isolation des outils | Partielle : preuves antérieures Bubblewrap et huit refus de patches conservées ; pas de nouvelle certification de toute la chaîne |
| Interdiction de délégation | Non démontrée techniquement ; aucun spawn_agent tenté, liste native précédemment appelable |
| Lanceur réel complet | Non prêt : run_relay refuse simulation=False ; pont MCP testé séparément, pas d'adaptateur réel raccordé |
| Capture/arrêt CLI → MCP → processus et accès modèle | Non qualifiés de bout en bout ; aucun appel authentifié, aucune garantie de quota |

**68 tests de maintenance réussis**, et non 68 tests de calculatrice. Deux nouveaux tests couvrent la capture binaire exacte et SIGINT avec contrôle de l'arrêt de l'enfant. Une correction remplace l'option `-P` dans la commande préparée pour `codex exec` par `-c default_permissions=...` ; `-P` reste réservé au chemin sandbox existant. Le parseur accepte désormais la commande avec `--help` (code zéro) : cela ne prouve ni le chargement du profil ni son confinement effectif.

OpenAI Docs a guidé cette correction de sélection du profil ; aucune valeur de configuration supposée ne remplace une preuve d'exécution. [Permissions officielles](https://learn.chatgpt.com/docs/permissions). [Bilan structuré](v2-2-qualification.json) · [Tests du transport](../tests/test_v2_2_transport.py) · [Lanceur verrouillé](../scripts/run_v2_2.py).

### Simplification proposée — à approuver, non appliquée

Un **pilote supervisé** en trois sessions CLI fraîches, Astra moyen : développeur, revue sur instantané, corrections. Un dossier neuf hors dépôt avec seulement le défi et les livrables ; collecte des messages visibles, métriques disponibles, différences de fichiers et verdict indépendant. Pas de pont MCP personnalisé ni de framework supplémentaire pour ce pilote.

**Compromis explicite :** dossiers séparés et consignes ne constituent pas un confinement technique complet. La non-délégation et les accès seraient contrôlés par consignes et audit des traces disponibles, sans prétendre prouver l'absence de tout accès non observé. Tout écart observé invaliderait le run ; aucune protection de secret ne serait supprimée automatiquement. Les droits exacts devront être écrits avant lancement.

Ce pilote serait étiqueté exploratoire, avec ses différences de dispositif publiées ; aucune comparaison strictement homogène avec l'historique ne serait revendiquée sans référence V1 sous les mêmes conditions. Autre choix : conserver l'exigence de confinement fort et accepter un chantier d'intégration dédié, distinct du benchmark.

**Arbitrage demandé : accepter ce pilote supervisé plutôt que poursuivre le dispositif automatique renforcé ?** Ce choix n'autorise pas encore un lancement : périmètre révisé et gel explicite d'abord. Gouvernance générale, défis et résultats historiques restent inchangés.

## Preuves antérieures conservées

## Suite — écritures natives contrôlées

**Huit sondes supplémentaires : quatre cibles × deux binaires, huit refus explicites, tous les témoins intacts.** `apply_patch` est disponible mais ne permet pas ces écritures avec `sandbox_mode="read-only"` et `approval_policy="never"`. Cela lève ce doute précis, pas tous les prérequis V2.2.

| Cible synthétique de la modification | CLI 0.153.4 | Extension 0.154.0-alpha.6.2 |
| --- | --- | --- |
| Fichier dans solution/ | Refus, intact | Refus, intact |
| Faux CHALLENGE.md parent | Refus, intact | Refus, intact |
| Fichier hors workspace | Refus, intact | Refus, intact |
| Lien symbolique vers ce fichier externe | Refus, cible et lien intacts | Refus, cible et lien intacts |

Chaque sonde crée un dossier temporaire neuf, trois fichiers témoins et un lien. Le fournisseur local renvoie une seule instruction fixe de modification. Après l'appel, le vérificateur compare les octets des trois fichiers et la destination du lien ; le dossier est ensuite supprimé. Le fichier « externe » reste dans notre propre arborescence temporaire : aucune donnée utilisateur n'est ciblée. Aucun modèle candidat, compte, secret ou sous-agent n'est utilisé.

**Vérifications : 66 tests de maintenance réussis**, dont trois nouveaux tests : cibles fixes et relatives ; interdiction d'étendre l'approbation MCP aux patches ; reconnaissance stricte du refus observé. Les huit sondes CLI sont distinctes de ces tests unitaires. [Preuves JSON des huit sondes](v2-2-native-patch.json) · [Tests sources](../tests/test_v2_2_dispatch.py).

Le statut global reste `blocked_tool_catalog`, non « préflight validé ». Les anciens résultats ci-dessous et leur JSON sont conservés comme étape précédente. Le refus natif est testé avec un pont REV-01 ; il ne valide pas le raccordement final MAIN, les lectures natives, les interruptions, la capture complète ni l'interdiction de créer des agents. Aucun appel à `spawn_agent` n'a été tenté.

OpenAI Docs a guidé le maintien de deux contrôles distincts : bac à sable de lecture seule et politique sans approbation. Le constat d'intégrité provient des sondes locales, pas de la documentation. [Documentation officielle](https://learn.chatgpt.com/docs/agent-approvals-security).

Reproduction sans modèle, une cible à la fois ; autres fixtures : `patch_contract`, `patch_outside`, `patch_symlink`. Utiliser `--cli CHEMIN_DU_BINAIRE` pour sélectionner une autre installation sans modifier PATH. Le code de sortie non nul reste attendu : arrêt volontaire du fournisseur et catalogue non conforme.

```bash
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture patch_solution --enable-code-mode-host-for-probe
```

**Suite :** qualifier le verrou de délégation sans lancer de candidat, puis les interruptions et la capture. Astra moyen conservé ; aucun gel ni lancement automatique.

## Étape précédente — routage MCP

La mise à jour de l’extension est visible : 0.154.0-alpha.6.2, contre 0.154.0-alpha.6.1 auparavant. Le CLI du terminal reste 0.153.4 avec la même empreinte. Aucun réglage global, PATH, compte ou fichier de VS Code n’a été modifié par cette intervention.

**Le trajet CLI → exécuteur → MCP → Bubblewrap → réponse est démontré pour un printf fixe. Il fonctionne sur les deux versions testées après activation de l’hôte Code Mode et approbation explicite du seul outil MCP de la sonde. Le succès n’est donc pas attribuable à la seule mise à jour.**

63 tests de maintenance réussis, dont 6 nouveaux tests de fixtures/réponses. Huit sondes diagnostiques distinctes ci-dessous ; ce ne sont ni huit benchmarks ni huit validations globales.

| Sonde | Version | Observation |
| --- | --- | --- |
| Hôte désactivé | 0.153.4 | Exécution refusée : code-mode host is disabled |
| Inventaire réel | 0.153.4 | Six outils accessibles dans l’exécuteur |
| Pont autorisé | 0.153.4 | printf exécuté, sortie exacte, code zéro |
| Inventaire après mise à jour | 0.154.0-alpha.6.2 | Même inventaire de six outils |
| Pont sans approbation | 0.154.0-alpha.6.2 | Refus d’approbation ; aucun tools/call MCP |
| Pont autorisé après mise à jour | 0.154.0-alpha.6.2 | printf exécuté et tools/call MCP observé |
| Terminal natif | 0.154.0-alpha.6.2 | tools.exec_command absent ; aucune commande exécutée |
| Liste des agents | 0.154.0-alpha.6.2 | Lecture exécutée : un orchestrateur /root, aucun sous-agent |

## Ce que cela corrige dans notre analyse

Un outil annoncé peut être refusé à l’exécution. Notre ancien contrôle de catalogue reste en échec, mais ne suffisait pas à conclure que toutes les désactivations étaient inopérantes. Les textes et mesures historiques restent conservés ; cette précision est ajoutée, pas appliquée rétroactivement aux runs.

L’inventaire effectif contient apply_patch, clock__curr_time, list_mcp_resource_templates, list_mcp_resources, mcp__agentbench__confined_command et read_mcp_resource. La fonction de lecture collaboration.list_agents est aussi réellement appelable hors de cet inventaire. Nous n’avons pas tenté spawn_agent, ni testé une écriture via apply_patch.

## Limites et suite

Le pont n’est validé ici que pour la commande constante de la sonde. Les permissions natives, les écritures MAIN/REV via tous les chemins, l’interdiction effective de créer des agents, les interruptions et la capture complète restent à qualifier avant gel. La présence d’apply_patch ne prouve ni fuite ni écriture réussie ; la lecture de liste ne prouve pas qu’un sous-agent pourrait être créé. Aucun changement de modèle nécessaire : Astra moyen actif, Astra élevé historique uniquement.

OpenAI Docs a guidé les événements de streaming et l’approbation MCP par outil. L’option d’approbation de la sonde est refusée pour toute autre fixture ; elle ne modifie pas la politique globale et n’autorise pas de benchmark. Toutes les réponses simulant le modèle sont fixes, servies en loopback avec un HOME/CODEX_HOME vierge ; aucun service de modèle ou secret réel n’est utilisé.

Tests ajoutés : correspondance des événements SSE ; rejet de fixture arbitraire et d’approbation élargie ; capture limitée au call_id connu ; sorties absentes/dupliquées non validées ; écho exact exigé ; distinction refus/inventaire/liste des agents.

Les sondes conservent un code de retour non nul : le catalogue global reste non conforme et le fournisseur factice arrête volontairement la conversation après la réponse d’outil. Cela n’annule pas l’écho confirmé, mais n’est pas une validation de lancement.

[Tests](../tests/test_v2_2_dispatch.py) · [JSON](v2-2-dispatch.json) · [CLI](v2-2-cli-qualification.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/extend/mcp)

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture inventory
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture bridge_echo --enable-code-mode-host-for-probe --approve-bridge-echo-for-probe
```

[README](../README.md) · [V2.2](../governance/V2_2_PROTOCOL.md)
