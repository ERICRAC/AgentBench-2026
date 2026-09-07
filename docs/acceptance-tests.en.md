# Acceptance-test catalogue

[Français](acceptance-tests.md) · **English (UK)** · [Español](acceptance-tests.es.md) · [Português](acceptance-tests.pt.md)

## Reading the verdicts

`unittest` reports one unit per **test method**. AgentBench therefore has six
Core groups and nine Scientific groups. On a fully passing run, these 15 groups
currently execute **71 elementary assertions**: 14 Core and 57 Scientific.
The public wording should expose both levels: **6/6 Core groups — 14/14 checks
passed**, rather than presenting `6/6` as six exhaustive requirements.

Audit path: [Core specification](../challenges/calculator/SPEC.md) →
[executable Core tests](../challenges/calculator/tests/test_acceptance.py) →
[Scientific specification](../challenges/scientific-calculator/SPEC.md) →
[executable Scientific tests](../challenges/scientific-calculator/tests/test_acceptance.py) →
[published results](../results/README.en.md).

## Core Calculator — 6 groups, 14 checks

- [ ] **C01 · Deliverables (2):** `calculator.py` and `README.md` exist.
- [ ] **C02 · Dynamic execution (1):** no `eval()` or `exec()` call.
- [ ] **C03 · Arithmetic (4):** `2 + 3 = 5`, `-2 - 3 = -5`,
  `1.5 * 2 = 3.0`, and `7 / 2 = 3.5`.
- [ ] **C04 · Unknown operator (1):** `%` raises `ValueError`.
- [ ] **C05 · Division by zero (1):** division by zero raises
  `ZeroDivisionError`.
- [ ] **C06 · CLI resilience (5):** exit code 0, no traceback, outputs 5,
  reports an understandable error, then resumes and outputs -8.

[Inspect the six methods](../challenges/calculator/tests/test_acceptance.py#L23).

## Scientific Calculator — 9 groups, 57 checks

- [ ] **S01 · Deliverables and documentation (7):** both files exist; the
  README contains `evaluate`, `plot`, `svg`, `sin`, and `history`.
- [ ] **S02 · Safety and dependencies (2):** no `eval()`, `exec()` or
  `compile()`; standard-library imports only.
- [ ] **S03 · Operators (10):** five expressions test precedence,
  parentheses, right-associative powers and unary signs; each checks `float`
  type and value.
- [ ] **S04 · Maths language (6):** trigonometric and inverse functions,
  `sqrt`, `ln`, `log10`, `exp`, `abs`, constants and scientific notation.
- [ ] **S05 · Variables and forbidden names (5):** valid `x`; missing `x`,
  unknown calls, `__import__` and attribute access are rejected.
- [ ] **S06 · Errors (6):** empty and incomplete input, invalid real domains,
  overflow and division by zero.
- [ ] **S07 · Sampling (8):** point count, both endpoints, midpoint,
  discontinuity as `None`, equal/reversed bounds and too few samples.
- [ ] **S08 · Passive SVG (7):** SVG root, two axes, curve, no script or
  JavaScript URL, escaped title and rejection when no finite point exists.
- [ ] **S09 · CLI (6):** clean exit, no traceback, correct result, readable
  domain error, recorded history and generated curve file.

[Inspect the nine methods](../challenges/scientific-calculator/tests/test_acceptance.py#L28).
The [French catalogue](acceptance-tests.md) expands every one of the 71 checks
with its exact input and expected outcome.

## Limits

These 71 checks describe current coverage, not absolute quality. They do not
replace edge-case analysis, exploratory checks or statistical repetitions. A
new official assertion would define a new suite and campaign; historical
results would remain attached to this version.
