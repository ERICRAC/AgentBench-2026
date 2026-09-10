# The run in 2 minutes — astra-medium-core-v2-001

[Français](astra-medium-core-v2-001.md) · **English (UK)** · [Español](astra-medium-core-v2-001.es.md) · [Português](astra-medium-core-v2-001.pt.md)

This layer precedes the detailed minutes in the reading journey; the original minutes remain unchanged. Missing cells do not mean zero.

Simple calculator · codex-multi · completed

## Observed facts

| | |
| --- | --- |
| Model / effort | gpt-6-astra / medium |
| First official pass | 6/6 groups; 14/14 checks |
| Final candidate result | 6/6 groups; 14/14 checks |
| Independent verdict | 6/6 groups; 14/14 checks |
| Wall duration (s) | 375.169 |
| Input + output tokens | 408616 |
| Recorded sessions (not API calls) | 7 |
| Functional corrections after first pass | Not recorded |

Cache is included in input; reasoning is included in output. Do not add them again. A CLI session may contain several model calls. The first official pass follows the critique, not the other way round.

## Team and sequence

MAIN: arbiter and sole writer; SA-01: requirements/security; SA-02: architecture/testability; SA-03: critical reviewer. RELAY is the external mechanical supervisor, not a candidate.

P1: independent analyses, then a barrier. P2: cross-reviews, then a barrier. Next MAIN → SA-03 → MAIN and verifier. Historical parallelism is specified, not measured overlap.

<details>
<summary>Recorded sessions (not API calls)</summary>

| Session | Role | Specified parallel group | Depends on | receives_from | Writer | CLI duration (s) | Input + output tokens | Measured start / end (s) | Measured invocation duration (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | SA-01 | P1 | — | — | No | 51.054 | 15919 | Not recorded | Not recorded |
| sa02_initial | SA-02 | P1 | — | — | No | 47.764 | 15812 | Not recorded | Not recorded |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.390 | 17485 | Not recorded | Not recorded |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.140 | 17483 | Not recorded | Not recorded |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Yes | 146.611 | 144301 | Not recorded | Not recorded |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 37.223 | 22386 | Not recorded | Not recorded |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Yes | 111.857 | 175230 | Not recorded | Not recorded |

Invocation measurements have a different origin from historical wall duration; see the instrumentation guide.

</details>

## Interpretative analysis

[CONTESTÉ → RETENU] SA-01 withdraws its finite-number preference during cross-review (MSG-003/004); MAIN arbitrates 21 items before coding. [CONFIRMÉ] SA-03 identifies numerical limits; MAIN checks them and clarifies the README without changing calculator.py. Eleven final decisions, no functional fix. Decisive interaction for the score: none demonstrated. Accepted advice does not prove MAIN would have failed alone; no automatic [BRUIT] label. See DECISIONS, final table and items 9–12, and PV MSG-006/007.

## Evidence and next steps

[PV / verbatim](../../runs/astra-medium-core-v2-001/PV.md) · [trace.json](../../runs/astra-medium-core-v2-001/trace.json) · [run.json](../../runs/astra-medium-core-v2-001/run.json) · [Decisions](../../runs/astra-medium-core-v2-001/solution/DECISIONS.md)

[Reading guide](../../docs/reading-guide.en.md) · [Tests](../../docs/acceptance-tests.en.md) · [Conclusions](../CONCLUSIONS.en.md) · [Index](index.en.md)
