# Multi-agent minutes template

[Français](PV_TEMPLATE.md) · **English (UK)** · [Español](PV_TEMPLATE.es.md) · [Português](PV_TEMPLATE.pt.md)

This template is mandatory from V2 onwards. It preserves visible text exchanged
between agents and links it to decisions, cost and outcome.

## Identification and team

Record run, campaign, objective, sponsor, experimental orchestrator, main
candidate/sole writer, verifier and first/final result.

| ID | Agent profession | Bounded mission | Allowed input | Write access | Model / effort | Context / compaction |
| --- | --- | --- | --- | --- | --- | --- |
| MAIN | Candidate orchestrator / writer | decide, produce, verify | challenge, messages, solution | `solution/` | … | … |
| SA-01 | Requirements and security analyst | duties, ambiguities, threats | challenge | none | … | … |
| SA-02 | Software architect and testability specialist | structure, invariants, tests | challenge | none | … | … |
| SA-03 | Adversarial QA critic | omissions, regressions, edge cases | challenge, decisions, solution | none | … | … |

`run.json` also records each thread ID, configuration hash and genuinely
available metrics.

## Visible messages

Create one numbered record per sent or returned message. Preserve the full text
after secret screening; disclose omissions rather than silently rewriting.

### MSG-001 — concise title

Record direction, phase, response duration and available input/cache/output/
reasoning counters.

#### Verbatim sent text

> …

#### Verbatim returned text

> …

#### Analytical summary

- testable proposals and new information;
- agreement, contradiction or duplication;
- risk or defect found;
- decision required from MAIN.

## Decision register

| ID | Source | Proposal | Disposition | MAIN's reason | Code or test evidence | Observed effect |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | MSG-… | … | accepted / rejected / unverifiable | … | file, test or check | gain, neutral or regression |

Every recommendation requires a disposition. MAIN's spontaneous decisions
also receive an ID.

## Social analysis and efficiency

Record inter-agent messages, explicit agreements, useful/unresolved conflicts,
duplicates, unique recommendations, dispositions, defects found before/after
the verifier and visible coordination volume in words and tokens when exposed.
Explain influence, consensus, productive disagreement and noise.

Compare V1 and V2 on first-pass quality, final quality, wall time, summed agent
time, input + output tokens, measurable coordination tokens and corrections.
Conclude separately whether quality, time and token gains are demonstrated,
then classify V2 as dominance, trade-off, no gain or inconclusive.

Never reconstruct hidden reasoning. Mark unavailable measures as unrecorded.
