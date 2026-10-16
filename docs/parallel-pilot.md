# Prochain pilote — calculatrice modulaire et développement parallèle

[Français](parallel-pilot.md) · [English (UK)](parallel-pilot.en.md) · [Español](parallel-pilot.es.md) · [Português](parallel-pilot.pt.md)

## Décision de préparation

**Préparation hors modèle, protocole proposé et non gelé. Aucun nouveau candidat lancé.**
La prochaine comparaison vise le **délai à qualité comparable** ; les tokens sont une contrainte et un résultat séparés. Un gain de temps avec plus de tokens sera présenté comme un compromis.
[Expertise qui motive ce choix](../results/intermediate-review.md).

Le nom proposé est **V2.1 légère** : deux développeurs, dont un intègre ensuite. Cette variante remplace la proposition à quatre rôles pour le prochain pilote seulement. V2 historique et ses preuves restent inchangées. Le protocole actuel à écrivain unique ne suffit pas à autoriser cette nouvelle organisation : les droits ci-dessous devront être figés pour cette campagne.

## Périmètre concret proposé

Créer une nouvelle calculatrice scientifique **modulaire avec traitement par lots**, bibliothèque standard Python, sans dépendance d'exécution, sans `eval` ni `exec`.
Le lot ajoute une interaction réelle : une expression invalide doit produire une erreur locale tout en permettant aux suivantes de réussir.

| Fichier livré | Responsabilité | Propriétaire pendant le parallèle |
| --- | --- | --- |
| `engine.py` | Expressions sûres et échantillonnage avec discontinuités | DEV-A, développeur moteur |
| `presentation.py` | SVG, lot JSON, traduction des erreurs en résultats | DEV-B, développeur présentation |
| `cli.py` | Commandes, lecture des entrées, sorties et erreurs | DEV-B |
| `README.md` | Usage, contrats, limites et exemples | DEV-B |
| Ensemble des livrables | Intégration, corrections et vérification finale | DEV-A, session INT |

Le solo reçoit les mêmes interfaces, le même découpage, le même exemple de lot et les mêmes commandes de test. Il peut travailler dans l'ordre de son choix. Aucun squelette fonctionnel n'est réservé à l'équipe.

Interfaces à fixer dans la nouvelle spécification :

- `engine.evaluate(expression, variables=None) -> float` ; syntaxe scientifique et règles de priorité explicitement reprises dans le nouveau contrat, sans importer une ancienne solution.
- `engine.sample_curve(expression, x_min, x_max, samples=201)` ; liste de couples, valeur `None` aux points non définis.
- `presentation.write_svg(points, output_path, title="")` ; XML valide, texte échappé, segments disjoints.
- `presentation.run_batch(jobs)` ; liste ordonnée de résultats : `{"ok": true, "value": nombre}` ou `{"ok": false, "error": texte}`. Chaque job porte `expression` et éventuellement `variables`.
- `python cli.py batch INPUT.json OUTPUT.json` ; entrées structurellement invalides : sortie non nulle et message sans traceback. Erreur d'une expression : conservée dans le résultat, autres jobs exécutés.
- `python cli.py plot EXPRESSION OUTPUT.svg --min A --max B --samples N` ; échantillonnage puis export dans un fichier choisi par l'utilisateur.

Avant gel : préciser types admis, nombres non finis, bornes numériques, limites de taille, codes de sortie, écrasement de fichier et erreurs de domaine. Ces points ne doivent pas être laissés à l'imagination du vérificateur.

## Liste des contrôles à transformer en suite indépendante

Cases non cochées : **exigences prévues, pas tests exécutés ni score annoncé**.

- [ ] M01 : import standard, livrables et interdiction des mécanismes dangereux.
- [ ] M02 : quatre opérations, priorités, parenthèses, puissance et signes.
- [ ] M03 : fonctions, constantes, variable et noms interdits.
- [ ] M04 : syntaxe invalide, domaines et résultats non finis.
- [ ] M05 : bornes, nombre de points et discontinuités d'échantillonnage.
- [ ] M06 : SVG analysable, échappement de titre et absence de pont sur une discontinuité.
- [ ] M07 : lot mixte réussi/échoué, ordre préservé et poursuite après erreur.
- [ ] M08 : structure JSON invalide et messages d'erreur de la CLI.
- [ ] M09 : intégration réelle moteur → lot et moteur → courbe → SVG.
- [ ] M10 : API documentée, exemples exécutables et responsabilités des modules.

Publier les cas élémentaires et leur nombre après écriture de la suite. Calibrer le chargeur avec des constructions Python standard et des variantes équivalentes ; injecter des défauts connus pour vérifier que les contrôles les détectent. Réserver une évaluation indépendante de robustesse, sans prétendre que les tests déjà publics sont cachés. Aucun nouveau score ne remplacera les anciens 6/9 groupes.

## Organisation et observation

V1 : une session neuve, un candidat, tout le périmètre. V2.1 légère : deux sessions simultanées en répertoires isolés ; DEV-A et DEV-B reçoivent le contrat commun et leur mission. Aucun accès aux fichiers vivants de l'autre. L'orchestrateur assemble les instantanés terminés, sans retouche, puis démarre INT avec les deux livraisons et leurs notes. INT peut corriger tous les fichiers ; toute correction doit être attribuée.

Une barrière impose la fin des deux développeurs avant l'intégration. En cas de fichier hors périmètre, d'absence de livrable ou d'échec de transport, conserver les preuves et arrêter ; aucune relance automatique. L'isolation doit être validée avec de faux candidats avant lancement réel.

Conserver les mandats, réponses visibles et messages d'intégration ; numéroter chaque avis et relier clause, preuve, décision, changement et test. Mesurer défauts corrigés, régressions, faux positifs et travail dupliqué. Une documentation meilleure n'est un gain mesuré que si la grille a été fixée avant le run.

Mesurer le temps mural de l'organisation, le chevauchement réel des développeurs, la somme des temps-agents, l'intégration et la vérification séparément. Publier tokens d'entrée, cache et sortie par session. Conserver aussi coûts des interruptions et temps de préparation hors candidat.

## Budget proposé et jalon

Astra moyen reste la condition demandée pour les deux organisations. Proposition à valider au gel : **un pilote solo puis un pilote parallèle**, seuil intersession de **150 000 tokens par organisation**, donc **300 000 tokens nominaux pour la paire**, sans retry. Les deux sessions parallèles peuvent ensemble dépasser le seuil avant le prochain contrôle ; ce n'est ni un plafond dur ni une garantie de quota Plus.

Le solo peut dépasser son seuil dans son unique session. Après le solo, publier qualité et coûts ; ne pas lancer automatiquement l'équipe si le budget disponible ou la mesure d'usage ne permet plus d'appliquer l'accord. Pour une répétition, équilibrer l'ordre des organisations. Une seule paire reste une exploration.

**Rappel : expertise du protocole final par le modèle le plus puissant disponible avant gel et lancement.** La sélection et les capacités effectives ne sont pas certifiées ici. Préparation autorisée ; budget et périmètre du lancement restent à approuver sur les artefacts prêts.

## Navigation et diagnostic des liens

Les quatre liens signalés existent dans le dépôt. Les adresses contenant le domaine interne `vscode-cdn.net` proviennent du rendu de l'éditeur ; elles ne sont pas enregistrées dans les Markdown. Leur fonctionnement dans le client WSL ne peut pas être vérifié ici. Dans VS Code, ouvrir un chemin avec **Ctrl+P**, depuis la racine du projet :

```text
scripts/audit_intermediate.py
results/intermediate-review-data.json
results/CONCLUSIONS.md
docs/acceptance-tests.md
```

Le contrôle `python3 -B scripts/check_links.py` parcourt les Markdown suivis, les liens relatifs, références, images HTML et ancres de titres. Les ancres sont approximées selon GitHub ; il ne remplace pas un navigateur et ne vérifie pas la disponibilité des sites externes.

Quatre liens inutilisables restent dans des messages candidats historiques, préservés sans réécriture. Les fichiers publiés correspondants sont accessibles ici : [code simple](../runs/astra-medium-core-v2-2-supervised-002/solution/calculator.py), [documentation simple](../runs/astra-medium-core-v2-2-supervised-002/solution/README.md), [code scientifique](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py), [documentation scientifique](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md).

## État de livraison

Contrat et budget proposés ; aucune suite nouvelle figée, aucun lanceur parallèle prêt, aucun appel modèle. Prochain travail technique : spécification complète, suite calibrée et transport isolé simulé, livrés ensemble avant le jalon de lancement.
