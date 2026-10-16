# Conclusions — when does collaboration pay off?

[Français](CONCLUSIONS.md) · **English (UK)** · [Español](CONCLUSIONS.es.md) · [Português](CONCLUSIONS.pt.md)

## Decision — what we do now

**Close the current V2.2 exploration.** Both difficulty levels have been completed with documented limitations. No identical retry or further launcher optimisation is recommended now. This neither makes the campaigns homogeneous nor resolves the research question.

### One-minute summary

| Organisation | Finding | Proposed decision |
| --- | --- | --- |
| Historical consultative V2 | Same score, higher cost than solo in available comparisons | Keep as reference; no repeat without a new hypothesis |
| Lean V2.2 pair | Scientific: +18.8% tokens, +10.1% time; no post-review corrections | Explicit review, but no demonstrated efficiency gain |
| Parallel V2.1 | Not yet measured | Next hypothesis to test, not an established gain |

### Where time and tokens go

In scientific 002, initial MAIN takes 159.910 s; review and final MAIN add 47.711 s, plus about 0.010 s of relay overhead. Historical solo takes 188.560 s: the final gap is 19.070 s. Merely matching that control would require removing **9.2% of the pair's total time and 15.8% of its tokens** (22,406 tokens), at equal quality. These are arithmetic thresholds against a historical reference, not demonstrated achievable savings.

Review alone accounts for 16,696 tokens. Subtracting it arithmetically still leaves 125,098, above solo's 119,388. This is not a reviewer-free trial: removal would also change final MAIN's context and behaviour. It only shows that the consultant does not account for all overhead; developer resumption and rereading matter too.

[PV / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md) · [V1/V2](astra-medium-v1-v2.en.md).

### The next useful experiment

**Proposal: V2.1 on a modular challenge, with a new V1 control, using Astra medium.** Example scope for approval: calculation engine on one side, plotting and interface on the other, with an integration contract fixed beforehand. Two parallel developers, an integrator and a reviewer; isolated contributions and bounded write permissions. Both organisations receive identical requirements, interfaces and tests. Solo may use the same decomposition.

Do not retroactively change the current single-file challenge. A modular challenge starts a new campaign; older results provide context, not a causal control. Prepare the contract, independent tests, write boundaries, integration protocol and measurements in one batch, then execute the authorised pilot. No sequence of model-backed preflights.

Pre-register criteria: quality at least equal to solo, time to final verdict and aggregate tokens across all agents; include integration and corrections, with interrupted attempts accounted for separately. Lower latency with higher tokens is an explicit trade-off. One pilot cannot locate a crossover: it determines whether balanced repetitions merit their budget.

**Approval still required: new challenge scope and budget for the V1/V2.1 pair.** No reliable Plus quota cap is inferred from previous runs. This synthesis launched no candidate or model call. Do not start the pilot without that overall approval.

**Scientific trial 002 passed: 9/9 groups, 57/57 checks, 141,794 tokens, 207.630 s.** No changes after review. The pair remains costlier than the historical scientific solo; exploratory comparison. [Lean scientific V2.2 — trial 002 completed](v2-2-lean-scientific-002.en.md).

Against historical solo: **+18.8% tokens, +10.1% time**, without a higher score or corrections. Against historical V2: **−75.1% tokens, −68.0% time**. The lean pair greatly reduces team overhead, but does not beat the solo on this case.

**Real lean V2.2 completed: 6/6 groups, 14 checks, 87,775 tokens, 65.964 s.** Target < 100,000 met. Observed reduction, but mandate ambiguity OBS-001 prevents a causal conclusion. [Rapport / Report / Informe / Relatório](v2-2-lean-001.en.md)

[Five V2 runs, two minutes each](run-summaries/index.en.md) · [📖 How to read and interpret an AgentBench run](../docs/reading-guide.en.md)

> On the tasks studied so far, coordination costs exceed the measured benefit. AgentBench now seeks the conditions where this relationship reverses: difficulty, specialisation, parallelism and the cost of errors.

This concerns available comparisons at identical model and effort, using the current advisory V2. It does not condemn all agent teams. Official tests do not fully measure the additional corrections observed.

**Astra medium V1 versus V2: equal official scores on both challenges.** V2 uses ×3.56 time and ×4.49 tokens overall. Review nevertheless contributes robustness fixes outside the score. [Full comparison and evidence](astra-medium-v1-v2.en.md)

## What the experiments show

| Comparison | V2 / V1 time | V2 / V1 tokens |
| --- | ---: | ---: |
| Sol high · simple calculator | ×4,19 | ×3,54 |
| Sol high · scientific calculator | ×1,57 | ×3,09 |
| Astra high · simple calculator | ×7,00 | ×4,75 |
| Astra medium · simple calculator | ×3.81 | ×4.15 |
| Astra medium · scientific calculator | ×3.44 | ×4.78 |

All five comparisons reach the same final official score: V1 uses less time and fewer tokens. For Sol, relative overhead decreases on the scientific calculator without becoming a gain. Two difficulties and one observation per cell cannot locate or extrapolate a crossover threshold.

[Sol V1/V2](sol-v2.en.md) · [Astra Core V1/V2](astra-v2-core.en.md)

V1/V2 describe organisations, never calculator generations. **Simple calculator** = historical Core identifier; **scientific calculator** = Scientific. Compare V1 and V2 on each identical exercise, then compare those differences across exercises. Comparing simple V1 directly with scientific V2 would mix difficulty and organisation.

For Astra medium, the time ratio decreases from 3.81 to 3.44 between simple and scientific, but the token ratio increases from 4.15 to 4.78. No threshold observed. New scientific V1 retains long-expression restrictions corrected after SA-03 (sub-agent 3, critical reviewer) in V2: a real contribution not valued by the official score; V1 probes were post-hoc and not preregistered.

## Organisations — baselines and proposed variants

| Organisation | Work allocation | Hypothesis |
| --- | --- | --- |
| Solo (V1) | One candidate does everything. | Both calculators complete. |
| Advisory (current V2) | One writer and three consultants. | Advice and review prevent errors. |
| **V2.1** — Parallel development | Two developers, one integrator and one reviewer; isolated contributions and interfaces agreed before development. | Simultaneous work offsets communication and integration. |
| **V2.2** — Lean pair | One developer and one reviewer, one bounded review. | Keep useful criticism with less coordination. |

**Agreed naming: V2** remains the historical advisory team; **V2.1** is parallel development; **V2.2** is the lean pair; **V2.x** denotes the family of future variants, not an additional run. V1 remains the solo baseline. Future comparisons use Astra medium on simple and scientific calculators. Names are agreed; detailed protocols and launches still require approval.

**Simple V2.2 completed with Astra medium: 3 sessions, 6/6 groups (14 checks), 159.977 s and 113,774 tokens.** No changes after review. Cheaper than historical V2, but costlier than the historical solo; exploratory comparison. [Rapport / Report / Informe / Relatório](v2-2-supervised-core-002.en.md).

All proposed variants use Astra medium. The same model does not imply identical context, actual expertise or total cost: record roles, supplied information and budgets. The pair also changes team size; it is not a topology-only comparison.

Variants are separate from frozen V2: no existing benchmark is rewritten. The current protocol does not authorise parallel writing. Preregister a new protocol, file or branch permissions, interfaces, integration and conflict handling before launching.

## Finding the crossover

The Astra medium solo baseline is complete. Preregister variants, then test organisations on both identical exercises. Single-file calculators provide an initial control but little genuinely divisible work. Then extend to a modular challenge or code evolution with more interactions; freeze new tests before runs.

Measure quality, total time to validation, all agents’ tokens, integration rework and exchanges separately. Repeat cells with balanced execution order; predefine budgets, stopping and quota handling. Separate imposed waiting from execution time. Repetition count and the new challenge remain open decisions.

Thresholds may differ for time, tokens and quality. Faster but more expensive is a trade-off, not a universal win. The crossover will be an observed range of conditions, not a magic line count. Finding no crossover is also useful.

## Limits and evidence

Astra medium V1 and V2 baselines are complete on both calculators. Astra medium V2 versus Sol high changes model and effort; Scientific Astra high has incomplete costs. These do not isolate organisation effects. Minutes reveal useful fixes, but 71/71 does not measure all quality or maintainability.

[Astra medium](astra-medium-v2.en.md) · [Guide](../docs/reading-guide.en.md) · [README](../README.en.md) · [Tests](../docs/acceptance-tests.en.md)
