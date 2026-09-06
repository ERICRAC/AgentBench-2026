# Modèle de procès-verbal multi-agent

**Français** · [English (UK)](PV_TEMPLATE.en.md) · [Español](PV_TEMPLATE.es.md) · [Português](PV_TEMPLATE.pt.md)

Ce modèle devient obligatoire à partir de V2. Il conserve les textes visibles
échangés entre agents et les relie aux décisions, aux coûts et au résultat.

## Identification

| Champ | Valeur |
| --- | --- |
| Run et campagne | … |
| Objectif | … |
| Commanditaire | … |
| Orchestrateur expérimental hors run | … |
| Candidat principal / seul écrivain | … |
| Vérificateur | … |
| Résultat premier passage / final | … |

## Équipe et métiers

| ID | Agent et métier | Mission bornée | Entrées autorisées | Droit d'écriture | Modèle / effort | Contexte / compaction |
| --- | --- | --- | --- | --- | --- | --- |
| MAIN | Orchestrateur candidat / rédacteur | arbitrer, produire et vérifier | challenge, messages, solution | `solution/` | … | … |
| SA-01 | Analyste exigences et sécurité | obligations, ambiguïtés, menaces | challenge | aucun | … | … |
| SA-02 | Architecte logiciel et testabilité | structure, invariants, tests | challenge | aucun | … | … |
| SA-03 | Critique QA adversarial | omissions, régressions, cas limites | challenge, décision, solution | aucun | … | … |

Pour chaque agent, `run.json` conserve aussi l'identifiant du thread,
l'empreinte de sa configuration et les métriques réellement exposées.

## Messages visibles

Une fiche est créée pour chaque message envoyé ou reçu. Le texte est conservé
intégralement après retrait d'un éventuel secret ; une omission est signalée,
jamais réécrite silencieusement.

### MSG-001 — titre synthétique

| Donnée | Valeur |
| --- | --- |
| Direction | `MAIN → SA-01` |
| Phase | analyse indépendante / contradiction / critique / arbitrage |
| Durée de réponse | … |
| Entrée / cache / sortie / raisonnement | … |

**Texte envoyé, mot pour mot**

> …

**Texte retourné, mot pour mot**

> …

**Synthèse analytique**

- propositions vérifiables : …
- information nouvelle : …
- accord, contradiction ou doublon : …
- risque ou défaut détecté : …
- décision attendue du candidat principal : …

## Registre des arbitrages

| ID | Message source | Proposition | Décision | Motif du candidat principal | Preuve dans le code ou les tests | Effet observé |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | MSG-… | … | retenue / écartée / non vérifiable | … | fichier, test ou contrôle | gain, neutre ou régression |

Une recommandation sans ligne d'arbitrage constitue une donnée manquante du
PV. Une décision prise spontanément par l'écrivain reçoit aussi son propre ID.

## Analyse de la relation sociale

| Indicateur | Valeur |
| --- | ---: |
| Messages inter-agents | … |
| Accords explicites | … |
| Contradictions utiles / non résolues | … / … |
| Doublons | … |
| Recommandations uniques | … |
| Retenues / écartées / non vérifiables | … / … / … |
| Défauts détectés avant / après vérificateur | … / … |
| Volume visible de coordination | … mots et, si disponible, … tokens |

La synthèse décrit qui influence qui, où apparaît un consensus, quelles
contradictions améliorent la solution et quel échange ne produit que du bruit.

## Qualité, temps et tokens

| Mesure | V1 de référence | V2 | Écart ou ratio |
| --- | ---: | ---: | ---: |
| Qualité au premier passage | … | … | … |
| Qualité finale | … | … | … |
| Temps mural | … | … | `V2 / V1` |
| Somme des temps-agents | n/a | … | … |
| Tokens entrée + sortie | … | … | `V2 / V1` |
| Tokens de coordination mesurables | 0 | … | … |
| Corrections | … | … | … |

## Conclusion expérimentale

- gain de qualité démontré : oui / non ; preuve : …
- gain de temps démontré : oui / non ; preuve : …
- gain de tokens démontré : oui / non ; preuve : …
- coût social utile : …
- bruit social : …
- verdict : domination V2 / compromis / absence de gain / non concluant.

Le raisonnement interne non visible n'est jamais reconstitué. Toute mesure non
exposée est marquée « non enregistrée ».
