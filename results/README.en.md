# Results

[Français](README.md) · **English (UK)** · [Español](README.es.md) · [Português](README.pt.md)

[Five V2 runs, two minutes each](run-summaries/index.en.md) · [📖 How to read and interpret an AgentBench run](../docs/reading-guide.en.md)

[Conclusions — when does collaboration pay off?](CONCLUSIONS.en.md)

Earlier V1 runs are [archived](ARCHIVE_V1.en.md). “Current baseline” in those reports refers to their historical status, not the Astra campaign.

**Suggested path:** [understand the 15 groups and 71 checks](../docs/acceptance-tests.en.md)
→ [view current results](#published-results) → open the report, then the run
minutes and trace. Legacy `6/6` and `9/9` labels count `unittest` groups, not
every assertion.

[V2 Astra medium](astra-medium-v2.en.md) · [Astra/high](astra-v2-retired.en.md) · [Guide](../docs/reading-guide.en.md)

## Preparation — no new result

**Next step prepared: [Astra medium V1 preflight](astra-medium-v1-preflight.en.md)** — two fresh directories, 44/44 static checks; no candidate launched.

## Published results

| Run | Mode | Objective | Result | Status | Details |
| --- | --- | --- | --- | --- | --- |
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
