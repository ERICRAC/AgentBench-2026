# Qualification du CLI V2.2

**Français** · [English (UK)](v2-2-cli-qualification.en.md) · [Español](v2-2-cli-qualification.es.md) · [Português](v2-2-cli-qualification.pt.md)

**Conclusion : changer d’installation ne lève pas le blocage.**

Trois exécutions de la même sonde sans modèle : CLI autonome 0.153.4, paquet npm officiel 0.153.4 installé séparément, binaire de l’extension 0.154.0-alpha.6.1. Chacune obtient 7/8 contrôles ; le catalogue reste hors liste autorisée. Les deux binaires 0.153.4 ont exactement la même empreinte SHA-256. Aucun PATH, compte ou fichier de l’extension n’a été modifié.

Le catalogue embarqué associe gpt-6-astra et gpt-5.6-sol à tool_mode=code_mode_only et multi_agent_version=v2. C’est un indice structurel compatible avec les outils observés, pas une preuve causale de l’implémentation interne. Nous ne modifions pas ces métadonnées pour forcer un résultat. Passer à Sol élevé n’est pas une correction démontrée ; Astra moyen reste actif, Astra élevé historique uniquement.

57 tests de maintenance réussis : 52 précédents et 5 nouveaux contrôles de lecture du catalogue (ancien format, additional_tools imbriqué, deux formats simultanés, catalogue vide/dupliqué, outil inconnu). Le parseur refuse un catalogue vide au lieu de le confondre avec une restriction réussie.

Le lanceur de préflight accepte désormais --cli pour comparer un chemin explicite, et enregistre version, empreinte du binaire et paramètres publics du catalogue embarqué. Le fournisseur HTTP reste factice et local, avec HOME/CODEX_HOME vierges, sans authentification ni inférence. Les erreurs HTTP sont intentionnelles ; aucun compteur n’est un coût modèle.

Suite utile : tester le routage effectif et le refus des capacités interdites au moyen d’appels factices non mutatifs. Un catalogue annoncé ne prouve pas que tous ses outils sont exécutables. Tant que cette frontière n’est pas démontrée, aucun gel, aucune sonde authentifiée et aucun benchmark. Réinstaller encore la même version n’apporterait pas une nouvelle preuve.

Installation de test conservée hors dépôt dans un répertoire temporaire dédié ; aucun helper ou paquet publié. OpenAI Docs a guidé le choix du paquet officiel ; le résultat repose sur les sondes locales.

[JSON](v2-2-cli-qualification.json) · [MCP](v2-2-bridge.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/codex/cli) · [README](../README.md)
