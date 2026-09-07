# Préflight V2 Astra — résultat

**Français** · [English (UK)](astra-v2-preflight.en.md) · [Español](astra-v2-preflight.es.md) · [Português](astra-v2-preflight.pt.md)

Le préflight minimal est **réussi pour 4 rôles sur 4**, après publication de V1 au commit `c959216`. Il ne compte pas comme une cellule du benchmark : la campagne reste à **2/6**.

| Rôle | Métier | Entrée + sortie | Durée session |
| --- | --- | ---: | ---: |
| MAIN | Orchestrateur / écrivain | 12673 | 8.406 s |
| SA-01 | Exigences et sécurité | 12512 | 8.7 s |
| SA-02 | Architecture et testabilité | 12514 | 7.134 s |
| SA-03 | Critique QA adversarial | 12320 | 7.383 s |

## Vérifications effectives

Chaque fichier TOML a été transmis à Codex avec validation stricte. Les quatre sessions possèdent des identifiants distincts, aucun historique de conversation fourni et une réponse exacte. Les empreintes SHA-256 correspondent aux fichiers appliqués. Tous les processus ont terminé avec code 0 et fourni leurs compteurs. Aucun appel de commande ni écriture dans le répertoire temporaire n'a été observé.

[JSON](../governance/astra-v2-preflight/run.json)

## Portée et limites

Le moteur retenu est le repli A-08 : sessions `codex exec --json` séparées. Le contrat de l'outil natif disponible n'expose pas les réglages individuels contexte/compaction et compteurs requis. Aucun benchmark comparatif des moteurs n'est revendiqué.

Modèle `gpt-6-astra`, effort `high`, contexte déclaré 200 000, compaction 180 000 (`total`), CLI 0.153.4. Les consultants sont configurés en lecture seule. Les instructions système et définitions d'outils de la plateforme restent présentes même sans historique hérité.

Le préflight ne force pas de compaction, ne mesure pas une limite serveur, ne tente pas d'écriture interdite et ne teste pas encore le cycle complet d'analyse/contradiction/critique. Les fichiers TOML de ce dossier sont propres au diagnostic et contiennent une consigne d'acquittement ; ils ne doivent pas être utilisés tels quels comme missions du benchmark.

## Mesures et analyse

49 961 tokens d'entrée + 58 de sortie = **50 019 tokens** ; 36 352 tokens en cache sont déjà inclus dans l'entrée. Raisonnement retourné : 0 token sur ces réponses triviales, malgré le réglage high. Somme des temps-sessions : **31,623 s**, différente du temps mural car les sessions se chevauchent ; le temps mural global n'a pas été enregistré.

Ces mesures décrivent le coût du diagnostic, pas une amélioration sociale ou une performance calculatrice. La présence d'un contexte d'infrastructure même pour un message bref justifie de mesurer tous les appels en V2.

## Textes observables

Chaque bloc associe le mandat exact au retour exact. Les métiers ne collaborent pas sur un problème dans ce préflight ; aucune influence inter-agent ne peut être déduite.

### 1 · MAIN

[Config](../governance/astra-v2-preflight/MAIN.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est MAIN — Orchestrateur candidat et écrivain unique.
Réponds exactement : MAIN | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
MAIN | READY | ASTRA-PREFLIGHT
```

### 2 · SA-01

[Config](../governance/astra-v2-preflight/SA-01.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-01 — Analyste exigences et sécurité.
Réponds exactement : SA-01 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-01 | READY | ASTRA-PREFLIGHT
```

### 3 · SA-02

[Config](../governance/astra-v2-preflight/SA-02.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-02 — Architecte logiciel et testabilité.
Réponds exactement : SA-02 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-02 | READY | ASTRA-PREFLIGHT
```

### 4 · SA-03

[Config](../governance/astra-v2-preflight/SA-03.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-03 — Critique QA adversarial.
Réponds exactement : SA-03 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-03 | READY | ASTRA-PREFLIGHT
```

## Suite

V1 publiée et préflight minimal terminé. La prochaine exécution expérimentale est V2 Core, avec transmission intégrale des avis et arbitrages, puis rapport avant Scientific. Le benchmark V2 n'a pas été lancé.
