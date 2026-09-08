# Sol V2 — Core and Scientific synthesis

[Français](sol-v2.md) · **English (UK)** · [Español](sol-v2.es.md) · [Português](sol-v2.pt.md)

## Direct answer

Sol/high V2 completes both challenges at the official ceiling: **15/15
`unittest` groups, or 71/71 elementary checks**. Core passes 6 groups and 14
checks first time. Scientific moves from 3/9 groups to 9/9 after a Python 3.13
loader correction; the independent verifier then confirms all 57 checks.

Final conformity equals Sol V1. V2 nevertheless uses **2,384.139 seconds** and
**1,475,626 input + output tokens**, versus 1,199.432 seconds and 454,376 tokens
for V1. Under the preregistered Pareto rule, **V1 dominates V2 on both
challenges**: equal measured quality with lower time and token costs.

[Explicit 71-check catalogue](../docs/acceptance-tests.en.md) · [V2 Core
report](sol-v2-core.en.md) · [Sol/Astra V1 comparison](sol-vs-astra-v1.en.md)

## Verdict table

| Cell | First pass | Independent final verdict | Wall time | Input + output |
| --- | ---: | ---: | ---: | ---: |
| Sol V1 · Core | 6/6 groups · 14/14 checks | 6/6 · 14/14 | 189.964 s | 158,101 |
| Sol V2 · Core | 6/6 groups · 14/14 checks | 6/6 · 14/14 | 796.534 s | 559,088 |
| Sol V1 · Scientific | 3/9 groups | 9/9 · 57/57 | 1,009.468 s | 296,275 |
| Sol V2 · Scientific | 3/9 groups | 9/9 · 57/57 | 1,587.605 s | 916,538 |
| **V1 total** | **9/15 groups** | **15/15 · 71/71** | **1,199.432 s** | **454,376** |
| **V2 total** | **9/15 groups** | **15/15 · 71/71** | **2,384.139 s** | **1,475,626** |

V2 is ×1.99 V1 wall time (+98.8%) and ×3.25 its tokens (+224.8%). On
Scientific alone the ratios are ×1.57 and ×3.09. Cache is included in input
and reasoning in output; neither is added twice.

## Scientific path observed

| Phase | Session time | Input | Output | Visible words |
| --- | ---: | ---: | ---: | ---: |
| SA-01 · analysis | 78.281 s | 14,402 | 2,015 | 915 / 1,200 max |
| SA-02 · analysis | 73.029 s | 14,404 | 1,860 | 1,065 / 1,200 max |
| SA-01 · cross-challenge | 41.247 s | 16,295 | 996 | 413 / 600 max |
| SA-02 · cross-challenge | 38.271 s | 16,297 | 917 | 466 / 600 max |
| MAIN · first solution | 810.863 s | 394,075 | 21,975 | 429 |
| SA-03 · critique | 226.117 s | 26,664 | 6,122 | 666 / 1,200 max |
| MAIN · final arbitration | 431.056 s | 389,108 | 11,408 | 555 |
| **Total** | **1,698.864 agent-seconds** | **871,245** | **45,293** | **4,509** |

Partly parallel phases explain why summed session time exceeds wall time. All
seven sessions have distinct thread IDs and use Sol/high, a declared 200,000
token window and compaction at 180,000.

## Social relation and corrections

SA-01 covers contract and security; SA-02 architecture and testability. Their
blind analyses and cross-challenge expose three useful decisions: non-contractual
resource caps, additional variable keys and output-path safety. MAIN groups 16
initial recommendations, retaining 15 and rejecting one.

SA-03 then raises 15 points: four defects, seven risks and four preferences.
MAIN retains 10 and rejects 5. Before the first verifier, the critique causes
six corrections: full Ctrl-C handling, faithful numeric display, iterative
deep-AST evaluation, corrected README example, terminal-control neutralisation
and the `0^-1` exception taxonomy.

The first official pass still errors in six groups before their functional
checks. One cause is identified: the token's `dataclass` decorator depends on
`sys.modules`, unlike the verifier's Python 3.13 loading method. MAIN replaces
it with a plain class and reaches 9/9. Sol V1 had the same 3/9 → 9/9 profile, so
V2 did not improve official convergence for this cell.

## What V2 does — and does not — demonstrate

- Specialist critique finds defects before the referee and leaves an auditable
  decision chain.
- Most improvements are not distinguished by the official suite and therefore
  are not a quantified quality gain.
- Core advice is largely redundant and its coordination cost is especially
  unfavourable.
- Scientific debate is richer, but does not prevent the loader defect that
  determines the first score.
- One observation per cell supports no general statistical conclusion.

The defensible result is: **V2 adds observable social traceability and early
corrections, but no gain on the 71 frozen checks; its overhead is clear.** The
observation gate must now decide whether V2.1 has a distinct, testable
hypothesis without rewriting V2.

## Auditable evidence

- Core: [verbatim minutes](../runs/sol-core-v2-001/PV.md) · [trace](../runs/sol-core-v2-001/trace.json) · [metadata](../runs/sol-core-v2-001/run.json).
- Scientific: [verbatim minutes](../runs/sol-scientific-v2-001/PV.md) · [trace](../runs/sol-scientific-v2-001/trace.json) · [metadata](../runs/sol-scientific-v2-001/run.json) · [decisions](../runs/sol-scientific-v2-001/solution/DECISIONS.md).

Protocol and runner did not change between Core and Scientific. Visible text
is published after screening; no raw internal reasoning, secret or work clock
time is exposed.
