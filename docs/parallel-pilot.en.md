# Next pilot — modular calculator and parallel development

[Français](parallel-pilot.md) · [English (UK)](parallel-pilot.en.md) · [Español](parallel-pilot.es.md) · [Português](parallel-pilot.pt.md)

**Technical preparation available** — The specification, ten test groups and isolated simulation are now delivered. Two synthetic variants pass and ten injected faults are detected. These results calibrate the apparatus; no model candidate was launched. Authenticated transport still needs adaptation before freeze. [Rapport / Report / Informe / Relatório](../results/parallel-pilot-preparation.en.md).

## Preparation decision

**Offline preparation; proposed protocol, not frozen. No new candidate launched.**
The next comparison targets **delivery time at comparable quality**. Tokens remain a separate constraint and outcome; faster delivery using more tokens is a trade-off.
[Supporting review](../results/intermediate-review.en.md).

The proposed name is **light V2.1**: two developers, one subsequently integrating. It replaces the four-role proposal for this pilot only. Historical V2 remains unchanged. Its single-writer protocol does not authorise this organisation; the new campaign must freeze the permissions below.

## Proposed scope

A new **modular scientific calculator with batch processing**, Python standard library only, no runtime dependencies, `eval` or `exec`. An invalid expression produces a local error while later jobs continue.

| Deliverable | Responsibility | Parallel-phase owner |
| --- | --- | --- |
| `engine.py` | Safe expressions and curve sampling with discontinuities | DEV-A, engine developer |
| `presentation.py` | SVG, JSON batches, error-to-result conversion | DEV-B, presentation developer |
| `cli.py` | Commands, inputs, outputs and errors | DEV-B |
| `README.md` | Usage, contracts, limitations and examples | DEV-B |
| All deliverables | Integration, corrections and final checks | DEV-A, INT session |

Solo receives the same interfaces, decomposition, batch example and test commands, and chooses its work order. No functional scaffold is exclusive to the team.

Interfaces to specify:

- `engine.evaluate(expression, variables=None) -> float`: scientific syntax and precedence explicitly restated in the new contract, without importing historical solutions.
- `engine.sample_curve(expression, x_min, x_max, samples=201)`: pairs with `None` for undefined values.
- `presentation.write_svg(points, output_path, title="")`: valid XML, escaped text, disconnected segments.
- `presentation.run_batch(jobs)`: ordered results `{"ok": true, "value": number}` or `{"ok": false, "error": text}`. Jobs contain `expression` and optional `variables`.
- `python cli.py batch INPUT.json OUTPUT.json`: invalid input structure returns a non-zero exit and a message without traceback. Individual expression errors remain in the results; other jobs continue.
- `python cli.py plot EXPRESSION OUTPUT.svg --min A --max B --samples N`: sample and export to the requested file.

Types, limits and errors are defined in the new [specification](../challenges/modular-calculator-draft/SPEC.md), still subject to expert review before freezing.

## Draft independent suite groups

Checked items are implemented groups calibrated on fixtures, **not candidate verdicts**. The catalogue details coverage and limitations, particularly M10.

- [x] M01: standard imports, deliverables and prohibited mechanisms.
- [x] M02: four operations, precedence, parentheses, powers and signs.
- [x] M03: functions, constants, variable and forbidden names.
- [x] M04: invalid syntax, domains and non-finite results.
- [x] M05: bounds, point counts and sampling discontinuities.
- [x] M06: parseable SVG, escaped title and no bridge across a discontinuity.
- [x] M07: mixed success/failure batch, preserved order and continuation.
- [x] M08: invalid JSON structure and CLI error messages.
- [x] M09: real engine → batch and engine → curve → SVG integration.
- [x] M10: documented API, runnable examples and module responsibilities.

Publish elementary cases and counts after implementing the suite. Calibrate its loader on standard Python constructions and equivalent implementations; inject known faults to test detection. Reserve an independent robustness evaluation without calling already-public tests hidden. Historical 6/9 groups remain unchanged.

## Organisation and observation

V1: one fresh session and one candidate for the entire scope. Light V2.1: two simultaneous sessions in isolated directories, each receiving the common contract and its assignment. Neither reads the other's live files. The orchestrator assembles finished snapshots without edits and starts INT with both submissions and notes. INT may correct all files; attribute each correction.

Integration starts only after both developers finish. Out-of-scope files, missing deliverables or transport failures stop the attempt with preserved evidence; no automatic retry. Validate isolation using fake candidates before live execution.

Keep mandates, visible responses and integration messages. Number findings and connect clause, evidence, decision, change and test. Track corrected defects, regressions, false positives and duplication. Documentation quality counts as a measured gain only under a predeclared rubric.

Measure organisational wall time, actual developer overlap, summed agent time, integration and verification separately. Report input, cache and output tokens per session, plus interrupted-attempt costs and preparation outside candidates.

## Proposed budget and checkpoint

Both organisations request Astra medium. Proposal for approval at freeze: **one solo pilot followed by one parallel pilot**, an **intersession threshold of 150,000 tokens per organisation**, hence **300,000 nominal tokens for the pair**, no retries. Parallel sessions can jointly overshoot before the next check: this is neither a hard cap nor a Plus quota guarantee.

Solo can exceed the threshold within its sole session. Publish its quality and costs before the team run; do not start the team automatically if available budget or usage accounting prevents compliance with the agreement. Balance order for repetitions. A single pair remains exploratory.

**Reminder: expert review of the final protocol with the most powerful available model before freeze and launch.** Model ranking and effective capabilities are not certified here. Preparation is authorised; launch scope and budget still require approval against ready artefacts.

## Navigation and link diagnosis

The four reported files exist. URLs containing the internal `vscode-cdn.net` domain come from editor rendering and are absent from the Markdown sources. Client-side WSL behaviour cannot be tested here. In VS Code, use **Ctrl+P** from the repository root:

```text
scripts/audit_intermediate.py
results/intermediate-review-data.json
results/CONCLUSIONS.md
docs/acceptance-tests.md
```

`python3 -B scripts/check_links.py` scans tracked Markdown, relative links, references, HTML images and heading anchors. GitHub anchors are approximated; it is not a browser and does not fetch external sites.

Four unavailable links remain in immutable candidate messages. Published replacements: [simple code](../runs/astra-medium-core-v2-2-supervised-002/solution/calculator.py), [simple documentation](../runs/astra-medium-core-v2-2-supervised-002/solution/README.md), [scientific code](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py), [scientific documentation](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md).

## Delivery status

The specification, ten test groups and isolated simulation are now delivered. Two synthetic variants pass and ten injected faults are detected. These results calibrate the apparatus; no model candidate was launched. Authenticated transport still needs adaptation before freeze. [Rapport / Report / Informe / Relatório](../results/parallel-pilot-preparation.en.md).
