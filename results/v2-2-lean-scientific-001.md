# Essai scientifique allégé — interruption OBS-002

[Français](v2-2-lean-scientific-001.md) · [English (UK)](v2-2-lean-scientific-001.en.md) · [Español](v2-2-lean-scientific-001.es.md) · [Português](v2-2-lean-scientific-001.pt.md)

L'essai réel est arrêté avant tout code : **11 968 tokens, 12,811 s, aucun résultat de calculatrice**. Ce n'est pas un épuisement de quota. Aucun retry effectué.

## Ce qui s'est passé

L'accord humain a été reçu et le lanceur a démarré une session MAIN. Mais le mandat indiquait que son gel seul n'autorisait pas le lancement, sans confirmer au candidat que l'accord était désormais acquis. MAIN a donc demandé cette confirmation et terminé sans utiliser d'outil. Le processus CLI a réussi (code 0), puis le relais a constaté les livrables absents et s'est arrêté (code 1). Le relecteur et MAIN final n'ont pas été lancés.

Il s'agit d'une erreur de transmission de l'autorisation dans le dispositif préparé par l'orchestrateur. Les 135 tests hors modèle validaient les chemins techniques ; leurs faux candidats n'interprétaient pas la condition linguistique d'autorisation. Nous conservons ce défaut sous OBS-002, sans corriger rétroactivement le gel.

## Mesures et vérification

Une session commencée et terminée côté CLI, zéro phase validée. Entrée : 11 810 ; sortie : 158 ; total : 11 968. Cache : 0, inclus dans l'entrée ; raisonnement : 89, inclus dans la sortie. Durée murale : 12,810581794 s ; session : 12,809085513 s. Le seuil 150 000 n'a pas été atteint, l'enveloppe initiale était de 5 023 caractères sur 24 000. Solde de quota et coût de l'orchestrateur : non enregistrés.

Contrôle indépendant : dossier solution vide, défi, script de vérification et suite copiés sans altération. Suite scientifique non exécutée : aucun score 9/9 ou 0/9 n'est attribué. L'état brut garde usage_complete=false, valeur posée par le relais à l'exception ; les compteurs de l'unique processus terminé sont néanmoins présents et publiés.

## Enseignement et prochaine action

Aucune comparaison d'efficacité solo/binôme n'est possible : la collaboration n'a pas commencé. Les résultats historiques restent intacts ; ces 11 968 tokens appartiennent aux essais interrompus, pas aux références terminées.

Correction recommandée pour une nouvelle version : après validation de l'accord, le relais doit dire explicitement au candidat « L'orchestrateur autorise maintenant cette phase ; commence le travail ». Supprimer les réserves ambiguës du message d'exécution, conserver l'autorisation dans le lanceur et tester la présence de cette confirmation. Aucun changement ni nouvel essai appliqué ici : identifiant neuf et accord de relance nécessaires.

## Artefacts

- [PV / messages](../runs/astra-medium-scientific-v2-2-lean-001/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-001/run.json) · [State](../runs/astra-medium-scientific-v2-2-lean-001/state.json).
- [Prompt](../runs/astra-medium-scientific-v2-2-lean-001/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-001/trace.json).
- [Checks](../runs/astra-medium-scientific-v2-2-lean-001/verifications.json) · [Snapshots](../runs/astra-medium-scientific-v2-2-lean-001/snapshots.json).
- [Manifest](../governance/v2-2-lean-scientific-001.json) · [Preflight](v2-2-lean-scientific-preflight.md).
