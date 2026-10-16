# Scientific preflight — lean pair

[Français](v2-2-lean-scientific-preflight.md) · [English (UK)](v2-2-lean-scientific-preflight.en.md) · [Español](v2-2-lean-scientific-preflight.es.md) · [Português](v2-2-lean-scientific-preflight.pt.md)

**Scientific trial 002 passed: 9/9 groups, 57/57 checks, 141,794 tokens, 207.630 s.** No changes after review. The pair remains costlier than the historical scientific solo; exploratory comparison. [Lean scientific V2.2 — trial 002 completed](v2-2-lean-scientific-002.en.md).

## Exchange 051

Transport connected and scientific protocol frozen. 135 maintenance tests passed; six new tests cover the adapter, exact capture, hashes, refusal without approval and a complete fake-process chain followed by rejection of a second launch.

No model call and no real candidate directory created. Planned ID: astra-medium-scientific-v2-2-lean-001; campaign astra-medium-lean-002. Astra medium, three sessions, 24,000-character envelopes, 150,000-token between-session stop without a hard cap. Historical simple conditions remain intact.

The frozen manifest does not grant launch permission. After explicit human approval, the orchestrator will use --run with a fresh external directory and --approve-run with the exact ID. This flag is operator confirmation, not automatic proof of consent or a security boundary against arbitrary code. Persistent reservation begins at launch, including on failure; no retry. Next: one real trial, independent verification, then minutes and cost publication.

[Manifest](../governance/v2-2-lean-scientific-001.json) · [Adapter](../scripts/run_v2_2_lean_scientific_live.py) · [Tests](../tests/test_lean_scientific_live.py).

[OpenAI Docs — non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) : CLI JSONL.

```bash
python3 -B scripts/run_v2_2_lean_scientific_live.py --check
```

## Update — exchange 050

The 24,000-character cap is approved. Versioned scientific engine validated offline: three simulated phases completed, 39 fictional tokens, no calculator verdict. 129 maintenance tests passed, including 21 for this engine. Frozen simple-launcher hashes remain unchanged.

Tests cover scientific files, byte-identical contract and suite copies, the --challenge scientific-calculator command, full captures, read-only REV-01, forbidden writes, oversized envelopes, missing usage, the 150,000 stop, overshoot, distinct sessions and no retry. PYTHONDONTWRITEBYTECODE=1 is explicit in the final command for child processes.

Real transport and a named freeze remain to be prepared before launch approval. The engine explicitly refuses live mode, including its internal entry point. No savings, sufficient quota or scientific score demonstrated. Earlier preparation below retains the sizing findings; its proposed cap is now approved.

[Script](../scripts/run_v2_2_lean_scientific.py) · [Tests](../tests/test_v2_2_lean_scientific.py) · [JSON](v2-2-lean-scientific-simulation.json).

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
