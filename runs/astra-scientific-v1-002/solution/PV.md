# Procès-verbal — Scientific Calculator, V1

## Acteurs et périmètre

- Commanditaire : utilisateur de la session.
- Orchestrateur expérimental : rôle distinct du candidat, responsable du
  lancement et de la publication ; identité précise non enregistrée ici.
- Agent candidat : Codex, mode V1, seul écrivain de la solution.
- Consultants et sous-agents du candidat : aucun ; aucune délégation.
- Vérificateur indépendant : `scripts/verify.py`, défi `scientific-calculator`.

Écritures limitées à `solution/`. Aucune autre tentative ou solution consultée.
Spécification, suite indépendante et scripts du dépôt inchangés. Aucune
opération Git effectuée. La publication relève de l'orchestrateur expérimental.

## Échanges, décisions et contrôles observables

1. **Mandat.** Réaliser le défi scientifique avec la bibliothèque standard
   Python, travailler seul, exécuter le vérificateur et documenter les limites.
   Lecture du `CHALLENGE.md` actif avant toute modification.
2. **Choix du candidat.** Analyseur de la grammaire autorisée et interprétation
   d'instructions arithmétiques postfixées. Les expressions ne sont jamais
   exécutées comme du code Python. Analyse bornée en taille et profondeur.
3. **Implémentation.** Création de `scientific_calculator.py` et `README.md` :
   évaluation réelle, échantillonnage avec lacunes, SVG sérialisé en XML,
   historique de session et récupération de la CLI après erreur.
4. **Premier verdict indépendant.** Exécution depuis le dossier de la tentative
   active : 9 tests réussis, code de sortie 0. Durée indiquée par unittest :
   0,039 seconde.
5. **Contrôles complémentaires.** Quatre tests du candidat exécutés initialement
   par un script Python transmis sur l'entrée standard : trois réussites et un
   échec sur l'interpolation entre deux bornes positives voisines du plus grand
   flottant. L'assertion d'appartenance à l'intervalle échoue. Ce défaut n'a pas
   été signalé par la suite indépendante.
6. **Correction confirmée.** Interpolation par différence lorsque les bornes
   ont le même signe ; maintien de la somme pondérée pour les signes opposés
   afin d'éviter un débordement de leur différence. Conservation des contrôles
   dans `verify_additional.py`, avec ajout du cas symétrique négatif.
7. **Validation après correction.** `python3 -B verify_additional.py` : 4 tests
   réussis, code 0, durée unittest 0,003 seconde. Vérificateur indépendant
   relancé : 9 tests réussis, code 0, durée unittest 0,042 seconde.
8. **Documentation finale.** Ajout des résultats, des limites numériques et du
   présent procès-verbal. Aucune intervention humaine supplémentaire ni
   modification de gouvernance pendant l'implémentation.

## Commandes de validation

Depuis le dossier de la tentative active, après création de `solution/.tmp` :

```bash
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/solution/.tmp" python3 ../../scripts/verify.py --challenge scientific-calculator --solution solution
```

Depuis `solution/` :

```bash
python3 -B verify_additional.py
```

Les paramètres d'environnement empêchent la génération de caches Python hors
de `solution/` et y dirigent les fichiers temporaires du vérificateur. Les
sorties de contrôle sont capturées dans les échanges d'outils de la session ;
aucun fichier de sortie brute supplémentaire n'est conservé.

## Limites et métriques

- Aucun contrôle restant en échec.
- Arrondis flottants et singularités entre échantillons : limites documentées,
  sans détection symbolique ni adaptative.
- Validité XML et absence de contenu actif contrôlées automatiquement ; rendu
  visuel dans un navigateur en thèmes clair et sombre non contrôlé.
- Compatibilité 3.10 visée par la syntaxe et les API ; aucune matrice de versions
  Python exécutée pendant cette session.
- Les durées ci-dessus sont celles rapportées par unittest, pas la durée totale
  du travail. Durée totale et consommation de tokens : non enregistrées.
- Aucun avis externe sollicité. Aucun commit ni push effectué par le candidat.
