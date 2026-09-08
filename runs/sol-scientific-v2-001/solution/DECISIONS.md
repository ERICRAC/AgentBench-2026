# Table d'arbitrage — première solution

Cette table synthétise les quatre textes autorisés de SA-01 et SA-02. Les
recommandations répétées ont été regroupées, mais chaque avis est relié à une
décision explicite. Les consultants sont en lecture seule et leurs avis restent
non contraignants ; l'orchestrateur candidat demeure l'unique décideur et
écrivain.

| Sources | Recommandation | Décision | Motivation et conséquence vérifiable |
|---|---|---|---|
| SA-01 initial, SA-02 initial, deux révisions | Séparer lexer, parseur, AST, évaluateur, API, SVG et CLI ; consommer toute l'entrée. | **Retenue.** | Une grammaire fermée et des phases distinctes rendent la précédence testable et empêchent l'accès à des constructions Python. |
| SA-01 initial, SA-02 initial, deux révisions | Interdire toute évaluation dynamique et résoudre constantes/fonctions par listes blanches. | **Retenue.** | Aucun `eval`, `exec`, `compile`, attribut, index, chaîne, import ou appel arbitraire ne sera utilisé ou accepté. |
| SA-01 initial, SA-02 initial, deux révisions | Implémenter `^` à droite, plus prioritaire que les signes, tout en acceptant un exposant signé. | **Retenue.** | La grammaire visera simultanément `2^3^2 == 512`, `-2^2 == -4` et `2^-2 == 0.25`. |
| SA-01 initial, SA-02 initial | Accepter les littéraux décimaux/scientifiques usuels, une fonction unaire avec parenthèses, et refuser virgule, `**`, multiplication implicite et suffixe résiduel. | **Retenue.** | Cela suit exactement la surface du langage spécifié et évite les reconnaissances partielles. Les espaces ASCII sont ignorés ; les autres caractères, notamment les ressemblants Unicode, sont rejetés. |
| SA-01 initial, SA-02 initial, deux révisions | Garantir un `float` fini ; préserver `ZeroDivisionError` et convertir domaine réel, complexe, débordement et non-finitude en `ValueError`. | **Retenue.** | La taxonomie d'erreurs fait partie du contrat public et ne doit pas laisser fuir des exceptions arithmétiques internes attendues. |
| SA-01 initial, SA-02 initial, deux révisions | Seul `x` est résolvable ; décider si les autres clés de `variables` sont rejetées ou ignorées ; refuser les valeurs invalides et les booléens. | **Retenue avec arbitrage : clés supplémentaires rejetées.** | Le dictionnaire est validé strictement : seulement `x`, valeur réelle finie, non booléenne. Cette politique simple rend les fautes d'appel visibles sans élargir le langage. |
| SA-01 initial, SA-02 initial, deux révisions | Valider des bornes finies, `x_min < x_max`, un entier véritable `samples >= 2`, inclure exactement les deux bornes. | **Retenue.** | Le dernier `x` sera forcé à `x_max`; `bool` sera refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Parser une seule fois ; lever les erreurs structurelles de `sample_curve`, convertir seulement les erreurs numériques dépendant de `x` en `None`. | **Retenue.** | Syntaxe, noms et mauvais appels seront validés avant la boucle. Division, domaine, dépassement et résultat non fini à un échantillon couperont localement la courbe. |
| SA-01 initial, SA-02 initial, deux révisions | Ajouter des plafonds de longueur, profondeur, jetons ou nombre d'échantillons contre le déni de service. | **Écartée pour cette version.** | Les révisions reconnaissent qu'aucun seuil n'est contractuel et qu'un plafond arbitraire pourrait rejeter une entrée d'acceptation valide. Les erreurs de récursion seront néanmoins normalisées, sans promettre la prise en charge d'entrées pathologiques. |
| SA-01 initial, SA-02 initial, deux révisions | Produire un SVG déterministe, autonome, analysable et inerte ; valider les nombres, échapper le titre et traiter les contrôles XML interdits. | **Retenue.** | Le document sera construit avec `xml.etree.ElementTree`, sans script, lien ni attribut actif. Le titre sera vérifié selon XML 1.0 avant sérialisation. |
| SA-01 initial, SA-02 initial, deux révisions | Chaque `None` coupe la courbe ; gérer les domaines dégénérés et les séquences d'un seul point ; lever si aucun point fini. | **Retenue.** | Chaque série contiguë aura son propre `polyline`; un singleton sera rendu par `circle`. Les étendues nulles seront élargies de façon déterministe. |
| SA-02 initial | Décider où placer un axe lorsque zéro est hors domaine. | **Retenue avec arbitrage : projection bornée au bord.** | Chaque axe reste un élément `line`; sa position est la projection de zéro limitée à la zone de tracé. |
| SA-01 initial, SA-02 initial | Autoriser ou refuser l'écrasement d'un SVG existant et ne pas inventer de bac à sable de chemins. | **Retenue avec arbitrage : écrasement autorisé.** | `output_path` est honoré comme fourni et l'écriture UTF-8 remplace un fichier existant, comportement standard documenté. Le nom CLI vide est refusé. |
| SA-01 initial, SA-02 initial, deux révisions | Rendre la CLI résiliente ; évaluer les bornes de `plot` avec le moteur ; exiger quatre champs et enregistrer seulement les succès complets. | **Retenue.** | Les erreurs sont affichées sans traceback et la boucle continue. `help`, `history`, `clear`, erreurs et sorties ne sont pas historisés ; un tracé l'est seulement après l'écriture. |
| SA-02 initial | Définir le comportement sur EOF et interruption clavier. | **Retenue : sortie propre.** | EOF et `KeyboardInterrupt` terminent la boucle avec une ligne de séparation, sans traceback. |
| SA-01 initial, SA-02 initial, deux révisions | Documenter syntaxe, radians, erreurs, discontinuités, absence de multiplication implicite, écrasement et limites ; effectuer des contrôles modulaires ciblés. | **Retenue.** | Le README couvrira l'API et la CLI. Cette phase exécutera des tests ciblés du moteur, SVG et CLI, mais pas le vérificateur officiel réservé à la phase suivant SA-03. |

## Arbitrage final de SA-03

Chaque puce de la critique finale est qualifiée ci-dessous. « Retenue
(maintien) » signifie que le comportement déjà livré est confirmé et ne
nécessite pas de modification. Les preuves désignent les éléments observables
de la solution finale ; le résultat du vérificateur est consigné après son
exécution.

| ID | Point de SA-03 | Qualification | Justification et preuve observable |
|---|---|---|---|
| SA03-01 | `KeyboardInterrupt` n'était intercepté qu'autour de `input()`. | **Retenu — correction.** | `main()` intercepte désormais aussi `KeyboardInterrupt` autour de `_handle_line`; une interruption pendant calcul, tracé, écriture ou affichage termine donc sans traceback. |
| SA03-02 | Le formatage CLI à 15 chiffres pouvait effacer une variation représentable. | **Retenu — correction.** | `_handle_line()` affiche directement le `float` retourné par `evaluate`; `1 + 1e-15` conserve ainsi la représentation `1.000000000000001`. |
| SA03-03 | Une profondeur d'AST issue d'une longue somme pouvait devenir une série de `None`. | **Retenu — correction.** | `_evaluate_ast()` utilise deux piles explicites plutôt que la pile d'appels Python et `sample_curve()` ne capture plus `RecursionError`. Une profondeur syntaxique réellement excessive reste normalisée par `_parse_expression()`. |
| SA03-04 | L'exemple interactif du README ne correspondait pas à l'ancien formatage CLI. | **Retenu — correction.** | L'affichage direct issu de SA03-02 produit bien `2.0000000000000004` pour `sqrt(2)^2`, conformément à l'exemple du README. |
| SA03-05 | Absence de plafonds contre les volumes pathologiques. | **Écarté.** | Le défi ne fixe aucun seuil. Un plafond arbitraire pourrait refuser une entrée contractuellement valide; cette limite reste explicitement déclarée dans la section « Sécurité et limites » du README. |
| SA03-06 | Une erreur numérique indépendante de `x`, comme `sqrt(-1)`, produit uniquement des `None`. | **Écarté comme défaut.** | Le contrat demande qu'une valeur hors domaine à un point devienne `None`; il n'exige pas d'analyse symbolique de la dépendance à `x`. Le parsing préalable continue de lever syntaxe, nom et appel invalides. |
| SA03-07 | Le rejet des clés de variables autres que `x` pourrait gêner un contexte plus large. | **Écarté.** | Le langage ne définit que `x`; `_validated_variables()` applique la politique stricte déjà documentée sans rendre un autre nom accessible. Aucun comportement contraire n'est exigé par le contrat. |
| SA03-08 | Le chemin arbitraire permet l'écrasement, les chemins absolus et les liens symboliques. | **Écarté.** | L'API publique reçoit précisément un `output_path` et ne définit aucun bac à sable. `write_svg()` honore ce chemin et le README documente le remplacement d'une cible existante. |
| SA03-09 | L'écriture directe n'est pas transactionnelle. | **Écarté.** | L'atomicité n'appartient pas au contrat et un fichier temporaire imposerait d'autres hypothèses de système de fichiers. L'historique reste transactionnel au niveau demandé : ajout seulement après retour réussi de `write_svg()`. |
| SA03-10 | Un chemin contenant des contrôles pouvait injecter une présentation terminal. | **Retenu — correction.** | `_terminal_text()` échappe les caractères non imprimables lors du message de succès et de l'affichage de l'historique, sans modifier le chemin réellement transmis à `write_svg()`. |
| SA03-11 | `0^-1` héritait d'un `ZeroDivisionError` Python malgré l'absence de `/`. | **Retenu — correction.** | `_apply_binary()` ne propage `ZeroDivisionError` que pour `/`; une puissance de zéro à exposant négatif est normalisée en `ValueError` comme opération hors domaine. |
| SA03-12 | `write_svg()` exige une `list` plutôt qu'un itérable. | **Retenu — maintien.** | La signature contractuelle annonce une `list`; le contrôle `isinstance(points, list)` reste cohérent et rend les erreurs d'appel explicites. |
| SA03-13 | Une coordonnée non finie fournie directement devient une coupure. | **Retenu — maintien.** | La normalisation de `write_svg()` ajoute `None` pour ce point et l'absence de tout point fini lève bien `ValueError`, conformément à l'objectif de segmentation sûre. |
| SA03-14 | Axes au bord, singleton par `circle` et écrasement autorisé sont des choix. | **Retenu — maintien.** | Ces trois arbitrages sont documentés dans la première table et matérialisés par la projection bornée, `append_segment()` et `ElementTree.write()`. Aucun ne contredit le contrat. |
| SA03-15 | Rejet des espaces Unicode, booléens et multiplications implicites. | **Retenu — maintien.** | `_tokenize()`, `_finite_float()` et la grammaire fermée rendent ces refus observables; ils évitent des extensions ambiguës du langage spécifié. |

## Vérification officielle finale

Commande exécutée depuis la racine du dépôt, sans variante :

```text
python3 scripts/verify.py --challenge scientific-calculator --solution runs/sol-scientific-v2-001/solution
```

- **Premier passage : échec, 9 tests exécutés, 3 succès et 6 erreurs.** Les six
  erreurs avaient la même trace : le chargement indépendant du module sous
  Python 3.13 échouait dans le décorateur `dataclass`, car le chargeur du test
  ne plaçait pas le module dans `sys.modules`. Aucun test fonctionnel concerné
  ne pouvait alors commencer.
- **Correction confirmée et appliquée :** `_Token`, simple conteneur lexical,
  est désormais une classe à `__slots__` avec initialiseur explicite. Cela
  retire la dépendance inutile de son import à l'introspection de
  `dataclasses`, sans changer la grammaire ni l'API publique.
- **Passage final : succès, 9 tests sur 9, `OK`, code retour 0.** Le même
  vérificateur confirme moteur, erreurs, échantillonnage, SVG, CLI, sécurité et
  documentation.
