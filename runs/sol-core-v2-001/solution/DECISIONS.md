# Arbitrages de conception

Ce document synthétise les quatre avis consultatifs reçus avant
l'implémentation : avis initial de SA-01, avis initial de SA-02, contradiction
de SA-01, puis contradiction de SA-02. Le candidat principal reste seul
décideur et seul écrivain.

| Recommandation consolidée | Source(s) | Décision | Motivation et conséquence observable |
|---|---|---|---|
| Garder `calculate(left, operator, right)` pure, sans parsing, lecture ni affichage | SA-01, SA-02, deux contradictions | Retenue | Sépare le contrat Python de l'interface et rend l'import/test direct sans effet de bord. |
| Accepter exactement `+`, `-`, `*` et `/` par branchement explicite | SA-01, SA-02 | Retenue | Une liste blanche minimale préserve `ValueError` pour tout autre opérateur et évite tout mécanisme dynamique. |
| Accepter naturellement les `int` et `float`, sans convertir des chaînes dans `calculate` | SA-01, contradictions | Retenue | Le parsing appartient à la CLI ; les opérations Python prennent déjà en charge entiers, décimaux et négatifs. |
| Exiger l'opérateur exact dans l'API | SA-01, contradictions | Retenue | `" + "` reste un opérateur inconnu lors d'un appel direct ; seuls les espaces de la ligne CLI sont structurants. |
| Laisser `calculate` lever `ZeroDivisionError` pour `0`, `0.0` et `-0.0` | SA-01, SA-02 | Retenue | Le test numérique exact `right == 0` correspond au contrat, sans tolérance arbitraire. |
| Utiliser une fonction interne de parsing et une fonction `main()` distincte | SA-02, contradictions | Retenue | Cette architecture minimale isole calcul, syntaxe et orchestration interactive. |
| Exiger exactement trois éléments, séparés par des espaces blancs souples | SA-01 révisé, SA-02 révisé | Retenue | `line.strip().split()` accepte espaces multiples, tabulations et bords ; `-2 * -3.5` est valide, tandis que `2+3` et les expressions composées sont rejetées sans ambiguïté. |
| Accepter la forme compacte `2+3` ou `-2*-3` | SA-01 initial, option ensuite révisée | Écartée | Elle n'est pas exigée et nécessiterait une analyse lexicale plus complexe pour distinguer signes et opérateurs. |
| Convertir les opérandes CLI avec `float` | SA-02 | Retenue | Cela couvre entiers, décimaux, signes et notation scientifique avec la bibliothèque standard. |
| Rejeter explicitement `nan` et `inf` | SA-01 et SA-02, option discutée | Écartée | Le contrat ne définit pas cette politique ; la conversion standard `float` est conservée et ces formes ne sont pas promises dans la documentation. |
| Afficher la représentation Python du résultat, sans convertir `5.0` en `5` | SA-02 | Retenue | Aucun format exact n'est imposé ; cette sortie est simple, stable et fidèle au calcul flottant. |
| Reconnaître `quit` et `exit` après retrait des espaces périphériques | SA-01, SA-02 | Retenue | Les commandes contractuelles terminent proprement, y compris avec des espaces accidentels. |
| Rendre les commandes de sortie insensibles à la casse | SA-01 et SA-02, confort facultatif | Écartée | La casse n'est pas spécifiée ; le comportement reste limité aux commandes exactes documentées. |
| Traiter EOF comme une sortie propre | SA-01, SA-02, contradictions | Retenue | Évite un traceback en entrée redirigée ou avec Ctrl-D et facilite les tests d'intégration. |
| Traiter aussi `KeyboardInterrupt` comme une sortie propre | SA-01, SA-02, confort facultatif | Retenue | Ctrl-C est une interruption utilisateur attendue ; sa capture au bord de la CLI n'altère pas le contrat métier. |
| Capturer uniquement les erreurs utilisateur attendues | SA-01, SA-02 | Retenue | La boucle traite `ValueError` et `ZeroDivisionError`, poursuit après erreur et ne masque pas les défauts de programmation par un `except Exception`. |
| Distinguer syntaxe CLI invalide et opérateur API inconnu | SA-01 révisé | Retenue | Le parseur vérifie la structure et les nombres ; un opérateur occupant le bon emplacement atteint `calculate`, qui conserve son `ValueError` contractuel. |
| Fournir des messages compréhensibles, stables et sans détails internes | SA-01, SA-02 | Retenue | Les erreurs sont préfixées par `Erreur :`, aucun traceback ni contenu intégral potentiellement démesuré n'est affiché. |
| Ajouter une limite arbitraire de longueur d'entrée | SA-01, option de durcissement | Écartée | Le cahier des charges ne fixe aucune limite ; le parsing retenu est structurellement simple et n'ajoute pas de politique imprévisible. |
| Protéger l'exécution par `if __name__ == "__main__"` | SA-01, SA-02 | Retenue | Importer le module expose `calculate` sans démarrer la boucle interactive. |
| N'utiliser ni évaluation dynamique, ni sous-processus, ni effet système | SA-01, SA-02 | Retenue | Le programme repose uniquement sur découpage, `float` et branchements explicites ; `eval`, `exec` et mécanismes équivalents sont absents. |
| Documenter les quatre opérations, un négatif, une erreur et les sorties | SA-01 | Retenue | Le README décrira uniquement la syntaxe et les capacités réellement implémentées. |
| Tester calcul, import, parsing et séquence CLI avec reprise après erreurs | SA-02, contradictions | Retenue pour les contrôles ciblés | Le vérificateur officiel, lancé seulement après la critique SA-03 comme prévu, confirme le calcul et la reprise de la CLI. |

## Arbitrage de la critique SA-03

La qualification ci-dessous couvre chaque défaut, risque et préférence énoncé
par SA-03. « Retenu » signifie que le constat est accepté, même lorsqu'il
confirme simplement l'existant ; « écarté » signifie qu'aucune correction
n'est justifiée par le contrat ; « non vérifiable » réserve le verdict au
contrôle officiel.

| Point SA-03 | Qualification | Justification et preuve observable | Correction |
|---|---|---|---|
| D1 — `DECISIONS.md` serait un livrable supplémentaire interdit | Écarté | La phase MAIN finale ordonne explicitement de compléter `solution/DECISIONS.md`. Cette exigence protocolaire plus précise impose de conserver cette trace, malgré la liste fonctionnelle de deux livrables dans le challenge. | Aucune ; le fichier est conservé. |
| D2 — exemple d'import incohérent avec le répertoire annoncé | Retenu | Depuis la racine, `calculator.py` n'est pas un module de premier niveau. Le README indique désormais le `cd runs/sol-core-v2-001/solution` préalable à `from calculator import calculate`. | Documentation corrigée. |
| D3 — garantie Ctrl-C plus large que la capture effective | Retenu | Dans `main()`, le bloc `try` englobe maintenant lecture, parsing, calcul et affichage ; `except (EOFError, KeyboardInterrupt)` assure la sortie sans traceback sur toute la boucle. | Portée de la capture corrigée. |
| R1 — `+`, `-` et `*` peuvent retourner un `int` avec des arguments `int` | Écarté | Le contrat demande d'accepter entiers et décimaux et annote l'API, mais n'impose pas `type(result) is float`. Préserver la sémantique numérique Python évite aussi une conversion artificielle ou un débordement sur de grands entiers. | Aucune. |
| R2 — acceptation implicite de `nan` et `inf` par la CLI | Écarté | Le contrat ne définit pas les valeurs non finies. Le README ne les promet pas et l'arbitrage initial avait déjà écarté une politique de rejet supplémentaire. | Aucune. |
| R3 — absence de limite de longueur d'entrée | Écarté | La CLI locale et le challenge ne fixent aucune borne. Une limite arbitraire modifierait le domaine accepté sans seuil contractuel. | Aucune. |
| R4 — `tuple[...]` impose Python 3.9+ | Retenu | L'annotation interne utilise désormais `typing.Tuple`, disponible dans les versions antérieures de Python 3, sans changer l'API publique ni ajouter de dépendance externe. | Compatibilité d'annotation corrigée. |
| R5 — validation non encore démontrée au moment de la critique | Retenu | Le constat était exact au moment de SA-03. Il est désormais levé par le premier passage officiel : 6 tests exécutés, tous réussis, code de sortie 0 et verdict `OK`. | Vérificateur officiel exécuté ; aucune correction fonctionnelle requise. |
| R6 — API permissive pour des objets hors annotations | Écarté | Les paramètres sont contractuellement numériques. Ajouter une validation de types non demandée pourrait rejeter des objets numériques compatibles ; les chaînes et autres objets restent hors contrat. | Aucune. |
| P1 — rejet de la syntaxe compacte compatible avec le challenge | Retenu | `_parse_expression()` exige trois éléments issus de `split()` et le README annonce que `2+3` est invalide. | Existant conservé. |
| P2 — sensibilité à la casse de `quit` et `exit` acceptable | Retenu | `line.strip() in {"quit", "exit"}` correspond exactement aux commandes nommées par le contrat. | Existant conservé. |
| P3 — affichage de `5.0` acceptable | Retenu | La CLI affiche directement le résultat avec `print(result)` ; aucun format textuel différent n'est imposé. | Existant conservé. |
| P4 — préfixe d'erreur commun compréhensible | Retenu | La capture ciblée affiche `Erreur : {error}` et reprend la boucle. | Existant conservé. |
| P5 — espaces multiples et tabulations raisonnables | Retenu | `line.strip().split()` traite les espaces blancs souples tout en maintenant exactement trois éléments. | Existant conservé. |
| P6 — cœur nominal correctement séparé et exceptions préservées | Retenu | L'inspection montre les fonctions séparées et le garde `__main__`. Le vérificateur confirme les quatre opérations, les variantes numériques, les exceptions, la reprise de la CLI et l'absence d'exécution dynamique. | Existant conservé. |

## Vérification officielle

Commande exécutée depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/sol-core-v2-001/solution
```

Premier passage : **réussi**, avec 6 tests exécutés, 6 réussites, code de
sortie 0 et verdict `OK`. Les contrôles couvrent la reprise de la CLI après
erreurs, la division par zéro, l'absence d'exécution dynamique interdite, les
quatre opérations et variantes numériques, l'opérateur invalide et la présence
des fichiers requis.

Aucun défaut n'a été confirmé par ce premier passage ; il n'y a donc eu aucune
correction fonctionnelle après vérification. Le passage final de confirmation,
effectué après consignation de la preuve documentaire, réussit lui aussi les
6 tests avec un code de sortie 0 et le verdict `OK`.
