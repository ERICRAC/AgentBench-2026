# V2 protocol — governed Codex multi-agent

[Français](V2_PROTOCOL.md) · **English (UK)** · [Español](V2_PROTOCOL.es.md) · [Português](V2_PROTOCOL.pt.md)

## Status and hypothesis

This protocol is frozen before the first V2 run. V2 tests whether three
specialist reviews improve the quality or convergence of one writer once
coordination cost is included. Current baselines are `codex-single-002` and
`scientific-single-002`; the `001` runs remain historical evidence.

## Controlled variables

| Parameter | Baseline and planned V2 value |
| --- | --- |
| Model / reasoning effort | `gpt-5.6-sol` / `high` |
| Declared context per agent | 200,000 tokens |
| Automatic compaction | 180,000 tokens, `total` scope |
| Sessions | fresh and ephemeral |
| Challenges and verifiers | currently frozen versions |
| Dependencies / human functional help | standard library only / none |

Before launch, the orchestrator must prove that each agent receives these
context limits. If delegation does not expose them, the run does not belong to
this campaign until a controllable execution method is used.

## Pre-registered organisation

One orchestrator is the only writer. Two read-only consultants analyse the
contract/security and design/testability before implementation. One read-only
critic reviews the first solution for edge cases. Exactly three consultants
are used, with no nested delegation and no access to another run.

The orchestrator resolves recommendations, implements, documents and runs the
official verifier. Only `solution/` may be written during the run. Candidates
and consultants must not run Git operations; experimental publication occurs
after closure in a separate commit.

## Required measurements and order

Record first-pass and independent final scores, total and per-role duration
when available, genuine per-agent token counters, calls, disagreements,
accepted and rejected advice, corrections, human interventions, incidents and
delivered size. A numbered `PV.md` records every mandate, recommendation,
response and reasoned disposition by role. Missing data remains explicitly
unrecorded.

Run and publish V2 Core first, then V2 Scientific without intermediate tuning.
Observe both before any V2.1 decision. Any parameter change opens a new
campaign and requires comparable baselines to be rerun.
