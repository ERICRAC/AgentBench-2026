# Procès-verbal — Calculator V1

1. **Mandat.** L'utilisateur demande une solution complète et documentée,
   réalisée seul, avec écritures limitées à `solution/` et exécution du
   vérificateur imposé. Le candidat a lu `../CHALLENGE.md` avant modification.
2. **Rôles.** Le commanditaire est l'utilisateur. L'orchestrateur expérimental
   mandate cette session et conserve la responsabilité de la publication.
   Le candidat est Codex en mode V1 ; il n'a utilisé aucun consultant,
   sous-agent ou modèle externe. Le vérificateur indépendant est
   `scripts/verify.py` du dépôt.
3. **Réalisation.** Création de `calculator.py` et `README.md`. Les opérations
   sont sélectionnées explicitement, sans évaluation dynamique ni dépendance
   externe. La CLI sépare les trois éléments de chaque expression et capture
   les erreurs attendues pour poursuivre la saisie.
4. **Incident mineur.** Une recherche initiale de chemins relatifs vers les
   scripts et la gouvernance a échoué ; les chemins ont été corrigés.
   Aucune modification du dépôt hors `solution/` n'a été effectuée par le
   candidat.
5. **Contrôle.** Depuis le dossier de la tentative, exécution de
   `python3 ../../scripts/verify.py --solution solution` : code de sortie 0,
   six tests réussis, verdict `OK`. Les contrôles couvrent la présence des
   livrables, les quatre opérations et variantes numériques, les opérateurs
   invalides, la division par zéro, l'absence d'évaluation dynamique et la
   récupération CLI après erreur avec sortie propre. Durée indiquée par le
   vérificateur : 0,013 seconde.
6. **Conclusion.** Aucun défaut confirmé par le vérificateur ; aucune
   correction fonctionnelle nécessaire. Aucun test ni script du dépôt n'a
   été modifié. Aucune opération Git n'a été lancée. Tokens et durée totale
   du candidat : non enregistrés. Aucune évolution de gouvernance proposée.
