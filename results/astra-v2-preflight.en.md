# Astra V2 preflight — result

[Français](astra-v2-preflight.md) · **English (UK)** · [Español](astra-v2-preflight.es.md) · [Português](astra-v2-preflight.pt.md)

The minimal preflight **passed for all 4 roles**, after V1 publication at `c959216`. It is not a benchmark cell: campaign progress remains **2/6**.

| Role | Profession | Input + output | Session duration |
| --- | --- | ---: | ---: |
| MAIN | Orchestrator / writer | 12673 | 8.406 s |
| SA-01 | Requirements and security | 12512 | 8.7 s |
| SA-02 | Architecture and testability | 12514 | 7.134 s |
| SA-03 | Adversarial QA critic | 12320 | 7.383 s |

## Observed checks

Each TOML file was passed through strict Codex configuration validation. Four distinct fresh thread IDs, no supplied conversation history, exact replies and matching SHA-256 hashes. All processes exited 0 and returned usage counters. No command calls or writes in the empty temporary working directory were observed.

[JSON](../governance/astra-v2-preflight/run.json)

## Scope and limitations

The selected engine is the approved A-08 fallback: separate `codex exec --json` sessions. The available native tool contract does not expose the required per-thread context/compaction settings and usage. This is not an engine benchmark.

`gpt-6-astra/high`, declared context 200,000, compaction 180,000 (`total`), CLI 0.153.4. Consultants are configured read-only. Platform instructions and tool definitions remain present even without inherited conversation.

This check does not trigger compaction, measure server limits, attempt forbidden writes or exercise the full analyse/challenge/review cycle. These TOML files are diagnostic acknowledgement configurations, not ready-made benchmark assignments.

## Measurements and analysis

49,961 input + 58 output = **50,019 tokens**; 36,352 cached tokens are already included. Reported reasoning is 0 for these trivial replies despite high effort. Summed session duration is **31.623 s**, not wall time: sessions overlap and total wall time was not recorded.

These figures measure diagnostic cost, not social or calculator performance. Infrastructure input overhead even for brief messages reinforces the need to count every V2 call.

## Observable text

Each block associates the exact request and reply. No joint problem-solving occurred, so no inter-agent influence can be inferred.

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

## Next step

V1 is published and the minimal preflight is complete. The next experiment is V2 Core, preserving complete advice and arbitration before its report and Scientific. The V2 benchmark has not been launched.
