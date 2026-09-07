# Results

[Français](README.md) · **English (UK)** · [Español](README.es.md) · [Português](README.pt.md)

Earlier V1 runs are [archived](ARCHIVE_V1.en.md). “Current baseline” in those reports refers to their historical status, not the Astra campaign.

**Suggested path:** [understand the 15 groups and 71 checks](../docs/acceptance-tests.en.md)
→ [view current results](#published-results) → open the report, then the run
minutes and trace. Legacy `6/6` and `9/9` labels count `unittest` groups, not
every assertion.

## Published results

| Run | Mode | Objective | Result | Status | Details |
| --- | --- | --- | --- | --- | --- |
| `astra-core-v1-002` | Codex alone | Core Calculator | 6/6 groups · 14/14 checks | Astra baseline | [Full report](astra-v1.en.md) |
| `astra-scientific-v1-002` | Codex alone | Scientific Calculator | 9/9 groups · 57/57 checks | Astra baseline | [Full report](astra-v1.en.md) |
| `sol-core-v1-001` | Codex alone | Core Calculator | 6/6 groups · 14/14 checks | Model control | [Comparison](sol-vs-astra-v1.en.md) |
| `sol-scientific-v1-001` | Codex alone | Scientific Calculator | 9/9 groups · 57/57 checks | Model control | [Comparison](sol-vs-astra-v1.en.md) |

## Retained data

For every attempt retain, at minimum: identifier and mode; date, environment
and Codex version; first test pass; final result; total duration; human
interventions; observations and limitations.
