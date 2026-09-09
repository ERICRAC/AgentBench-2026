# V2 Astra — Calculatrice Core

**Français** · [English (UK)](astra-v2-core.en.md) · [Español](astra-v2-core.es.md) · [Português](astra-v2-core.pt.md)

## Verdict et comparaison

Core réussit dès le premier passage, puis au contrôle indépendant : **6/6 groupes et 14/14 contrôles**. À qualité officielle égale, V1 Astra domine V2 Astra : V2 demande ×7,00 le temps et ×4,75 les tokens. Face à V2 Sol, Astra prend 12,0 % de temps en moins mais 2,3 % de tokens en plus : compromis, sans dominance.

| Run | groupes · contrôles | Temps mural | Entrée + sortie |
| --- | ---: | ---: | ---: |
| Astra V1 Core | 6/6 · 14/14 | 100.175 s | 120 478 |
| Sol V2 Core | 6/6 · 14/14 | 796.534 s | 559 088 |
| Astra V2 Core | 6/6 · 14/14 | 700.994 s | 572 168 |

[Catalogue](../docs/acceptance-tests.md) · [V1 Astra](astra-v1.md) · [V2 Sol](sol-v2-core.md)

## Lecture sociale

Les trois métiers sont SA-01 (contrat/sécurité), SA-02 (architecture/testabilité) et SA-03 (critique QA). MAIN est l'unique écrivain, réparti sur deux sessions neuves. Les analyses et les contradictions convergent sur une grammaire CLI simple ; MAIN produit 17 lignes de décision préalable. SA-03 ne confirme aucun défaut fonctionnel. MAIN décompose son avis en 14 arbitrages : 7 retenus, 3 écartés et 4 non vérifiables dans sa session ; seules la documentation et la traçabilité évoluent.

Les cinq réponses consultantes totalisent 2 995 mots, toutes sous leur plafond ; l'ensemble des messages visibles atteint 3 446 mots. MAIN recopie les avis dans DECISIONS.md (386 lignes), puis le runner retransmet ce document : cette répétition observable augmente le dossier et fait partie du coût mesuré.

Sept threads distincts, mêmes rôles, prompts et runner que V2 Sol, modèle gpt-6-astra/high, contexte client 200k/compaction 180k. Cache inclus : 430 848 tokens ; raisonnement inclus dans la sortie : 1 261. Temps-sessions cumulé : 775,480 s. Les consultants n'ont exécuté aucun outil ; toutes les modifications enregistrées concernent la solution active. Une seule observation par cellule, aucune généralisation statistique.

Les compteurs absents de la restitution candidate sont disponibles dans la capture du relais. Les réserves « non vérifiable » de MAIN portent sur son dossier local ; le PV de l'orchestrateur conserve les mandats et la trace complète des consultants. Le statut V2 non lancé dans le protocole gelé décrit son état lors du gel ; ce rapport enregistre l'exécution.

## Preuves

[PV](../runs/astra-core-v2-001/PV.md) · [Trace JSON](../runs/astra-core-v2-001/trace.json) · [Run JSON](../runs/astra-core-v2-001/run.json) · [DECISIONS](../runs/astra-core-v2-001/solution/DECISIONS.md)
