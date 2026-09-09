# Understand AgentBench

[Français](reading-guide.md) · **English (UK)** · [Español](reading-guide.es.md) · [Português](reading-guide.pt.md)

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
