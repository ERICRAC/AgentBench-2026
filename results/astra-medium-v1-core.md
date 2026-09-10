# V1 Astra moyen — calculatrice simple

**Français** · [English (UK)](astra-medium-v1-core.en.md) · [Español](astra-medium-v1-core.es.md) · [Português](astra-medium-v1-core.pt.md)

La tentative astra-medium-core-v1-001 est terminée : **6/6 groupes, soit 14/14 contrôles**, dès le premier passage, confirmés indépendamment. **98,572 s et 98 496 tokens entrée + sortie.** Aucun candidat scientifique lancé.

## Le run en deux minutes

Un développeur candidat dans une session éphémère Astra moyen, aucun consultant ni sous-agent. L’orchestrateur externe mandate, capture et publie ; il ne participe pas à la résolution.

Le candidat lit le défi, choisit des branches explicites pour les quatre opérations, sépare calculate de la CLI et traite les entrées comme trois éléments séparés par des blancs. Il documente lancement, exemples, erreurs et précision flottante. Une recherche de chemins relatifs échoue, puis il corrige les chemins de lecture. Il écrit le code et le README, passe le vérificateur, ajoute son PV puis termine. Aucun correctif fonctionnel après le premier verdict ; aucun test supplémentaire enregistré.

51 lignes de code avec trois docstrings (module, calculate, main), README de 72 lignes, PV de 29 lignes. Cela facilite la lecture sans constituer un test de maintenabilité. Le PV supplémentaire dépasse la liste des deux livrables du challenge : tension de journalisation conservée, non sanctionnée par la suite. Aucune solution retouchée après la clôture.

## Ce qui a été vérifié

- [x] Présence de calculator.py et README.md — 2 contrôles.
- [x] Absence d’appels directs eval/exec — 1 contrôle syntaxique, pas une preuve exhaustive de sécurité.
- [x] Quatre opérations : 2 + 3 = 5 ; -2 - 3 = -5 ; 1.5 * 2 = 3 ; 7 / 2 = 3.5 — 4 cas dans un groupe.
- [x] Opérateur % rejeté par ValueError — 1 contrôle.
- [x] Division par zéro : ZeroDivisionError — 1 contrôle.
- [x] CLI : sortie 0, absence de traceback, résultats 5 et -8, diagnostic d’erreur — 5 contrôles.

Total : six méthodes unittest, quatorze contrôles. Le candidat puis l’orchestrateur ont exécuté la même suite figée avec succès. Les quatre opérations ne sont donc pas comptées comme un seul calcul. [Catalogue détaillé](../docs/acceptance-tests.md).

## V1 contre V2 — même modèle et effort, calculatrice simple

| Mesure | V1 solo | V2 consultative |
| --- | ---: | ---: |
| Premier passage / final | 6/6 / 6/6 | 6/6 / 6/6 |
| Contrôles finaux | 14/14 | 14/14 |
| Temps | 98.572 s | 375.169 s |
| Entrée + sortie | 98496 | 408616 |
| Sessions / métiers candidats | 1 / 1 | 7 / 4 |
| Corrections fonctionnelles après premier passage | 0 | 0 |

**Sur cette cellule, V1 domine V2 selon les mesures officielles : même résultat, moins de temps et de tokens.** V2 représente ×3,81 le temps et ×4,15 les tokens, soit +276,597 s et +310 120 tokens. En V2, la relecture avait surtout précisé la documentation, sans correction fonctionnelle. Ce n’est pas une comparaison entre deux cerveaux différents : modèle demandé et effort sont identiques ; l’organisation change.

Cela renforce le constat d’un surcoût du collectif consultatif sur ce petit exercice. Ce n’est ni une preuve que tout collectif échoue, ni la mesure d’une équipe de développeurs parallèles. Aucune analyse inter-agents à inventer pour la V1.

## Coûts et limites

Entrée 96 182 ; cache 76 800 inclus ; sortie 2 314 ; raisonnement 104 inclus. Total 98 496, sans double comptage. Durée candidate comprenant lancement/clôture CLI ; préparation, contrôle indépendant et publication exclus. Aucun nouveau plafond imposé, aucune instrumentation nouvelle.

Contexte 200k et compaction 180k configurés, CLI 0.153.4. Le succès confirme une session exécutée avec la configuration soumise, pas un snapshot serveur immuable ni une démonstration du plafond de contexte. Référence V1 après V2, une seule observation par cellule, conditions de charge/cache variables. Les frontières de mesure V1/V2 diffèrent légèrement ; V2 inclut le relais. Le premier passage V2 suit la critique obligatoire. [Préflight et réserves](astra-medium-v1-preflight.md).

La conformité mesurée reste limitée à ces tests. Les défauts hors couverture et la maintenabilité ne sont pas quantifiés.

## Preuves et suite

[PV / verbatim](../runs/astra-medium-core-v1-001/PV.md) · [trace.json](../runs/astra-medium-core-v1-001/trace.json) · [run.json](../runs/astra-medium-core-v1-001/run.json) · [Code](../runs/astra-medium-core-v1-001/solution/calculator.py) · [README](../runs/astra-medium-core-v1-001/solution/README.md) · [V2](astra-medium-v2.md) · [Conclusions](CONCLUSIONS.md)

La scientifique reste prepared_not_started, dossier solution/ vide et autorisation false. Son lancement demandera un nouvel accord après publication de ce rapport.
