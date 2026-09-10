# Astra medium V1 — simple calculator

[Français](astra-medium-v1-core.md) · **English (UK)** · [Español](astra-medium-v1-core.es.md) · [Português](astra-medium-v1-core.pt.md)

astra-medium-core-v1-001 completed: **6/6 groups, 14/14 checks**, on the first pass, independently confirmed. **98.572 s and 98,496 input + output tokens.** No scientific candidate launched.

## The run in two minutes

One developer candidate in a fresh Astra medium session, no consultants or candidate subagents. The external orchestrator launches, records and publishes, without solving the task.

The candidate reads the challenge, implements explicit arithmetic branches, separates calculate from the CLI and parses three whitespace-separated elements. It documents launch, examples, errors and floating-point precision. A relative-path search fails, then correct reading paths are used. Code and README are written, the verifier passes, candidate minutes are added, then the session ends. No functional fix after the first verdict; no additional tests recorded.

51 code lines with three docstrings (module, calculate, main), 72 README lines and 29 candidate-minutes lines. Readability is not a maintainability test. The extra PV exceeds the challenge’s two listed deliverables: preserved logging tension, not penalised by the suite. No post-session edits to the solution.

## What was checked

- [x] calculator.py and README.md present — 2 checks.
- [x] No direct eval/exec calls — 1 syntactic check, not exhaustive security proof.
- [x] Four operations: 2 + 3 = 5; -2 - 3 = -5; 1.5 * 2 = 3; 7 / 2 = 3.5 — 4 cases in one group.
- [x] % rejected with ValueError — 1 check.
- [x] Zero division raises ZeroDivisionError — 1 check.
- [x] CLI: exit 0, no traceback, outputs 5 and -8, error diagnostic — 5 checks.

Six unittest methods, fourteen checks. Candidate and orchestrator independently ran the same frozen suite successfully. Four operations are not counted as one calculation. [Detailed catalogue](../docs/acceptance-tests.en.md).

## V1 versus V2 — same model and effort, simple calculator

| Metric | V1 solo | V2 advisory |
| --- | ---: | ---: |
| First / final pass | 6/6 / 6/6 | 6/6 / 6/6 |
| Final checks | 14/14 | 14/14 |
| Time | 98.572 s | 375.169 s |
| Input + output | 98496 | 408616 |
| Sessions / candidate roles | 1 / 1 | 7 / 4 |
| Functional fixes after first pass | 0 | 0 |

**On this cell, V1 dominates V2 on official measurements: equal result, lower time and tokens.** V2 uses ×3.81 time and ×4.15 tokens: +276.597 s and +310,120 tokens. V2 review mainly clarified documentation, without functional corrections. Requested model and effort are identical; organisation changes.

This strengthens the advisory-team overhead finding on this small exercise, not a claim against every team or an evaluation of parallel developers. No inter-agent dialogue is invented for V1.

## Costs and limits

Input 96,182; cache 76,800 included; output 2,314; reasoning 104 included. Total 98,496 without double counting. Candidate duration includes CLI start/close, excludes preparation, independent verification and publication. No new cap or instrumentation.

Configured context 200k, compaction 180k, CLI 0.153.4. Successful execution with submitted config does not prove immutable server weights or effective context-limit enforcement. V1 follows V2; one observation each, varying load/cache. Timing boundaries differ slightly; V2 includes relay. Its first pass follows mandatory criticism. [Preflight caveats](astra-medium-v1-preflight.en.md).

Measured compliance is limited to these tests. Uncovered defects and maintainability are not quantified.

## Evidence and next steps

[PV / verbatim](../runs/astra-medium-core-v1-001/PV.md) · [trace.json](../runs/astra-medium-core-v1-001/trace.json) · [run.json](../runs/astra-medium-core-v1-001/run.json) · [Code](../runs/astra-medium-core-v1-001/solution/calculator.py) · [README](../runs/astra-medium-core-v1-001/solution/README.md) · [V2](astra-medium-v2.en.md) · [Conclusions](CONCLUSIONS.en.md)

Scientific remains prepared_not_started, its solution/ empty and authorisation false. Launch needs fresh approval after this report is published.
