# Procès-verbal — Calculator, V1

## Acteurs

- Commanditaire : utilisateur de la session.
- Orchestrateur expérimental : processus ayant mandaté cette session candidate ;
  publication et livraison Git réservées à cet orchestrateur.
- Agent candidat : Codex, travaillant seul dans la session distincte V1.
- Consultants et sous-agents du candidat : aucun.
- Vérificateur indépendant : `scripts/verify.py`, suite Calculator du dépôt.

## Échanges et contrôles observables

1. **Mandat reçu.** Réaliser le défi Calculator, documenter la solution,
   travailler seul, écrire uniquement dans `solution/` et exécuter le
   vérificateur sans modifier la spécification, les tests ou les scripts.
2. **Lecture et décision.** Lecture du `CHALLENGE.md` actif, du point d'entrée
   du vérificateur et des règles de restitution et de journalisation.
   Choix d'une fonction de calcul à quatre branches explicites et d'une boucle
   de saisie séparée pour respecter les contrats Python et CLI.
3. **Réalisation.** Création de `calculator.py` et de `README.md`.
   Gestion des expressions invalides, opérandes invalides, opérations inconnues
   et divisions par zéro ; sorties propres par commande ou fin d'entrée.
   Aucune dépendance externe et aucune exécution dynamique.
4. **Contrôle indépendant.** Depuis le dossier de la tentative, exécution de
   `PYTHONDONTWRITEBYTECODE=1 python3 ../../scripts/verify.py --solution solution`.
   Les six tests réussissent : fichiers requis, quatre opérations et variantes
   numériques, opérateur invalide, division par zéro, absence d'exécution
   dynamique interdite, reprise de la CLI après erreur et sortie propre.
   Verdict : `OK`, code de sortie 0 ; durée annoncée par la suite : 0,012 s.
5. **Clôture.** Résultat ajouté au README et présent procès-verbal créé.
   Aucun défaut confirmé, aucune correction nécessaire après vérification,
   aucune intervention humaine supplémentaire observée. Aucune opération Git
   effectuée. La publication relève de l'orchestrateur expérimental.

## Mesures et limites de la trace

Tokens et durée totale de la tentative : non enregistrés. Aucun horodatage de
travail publié. Les résultats ci-dessus décrivent les contrôles effectivement
exécutés ; aucune modification de gouvernance n'a été réalisée pendant ce run.
