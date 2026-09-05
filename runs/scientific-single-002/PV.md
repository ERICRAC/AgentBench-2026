# Procès-verbal du run — `scientific-single-002`

## Objet et portée

Ce procès-verbal restitue les interactions observables du run V1 Calculatrice
Scientific. Il a été établi après clôture à partir du flux d'événements du
candidat, des fichiers produits et du contrôle indépendant. Il ne publie ni
raisonnement interne brut, ni heure de travail, ni donnée d'authentification.

## Acteurs

| Acteur | Rôle | Dans le périmètre V1 candidat |
| --- | --- | --- |
| Éric Racineux | commanditaire de l'expérience | hors run |
| Orchestrateur expérimental Codex | crée la tentative, fixe les paramètres, mandate le candidat, vérifie et publie | hors run candidat |
| Agent candidat Codex | analyse, implémente, documente et teste | unique agent du run |
| Consultants ou sous-agents | aucun lancé par le candidat | 0 |
| Vérificateur indépendant | exécute les neuf groupes d'acceptation | arbitre technique |

## Échanges et décisions observables

### PV-001 — Mandat expérimental

**Émetteur → destinataire** — Orchestrateur → agent candidat.

**Mandat** — Réaliser seul le `CHALLENGE.md`, sans lire une autre tentative,
avec la bibliothèque standard et sans exécution dynamique. La session candidate
distincte reçoit `gpt-5.6-sol`, effort `high`, contexte déclaré 200 000 tokens
et compaction à 180 000.

### PV-002 — Prise en compte et conception

**Candidat** — Relit le challenge. Le chemin relatif initial vers le format de
restitution échoue, puis le candidat poursuit sans aide. Il choisit un tokenizer
à liste blanche et un parseur récursif.

**Résultat observable** — Aucun accès à une autre solution dans la trace.

### PV-003 — Réalisation

**Candidat** — Implémente le moteur d'expressions, les fonctions et constantes,
la variable `x`, l'échantillonnage, l'export SVG passif et la CLI avec
historique. Il documente syntaxe, sécurité, API et limites.

**Résultat observable** — Deux fichiers produits dans `solution/`.

### PV-004 — Contrôles ciblés

**Candidat** — Teste les priorités, domaines, noms interdits, discontinuités,
échappement XML, historique et reprise après division par zéro.

**Résultat observable** — Les contrôles ciblés rapportent une réussite.

### PV-005 — Premier arbitrage technique

**Candidat → vérificateur** — Lance la commande officielle.

**Vérificateur** — Quitte avec le code 1 pendant le chargement du module. La
sortie détaillée de ce premier passage n'a pas été capturée ; aucun score
partiel n'est donc reconstruit.

**Candidat** — Diagnostique une interaction entre `dataclass`, le chargeur
dynamique du vérificateur et Python 3.13.

### PV-006 — Correction et second arbitrage

**Candidat** — Remplace la dataclass interne par une classe légère, sans
modifier la grammaire ni les tests.

**Vérificateur** — La seconde passe réussit : **9 tests sur 9**.

**Décision** — Aucun autre défaut confirmé ; la solution est clôturée.

### PV-007 — Collision de gouvernance

**Candidat** — Crée un commit limité aux deux livrables puis tente un push en
appliquant la règle Git globale.

**Infrastructure** — L'authentification SSH bloque le push ; le dépôt distant
n'est pas modifié par le candidat.

**Arbitrage post-run** — Les opérations Git sont désormais interdites aux
candidats et consultants pendant un run.

### PV-008 — Contre-vérification et publication

**Orchestrateur** — Relance la suite sans modifier la solution : **9/9**. Il
extrait les métriques, produit la trace, le rapport et le présent PV, puis
publie les commits.

## Verdict

V1 Scientific comprend **un agent candidat distinct mandaté**, mais **aucun
consultant ou sous-agent à l'intérieur du run candidat**. Verdict indépendant :
**9/9** après une correction autonome. Intervention humaine fonctionnelle :
**0**.

Les métriques détaillées figurent dans la [trace synthétique](trace.md) et le
[rapport public](../../results/scientific-single-002.md).
