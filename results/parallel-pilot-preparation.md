# Préparation technique — pilote V1 / V2.1 légère

[Français](parallel-pilot-preparation.md) · [English (UK)](parallel-pilot-preparation.en.md) · [Español](parallel-pilot-preparation.es.md) · [Português](parallel-pilot-preparation.pt.md)

**Préparation hors modèle réalisée ; campagne non gelée et aucun candidat lancé.**
La question reste : le développement parallèle réduit-il le délai à qualité comparable, une fois l'intégration comptée ?

## Ce qui est livré

- [Spécification candidate complète](../challenges/modular-calculator-draft/SPEC.md) : quatre fichiers, syntaxe scientifique, limites explicites, courbes, lots, erreurs CLI et documentation. Instruction canonique en français.
- [Catalogue détaillé des dix groupes](../challenges/modular-calculator-draft/catalogue.json) et [suite indépendante](../challenges/modular-calculator-draft/tests/test_acceptance.py). M01 contraintes ; M02 calcul ; M03 fonctions ; M04 erreurs/limites ; M05 échantillonnage ; M06 SVG ; M07 lots ; M08 erreurs CLI ; M09 intégration ; M10 documentation.
- [Calibration](../tests/test_modular_acceptance.py) : deux variantes synthétiques admises et dix défauts injectés détectés, un par groupe. Les fixtures sont des outils de maintenance, jamais des références candidates à transmettre aux agents.
- [Simulation parallèle](../scripts/preflight_parallel_pilot.py) : deux processus fictifs isolés, rendez-vous avant travail, assemblage sans retouche, puis intégrateur fictif.
- [Preuves, durées relatives et empreintes](parallel-pilot-preparation.json). Sept tests de maintenance ciblés réussis ; douze exécutions de la suite dans la calibration (deux variantes et dix mutants).

## Ce que ces contrôles établissent

Le chargeur accepte les imports Python ordinaires, y compris une dataclass et un import entre modules. Deux représentations autorisées de courbe, polyline et chemin M/L, réussissent. Chaque mutation provoque l'échec du groupe prévu. Cela calibre la suite ; ce n'est pas une preuve d'exhaustivité.

Les processus DEV-A et DEV-B lisent leur contrat, mais ne peuvent ni le modifier ni lire/écrire le canari de l'autre, y compris via lien symbolique. Six contrôles par développeur réussissent. Les deux processus sont prêts avant libération ; INT démarre après collecte des deux résultats. L'assemblage est tracé par empreintes et une seule correction fictive est attribuée à INT.

Le premier essai d'isolation a été bloqué par le bac à sable englobant. L'exécution locale autorisée hors de ce bac a réussi en conservant le confinement des processus enfants. Aucun accès aux identifiants, aucun appel modèle. Les temps de fin sont des observations du parent ; ne pas les interpréter comme des instants exacts de sortie du noyau ni comme une mesure de gain collaboratif.

## Limites et prochaine livraison

M10 contrôle présence des API, limites et docstrings ; la pertinence des explications et l'exécution des exemples documentaires ne sont pas encore évaluées automatiquement. Le scan AST n'est pas une défense contre un candidat malveillant. La liste des limites de couverture est publiée dans le catalogue, sans prétendre à des tests cachés.

Le simulateur ne reçoit aucun modèle et n'offre aucun mode réel. Restent avant lancement : adaptation du transport authentifié aux deux rôles écrivains, capture des échanges et compteurs réels, validation des frontières de tous les outils, mandats définitifs et manifeste gelé. Le bac isolé de cette simulation n'a pas d'identifiants et ne peut pas être présenté comme un lanceur Codex prêt.

Le [protocole proposé](../docs/parallel-pilot.md) conserve Astra moyen, un solo puis une équipe, et 150 000 tokens intersession par organisation : proposition, pas plafond strict. Le solo segmenté reste un contrôle ultérieur distinct. Faire expertiser les artefacts avant le gel ; **rappel demandé : utiliser alors le modèle le plus puissant disponible**. Aucune autorisation de lancement ou de budget nouveau n'est inférée de cette préparation.

## Reproduire hors modèle

```bash
python3 -B -m unittest tests/test_modular_acceptance.py tests/test_parallel_pilot.py
python3 -B scripts/preflight_parallel_pilot.py --simulate
```

La seconde commande nécessite que l'environnement autorise les espaces de noms Linux utilisés par bubblewrap. En cas de refus, elle doit être signalée bloquée, jamais comptée comme réussie.
