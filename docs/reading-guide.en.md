# Understand AgentBench

[Français](reading-guide.md) · **English (UK)** · [Español](reading-guide.es.md) · [Português](reading-guide.pt.md)

[Conclusions — when does collaboration pay off?](../results/CONCLUSIONS.en.md)

Reader-facing names are **simple calculator** (Core) and **scientific calculator** (Scientific). Technical identifiers and historical evidence remain unchanged.

R&D laboratory on agent collaboration: calculators are shared exercises. V1 = one candidate alone; V2 = one writer and three consultants; V3 = future local consultants. We measure quality, time and tokens: V2 is not promised to be better.

| ID | Role |
| --- | --- |
| RELAY | Experimental orchestrator |
| MAIN | Lead developer, sole writer and decision-maker |
| SA-01 | Sub-agent 1 — requirements and security |
| SA-02 | Sub-agent 2 — architecture and testability |
| SA-03 | Sub-agent 3 — critical quality reviewer, defects and edge cases |

In the minutes, expand “Texte envoyé, mot pour mot” and read “Texte retourné”. MSG-003/004: cross-replies; MSG-006: SA-03 review; MSG-007: final decision. Seven sessions represent four candidate roles. The verifier is an independent programme. `trace.json` records commands and counters; `DECISIONS.md` decisions. Visible messages are screened, without internal reasoning.

[Sol Core PV](../runs/sol-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Sol Scientific PV](../runs/sol-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium](../results/astra-medium-v2.en.md)

[Astra medium Core PV](../runs/astra-medium-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium Scientific PV](../runs/astra-medium-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré)

Future, inactive Vx: assign a frozen change to a fresh maintainer with only code and documentation; measure success, regressions, time, tokens and clarifications. Current tests do not measure maintainability (Scientific checks five documentation keywords). Assess useful explanations, not comment counts. Work from a solution in a new branch or directory to preserve evidence.

[README](../README.en.md) → [Tests](acceptance-tests.en.md) → [Results](../results/README.en.md)

## Attached documentation work — still pending

These items come from the supplied brief; agreeing V2.x names does not mark them complete.

- [ ] Two-level guide and where-to-find-what table, reusing this guide rather than duplicating it.
- [ ] Sequence diagram: parallel phases, barriers, recipients and supplied information; distinguish mechanical RELAY from candidate MAIN.
- [ ] Automatically generated two-minute run summaries outside runs, separate from historical verbatim: team, verdict, metrics and decisive interaction.
- [ ] Explicit interpretive annotations: proposal → transmission → decision → change → effect; distinguish confirmation, rejection and no observable effect, without automatically calling the latter noise.
- [ ] Future-run instrumentation: measured relative times, dependencies and parallel groups, generic N-agent/V3 structure. Never invent historical timing; check any impact before applying changes.
- [ ] Multilingual audit: separate frozen protocol from current status; check historical evidence, metrics, tests and runner behaviour without rerunning benchmarks for documentation.
