# Arbitrages MAIN — première solution

Le candidat MAIN est l'unique écrivain. L'orchestrateur expérimental a fourni
les avis consultatifs en lecture seule ; aucun agent supplémentaire n'est lancé.
Le challenge actif a été lu avant cette table, elle-même écrite avant le code.

Ordre des textes visibles reçus, conservés intégralement dans le message source
pour l'annexe verbatim du PV de l'orchestrateur expérimental :
1. SA-01 INITIAL — contrat et sécurité.
2. SA-02 INITIAL — conception et testabilité.
3. SA-01 CONTRADICTION — confrontation et corrections.
4. SA-02 CONTRADICTION — confrontation et révision.

I = avis initial ; C = contradiction. Les recommandations communes sont regroupées.

| Source | Recommandation | Décision motivée |
|---|---|---|
| SA-01 I, SA-02 I | Bibliothèque standard, grammaire fermée, consommation totale, aucune exécution dynamique | Retenue : lexeur dédié et analyse descendante ; aucune résolution libre de nom. |
| SA-01 I | Livrer uniquement moteur et README | Adaptée : ces livrables plus DECISIONS et traces de contrôles dans solution, demandés par le protocole MAIN. |
| SA-02 I | Séparer syntaxe, calcul, échantillonnage, SVG, CLI ; import sans effet | Retenue : représentation postfixée interne, exécution numérique itérative, garde main. |
| SA-01 I, SA-02 I | Puissance à droite, précédence sur unaire, exposant signé | Retenue : grammaire unary → signe unary ou power ; power → primary [^ unary]. |
| SA-01 I, SA-02 I | Décimaux .5 et 5., exposants signés, chiffres ASCII | Retenue : formes usuelles explicites ; rejet des autres caractères et suffixes. |
| SA-01 I, SA-02 I/C, SA-01 C | Fonctions à un argument, compositions autorisées ; pas d'appel indirect ni multiplication implicite | Retenue avec correction des avis initiaux : sin(cos(x)) est valide. |
| SA-01 I, SA-02 I | Seul x est variable ; constantes non redéfinissables | Retenue : clés inutilisées ignorées, valeur de x contrôlée uniquement si utilisée. |
| SA-01 I, SA-02 I | Float réel fini ; division par zéro distincte ; overflow en ValueError | Retenue : contrôle après chaque opération ; math.pow refuse les complexes. |
| SA-01 I, SA-02 I/C | Conventions 0^0, 0^-1, tan aux pôles | Retenue : 1, ValueError, et comportement math.tan sans seuil artificiel. |
| SA-01 I, SA-02 I/C, SA-01 C | Analyser une fois ; distinguer structure invalide et échec numérique | Retenue avec correction : sqrt(-1) produit tous les points à None, même sans dépendance à x. |
| SA-01 I, SA-02 I | Bornes finies croissantes, entier ≥ 2, booléens rejetés | Retenue : diagnostics explicites et contrat numérique sans ambiguïté. |
| SA-02 I, SA-01 C | Extrémités exactes et interpolation stable | Retenue : interpolation convexe si signes opposés ; différence sinon ; bornes assignées exactement. |
| SA-01 I/C, SA-02 I/C | Ne pas promettre toutes les asymptotes | Retenue : coupures sur points invalides ; heuristique de saut écartée car elle peut couper une fonction continue. |
| SA-01 I, SA-02 I/C | XML échappé, caractères interdits traités, coordonnées finies, aucun contenu actif | Retenue : structure SVG fixe et sérialisation XML standard ; remplacement des caractères XML interdits. |
| SA-01 I, SA-02 I/C | Échelles stables, marges, constantes, points isolés, rendu vide refusé | Retenue : normalisation avant soustraction, plage constante centrée, cercle isolé. |
| SA-02 I | Inclure zéro dans toute fenêtre | Écartée suivant SA-01 I/C et SA-02 C : compression excessive des données éloignées. |
| SA-01 I/C, SA-02 C | Axes ramenés au bord | Retenue : position bornée ; légende explicite si origine hors champ. |
| SA-01 I, SA-02 C | Limites de ressources raisonnables | Adaptée : longueur maximale 10 000 caractères et profondeur de syntaxe limitée par Python, convertie en ValueError ; pas de plafond arbitraire d'échantillons. Calcul float et pile numérique itérative. Limites documentées. |
| SA-01 I, SA-02 I/C | Valider document avant ouverture ; erreurs de chemin récupérables | Retenue : document entièrement construit avant écriture et OSError présenté par CLI. |
| SA-01 I, SA-02 I/C | Historique ordonné des réussites ; EOF et reprise après erreur | Retenue : ajout après succès, commandes de contrôle exclues, EOF propre. |
| Tous | Contrôles publics ciblés et documentation des conventions | Retenue : précédence, refus, domaines, SVG extrême et hostile, CLI ; aucun test de forme interne. |
| SA-01 I, SA-02 I | Vérificateur indépendant et corrections | Différée conformément à la phase : uniquement après SA-03 ; aucun verdict officiel revendiqué ici. |

## Trace synthétique

1. Demande : première solution V2, arbitrages préalables, aucun autre consultant.
2. Avis : quatre textes reçus dans l'ordre ci-dessus ; les consultants déclarent
   n'avoir utilisé aucun outil ni exécuté de contrôle.
3. Arbitrage : table ci-dessus ; code et contrôles candidats viennent ensuite.
4. SA-03 et vérification officielle : non exécutés dans cette phase.

Tokens et durée totale des consultants et du candidat : non enregistrés.
Aucune modification de gouvernance ; aucune opération Git autorisée dans ce run.

## Arbitrage final SA-03 — avant corrections

Cinquième texte consultatif reçu : SA-03 CRITIQUE, après la première solution.
Son texte visible intégral reste dans le relais utilisateur, après les quatre
avis précédents et le snapshot ; aucun nouvel échange consultant n'est demandé.
MAIN reste seul écrivain ; le relais et le PV relèvent de l'orchestrateur
expérimental. Les lignes historiques ci-dessus décrivent la première phase.

| Point SA-03 | Qualification | Justification et preuve disponible |
|---|---|---|
| Absence de défaut manifeste de sécurité/précédence ; corrections antérieures présentes | Retenu | Lecture du fichier actif : noms fermés, sérialisation ElementTree, postfixe, capture des erreurs numériques et ajout d'historique après succès. Ce constat statique ne prouve pas l'absence universelle de défaut. |
| Restriction à 10 000 caractères | Retenu | `_MAX_LENGTH` et rejet dans `_tokens` confirment le contre-exemple des 5 001 termes. Supprimer ce plafond absent du contrat. |
| Restriction de profondeur | Retenu | Les appels récursifs de `_Parser` imposent la limite Python. Remplacer la pile d'appels par une pile explicite conservant la même grammaire. |
| Contrôles du terminal réaffichés | Retenu | Message de réussite, historique et erreurs interpolent du texte brut. Échapper les caractères non imprimables lors de l'affichage seulement, sans changer le chemin transmis au système de fichiers. L'effet sur un terminal réel n'est pas démontré. |
| Récupération CLI partielle | Retenu | Lecture et commandes de contrôle sont hors du bloc d'erreurs des opérations. Ajouter une protection globale pour OSError/MemoryError et un diagnostic sur stderr ; terminer si le canal est défaillant pour éviter une boucle sans entrée exploitable. Une reprise universelle n'est pas possible. |
| Ressources non bornées de l'API | Écarté comme correction | Coût confirmé par les listes et le document matérialisés ; pas de limite contractuelle de samples. Garder le compromis documenté et 201 points en CLI, sans introduire un nouveau plafond arbitraire. Épuisement effectif non mesuré. |
| Perte du fichier en cas d'échec d'écriture | Écarté comme correction | `Path.write_bytes` n'est pas transactionnel ; risque déjà documenté. L'atomicité n'est pas exigée ; aucune panne de stockage constatée. |
| Couverture des 131 assertions historiques | Non vérifiable | Seule la sortie rapportée est conservée, pas le programme. Ne pas la réinterpréter comme une preuve indépendante ; conserver de nouveaux contrôles reproductibles pour les changements. |
| Vérificateur officiel nécessaire | Retenu | Aucun passage dans la première phase ; exécuter la commande exacte après les corrections et consigner premier passage et verdict final. |
| Axes au bord, cercle isolé, absence d'heuristique | Retenu | `_projection`, `draw` et légende correspondent aux conventions README ; pas de correction demandée par un défaut établi. |
| Arrondi de sqrt(2)^2 | Retenu | Le résultat flottant documenté suit math.sqrt et math.pow ; aucune exigence d'arrondi décimal. Aucun changement. |
| Fichiers de décisions et contrôles supplémentaires | Retenu | Le challenge fixe leur destination ; le mandat MAIN exige DECISIONS et la traçabilité. Aucun retrait. |
| Aucun défaut de projection établi | Retenu | Traitement explicite des plages constantes et normalisation dans `_projection`. Aucun changement ; ce constat n'est pas une preuve exhaustive. |

Les corrections retenues sont exclusivement les trois groupes langage,
affichage terminal et gestion des canaux CLI, plus leur documentation et leurs
contrôles. Les preuves d'exécution seront ajoutées après les contrôles.

## Preuves finales et clôture

- Langage : `controle_final.py::FinalChecks.test_long_and_deep_valid_expressions`
  réussit pour la somme de 5 001 termes, 3 000 parenthèses, 3 001 signes,
  1 500 compositions et 3 000 opérandes de puissance. La pile explicite de
  `_parse` remplace les appels récursifs ; le plafond `_MAX_LENGTH` est supprimé.
  L'arbitrage initial de restriction des ressources est donc révisé, sans
  modifier la trace historique. Les limites physiques de mémoire demeurent.
- Grammaire : `test_grammar_preserved` réussit sur les priorités, les erreurs,
  les nombres, les compositions et le domaine entièrement invalide.
- Terminal : `test_terminal_and_history` vérifie que le chemin transmis à
  `write_svg` reste intact, que le caractère ESC n'est pas réémis et que la
  session continue après une division par zéro. Aucun effet sur un terminal
  physique n'a été testé ; la preuve porte sur le texte émis par la CLI.
- Canaux : `test_failed_channels` réussit avec OSError et MemoryError simulés
  en lecture, erreurs de sortie sur help/history/clear et perte de stderr.
  La sortie contrôlée ne garantit pas la reprise lorsque les canaux sont perdus.
- Vérificateur officiel : premier passage après les corrections SA-03,
  9 tests réussis, `OK`, code de sortie 0. Verdict final identique au premier
  passage ; aucun défaut officiel à corriger et aucun second passage nécessaire.
  Commande exacte et sortie conservées dans CONTROLES.md.

Les quatre méthodes candidates réussissent (`Ran 4 tests`, `OK`, sortie 0).
Leur source est conservé dans solution/controle_final.py ; elles ne remplacent
pas le vérificateur indépendant et ne reconstituent pas les 131 assertions.
Aucune autre correction appliquée, aucune nouvelle consultation, aucune opération
Git. Tokens et durée globale de cette phase : non enregistrés. Durées affichées
par les suites : 0,037 s candidates et 0,046 s officielles ; ce ne sont pas les
durées du run. Aucune règle de gouvernance modifiée.
