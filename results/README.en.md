# Results

[Français](README.md) · **English (UK)** · [Español](README.es.md) · [Português](README.pt.md)

**V2.2: simulation runner and static preflight passed, no model calls.** 26 new tests, 38 maintenance tests in total; live mode locked, choices and isolation pending before freeze. [Preflight and checklist](v2-2-preflight.en.md)

[Five V2 runs, two minutes each](run-summaries/index.en.md) · [📖 How to read and interpret an AgentBench run](../docs/reading-guide.en.md)

[Conclusions — when does collaboration pay off?](CONCLUSIONS.en.md)

Earlier V1 runs are [archived](ARCHIVE_V1.en.md). “Current baseline” in those reports refers to their historical status, not the Astra campaign.

**Suggested path:** [understand the 15 groups and 71 checks](../docs/acceptance-tests.en.md)
→ [view current results](#published-results) → open the report, then the run
minutes and trace. Legacy `6/6` and `9/9` labels count `unittest` groups, not
every assertion.

[V2 Astra medium](astra-medium-v2.en.md) · [Astra/high](astra-v2-retired.en.md) · [Guide](../docs/reading-guide.en.md)

## Astra medium V1 baseline — both calculators complete

**Astra medium V1 versus V2: equal official scores on both challenges.** V2 uses ×3.56 time and ×4.49 tokens overall. Review nevertheless contributes robustness fixes outside the score. [Full comparison and evidence](astra-medium-v1-v2.en.md)

## Published results

| Run | Mode | Objective | Result | Status | Details |
| --- | --- | --- | --- | --- | --- |
| `astra-medium-core-v1-001` | V1 solo Astra medium | Simple | 6/6 groups · 14/14 checks | completed | [Report](astra-medium-v1-core.en.md) |
| `astra-medium-scientific-v1-001` | V1 solo Astra medium | Scientific | 9/9 groups · 57/57 checks | completed | [Full comparison and evidence](astra-medium-v1-v2.en.md) |
| `astra-core-v1-002` | Codex alone | Core Calculator | 6/6 groups · 14/14 checks | Astra baseline | [Full report](astra-v1.en.md) |
| `astra-scientific-v1-002` | Codex alone | Scientific Calculator | 9/9 groups · 57/57 checks | Astra baseline | [Full report](astra-v1.en.md) |
| `sol-core-v1-001` | Codex alone | Core Calculator | 6/6 groups · 14/14 checks | Model control | [Comparison](sol-vs-astra-v1.en.md) |
| `sol-scientific-v1-001` | Codex alone | Scientific Calculator | 9/9 groups · 57/57 checks | Model control | [Comparison](sol-vs-astra-v1.en.md) |
| `sol-core-v2-001` | Codex team | Core Calculator | 6/6 groups · 14/14 checks | Sol V2 published | [Report, minutes and trace](sol-v2-core.en.md) |
| `sol-scientific-v2-001` | Codex team | Scientific Calculator | 9/9 groups · 57/57 checks | Sol V2 published | [Synthesis, minutes and trace](sol-v2.en.md) |
| `astra-core-v2-001` | Astra team | Calculator Core | 6/6 groups · 14/14 checks | V2 Astra | [Report](astra-v2-core.en.md) |
| `astra-medium-core-v2-001` | Astra medium team | Calculator Core | 6/6 groups · 14/14 checks | V2 Astra medium | [Report](astra-medium-v2.en.md) |
| `astra-medium-scientific-v2-001` | Astra medium team | Calculator Scientific | 9/9 groups · 57/57 checks | V2 Astra medium | [Report](astra-medium-v2.en.md) |

## Retained data

For every attempt retain, at minimum: identifier and mode; date, environment
and Codex version; first test pass; final result; total duration; human
interventions; observations and limitations.
