# The run in 2 minutes — astra-core-v2-001

[Français](astra-core-v2-001.md) · **English (UK)** · [Español](astra-core-v2-001.es.md) · [Português](astra-core-v2-001.pt.md)

This layer precedes the detailed minutes in the reading journey; the original minutes remain unchanged. Missing cells do not mean zero.

Simple calculator · codex-multi · completed

## Observed facts

| | |
| --- | --- |
| Model / effort | gpt-6-astra / high |
| First official pass | 6/6 unittest groups; 14/14 elementary checks |
| Final candidate result | 6/6 unittest groups; 14/14 elementary checks |
| Independent verdict | 6/6 unittest groups; 14/14 elementary checks |
| Wall duration (s) | 700.994 |
| Input + output tokens | 572168 |
| Recorded sessions (not API calls) | 7 |
| Functional corrections after first pass | 0 |

Cache is included in input; reasoning is included in output. Do not add them again. A CLI session may contain several model calls. The first official pass follows the critique, not the other way round.

## Team and sequence

MAIN: arbiter and sole writer; SA-01: requirements/security; SA-02: architecture/testability; SA-03: critical reviewer. RELAY is the external mechanical supervisor, not a candidate.

P1: independent analyses, then a barrier. P2: cross-reviews, then a barrier. Next MAIN → SA-03 → MAIN and verifier. Historical parallelism is specified, not measured overlap.

<details>
<summary>Recorded sessions (not API calls)</summary>

| Session | Role | Specified parallel group | Depends on | receives_from | Writer | CLI duration (s) | Input + output tokens | Measured start / end (s) | Measured invocation duration (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | Not recorded | P1 | — | — | No | 48.093 | 15602 | Not recorded | Not recorded |
| sa02_initial | Not recorded | P1 | — | — | No | 46.555 | 15491 | Not recorded | Not recorded |
| sa01_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 27.954 | 16949 | Not recorded | Not recorded |
| sa02_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 33.817 | 16980 | Not recorded | Not recorded |
| main_first | Not recorded | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Yes | 393.690 | 213048 | Not recorded | Not recorded |
| sa03_critic | Not recorded | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 44.659 | 27115 | Not recorded | Not recorded |
| main_final | Not recorded | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Yes | 180.712 | 266983 | Not recorded | Not recorded |

Invocation measurements have a different origin from historical wall duration; see the instrumentation guide.

</details>

## Interpretative analysis

[CONFIRMÉ] Consensus and contract clarification: 17 initial decisions. After MSG-006, MAIN arbitrates 14 items (7 accepted, 3 rejected, 4 unverifiable) and changes documentation only. No confirmed functional defect or score-changing interaction. Repeating consultations in DECISIONS enlarges later prompts: observable transmission cost, not proof every repetition is useless. See the [Core high report](../astra-v2-core.en.md), then DECISIONS and MSG-007. No forced [NOUVEAU] or [BRUIT] label.

## Evidence and next steps

[PV / verbatim](../../runs/astra-core-v2-001/PV.md) · [trace.json](../../runs/astra-core-v2-001/trace.json) · [run.json](../../runs/astra-core-v2-001/run.json) · [Decisions](../../runs/astra-core-v2-001/solution/DECISIONS.md)

[Reading guide](../../docs/reading-guide.en.md) · [Tests](../../docs/acceptance-tests.en.md) · [Conclusions](../CONCLUSIONS.en.md) · [Index](index.en.md)
