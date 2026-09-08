# Calculator — solution V2

Calculatrice Python 3.9 ou ultérieur, sans dépendance externe.

Depuis le dossier de cette tentative :

```bash
python3 solution/calculator.py
```

Depuis la racine du dépôt :

```bash
python3 runs/astra-medium-core-v2-001/solution/calculator.py
```

Saisir deux nombres et un opérateur parmi `+`, `-`, `*`, `/`, séparés par
des espaces ou tabulations. Les espaces multiples sont acceptés. Chaque
ligne doit contenir exactement trois éléments : `2+3`, les parenthèses et
les expressions composées sont refusés. Les espaces obligatoires sont un
choix d'interprétation de la forme donnée dans le challenge.

```text
> 2 + 3
5.0
> -2.5 * -4
10.0
> 1 / 0
Erreur : Division par zéro impossible.
> texte
Erreur : Expression invalide : saisissez nombre opérateur nombre (ex. 2 + 3).
> 1e2 / 4
25.0
> quit
```

`quit` ou `exit` termine normalement la boucle, y compris avec des majuscules
ou des blancs périphériques. Une erreur, y compris une ligne blanche, affiche
un diagnostic sans traceback puis permet un nouveau calcul. La fin du flux
d'entrée (EOF) et Ctrl+C terminent également normalement le programme.

Les nombres suivent la conversion `float` de Python : point décimal,
signes et notation scientifique sont acceptés, la virgule décimale est
refusée. Les valeurs `nan` et `inf`, ainsi que les résultats non finis,
conservent le comportement standard Python. Aucun arrondi supplémentaire
n'est appliqué : `0.1 + 0.2` peut afficher `0.30000000000000004`.
Le zéro positif ou négatif au dénominateur reste interdit, même avec un
numérateur non fini ; un dénominateur petit mais non nul après conversion
en `float` reste accepté. Une valeur trop petite peut être convertie en zéro :
`1 / 1e-400` produit ainsi une erreur de division par zéro.

## Utilisation Python

Depuis le dossier `solution/` :

```python
from calculator import calculate

result = calculate(-2.5, "*", 4)  # -10.0
```

`calculate(left: float, operator: str, right: float) -> float` accepte les
entiers et flottants dans les limites de l'arithmétique `float` de Python et
retourne un `float`. Les entiers arbitrairement grands ne sont pas garantis :
`calculate(10**400, "+", 0)` lève `OverflowError` lors de la conversion du
résultat en `float`. Elle lève `ValueError` pour
un opérateur inconnu et `ZeroDivisionError` pour une division par zéro,
sans afficher de message. Les types d'arguments hors contrat ne font pas
l'objet de validations supplémentaires. Importer le module ne lance pas
la CLI. Les expressions saisies ne sont jamais interprétées comme du code.

## État de validation

Les arbitrages et contrôles ciblés sont consignés dans `DECISIONS.md`.
La critique SA-03 a été arbitrée ; les limites numériques signalées sont
précisées ci-dessus. Commande officielle depuis la racine du dépôt :

```bash
python3 scripts/verify.py --solution runs/astra-medium-core-v2-001/solution
```

Premier passage officiel en phase finale : six tests réussis, verdict `OK`,
code de sortie 0. Aucune correction fonctionnelle nécessaire après ce passage.
