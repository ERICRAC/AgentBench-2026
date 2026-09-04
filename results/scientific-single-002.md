# Résultat détaillé — `scientific-single-002`

**Français** · [English (UK)](scientific-single-002.en.md) · [Español](scientific-single-002.es.md) · [Português](scientific-single-002.pt.md)

## Résumé exécutif

La seconde référence V1 de la **Calculatrice Scientific** atteint un verdict
final de **9 tests sur 9**. Un seul agent a livré un moteur d'expressions sûr,
l'échantillonnage, l'export SVG et la CLI sans dépendance externe ni aide
fonctionnelle humaine.

Le premier vérificateur officiel a échoué pendant le chargement du module à
cause de l'interaction connue entre `dataclass` et le chargeur dynamique sous
Python 3.13. Une correction ciblée a suffi. La réplication devient la référence
courante pour V2, tandis que `scientific-single-001` reste publiée.

## Identité et résultat

| Donnée | Valeur |
| --- | --- |
| Mode | V1 · Codex seul |
| Objectif | Calculatrice Scientific |
| Modèle / effort | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Fenêtre / compaction | 200 000 / 180 000 tokens, portée `total` |
| Prompt | [`prompts/scientific-single.md`](../prompts/scientific-single.md) |
| Sous-agents / intervention humaine | 0 / 0 |
| Premier passage | échec au chargement du module |
| Verdict candidat final | **9/9** |
| Verdict indépendant final | **9/9** |

## Traitement réalisé

La solution repose sur un tokenizer à liste blanche et un parseur récursif :
aucune chaîne n'est confiée à l'interpréteur Python. Les fonctions et
constantes sont mappées explicitement, les domaines réels et nombres non finis
sont normalisés, et seule la variable `x` est permise.

L'échantillonnage conserve les bornes et remplace les valeurs indéfinies par
`None`. Le SVG adapte son échelle, échappe le titre, trace les axes et produit
des polylignes séparées sans script ni ressource externe. La CLI gère l'aide,
le tracé, l'historique, son effacement et la reprise après erreur.

## Parcours de validation

| Étape | Résultat | Action |
| --- | --- | --- |
| Contrôles ciblés | réussis | aucune |
| Vérificateur officiel 1 | code 1 au chargement | remplacement de la dataclass interne |
| Vérificateur officiel 2 | **9/9** | clôture du candidat |
| Vérification indépendante | **9/9** | aucune modification |

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/scientific-single-002/solution
```

## Mesures

| Indicateur | Valeur observée |
| --- | ---: |
| Durée murale arrondie | 541 s |
| Entrée | 587 315 tokens |
| Entrée mise en cache | 541 312 tokens |
| Sortie | 16 177 tokens |
| Raisonnement inclus dans la sortie | 6 289 tokens |
| Entrée + sortie | 603 492 tokens |
| Commandes terminées | 16 |
| Lots de modifications | 2 |
| Code / documentation | 487 / 97 lignes |

Les tokens d'entrée sont cumulés sur les tours et incluent le cache ; ils ne
représentent pas une fenêtre de contexte simultanée de 587 315 tokens.

## Limites et gouvernance

Le chargeur du vérificateur reste biaisé envers certaines constructions
`dataclass`. Conformément à la gouvernance, la suite figée n'est pas modifiée
silencieusement. L'échantillonnage uniforme peut également manquer une
discontinuité placée entre deux points.

Le candidat a créé un commit limité à sa solution puis tenté un push en
appliquant la règle Git globale. L'authentification a bloqué l'opération et le
distant n'a pas été modifié. Cette collision est corrigée pour les futurs runs.

La [trace synthétique](../runs/scientific-single-002/trace.md) et les
[métadonnées](../runs/scientific-single-002/run.json) conservent les preuves.
