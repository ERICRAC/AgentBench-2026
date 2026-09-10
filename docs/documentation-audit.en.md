# Documentation and observability audit

**English (UK)** · [Français](documentation-audit.md) · [Español](documentation-audit.es.md) · [Português](documentation-audit.pt.md)

[Guide](reading-guide.en.md) · [Five V2 summaries](../results/run-summaries/index.en.md) · [Instrumentation](observability.en.md)

## Result and scope

Reading journey: README → guide → two-minute cover → minutes/verbatim → trace/run.json. Four languages, five completed V2 runs covered, no benchmark rerun. The guide explains professions, transmission, parallelism, barriers, corrections and comparison limits. Interpretations are separate from generated facts.

Covers stay outside runs/: editing historical minutes would invalidate their hashes. New summaries lead to intact detail. Governance and protocol are unchanged.

## Executed checks

| Check | Result and scope |
| --- | --- |
| Python maintenance | 12/12 test methods passed, no model call; listed below. |
| Generation | summarize_runs.py then --check: reproducible, current output. |
| Links and languages | check_documentation.py: local links across README/docs/results/logs/governance, reciprocal navigation for new families; 64 historical hashes checked. |
| Markdown | markdownlint '**/*.md' passed with existing historical exclusions. |
| Existing solutions | Nine V1/V2 solutions rechecked: 66 successful group executions. The usual 15 distinct methods repeated, not 66 new tests. |
| Scientific medium candidate checks | 4/4 controle_final.py methods passed, separate from official score. |
| Preservation | git diff 1dd93a7 -- runs challenges prompts governance scripts/run_v2.py scripts/publish_v2.py: no differences. No run counter, text, configuration or solution changed. |

## Twelve explicit maintenance tests

| Test in tests/test_observability.py | Coverage |
| --- | --- |
| test_success_passes_arguments_and_return_unchanged | Same arguments/return, exact relative times, no prompt/path in measurements. |
| test_failure_is_persisted_and_propagated | Same exception propagated; failed status without private error text. |
| test_arbitrary_parallel_agents_are_not_serialised | Five sessions cross a common barrier; measured intervals overlap in this local test. |
| test_original_frozen_runner_and_publisher_hashes | Current historical scripts retain their hashes. |
| test_full_sequence_prompts_arguments_and_barriers_unchanged | Both runners call seven fake sessions: same prompts/arguments, dependencies, two concurrent groups, original function restored. |
| test_allowlist_and_original_duration_preserved | Copy-only merge, private fields excluded, original CLI duration retained. |
| test_rejects_missing_duplicate_or_mismatched_sessions | Reject partial capture, duplicate or mismatched role. |
| test_rejects_invalid_times_and_dependencies | Reject negative/non-finite/inconsistent times, invalid dependency, unknown source. |
| test_merge_cli_does_not_overwrite | Existing destination remains intact. |
| test_missing_metrics_are_not_zero_and_no_fake_timing | Missing data is not zero; no fabricated timeline. |
| test_measured_timing_generic_role_and_no_counter_double_count | Arbitrary local role, interval rendering, no cache/reasoning double counting. |
| test_generated_pages_are_current | Five covers and index, four languages, match generator. |

Reproducible commands in the [technical guide](observability.en.md). Tests never call Codex: they test measurement software, not candidate intelligence.

## Existing verifiers rerun

| Preserved solutions | Groups passed per solution |
| --- | ---: |
| astra-medium-core-v2-001, astra-core-v2-001, sol-core-v2-001 | 6 each |
| astra-medium-scientific-v2-001, sol-scientific-v2-001 | 9 each |
| astra-core-v1-002, sol-core-v1-001 | 6 each |
| astra-scientific-v1-002, sol-scientific-v1-001 | 9 each |

Command: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --solution runs/IDENTIFIER/solution, adding --challenge scientific-calculator for scientific exercises. These are maintenance checks, **not new attempts or benchmark costs**. [The 71 named checks](acceptance-tests.en.md) are unchanged.

## Historical inconsistency audit

“V2 not launched” statements in protocol and old preflight describe freeze-time status. The guide now explicitly separates that from published results; evidence is not rewritten. Historical “contradiction croisée” and “MAIN/RELAY” are explained, not replaced in traces. V2.x remains proposed, without assumed launch or gain.

Three runs reference older publishers: Sol uses commit ad7e234; Core Astra high uses 63f9b92. Their hashes are verified from Git, not aligned artificially with the current file. A clone lacking history must retrieve those commits for this check. The shared experimental runner is unchanged.

## Limits and next steps

- The new wrapper is tested with fake sessions, **not yet a real model run**; measurement overhead is unquantified.
- Mermaid uses reader themes, without a forced light palette. GitHub light/dark rendering was not visually checked here because no rendering browser was available; check on GitHub.
- Link checks cover local files, not Web availability or every GitHub anchor fragment.
- Texts and decisions are observations; absolute novelty, noise and causality are not artificially quantified.
- Astra medium V1 and V2.1/V2.2 protocols remain separate experimental work.

No new Python runtime dependency, governance update or secret publication. The pre-existing local .gitignore edit is excluded from delivery.
