# PV — astra-scientific-v1-002

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

Le prompt exact est [conservé](../../prompts/scientific-single.md) ; les instructions du
lanceur sont [figées](../../governance/astra-v1.toml). Empreintes et identifiant
de thread figurent dans [run.json](run.json).

## Messages visibles du candidat

Les messages suivants sont reproduits dans leur ordre. Seul le préfixe local
du dépôt est remplacé par `<repo>`. Le raisonnement interne est exclu.

### Message 1

````text
Je vais lire le défi de la tentative active, implémenter la solution avec la bibliothèque standard Python, puis exécuter le vérificateur demandé. Je travaillerai seul et limiterai les écritures au dossier `solution/`.
````

### Message 5

````text
Le contrat fixe notamment la priorité de la puissance, la coupure des courbes aux points indéfinis et la sécurité du SVG. Je vais utiliser un analyseur dédié à la grammaire autorisée, réutiliser l’expression analysée pendant l’échantillonnage et sérialiser le SVG avec les outils XML de Python.
````

### Message 7

````text
Le moteur, l’échantillonnage, l’export SVG et la CLI sont implémentés et documentés. Les points hors domaine coupent la courbe ; la documentation précise aussi qu’une singularité située entre deux échantillons peut échapper au tracé. Je vais maintenant lancer les contrôles.
````

### Message 11

````text
Le vérificateur indépendant réussit ses 9 tests, notamment ceux de sécurité, de syntaxe, de tracé et de récupération de la CLI après erreur. Je complète la validation sur les bornes flottantes extrêmes, les limites de complexité et les caractères interdits en XML, puis je consignerai les résultats dans le procès-verbal.
````

### Message 13

````text
Le contrôle complémentaire a trouvé un défaut d’arrondi pour deux bornes voisines du plus grand flottant : l’interpolation peut sortir légèrement de l’intervalle. Je vais utiliser la différence des bornes lorsqu’elles ont le même signe, puis relancer ce contrôle et le vérificateur indépendant.
````

### Message 19

````text
**Traitement réalisé.** Calculatrice complète dans [scientific_calculator.py](<repo>/runs/astra-scientific-v1-002/solution/scientific_calculator.py) : analyseur sûr, fonctions scientifiques, échantillonnage, SVG et CLI avec historique. Bibliothèque standard uniquement, aucun sous-agent.

**Vérifications.** Les 9 tests du vérificateur indépendant et les 4 contrôles complémentaires réussissent.

**Correction.** Les contrôles complémentaires ont révélé un défaut d’interpolation près du plus grand flottant. Il est corrigé et couvert par un test.

**Limites.** Arrondis flottants et singularités entre échantillons documentés. Aucun contrôle restant en échec ; rendu visuel en navigateur non vérifié.

**Documentation et livraison.** Utilisation dans `README.md`, décisions et contrôles dans `PV.md`. Écritures limitées à `solution/`. Aucune opération Git ; publication réservée à l’orchestrateur expérimental.
````

## Synthèse des contrôles et décisions

- Premier passage officiel : 9/9. Dernier passage candidat : 9/9.
- Verdict relancé séparément par l'orchestrateur : 9/9, code de sortie 0.
- Quatre tests complémentaires du candidat : 4/4, également relancés par l'orchestrateur. Un premier contrôle avait échoué sur l'interpolation de bornes voisines du plus grand flottant. Le candidat a corrigé le calcul puis ajouté la régression symétrique négative.
- Aucune aide fonctionnelle humaine, aucune délégation ni opération Git observée dans les commandes du candidat.
- Durée murale de la session CLI : 399.478 s.
- Entrée : 208078 ; cache inclus dans l'entrée : 167808 ; sortie : 12432 ; raisonnement inclus dans la sortie : 1429 tokens.
- Total entrée + sortie : 220510 tokens. Le cache et le raisonnement ne sont pas ajoutés une seconde fois.

## Analyse et limites

La réussite immédiate des neuf tests n'empêchait pas un défaut numérique hors de leur couverture. La correction spontanée est un résultat utile sur l'auto-contrôle du candidat solo ; elle ne démontre aucun bénéfice multi-agent. Certaines sorties d'outils sont vides dans l'export JSON malgré un code 0 : le premier 9/9 est corroboré par le message visible du candidat, puis par la vérification finale séparée.

Les singularités entre échantillons et les arrondis restent des limites du défi
scientifique. Aucun test comparatif statistique ni contrôle visuel navigateur
n'est revendiqué. Les anciennes campagnes diffèrent aussi par CLI et consignes.
La [trace structurée](trace.json) conserve l'ordre des messages, commandes et
écritures ; les sorties non nécessaires sont omises pour la confidentialité.
