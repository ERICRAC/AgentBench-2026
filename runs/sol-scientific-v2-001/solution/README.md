# Scientific Calculator

Cette solution fournit un moteur d'expressions fermé, un échantillonneur de
courbes, un export SVG autonome et une interface interactive. Elle utilise
uniquement la bibliothèque standard de Python 3.10 ou supérieur.

## Lancement

Depuis la racine du dépôt :

```bash
python3 solution/scientific_calculator.py
```

La boucle affiche l'invite `>`. Une expression est calculée immédiatement :

```text
> sqrt(2) ^ 2
2.0000000000000004
```

Les commandes disponibles sont `help`, `history`, `clear`, `quit` et `exit`.
Seules les évaluations et écritures de courbes entièrement réussies figurent
dans l'historique de la session.

## Langage accepté

- Littéraux entiers, décimaux et scientifiques : `2`, `.5`, `1.`, `6.02e23`.
- Opérateurs : `+`, `-`, `*`, `/`, `^` et parenthèses.
- Constantes : `pi`, `e`.
- Fonctions à un argument : `sin`, `cos`, `tan`, `asin`, `acos`, `atan`,
  `sqrt`, `ln`, `log10`, `exp`, `abs`.
- Variable `x`, seulement lorsqu'une valeur est fournie par l'API ou pendant
  l'échantillonnage d'une courbe.

Les angles sont en radians. La puissance est associative à droite et plus
prioritaire que les signes : `2^3^2` vaut `512.0`, `-2^2` vaut `-4.0`, et
`2^-2` vaut `0.25`.

Le langage n'accepte pas la multiplication implicite (`2pi`, `2(x)`), les
virgules, chaînes, crochets, attributs, mots-clés Python, opérateur `**` ou
appel d'une fonction non listée. Une fonction exige exactement un argument
entre parenthèses.

## Tracer une courbe

La commande `plot` contient exactement quatre champs séparés par des
points-virgules. Les bornes sont elles-mêmes des expressions sûres :

```text
> plot sin(x); -pi; pi; sinus.svg
Courbe enregistrée dans sinus.svg
```

Le fichier UTF-8 obtenu ne dépend d'aucune ressource externe et ne contient
aucun contenu actif. Une valeur hors domaine ou non finie devient une coupure
dans la courbe au lieu de faire échouer tout le tracé. Un fichier existant au
chemin demandé est remplacé ; les répertoires parents ne sont pas créés.

## API Python

```python
from scientific_calculator import evaluate, sample_curve, write_svg

value = evaluate("sin(pi / 2)")
value_at_two = evaluate("x^2 + 1", {"x": 2.0})
points = sample_curve("1 / x", -1.0, 1.0, samples=201)
write_svg(points, "inverse.svg", title="1 / x")
```

`evaluate` retourne toujours un `float` fini. Une expression vide, mal formée,
un nom inconnu, une valeur non réelle ou hors domaine lève `ValueError`; seul
l'opérateur `/` appliqué à zéro lève `ZeroDivisionError` (ainsi `0^-1` est une
opération hors domaine). Le dictionnaire `variables`, s'il est fourni, ne peut
contenir que `x`, associé à un réel fini non booléen.

`sample_curve` exige des bornes finies strictement croissantes et un entier
`samples >= 2`; les deux bornes sont incluses. Les erreurs de syntaxe et de nom
sont levées avant l'échantillonnage. Les erreurs numériques ponctuelles sont
représentées par `None`.

`write_svg` exige au moins un couple de coordonnées finies. Chaque `None` ou
coordonnée non finie coupe le segment. Les titres sont sérialisés comme texte
XML et les caractères interdits par XML 1.0 sont refusés.

## Sécurité et limites

Le lexer consomme toute l'entrée et le parseur n'expose qu'une liste blanche
d'opérations mathématiques. Aucun code, commande système, accès réseau,
attribut ou import issu d'une expression n'est exécuté.

La solution n'impose pas de plafond arbitraire à la longueur d'une expression
ou au nombre d'échantillons. L'appelant doit donc choisir des tailles adaptées
à ses ressources. Une imbrication qui dépasse les capacités récursives de
Python est signalée comme expression trop profonde. Le calcul utilise les
flottants binaires de Python : les arrondis usuels sont visibles et les
résultats infinis sont refusés. Les caractères de contrôle présents dans un
chemin sont réaffichés sous forme échappée dans le terminal et l'historique.
