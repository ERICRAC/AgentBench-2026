# V2.2 — pilote supervisé figé

**Français** · [English (UK)](V2_2_SUPERVISED.en.md) · [Español](V2_2_SUPERVISED.es.md) · [Português](V2_2_SUPERVISED.pt.md)

L'utilisateur autorise l'essai **calculatrice simple uniquement**, Astra moyen, identifiant astra-medium-core-v2-2-supervised-001. Scientifique et répétitions exigent un nouvel accord. [Manifeste figé et empreintes](v2-2-supervised.json).

Deux métiers, trois sessions fraîches : MAIN implémente, REV-01 relit, MAIN arbitre et corrige. Les [mandats V2.2](V2_2_PROTOCOL.md) restent les textes de base ; le lanceur ajoute seulement le contexte de dossier et la commande locale du vérificateur. Ni aide humaine au code ni autre consultant. Première vérification officielle en phase finale ; diagnostic de l'instantané initial seulement après clôture.

Dossier jetable neuf hors dépôt, copies inchangées du défi, du vérificateur et des tests, solution vide. CLI natif : MAIN workspace-write, REV-01 read-only, approval never, web désactivé. Aucun contournement du sandbox. Délégation interdite par mandat et désactivée dans la configuration, **sans garantie technique absolue**. Un audit des fichiers et des événements observables ne prouve pas l'absence de toute lecture extérieure. Secrets non fournis aux candidats, anciennes solutions non consultées ; aucune baisse globale des protections.

Contexte 200000, compaction 180000 total ; limites finales 600/1200/1200 mots. Aucun nouveau plafond cumulé, aucune garantie de quota. Pas de relance après échec, quota, capture non interprétable ou violation observée. Traces brutes privées conservées ; seules données auditées, textes visibles et métriques réellement exposées seront publiés. Raisonnement privé exclu. Capture locale des sorties testée ; complétude des événements CLI évaluée au passage, arrêt si le parseur les refuse.

Le dispositif MCP renforcé reste NON-GO : ce pilote est **une campagne exploratoire distincte**, non une validation rétroactive du confinement ni une comparaison causale avec V1/V2 historiques. Une comparaison homogène demandera une référence V1 dans les mêmes conditions.

72 tests de maintenance réussis avant lancement : quatre nouveaux couvrent la séquence, l'absence de reprise, l'arrêt après échec, l'autorisation et les arguments TOML. [Lanceur](../scripts/run_v2_2_supervised.py) · [Tests](../tests/test_v2_2_supervised.py).

OpenAI Docs a guidé le mode CLI non interactif et la capture JSONL. Le login local signale ChatGPT ; disponibilité réelle d'Astra et consommation seront constatées, pas présumées. [Documentation officielle](https://learn.chatgpt.com/docs/non-interactive-mode).

[README](../README.md) · [Qualification précédente](../results/v2-2-dispatch.md)
