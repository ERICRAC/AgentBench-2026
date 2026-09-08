# Calculator

Calculatrice Python interactive pour une opération binaire parmi `+`, `-`,
`*` et `/`. Python 3.9 ou ultérieur suffit ; aucune dépendance à installer.

## Lancement

Depuis la racine du dépôt, pour cette tentative :

```bash
python3 runs/astra-core-v2-001/solution/calculator.py
```

Depuis le dossier `runs/astra-core-v2-001` :

```bash
python3 solution/calculator.py
```

Depuis le dossier `solution` de cette tentative :

```bash
python3 calculator.py
```

## Utilisation

À chaque invite `>`, saisir exactement `nombre opérateur nombre`. Séparer les
trois éléments par des espaces ou des tabulations ; les espaces périphériques
et multiples sont acceptés. Les signes appartiennent aux nombres :

```text
> 2 + 3
5.0
> -2.5 * -4
10.0
> 7 / 2
3.5
> 1 / -0.0
Erreur : Division par zéro impossible.
> 9 - 12
-3.0
> exit
```

`quit` et `exit` terminent le programme, même en majuscules et avec des espaces
périphériques. Une fin de fichier (EOF) ou Ctrl+C termine aussi proprement.
Les entrées peuvent être redirigées depuis un fichier ou un autre programme.

Une ligne vide, un nombre invalide, un opérateur inconnu, une division par zéro
ou un nombre incorrect d'éléments produit un message d'erreur sans traceback ;
la calculatrice attend ensuite la prochaine ligne.

La grammaire choisie ne prend pas en charge `2+3`, les parenthèses ou les
opérations chaînées comme `2 + 3 * 4`. Utiliser le point pour les décimaux :
`1.5 + 2` est valide, `1,5 + 2` est invalide. La notation scientifique est
acceptée, par exemple `1e3 / -2` donne `-500.0`.

## API Python

Depuis le dossier de la solution :

```python
from calculator import calculate

calculate(2, "+", 3)       # 5
calculate(-2.5, "*", -4)   # 10.0
calculate(7, "/", 2)       # 3.5
```

La fonction expose `calculate(left: float, operator: str, right: float) -> float`.
Elle accepte des arguments numériques entiers ou flottants, conserve l'ordre
des opérandes et utilise l'arithmétique Python. Elle lève `ValueError` pour un
opérateur inconnu et `ZeroDivisionError` pour une division par `0` ou `-0.0`.
Un opérateur inconnu avec zéro à droite lève bien `ValueError`. Elle ne convertit
pas les chaînes en nombres et ne réalise aucune entrée-sortie. Importer le
module ne lance pas la boucle interactive.

`parse_expression` convertit une ligne en `(left, operator, right)` ;
`calculate` valide l'opérateur ; `main` pilote la console et présente les erreurs.
Les saisies sont traitées comme des données, sans exécution dynamique.

## Choix numériques et limites

La CLI utilise `float` et son affichage habituel, sans arrondi ajouté. La
représentation binaire peut donc donner `0.30000000000000004` pour `0.1 + 0.2`.
Les formes numériques reconnues par `float`, dont `nan`, `inf` et la notation
scientifique, sont acceptées. Un nombre tel que `1e999` devient `inf` et un
débordement flottant peut produire un infini ; aucune restriction de finitude
n'est ajoutée. Une très petite valeur peut être arrondie à zéro par `float`
et provoquer une erreur si elle sert de diviseur. Ces comportements sont des
choix documentés sur des points non précisés par le challenge.

Aucune limite de longueur de saisie n'est imposée ; une entrée démesurée peut
épuiser les ressources. Les erreurs d'entrée-sortie, telles qu'un tube de sortie
fermé, ne sont pas interceptées. La reprise après erreur concerne les erreurs
d'expression et de division par zéro décrites plus haut.

## État de la tentative

La phase MAIN finale reprend la première solution après la critique SA-03.
Les arbitrages préalables et finaux, les cinq textes relayés dans leur ordre
d'origine et les contrôles figurent dans [DECISIONS.md](DECISIONS.md).

La commande officielle depuis la racine du dépôt est :

```bash
python3 scripts/verify.py --solution runs/astra-core-v2-001/solution
```

Résultat final sous Python 3.13.5 : **6 tests réussis, `OK`, code de sortie 0**
dès le premier passage officiel. Aucune correction fonctionnelle n'a été
nécessaire après SA-03. La sortie du vérificateur et les limites de preuve
sont conservées dans `DECISIONS.md`.
