# Astra medium V2 — Core and Scientific results

[Français](astra-medium-v2.md) · **English (UK)** · [Español](astra-medium-v2.es.md) · [Português](astra-medium-v2.pt.md)

Both runs completed and were independently confirmed: **15/15 groups, 71/71 checks**, on the first official pass. Total: **1 023.177 s and 978 998 input + output tokens**. No interruption in this series. Measurements exclude maintenance, publication and older attempts.

## Verdicts

| Run | First pass | Final verdict | Wall time | Tokens |
| --- | ---: | ---: | ---: | ---: |
| Core | 6/6 | 6/6 · 14/14 | 375.169 s | 408 616 |
| Scientific | 9/9 | 9/9 · 57/57 | 648.008 s | 570 382 |
| **Total** | **15/15** | **15/15 · 71/71** | **1 023.177 s** | **978 998** |

[Tests](../docs/acceptance-tests.en.md) · [Guide](../docs/reading-guide.en.md)

## Social observations

Core: SA-01 drops its finite-only preference after cross-replies. MAIN records 21 initial decisions and 11 review dispositions. SA-03 prompts documentation clarifications only; no functional fix.

Scientific: cross-replies correct two initial proposals (function composition and an everywhere-undefined constant expression). MAIN records 22 decisions. Following SA-03, 13 points receive 10 retained, 2 rejected and 1 unverifiable dispositions within its dossier. Three correction groups follow: remove length/recursion limits, escape terminal output and handle failed CLI channels. Four reproducible candidate tests pass; they are not added to the 71 official checks.

The initial 131 assertions remain candidate checks. Their script is observable in the recorded initial MAIN command, but was not supplied to SA-03 or final MAIN: their “unverifiable” reservation concerns their dossier, not missing relay capture. No correction follows the first official verdict.

## Metrics and limits

| Metric | Core | Scientific | Total |
| --- | ---: | ---: | ---: |
| Input | 395 814 | 548 369 | 944 183 |
| Cache (included) | 302 080 | 409 216 | 711 296 |
| Output | 12 802 | 22 013 | 34 815 |
| Reasoning (included) | 122 | 955 | 1 077 |
| Session time sum | 451.039 s | 730.595 s | 1 181.634 s |

Five consultant replies total 3 480 Core and 3 625 Scientific words, all within limits; all visible messages total 3 818 and 4 061 words respectively. Seven fresh threads per run; tool-free consultants, one writer, no functional human help. Astra/medium, 200k context, 180k compaction, CLI 0.153.4; unchanged runner, prompts and verifiers. Core was published in 5c143cd before Scientific started.

Session-time sums exceed wall time because some consultations run in parallel. Cache is included in input; reasoning in output: do not add them twice. Per-session counters and texts are in the minutes and JSON.

## Valid comparison

Against Sol/high V2, this series uses 57.1% less time and 33.7% fewer tokens with the same final verdict. First-pass total is 15/15 versus Sol's 9/15, whose Scientific encountered a documented Python 3.13 loader issue. Both model **and** effort change: no causal proof of Astra or medium superiority.

Core medium uses 46.5% less time and 28.6% fewer tokens than Core high at equal official outcome. Fully completed Core high is restored. Scientific high reached 9/9 before its final interruption, but costs are incomplete: no high/medium total-cost comparison is calculated.

No Astra/medium V1 exists: no constant-effort V1/V2 dominance is established here. One observation per cell does not support statistical generalisation. Sol remains the complete dashboard campaign (4/6); the medium V2 series is complete at 2/2.

[Sol V2](sol-v2.en.md) · [Core high](astra-v2-core.en.md) · [Scientific high](astra-v2-retired.en.md)

## Code handover and next steps

Current modules contain 4 Core and 10 Scientific docstrings, with 0 and 1 lexical comments respectively; “no comments” therefore misses part of their documentation. This does not measure maintainability. Scientific has 348 code lines and a 127-line README; decisions and checks are linked below. Handover Vx remains a proposal to freeze, not a retroactive score.

## Evidence

- Core : [PV](../runs/astra-medium-core-v2-001/PV.md) · [trace](../runs/astra-medium-core-v2-001/trace.json) · [metadata](../runs/astra-medium-core-v2-001/run.json) · [DECISIONS](../runs/astra-medium-core-v2-001/solution/DECISIONS.md).
- Scientific : [PV](../runs/astra-medium-scientific-v2-001/PV.md) · [trace](../runs/astra-medium-scientific-v2-001/trace.json) · [metadata](../runs/astra-medium-scientific-v2-001/run.json) · [README](../runs/astra-medium-scientific-v2-001/solution/README.md) · [DECISIONS](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md) · [CONTROLES](../runs/astra-medium-scientific-v2-001/solution/CONTROLES.md) · [controle_final.py](../runs/astra-medium-scientific-v2-001/solution/controle_final.py).
