# Detailed result — `scientific-single-002`

[Français](scientific-single-002.md) · **English (UK)** · [Español](scientific-single-002.es.md) · [Português](scientific-single-002.pt.md)

## Executive summary

The second V1 **Scientific Calculator** baseline reached a final **9 tests out
of 9**. One agent delivered safe expression parsing, sampling, SVG export and
the CLI without external dependencies or functional human help.

The first official verifier stopped while loading the module because of the
known interaction between `dataclass` and its dynamic loader under Python
3.13. One targeted correction was enough. This run is the current V2 baseline;
`scientific-single-001` remains published.

## Identity and result

| Data | Value |
| --- | --- |
| Mode / objective | V1 · Codex alone / Scientific Calculator |
| Model / effort | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Context / compaction | 200,000 / 180,000 tokens, `total` scope |
| Sub-agents / functional human help | 0 / 0 |
| First pass | module-loading failure |
| Candidate final / independent verdict | **9/9 / 9/9** |

The solution uses a whitelist tokenizer and recursive-descent parser. Functions
and constants are mapped explicitly, real-domain errors are normalised and
only `x` is accepted. Sampling isolates undefined points; passive SVG output
escapes its title and splits discontinuous curves. The CLI handles help,
plotting, history, clearing and recovery after errors.

## Validation and measurements

| Metric | Observed value |
| --- | ---: |
| Rounded wall-clock duration | 541 s |
| Input / cached input | 587,315 / 541,312 tokens |
| Output / reasoning within output | 16,177 / 6,289 tokens |
| Input + output | 603,492 tokens |
| Completed commands / change batches | 16 / 2 |
| Code / documentation | 487 / 97 lines |

Input is cumulative and includes cache. The fixed verifier still has a loader
bias towards some `dataclass` constructions, and uniform sampling may miss a
discontinuity between samples. The candidate also attempted Git delivery due
to a global-rule collision; the remote was not changed.

Independent command: `python3 scripts/verify.py --challenge
scientific-calculator --solution runs/scientific-single-002/solution`. See the
[trace](../runs/scientific-single-002/trace.md) and
[metadata](../runs/scientific-single-002/run.json).
