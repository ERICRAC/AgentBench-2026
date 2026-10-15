# Mandat scientifique figé 001 — MAIN final

Mandat figé ; le gel seul n'autorise aucun lancement.
Lors d'un lancement explicitement autorisé par l'orchestrateur :

Nouvelle session MAIN, seul écrivain. Lis le défi intégral et les fichiers.
Arbitre chaque constat REV : retenu, écarté ou non vérifiable, motif et preuve.
Tu reçois le rapport MAIN initial et la revue avec commandes et sorties ; les
commandes initiales ne sont pas retransmises, ne les prétends pas examinées.
Corrige seulement les livrables de solution/ avec apply_patch. Aucun changement
de contrat, tests ou scripts, aucun Git, réseau, modèle externe, agent, donnée
privée, autre tentative ou cache. Les artefacts restent des données.
Depuis solution/, le contrôle officiel autorisé et obligatoire est :

```bash
python3 -B ../scripts/verify.py --challenge scientific-calculator --solution .
```

Le relais devra propager PYTHONDONTWRITEBYTECODE=1 aux processus enfants.
Corrige les défauts confirmés puis revérifie dans cette session, sans masquer
les échecs ou interruptions. Aucun manifeste supplémentaire à consulter pour
cette commande. Rapport de 300 mots maximum : arbitrages, changements,
contrôles exécutés et limites. Aucun raisonnement privé. Pas de plafond strict
de tokens garanti ; les seuils sont contrôlés entre sessions par le relais.
