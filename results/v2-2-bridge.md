# V2.2 — pont d’outils et blocage du catalogue

**Français** · [English (UK)](v2-2-bridge.en.md) · [Español](v2-2-bridge.es.md) · [Português](v2-2-bridge.pt.md)

## Décision et résultat

**Astra élevé devient historique uniquement : aucun nouveau run prévu, tous les résultats conservés.** Astra moyen reste actif ; Sol élevé reste une possibilité de comparaison à autoriser séparément. [Décision enregistrée](../governance/v2-2-draft/model-policy.json).

Le pont d’outils confiné fonctionne. **Le raccordement au CLI reste bloqué par son catalogue effectif**, pas par un manque de crédits. Aucun appel modèle, aucune authentification réelle utilisée, aucun gel ou lancement de benchmark.

## Ce qui a été construit et vérifié

Le [serveur MCP](../scripts/v2_2_tool_bridge.py) reçoit seulement une commande. L’orchestrateur fixe le métier, le workspace et la capture privée ; le candidat ne peut changer ni rôle, ni répertoire, ni permissions, ni environnement. La commande passe par Bubblewrap : MAIN écrit dans solution/, REV-01 reste en lecture seule. stdin vide et environnement nettoyé dans le processus confiné ; les identifiants Codex ne lui sont pas transmis.

**52 tests de maintenance réussis**, dont [6 nouveaux tests](../tests/test_v2_2_tool_bridge.py) : initialisation et outil unique ; refus de surcharge rôle/chemins/permissions ; commandes invalides ; séparation et non-réutilisation des captures ; notifications sans exécution ; protocole et méthodes inconnus.

Le [préflight réel sans modèle](../scripts/preflight_v2_2_bridge.py) effectue **7 contrôles réussis sur 8** :

- [x] MAIN : initialisation/listage ; stdout/stderr complets ; écriture permise.
- [x] REV-01 : initialisation/listage ; stdout/stderr complets ; écriture refusée.
- [x] CLI : requête reçue par le serveur HTTP local factice.
- [ ] Catalogue candidat limité à l’outil confiné.

[Observations et empreintes](v2-2-bridge.json) · [Isolation de l’étape précédente](v2-2-transport.md)

## Blocage observé

Le vrai CLI utilise un HOME et un CODEX_HOME temporaires vierges, sans jeton hérité. Son fournisseur pointe exclusivement vers un serveur loopback qui refuse l’inférence avec une erreur HTTP contrôlée. Aucun en-tête, prompt ou identifiant de session n’est publié.

Codex initialise le MCP en version 2025-06-18 et appelle tools/list. Son catalogue est transmis dans input/additional_tools, pas dans le champ tools classique : la première inspection donnant une liste vide était donc incomplète, pas une preuve d’absence d’outils.

Le catalogue effectif contient notamment functions.exec et collaboration.spawn_agent, malgré features.shell_tool=false et features.multi_agent=false. La présence de ces entrées ne prouve pas que chaque opération réussirait ; **elle ne permet pas de certifier le passage exclusif par le pont confiné**. Le MCP n’est pas annoncé comme outil direct unique ; sa disponibilité éventuelle via l’exécuteur reste à qualifier.

La sonde sort volontairement en échec tant que ce critère ne passe pas. La sortie non nulle du CLI est attendue, puisque le fournisseur factice refuse l’inférence ; ce n’est pas un test de quota ou d’accès au compte.

## Limites et suite

OpenAI Docs a guidé la configuration MCP et la désactivation des outils, mais les options acceptées ne suffisent pas : nous contrôlons leur effet observé. [Référence de configuration](https://learn.chatgpt.com/docs/config-file/config-reference).

Ce prototype MCP change l’interface d’outillage par rapport aux runs historiques : il doit entrer dans la nouvelle campagne, jamais être appliqué rétroactivement. La capture brute reste privée ; sortie binaire invalide ou erreur d’infrastructure arrête le pont. Le timeout MCP du client, ses troncatures, les appels via exécuteur et la fermeture de toute l’arborescence de processus restent à qualifier avant gel. Aucun timeout candidat nouveau n’est approuvé par ces sondes.

Prochaine décision technique : qualifier une configuration réellement restrictive ou tester un CLI séparé, sans remplacer celui de VS Code. Ensuite seulement, demander une sonde authentifiée Astra moyen. Aucun secret à ajouter au dépôt.

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py
```

La seconde commande nécessite une exécution autorisée des namespaces Linux et doit actuellement retourner un échec de catalogue. Les fichiers témoins sont supprimés après la sonde ; aucune solution historique n’est utilisée.

[Protocole](../governance/V2_2_PROTOCOL.md) · [Conclusions](CONCLUSIONS.md) · [README](../README.md)
