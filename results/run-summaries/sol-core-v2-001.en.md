# The run in 2 minutes — sol-core-v2-001

[Français](sol-core-v2-001.md) · **English (UK)** · [Español](sol-core-v2-001.es.md) · [Português](sol-core-v2-001.pt.md)

This layer precedes the detailed minutes in the reading journey; the original minutes remain unchanged. Missing cells do not mean zero.

Simple calculator · codex-multi · completed

## Observed facts

| | |
| --- | --- |
| Model / effort | gpt-5.6-sol / high |
| First official pass | 6/6 unittest groups; 14/14 elementary checks |
| Final candidate result | 6/6 unittest groups; 14/14 elementary checks |
| Independent verdict | 6/6 unittest groups; 14/14 elementary checks |
| Wall duration (s) | 796.534 |
| Input + output tokens | 559088 |
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
| sa01_initial | Not recorded | P1 | — | — | No | 62.931 | 15125 | Not recorded | Not recorded |
| sa02_initial | Not recorded | P1 | — | — | No | 72.214 | 15401 | Not recorded | Not recorded |
| sa01_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 48.026 | 17385 | Not recorded | Not recorded |
| sa02_cross | Not recorded | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 38.788 | 17142 | Not recorded | Not recorded |
| main_first | Not recorded | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Yes | 236.374 | 159299 | Not recorded | Not recorded |
| sa03_critic | Not recorded | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 118.418 | 23556 | Not recorded | Not recorded |
| main_final | Not recorded | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Yes | 321.478 | 311180 | Not recorded | Not recorded |

Invocation measurements have a different origin from historical wall duration; see the instrumentation guide.

</details>

## Interpretative analysis

[CONTESTÉ → RETENU] Agreement on three whitespace-separated elements and rejecting 2+3. MAIN arbitrates 23 recommendations (19 accepted, 4 rejected). [IMPACT] After SA-03: fixed import example, Ctrl-C throughout the loop, internal annotation compatible with older Python versions. [REJETÉ] MAIN keeps DECISIONS despite SA-03’s deliverable objection, following the protocol. Ten final items accepted and five rejected. See [Sol Core report](../sol-v2-core.en.md), DECISIONS and MSG-006/007. No official score gain; no proof MAIN would have failed alone. Often redundant advice, without reliable [BRUIT] quantification.

## Evidence and next steps

[PV / verbatim](../../runs/sol-core-v2-001/PV.md) · [trace.json](../../runs/sol-core-v2-001/trace.json) · [run.json](../../runs/sol-core-v2-001/run.json) · [Decisions](../../runs/sol-core-v2-001/solution/DECISIONS.md)

[Reading guide](../../docs/reading-guide.en.md) · [Tests](../../docs/acceptance-tests.en.md) · [Conclusions](../CONCLUSIONS.en.md) · [Index](index.en.md)
