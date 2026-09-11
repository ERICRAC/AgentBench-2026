# V2.2 protocol — Astra medium lean pair

[Français](V2_2_PROTOCOL.md) · **English (UK)** · [Español](V2_2_PROTOCOL.es.md) · [Português](V2_2_PROTOCOL.pt.md)

**V2.2: pilot choices approved; 46 maintenance tests and local isolation 30/30.** Six synthetic processes, no model calls. Native profile 26/30: model integration unqualified, launch locked. Sol/Astra and effort comparison retained. [Transport / isolation](../results/v2-2-transport.en.md)

## One-minute overview

**Prepared for approval, not frozen; no launch authorised.** V2.2 tests whether one review retains V2’s useful contribution with less coordination. It is not parallel development: one developer remains sole writer. Optional variant outside the six main cells; neither historical V2 nor V2.1 is replaced.

The [Astra medium comparison](../results/astra-medium-v1-v2.en.md) motivates the hypothesis: equal V1/V2 official scores, V2 using ×3.56 time and ×4.49 tokens, with some robustness fixes outside scoring. Hypothesis, not a guaranteed outcome: **V2.2 costs less than V2 without losing quality, and review produces verifiable fixes.**

## Proposed organisation

| Organisation | Candidate roles | Sessions per challenge | Relationship |
| --- | ---: | ---: | --- |
| V1 | 1 | 1 | Solo developer |
| Historical V2 | 4 | 7 | Two analyses, two cross-reviews, implementation, criticism, corrections |
| V2.2 | 2 | 3 | Developer → reviewer → developer |

MAIN is developer/arbitrator and sole solution/ writer. REV-01 is the sole critical reviewer, read-only, covering contract, security, behaviour and documentation, with no delegation. RELAY is the external experimental orchestrator: prepare, capture, forward without advice or summaries, verify and publish. The independent verifier is the frozen test suite, not an LLM.

Initial and final MAIN are **two fresh sessions of the same role**, not a resumed conversation: three threads, two roles. REV-01 resembles V2’s SA-03 function but has a distinct identity. No upstream consultants, cross-review or second opinion.

## Sequence and exact inputs

| Phase | Permitted inputs | Output / barrier |
| --- | --- | --- |
| P1 · Initial MAIN | Active challenge + initial mandate; empty solution | Complete code/README; handover ≤600 words; own check commands/outputs |
| P2 · REV-01 | Challenge + full P1 snapshot + P1 handover + P1 check commands/outputs | One review ≤1200 words; REV-001… findings with evidence/severity |
| P3 · Final MAIN | Challenge + P1 solution + P1 handover/checks + complete P2 review/checks | Every finding disposition, corrections, official verifier; final response ≤1200 words |

Each phase waits for the previous one to close. RELAY copies every snapshot file with relative paths and hashes, without selection or reading another attempt. Visible texts are forwarded verbatim, never private thoughts. Tool outputs must be complete; truncation, omissions and filtering are declared. Missing input blocks the next phase, not an improvised summary. Candidate artefacts never become role instructions.

P1 and REV may perform their own non-destructive checks; **the first official pass occurs in P3 after review**, as in V2. Final MAIN may correct official failures within its session but cannot recall REV. A review with no findings is valid. Word overruns are recorded as deviations, never silently truncated or sent back for rephrasing. Proposed count: whitespace-separated elements in the final response, including code/tables; intermediate messages remain captured and counted separately.

Canonical French draft mandates: [Initial MAIN](../prompts/v2-2-developer-initial.md), [REV-01](../prompts/v2-2-reviewer.md), [Final MAIN](../prompts/v2-2-developer-final.md). Same mandates for both challenges, with the active CHALLENGE separately supplied. Candidates receive no human comparison, historical conclusions or historical defect list.

## Parameters and boundaries

Request **gpt-6-astra / medium for all three sessions**, context 200000, compaction 180000, total scope; ephemeral sessions. Use recorded reference parameters, not the chat’s selected model. Actual model access, strict configuration acceptance and quota remain preflight checks, not guarantees from this document.

Unchanged challenges and suites: [simple](../challenges/calculator/SPEC.md), 6 groups / 14 checks; [scientific](../challenges/scientific-calculator/SPEC.md), 9 groups / 57 checks. [Complete checklist](../docs/acceptance-tests.en.md). No test changes or additions to current scoring.

MAIN writes only challenge deliverables in solution/. REV is read-only, with no files or caches from checks. No candidate Git, network, delegation or extra dependencies. RELAY manages minutes, snapshots and measurements outside candidate deliverables, privately during the run, publishing after closure with separate code/maintenance commits. A working directory alone does not prove filesystem isolation; effective permissions must be tested.

## Budgets, interruptions and order

Proposed pilot: **one attempt per calculator, at most three sessions each**, one review, no automatic retry. Simple first, verified and published, then separate scientific authorisation; no refinement between them.

Comparability proposal: no new overall token or time cap, because references had none. **This does not guarantee fitting a subscription quota.** Context and word limits are not cumulative budgets. Sum all three sessions’ costs including failures; separate RELAY/publication costs.

On quota exhaustion, incomplete capture, forbidden writes, infrastructure failure or excess sessions: stop and retain status, phase, artefacts and available counters. No automatic quota-renewal wait, hidden resume or model substitution. A restart from scratch needs a new ID and must not read the old solution. Any desired numerical safety cap must be agreed and implemented before freeze, with comparable treatment across organisations.

## Quality and review contribution

Preserve P1 before any correction. **After the run**, RELAY executes the frozen suite on a copy of P1 and the final delivery. Label the P1 verdict “retrospective snapshot diagnostic”, never “first candidate pass”; do not supply it during the run. This observes before/after without adding verifier feedback to initial MAIN.

For each finding retain ID, clause, severity, evidence/reproduction, executed/not executed, accepted/rejected/unverifiable disposition, change and final check. Separate REV-driven, spontaneous MAIN and verifier-driven fixes. Replaying applicable findings on both snapshots after the run can confirm fixes or regressions; these checks are **exploratory**, outside the 71 official checks.

A shared robustness suite still needs design, calibration and freezing in a new campaign before candidates run. Do not recast V1’s two post-hoc probes as preregistered tests. A proposed assertion is not evidence until executed.

## Social minutes and measures

Apply the [minutes template](PV_TEMPLATE.en.md), listing only MAIN and REV-01 as candidate roles. Preserve screened full visible mandates/replies, MSG-001…, threads and hashes; no secrets, public clock times or private reasoning. Analyse who raised what, who accepted/rejected it and which evidence connects advice, change and effect. Do not infer emotions or private thoughts.

Publish explicit agreements, contradictions, duplicates, unique findings, dispositions, confirmed fixes, regressions and unverifiable points. No second exchange does not mean consensus; acceptance does not prove necessity. Judge novelty only against observable P1 state and texts.

Measure wall time from before preparing the first call until final closure/capture; session durations and sum; input/cache/output/reasoning tokens; transmitted words and artefact volume. Cache is included in input, reasoning in output. Separate post-run verification/publication time. Missing counters and unavailable exact coordination tokens remain unrecorded, not word-based token estimates. Freeze instrumentation and boundaries at preflight; do not reuse the seven-phase V2 graph unchanged.

Compare V2.2/V1 and V2.2/V2 **within each calculator**, then aggregate completed pairs. An official-indicator win requires no lower score, no higher time/tokens and at least one strict improvement. Additional robustness at greater cost is a trade-off. Equal scores are not equal exhaustive quality; a single before/after cannot establish causality.

## Campaign and strength of evidence

New topology/prompts are a substantial treatment change: plan a **new campaign**, proposed ID astra-medium-lean-001, leaving astra-medium-001 untouched. Relating the V2.2 pilot to existing V1/V2 references is only an **explicitly qualified exploratory historical comparison** (order, cache/load, prompts, session counts, instrumentation).

Homogeneous confirmation must rerun V1, V2 and V2.2 in the new campaign on both challenges under common rules. Proposal, not a consumption commitment: three repetitions per cell, counterbalanced order, **18 runs**; publish dispersion and medians, not just the best run. No significance claim or universal threshold from this small sample. Preparation authorises neither these repetitions nor the pilot.

## Preflight required before freeze and launch

- [x] Hypothesis, roles, three phases, mandates, criteria and interruptions documented.
- [x] FR, UK, ES, PT linked; previous protocols/runs preserved.
- [x] Approved: pilot without a new aggregate cap; repetitions not authorised.
- [x] Three-phase relay tested with fake candidates: handovers, write audits, limits, stops, capture, snapshots and live lock. Not OS isolation validation.
- [x] Two draft configurations and 15-hash inventory; simulations in fresh temporary directories. Benchmark directories and frozen hashes remain pending.
- [ ] Verify actual isolation/model access; a real trivial test costs tokens and requires separate approval.
- [ ] Freeze protocol, mandates and runner; publish static preflight, then explicitly authorise simple calculator.

**Current stage: local transport and Bubblewrap isolation tested; model integration unqualified, no freeze or benchmark.** No candidate launched.

Previous simulation-stage validation: 38 maintenance tests (12 existing + 26 V2.2), two three-phase simulations, zero model calls. The [technical report](../results/v2-2-preflight.en.md) separates tested properties from missing guarantees.

[README](../README.en.md) · [Conclusions](../results/CONCLUSIONS.en.md) · [Frozen V2](V2_PROTOCOL.en.md) · [Experimental design](EXPERIMENTAL_DESIGN.en.md) · [Instrumentation](../docs/observability.en.md)
