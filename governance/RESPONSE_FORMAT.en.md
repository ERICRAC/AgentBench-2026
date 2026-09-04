# Response format

[Français](RESPONSE_FORMAT.md) · **English (UK)** · [Español](RESPONSE_FORMAT.es.md) · [Português](RESPONSE_FORMAT.pt.md)

Responses must be quick to read yet complete enough to explain what was
actually done. They use named sections instead of artificial numbering and
omit sections that add no useful information.

## Objective

Restate the desired outcome and its acceptance criteria. For a run, identify
the mode, challenge and permitted write boundary.

## Direct answer

Answer the human's questions and decisions directly. State any assumption on
which the answer depends.

## Completed work

Describe material changes, important choices and their rationale. For a
multi-agent experiment, record consulted roles, accepted or rejected advice,
and the orchestrator's decision.

## Verification

Name the checks actually run and their results. Distinguish candidate tests,
protocol controls and Git state; never present an impression as validation.

## Open points

State errors, risks, missing data and decisions required from the human.
Never reconstruct a missing measurement after the fact.

## TODO

Use a short checklist of concrete next actions, distinguishing complete, ready
and blocked work.

## Git delivery

When tracked files changed, finish with the commit and push state. Explicitly
report a local-only commit or dirty worktree.
