# Technical preparation — V1 / light V2.1 pilot

[Français](parallel-pilot-preparation.md) · [English (UK)](parallel-pilot-preparation.en.md) · [Español](parallel-pilot-preparation.es.md) · [Português](parallel-pilot-preparation.pt.md)

**Offline preparation delivered; campaign not frozen and no candidate launched.**
The question remains: does parallel development reduce delivery time at comparable quality, including integration?

## Delivered artefacts

- [Complete candidate specification](../challenges/modular-calculator-draft/SPEC.md): four files, scientific syntax, explicit limits, curves, batches, CLI errors and documentation. Canonical French agent instruction.
- [Detailed ten-group catalogue](../challenges/modular-calculator-draft/catalogue.json) and [independent suite](../challenges/modular-calculator-draft/tests/test_acceptance.py). M01 constraints; M02 arithmetic; M03 functions; M04 errors/limits; M05 sampling; M06 SVG; M07 batches; M08 CLI errors; M09 integration; M10 documentation.
- [Calibration](../tests/test_modular_acceptance.py): two passing synthetic variants and ten detected injected faults, one per group. Fixtures are maintenance tools, never candidate references to distribute.
- [Parallel simulation](../scripts/preflight_parallel_pilot.py): two isolated fake processes, readiness barrier, unedited assembly, then a fake integrator.
- [Evidence, relative durations and hashes](parallel-pilot-preparation.json). Seven targeted maintenance tests passed; twelve suite executions in calibration (two variants and ten mutants).

## What the checks establish

The loader supports normal Python imports, including a dataclass and sibling imports. Both permitted curve representations, polyline and M/L path, pass. Each mutation fails its intended group. This calibrates the suite rather than establishing completeness.

DEV-A and DEV-B read their own contract but cannot modify it or read/write the peer canary, including through symlinks. Six checks per developer pass. Both processes are ready before release; INT starts after both results are collected. Hashes track assembly and one synthetic correction attributed to INT.

The outer sandbox blocked the first isolation attempt. An approved elevated local execution succeeded while retaining child-process confinement. No credentials or model calls. Completion times are parent observations, not exact kernel exit timestamps or measured collaborative gains.

## Limitations and next delivery

M10 checks API names, limits and docstrings; explanation quality and execution of documentation examples are not yet evaluated automatically. AST scanning is not a malicious-candidate defence. Coverage limitations are explicit in the catalogue; no hidden tests are claimed.

The simulator has no model input or live mode. Before launch, authenticated transport must support both writer roles, real messages and usage counters, all tool boundaries, final mandates and a frozen manifest. The isolated simulation has no credentials and is not a ready Codex launcher.

The [proposed protocol](../docs/parallel-pilot.en.md) keeps Astra medium, solo then team, and a 150,000-token intersession threshold per organisation: a proposal, not a hard cap. Segmented solo remains a separate later control. Review these artefacts before freezing; **requested reminder: use the most powerful available model at that checkpoint**. Preparation does not imply new launch or budget approval.

## Reproduce without models

```bash
python3 -B -m unittest tests/test_modular_acceptance.py tests/test_parallel_pilot.py
python3 -B scripts/preflight_parallel_pilot.py --simulate
```

The second command requires Linux namespaces permitted for bubblewrap. A refusal must be reported as blocked, never counted as a pass.
