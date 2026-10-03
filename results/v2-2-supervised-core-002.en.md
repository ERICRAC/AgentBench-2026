# Supervised V2.2 — simple pair completed

[Français](v2-2-supervised-core-002.md) · **English (UK)** · [Español](v2-2-supervised-core-002.es.md) · [Português](v2-2-supervised-core-002.pt.md)

**Simple V2.2 completed with Astra medium: 3 sessions, 6/6 groups (14 checks), 159.977 s and 113,774 tokens.** No changes after review. Cheaper than historical V2, but costlier than the historical solo; exploratory comparison.

The lean pair completed without a quota interruption or retry. MAIN develops, REV-01 reviews read-only, then a fresh MAIN session decides and verifies. Interrupted attempt 001 is preserved; 002 started from scratch.

## Results and comparison

| Organisation | Time (s) | Input + output tokens | Quality |
| --- | ---: | ---: | --- |
| Historical V1 solo | 98.572 | 98 496 | 6/6 groups, 14 checks |
| Historical V2, three consultants | 375.169 | 408 616 | 6/6 groups, 14 checks |
| Supervised V2.2 002, one reviewer | 159.977 | 113 774 | 6/6 groups, 14 checks |

**The pair shows no measured quality gain on this simple calculator.** Initial and final artefacts are identical and both pass independent checks. The reviewer finds no confirmed defect. Against historical solo: **+62.3% time, +15.5% tokens**. Against historical V2: **−57.4% time, −72.2% tokens**. The lean arrangement reduces observed team cost without outperforming solo.

These differences are exploratory, not an isolated causal effect: CLI versions, served model snapshot, cache, load, prompts and instrumentation may differ. Both historical references use the Simple row below, not combined simple + scientific totals. One observation per organisation cannot establish the break-even threshold for collaboration.

[V1 / V2 Astra medium](astra-medium-v1-v2.en.md)

## Measurements and limitations

Input: 110,511 tokens; output: 3,263. The 65,280 cached tokens are already included in input and 165 reasoning tokens in output. Three sessions do not mean three model requests. Summed session duration: 159.958 s; wall time: 159.977 s. Maintenance, publication and independent checks are outside candidate cost.

**This attempt finished.** Starting and ending quota balances were not measured, so neither the proportion of a Plus window consumed nor success of the next attempt can be guaranteed. Attempt 001's 48.641 s and missing token count remain separate: the campaign's total token cost remains incomplete.

## Evidence and social analysis

First official verifier: 6/6; independent final confirmation: 6/6; retrospective initial diagnostic: 6/6, not fed back to the candidate. The 14 checks are not 14 arithmetic operations. Direct review cost: 29.177 s and 14,489 tokens; one explicit agreement, no confirmed defect and no correction. Total coordination cost is not isolated. The minutes identify professions and publish five returned messages, three full mandates and decisions, without private reasoning.

[PV — MAIN / REV-01](../runs/astra-medium-core-v2-2-supervised-002/PV.md) · [Prompts](../runs/astra-medium-core-v2-2-supervised-002/prompts.json) · [Trace](../runs/astra-medium-core-v2-2-supervised-002/trace.json) · [JSON](../runs/astra-medium-core-v2-2-supervised-002/run.json) · [Tests](../docs/acceptance-tests.en.md) · [001](v2-2-supervised-core.en.md) · [Protocol](../governance/V2_2_SUPERVISED.en.md)

## Next

The scientific calculator is still unauthorised. Proposed next step: decide whether to launch a fresh supervised Astra medium attempt, without automatic retry. No further candidate was launched here.

[README](../README.en.md) · [Conclusions](CONCLUSIONS.en.md)
