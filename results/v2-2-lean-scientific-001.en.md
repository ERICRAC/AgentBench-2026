# Lean scientific trial — OBS-002 interruption

[Français](v2-2-lean-scientific-001.md) · [English (UK)](v2-2-lean-scientific-001.en.md) · [Español](v2-2-lean-scientific-001.es.md) · [Português](v2-2-lean-scientific-001.pt.md)

## OBS-002 correction prepared, without a new trial

Version 002 explicitly tells each phase that the orchestrator has validated human approval and authorises that phase now. Launch still requires confirmation of the exact run ID; the message is delivered only after that gate. Role restrictions and the prohibition on delegation are unchanged.

141 tests passed. The six adapter-002 tests cover the three prompts actually delivered to the fake process, their equality with captured prompts, the run ID and phase name, removal of ambiguous caveats, refusal without approval and refusal of a repeated launch. Delivery checks alone do not guarantee the model's future interpretation.

Planned trial: astra-medium-scientific-v2-2-lean-002; new campaign astra-medium-lean-003. Astra medium, 24,000 characters, 150,000-token intersession stop without a hard cap. No model call or run-002 directory created. Run 001, its costs and frozen files remain byte-identical. Real launch still requires human approval; no further preparation is planned before that approval.

[Manifest 002](../governance/v2-2-lean-scientific-002.json) · [Adapter 002](../scripts/run_v2_2_lean_scientific_live_002.py) · [Tests 002](../tests/test_lean_scientific_live_002.py).

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
