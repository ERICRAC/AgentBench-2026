# PV — astra-core-v1-002

## Acteurs et mandat

Le commanditaire fixe le protocole. L'orchestrateur expérimental lance cette
session Codex distincte, observe ses sorties et publie après sa clôture.
Le candidat est l'unique écrivain ; il n'utilise aucun consultant ni sous-agent.
Le vérificateur officiel est ensuite relancé par l'orchestrateur.

Modèle : `gpt-6-astra`, effort `high`, CLI `0.153.4`.
Fenêtre déclarée : 200 000 tokens ; compaction : 180 000, portée `total`.
La configuration client est enregistrée, sans prétendre mesurer une limite
interne du serveur. L'isolation repose sur une session neuve et des consignes
explicites ; ce n'est pas une interdiction système de lire tout autre dossier.

Le prompt exact est [conservé](../../prompts/codex-single.md) ; les instructions du
lanceur sont [figées](../../governance/astra-v1.toml). Empreintes et identifiant
de thread figurent dans [run.json](run.json).

## Messages visibles du candidat

Les messages suivants sont reproduits dans leur ordre. Seul le préfixe local
du dépôt est remplacé par `<repo>`. Le raisonnement interne est exclu.

### Message 1

````text
Je vais lire le défi, implémenter et documenter la solution dans `solution/`, puis lancer le vérificateur indiqué. Je travaillerai seul, sans sous-agent.
````

### Message 7

````text
Le contrat demande quatre opérations et une boucle interactive qui continue après une erreur de saisie ou une division par zéro. Je vais séparer le calcul de la lecture des expressions et prévoir une sortie propre sur `quit`, `exit` et la fin de l’entrée.
````

### Message 10

````text
Le vérificateur indépendant a réussi les 6 tests, notamment les opérations, les exceptions attendues et la reprise de la CLI après une erreur. Je vais consigner ce résultat et le procès-verbal synthétique dans `solution/`.
````

### Message 12

````text
Solution complète dans `solution/` :

- `calculator.py` : quatre opérations, CLI interactive et gestion des erreurs.
- `README.md` : lancement, exemples et interface Python.
- `PV.md` : trace synthétique de la tentative.

Vérificateur exécuté depuis la tentative active : **6 tests réussis, aucun échec, code de sortie 0**.

Travail réalisé seul, sans sous-agent ni opération Git. Aucune modification hors de `solution/`.
````

## Synthèse des contrôles et décisions

- Premier passage officiel : 6/6. Dernier passage candidat : 6/6.
- Verdict relancé séparément par l'orchestrateur : 6/6, code de sortie 0.
- Aucune correction fonctionnelle. Une recherche initiale du chemin du vérificateur a échoué (code 2) et la recherche de fichiers dans la solution vierge a retourné 1 ; ces événements sont de la navigation, pas des échecs d'acceptation.
- Aucune aide fonctionnelle humaine, aucune délégation ni opération Git observée dans les commandes du candidat.
- Durée murale de la session CLI : 100.175 s.
- Entrée : 117769 ; cache inclus dans l'entrée : 96896 ; sortie : 2709 ; raisonnement inclus dans la sortie : 195 tokens.
- Total entrée + sortie : 120478 tokens. Le cache et le raisonnement ne sont pas ajoutés une seconde fois.

## Analyse et limites

Le contrat Core est satisfait sans correction fonctionnelle. Le score maximal crée un effet plafond : V2 devra être jugée aussi sur les coûts et les erreurs hors suite.

Les singularités entre échantillons et les arrondis restent des limites du défi
scientifique. Aucun test comparatif statistique ni contrôle visuel navigateur
n'est revendiqué. Les anciennes campagnes diffèrent aussi par CLI et consignes.
La [trace structurée](trace.json) conserve l'ordre des messages, commandes et
écritures ; les sorties non nécessaires sont omises pour la confidentialité.
