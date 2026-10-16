# Intermediate review — what AgentBench establishes

[Français](intermediate-review.md) · [English (UK)](intermediate-review.en.md) · [Español](intermediate-review.es.md) · [Português](intermediate-review.pt.md)

## Answer to the research question

> Under what conditions does a team of agents become more efficient than one agent, with the same requested model and effort, accounting for quality, time, tokens and coordination?

**The project demonstrates observable cooperation and useful corrections in some runs. It has not demonstrated a net, reproducible team advantage.** The calculators currently serve mainly to calibrate the experiment; the crossover remains unknown.

Historical consultative V2 achieves the same official score as solo at higher cost. The pair greatly reduces that overhead. Its latest scientific trial still uses 18.8% more tokens and 10.1% more time than historical solo, with no post-review corrections. Lean simple is faster and uses fewer gross tokens than historical solo, but OBS-001 changes the work performed; it does not establish pair superiority.

This review examines existing artefacts, with two independent methodological and social-observation reviews outside the candidates. No benchmark or new model campaign was launched. Review costs are unrecorded and excluded from candidate costs.

## Verified measurements

| Challenge, Astra medium | Organisation | Time (s) | Input + output tokens |
| --- | --- | ---: | ---: |
| Simple | Solo V1 | 98.572 | 98,496 |
| Simple | Consultative V2 | 375.169 | 408,616 |
| Simple | Supervised pair | 159.977 | 113,774 |
| Simple | Lean pair, OBS-001 | 65.964 | 87,775 |
| Scientific | Solo V1 | 188.560 | 119,388 |
| Scientific | Consultative V2 | 648.008 | 570,382 |
| Scientific | Lean pair | 207.630 | 141,794 |

All pass their final suite: simple 6 groups / 14 checks, scientific 9 groups / 57 checks. These rows are not one controlled campaign. One observation per condition cannot establish variability.

[Recomputed data and hashes](intermediate-review-data.json) · [V1/V2](astra-medium-v1-v2.en.md) · [OBS-001](v2-2-lean-001.en.md) · [Scientific 002](v2-2-lean-scientific-002.en.md).

## Equal scores conceal quality differences

Two previously known probes were applied identically to the three archived scientific solutions under Python 3.13.5, read-only:

| Probe | Expected | Solo V1 | Consultative V2 | Lean pair |
| --- | ---: | --- | --- | --- |
| P1: 1 followed by 10,000 spaces | 1 | Rejects: length | 1 | 1 |
| P2: sum of 1,500 ones | 1,500 | Rejects: complexity | 1,500 | Rejects: complexity |

Historical V2 handles both cases. Its trace links SA-03 criticism to length/depth corrections: a verifiable contribution on particular cases, not an average organisational effect.

These probes were selected after runs with knowledge of defects. They are neither hidden evaluation nor a new official score, exhaustive assessment or requirement for unlimited resources. Rejection here exposes a usage limit, not by itself a general contract violation.

For a new campaign, freeze more discriminating robustness, integration and code-maintenance checks, including independent evaluation cases unseen by candidates. Keep the current suite intact. The 71 checks are neither 71 experimental repetitions nor a complete quality score.

## What interactions establish

Scientific V2 contains disagreements, arbitration and targeted corrections after QA criticism: observable information flow and influence. It does not establish that the same developer with more time or self-review could not have made those corrections.

In the latest pair, the reviewer finds no confirmed defect, runs no checks and leaves the code unchanged. It correctly distinguishes MAIN's claimed 78 checks from execution evidence it received. That is good evidence discipline without observed quality gain in this run. No correction proves neither universal uselessness nor prevention of an invisible error.

Teams can also introduce questionable restrictions: MAIN adopted a 10,000-character limit before removing it after SA-03. Counting only final corrections would conceal this trajectory. Track introduced and withdrawn restrictions too. [Decisions](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md).

Minutes support analysis of agreements, contradictions, adoption and changes. Accepted advice is a decision count, not efficiency. Consensus among instances of one model does not guarantee independent expertise; traces alone establish neither sycophancy nor human psychology.

Link each useful finding: **clause → evidence → decision → change → before/after check**. Measure confirmed defects, false alarms, regressions, duplication and unverifiable points separately. Reviewer calibration on known injected defects could measure detection and precision in a separate study.

[V2 minutes](../runs/astra-medium-scientific-v2-001/PV.md) · [Pair minutes](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).

## Main methodological issues

| Priority | Issue | Implication / improvement |
| --- | --- | --- |
| High | One trial per condition, varying order and environment | Descriptive differences; balanced repetitions before general conclusions |
| High | Solo already reaches maximum score | Separate minimal compliance, robustness, integration and maintainability |
| High | One solo session versus three fresh pair sessions | Social role, restart and extra computation change together; add a segmented-solo control |
| High | OBS-001 and new campaigns | Simple lean differences cannot be attributed only to coordination |
| Medium | Model aliases and effort differences across some series | Record exposed metadata; do not rank model families and efforts in isolation |
| Medium | V2 official tests follow review | Distinguish retrospective first draft from first official invocation |
| Medium | Excluded costs and incomplete interrupted-run metrics | State candidate, interrupted-trial and maintenance scopes explicitly |

Which complete workflow delivers the best practical trade-off, and what exactly does a consultant add at comparable sessions and budget? These are separate questions.

## Recommended optimisations

Latest scientific costs: initial MAIN 65,015 tokens, REV-01 16,696, final MAIN 60,083. Resumption accounts for about 42.4% of total, including reading and verification; it is not measured pure coordination.

Review and resumption add about 47.72 s. Subtracting them arithmetically does not simulate another workflow. Reusing the developer thread or keeping a smaller context are hypotheses for new conditions, not changes to historic runs.

For simple, gross tokens fall from 98,496 to 87,775, while uncached input + output rises from 21,696 to 39,647. The latter remains a diagnostic, not money or Plus quota. Publish cache, output, total and time separately.

The 150,000 stop is checked between sessions; it cannot bound an active session. A 24,000-character envelope does not bound tool-driven token use. On failure retain file state, and distinguish complete counters from completed protocol: the current engine sets usage_complete=false on every exception.

Group preparation and keep one current editorial entry point. Reports and handover accumulate historical instructions; the dashboard mixes Sol and Astra references. These create reading overhead and unnecessary restart risk. Improve navigation without rewriting evidence.

## Strategy for the crossover

**Refine the earlier four-role proposal: start with a lightweight parallel variant.** Two developers own isolated components, then one integrates in a fresh session. Three sessions, two professions, followed by independent verification. Record integration cost; add a dedicated reviewer later if justified. This is a proposed new subcondition, not a retrospective redefinition of V2.1.

Prepare a modular challenge and contemporary V1 control in one batch with identical interfaces and requirements. Solo may use the same decomposition. Include integration tests: completely independent pieces would favour the team without testing interaction costs; making everything dependent removes parallel potential.

Team latency follows the critical path: preparation, maximum parallel work duration, integration and validation. Record actual relative start/end, overlap, wall time, summed agent time, individual tokens and integration rework. Faster delivery with more tokens is a trade-off.

To explain the current pair, the targeted control is solo in three sessions with self-review. To explore collaborative speed, the lightweight parallel pilot is recommended next. These complementary questions should not trigger every variant simultaneously.

A pilot tests feasibility, not reproducibility. Before the campaign choose the principal constraint — time, tokens or quality — stop rules and overall budget. Repeat promising conditions in balanced order. The crossover is a region of tasks and constraints, not a universal line count.

## Open questions and milestone review

- Is the main objective latency, token economy or avoiding expensive defects?
- Will integration defects and challenge difficulty discriminate between organisations?
- Does another agent's criticism outperform self-review at comparable resources?
- Does any advantage persist across repetitions and interrupted-trial accounting?

Technical choices can follow these questions without repeated human confirmations. A new campaign still needs a defined scope and budget.

Both audit reviews were incorporated: methodological review requests session controls and separate cache measures; social review requests counting introduced restrictions and starting with two developers, one integrating. They differ on experimental order: explain the pair through segmented solo, or explore parallelism. This report prioritises lightweight parallelism as the untested direction; segmented solo remains necessary to isolate consultant effects later. Neither reviewer is a benchmark candidate.

**Requested reminder: have the agreed protocol reviewed by the most capable available model before new runs, then review results at the milestone.** This review uses the current session and two readers; it certifies no ranking of available models. Audit-reader cost metrics are not exposed.

## Verification and evidence

Costs of seven runs recomputed from metadata with source hashes; six common probe executions on three solutions; no candidate or run file changed. The diagnostic writes only to standard output and disables bytecode when launched.

```bash
python3 -B scripts/audit_intermediate.py
```

[Script](../scripts/audit_intermediate.py) · [Data](intermediate-review-data.json) · [Central conclusion](CONCLUSIONS.en.md) · [Test catalogue](../docs/acceptance-tests.en.md).
