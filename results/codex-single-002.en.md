# Detailed result — `codex-single-002`

[Français](codex-single-002.md) · **English (UK)** · [Español](codex-single-002.es.md) · [Português](codex-single-002.pt.md)

## Executive summary

The second V1 **Core Calculator** baseline passed **6 tests out of 6** on its
first official run and in the independent verification. The experimental
orchestrator commissioned a separate Codex candidate session; that candidate
worked without consultants, sub-agents or functional human help, with the
model, effort and context explicitly pinned. It is the current V2 baseline;
`codex-single-001` remains available as the first historical observation.

## Identity and result

| Data | Value |
| --- | --- |
| Mode / objective | V1 · Codex alone / Core Calculator |
| Model / effort | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Context / compaction | 200,000 / 180,000 tokens, `total` scope |
| Candidate / its consultants or sub-agents | separate `codex exec` session / 0 |
| Functional human help | 0 |
| First pass / independent final verdict | **6/6 / 6/6** |

The candidate implemented an explicit four-operation engine, input parsing
and a resilient CLI. A manual check after the first 6/6 exposed only an
ambiguous launch location in the README; documentation was corrected without
a functional code change.

## Measurements

| Metric | Observed value |
| --- | ---: |
| Rounded wall-clock duration | 193 s |
| Input / cached input | 549,279 / 480,384 tokens |
| Output / reasoning within output | 7,182 / 2,881 tokens |
| Input + output | 556,461 tokens |
| Completed commands / change batches | 17 / 2 |
| Code / documentation | 84 / 44 lines |

Input tokens are cumulative across turns and include cached input; they do not
represent a simultaneous context larger than the declared limit.

The candidate also interpreted the repository-wide Git delivery rule and
created a solution-only commit before attempting a push. The remote was not
changed. Future run prompts now exclude Git operations explicitly.

Independent command: `python3 scripts/verify.py --solution
runs/codex-single-002/solution`. See the [minutes](../runs/codex-single-002/PV.md),
[trace](../runs/codex-single-002/trace.md) and
[metadata](../runs/codex-single-002/run.json).
