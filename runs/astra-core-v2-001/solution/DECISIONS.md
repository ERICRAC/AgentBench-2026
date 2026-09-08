# Arbitrages — Calculator V2, première solution et phase finale

Les sections de première phase ci-dessous sont conservées comme trace historique.
La section « Phase MAIN finale » actualise les décisions et l'état du run.

Ce document a été créé avant le code, après lecture du `CHALLENGE.md` de la
tentative `astra-core-v2-001` et des quatre textes fournis dans le relais.
Les avis sont consultatifs ; leurs convergences ne constituent pas une preuve
de conformité. Aucune autre tentative, solution ou résultat n'a été consulté.

## Rôles et ordre des échanges observables

1. L'utilisateur mandate la phase MAIN : première solution, arbitrage préalable,
   contrôles ciblés possibles, vérificateur officiel réservé à la phase finale.
2. L'orchestrateur expérimental fournit **SA-01 INITIAL**, analyste du contrat
   et de la sécurité, puis **SA-02 INITIAL**, analyste de conception et de
   testabilité. Leur exécution indépendante est rapportée par le relais.
3. Il fournit ensuite **SA-01 CONTRADICTION**, puis **SA-02 CONTRADICTION**.
   Les quatre textes visibles sont conservés intégralement en annexe ci-dessous,
   dans cet ordre ; aucun nouvel échange avec un consultant n'a été lancé ici.
4. MAIN, agent candidat et unique écrivain, décide des arbitrages ci-dessous.
   L'orchestrateur expérimental est distinct du candidat. SA-03 doit intervenir
   après cette première solution ; sa critique n'est pas encore disponible.

## Table de décision préalable à l'implémentation

Les recommandations répétées sont regroupées avec leurs sources : I désigne
l'avis initial et C la contradiction. Les réserves des contradictions priment
sur les formulations initiales qu'elles corrigent.

| Réf. | Sources et recommandation | Décision motivée |
| --- | --- | --- |
| D01 | SA-01 I §1 ; SA-02 I §1, §6 et C §1 : livrables, bibliothèque standard, périmètre d'écriture | Retenue : `calculator.py` et `README.md` dans la solution active. Ajout de `DECISIONS.md` expressément demandé par la phase MAIN, qui contient aussi la trace ; la lecture limitant absolument à deux fichiers est écartée pour cette raison. Aucun changement aux tests, scripts ou gouvernance. |
| D02 | SA-01 I §1, C accords ; SA-02 I §1–2, C accords : séparer métier, parsing et console | Retenue : `calculate`, `parse_expression`, `main` dans un seul module. Le helper de parsing est un choix de testabilité, pas une obligation du challenge (réserve SA-01 C). Pas de classe ni de framework. |
| D03 | SA-01 I §1, §3 ; SA-02 I §2 ; les deux C : quatre opérations, signes, ordre et exceptions | Retenue : sélection explicite de `+`, `-`, `*`, `/`, calcul sans entrée-sortie ; `ValueError` si opérateur inconnu, `ZeroDivisionError` uniquement dans la branche division, également pour `-0.0`. Vérifier soustraction, division et opérateur inconnu avec zéro. |
| D04 | SA-01 I §2 ; SA-02 C compléments : types Python | Retenue : arguments numériques selon la signature, sans conversion générale de chaînes ou d'objets dans l'API. Les conversions textuelles appartiennent au parsing CLI. |
| D05 | SA-01 I §2–3 ; SA-02 I §3 ; les deux C : grammaire, espaces et signes | Retenue : exactement trois éléments séparés par des espaces blancs (`split`), espaces périphériques, multiples et tabulations acceptés. Formes compactes, parenthèses, chaînes d'opérations et contenu supplémentaire rejetés par cette grammaire documentée. L'idée qu'ils seraient expressément interdits par le challenge est écartée conformément à SA-02 C. |
| D06 | SA-01 I §2 ; SA-02 I §3–5 : sortie et ligne vide | Retenue : `quit` et `exit` après retrait des espaces périphériques, avec insensibilité à la casse facultative adoptée pour la commodité. Une ligne vide est une erreur de format, puis la boucle reprend. |
| D07 | SA-01 I §2 ; SA-02 I §6 : nombres et affichage | Retenue : conversion CLI par `float`, point décimal et notation scientifique documentés, pas de conversion de virgule. Affichage Python usuel sans arrondi ajouté ; tolérance pour les contrôles décimaux. |
| D08 | SA-01 I §2, C §4 ; SA-02 I §6 et C compléments : valeurs non finies | Retenue : conserver les comportements flottants Python, y compris `nan`, `inf` et débordements flottants, sans rejet additionnel ni nouvelle exception métier. Documenter cette politique, qui est un choix hors exigences explicites. |
| D09 | SA-01 I §4 ; SA-02 I §2 ; SA-01 C précision : données jamais exécutées | Retenue : opérations explicites, aucune évaluation de code, commande système ou résolution arbitraire. La réserve SA-01 C sur les tables fixes est acceptée ; une telle table serait admissible mais n'est pas nécessaire ici. Aucun usage de `eval`, `exec` ou `compile`. |
| D10 | SA-01 I §1, §4 ; SA-02 I §4 ; SA-01 C réserves : erreurs CLI | Retenue : intercepter seulement les erreurs attendues de format, nombre, opérateur et zéro ; messages explicites puis reprise. Aucun libellé exact n'est présenté comme imposé par le contrat. Les exceptions ne sont pas remplacées par des chaînes dans `calculate`. |
| D11 | SA-01 I §3 ; SA-02 I §1 ; les deux C : import sans interaction | Retenue : garde `if __name__ == "__main__"`, import silencieux contrôlé sans lecture de l'entrée. |
| D12 | SA-01 I §4 ; SA-02 I §4 ; les deux C : EOF et interruption clavier | Retenue comme robustesse facultative : EOF termine normalement, interruption clavier termine sans traceback. Ne pas présenter ces comportements comme des exigences explicites. |
| D13 | SA-01 I §4 ; SA-02 C §4 : limites de taille | Retenue : aucune limite numérique ou de longueur arbitraire ajoutée. La résistance à l'épuisement de ressources n'est pas garantie par ce petit outil et n'est pas une exigence établie. |
| D14 | SA-01 I §3, §5 ; SA-02 I §5 ; les deux C : contrôles observables | Retenue : contrôler les quatre opérations, ordre, signes, décimaux avec tolérance, zéros, exceptions, import et sessions CLI avec erreurs suivies de réussite, sorties et EOF. Contrôles ponctuels sans fichier de tests ajouté ; pas de modification du vérificateur. |
| D15 | SA-01 I §3 ; SA-02 I §6 ; les deux C : documentation | Retenue : expliquer les chemins réels de lancement depuis la racine et le dossier solution, API, syntaxe, exemples, erreurs et choix non imposés. |
| D16 | SA-01 I §5 ; SA-02 I §5–6 ; les deux C : vérification officielle et corrections | Différée, et non abandonnée : la phase MAIN interdit ce lancement avant SA-03. Commande de phase finale : `python3 scripts/verify.py --solution runs/astra-core-v2-001/solution` depuis la racine. Le verdict indépendant reste à établir. |
| D17 | SA-01 I §1, §5 ; SA-02 I conclusion ; les deux C : pas d'intervention humaine ni de Git | Retenue : décisions prises dans le périmètre autorisé, aucun autre agent lancé, aucune opération Git. Le relais expérimental conserve la responsabilité des consultations et du PV du run. |

## Traçabilité de cette phase

5. MAIN écrit `calculator.py` et `README.md` après la table préalable, et
   conserve les quatre textes relayés dans l'annexe de ce document.
6. MAIN exécute deux scripts ponctuels par `python3 -B -` depuis le dossier
   solution, sans créer de fichier de tests. Le premier importe le module et
   contrôle l'API et le parsing ; le second lance sept processus CLI par
   `subprocess.run([sys.executable, '-B', 'calculator.py'], ...)`, chacun avec
   un délai maximal de cinq secondes. Les deux scripts terminent avec le code
   0. Les assertions sur les messages servent à vérifier cette implémentation
   et n'ajoutent aucune exigence au contrat officiel.
7. Tous les contrôles ciblés passent ; aucune correction fonctionnelle n'est
   nécessaire à la suite de ces contrôles. MAIN consigne leur résultat puis
   livre la première solution pour SA-03. Aucune critique SA-03 ni vérification
   officielle n'a été effectuée dans cette phase.

| Contrôle candidat | Résultat observé |
| --- | --- |
| Import avec saisie interdite et capture des sorties | Import sans appel à `input`, stdout et stderr vides. |
| 12 calculs | Quatre opérations, ordre, signes, décimaux et résultats nuls corrects ; comparaison avec `math.isclose`, tolérances relative et absolue de `1e-12`. |
| 6 opérateurs inconnus avec zéro à droite | `**`, `//`, `%`, chaîne vide, `plus` et ` + ` lèvent tous `ValueError`. |
| 3 représentations de zéro comme diviseur | `0`, `0.0` et `-0.0` lèvent `ZeroDivisionError`. |
| 5 contrôles de parsing et valeurs spéciales | Espaces/tabulations, notation scientifique, conversion de `1e999`, propagation de NaN et débordement de multiplication flottante conformes aux choix documentés. |
| 10 expressions invalides | Ligne vide, forme compacte, parenthèses, chaîne d'opérations, opérande manquant, nombres invalides à gauche et à droite, virgule décimale, suffixe et texte d'appel Python lèvent `ValueError`. |
| Interruption clavier simulée | `main` termine normalement lorsqu'`input` lève `KeyboardInterrupt`. Un véritable signal terminal n'a pas été testé. |
| Session mixte | Résultats `5.0`, `10.0`, deux erreurs entre les calculs, arrêt à `quit` avant le calcul suivant. |
| Session exit | Une erreur de division par zéro puis `3.5`, arrêt à `exit` avant le calcul suivant. |
| Session entrées invalides | Cinq erreurs puis résultat `5.0`, attestant la reprise. |
| Session espaces et casse | Résultat `6.0` puis arrêt à `  EXIT  ` avant le calcul suivant. |
| EOF après calcul, immédiat et après erreur | Respectivement résultat `-500.0`, aucune expression, et une erreur de format ; les trois sessions terminent. |
| Ensemble des sept processus CLI | Tous terminent avec code 0, stderr vide et aucun traceback en stdout ; résultats et nombres d'erreurs vérifiés. |

Ces contrôles ne remplacent pas le verdict officiel. Les tokens et la durée
totale de phase sont non enregistrés ; aucune mesure globale n'est reconstruite.
Aucun horodatage de travail n'est publié. Aucune évolution de gouvernance n'est
effectuée pendant cette tentative. Aucune opération Git n'a été lancée.

La suite revient au relais expérimental : transmettre à SA-03 le challenge,
`calculator.py`, `README.md` et cette table, puis fournir sa critique à MAIN.
La phase finale pourra arbitrer cette critique et lancer la commande officielle
indiquée en D16, avec correction des défauts confirmés si nécessaire.

## Phase MAIN finale — arbitrage de SA-03 avant vérification

8. L'utilisateur mandate une nouvelle session éphémère du même rôle MAIN,
   candidat orchestrateur et unique écrivain. Il demande explicitement de
   compléter `solution/DECISIONS.md`, d'arbitrer SA-03 et de lancer exactement
   `python3 scripts/verify.py --solution runs/astra-core-v2-001/solution`.
   Aucun nouveau consultant n'est autorisé ni sollicité. L'orchestrateur
   expérimental fournit le cinquième texte, **SA-03 CRITIQUE**, après la première
   solution. SA-01 analyse le contrat et la sécurité ; SA-02 la conception et
   la testabilité ; SA-03 les cas limites. Ces trois rôles restent consultatifs.
9. MAIN relit le `CHALLENGE.md` de la tentative active, les trois fichiers de
   solution, les règles de restitution et de journalisation et le script officiel.
   Le code et les documents lus correspondent à la première solution relayée.
   `python3 --version` retourne `Python 3.13.5` (code 0). MAIN arbitre ci-dessous
   avant tout lancement officiel ; aucune correction fonctionnelle n'est retenue.

| Réf. SA-03 | Qualification | Justification, preuve et action |
| --- | --- | --- |
| Introduction et §1 : absence de défaut confirmé, constats favorables | Retenu | Lecture de `calculator.py` : branches explicites dans `calculate`, contrôle du zéro seulement pour `/`, `split()` et longueur 3 dans `parse_expression`, interceptions dans la boucle, commandes de sortie et garde d'import. Aucun import ni exécution dynamique dans le module. Cela confirme les constats statiques, sans suffire à prononcer le verdict officiel. Code conservé. |
| §2 : résultat entier possible avec arguments entiers | Retenu | Les retours `left + right`, `left - right` et `left * right` conservent l'arithmétique Python ; l'exemple `calculate(2, "+", 3) # 5` du README le décrit. L'annotation seule ne réalise aucune conversion. Le challenge ne demande pas explicitement un contrôle strict du type concret des résultats. |
| §2 : imposer une conversion systématique en `float` | Écarté | Aucun défaut établi ; D04 et D07 conservent les opérations numériques natives. Une conversion modifierait notamment la précision des résultats entiers. Le risque hypothétique d'une assertion stricte sera confronté au passage officiel, sans anticiper une exigence absente. |
| §3 : dépendance à Python 3.9 ou ultérieur | Retenu | `tuple[float, str, float]` est une annotation évaluée au chargement ; le README annonce Python 3.9 minimum. La commande de version observe Python 3.13.5 dans l'environnement actif. Aucun correctif de compatibilité n'est retenu. |
| §3 : échec effectivement observé sous Python 3.8 | Non vérifiable | Aucun interpréteur 3.8 n'a été lancé ; l'incompatibilité décrite est une propriété statique connue, pas un résultat d'exécution de cette session. Aucun support 3.8 n'est revendiqué. |
| §4 : autorisation actuelle de la trace et nécessité du vérificateur | Retenu | Le mandat final visible demande « complète `solution/DECISIONS.md` » et « Exécute ensuite le vérificateur officiel exactement ainsi ». Il autorise donc directement la trace et l'exécution finale. D16 est désormais mis en œuvre ; le report historique reste conservé. La suppression de la trace est écartée. |
| §4 : preuve directe du mandat de première phase | Non vérifiable | Ce mandat original n'est pas reproduit intégralement dans cette session. D01, D16 et le relais en rapportent la teneur ; l'autorisation présente n'est pas utilisée pour reconstruire rétroactivement une preuve manquante. |
| §5 : limites de ressources, erreurs d'entrée-sortie et messages fixes | Retenu | `input` charge la ligne et `split` la découpe sans plafond ; les interceptions portent sur EOF, interruption clavier, `ValueError` et `ZeroDivisionError`, pas sur les erreurs d'entrée-sortie. Les messages d'erreur sont fixes, sans interpolation de la saisie. Ces limites sont reconnues et ajoutées au README. |
| §5 : plafonnement arbitraire ou interception générale | Écarté | Aucun besoin contractuel ni défaut confirmé ne justifie ces changements ; D10 et D13 restent applicables. Aucun essai d'épuisement mémoire ou de tube fermé n'est réalisé, et aucune résistance à ces conditions n'est revendiquée. |
| §6 : conserver les choix de syntaxe et de flottants | Retenu | Le README documente trois éléments séparés par des blancs, le point décimal, les non-finis et le sous-débordement. Le code réalise ces choix via `split`, `float` et l'affichage ordinaire. |
| §6 : syntaxe compacte, rejet des non-finis, arrondi, virgule ou validation générale des types | Écarté | Ces extensions ou restrictions ne corrigent aucun défaut démontré du contrat. Pas de modification fonctionnelle. |
| Conclusion : authenticité indépendante des contrôles ciblés antérieurs et régression | Non vérifiable | La trace historique fournit une synthèse, mais pas les scripts et sorties brutes ; elle reste qualifiée de résultat rapporté dans cette session. Aucune comparaison de régression n'est établie. Aucune autre tentative n'est consultée. |
| Conclusion : priorité au vérificateur officiel | Retenu | La phase finale l'autorise et l'exige. Le premier passage et le verdict final seront consignés à la suite de cette table avec la sortie effectivement observée. |
| Déclaration finale : consultation SA-03 sans outil, fichier, test, sous-agent ni Git | Non vérifiable | Déclaration du consultant relayée textuellement ; MAIN ne dispose pas de sa trace d'exécution indépendante. Dans la présente session MAIN, aucun consultant ou sous-agent n'est lancé et aucune opération Git n'est effectuée. |

Corrections retenues à ce stade : documentation et traçabilité uniquement,
pour actualiser l'état de phase et expliciter les limites relevées au §5.
`calculator.py` reste inchangé. Les arbitrages ne transforment pas les
préférences des consultants en nouvelles exigences du challenge.

## Annexe — textes visibles relayés

Le bilan final figure après les cinq textes, afin de conserver leur ordre.

Les quatre avis sont reproduits ci-après dans l'ordre du message de lancement.

### SA-01 INITIAL

Avis SA-01 fondé uniquement sur le challenge fourni. Aucune consultation du dépôt, exécution, modification ou délégation. Le contrat permet une réalisation simple ; les principaux arbitrages concernent la grammaire des entrées et les valeurs numériques particulières.

1. **Obligations à retenir**

   - Livrer exclusivement `calculator.py` et `README.md` dans `solution/`, avec logique métier et CLI dans le premier, lancement, utilisation et exemples dans le second.
   - Exposer `calculate(left: float, operator: str, right: float) -> float` et prendre en charge exactement les quatre opérateurs annoncés.
   - Accepter les nombres entiers, décimaux et négatifs ; lever `ValueError` pour un opérateur inconnu et `ZeroDivisionError` pour une division par zéro.
   - Ne jamais employer `eval()` ou `exec()` ; utiliser uniquement la bibliothèque standard.
   - Lancer une boucle interactive avec la commande indiquée ; reconnaître `quit` et `exit`.
   - Pour une expression invalide ou une division par zéro, afficher une erreur compréhensible sans traceback, puis permettre une nouvelle saisie.
   - Ne modifier ni cahier des charges ni tests et ne solliciter aucune intervention humaine hors autorisation système.

   **Recommandation :** distinguer explicitement les deux interfaces. Les exceptions prescrites appartiennent au contrat Python ; leur traduction en messages appartient à la CLI. Retourner un message d’erreur depuis `calculate` compromettrait ce contrat.

2. **Ambiguïtés nécessitant un arbitrage**

   | Sujet | Lecture du contrat | Recommandation |
   |---|---|---|
   | Espaces | L’exemple contient trois éléments séparés par des espaces ; les variantes ne sont pas définies. | Accepter les espaces périphériques, multiples et les tabulations. Considérer les formes compactes comme `2+3` hors périmètre minimal. |
   | Grammaire | Une ligne représente une opération binaire. | Rejeter les opérandes manquants, éléments supplémentaires, parenthèses et opérations chaînées. Ne pas ajouter de priorité opératoire. |
   | Commandes de sortie | Seuls `quit` et `exit` sont cités. | Les reconnaître après retrait des espaces périphériques. La reconnaissance des majuscules reste facultative. |
   | Ligne vide | Aucun comportement spécifique. | La traiter comme une expression invalide et poursuivre la boucle. |
   | Décimaux | Le séparateur et la notation scientifique ne sont pas précisés. | Documenter le point décimal. Ne pas ajouter de conversion implicite de la virgule. L’acceptation de notation scientifique reste compatible avec le contrat. |
   | Valeurs non finies | `NaN`, les infinis et les débordements ne sont pas spécifiés. | Les identifier comme un choix de politique numérique ; ne pas inventer une obligation de rejet ni étendre silencieusement les exceptions de l’API. |
   | Types à l’appel Python | Les annotations donnent les types attendus sans définir les appels hors contrat. | Garantir les entrées numériques annoncées, sans imposer une conversion générale de chaînes ou d’objets. |
   | Présentation du résultat | Aucune chaîne de sortie exacte n’est prescrite. | Préférer un affichage numérique simple et éviter les arrondis arbitraires. |

   Ces arbitrages peuvent être pris et documentés par le candidat sans intervention humaine.

3. **Erreurs fonctionnelles prioritaires**

   - **Confusion entre signe et opérateur :** une valeur négative doit rester un opérande valide, y compris à droite.
   - **Zéro signé :** une division par `-0.0` constitue également une division par zéro.
   - **Validation incomplète :** une ligne contenant une expression valide suivie de contenu supplémentaire doit être rejetée intégralement.
   - **Perte de continuité :** un message d’erreur correct ne suffit pas si le programme termine ensuite ou ne traite plus les saisies.
   - **Import déclenchant la CLI :** l’exposition d’une fonction réutilisable appelle une séparation du lancement interactif ; importer le module ne devrait pas attendre une saisie.
   - **Chemins de lancement :** distinguer dans le README le lancement depuis la racine du dépôt et depuis le dossier de solution.

4. **Surfaces d’attaque et robustesse**

   **Priorité élevée :** traiter les saisies comme des données. Aucune entrée ne doit devenir du code Python, une commande système ou un nom de fonction résolu dynamiquement. L’interdiction d’`eval()` et d’`exec()` ne justifie pas un mécanisme d’exécution équivalent.

   **Priorité élevée :** contenir les erreurs attendues à la frontière CLI. Une capture trop étroite peut exposer un traceback ; une capture générale peut masquer des défauts internes et gêner l’arrêt du programme.

   **Priorité moyenne :** terminer proprement à la fin de l’entrée standard. Continuer indéfiniment après EOF provoquerait une boucle inutile. La gestion propre d’une interruption clavier est également souhaitable, mais n’est pas explicitement exigée.

   **Priorité secondaire :** les entrées démesurées peuvent consommer des ressources. Le challenge ne fixe aucune limite ; éviter d’ajouter une restriction arbitraire aux nombres valides sans besoin démontré.

5. **Vérification et décision proposées**

   Retenir le périmètre minimal : opération binaire, quatre opérateurs, erreurs explicites et boucle persistante. Vérifier particulièrement une séquence mêlant calcul valide, erreur de syntaxe, division par zéro, nouveau calcul valide et sortie.

   La commande officielle doit être exécutée par le candidat depuis la racine du dépôt, avec l’identifiant réel de la tentative. **Aucun résultat de vérification n’est disponible dans cet avis** ; le verdict technique demeure celui du vérificateur indépendant. Aucune livraison Git ne relève de cette consultation.

### SA-02 INITIAL

Avis SA-02 : privilégier une architecture minimale, avec une fonction métier indépendante de la console et une boucle CLI responsable de la saisie, des messages et de la reprise après erreur.

1. **Structure recommandée — à retenir**

   Dans `calculator.py`, distinguer trois responsabilités : calculer une opération, interpréter une ligne et piloter la boucle interactive. Une petite fonction de lecture d’expression peut rendre la conversion des nombres testable, sans introduire de classes ni de framework.

   Protéger le lancement de la CLI par le garde Python habituel : importer le module doit permettre d’appeler `calculate` sans attendre une saisie ni produire de sortie.

   **Arbitrage :** retenir cette séparation légère. Une architecture à plusieurs modules serait disproportionnée et dépasserait les livrables demandés.

2. **Invariants métier — obligatoires**

   `calculate` doit :
   - reconnaître exactement les quatre opérateurs annoncés ;
   - préserver l’ordre des opérandes, particulièrement pour la soustraction et la division ;
   - accepter les nombres négatifs et décimaux ;
   - lever `ValueError` pour tout opérateur inconnu ;
   - lever `ZeroDivisionError` lorsque le diviseur vaut zéro, y compris `-0.0` ;
   - rester indépendante de toute entrée ou sortie console.

   Une sélection explicite de l’opération suffit. Aucune évaluation dynamique n’est nécessaire.

   **Arbitrage sensible :** contrôler la validité de l’opérateur avant une éventuelle vérification du diviseur. Avec un opérateur inconnu et un opérande droit nul, l’erreur pertinente reste `ValueError`. Ne pas transformer les exceptions métier en chaînes de caractères : leur présentation appartient à la CLI.

3. **Syntaxe CLI — fixer un périmètre conservateur**

   La forme documentée comprend deux nombres et un opérateur. Une séparation sur les espaces blancs permet de gérer naturellement plusieurs espaces, les tabulations et les espaces périphériques. Vérifier qu’il existe exactement trois éléments avant de convertir les opérandes.

   Les nombres négatifs doivent être traités comme des opérandes signés : `-2 * -3` constitue un cas essentiel. Découper la ligne directement sur les caractères d’opération risquerait de confondre signe et opérateur.

   **Arbitrage :** documenter la forme avec espaces. Le challenge n’impose pas explicitement `2+3`, les parenthèses ou les expressions composées ; leur prise en charge ajouterait une grammaire inutile.

   Reconnaître `quit` et `exit` sur la ligne entière après retrait des espaces périphériques. L’insensibilité à la casse est une commodité facultative.

4. **Gestion des erreurs et terminaison — obligatoires et recommandées**

   Les erreurs de format, de conversion numérique, d’opérateur et de division par zéro doivent produire un message compréhensible, puis rendre la main à la boucle. Distinguer au minimum « expression invalide » et « division par zéro ».

   Limiter les interceptions aux exceptions attendues. Une capture générale pourrait masquer un défaut de programmation tout en donnant l’apparence d’une CLI robuste.

   **Arbitrage :** traiter également la fin de l’entrée standard comme une sortie normale. Ce comportement facilite l’utilisation par redirection et les vérifications automatisées. Une sortie propre sur interruption clavier est utile, mais secondaire par rapport aux obligations explicites.

5. **Validation — prioriser les comportements observables**

   Pour la fonction métier, couvrir les quatre opérations, les signes, les décimaux, les résultats nuls, les divisions non entières, les opérateurs inconnus et les deux représentations signées du zéro comme diviseur. Comparer les résultats décimaux avec une tolérance adaptée aux flottants.

   Pour la CLI, utiliser des sessions complètes, notamment :
   - erreur de syntaxe, puis calcul valide, puis `quit` ;
   - division par zéro, puis calcul valide, puis `exit` ;
   - ligne vide, nombre invalide et nombre incorrect d’éléments ;
   - fin de fichier sans commande de sortie.

   Vérifier les résultats, l’absence de traceback, la poursuite effective après erreur et la terminaison du processus. Éviter d’imposer un libellé exact de message ou d’invite que le contrat ne fixe pas.

   **Arbitrage :** ne pas ajouter de fichier de tests aux deux livrables autorisés ni modifier les tests existants. L’agent principal doit exécuter la commande officielle depuis la racine du dépôt ; le verdict technique appartient au vérificateur indépendant.

6. **Points ouverts et livraison**

   Le contrat ne précise ni le format exact des résultats ni le traitement de `NaN` et des infinis. Éviter d’ajouter des restrictions sans nécessité démontrée. Le README doit expliquer le lancement, la syntaxe retenue, les sorties et la reprise après erreur, avec quelques exemples représentatifs.

   Priorité d’exécution : fonction métier, interprétation des lignes, boucle résiliente, documentation, vérification officielle et correction des défauts confirmés.

Cet avis repose uniquement sur le challenge fourni. Aucun outil, dépôt, test ou sous-agent n’a été utilisé ; aucune modification ni opération Git n’a été effectuée.

### SA-01 CONTRADICTION

Je confirme l’essentiel de l’avis SA-02 et révise deux formulations de mon avis initial. Cette confrontation repose uniquement sur les deux avis reproduits ; le texte du challenge n’est pas présent ici, donc leur concordance ne constitue pas une vérification indépendante du contrat.

**Accords et doublons.** Les deux avis convergent sur la séparation entre fonction métier et CLI, les exceptions prescrites, les opérandes négatifs, le zéro signé, le rejet intégral des expressions mal formées, la reprise après erreur et l’absence d’exécution dynamique. Ils recommandent également un import sans lancement interactif, une syntaxe documentée avec espaces et des vérifications portant sur les comportements observables. Ces recommandations peuvent être regroupées : leur répétition n’ajoute pas de preuve.

**Apports utiles de SA-02.** La préservation de l’ordre des opérandes mérite une vérification explicite pour la soustraction et la division. L’opérateur inconnu associé à un opérande droit nul constitue aussi un cas discriminant : la présence de zéro ne doit pas provoquer une erreur de division lorsqu’aucune division valide n’est demandée. Enfin, les comparaisons avec une tolérance adaptée aux flottants évitent de confondre représentation numérique et défaut fonctionnel.

**Révisions et réserves.** Aucun désaccord fonctionnel majeur n’apparaît. Deux distinctions doivent néanmoins rester explicites :

- Une fonction dédiée à l’interprétation des lignes est une option d’organisation, pas une obligation contractuelle établie.
- La sortie propre sur EOF reste une recommandation de robustesse d’après les textes fournis. De même, distinguer les messages selon leur cause est utile, mais ne permet pas d’imposer deux libellés précis.

Je précise aussi ma formulation sur les noms de fonctions résolus dynamiquement : le risque concerne la résolution arbitraire pilotée par l’entrée. Une table fixe associant les quatre opérateurs autorisés à des opérations connues ne constitue pas, à elle seule, une surface d’exécution arbitraire.

**Priorités consolidées.**

1. Respecter le contrat métier et les interdictions : opérations autorisées, exceptions correctes, absence d’exécution des saisies et de dépendance interdite.
2. Garantir les comportements CLI : validation complète, messages compréhensibles, continuité après erreur et sorties demandées.
3. Vérifier les cas discriminants : signes, ordre des opérandes, opérateur inconnu avec zéro, import et session mêlant erreurs et réussites.
4. Documenter les arbitrages non imposés : espaces, valeurs non finies, affichage et EOF ; éviter les restrictions arbitraires.

Aucun contrôle n’a été exécuté dans cette consultation. La vérification officielle et le verdict indépendant restent à établir ; aucune modification ni opération Git n’a été effectuée.

### SA-02 CONTRADICTION

Je confirme la convergence des deux avis et révise un point de formulation : les choix de syntaxe proposés constituent un périmètre d’implémentation raisonnable, mais les textes cités ne permettent pas de les présenter tous comme des obligations explicites du challenge.

**Accords et doublons.** Nous recommandons la même séparation légère : calcul sans entrée-sortie, interprétation d’une ligne, puis boucle interactive. Les exceptions métier doivent rester des exceptions dans `calculate` et devenir des messages à la frontière CLI. La protection du lancement à l’import, les opérandes négatifs, le zéro signé et la reprise après erreur sont également consensuels. Ces répétitions peuvent être fusionnées en une seule liste d’invariants ; elles ne justifient ni davantage de modules ni plusieurs campagnes de tests équivalentes.

**Désaccord utile sur la portée de la grammaire.** SA-01 recommande de rejeter explicitement les formes compactes, parenthèses et opérations chaînées ; mon avis les considère hors périmètre minimal. La conséquence pratique peut être identique avec une lecture en trois éléments, mais la justification doit rester précise : documenter la syntaxe retenue, puis rejeter les lignes qui ne la respectent pas. Éviter d’affirmer que le contrat interdit expressément chaque variante non décrite. La validation doit mesurer les exigences établies, sans transformer une préférence de lecture en contrainte supplémentaire du vérificateur.

**Compléments à retenir.** SA-01 précise utilement que les annotations de types n’imposent pas une conversion générale des arguments Python et qu’un affichage simple évite les arrondis arbitraires. Je maintiens aussi la priorité de l’erreur d’opérateur : un opérateur inconnu accompagné d’un opérande droit nul doit conduire à `ValueError`. Le contrôle du zéro ne concerne que la division. Sur les valeurs non finies, aucun désaccord : ne pas ajouter de politique restrictive sans fondement contractuel.

**Priorités consolidées.**

1. **Contrat métier et livrables.** Garantir les quatre opérations, l’ordre des opérandes, les exceptions prescrites et l’indépendance de la console ; respecter les fichiers autorisés et l’interdiction d’évaluation dynamique.
2. **Continuité observable de la CLI.** Vérifier une session réunissant calcul valide, erreur de syntaxe, division par zéro, nouveau calcul valide et sortie. Le traitement effectif du calcul suivant établit la reprise ; l’affichage d’un message seul ne suffit pas.
3. **Cas sensibles ciblés.** Vérifier signes des deux opérandes, décimaux avec tolérance adaptée, `-0.0`, opérateur inconnu avec zéro à droite, éléments supplémentaires et import sans interaction. Contrôler aussi la terminaison à EOF, recommandation utile pour l’automatisation.
4. **Documentation et vérification officielle.** Expliquer syntaxe, lancement et erreurs, puis exécuter la commande officielle dans le contexte prescrit. Majuscules des commandes, interruption clavier et limites de taille restent secondaires.

Les deux avis suffisent à établir ces recommandations, mais aucun résultat d’exécution ne permet de confirmer une conformité réelle. Cette consultation repose exclusivement sur les textes intégrés au message ; aucun outil, fichier, sous-agent ou acte Git n’a été utilisé.

### SA-03 CRITIQUE

La lecture statique ne révèle **aucun défaut fonctionnel confirmé sur les exigences explicites**. La première solution paraît cohérente avec les arbitrages retenus ; sa conformité officielle reste à établir.

1. **Constats favorables confirmés par le code.** Les quatre opérations préservent l’ordre des opérandes. Un opérateur inconnu conduit à `ValueError`, même avec zéro à droite. La division vérifie également `-0.0`. Le découpage en exactement trois éléments préserve les signes et rejette les suffixes ou expressions composées. Les erreurs attendues sont interceptées dans la boucle, qui continue après leur affichage. Les commandes de sortie, EOF et le garde d’import sont correctement placés. Aucun mécanisme d’exécution des saisies, accès système ou dépendance externe n’apparaît.

2. **Risque d’interprétation du contrat — type du résultat.** Avec deux arguments entiers, `calculate(2, "+", 3)` retourne un `int`, malgré l’annotation `-> float`. Ce comportement est observable dans le code et reconnu dans le README. Il ne constitue pas automatiquement une violation : les annotations Python permettent couramment l’emploi d’entiers là où des flottants sont attendus. Toutefois, une exigence de résultat strictement de type `float` ferait échouer les branches addition, soustraction et multiplication sur des entiers. Le challenge ne précise pas cette distinction ; ne pas transformer cette ambiguïté en défaut certain ni imposer une conversion sans arbitrage.

3. **Risque de compatibilité — version minimale.** L’annotation `tuple[float, str, float]`, évaluée au chargement, nécessite Python 3.9 ou ultérieur. Sur Python 3.8, le module échouerait avant même de lancer la CLI, avec traceback. Le README annonce correctement cette limite ; le challenge ne fixe aucune version minimale au-delà de `python3`. C’est donc une dépendance à l’environnement à confronter au vérificateur, pas un échec établi dans l’environnement réel.

4. **Point de traçabilité ouvert — fichier supplémentaire et vérification différée.** D01 rapporte une autorisation explicite d’ajouter `DECISIONS.md`, et D16 rapporte une interdiction temporaire de lancer le vérificateur. Le mandat MAIN correspondant n’est pas reproduit directement dans les pièces fournies : ces éléments restent des autorisations rapportées. Leur absence du dossier de consultation ne prouve aucune infraction. De plus, « créer exclusivement dans le dossier `solution/` » ne signifie pas sans ambiguïté « créer seulement deux fichiers ». Il serait injustifié d’exiger ici la suppression de la trace. La vérification officielle demeure néanmoins nécessaire avant de conclure le run ; son report annoncé n’est pas un défaut de cette première phase.

5. **Risques résiduels de robustesse, sans faille de sécurité confirmée.** Une ligne démesurée est chargée entièrement puis découpée sans limite ; elle peut épuiser les ressources. D13 reconnaît déjà cette limite, et aucun besoin contractuel ne justifie actuellement un plafonnement arbitraire. Les erreurs d’entrée-sortie, telles qu’un tube de sortie fermé, ne sont pas interceptées. Elles peuvent interrompre le programme, mais ne relèvent pas des erreurs d’expression que le challenge exige de contenir. Les messages fixes n’exposent pas directement le contenu hostile saisi.

6. **Préférences à ne pas convertir en corrections obligatoires.** Accepter `2+3`, rejeter `nan` ou `inf`, arrondir les résultats, accepter la virgule décimale ou ajouter une validation générale des types modifierait le périmètre choisi sans nécessité démontrée. Les limites des flottants, notamment le sous-débordement vers zéro, sont explicitement documentées.

Les contrôles ciblés sont **rapportés**, sans scripts ni sorties brutes permettant leur examen indépendant. Ils couvrent les principaux cas discriminants annoncés. Aucune régression ne peut être établie sans version antérieure comparable. La priorité restante est le vérificateur officiel, puis l’arbitrage de ses éventuels échecs au regard du contrat.

Avis SA-03 fondé uniquement sur les textes transmis ; aucun outil, fichier, sous-agent, test ou acte Git utilisé.

## Bilan final — contrôles et clôture MAIN

10. MAIN complète la table d'arbitrage de chaque point SA-03 avant vérification,
    conserve sa critique intégralement après les quatre avis antérieurs et
    actualise le README. Seules les précisions documentaires retenues sont
    appliquées ; aucune modification de `calculator.py` n'est nécessaire.
11. MAIN lance depuis la racine du dépôt la commande exacte ci-dessous.
    La variable d'environnement `PYTHONDONTWRITEBYTECODE=1` est exportée au
    préalable pour éviter la création de caches Python hors de `solution/`.
    Aucun argument ni script du vérificateur n'est modifié.

```bash
python3 scripts/verify.py --solution runs/astra-core-v2-001/solution
```

Premier passage officiel observé, sortie capturée :

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

12. Le processus termine avec le code **0**. Premier passage : **6 tests réussis,
    OK**. Verdict final : **OK**, identique au premier passage ; un seul passage
    officiel est réalisé dans cette session. Aucun défaut confirmé, aucune
    correction fonctionnelle ni nouvelle exécution nécessaire. MAIN ajoute
    ensuite uniquement le présent résultat et l'état final du README.

### Portée des preuves et limites

- Le verdict appartient au vérificateur officiel ; il établit la réussite des
  six contrôles exécutés. Il ne prouve pas une résistance à toutes les entrées
  démesurées, aux erreurs d'entrée-sortie ou une compatibilité Python 3.8.
- Le passage réussit sous Python 3.13.5 avec les retours numériques natifs.
  Il ne tranche pas à lui seul l'interprétation abstraite d'une exigence de
  résultat strictement `float` ; aucune telle correction n'est requise par
  les résultats observés. Python 3.9 minimum reste documenté.
- Les contrôles ciblés de première phase sont des résultats rapportés dans
  cette nouvelle session ; leurs sorties brutes ne sont pas disponibles ici.
  Le véritable signal Ctrl+C, le tube fermé et l'épuisement de ressources ne
  sont pas testés dans cette phase finale.
- Les textes SA-01 INITIAL, SA-02 INITIAL, SA-01 CONTRADICTION,
  SA-02 CONTRADICTION et SA-03 CRITIQUE sont conservés dans cet ordre,
  sans nouvel échange candidat-consultant. Le relais expérimental reste
  responsable de l'assemblage du PV du run ; les entrées numérotées de cette
  trace en fournissent la synthèse observable.
- Les tokens et la durée totale de cette session, des consultations et du run
  sont **non enregistrés** dans les éléments disponibles. La durée `0.010s`
  est celle annoncée par la suite de tests uniquement, pas celle du run.
- Aucun autre run, solution ou résultat n'est consulté. Les écritures de cette
  phase portent uniquement sur `DECISIONS.md` et `README.md` dans la solution
  active ; le code, le challenge, les tests, les scripts et la gouvernance
  restent inchangés. Aucune opération Git n'est effectuée.
- Aucun contrôle officiel ne reste en échec et aucune correction n'est en
  attente. Aucune évolution de gouvernance n'est proposée : les réserves de
  preuve sont déjà couvertes par les règles de traçabilité existantes.
