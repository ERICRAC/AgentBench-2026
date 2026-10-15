# PV — astra-medium-scientific-v2-2-lean-001

## Identification

- Commanditaire : Éric Racineux ; accord explicite pour un seul essai.
- Orchestrateur expérimental : assistant principal, hors candidat.
- RELAY : lanceur mécanique, hors équipe candidate ; gel 16f300a.
- MAIN : développeur, seul écrivain autorisé dans solution/, Astra moyen.
- REV-01 : relecteur critique prévu, **non lancé**.
- MAIN final : session d'arbitrage prévue, **non lancée**.
- Contexte configuré : 200 000 ; compaction : 180 000 total.
- Vérificateur indépendant : suite scientifique figée, non exécutée faute de livrables.
- Résultat : interruption du protocole, aucun score scientifique.

## MSG-001 — RELAY → MAIN initial

Le [prompt exact](prompts.json) contient le mandat ci-dessous, le dossier courant,
la commande officielle réservée à P3 et le défi intégral dans une enveloppe JSON.
Il compte 6 400 caractères, dont 5 023 pour l'enveloppe. Aucun contenu omis
dans l'artefact publié. Le [mandat figé](../../prompts/v2-2-lean-scientific-001-initial.md)
et le [défi](CHALLENGE.md) sont accessibles séparément.

Point déterminant du mandat, mot pour mot :

> Mandat figé ; le gel seul n'autorise aucun lancement.
> Lors d'un lancement explicitement autorisé par l'orchestrateur :

**Analyse :** le lanceur avait reçu la confirmation nominative, mais aucune
phrase du prompt ne confirmait que cette condition était satisfaite maintenant.
La configuration désignait MAIN comme candidat ; cela n'a pas suffi à lever
la réserve. C'est un défaut de transmission du protocole, pas un défaut de calcul.

## MSG-002 — MAIN initial → RELAY

Durée de session : 12,809 s. Entrée : 11 810 ; cache : 0 ; sortie : 158 ;
raisonnement comptabilisé dans la sortie : 89. Thread dans [run.json](run.json).
Texte intégral retourné :

> CHALLENGE lu intégralement. Le mandat précise que son gel seul n’autorise aucun lancement ; aucune autorisation explicite de lancement n’est fournie.
> 
> Aucun fichier modifié, aucun contrôle exécuté. En attente de l’autorisation explicite de l’orchestrateur pour la phase MAIN initial.

**Analyse :** MAIN demande une autorisation, ne lance aucun outil et ne produit
aucun fichier. Il ne s'agit pas d'une revue, ni d'un échange entre développeur et
consultant. Aucune discussion multi-agent n'a commencé.

## Arbitrages et contrôles

| ID | Source | Décision | Preuve et effet |
| --- | --- | --- | --- |
| DEC-001 | Accord humain | RELAY lance une fois | Réservation et commande avec identifiant exact |
| DEC-002 | MSG-002 | Arrêt conservé, aucune relance | Code CLI 0, puis erreur Missing or extra deliverable ; code lanceur 1 |
| DEC-003 | Contrôle indépendant | Aucun score de calculatrice attribué | Dossier solution vide ; contrat et suite inchangés |
| DEC-004 | OBS-002 | Proposer une transmission explicite de l'accord dans une future version | Non appliquée au protocole figé ; nouveau run et nouvel accord nécessaires |

## Analyse sociale et expérimentale

- Deux messages visibles : un mandat et une réponse ; zéro échange entre candidats.
- Une demande de clarification de MAIN à RELAY ; aucune réponse candidate supplémentaire.
- Zéro recommandation de consultant, zéro correction, aucune revue ni arbitrage MAIN final.
- L'agent interprète prudemment la condition d'autorisation. Cette observation
  porte sur un seul prompt, pas sur une propriété générale du modèle.
- Les tests synthétiques valident les branchements techniques, pas la manière
  dont un modèle interprétera le mandat. Leur réussite n'était pas une preuve
  d'exécutabilité sémantique du protocole.
- Aucun élément ne permet d'évaluer le bénéfice social du binôme ou son seuil
  de rentabilité sur ce run.

## Coûts et confidentialité

Temps mural observé : 12,810581794 s ; temps du processus candidat : 12,807211196 s.
Tokens observés : **11 968 = 11 810 entrée + 158 sortie**.
Le cache (0) et le raisonnement (89) ne sont pas ajoutés une seconde fois.
Une seule session candidate, terminée côté CLI ; zéro phase validée par le relais.
Le relais marque usage_complete=false à toute exception : champ préservé,
bien que le compteur de l'unique processus soit présent.
Coût de maintenance/publication/orchestration et solde d'abonnement : non enregistrés.
Aucune erreur quota observée. Le seuil intersession 150 000 n'a pas été atteint.

La trace publiée contient tous les quatre événements JSONL observés et aucun
raisonnement privé. Les empreintes des captures originales sont conservées.
Aucun secret, chemin privé ou heure de travail n'est publié.

## Conclusion

**Essai non concluant, défaut de protocole OBS-002, pas échec de quota.**
Ne pas inclure ce coût dans les références terminées ; le conserver séparément
comme coût d'essai interrompu. Aucun verdict de supériorité V1/V2 ni de modèle.
