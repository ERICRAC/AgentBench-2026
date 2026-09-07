# Catalogue des tests d'acceptation

**Français** · [English (UK)](acceptance-tests.en.md) · [Español](acceptance-tests.es.md) · [Português](acceptance-tests.pt.md)

## Comment lire les verdicts

`unittest` affiche une unité par **méthode de test**. AgentBench possède donc
6 groupes Core et 9 groupes Scientific. Ces 15 groupes exécutent actuellement,
sur un passage intégralement réussi, **71 assertions élémentaires** : 14 pour
Core et 57 pour Scientific.

Ainsi, « quatre opérations » ne vaut pas un seul contrôle fonctionnel : le
groupe C03 exécute quatre cas distincts. Le verdict public doit annoncer les
deux niveaux, par exemple : **6/6 groupes Core — 14/14 contrôles réussis**.

Chemin d'audit : [spécification Core](../challenges/calculator/SPEC.md) →
[tests Core exécutables](../challenges/calculator/tests/test_acceptance.py) →
[spécification Scientific](../challenges/scientific-calculator/SPEC.md) →
[tests Scientific exécutables](../challenges/scientific-calculator/tests/test_acceptance.py) →
[résultats publiés](../results/README.md).

## Calculatrice Core — 6 groupes, 14 contrôles

### C01 — Livrables requis · 2 contrôles

- [ ] `calculator.py` existe.
- [ ] `README.md` existe.

### C02 — Absence d'exécution dynamique · 1 contrôle

- [ ] L'arbre syntaxique ne contient aucun appel à `eval()` ou `exec()`.

### C03 — Opérations et variantes numériques · 4 contrôles

- [ ] `2 + 3` retourne `5`.
- [ ] `-2 - 3` retourne `-5`.
- [ ] `1.5 * 2` retourne `3.0`.
- [ ] `7 / 2` retourne `3.5`.

### C04 — Opérateur inconnu · 1 contrôle

- [ ] `calculate(1, "%", 2)` lève `ValueError`.

### C05 — Division par zéro · 1 contrôle

- [ ] `calculate(1, "/", 0)` lève `ZeroDivisionError`.

### C06 — Résilience de la CLI · 5 contrôles

La même session envoie succès, division par zéro, expression invalide, nouveau
succès puis `quit`.

- [ ] Le processus termine avec le code `0`.
- [ ] Aucun traceback n'est affiché.
- [ ] Le résultat `5` est affiché.
- [ ] Le résultat `-8` après les erreurs prouve la reprise de la boucle.
- [ ] Un message compréhensible contient « erreur », « invalide » ou
  « division ».

[Voir les six méthodes dans le code](../challenges/calculator/tests/test_acceptance.py#L23).

## Calculatrice Scientific — 9 groupes, 57 contrôles

### S01 — Livrables et documentation · 7 contrôles

- [ ] `scientific_calculator.py` existe.
- [ ] `README.md` existe.
- [ ] La documentation contient `evaluate`, `plot`, `svg`, `sin` et `history`
  — cinq contrôles séparés.

### S02 — Sécurité et dépendances · 2 contrôles

- [ ] Aucun appel à `eval()`, `exec()` ou `compile()`.
- [ ] Tous les imports appartiennent à la bibliothèque standard Python.

### S03 — Priorités, parenthèses, puissances et signes · 10 contrôles

Chaque expression doit produire un `float` puis la valeur attendue, soit deux
assertions par ligne.

- [ ] `2 + 3 * 4 = 14.0`.
- [ ] `(2 + 3) * 4 = 20.0`.
- [ ] `2 ^ 3 ^ 2 = 512.0`.
- [ ] `-2 ^ 2 = -4.0`.
- [ ] `2 ^ -2 = 0.25`.

### S04 — Constantes, fonctions et notation scientifique · 6 contrôles

- [ ] `sin(pi / 2) = 1.0`.
- [ ] `cos(0) + tan(0) = 1.0`.
- [ ] `asin(1) + acos(1) + atan(0) = pi / 2`.
- [ ] `sqrt(9) + ln(e) + log10(100) = 6.0`.
- [ ] `exp(0) + abs(-3) = 4.0`.
- [ ] `1e-3 + 2E2 = 200.001`.

### S05 — Variable et noms interdits · 5 contrôles

- [ ] `x ^ 2 + 1`, avec `x = 3`, retourne `10.0`.
- [ ] `x + 1` sans valeur de `x` lève `ValueError`.
- [ ] `unknown(2)` lève `ValueError`.
- [ ] `__import__('os')` lève `ValueError`.
- [ ] `pi.real` lève `ValueError`.

### S06 — Syntaxe, domaine et arithmétique · 6 contrôles

- [ ] Une expression vide lève `ValueError`.
- [ ] `2 +` lève `ValueError`.
- [ ] `sqrt(-1)` lève `ValueError`.
- [ ] `ln(0)` lève `ValueError`.
- [ ] `exp(10000)` lève `ValueError`.
- [ ] `1 / 0` lève `ZeroDivisionError`.

### S07 — Échantillonnage et discontinuités · 8 contrôles

- [ ] `x ^ 2` sur `[-2, 2]` avec cinq échantillons retourne cinq points.
- [ ] Le premier point vaut `(-2.0, 4.0)`.
- [ ] Le dernier point vaut `(2.0, 4.0)`.
- [ ] Le point central vaut `(0.0, 0.0)`.
- [ ] `1 / x` représente le point central par `(0.0, None)`.
- [ ] Deux bornes égales sont rejetées.
- [ ] Des bornes inversées sont rejetées.
- [ ] Un seul échantillon est rejeté.

### S08 — SVG valide et passif · 7 contrôles

- [ ] La racine XML est un élément `svg`.
- [ ] Au moins deux éléments `line` représentent les axes.
- [ ] Un élément `polyline` ou `path` représente la courbe.
- [ ] Aucun élément `script` brut n'est injecté.
- [ ] Aucune URL `javascript:` n'est injectée.
- [ ] Le titre utilisateur contenant `<` et `&` est échappé.
- [ ] Une courbe sans aucun point fini lève `ValueError`.

### S09 — CLI, tracé et historique · 6 contrôles

La session calcule `14`, provoque une erreur de domaine, trace `sin(x)`, consulte
et efface l'historique, puis quitte.

- [ ] Le processus termine avec le code `0`.
- [ ] Aucun traceback n'est affiché.
- [ ] Le résultat `14` est affiché.
- [ ] Une erreur de domaine compréhensible est affichée.
- [ ] `sin(x)` apparaît dans l'historique.
- [ ] Le fichier `curve.svg` est créé.

[Voir les neuf méthodes dans le code](../challenges/scientific-calculator/tests/test_acceptance.py#L28).

## Ce que ces nombres ne prouvent pas

Les 71 contrôles décrivent la couverture actuelle, pas une qualité absolue. Ils
ne remplacent ni l'analyse des cas limites, ni les contrôles exploratoires, ni
les répétitions statistiques. Une nouvelle assertion officielle changerait la
suite et imposerait une nouvelle campagne ; les résultats existants resteraient
liés à la version ci-dessus.
