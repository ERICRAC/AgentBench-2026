# Contrôles candidats — première solution

## Échange 001 — mandat et avis

Demande : préparer une première solution complète avant SA-03, en V2 gouvernée.
MAIN, candidat et unique écrivain, a lu le CHALLENGE.md actif et les quatre avis
fournis par l'orchestrateur expérimental. Aucun autre agent n'a été lancé.
L'ordre des messages sources est enregistré dans DECISIONS.md ; leurs textes
visibles intégraux restent dans le message de relais, sans réécriture par MAIN.
L'orchestrateur expérimental conserve la production du PV et de son annexe.

## Échange 002 — réalisation

DECISIONS.md a été créé avant scientific_calculator.py et README.md.
Les désaccords et corrections ont été arbitrés explicitement : compositions
permises, domaines entièrement invalides échantillonnés en None, axes au bord,
limite de longueur documentée, aucune heuristique d'asymptote.

## Échange 003 — contrôles ciblés

Commande candidate exécutée dans solution :
`PYTHONDONTWRITEBYTECODE=1 python3 -` avec un programme de contrôle fourni sur
l'entrée standard (bibliothèque standard, assertions, mock de l'entrée CLI et
parseur XML). Le programme de contrôle n'est pas une suite indépendante figée.

Sortie capturée :

```text
131 assertions ciblées réussies ; aucun vérificateur officiel lancé.
```

Code de sortie : 0.

Couverture observée :

- Précédence, associativité, exposants signés, constantes, toutes les fonctions,
  compositions et notation scientifique ; type float et résultats attendus.
- Rejet de syntaxe étrangère, appels indirects, noms arbitraires, caractères
  numériques non ASCII, entrées vides et suffixes ; domaines, overflow,
  variable absente/non finie et division par zéro.
- Longueur excessive et profondeur excessive converties en ValueError.
- Bornes exactes, point central de 1/x, domaine partiel de sqrt(x), domaine
  entièrement invalide, expression structurellement invalide, paramètres rejetés.
- Interpolation finie de -1.7e308 à 1.7e308.
- SVG parsé en XML, deux axes line, deux segments séparés pour 1/x,
  titre hostile conservé comme texte et contrôles XML remplacés, aucun script.
- Projections extrêmes, sous-normales, plage constante, abscisses constantes,
  points isolés et trous ; attributs de coordonnées contrôlés finis.
- Aucun point fini : ValueError sans altérer le fichier préexistant.
- CLI simulée : succès, erreur numérique, succès, échec d'écriture, tracé réussi,
  historique des seules réussites, effacement, sortie et EOF.
- Inspection syntaxique du source : aucun appel à eval, exec ou compile.

L'artefact temporaire `_controle.svg`, créé exclusivement dans solution, a été
supprimé après les contrôles. Aucun fichier du challenge, des tests, des scripts
ou de la gouvernance n'a été modifié. Aucun défaut n'a été révélé par ces
contrôles ; aucune correction consécutive à un échec n'a été nécessaire.

## Échange 004 — frontière de phase

Première solution prête à être transmise à SA-03 par l'orchestrateur
expérimental. Aucun avis SA-03 reçu et aucune vérification officielle exécutée.
Le verdict indépendant reste ouvert. Après la critique, la phase finale devra
arbitrer ses recommandations, corriger les défauts confirmés et exécuter la
commande exacte documentée dans README.md.

Aucune opération Git effectuée. Tokens et durée globale : non enregistrés.
Les contrôles candidats ne garantissent ni la couverture exhaustive ni le
résultat du vérificateur indépendant. Aucun visuel éditorial public produit ;
le SVG livré est un artefact autonome à fond blanc explicite.

## Échange 005 — mandat final et arbitrage SA-03

Le commanditaire demande la clôture de la même tentative dans une nouvelle
session éphémère MAIN. L'orchestrateur expérimental relaie les avis autorisés ;
MAIN, orchestrateur candidat et unique écrivain, ne lance aucun consultant.
Rôles consultatifs reçus : SA-01 contrat/sécurité, SA-02 conception/testabilité,
SA-03 critique des limites. Ordre source conservé : SA01_INITIAL,
SA02_INITIAL, SA01_CROSS, SA02_CROSS, première solution, SA-03 CRITIQUE.
Les textes visibles intégraux restent dans le relais utilisateur pour l'annexe
verbatim que doit produire l'orchestrateur expérimental ; ils ne sont ni
résumés à leur place ni présentés comme de nouveaux échanges dans cette session.

CHALLENGE.md actif et fichiers présents relus avant modification. Chaque point
SA-03 est qualifié dans DECISIONS.md avant correction. Retenus : suppression
des plafonds syntaxiques par pile explicite, échappement des contrôles du
terminal, protection globale des canaux CLI. Écartés comme corrections :
plafond de samples et écriture transactionnelle. Couverture précise des
131 assertions historiques : non vérifiable dans cette session.

## Échange 006 — corrections et contrôles candidats finaux

Fichiers : scientific_calculator.py et README.md mis à jour ; DECISIONS.md et
CONTROLES.md complétés ; controle_final.py conserve les nouveaux contrôles.
Aucun changement de challenge, de suite indépendante, de script ni de gouvernance.

Commande dans solution :

```bash
PYTHONDONTWRITEBYTECODE=1 python3 controle_final.py
```

Sortie :

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.037s

OK
```

Code de sortie : 0. Couverture détaillée et limites des preuves dans
DECISIONS.md. Aucun échec pendant ces contrôles ; aucune correction consécutive.

## Échange 007 — premier passage officiel et verdict final

Commande exécutée exactement depuis la racine du dépôt :

```bash
python3 scripts/verify.py --challenge scientific-calculator --solution runs/astra-medium-scientific-v2-001/solution
```

Sortie capturée :

```text
test_cli_recovers_plots_tracks_history_and_exits (test_acceptance.ScientificCalculatorAcceptanceTests.test_cli_recovers_plots_tracks_history_and_exits) ... ok
test_constants_functions_and_scientific_notation (test_acceptance.ScientificCalculatorAcceptanceTests.test_constants_functions_and_scientific_notation) ... ok
test_curve_sampling_and_discontinuities (test_acceptance.ScientificCalculatorAcceptanceTests.test_curve_sampling_and_discontinuities) ... ok
test_only_standard_library_and_no_dynamic_execution (test_acceptance.ScientificCalculatorAcceptanceTests.test_only_standard_library_and_no_dynamic_execution) ... ok
test_operator_precedence_parentheses_and_unary_signs (test_acceptance.ScientificCalculatorAcceptanceTests.test_operator_precedence_parentheses_and_unary_signs) ... ok
test_required_files_and_documentation_exist (test_acceptance.ScientificCalculatorAcceptanceTests.test_required_files_and_documentation_exist) ... ok
test_svg_is_valid_safe_and_contains_axes_and_curve (test_acceptance.ScientificCalculatorAcceptanceTests.test_svg_is_valid_safe_and_contains_axes_and_curve) ... ok
test_syntax_domain_and_arithmetic_errors (test_acceptance.ScientificCalculatorAcceptanceTests.test_syntax_domain_and_arithmetic_errors) ... ok
test_variables_and_unsafe_or_unknown_names (test_acceptance.ScientificCalculatorAcceptanceTests.test_variables_and_unsafe_or_unknown_names) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.046s

OK
```

Code de sortie : 0. Premier passage officiel : réussi, après les corrections
retenues de SA-03. Verdict final : réussi, 9 tests sur 9. Aucun échec confirmé
par le vérificateur, aucune correction après ce passage, aucune relance.
Seules les traces et la mention du résultat dans README sont complétées ensuite.

## Échange 008 — limites et restitution

La suite valide ses neuf tests, sans garantie exhaustive. Restent documentés :
ressources physiques finies, échantillonnage non exhaustif des discontinuités,
arrondis flottants, écriture non transactionnelle, terminaison en cas de perte
des canaux CLI, impossibilité de vérifier rétroactivement les 131 assertions.
Aucune mesure d'épuisement réel ou de panne de stockage, aucun terminal physique
testé. Les durées des suites ci-dessus sont observées ; tokens et durée globale
de la phase sont non enregistrés. Aucun horodatage de travail ajouté.
Aucune opération Git ; livraison et PV externe réservés à l'orchestrateur
expérimental. Aucun changement de gouvernance proposé ou appliqué.
