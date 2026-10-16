# Défi proposé — calculatrice scientifique modulaire

Instruction candidat canonique. **Brouillon non gelé ; aucun run autorisé.**
Identifiant de défi proposé : `modular-calculator-001`. Les anciens défis
restent indépendants. Cette version doit encore passer le jalon d'expertise.

## Livrables et contraintes

Livrer `engine.py`, `presentation.py`, `cli.py`, `README.md` dans `solution/`.
Python 3.11 ou supérieur, bibliothèque standard uniquement, aucun `eval`,
`exec`, `compile` ni exécution dynamique de code fourni par l'utilisateur.
Pas de réseau. Les modules sont importables sans exécuter la CLI, imprimer
ou créer de fichier. Pas d'autres fichiers source nécessaires à l'exécution.
Le module de présentation utilise le moteur livré, pas une copie du parseur.

## Moteur

`engine.evaluate(expression: str, variables=None) -> float` renvoie un réel
fini. Les résultats complexes, débordements et erreurs de domaine sont rejetés
par `ValueError`, avec un message non vide. Tous les rejets ci-dessous suivent
ce contrat. Les erreurs internes ne doivent pas sortir comme `RecursionError`
ou `ZeroDivisionError`.

Syntaxe : entiers, décimaux, notation scientifique ; espaces ; `+ - * / ^`,
parenthèses et signes unaires. La puissance est associative à droite et
prioritaire sur le signe : `2^3^2=512`, `-2^2=-4`, `2^-2=0.25`.
Fonctions à un argument : `sin cos tan asin acos atan sqrt ln log10 exp abs`.
Angles en radians ; constantes `pi` et `e`. Aucun attribut, index, chaîne,
conteneur, comparaison, affectation, import ou autre nom autorisé.

`variables` vaut `None` ou un dictionnaire vide ou contenant uniquement `x`.
La valeur de `x` est un entier/flottant fini, hors booléen. L'emploi de `x`
sans valeur est une erreur ; toute autre clé est une erreur. Les expressions
doivent être des chaînes non vides après retrait des espaces périphériques.

Limites explicites de cette nouvelle campagne : au plus 4 096 caractères
avant retrait des espaces, au plus 64 niveaux de parenthèses imbriquées.
Tout dépassement est rejeté avec `ValueError`. À l'intérieur de ces limites,
une somme de 500 termes et 32 parenthèses imbriquées doivent fonctionner.
Ce contrat borné ne redéfinit pas les observations historiques sur 1 500 termes.
Tolérance numérique des tests : relative et absolue `1e-9`.

`engine.sample_curve(expression, x_min, x_max, samples=201)` renvoie une liste
de `samples` couples `(x, y)` incluant les deux bornes, régulièrement espacés.
Bornes finies, hors booléens, `x_min < x_max`, et `2 <= samples <= 1001`, entier
hors booléen. Valeurs invalides : `ValueError`. Une expression mal formée est
rejetée même si tous les points échoueraient. Une erreur de domaine à un point
donne `y=None`. Une courbe entièrement hors domaine est permise (tous `None`).

## Présentation et lots

`presentation.write_svg(points, output_path, title="")` écrit un SVG UTF-8
autonome avec espace de noms SVG, largeur/hauteur positives et `viewBox`.
Le titre est conservé comme texte XML, jamais injecté comme balisage.
Pas de script, événement `on...`, ressource externe ni contenu actif.
Les coordonnées graphiques sont finies, dans le cadre ; la projection est
linéaire, les ordonnées croissantes vont vers le haut. Une série constante
reste visible. Chaque séquence contiguë de valeurs définies forme un tracé
distinct (`polyline` ou `path` avec commandes absolues M/L) ; aucun pont à travers
`None`. Chaque tracé de données porte `data-series="curve"` pour distinguer
les courbes des axes et décorations lors de la vérification indépendante.
Les points isolés peuvent être omis. Une liste vide ou sans valeurs définies
produit un SVG valide sans tracé. Les tests fournissent des abscisses croissantes
et des valeurs finies ou `None` ; validation d'autres points hors périmètre.
Un fichier existant est remplacé. Les erreurs d'accès restent des `OSError`.

`presentation.run_batch(jobs)` accepte une liste d'au plus 100 objets.
Chaque objet a exactement `expression` (chaîne), et éventuellement `variables`
suivant le contrat du moteur. Une liste vide est acceptée. Types erronés,
clés inconnues, clé manquante ou variables invalides : `ValueError` pour le
lot entier, **validé avant tout calcul**. Une expression vide ou syntaxiquement
invalide est en revanche une erreur locale. Ne pas modifier les entrées.
Résultats dans le même ordre : `{"ok": true, "value": flottant}` en cas de
succès, `{"ok": false, "error": message non vide}` en cas d'erreur d'expression.
Une erreur locale n'empêche jamais les tâches suivantes.

## CLI et documentation

`python cli.py batch INPUT.json OUTPUT.json` lit puis traite le lot et écrit
du JSON UTF-8 standard sans NaN/Infinity. Des erreurs locales dans les résultats
ne changent pas le code de sortie 0. Entrée illisible, JSON/structure invalides,
sortie inaccessible ou mauvais arguments : code 2, message non vide sur stderr,
aucun traceback. Une entrée invalide ne crée ni ne remplace la sortie.

`python cli.py plot EXPRESSION OUTPUT.svg --min A --max B --samples N` utilise
les deux API de courbe ; `--samples` est facultatif (201). Bornes obligatoires.
Succès : code 0. Erreurs : même contrat code 2, sans traceback. La CLI fonctionne
depuis un répertoire différent de celui du script. `--help` sort avec code 0.

Le README décrit chaque API, les responsabilités des trois modules, les limites
ci-dessus et les deux commandes. Il contient un exemple JSON de lot réussi,
un exemple d'erreur locale et un exemple de tracé exécutable. Les fonctions
publiques portent une docstring décrivant entrées, sortie et erreurs ; pas de
notation subjective du style ou de la quantité de commentaires.

## Vérification

Commande depuis la racine du dépôt, avec chemin absolu du dossier candidat :

```bash
python3 -B challenges/modular-calculator-draft/tests/test_acceptance.py --solution /chemin/solution
```

Les dix groupes M01–M10 sont détaillés dans le catalogue JSON voisin et les
tests sources. Une suite publique n'est pas un jeu caché. Les tests ne prouvent
ni exhaustivité ni gain collectif ; le verdict appartient au vérificateur.
