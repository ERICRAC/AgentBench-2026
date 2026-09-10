# The run in 2 minutes — sol-scientific-v2-001

[Français](sol-scientific-v2-001.md) · **English (UK)** · [Español](sol-scientific-v2-001.es.md) · [Português](sol-scientific-v2-001.pt.md)

This layer precedes the detailed minutes in the reading journey; the original minutes remain unchanged. Missing cells do not mean zero.

Scientific calculator · codex-multi · completed

## Observed facts

| | |
| --- | --- |
| Model / effort | gpt-5.6-sol / high |
| First official pass | 3/9 unittest groups; 6 import errors from one dataclass loader incompatibility |
| Final candidate result | 9/9 unittest groups; 57/57 elementary checks |
| Independent verdict | 9/9 unittest groups; 57/57 elementary checks |
| Wall duration (s) | 1587.605 |
| Input + output tokens | 916538 |
| Recorded sessions (not API calls) | 7 |
| Functional corrections after first pass | 1 |

Cache is included in input; reasoning is included in output. Do not add them again. A CLI session may contain several model calls. The first official pass follows the critique, not the other way round.

## Team and sequence

MAIN: arbiter and sole writer; SA-01: requirements/security; SA-02: architecture/testability; SA-03: critical reviewer. RELAY is the external mechanical supervisor, not a candidate.

P1: independent analyses, then a barrier. P2: cross-reviews, then a barrier. Next MAIN → SA-03 → MAIN and verifier. Historical parallelism is specified, not measured overlap.

<details>
<summary>Recorded sessions (not API calls)</summary>

| Session | Role | Specified parallel group | Depends on | receives_from | Writer | CLI duration (s) | Input + output tokens | Measured start / end (s) | Measured invocation duration (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | Not recorded | P1 | — | — | No | 78.281 | 16417 | Not recorded | Not recorded |
| sa02_initial | Not recorded | P1 | — | — | No | 73.029 | 16264 | Not recorded | Not recorded |
| sa01_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 41.247 | 17291 | Not recorded | Not recorded |
| sa02_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 38.271 | 17214 | Not recorded | Not recorded |
| main_first | Not recorded | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Yes | 810.863 | 416050 | Not recorded | Not recorded |
| sa03_critic | Not recorded | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 226.117 | 32786 | Not recorded | Not recorded |
| main_final | Not recorded | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Yes | 431.056 | 400516 | Not recorded | Not recorded |

Invocation measurements have a different origin from historical wall duration; see the instrumentation guide.

</details>

## Interpretative analysis

[CONTESTÉ] Cross-reviews: non-contractual caps, extra variable keys and path safety. MAIN accepts 15 of 16 initial recommendations. [IMPACT] SA-03 → MSG-006 transmission → MAIN arbitration (10 accepted, 5 rejected) → six pre-verification corrections: Ctrl-C, numerical display, deep ASTs, README example, terminal, 0^-1. See [Sol report](../sol-v2.en.md) and DECISIONS. First score remains 3/9: the Python 3.13 loader fails with dataclass. MAIN replaces the container and reaches 9/9. This last correction comes from the verifier, not a consultant. V1 Sol had the same profile: observable contributions do not improve official convergence. Absolute novelty and [BRUIT] volume are not established.

## Evidence and next steps

[PV / verbatim](../../runs/sol-scientific-v2-001/PV.md) · [trace.json](../../runs/sol-scientific-v2-001/trace.json) · [run.json](../../runs/sol-scientific-v2-001/run.json) · [Decisions](../../runs/sol-scientific-v2-001/solution/DECISIONS.md)

[Reading guide](../../docs/reading-guide.en.md) · [Tests](../../docs/acceptance-tests.en.md) · [Conclusions](../CONCLUSIONS.en.md) · [Index](index.en.md)
