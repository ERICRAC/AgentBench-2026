# Astra V1 — full report

[Français](astra-v1.md) · **English (UK)** · [Español](astra-v1.es.md) · [Português](astra-v1.pt.md)

Both solo candidates in `astra-high-001` have completed and passed separate verification. Earlier V1 runs are [archived](ARCHIVE_V1.en.md), outside this campaign.

| Metric | Core · astra-core-v1-002 | Scientific · astra-scientific-v1-002 |
| --- | ---: | ---: |
| First / final / independent | 6/6 · 6/6 · 6/6 | 9/9 · 9/9 · 9/9 |
| Session duration | 100.175 s | 399.478 s |
| Input | 117769 | 208078 |
| Included cache | 96896 | 167808 |
| Output | 2709 | 12432 |
| Included reasoning | 195 | 1429 |
| Input + output | 120478 | 220510 |
| Additional checks | — | 4/4 |

## Implementation and sequence

Core separates the four operations from its CLI and recovers from input errors. Its first official run passed without a functional correction. An initial verifier-path lookup error is retained in the minutes.

Scientific uses a dedicated parser and postfix arithmetic representation, bounded by size and nesting depth. Sampling reuses the parsed expression; undefined points break the curve, XML serialization protects SVG output, and the CLI retains history. After the first official 9/9, the candidate's extra tests found interpolation outside the interval near the largest float. It corrected interpolation according to endpoint signs and retained four passing regression checks. The orchestrator reran both the frozen suite and these checks after closure.

## Protocol, evidence and limits

Both use `gpt-6-astra/high`, CLI `0.153.4`, Python `3.13.5`, a declared 200,000-token window and 180,000-token compaction (`total`). Fresh ephemeral sessions, no consultants or functional human help, and no observed candidate Git operations. User configuration is ignored; authentication stays outside the repository.

Final JSON usage counters include cache within input and reasoning within output. The completed sessions total 340,988 tokens and 499.653 s; this is not the full campaign cost. Duration includes CLI startup/shutdown but excludes preparation, publication and preflight.

Some Scientific tool outputs are empty in exported JSON. The first 9/9 is supported by the visible candidate statement and exit code 0; final verification was independently rerun. Client configuration is not a measurement of the server context window. Neither a Python-version matrix nor browser visual checks were performed.

[Core PV](../runs/astra-core-v1-002/PV.md) · [Core JSON](../runs/astra-core-v1-002/run.json)

[Scientific PV](../runs/astra-scientific-v1-002/PV.md) · [Scientific JSON](../runs/astra-scientific-v1-002/run.json)

## Retained incidents

`astra-core-v1-001`: server rejected CLI 0.152.1 before candidate work, 5.301 s, usage unrecorded. Updated CLI and started a fresh attempt.

`astra-scientific-v1-001`: quota interruption after initial writing, before verification, 216.929 s, usage unrecorded. Its code is preserved but was not reused. Missing usage prevents a full campaign-cost figure.

[Core incident](../runs/astra-core-v1-001/run.json) · [Scientific incident](../runs/astra-scientific-v1-001/PV.md)

## Observations and next step

Core: 100.175 s / 120,478 tokens versus Sol's 193 s / 556,461. Scientific: 399.478 s / 220,510 versus 541 s / 603,492. These are descriptive differences, not causal model or multi-agent gains: model, CLI and launch instructions changed, with only one completed run per cell.

A defect discovered after 9/9 illustrates ceiling effects. The historical dataclass-loader bias remains documented and the frozen suite unchanged. Publish V1 before V2 preflight; do not start the V2 benchmark yet.
