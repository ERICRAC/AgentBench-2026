# V2 protocol — governed Codex multi-agent

[Français](V2_PROTOCOL.md) · **English (UK)** · [Español](V2_PROTOCOL.es.md) · [Português](V2_PROTOCOL.pt.md)

## Status and hypothesis

This protocol is frozen: the sponsor approved A-01 to A-08. The technical
preflight is the next mandatory step before the first V2 run. V2 tests whether three
specialist reviews improve the quality or convergence of one writer once
coordination cost is included. Current baselines are `astra-core-v1-001` and
`astra-scientific-v1-001`; the `001` runs remain historical evidence.

## Frozen decisions

The approved settings are: A-01 200k context/180k compaction (100k requires V1
reruns); A-02 three roles; A-03 blind analyses followed by one cross-challenge;
A-04 limits of 1,200 words per analysis, 600 per reply and 1,200 for the final
critique; A-05 the same `gpt-6-astra`/`high` for all; A-06 full visible text
after secret screening; A-07 a quality/time/token dashboard with Pareto
dominance rather than arbitrary composite weights; A-08 native subagents only
if they expose per-thread configuration and counters, otherwise separate
`codex exec --json` sessions. A trivial, non-benchmark preflight checks role,
isolation, configuration, visible text and JSON usage before any challenge is
read. The sponsor opened campaign `astra-high-001`: rerun both V1 baselines with
Astra before the V2 preflight. A-01 to A-08 remain fixed, with A-05 explicitly
migrated to Astra for every role. The previous Sol protocol is preserved at
commit `158d087`.

## Controlled variables

| Parameter | Baseline and frozen V2 value |
| --- | --- |
| Model / reasoning effort | `gpt-6-astra` / `high` |
| Declared context per agent | 200,000 tokens |
| Automatic compaction | 180,000 tokens, `total` scope |
| Sessions | fresh and ephemeral |
| Challenges and verifiers | currently frozen versions |
| Dependencies / human functional help | standard library only / none |

## What “validated context limit” means

Active capacity, compaction threshold and cumulative usage are separate. Each
role file must set the 200,000-token window and 180,000-token `total`
compaction threshold. Strict configuration validation must accept it; every
consultant must start in a clean thread with no inherited conversation; and
`run.json` must retain role, thread ID, values and the role file's SHA-256.
The minutes map visible text and available counters to that thread.

This proves Codex client configuration and input isolation, not an internal
server limit. If native delegation cannot provide this evidence, use distinct
ephemeral `codex exec` sessions with the same options. Otherwise stop before
the first model call.

See the official [Codex configuration reference](https://developers.openai.com/codex/config-reference)
and [subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).

## Pre-registered organisation

The main candidate is the sole orchestrator/writer. SA-01 is a requirements and
security analyst; SA-02 is a software architecture and testability specialist;
SA-03 is an adversarial QA critic. All are read-only, with no nested delegation
or access to another run.

SA-01 and SA-02 first answer independently. Their full visible answers are
then cross-relayed, and each has exactly one response to agree, disagree or
revise. The main candidate records a decision table and writes the first
solution. SA-03 receives the challenge, solution and decision table for one
final critique. Every recommendation is marked accepted, rejected or
unverifiable with a concise reason.

The orchestrator resolves recommendations, implements, documents and runs the
official verifier. Only `solution/` may be written during the run. Candidates
and consultants must not run Git operations; experimental publication occurs
after closure in a separate commit.

## Required measurements and order

Record first-pass and independent final scores, total and per-role duration
when available, genuine per-agent token counters, calls, disagreements,
accepted and rejected advice, corrections, human interventions, incidents and
delivered size. Numbered [minutes](PV_TEMPLATE.en.md) preserve every visible inter-agent message
verbatim after secret screening, then records every recommendation and its
reasoned disposition by role. Missing data remains explicitly unrecorded.

Quality is reported as first-pass and final test ratios. Time and tokens are
reported as V2/V1 ratios, alongside wall time, summed agent time, per-role
input/output, coordination volume, agreements, contradictions, duplicates and
accepted advice. V2 dominates only when quality is no lower, costs are no
higher and at least one dimension improves strictly; otherwise it is a
trade-off, not a win.

Run and publish V2 Core first, then V2 Scientific without intermediate tuning.
Observe both before any V2.1 decision. Any parameter change opens a new
campaign and requires comparable baselines to be rerun.
