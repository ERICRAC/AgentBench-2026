# Résultat détaillé — `codex-single-002`

**Français** · [English (UK)](codex-single-002.en.md) · [Español](codex-single-002.es.md) · [Português](codex-single-002.pt.md)

## Résumé exécutif

La seconde référence V1 de la **Calculatrice Core** atteint **6 tests sur 6**
dès son premier passage officiel et lors de la vérification indépendante. Elle
a été exécutée par un seul agent, sans sous-agent ni aide fonctionnelle
humaine, avec le modèle, l'effort et le contexte explicitement épinglés.

Cette réplication devient la référence courante pour préparer V2. Elle ne
supprime pas `codex-single-001`, conservée comme première observation
historique aux paramètres incomplets.

## Identité et résultat

| Donnée | Valeur |
| --- | --- |
| Mode | V1 · Codex seul |
| Objectif | Calculatrice Core |
| Modèle | `gpt-5.6-sol` |
| Effort | `high` |
| Codex CLI | `0.152.1` |
| Fenêtre déclarée | 200 000 tokens |
| Compaction | 180 000 tokens, portée `total` |
| Prompt | [`prompts/codex-single.md`](../prompts/codex-single.md) |
| Sous-agents | 0 |
| Intervention humaine fonctionnelle | 0 |
| Premier passage | **6/6** |
| Verdict indépendant final | **6/6** |

## Traitement réalisé

Le candidat a séparé le contrat public `calculate`, l'analyse de la ligne de
commande et la boucle interactive. Les quatre opérations utilisent des
branches explicites ; `ValueError` et `ZeroDivisionError` sont conservées au
niveau métier puis converties en messages lisibles dans la CLI. Les lignes
vides, erreurs, fins de flux et interruptions clavier sont traitées sans
traceback.

Après le premier 6/6, un contrôle manuel lancé depuis un mauvais répertoire a
révélé que le README décrivait son point de départ de façon ambiguë. Seule la
documentation a été corrigée ; aucun défaut fonctionnel n'a été trouvé.

## Vérification et mesures

```bash
python3 scripts/verify.py --solution runs/codex-single-002/solution
```

| Indicateur | Valeur observée |
| --- | ---: |
| Durée murale arrondie | 193 s |
| Entrée | 549 279 tokens |
| Entrée mise en cache | 480 384 tokens |
| Sortie | 7 182 tokens |
| Raisonnement inclus dans la sortie | 2 881 tokens |
| Entrée + sortie | 556 461 tokens |
| Commandes terminées | 17 |
| Lots de modifications | 2 |
| Fichiers livrés | 2 |
| Code / documentation | 84 / 44 lignes |

Les tokens d'entrée sont cumulés sur les tours et incluent le cache ; ils ne
décrivent pas une fenêtre simultanée supérieure à la limite déclarée.

## Incident de gouvernance

Le candidat a interprété la règle globale de livraison Git malgré la limite
d'écriture du run. Son commit contient uniquement les deux livrables, mais la
tentative de push constitue du bruit organisationnel inutile. Le distant n'a
pas été modifié par le candidat. Le protocole suivant interdit explicitement
aux candidats de lancer `git add`, `git commit` ou `git push`.

## Conclusion

La conformité Core est reproduite sans correction fonctionnelle. Avec un
score déjà maximal, V2 ne pourra démontrer un intérêt qu'en réduisant le coût,
en améliorant la qualité non couverte par les tests ou en détectant plus tôt
les risques — pas en revendiquant simplement le même 6/6.

La [trace synthétique](../runs/codex-single-002/trace.md) et les
[métadonnées](../runs/codex-single-002/run.json) rendent le parcours auditable.
