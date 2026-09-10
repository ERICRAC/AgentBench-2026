# Procès-verbal — défi scientifique, mode V1

## Échange 001 — Mandat et périmètre

Le commanditaire demande une calculatrice scientifique complète en Python
standard, réalisée seul dans `solution/`. L'orchestrateur expérimental mandate
la session candidate et reste responsable de la publication après le run.
L'agent candidat est Codex, modèle GPT-6, sans consultant ni sous-agent.
La spécification active `../CHALLENGE.md` a été lue avant toute modification.
Aucune autre tentative ou solution n'a été consultée. Aucune opération Git
n'a été exécutée par le candidat.

## Échange 002 — Réalisation et choix

Création de `scientific_calculator.py` et `README.md`. Un analyseur récursif
dédié applique la grammaire autorisée et la priorité des puissances. Les
résultats numériques doivent être finis. L'échantillonneur valide la syntaxe
avant de convertir les erreurs numériques locales en points absents. Le SVG
échappe le titre, retire les caractères XML interdits et sépare les segments.
La CLI mémorise seulement les opérations réussies et reprend après erreur.
La documentation décrit les commandes, l'API, la sécurité et les limites.

## Échange 003 — Contrôles observables

Un contrôle manuel de la CLI a évalué `2^3^2`, `-2^2`, `2^-2`, puis `1/0`,
`history` et `quit`. Résultats : `512.0`, `-4.0`, `0.25`, message d'erreur sans
traceback et historique des trois expressions réussies.

Le vérificateur indépendant du dépôt a été exécuté depuis le dossier actif :

```bash
python3 -B ../../scripts/verify.py --challenge scientific-calculator --solution solution
```

Verdict observé : **9 tests réussis, OK, code de sortie 0**. La suite couvre
CLI et historique, fonctions et constantes, échantillonnage, sécurité,
priorités, documentation, SVG, erreurs et variables. Durée rapportée par la
suite : 0,040 seconde. Aucun défaut confirmé et aucune correction après ce
contrôle. Les sorties ont été observées dans la session ; aucun fichier de
sortie brute supplémentaire n'a été créé par le candidat.

## Échange 004 — Limites et clôture

Les singularités situées entre deux échantillons peuvent ne pas être détectées.
Le calcul suit les arrondis flottants usuels. La taille des expressions est
bornée et les dépassements de profondeur sont signalés. Le nombre de points
choisi par un appelant API détermine sa consommation de mémoire et de temps.
Aucun échec de contrôle ne reste ouvert. Aucun changement de gouvernance
n'est proposé pour ce run. La publication appartient à l'orchestrateur.

Tokens, coût et durée totale du travail candidat : non enregistrés.
