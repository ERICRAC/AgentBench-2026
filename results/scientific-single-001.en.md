# Detailed result — `scientific-single-001`

[Français](scientific-single-001.md) · **English (UK)** · [Español](scientific-single-001.es.md) · [Português](scientific-single-001.pt.md)

## Executive summary

The first solo Scientific Calculator attempt finished with **9 tests out of
9**. One Codex agent delivered a safe expression parser, scientific functions,
curve sampling, standalone SVG export and a documented CLI without external
dependencies.

The first official pass validated 3/9 groups. One correction removed an
incompatibility with the test loader and a second fixed `log10` tokenisation.
The candidate converged without functional human assistance.

![sin(x) curve produced by the solution](assets/scientific-single-001-sine.svg)

The SVG is a post-run demonstration artefact and not a candidate modification.

## Run identity

| Field | Value |
| --- | --- |
| Identifier | `scientific-single-001` |
| Objective | Scientific Calculator |
| Mode | Codex alone |
| Architecture | One general-purpose agent, no sub-agent |
| Model | `gpt-5.6-sol` |
| Reasoning level | Not exposed |
| Prompt | [`prompts/scientific-single.md`](../prompts/scientific-single.md) |
| Measured duration | 5 min 31 s |
| Functional human intervention | None |
| First official pass | 3 passed, 6 errors |
| Final result | 9/9 |
| Code corrections | 2 |

## Protocol and implementation

Specification, prompt and tests were frozen in commit `71ae527` before the run.
The candidate used a clean directory, saw no other solution and wrote only the
two `solution/` deliverables.

A whitelist tokenizer and recursive parser handle scientific notation,
parentheses, unary signs, five operators and right-associative exponentiation.
Twelve functions, constants `pi` and `e`, and only variable `x` map explicitly
to `math`. Complex, non-finite or out-of-domain results become `ValueError`;
division by zero remains `ZeroDivisionError`.

`sample_curve` samples an inclusive interval and splits undefined points.
`write_svg` scales data, draws axes and continuous segments, escapes the title
and includes no script, link or external resource. The CLI evaluates, plots,
records, shows and clears history, provides help and recovers without traceback.

## Validation journey

| Pass | Observed result | Diagnosis | Candidate action |
| --- | --- | --- | --- |
| Targeted checks | Passed in trace | Sensitive cases checked | None |
| Official verifier 1 | 3/9, 6 errors | `dataclass` / dynamic-loader interaction | Replace internal dataclass |
| Intermediate pass | Exit 1, output missing | Candidate reported split `log10` | Extend identifier tokenisation |
| Final official verifier | 9/9 | No remaining contract failure | Close |
| Independent verification | 9/9 | Orchestrator reproduced result | No change |

The candidate-mentioned intermediate 8/9 is not treated as a certain measure;
the command failed but its output was not captured. The
[concise trace](../runs/scientific-single-001/trace.md) retains that nuance.

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/scientific-single-001/solution
```

All nine groups passed: deliverables, standard-library-only security,
precedence, functions and notation, variable safety, errors, curve sampling,
safe SVG and recoverable CLI behaviour.

## Measurements

| Indicator | Value |
| --- | --- |
| Actual run duration | 331 seconds |
| Reported input / cached / non-cached | 324,237 / 303,360 / 20,877 tokens |
| Output / reported reasoning | 8,459 / 941 tokens |
| Commands / change batches / agent messages | 8 / 3 / 9 |
| Delivered files | 2 |
| Code / documentation size | 352 / 64 lines |
| Python functions / classes | 16 / 2 |
| External dependencies | 0 |

Input includes a large cache share and cannot be compared directly with the
first Core Calculator estimate without harmonising accounting.

## Incidents and limitations

A pre-run launch failed before reaching the model because the Codex state store
was read-only; it is excluded from duration. The global response-format file
was not available inside the run. The verifier's dynamic loader rejected a
normally valid `dataclass`; tests remained frozen to preserve the protocol.
Parent Git writes were unavailable to the candidate and publication happened
afterwards.

Uniform sampling may miss a discontinuity between points. SVG tests assess
structure and safety, not rendering quality across engines. Reasoning level and
intermediate raw output are unavailable. The 9/9 establishes a demanding solo
baseline, not evidence that multi-agent organisation is beneficial.

## Conclusion

V1 Scientific reached the full contract in 331 seconds and two autonomous
corrections. A future multi-agent team must do more than match 9/9: for example,
pass sooner, anticipate verifier bias, reduce corrections or improve the
quality-to-complexity ratio.
