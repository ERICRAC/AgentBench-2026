# PV V1 — calculatrice scientifique Astra moyen

## Le run en 2 minutes

Un candidat développeur solo mandaté dans une session distincte ; aucun consultant ni sous-agent du candidat. **188,560 s ; 119 388 tokens entrée + sortie ; 9/9 groupes et 57/57 contrôles**, au premier passage puis au contrôle indépendant. Aucune correction après le premier verdict officiel ; pas de reprise ni d’intervention humaine fonctionnelle.

Le candidat construit un analyseur récursif dédié, un arbre d’expression réutilisé pour les échantillons, un export SVG avec titre échappé et segments séparés, puis une CLI avec historique des opérations réussies. Il documente syntaxe, fonctions, API, erreurs et limites. Livrables conservés sans retouche dans le commit aaa83de : 295 lignes Python, README de 83 lignes, PV candidat de 51 lignes.

## Rôles et séquence observable

1. L’humain autorise Scientific après publication de Core (bcaeb67). RELAY, orchestrateur expérimental hors candidat, vérifie les six empreintes et le dossier vide ; autorisation enregistrée dans b312fb5.
2. RELAY lance une session éphémère avec le prompt historique et gpt-6-astra / medium. Aucun conseil issu de V2 n’est transmis.
3. CANDIDATE lit CHALLENGE puis les règles de restitution/journalisation. La recherche rg dans le dossier vide retourne 1 : absence de fichier, pas un échec fonctionnel.
4. CANDIDATE écrit le code et README par commande shell, puis vérifie manuellement la CLI : 512.0, -4.0, 0.25 ; division par zéro lisible ; historique limité aux trois calculs réussis.
5. Il lance une fois le vérificateur officiel : neuf succès, code 0. Il ajoute son PV et restitue. Aucun échange entre agents candidats.
6. Après clôture, RELAY relance la suite indépendante : neuf succès, code 0, sans modifier la solution. Les fichiers candidats sont commités séparément.
7. RELAY examine deux limites avec des sondes exploratoires, puis publie trace, métriques et comparaison multilingue. Ces sondes ne changent ni les tests figés ni le score.

## Mesures

| Mesure | Valeur |
| --- | ---: |
| Modèle / effort demandés | gpt-6-astra / medium |
| CLI | 0.153.4 |
| Contexte / compaction configurés | 200000 / 180000, total |
| Sessions / consultants | 1 / 0 |
| Durée candidate | 188.560 s |
| Entrée | 113746 |
| Cache inclus dans entrée | 98944 |
| Sortie | 5642 |
| Raisonnement inclus dans sortie | 164 |
| Entrée + sortie | 119388 |
| Commandes terminées / messages visibles | 6 / 5 |
| Corrections après premier passage officiel | 0 |
| Interventions humaines fonctionnelles | 0 |

Durée incluant lancement/clôture CLI ; préparation, vérification indépendante et publication exclues. Compteurs du turn.completed final, sans double comptage. Aucun compteur autonome des appels modèle internes. Configuration acceptée par la CLI ; ni plafond effectif de contexte atteint/démontré, ni identité immuable des poids serveur prouvée. Le PV candidat indique métriques non enregistrées : elles ne sont pas disponibles localement pour lui, mais le sont dans la capture externe.

## Limites et écarts observés

Le candidat crée solution/PV.md en plus des deux livrables listés : tension entre journalisation et défi, conservée et non sanctionnée par la suite. Il utilise des redirections shell plutôt que apply_patch ; fait observable, sans réécriture corrective de l’historique. Zéro événement file_change ne signifie donc pas zéro écriture : les créations figurent dans les commandes.

Le plafond de 10000 caractères et la récursion limitent des expressions mathématiquement valides. Deux sondes après run confirment ValueError pour `"1" + " " * 10000` (résultat mathématique 1) et `"+".join(["1"] * 1500)` (1500). Ce sont des observations exploratoires **hors 57 contrôles**, non préenregistrées, sur V1 uniquement. Le rapport V2 documente une correction de cette famille de limites après SA-03 — sous-agent 3, relecteur critique. Pas de rejeu V2 identique dans cet échange, pas de mesure exhaustive d’avantage de robustesse.

Les arrondis, singularités entre échantillons et ressources consommées par un grand échantillonnage restent des limites documentées. Aucun résultat officiel ne vaut preuve générale de conformité ou de maintenabilité.

## Mandat transmis — texte exact

````text
Réalise le défi scientifique décrit dans CHALLENGE.md.

Contraintes particulières pour cette tentative :

- travaille seul et ne lance aucun sous-agent ;
- ne lis aucune autre tentative ni aucune autre solution du dépôt ;
- écris uniquement dans le dossier solution/ de la tentative active ;
- ne modifie ni la spécification, ni les tests, ni les scripts du dépôt ;
- utilise uniquement la bibliothèque standard Python ;
- implémente une solution complète, sûre et documentée, sans placeholder ;
- lance le vérificateur scientifique indiqué dans CHALLENGE.md ;
- corrige uniquement les défauts confirmés par ton analyse ou les contrôles ;
- termine par une restitution structurée indiquant le traitement, les choix,
  les tests exécutés, les corrections et les limites observées.
````

Les instructions complémentaires de rôle figurent dans [config.toml](config.toml).

## Réponses visibles — texte exact filtré

### MSG-001 — candidat vers orchestrateur

````text
Je vais lire le défi, implémenter la solution avec la bibliothèque standard Python, puis lancer le vérificateur indiqué. Je travaillerai seul et limiterai les écritures au dossier `solution/`.
````

### MSG-002 — candidat vers orchestrateur

````text
Le contrat impose notamment une puissance associative à droite, prioritaire sur les signes unaires, et des coupures de courbe aux points non définis. Je vais utiliser un analyseur dédié, puis générer le SVG en échappant le titre et en séparant les segments aux valeurs absentes.
````

### MSG-003 — candidat vers orchestrateur

````text
L’implémentation et la documentation sont en place. Le contrôle initial confirme les priorités des puissances et la reprise de la CLI après une division par zéro. Le tracé utilise un échantillonnage uniforme ; la documentation précise qu’une singularité entre deux échantillons peut échapper à la détection. Je lance maintenant le vérificateur indépendant depuis la tentative active.
````

### MSG-004 — candidat vers orchestrateur

````text
Les neuf tests d’acceptation du vérificateur indépendant passent. Aucun défaut nécessitant une correction n’a été signalé. Je consigne les choix, les contrôles et les limites dans un procès-verbal local.
````

### MSG-005 — candidat vers orchestrateur

````text
## Résultat

Défi réalisé seul, uniquement dans `solution/`, avec la bibliothèque standard Python.

## Traitement et choix

- `scientific_calculator.py` : analyseur sécurisé, calcul scientifique, échantillonnage, SVG et CLI avec historique.
- `README.md` : syntaxe, exemples, API et limites.
- `PV.md` : procès-verbal des décisions et contrôles.

## Vérifications et corrections

Vérificateur scientifique exécuté depuis la tentative active : **9 tests réussis, aucun échec**. Le contrôle manuel confirme également les priorités et la récupération après erreur. Aucune correction supplémentaire nécessaire.

## Limites

Les arrondis flottants subsistent. Une singularité entre deux échantillons peut ne pas être détectée.

## Livraison Git

Aucune opération Git effectuée ; publication réservée à l’orchestrateur expérimental.
````

## Vérifications et preuves

- Candidat : `python3 -B ../../scripts/verify.py --challenge scientific-calculator --solution solution`, code 0, 9 tests, OK ; une invocation officielle observée.
- Orchestrateur après clôture : `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --challenge scientific-calculator --solution runs/astra-medium-scientific-v1-001/solution`, code 0, 9 tests, OK.
- [Liste des neuf groupes et 57 contrôles](../../docs/acceptance-tests.md) · [Trace observable et sondes](trace.json) · [Métadonnées](run.json).
- [Code](solution/scientific_calculator.py) · [README candidat](solution/README.md) · [PV candidat](solution/PV.md).
- [Bilan V1/V2 sur les deux calculatrices](../../results/astra-medium-v1-v2.md) · [Preuves V2](../../results/astra-medium-v2.md).

Les chemins locaux sont normalisés et les éléments privés exclus. Un masquage automatique peut remplacer dans les commandes de trace des identifiants de code nommés token ; cela ne signifie pas la présence d’un secret. Les fichiers candidats font foi pour le code exact. Aucun raisonnement interne ni horaire de travail publié.
