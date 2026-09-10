# Astra medium — V1/V2 comparison and scientific V1 run

[Français](astra-medium-v1-v2.md) · **English (UK)** · [Español](astra-medium-v1-v2.es.md) · [Português](astra-medium-v1-v2.pt.md)

## One-minute conclusion

**On both calculators, solo V1 reaches the same official score as advisory V2, using less time and fewer tokens.** Overall, V2 uses **×3.56 the time and ×4.49 the tokens**. These measures show no crossover in favour of collaboration.

Crucially, an equal score does not mean equal robustness. Scientific V2 review corrected length/depth restrictions which the new V1 retains. Coordination therefore has an observable technical contribution, but the current official tests do not value that benefit. This does not mean “consultants are useless”.

## Same requested model and effort

gpt-6-astra / medium; context 200000, compaction 180000, total scope. V1 = one developer in one session. V2 = one writer, three consultants, seven sessions per challenge; not parallel developers.

| Calculator | Final V1 = V2 score | V1 time | V2 time | V2/V1 | V1 tokens | V2 tokens | V2/V1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Simple | 6/6 groups · 14/14 checks | 98.572 s | 375.169 s | ×3.81 | 98496 | 408616 | ×4.15 |
| Scientific | 9/9 groups · 57/57 checks | 188.560 s | 648.008 s | ×3.44 | 119388 | 570382 | ×4.78 |
| Both challenges | 15/15 groups · 71/71 checks | 287.132 s | 1023.177 s | ×3.56 | 217884 | 978998 | ×4.49 |

All first official passes succeed; V2 passes follow mandatory criticism. Totals sum these two completed runs per organisation, not the entire campaign or subscription. Tokens = input + output, already including cache and reasoning. Scientific V2 adds 459.448 s and 450,994 tokens over V1.

From simple to scientific, the time ratio falls slightly (3.81 → 3.44), but the token ratio rises (4.15 → 4.78). Additional difficulty is insufficient to make this organisation pay off on official indicators. Two exercises and one observation per cell cannot establish a threshold.

## New scientific V1 — what happened

Attempt astra-medium-scientific-v1-001 was authorised after Core publication. Fresh directory, historical prompt, no previous solution read by the candidate, no consultants or V2 advice supplied. The candidate reads the contract, builds a restricted recursive parser, reuses its expression tree for sampling, exports escaped segmented SVG, then adds the CLI, history and documentation.

A manual CLI check precedes the only official invocation: powers 512, -4 and 0.25; recovery after division by zero; successful-only history. **9/9, independently confirmed 9/9, with no functional correction after the verdict.** Untouched code committed as aaa83de. Files: 295 Python lines, 83 README lines, 51 candidate minutes lines; these counts do not measure maintainability.

Duration: 188.560 s. Input: 113,746 including 98,944 cached; output: 5,642 including 164 reasoning. Total: 119,388. Five visible messages, six completed commands, no delegation. Empty-directory rg search finds no file; extra minutes beyond two listed deliverables; shell redirections instead of apply_patch: recorded facts, not penalised by the technical verifier.

## Scientific checklist — nine groups, 57 checks

- [x] S01 · Deliverables and documentation — 7 checks.
- [x] S02 · Standard library and no forbidden dynamic execution — 2.
- [x] S03 · Precedence, parentheses, powers and signs — 10.
- [x] S04 · Functions, constants and scientific notation — 6.
- [x] S05 · Variable x and forbidden names — 5.
- [x] S06 · Syntax, domains and division by zero — 6.
- [x] S07 · Sampling, endpoints and discontinuities — 8.
- [x] S08 · Valid SVG, axes, curve, escaped title and inert content — 7.
- [x] S09 · CLI, plotting, history, recovery and exit — 6.

[Every case and expected result](../docs/acceptance-tests.en.md) · [Six simple groups](astra-medium-v1-core.en.md). Exploratory and candidate checks are not added to the 71 official checks.

## What collaboration contributes despite its overhead

On the simple calculator, V2 mainly clarified documentation without functional changes. For scientific, **SA-03 = sub-agent 3, critical reviewer**: MAIN responded by removing length/recursion limits, protecting terminal output and handling failed CLI channels. Cross-reviews also corrected proposals about function composition and expressions undefined everywhere. [V2 analysis and evidence](astra-medium-v2.en.md).

After V1 completion, two exploratory orchestrator probes confirm its restrictions: `"1" + " " * 10000` should mathematically yield 1, and `"+".join(["1"] * 1500)` should yield 1500; both raise ValueError. Results are in the trace. **These are post-hoc V1-only probes, not preregistered and outside the score.** V2 evidence comes from its existing report and recorded checks; there is no identical V2 replay here. This exposes a scoring blind spot, not an exhaustive estimate of V2 superiority.

## Limits and next decision

One observation per cell; V1 collected after V2; identical alias without a guaranteed server snapshot; variable load/cache. V1 timing includes CLI startup/shutdown, V2 also includes relay work; preparation, post-run verification and publication are excluded. Configured context is not a total consumption cap, nor is enforcement demonstrated by these runs. No reliable monetary cost recorded.

The Astra medium V1/V2 baseline now covers both exercises. Proposed next step: preregister V2.2 (lean pair), then V2.1 (parallel development), with explicit budgets, repeats and robustness measures. Genuine parallelism will need a divisible challenge. No further launch or governance change here. [Central conclusion](CONCLUSIONS.en.md).

## Audit — summary to evidence

[Scientific minutes: roles, sequence and visible texts](../runs/astra-medium-scientific-v1-001/PV.md) · [Trace and probes](../runs/astra-medium-scientific-v1-001/trace.json) · [Metadata](../runs/astra-medium-scientific-v1-001/run.json) · [Code](../runs/astra-medium-scientific-v1-001/solution/scientific_calculator.py) · [Candidate README](../runs/astra-medium-scientific-v1-001/solution/README.md)

[Simple V1 evidence](astra-medium-v1-core.en.md) · [V2 and both minutes](astra-medium-v2.en.md) · [Historical preflight](astra-medium-v1-preflight.en.md) · [Index](README.en.md) · [Project](../README.en.md)

## Publication checks

Maintenance checks, separate from the benchmark: 12 unit tests without model calls; links across 152 editorial documents and 64 historical hashes; reproducibility of five V2 summaries; Markdown lint and git diff --check. Audit of this attempt’s 11 hashes and counters against the private capture. Previous solutions, challenges, scripts, prompts and governance unchanged. Four duplicate blank lines flagged by lint were removed; no candidate correction.
