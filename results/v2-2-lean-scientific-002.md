# V2.2 scientifique allégée — essai 002 terminé

[Français](v2-2-lean-scientific-002.md) · [English (UK)](v2-2-lean-scientific-002.en.md) · [Español](v2-2-lean-scientific-002.es.md) · [Português](v2-2-lean-scientific-002.pt.md)

**Essai scientifique 002 réussi : 9/9 groupes, 57/57 contrôles, 141 794 tokens, 207,630 s.** Aucun changement après revue. Le binôme reste plus coûteux que le solo scientifique historique ; comparaison exploratoire.

## Résultat et déroulement

Trois sessions Astra moyen : MAIN développe et exécute 78 contrôles locaux, REV-01 relit statiquement sans défaut confirmé, MAIN final arbitre puis réussit le vérificateur officiel au premier passage. L'orchestrateur confirme indépendamment les 9 groupes / 57 contrôles sur les versions initiale et finale, identiques octet pour octet. Les 78 contrôles du candidat ne sont pas des tests indépendants supplémentaires.

La confirmation explicite de lancement a été transmise : OBS-002 ne s'est pas reproduit. Aucun arrêt quota ni retry. Les trois enveloppes ont mesuré 5 023, 21 226 et 22 569 caractères, sous le plafond de 24 000. Les rapports finaux respectent leurs limites de mots.

## Coûts et efficacité

| Condition | Tokens entrée + sortie | Durée (s) | Score |
| --- | ---: | ---: | --- |
| Solo V1 historique | 119 388 | 188,560 | 9/9 · 57/57 |
| V2 historique | 570 382 | 648,008 | 9/9 · 57/57 |
| Binôme allégé 002 | 141 794 | 207,630 | 9/9 · 57/57 |

Face au solo historique : **+18,8 % de tokens, +10,1 % de temps**, sans gain de score ni correction. Face à V2 historique : **−75,1 % de tokens, −68,0 % de temps**. Le binôme allégé réduit fortement le surcoût du collectif, mais ne dépasse pas le solo sur ce cas.

Entrée : 134 416, dont cache 77 440 ; sortie : 7 378, dont raisonnement 397. Cache et raisonnement ne s'ajoutent pas au total. Seuil intersession 150 000 non atteint, pas de plafond strict garanti. Temps mural 207,630 s ; somme des sessions 207,620 s. Quota disponible et coûts d'orchestration, préparation et publication non enregistrés.

L'essai 001 interrompu reste séparé : 11 968 tokens, 12,811 s. Sous-total des seuls essais scientifiques allégés 001+002 : **153 762 tokens, 220,441 s**. Ce n'est pas le coût de toute la campagne.

## Ce que la revue apporte — et ne démontre pas

REV-01 confirme la structure et distingue des preuves absentes les 78 contrôles annoncés par MAIN. Il signale la limite des singularités entre échantillons, déjà documentée. MAIN final retient trois constats et marque un point non vérifiable faute de sorties transmises. Aucun défaut confirmé, aucune correction, aucun gain de qualité démontré ; une validation supplémentaire explicite, dont la prévention d'erreurs n'est pas mesurée ici.

## Limites et suite

Nouvelle campagne astra-medium-lean-003, mêmes modèle demandé et effort mais prompts, transmission, environnement et cache différents des références. Un seul essai par condition ; la version serveur exacte et celle de la CLI au lancement ne sont pas enregistrées. Ces différences interdisent d'attribuer les écarts à la seule organisation ou de présenter simple et scientifique comme une paire strictement homogène.

Aucun nouveau lancement automatique. Recommandation : analyser ces résultats avant de dépenser davantage. Le seuil où plusieurs agents deviennent plus efficaces reste inconnu ; un défi réellement parallélisable ou une référence solo contemporaine nécessiterait un protocole et un budget séparément approuvés.

## Artefacts

- [PV / messages / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-002/run.json) · [Prompts](../runs/astra-medium-scientific-v2-2-lean-002/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-002/trace.json).
- [Solution](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md) · [Code](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py) · [Checks](../runs/astra-medium-scientific-v2-2-lean-002/verifications.json).
- [V1/V2](astra-medium-v1-v2.md) · [OBS-002 / 001](v2-2-lean-scientific-001.md).
- [57 checks](../docs/acceptance-tests.md) · [Manifest](../governance/v2-2-lean-scientific-002.json).

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-2-lean-002/solution
```
