# Résultats

**Français** · [English (UK)](README.en.md) · [Español](README.es.md) · [Português](README.pt.md)

Les V1 antérieures sont [archivées](ARCHIVE_V1.md). Les mentions « référence courante » dans leurs rapports décrivent leur statut historique, pas la campagne Astra.

**Parcours conseillé :** [comprendre les 15 groupes et 71 contrôles](../docs/acceptance-tests.md)
→ [voir les résultats courants](#résultats-publiés) → ouvrir le rapport, puis le
PV et la trace du run. Les anciens rapports utilisent parfois le raccourci
`6/6` ou `9/9` : il désigne des groupes `unittest`, pas toutes les assertions.

[V2 Astra medium](astra-medium-v2.md) · [Astra/high](astra-v2-retired.md) · [Guide](../docs/reading-guide.md)

## Résultats publiés

| Tentative | Mode | Objectif | Résultat | Statut | Détails |
| --- | --- | --- | --- | --- | --- |
| `astra-core-v1-002` | Codex seul | Calculatrice Core | 6/6 groupes · 14/14 contrôles | Référence Astra | [Rapport complet](astra-v1.md) |
| `astra-scientific-v1-002` | Codex seul | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | Référence Astra | [Rapport complet](astra-v1.md) |
| `sol-core-v1-001` | Codex seul | Calculatrice Core | 6/6 groupes · 14/14 contrôles | Contrôle modèle | [Comparaison](sol-vs-astra-v1.md) |
| `sol-scientific-v1-001` | Codex seul | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | Contrôle modèle | [Comparaison](sol-vs-astra-v1.md) |
| `sol-core-v2-001` | Équipe Codex | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Sol publiée | [Rapport, PV et trace](sol-v2-core.md) |
| `sol-scientific-v2-001` | Équipe Codex | Calculatrice Scientific | 9/9 groupes · 57/57 contrôles | V2 Sol publiée | [Synthèse, PV et trace](sol-v2.md) |
| `astra-core-v2-001` | Équipe Astra | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Astra | [Rapport](astra-v2-core.md) |
| `astra-medium-core-v2-001` | Équipe Astra medium | Calculatrice Core | 6/6 groupes · 14/14 contrôles | V2 Astra medium | [Rapport](astra-medium-v2.md) |

## Données conservées

Pour chaque tentative, conserver au minimum :

- identifiant et mode d'exécution ;
- date, environnement et version de Codex ;
- résultat du premier passage des tests ;
- résultat final ;
- durée totale ;
- interventions humaines ;
- remarques et limites observées.
