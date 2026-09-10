# PV V1 — calculatrice simple Astra moyen

## Le run en 2 minutes

Un candidat développeur solo, mandaté par un orchestrateur expérimental externe. Aucun consultant ni sous-agent du candidat. Une session neuve : **98,572 s ; 98 496 tokens entrée + sortie ; 6/6 groupes, 14/14 contrôles**, au premier passage puis à la vérification indépendante. Aucune correction fonctionnelle après le premier passage, aucun contrôle candidat supplémentaire enregistré.

Implémentation : sélection explicite des quatre opérations ; fonction calculate séparée de la boucle CLI ; trois éléments séparés par des blancs ; erreurs affichées sans interrompre la saisie. Documentation de lancement, exemples et limites des flottants. Les seuls fichiers ajoutés sont calculator.py, README.md et PV.md dans solution/.

Incident : recherche de chemins relatifs inexistants (sortie 2), puis lecture des chemins corrects de gouvernance. Aucun effet fonctionnel établi. Le PV supplémentaire suit les exigences de journalisation mais dépasse la liste des deux livrables du défi : tension documentaire conservée, non sanctionnée par le vérificateur. Ne pas transformer 6/6 en conformité exhaustive.

## Rôles et ordre observé

1. L’humain autorise uniquement Core ; Scientific reste vierge.
2. L’orchestrateur rejoue le préflight 44/44, enregistre l’autorisation (70857ec) et mandate une session éphémère avec les configurations figées.
3. Le candidat lit le challenge, rencontre une erreur de chemins, consulte le format de restitution et la journalisation.
4. Il écrit le code et son README, lance le vérificateur depuis le dossier du run et obtient six succès.
5. Il ajoute son PV et restitue le résultat. Aucun échange avec un autre candidat, aucun conseil fourni par le relais.
6. Après clôture, l’orchestrateur relance indépendamment la suite : six succès, code 0 ; il conserve les trois fichiers sans modification (ddf4745).
7. Publication séparée : ce PV, trace filtrée, métadonnées et rapport multilingue. Les heures et raisonnements internes ne sont pas publiés.

## Mesures enregistrées

| Mesure | Valeur |
| --- | ---: |
| Modèle / effort configurés | gpt-6-astra / medium |
| CLI | 0.153.4 |
| Contexte / compaction configurés | 200000 / 180000, total |
| Sessions candidates | 1 |
| Appels modèle internes | Non enregistrés comme compteur autonome |
| Durée de session | 98.572 s |
| Entrée | 96182 |
| Cache, inclus dans entrée | 76800 |
| Sortie | 2314 |
| Raisonnement, inclus dans sortie | 104 |
| Entrée + sortie | 98496 |
| Corrections après premier passage officiel | 0 |
| Interventions humaines fonctionnelles | 0 |

La durée comprend lancement/clôture CLI, pas préparation, contrôle indépendant ou publication. Compteurs extraits du turn.completed final ; pas de double comptage. Les paramètres sont enregistrés et la session a réussi ; aucune compaction ou saturation ne prouve ici l’application d’un plafond effectif de contexte. Le modèle demandé n’est pas une preuve d’immuabilité des poids serveur.

## Mandat transmis — texte exact

````text
Réalise le défi décrit dans CHALLENGE.md.

Contraintes particulières pour cette tentative :

- travaille seul et ne lance aucun sous-agent ;
- écris uniquement dans le dossier solution/ ;
- ne modifie ni la spécification, ni les tests, ni les scripts du dépôt ;
- implémente une solution complète et documentée ;
- lance le vérificateur indiqué dans CHALLENGE.md ;
- corrige les défauts confirmés et termine en résumant le résultat des tests.
````

Les instructions de rôle supplémentaires sont conservées dans [config.toml](config.toml). Aucune nouvelle instruction de solution ajoutée.

## Réponses visibles — texte exact filtré

### MSG-001 — candidat vers orchestrateur

````text
Je vais lire le défi, implémenter la solution dans `solution/`, puis lancer le vérificateur prévu. Je travaillerai seul, sans sous-agent.
````

### MSG-002 — candidat vers orchestrateur

````text
Le contrat prévoit une fonction Python et une boucle interactive. Je vais analyser chaque ligne en trois éléments, gérer les erreurs sans interrompre la boucle et documenter les usages dans le README.
````

### MSG-003 — candidat vers orchestrateur

````text
Le vérificateur indépendant a réussi les six tests, notamment les quatre opérations, les exceptions et la reprise de la saisie après une erreur. Je consigne ce résultat dans le procès-verbal de la tentative, dans `solution/`.
````

### MSG-004 — candidat vers orchestrateur

````text
Solution complète dans `solution/` : `calculator.py`, `README.md` et `PV.md`.

Le vérificateur a été lancé depuis le dossier de la tentative :

```bash
python3 ../../scripts/verify.py --solution solution
```

**Résultat : 6 tests réussis, aucun échec.** Les opérations, exceptions et la reprise interactive après erreur sont validées.

Travail réalisé seul, sans modification des tests ni des scripts. Aucune opération Git ; publication réservée à l’orchestrateur.
````

## Vérifications et sources

- Premier passage candidat : commande `python3 ../../scripts/verify.py --solution solution`, code 0, 6 tests, OK ; sortie complète dans [trace.json](trace.json).
- Contrôle indépendant après clôture : `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --solution runs/astra-medium-core-v1-001/solution`, code 0, 6 tests, OK.
- [Catalogue des six groupes et quatorze contrôles](../../docs/acceptance-tests.md) ; les quatre opérations sont quatre cas dans un groupe, pas un seul calcul.
- [Métadonnées](run.json) · [PV du candidat](solution/PV.md) · [Code](solution/calculator.py) · [README candidat](solution/README.md).
- [Rapport et comparaison V1/V2](../../results/astra-medium-v1-core.md).

Le candidat écrit « tokens et durée non enregistrés » dans son PV : c’est vrai de sa visibilité locale, pas de la capture externe. Ces textes sont conservés sans correction rétroactive. Aucune interaction inter-agents à analyser dans cette V1 ; sa comparaison avec la V2 évalue le coût et le résultat des organisations, pas des pensées privées.
