# V2.2 allégée — lanceur préparé, réel verrouillé

**Français** · [English (UK)](v2-2-lean-preflight.en.md) · [Español](v2-2-lean-preflight.es.md) · [Português](v2-2-lean-preflight.pt.md)

**Préparation autorisée et réalisée ; aucun candidat réel lancé.** Astra moyen conservé. Le moteur enchaîne maintenant les trois phases avec les nouveaux mandats et les enveloppes allégées ; il ne se limite plus à calculer leur taille.

## Paramètres retenus pour la préparation

| Paramètre | Valeur |
| --- | --- |
| Modèle / effort demandés pour un futur essai | gpt-6-astra / medium |
| Sessions maximales | MAIN initial → REV-01 relecteur → MAIN final |
| Enveloppe JSON par phase | 12 000 caractères Unicode, hors mandat |
| Cible expérimentale | Moins de 100 000 tokens candidat, pas une prévision |
| Arrêt entre sessions | À partir de 150 000 tokens entrée + sortie observés |
| Plafond strict en cours de session | Aucun |
| Rapports finaux | 150 / 300 / 300 mots ; dépassements signalés, jamais tronqués |
| Retry / scientifique / lancement réel | Non autorisés |

Les 60 000 tokens de l'audit précédent étaient une proposition, remplacée pour cette préparation par l'accord sur 150 000. Ni le cache ni le raisonnement ne sont comptés deux fois. Compteur absent/invalide : arrêt et total incomplet explicite, jamais assimilé à zéro.

## Ce qui est raccordé et vérifié

Nouveau répertoire privé obligatoire, contrat et vérificateur copiés sans changement, solution vierge. Construction des prompts depuis les trois mandats allégés, application des configurations de rôles existantes, capture intégrale des réponses synthétiques, contrôle des fichiers protégés et de la lecture seule, instantanés et checkpoints. Les commandes initiales restent archivées mais ne sont plus retransmises ; les commandes du relecteur sont conservées pour l'arbitrage.

**100 tests de maintenance réussis**, dont 18 nouveaux tests d'intégration. Ils couvrent capture complète, transmission allégée, non-réutilisation du dossier, refus du réel avant écriture, limites de taille et de tokens, compteurs manquants/invalides, coûts exposés d'un processus en échec, écritures interdites, thread réutilisé, sortie tronquée, limites de mots et manifeste non autorisable.

Une simulation complète : trois phases, 39 tokens **fictifs**, enveloppes de 1 652 / 2 078 / 2 280 caractères ; aucun verdict de calculatrice. Deux sessions synthétiques de 75 000 tokens bloquent bien la troisième. Les compteurs historiques réinjectés comme fixture terminent à 113 774 : sous le seuil, au-dessus de la cible. Ce n'est pas une nouvelle mesure modèle.

## Limites et livraison suivante

Le seuil ne peut arrêter qu'avant la phase suivante. Un dépassement pendant une session reste possible et enregistré. Si la dernière phase termine en dépassant le seuil, son résultat reste terminé avec dépassement signalé, pas réécrit en interruption. Les limites de mots sont auditées, pas imposées au modèle.

Le CLI n'expose que la simulation ; même modifier le manifeste ne permet pas le réel. Le callback injectable sert aux tests. **L'adaptateur de transport réel, son autorisation nominative et le gel de la nouvelle campagne restent nécessaires avant tout benchmark.** Les contrôles de fichiers prouvent les altérations observées, pas un confinement complet. Aucune économie de quota ou réussite dans une fenêtre d'abonnement garantie. L'historique, la gouvernance générale et le dossier utilisateur non suivi .github/ sont inchangés.

[JSON — CLI simulation](v2-2-lean-preflight.json) · [Manifest](../governance/v2-2-lean-draft.json) · [Launcher](../scripts/run_v2_2_lean.py) · [Tests](../tests/test_v2_2_lean.py) · [Audit](v2-2-cost-audit.md) · [README](../README.md)
