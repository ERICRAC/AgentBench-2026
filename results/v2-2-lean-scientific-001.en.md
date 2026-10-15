# Lean scientific trial — OBS-002 interruption

[Français](v2-2-lean-scientific-001.md) · [English (UK)](v2-2-lean-scientific-001.en.md) · [Español](v2-2-lean-scientific-001.es.md) · [Português](v2-2-lean-scientific-001.pt.md)

The real trial stopped before any code: **11,968 tokens, 12.811 s, no calculator result**. This was not quota exhaustion. No retry occurred.

## What happened

Human approval was received and the launcher started one MAIN session. However, the mandate said freezing alone did not authorise a launch, without telling the candidate that approval had now been granted. MAIN requested confirmation and ended without tools. The CLI process returned 0, then the relay detected missing deliverables and exited with 1. Neither the reviewer nor final MAIN started.

This is an approval-transmission defect in the orchestrator's setup. The 135 offline tests checked technical paths; fake candidates did not interpret the linguistic approval condition. The defect is preserved as OBS-002 without retroactively changing frozen inputs.

## Measurements and verification

One CLI session started and completed, zero validated phases. Input: 11,810; output: 158; total: 11,968. Cache: 0, included in input; reasoning: 89, included in output. Wall duration: 12.810581794 s; session: 12.809085513 s. The 150,000 threshold was not reached; initial envelope: 5,023 of 24,000 characters. Quota balance and orchestrator cost: not recorded.

Independent inspection: empty solution directory, unchanged copied challenge, verifier and suite. Scientific acceptance suite not run: neither 9/9 nor 0/9 awarded. Raw state retains usage_complete=false, set by the relay on exception; the sole completed process nevertheless supplied published usage counters.

## Lesson and next action

No solo/pair efficiency comparison is possible: collaboration never started. Historical results remain intact; these 11,968 tokens belong to interrupted trials, not completed references.

Recommended fix in a new version: after approval validation, explicitly tell the candidate that the orchestrator authorises this phase now and work must begin. Remove ambiguous execution-message caveats, retain the launcher approval gate and test that confirmation is present. No fix or further trial applied here: a fresh ID and retry approval are required.

## Artefacts

- [PV / messages](../runs/astra-medium-scientific-v2-2-lean-001/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-001/run.json) · [State](../runs/astra-medium-scientific-v2-2-lean-001/state.json).
- [Prompt](../runs/astra-medium-scientific-v2-2-lean-001/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-001/trace.json).
- [Checks](../runs/astra-medium-scientific-v2-2-lean-001/verifications.json) · [Snapshots](../runs/astra-medium-scientific-v2-2-lean-001/snapshots.json).
- [Manifest](../governance/v2-2-lean-scientific-001.json) · [Preflight](v2-2-lean-scientific-preflight.en.md).
