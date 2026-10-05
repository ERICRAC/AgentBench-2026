# Audit de coût V2.2 — variante allégée hors modèle

**Français** · [English (UK)](v2-2-cost-audit.en.md) · [Español](v2-2-cost-audit.es.md) · [Português](v2-2-cost-audit.pt.md)

**Aucun candidat lancé.** Le run 002 terminé reste intact. Le prototype réduit les données transmises, pas la qualité démontrée ni le quota mesuré.

## Mesures exactes

Les captures publiques normalisées donnent les tailles suivantes, en **caractères Unicode, pas en tokens**. Le calcul compare uniquement l'enveloppe JSON, à sérialisation identique ; le texte des nouveaux mandats n'entre pas dans cette économie.

| Phase | Prompt historique complet | Données historiques | Données proposées |
| --- | ---: | ---: | ---: |
| MAIN initial | 3 430 | 1 652 | 1 652 |
| REV-01 | 13 927 | 12 084 | 6 886 |
| MAIN final | 16 388 | 14 347 | 9 149 |

Retrait total : **10 396 caractères**, soit **37,0 %** des 28 083 caractères d'enveloppes cumulées. Les commandes/sorties MAIN initial représentent 5 062 caractères JSON retransmis dans chacune des deux phases suivantes. Le reste retiré correspond au message intermédiaire et à sa sérialisation. Contrat, fichiers complets, transmissions finales et preuves de commandes du relecteur sont conservés.

Les 110 511 tokens d'entrée historiques ne sont pas la longueur d'un prompt : ce sont des compteurs cumulés de sessions, avec 65 280 tokens de cache inclus. Sortie : 3 263. Les captures ne permettent pas d'attribuer exactement tous les tokens au contexte système, aux outils ou aux transferts. **Aucune estimation de baisse des tokens ou du quota n'est revendiquée.**

## Variante proposée, non gelée

Trois sessions et deux métiers conservés, Astra moyen inchangé comme proposition. Rapports finaux proposés : 150 / 300 / 300 mots, au lieu de 600 / 1 200 / 1 200. Ce raccourcissement n'est pas mesuré par le tableau. Les traces complètes restent archivées, mais les commandes initiales ne sont plus injectées dans les deux phases suivantes.

**Compromis :** le relecteur dispose de moins de preuves sur les tests initiaux. Il doit distinguer une affirmation MAIN d'une exécution qu'il a vérifiée. Une revue plus courte peut omettre un point : dépassement à signaler, jamais troncature silencieuse. Ce changement ouvre une nouvelle condition, sans modifier le protocole historique.

## Arrêts testés et limites

Le simulateur ne contient aucun transport réel. Dix tests ajoutés couvrent trois réponses synthétiques, refus du réel, taille excessive avant session, seuil exact, dépassement visible, compteur absent, échec sans retry, limites invalides, conservation des données utiles et calcul d'audit.

Proposition à arbitrer : enveloppe limitée à **12 000 caractères par phase**, refus intégral plutôt que troncature ; arrêt entre sessions dès **60 000 tokens cumulés observés**. Ce sont des paramètres proposés, ni gelés ni une limite du compte. Avec les coûts historiques inchangés, le seuil aurait arrêté après la revue à 66 038 tokens : dépassement de 6 038 et aucun verdict final. **Un contrôle entre sessions ne borne pas une session en cours.** Aucun watchdog ni plafond natif validé n'est implémenté ici.

Les valeurs 100 tokens/1 000 caractères des tests sont des fixtures, pas des recommandations de budget. Les 82 tests de maintenance réussissent ; aucun score de calculatrice nouveau. Le prochain arbitrage porte sur la perte d'information acceptée et la politique d'arrêt. Ne pas lancer la scientifique, ni une référence solo, sans accord distinct.

[JSON](v2-2-cost-audit.json) · [Audit / simulation](../scripts/audit_v2_2_cost.py) · [Tests](../tests/test_v2_2_cost.py) · [MAIN initial](../prompts/v2-2-lean-initial-draft.md) · [REV-01](../prompts/v2-2-lean-review-draft.md) · [MAIN final](../prompts/v2-2-lean-final-draft.md) · [Run 002](v2-2-supervised-core-002.md)
