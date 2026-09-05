# Procès-verbal du run — `codex-single-002`

## Objet et portée

Ce procès-verbal restitue les interactions observables du run V1 Calculatrice
Core. Il a été établi après clôture à partir du flux d'événements du candidat,
des fichiers produits et du contrôle indépendant. Il ne publie ni raisonnement
interne brut, ni heure de travail, ni donnée d'authentification.

## Acteurs

| Acteur | Rôle | Dans le périmètre V1 candidat |
| --- | --- | --- |
| Éric Racineux | commanditaire de l'expérience | hors run |
| Orchestrateur expérimental Codex | crée la tentative, fixe les paramètres, mandate le candidat, vérifie et publie | hors run candidat |
| Agent candidat Codex | analyse, implémente, documente et teste | unique agent du run |
| Consultants ou sous-agents | aucun lancé par le candidat | 0 |
| Vérificateur indépendant | exécute les six contrôles d'acceptation | arbitre technique |

## Échanges et décisions observables

### PV-001 — Mandat expérimental

**Émetteur → destinataire** — Orchestrateur → agent candidat.

**Mandat** — Réaliser seul le `CHALLENGE.md`, écrire uniquement dans
`solution/`, ne modifier ni tests ni spécification, puis lancer le vérificateur.
La session candidate distincte reçoit `gpt-5.6-sol`, effort `high`, contexte
déclaré 200 000 tokens et compaction à 180 000.

**Décision** — Aucun consultant ni sous-agent autorisé en V1.

### PV-002 — Prise en compte du contrat

**Candidat** — Relit le challenge, retrouve le vérificateur et le format de
restitution à la racine. Il annonce limiter ses écritures à `solution/`.

**Résultat observable** — Aucune autre solution consultée dans la trace.

### PV-003 — Réalisation

**Candidat** — Crée `calculator.py` et son README. Il sépare logique métier,
analyse de l'entrée et boucle interactive, sans dépendance externe ni exécution
dynamique.

**Résultat observable** — Deux fichiers produits dans `solution/`.

### PV-004 — Premier arbitrage technique

**Candidat → vérificateur** — Lance la commande officielle.

**Vérificateur** — **6 tests sur 6 réussis**.

**Décision** — Aucune correction fonctionnelle nécessaire.

### PV-005 — Autocontrôle documentaire

**Candidat** — Lance un scénario manuel depuis un mauvais répertoire. L'échec
révèle une formulation ambiguë du README sur le répertoire de lancement.

**Décision** — Corriger uniquement la documentation. Le second passage du
vérificateur reste à **6/6**.

### PV-006 — Collision de gouvernance

**Candidat** — Interprète la règle Git globale et crée un commit contenant ses
deux livrables, puis tente un push malgré la frontière du run.

**Infrastructure** — Le push échoue ; le dépôt distant n'est pas modifié par le
candidat.

**Arbitrage post-run** — La livraison Git est désormais explicitement réservée
à l'orchestrateur, et cet incident reste compté comme bruit de gouvernance.

### PV-007 — Contre-vérification et publication

**Orchestrateur** — Relance la suite sans modifier la solution : **6/6**. Il
extrait les métriques, produit la trace, le rapport et le présent PV, puis
publie les commits.

## Verdict

V1 Core comprend **un agent candidat distinct mandaté**, mais **aucun
consultant ou sous-agent à l'intérieur du run candidat**. Verdict indépendant :
**6/6**. Intervention humaine fonctionnelle : **0**.

Les métriques détaillées figurent dans la [trace synthétique](trace.md) et le
[rapport public](../../results/codex-single-002.md).
