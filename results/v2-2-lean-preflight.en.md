# Lean V2.2 — launcher prepared, live use locked

[Français](v2-2-lean-preflight.md) · **English (UK)** · [Español](v2-2-lean-preflight.es.md) · [Português](v2-2-lean-preflight.pt.md)

**Authorised preparation completed; no real candidate launched.** Astra medium retained. The engine now sequences three phases using lean mandates and envelopes, rather than merely measuring their sizes.

## Preparation settings

| Setting | Value |
| --- | --- |
| Future requested model / effort | gpt-6-astra / medium |
| Maximum sessions | MAIN initial → REV-01 reviewer → MAIN final |
| JSON envelope per phase | 12,000 Unicode characters, excluding mandate |
| Experimental target | Under 100,000 candidate tokens, not a forecast |
| Between-session stop | At 150,000 observed input + output tokens |
| Strict within-session cap | None |
| Final reports | 150 / 300 / 300 words; excess recorded, never truncated |
| Retry / scientific / live launch | Not authorised |

The earlier 60,000-token proposal is superseded for this preparation by the agreed 150,000 threshold. Cache/reasoning are not double-counted. Missing or invalid usage stops the sequence and marks the total incomplete, not zero.

## Wiring and checks

Fresh private directory, unchanged contract/verifier copies, empty solution. Lean prompt construction, existing role configurations, full synthetic response capture, protected-file/read-only checks, snapshots and checkpoints. Initial commands stay archived but are not retransmitted; reviewer command evidence remains available for arbitration.

**100 maintenance tests pass**, including 18 new integration tests: capture, handovers, exclusive directories, live refusal before writes, size/token gates, absent/invalid usage, exposed failed-process costs, prohibited writes, reused threads, truncated output, word limits and locked manifest.

A full simulation completes three phases with 39 **fake** tokens and envelopes of 1,652 / 2,078 / 2,280 characters, with no calculator verdict. Two synthetic 75,000-token sessions block the third. Historical counters injected as fixtures complete at 113,774, below the stop but above the target; this is not a fresh model measurement.

## Limits and next delivery

The threshold only prevents a subsequent phase. An ongoing session may overshoot. A final phase completing over threshold remains completed with excess recorded. Word limits are audited, not enforced by the model runtime.

The CLI exposes simulation only; editing the manifest cannot unlock live use. The injectable callback is for tests. **A real transport adapter, explicit attempt authorisation and a new campaign freeze are still required before benchmarking.** File checks detect observed changes, not complete isolation. No quota savings or subscription-window guarantee. Historical evidence, general governance and the user's untracked .github/ directory remain unchanged.

[JSON — CLI simulation](v2-2-lean-preflight.json) · [Manifest](../governance/v2-2-lean-draft.json) · [Launcher](../scripts/run_v2_2_lean.py) · [Tests](../tests/test_v2_2_lean.py) · [Audit](v2-2-cost-audit.en.md) · [README](../README.en.md)
