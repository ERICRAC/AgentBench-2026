# Conclusions — when does collaboration pay off?

[Français](CONCLUSIONS.md) · **English (UK)** · [Español](CONCLUSIONS.es.md) · [Português](CONCLUSIONS.pt.md)

[Five V2 runs, two minutes each](run-summaries/index.en.md) · [📖 How to read and interpret an AgentBench run](../docs/reading-guide.en.md)

> On the tasks studied so far, coordination costs exceed the measured benefit. AgentBench now seeks the conditions where this relationship reverses: difficulty, specialisation, parallelism and the cost of errors.

This concerns available comparisons at identical model and effort, using the current advisory V2. It does not condemn all agent teams. Official tests do not fully measure the additional corrections observed.

## What the experiments show

| Comparison | V2 / V1 time | V2 / V1 tokens |
| --- | ---: | ---: |
| Sol high · simple calculator | ×4,19 | ×3,54 |
| Sol high · scientific calculator | ×1,57 | ×3,09 |
| Astra high · simple calculator | ×7,00 | ×4,75 |

All three comparisons reach the same final official score: V1 uses less time and fewer tokens. For Sol, relative overhead decreases on the scientific calculator without becoming a gain. Two difficulties and one observation per cell cannot locate or extrapolate a crossover threshold.

[Sol V1/V2](sol-v2.en.md) · [Astra Core V1/V2](astra-v2-core.en.md)

V1/V2 describe organisations, never calculator generations. **Simple calculator** = historical Core identifier; **scientific calculator** = Scientific. Compare V1 and V2 on each identical exercise, then compare those differences across exercises. Comparing simple V1 directly with scientific V2 would mix difficulty and organisation.

## Organisations to compare — proposals, not launched

| Organisation | Work allocation | Hypothesis |
| --- | --- | --- |
| Solo (V1) | One candidate does everything. | Missing Astra medium baseline. |
| Advisory (current V2) | One writer and three consultants. | Advice and review prevent errors. |
| **V2.1** — Parallel development | Two developers, one integrator and one reviewer; isolated contributions and interfaces agreed before development. | Simultaneous work offsets communication and integration. |
| **V2.2** — Lean pair | One developer and one reviewer, one bounded review. | Keep useful criticism with less coordination. |

**Agreed naming: V2** remains the historical advisory team; **V2.1** is parallel development; **V2.2** is the lean pair; **V2.x** denotes the family of future variants, not an additional run. V1 remains the solo baseline. Future comparisons use Astra medium on simple and scientific calculators. Names are agreed; detailed protocols and launches still require approval.

All proposed variants use Astra medium. The same model does not imply identical context, actual expertise or total cost: record roles, supplied information and budgets. The pair also changes team size; it is not a topology-only comparison.

Variants are separate from frozen V2: no existing benchmark is rewritten. The current protocol does not authorise parallel writing. Preregister a new protocol, file or branch permissions, interfaces, integration and conflict handling before launching.

## Finding the crossover

Start with the Astra medium solo baseline, then test organisations on both identical exercises. Single-file calculators provide an initial control but little genuinely divisible work. Then extend to a modular challenge or code evolution with more interactions; freeze new tests before runs.

Measure quality, total time to validation, all agents’ tokens, integration rework and exchanges separately. Repeat cells with balanced execution order; predefine budgets, stopping and quota handling. Separate imposed waiting from execution time. Repetition count and the new challenge remain open decisions.

Thresholds may differ for time, tokens and quality. Faster but more expensive is a trade-off, not a universal win. The crossover will be an observed range of conditions, not a magic line count. Finding no crossover is also useful.

## Limits and evidence

Astra medium V1 has not run. Astra medium V2 versus Sol high changes model and effort; Scientific Astra high has incomplete costs. These do not isolate organisation effects. Minutes reveal useful fixes, but 71/71 does not measure all quality or maintainability.

[Astra medium](astra-medium-v2.en.md) · [Guide](../docs/reading-guide.en.md) · [README](../README.en.md) · [Tests](../docs/acceptance-tests.en.md)
