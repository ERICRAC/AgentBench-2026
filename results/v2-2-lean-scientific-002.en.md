# Lean scientific V2.2 — trial 002 completed

[Français](v2-2-lean-scientific-002.md) · [English (UK)](v2-2-lean-scientific-002.en.md) · [Español](v2-2-lean-scientific-002.es.md) · [Português](v2-2-lean-scientific-002.pt.md)

**Scientific trial 002 passed: 9/9 groups, 57/57 checks, 141,794 tokens, 207.630 s.** No changes after review. The pair remains costlier than the historical scientific solo; exploratory comparison.

## Result and sequence

Three Astra medium sessions: MAIN implements and runs 78 local checks, REV-01 performs a static review with no confirmed defect, final MAIN arbitrates and passes the official verifier on its first invocation. The orchestrator independently confirms 9 groups / 57 checks on both initial and final versions, which are byte-identical. The candidate's 78 checks are not additional independent tests.

Explicit launch confirmation was delivered: OBS-002 did not recur. No quota interruption or retry. Envelopes measured 5,023, 21,226 and 22,569 characters, within 24,000. Final reports met their word limits.

## Cost and efficiency

| Condition | Input + output tokens | Duration (s) | Score |
| --- | ---: | ---: | --- |
| Historical solo V1 | 119,388 | 188.560 | 9/9 · 57/57 |
| Historical V2 | 570,382 | 648.008 | 9/9 · 57/57 |
| Lean pair 002 | 141,794 | 207.630 | 9/9 · 57/57 |

Against historical solo: **+18.8% tokens, +10.1% time**, without a higher score or corrections. Against historical V2: **−75.1% tokens, −68.0% time**. The lean pair greatly reduces team overhead, but does not beat the solo on this case.

Input: 134,416, including 77,440 cached; output: 7,378, including 397 reasoning. These subsets are not added twice. The 150,000 intersession threshold was not reached; no hard cap guaranteed. Wall time 207.630 s; summed sessions 207.620 s. Available quota and orchestration, preparation and publication costs were not recorded.

Interrupted trial 001 remains separate: 11,968 tokens, 12.811 s. Subtotal for scientific lean trials 001+002 only: **153,762 tokens, 220.441 s**. This is not the entire campaign's cost.

## What review adds — and does not establish

REV-01 confirms the structure and distinguishes MAIN's claimed 78 checks from unavailable evidence. It flags the already-documented limitation of singularities between samples. Final MAIN retains three findings and marks one unverified because tool outputs were not handed over. No confirmed defect, correction or demonstrated quality gain; an explicit additional review whose error-prevention value is not measured here.

## Limitations and next step

New campaign astra-medium-lean-003: same requested model and effort, but different prompts, handover, environment and cache from the references. One trial per condition; exact server revision and CLI version at launch were not recorded. Differences cannot be attributed solely to organisation, and simple/scientific are not a strictly matched pair.

No automatic further run. Recommendation: analyse these results before spending more. The point where collaboration becomes more efficient remains unknown; a genuinely parallelisable challenge or contemporary solo control would require separately approved protocol and budget.

## Artefacts

- [PV / messages / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-002/run.json) · [Prompts](../runs/astra-medium-scientific-v2-2-lean-002/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-002/trace.json).
- [Solution](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md) · [Code](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py) · [Checks](../runs/astra-medium-scientific-v2-2-lean-002/verifications.json).
- [V1/V2](astra-medium-v1-v2.en.md) · [OBS-002 / 001](v2-2-lean-scientific-001.en.md).
- [57 checks](../docs/acceptance-tests.en.md) · [Manifest](../governance/v2-2-lean-scientific-002.json).

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-2-lean-002/solution
```
