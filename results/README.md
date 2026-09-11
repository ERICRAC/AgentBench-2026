# Résultats

**Français** · [English (UK)](README.en.md) · [Español](README.es.md) · [Português](README.pt.md)

**V2.2 : 57 tests de maintenance réussis ; trois sondes de CLI restent à 7/8.** Le paquet officiel séparé reproduit le blocage du catalogue. Aucun modèle lancé ; installations existantes inchangées. **Astra élevé : historique uniquement.** [CLI](v2-2-cli-qualification.md)

[Les cinq runs V2 en 2 minutes chacun](run-summaries/index.md) · [📖 Comment lire et interpréter un run AgentBench](../docs/reading-guide.md)

[Conclusions — quand le collectif devient-il rentable ?](CONCLUSIONS.md)

Les V1 antérieures sont [archivées](ARCHIVE_V1.md). Les mentions « référence courante » dans leurs rapports décrivent leur statut historique, pas la campagne Astra.

**Parcours conseillé :** [comprendre les 15 groupes et 71 contrôles](../docs/acceptance-tests.md)
→ [voir les résultats courants](#résultats-publiés) → ouvrir le rapport, puis le
PV et la trace du run. Les anciens rapports utilisent parfois le raccourci
`6/6` ou `9/9` : il désigne des groupes `unittest`, pas toutes les assertions.

[V2 Astra medium](astra-medium-v2.md) · [Astra/high](astra-v2-retired.md) · [Guide](../docs/reading-guide.md)

## Référence V1 Astra moyen — deux calculatrices terminées

**V1 contre V2, Astra moyen : même score officiel sur les deux défis.** V2 utilise ×3,56 le temps et ×4,49 les tokens au total. La relecture apporte toutefois des corrections de robustesse hors score. [Bilan complet et preuves](astra-medium-v1-v2.md)

## Résultats publiés

| Tentative | Mode | Objectif | Résultat | Statut | Détails |
| --- | --- | --- | --- | --- | --- |
| `astra-medium-core-v1-001` | V1 solo Astra medium | Simple | 6/6 groupes · 14/14 contrôles | completed | [Report](astra-medium-v1-core.md) |
| `astra-medium-scientific-v1-001` | V1 solo Astra medium | Scientifique | 9/9 groupes · 57/57 contrôles | completed | [Bilan complet et preuves](astra-medium-v1-v2.md) |
| `astra-core-v1-002` | Codex seul | Calculatrice Core | 6/6 groupes · 14/14 contrôles | Référence Astra | [Rapport complet](astra-v1.md) |
| `astra-scientific-v1-002` | Codex seul | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | Référence Astra | [Rapport complet](astra-v1.md) |
| `sol-core-v1-001` | Codex seul | Calculatrice Core | 6/6 groupes · 14/14 contrôles | Contrôle modèle | [Comparaison](sol-vs-astra-v1.md) |
| `sol-scientific-v1-001` | Codex seul | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | Contrôle modèle | [Comparaison](sol-vs-astra-v1.md) |
| `sol-core-v2-001` | Équipe Codex | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Sol publiée | [Rapport, PV et trace](sol-v2-core.md) |
| `sol-scientific-v2-001` | Équipe Codex | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | V2 Sol publiée | [Synthèse, PV et trace](sol-v2.md) |
| `astra-core-v2-001` | Équipe Astra | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Astra | [Rapport](astra-v2-core.md) |
| `astra-medium-core-v2-001` | Équipe Astra medium | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Astra medium | [Rapport](astra-medium-v2.md) |
| `astra-medium-scientific-v2-001` | Équipe Astra medium | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | V2 Astra medium | [Rapport](astra-medium-v2.md) |

## Données conservées

Pour chaque tentative, conserver au minimum :

- identifiant et mode d'exécution ;
- date, environnement et version de Codex ;
- résultat du premier passage des tests ;
- résultat final ;
- durée totale ;
- interventions humaines ;
- remarques et limites observées.
