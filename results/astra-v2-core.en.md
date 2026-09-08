# Astra V2 — Core Calculator

[Français](astra-v2-core.md) · **English (UK)** · [Español](astra-v2-core.es.md) · [Português](astra-v2-core.pt.md)

## Verdict and comparison

Core passes first time and independently: **6/6 groups and 14/14 checks**. With equal official quality, Astra V1 dominates Astra V2: V2 takes ×7.00 the time and ×4.75 the tokens. Against Sol V2, Astra takes 12.0% less time but 2.3% more tokens: a trade-off, without dominance.

| Run | groups · checks | Wall time | Input + output |
| --- | ---: | ---: | ---: |
| Astra V1 Core | 6/6 · 14/14 | 100.175 s | 120 478 |
| Sol V2 Core | 6/6 · 14/14 | 796.534 s | 559 088 |
| Astra V2 Core | 6/6 · 14/14 | 700.994 s | 572 168 |

[Catalogue](../docs/acceptance-tests.en.md) · [V1 Astra](astra-v1.en.md) · [V2 Sol](sol-v2-core.en.md)

## Social observations

The three professions are SA-01 (contract/security), SA-02 (architecture/testability) and SA-03 (QA critique). MAIN is the sole writer across two fresh sessions. Initial and cross-analyses converge on a simple CLI grammar; MAIN writes 17 initial decision rows. SA-03 confirms no functional defect. MAIN separates its advice into 14 dispositions: 7 retained, 3 rejected and 4 unverifiable within its session; changes concern documentation and traceability only.

Five consultant replies total 2,995 words, all below their caps; all visible messages total 3,446 words. MAIN copies the advice into DECISIONS.md (386 lines), then the runner retransmits it: this observable repetition enlarges the input and contributes to measured cost.

Seven distinct threads, same roles, prompts and runner as Sol V2, gpt-6-astra/high, client context 200k/compaction 180k. Included cache: 430,848 tokens; reasoning included in output: 1,261. Summed session time: 775.480 s. Consultants use no tools; recorded changes concern the active solution. One observation per cell, no statistical generalisation.

Counters unavailable to the candidate are captured by the relay. MAIN's unverifiable labels concern its local input; the orchestrator's minutes retain the mandates and consultant trace. The frozen protocol's not-started status describes its original state; this report records execution.

## Evidence

[PV](../runs/astra-core-v2-001/PV.md) · [Trace JSON](../runs/astra-core-v2-001/trace.json) · [Run JSON](../runs/astra-core-v2-001/run.json) · [DECISIONS](../runs/astra-core-v2-001/solution/DECISIONS.md)
