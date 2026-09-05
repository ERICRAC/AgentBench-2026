# Trace synthétique — `codex-single-002`

## Cadre

- mode : V1, Codex seul ;
- objectif : Calculatrice Core ;
- modèle : `gpt-5.6-sol` ;
- effort de raisonnement : `high` ;
- contexte déclaré : 200 000 tokens ;
- compaction automatique : 180 000 tokens, portée `total` ;
- orchestrateur expérimental : session Codex extérieure au run candidat ;
- agent candidat : processus `codex exec` distinct, mandaté par l'orchestrateur ;
- consultants ou sous-agents lancés par le candidat : aucun ;
- intervention humaine fonctionnelle : aucune.

La session était éphémère. Les deux tentatives de lancement qui ont précédé le
vrai run ont été rejetées localement avant tout appel au modèle : absence du
binaire `/usr/bin/time`, puis combinaison d'options CLI incompatible. Elles ne
sont incluses ni dans la durée ni dans les tokens du run.

## Parcours observable

1. Le candidat a relu `CHALLENGE.md`, retrouvé le vérificateur et le format de
   restitution à la racine, sans consulter une autre solution.
2. Il a créé `calculator.py` et le README dans `solution/`.
3. Le premier passage du vérificateur officiel a réussi : **6/6**.
4. Un contrôle manuel lancé depuis le mauvais répertoire a révélé une
   formulation imprécise dans le README. Le candidat a corrigé uniquement la
   documentation, puis le second passage a de nouveau réussi : **6/6**.
5. L'orchestrateur a reproduit le verdict après le run : **6/6**.

## Mesures

| Indicateur | Valeur observée |
| --- | ---: |
| Durée murale arrondie | 193 s |
| Entrée | 549 279 tokens |
| Entrée servie depuis le cache | 480 384 tokens |
| Sortie | 7 182 tokens |
| Raisonnement inclus dans la sortie | 2 881 tokens |
| Entrée + sortie | 556 461 tokens |
| Commandes terminées | 17 |
| Lots de modifications | 2 |
| Messages du candidat | 11 |

Les compteurs d'entrée sont cumulés sur les tours et incluent le cache. Ils ne
représentent pas une fenêtre de contexte simultanée de 549 279 tokens.

## Incident de gouvernance

La règle globale « commit et push après modification » a été interprétée par
le candidat alors que la règle du run limitait ses écritures à `solution/`.
Il a créé un commit contenant exclusivement les deux livrables, puis a tenté
un push. Le push a échoué et aucun état distant n'a été modifié par le
candidat. Cet événement est conservé comme bruit de gouvernance ; il justifie
une exclusion explicite des opérations Git dans les futurs prompts de run.

Le [procès-verbal](PV.md) distingue les échanges de l'orchestrateur, du
candidat et du vérificateur sans publier le raisonnement interne brut.
