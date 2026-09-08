# Arbitrages — première solution V2

Table établie avant l'implémentation. Les avis sont consultatifs : le candidat
MAIN décide et reste l'unique écrivain. L'orchestrateur expérimental a fourni
les quatre textes ; aucun consultant supplémentaire n'est lancé ici.

## Ordre des échanges reçus

1. SA-01 INITIAL — analyste du contrat et de la sécurité.
2. SA-02 INITIAL — analyste de conception et de testabilité.
3. SA-01 CONTRADICTION — retrait de la préférence pour les nombres finis.
4. SA-02 CONTRADICTION — maintien du comportement numérique standard et
   distinction entre ligne blanche et EOF.

Les textes visibles intégraux sont ceux du message de relais, dans cet ordre,
sans modification ; ils constituent la source de l'annexe verbatim que
l'orchestrateur expérimental doit produire. Cette table en est une synthèse,
pas une substitution aux textes originaux.

## Table de décision

| Recommandation et provenance | Décision motivée |
| --- | --- |
| Quatre opérateurs explicites, sans interprétation de code (SA-01/02, initiaux et croisés) | Retenue : branches arithmétiques explicites, bibliothèque standard uniquement ; aucune exécution dynamique. |
| API sans entrées-sorties, exceptions observables (SA-01/02) | Retenue : `calculate` retourne un nombre ou lève les exceptions demandées ; la CLI seule affiche les erreurs. |
| Retour `float`, même sur entiers (SA-01/02) | Retenue : conversion du résultat en `float`, sans validation supplémentaire des objets Python hors contrat. |
| Zéro exact, y compris `-0.0`, même avec un numérateur non fini (SA-01 initial/croisé, SA-02 croisé) | Retenue : comparaison exacte du dénominateur avant division ; aucun seuil approximatif. |
| Trois éléments séparés par des blancs (SA-01/02) | Retenue comme interprétation : `split()` accepte espaces multiples et tabulations, conserve signes et exposants. `2+3` est rejeté ; l'ambiguïté du challenge reste signalée. |
| Consommer toute la ligne, refuser expressions composées et éléments supplémentaires (SA-01/02) | Retenue : exactement trois éléments, sans parenthèses ni priorités. |
| Ligne vide invalide, distincte de EOF (SA-01 initial et deux avis croisés) | Retenue : message puis reprise pour une ligne blanche ; arrêt normal sur EOF. |
| Point décimal et conversion standard, notation scientifique (SA-01/02) | Retenue : `float` pour la CLI ; virgule refusée, notation scientifique acceptée. |
| Restreindre aux nombres finis (SA-01 initial) | Écartée, conformément à sa révision et à SA-02 : restriction absente du contrat ; `nan`, `inf` et résultats non finis suivent Python. |
| Pas d'arrondi arbitraire (SA-02 initial, SA-01 croisé) | Retenue : résultat flottant et affichage standard, avec précision binaire documentée. |
| Commandes après suppression des blancs ; casse facultative (SA-01/02) | Retenue avec tolérance de casse : `strip().lower()` sur la ligne complète ; `quit + 2` ne quitte pas. |
| Séparer calcul, analyse et boucle (SA-02, confirmations croisées) | Retenue : trois fonctions simples isolent les responsabilités et facilitent les contrôles. |
| Import inactif (SA-01/02) | Retenue : garde `__name__` pour lancer la boucle uniquement en exécution directe. |
| Erreurs ciblées et reprise interactive (SA-01/02) | Retenue : captures de `ValueError` et `ZeroDivisionError`, diagnostics distincts ; pas de capture générale. |
| EOF et interruption clavier propres (SA-01/02) | Retenue : sorties normales sans traceback, robustesse complémentaire au contrat. |
| Affichage simple et stable (SA-01/02) | Retenue : invite `> `, résultats Python et erreurs françaises sur la sortie standard ; arrêt normal avec code zéro. |
| Éviter limites de longueur et validation hors contrat (SA-01, confirmations croisées) | Retenue : aucun plafond arbitraire, aucune dépendance, aucun accès réseau ou fichier de données. |
| Livrer seulement calculator.py et README.md (SA-01/02) | Adaptée : ces deux livrables sont fournis ; `DECISIONS.md` est ajouté à la demande explicite de la phase MAIN, prioritaire sur cette lecture des avis. |
| README avec lancement, syntaxe, exemples et récupération (SA-01/02) | Retenue : documentation des choix, limites numériques et utilisation Python/CLI. |
| Contrôles API, exceptions, import et sessions (SA-01/02) | Retenue : contrôles ciblés complémentaires, incluant plusieurs erreurs suivies d'un calcul valide, sorties distinctes et EOF. Les non-finis sont exploratoires. |
| Vérificateur officiel (SA-01/02) | Différée : la phase courante interdit son lancement avant la critique SA-03 ; le verdict indépendant reste à établir. |

## Trace de phase

5. MAIN lit le challenge actif et les règles de journalisation/restitution,
   puis écrit la présente table avant tout code.
6. MAIN crée `calculator.py` et `README.md`, puis exécute un contrôle ciblé
   avec `python3 -B -` (script transmis sur l'entrée standard). Code de sortie
   observé : 0. Les assertions couvrent les quatre opérations, entiers,
   décimaux, négatifs, retour `float`, petit dénominateur non nul, quatre
   opérateurs invalides et neuf combinaisons de division par zéro (trois
   représentations du zéro et numérateurs fini, infini, NaN). Les explorations
   de NaN et de débordement vers l'infini réussissent également.
   Les sous-processus CLI vérifient neuf saisies invalides suivies de deux
   calculs valides, espaces et tabulations, notation scientifique, `quit`,
   `exit`, casse et blancs périphériques, absence de traitement après sortie,
   EOF immédiat et après calcul, absence de traceback et de sortie d'erreur.
   L'import en processus distinct est silencieux et termine normalement.
   Ctrl+C est contrôlé par simulation de `KeyboardInterrupt`, pas par signal
   envoyé dans un terminal. Aucune correction fonctionnelle n'a été nécessaire.
   Sorties visibles : « API : opérations, types, exceptions, zéros signés et
   exploration non-finis réussis. » puis « CLI : neuf erreurs puis calculs
   valides, sorties, EOF, interruption simulée et import silencieux réussis. »
7. SA-03 et vérificateur officiel : en attente de la phase suivante, pilotée
   par l'orchestrateur expérimental. Aucun avis SA-03 n'a été reçu ici.

Tokens et durée globale : non enregistrés. Aucun changement de gouvernance,
de challenge, de tests ou de scripts ; aucune opération Git autorisée.

## Phase MAIN finale — arbitrage de SA-03

La trace précédente décrit la première phase et reste historique. La présente
session reprend le même rôle candidat MAIN, unique écrivain. L'orchestrateur
expérimental relaie les avis ; SA-01 (contrat et sécurité), SA-02 (conception
et testabilité) et SA-03 (critique finale) sont les trois consultants autorisés,
en lecture seule. Aucun nouveau consultant ni sous-agent n'est appelé ici.

| Point de SA-03 | Qualification | Justification et preuve |
| --- | --- | --- |
| Aucun défaut fonctionnel confirmé sur le cœur usuel ; exceptions, reprise, import et absence d'injection | Retenu comme constat statique limité | Lecture de `calculator.py` : quatre branches explicites, captures ciblées, garde `__name__`, aucune interprétation de code. L'acceptation technique dépend du contrôle officiel ci-dessous. |
| Acceptation des entiers trop générale dans le README | Retenu | Contrôle ciblé de cette session : `calculate(10**400, '+', 0)` lève effectivement `OverflowError`. README corrigé pour préciser la limite ; aucune arithmétique arbitraire ajoutée. La violation contractuelle pour cette plage non spécifiée reste non vérifiable. |
| Validation officielle absente au moment de la critique | Retenu | La trace historique la reportait explicitement. Exécution désormais autorisée en phase finale ; résultat consigné après passage. |
| Couverture et exécution des contrôles de la première phase non confirmables par SA-03 | Non vérifiable indépendamment dans cette session | Le relais et la trace déclarent des succès, sans script complet ni sorties brutes disponibles ici. Ils restent des déclarations historiques, distinctes des contrôles directement observés ci-dessous. |
| Présence de DECISIONS.md, éventuelle interdiction du troisième fichier | Écarté comme défaut d'autorisation | Le mandat final exige explicitement de compléter `solution/DECISIONS.md`. Sa présence est confirmée et autorisée ; les deux livrables du challenge existent. |
| Espaces obligatoires, refus de 2+3 et ambiguïté du challenge | Retenu comme limite d'interprétation | `_parse_expression('2+3')` lève `ValueError` dans le contrôle ciblé. Le README l'annonce. Aucun élargissement de grammaire retenu ; le consensus ne transforme pas ce choix en exigence textuelle. |
| Perte de précision et sous-dépassement | Retenu | Le contrôle ciblé confirme que `1e-400` devient `0.0`, puis provoque `ZeroDivisionError`. README corrigé : le caractère non nul s'apprécie après conversion. L'exemple de précision `0.1 + 0.2` était déjà documenté. |
| Entrées sans limite, consommation potentielle de mémoire | Retenu comme risque résiduel ; plafond écarté | Lecture de `input()` et `split()` sans borne. Aucune résistance à l'épuisement des ressources exigée ; aucune mesure de saturation réalisée. Un plafond arbitraire n'est pas justifié par le contrat. |
| Non-finis, erreurs sur stdout, casse tolérée, absence d'arrondi : changements inutiles | Retenu | Code et README concordent sur ces choix. Aucun changement fonctionnel retenu. |
| Régression non établie faute d'élément comparatif | Non vérifiable | Aucun autre run ni résultat consulté ; aucune affirmation comparative ajoutée. |
| Priorité : documentation numérique puis vérification officielle | Retenu | Corrections documentaires appliquées avant le premier passage officiel. |

## Suite numérotée des échanges et contrôles

8. L'orchestrateur expérimental fournit le mandat final, les quatre avis
   précédents, le snapshot et SA-03 CRITIQUE, cinquième texte consultatif.
   L'ordre des avis reste SA01_INITIAL, SA02_INITIAL, SA01_CROSS, SA02_CROSS,
   SA-03 CRITIQUE. Le texte visible intégral du relais demeure la source
   verbatim pour le PV de l'orchestrateur ; aucune reformulation ne le remplace.
9. MAIN relit le challenge actif, les trois fichiers et les règles de trace.
   Un contrôle ciblé `python3 -B -` confirme les trois observations numériques
   et syntaxiques ci-dessus, avec code de sortie 0. Sorties visibles :
   « Grand entier : OverflowError confirmé. »,
   « Sous-dépassement : dénominateur converti en zéro, ZeroDivisionError confirmé. »,
   « Grammaire : 2+3 refusé par ValueError confirmé. »
10. MAIN arbitre tous les points de SA-03 dans cette table et corrige seulement
    le README : limites des grands entiers, zéro après conversion et état de
    phase. `calculator.py` reste inchangé ; aucun défaut fonctionnel confirmé
    n'impose une correction à ce stade.
11. MAIN exécute depuis la racine du dépôt la commande exacte :
    `python3 scripts/verify.py --solution runs/astra-medium-core-v2-001/solution`.
    La variable `PYTHONDONTWRITEBYTECODE=1` empêche les écritures de caches
    Python hors de `solution/` ; aucun script ni test n'est modifié.
    Premier passage officiel : code de sortie 0, six tests réussis.
    Sortie visible du vérificateur :

    ```text
    test_cli_recovers_from_errors_and_exits_cleanly (test_acceptance.CalculatorAcceptanceTests.test_cli_recovers_from_errors_and_exits_cleanly) ... ok
    test_division_by_zero (test_acceptance.CalculatorAcceptanceTests.test_division_by_zero) ... ok
    test_forbidden_dynamic_execution_is_absent (test_acceptance.CalculatorAcceptanceTests.test_forbidden_dynamic_execution_is_absent) ... ok
    test_four_operations_and_numeric_variants (test_acceptance.CalculatorAcceptanceTests.test_four_operations_and_numeric_variants) ... ok
    test_invalid_operator (test_acceptance.CalculatorAcceptanceTests.test_invalid_operator) ... ok
    test_required_files_exist (test_acceptance.CalculatorAcceptanceTests.test_required_files_exist) ... ok

    ----------------------------------------------------------------------
    Ran 6 tests in 0.010s

    OK
    ```

12. Verdict final : `OK`, identique au premier passage. Aucun défaut confirmé
    par le vérificateur, aucune correction fonctionnelle ni relance nécessaire.
    MAIN consigne le résultat ici et dans le README. Les seules corrections
    portent sur la documentation ; le code de la première solution est conservé.

Limites finales : syntaxe à trois éléments séparés par des blancs, précision
et plage des flottants Python, consommation mémoire non bornée par une limite
de saisie. Le succès des six tests ne résout pas toutes les ambiguïtés du
challenge. Les contrôles antérieurs restent rapportés par le relais ; les
contrôles ciblés et le passage officiel de cette session sont directement
observés. Aucun nouveau contrôle de Ctrl+C par signal réel n'a été effectué.
Tokens et durée globale : non enregistrés. Seule la durée de suite annoncée
par le vérificateur est disponible : 0.010 s. Aucune opération Git, aucune
consultation d'une autre tentative, aucun changement de gouvernance, de
challenge, de script ou de test. Aucun TODO fonctionnel ouvert ; le PV et
son annexe verbatim relèvent de l'orchestrateur expérimental hors de ce run.
