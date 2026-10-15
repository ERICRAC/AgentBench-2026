# Scientific preflight — lean pair

[Français](v2-2-lean-scientific-preflight.md) · [English (UK)](v2-2-lean-scientific-preflight.en.md) · [Español](v2-2-lean-scientific-preflight.es.md) · [Português](v2-2-lean-scientific-preflight.pt.md)

Preparation only: no candidate launched and no model call. Simple results remain unchanged.

## Finding and proposal

The full contract takes an initial envelope of 5,023 characters. These profiles contain synthetic text only, never an earlier solution: a 1,000-character README, a 150-word MAIN handover, a 300-word review and 1,000 characters of check output. These are neither predictions of future code size nor tokens.

| Synthetic code | Review | Final handover | 12,000 | Proposed 24,000 |
| ---: | ---: | ---: | :---: | :---: |
| 4 000 | 12 527 | 16 791 | ✗ | ✓ |
| 8 000 | 17 073 | 21 337 | ✗ | ✓ |
| 16 000 | 26 165 | 30 429 | ✗ | ✗ |

No profile fits 12,000; these dummy handovers exceed it even without code. At 24,000 the fixture boundary is 10,342 code characters. JSON escaping counts; mandates and client context are excluded. Longer review output may exceed the cap. Content must never be silently truncated.

## Proposed protocol

Astra medium, one writer and one reviewer, three separate sessions, no retry. Stop between sessions at 150,000 observed input + output tokens; one session may overshoot. No sub-100,000 target promised for scientific. To be measured: 9 groups / 57 checks, not an achieved score.

New mandates address OBS-001 by explicitly permitting local checks without an unavailable manifest. Proposed new campaign astra-medium-lean-002; historical comparison remains exploratory, not causal evidence about organisation. Homogeneous comparisons require separately authorised controls.

## Next steps and limitations

Frozen engine 001 remains simple-only; this preparation delivers no live adaptation. After approval of 24,000: version the challenge, deliverables, copied suite and scientific command; test all three phases, file boundaries and stops offline, then freeze. Real launch requires explicit approval. No general governance change.

## Artefacts

- [JSON](v2-2-lean-scientific-size.json) · [Script](../scripts/preflight_lean_scientific.py) · [Tests](../tests/test_lean_scientific_preflight.py).
- [Draft](../governance/v2-2-lean-scientific-draft.json).
- [MAIN initial](../prompts/v2-2-lean-scientific-initial-draft.md) · [REV-01](../prompts/v2-2-lean-scientific-review-draft.md) · [MAIN final](../prompts/v2-2-lean-scientific-final-draft.md).
- [OBS-001](v2-2-lean-001.en.md).

```bash
python3 -B scripts/preflight_lean_scientific.py
python3 -B -m unittest discover -s tests -q
```
