# V2.2 — routage réel après mise à jour

**Français** · [English (UK)](v2-2-dispatch.en.md) · [Español](v2-2-dispatch.es.md) · [Português](v2-2-dispatch.pt.md)

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
