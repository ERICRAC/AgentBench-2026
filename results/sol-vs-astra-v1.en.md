# V1 Sol vs Astra — like-for-like control

[Français](sol-vs-astra-v1.md) · **English (UK)** · [Español](sol-vs-astra-v1.es.md) · [Português](sol-vs-astra-v1.pt.md)

## Direct answer

All four solutions reach their final official verdict: Core **6/6 groups and
14/14 checks**, Scientific **9/9 groups and 57/57 checks**. The
[acceptance catalogue](../docs/acceptance-tests.en.md) expands all 71 assertions.
Across these two observations, however, `gpt-5.6-sol/high` uses **2.40×
the time** and **1.33× the tokens** of `gpt-6-astra/high`. Scientific Sol also
needs a correction after an initial 3/9, while Astra reaches 9/9 on its first
official pass.

This favours Astra on observed efficiency, but does not establish general
superiority: there is only one repeat per cell and generation is stochastic.

## Controlled scope

Control campaign `sol-high-control-001` was preregistered in commit `a616b2d`.
Specifications, acceptance tests, prompts, CLI `0.153.4`, Python `3.13.5`,
capture harness, `high` effort, 200k client context, 180k total compaction,
fresh ephemeral sessions, sandbox, network policy and solo topology all match
`astra-high-001`. SHA-256 fingerprints confirm the immutable inputs.

The configuration diff contains one intended variable only: the model changes
from `gpt-6-astra` to `gpt-5.6-sol`. OpenAI documents `high` effort and the same
maximum context window for [gpt-5.6-sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
Server infrastructure, sampling variability and internal deployments cannot be
frozen, so “like-for-like” refers to the observable client protocol.

## Results

| Challenge | Measure | Astra/high | Sol/high | Sol difference |
| --- | --- | ---: | ---: | ---: |
| Core | First / final / independent | 6/6 · 6/6 · 6/6 | 6/6 · 6/6 · 6/6 | tie |
| Core | Duration | 100.175 s | 189.964 s | +89.6% |
| Core | Input + output | 120,478 | 158,101 | +31.2% |
| Scientific | First / final / independent | 9/9 · 9/9 · 9/9 | 3/9 · 9/9 · 9/9 | Sol corrected |
| Scientific | Duration | 399.478 s | 1,009.468 s | +152.7% |
| Scientific | Input + output | 220,510 | 296,275 | +34.4% |
| **Total** | **Groups / elementary checks** | **15/15 · 71/71** | **15/15 · 71/71** | **tie** |
| **Total** | **Duration** | **499.653 s** | **1,199.432 s** | **+140.1%** |
| **Total** | **Input + output** | **340,988** | **454,376** | **+33.3%** |

Cache is already included in input and reasoning in output; neither is counted
twice.

## Quality and interpretation

Core hits the official ceiling for both models without a functional fix; Sol
is slower and uses more tokens without a measured quality gain. On Scientific,
Sol diagnoses and fixes a Python 3.13 loader interaction after six import errors.
Astra passes 9/9 first, then finds and fixes an extreme-float interpolation flaw
through its own supplementary checks.

After both runs, the same Astra-authored four-method suite was replayed without
editing either solution: Astra passes 4/4; Sol fails all four methods with six
assertion failures. This is exploratory, not an official verdict: it was not
preregistered for Sol and one SVG assertion requires a tree layout stricter
than the contract. The other findings still suggest robustness hypotheses for
extreme floats, complexity limits and wholly invalid sampled expressions.

The defensible conclusions are: equal final official conformity; a clear Astra
advantage in observed time and token cost; self-correction by both models at
different stages; and no general statistical inference with `n = 1`. A future
campaign should preregister neutral robustness tests and use repeated runs.

[Sol Core minutes](../runs/sol-core-v1-001/PV.md) · [Sol Scientific minutes](../runs/sol-scientific-v1-001/PV.md) · [Astra report](astra-v1.en.md)
