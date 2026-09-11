# V2.2 technical preflight — simulations, no model

[Français](v2-2-preflight.md) · **English (UK)** · [Español](v2-2-preflight.es.md) · [Português](v2-2-preflight.pt.md)

**V2.2: pilot choices approved; 46 maintenance tests and local isolation 30/30.** Six synthetic processes, no model calls. Native profile 26/30: model integration unqualified, launch locked. Sol/Astra and effort comparison retained. [Transport / isolation](v2-2-transport.en.md)

**Static/synthetic preflight passed: 2 challenges × 3 phases; 26 new tests, 38 maintenance tests in total. No model call, calculator score or historical run change.** Protocol remains unfrozen and launch unauthorised.

## Delivered

The [relay](../scripts/run_v2_2.py) executes initial MAIN → REV-01 → final MAIN through an injected deterministic transport. The [preflight](../scripts/preflight_v2_2.py) checks choices and both configurations, inventories 15 hashes and simulates both challenges in fresh temporary directories. Three [mandates](../governance/V2_2_PROTOCOL.en.md) unchanged. [Draft settings and choices](../governance/v2-2-draft/choices.json).

Private captures contain exact prompts, JSONL events, visible replies, commands/outputs, counters, phase checkpoints and initial/final snapshots with text/SHA-256. No automatic publication filter: do not push raw directories. Reasoning stays private and out of handovers. Failure preserves available evidence and stops progression without retry. If incomplete capture prevents counter parsing, raw data remains and the total stays unknown.

**Simulation is not live transport validation.** The module builds Codex arguments for inspection but invokes no model process; --live fails before creating captures. Fake sessions write SIMULATION ONLY files, not solutions. Fixture counters are synthetic (39 input + output per nominal scenario), never real consumption. Public preflight publishes no artificial score or usage as benchmark evidence.

Hashes detect persistent prohibited writes inside the workspace; they neither prevent nor detect all external reads or transient writes. read-only/workspace-write settings are checked, not enforced by a real OS sandbox in these Python tests. Declared truncation or recognised markers stop processing; no marker does not prove complete CLI output. SIGKILL cannot be caught: only the last checkpoint is guaranteed. Effective permissions, live transport/process termination, independent snapshot verification and screened publication still need qualification before benchmarking.

## Reproduce without a model

```bash
python3 -B scripts/preflight_v2_2.py
python3 -B -m unittest discover -s tests -v
```

```bash
sim_root=$(mktemp -d /tmp/agentbench-lean-demo-XXXXXX)
python3 -B scripts/run_v2_2.py --simulate --challenge calculator --output "$sim_root/simple"
python3 -B scripts/run_v2_2.py --simulate --challenge scientific-calculator --output "$sim_root/scientific"
```

## Checklist of 26 V2.2 tests

Each row maps to a test_ method in the [test file](../tests/test_v2_2.py), alphabetically. The 12 previous maintenance tests are additional; none replaces calculator groups. V2.2 tests replace subprocess.Popen and socket entry points with failing guards.

| ID | Check | test_… |
| --- | --- | --- |
| T01 | Capture separate from candidate workspace | capture_cannot_be_nested_in_workspace |
| T02 | Configurations and unexecuted command | configuration_and_unexecuted_argv |
| T03 | Effort drift rejected | configuration_drift_rejected |
| T04 | Invalid event envelopes rejected | invalid_event_envelope |
| T05 | Incomplete JSON retained; phase stopped | invalid_json_capture_preserved |
| T06 | Keyboard interruption checkpointed | keyboard_interrupt_checkpointed |
| T07 | Live mode rejected before transport or writes | live_rejected_before_transport_or_capture |
| T08 | Missing deliverable blocks progression | missing_deliverable_stops |
| T09 | Extra deliverable blocks progression | missing_or_extra_deliverable_stops |
| T10 | Missing usage remains unknown | missing_usage_is_not_zero |
| T11 | Existing solution/capture reuse refused | nonempty_solution_and_existing_capture_refused |
| T12 | Failure retains raw capture and counters | nonzero_process_retains_raw_and_metrics |
| T13 | Missing outputs, truncation, unknown events, invalid usage | parser_rejects_incomplete_unsupported_events_and_bad_usage |
| T14 | Review failure: no retry or final phase | phase_failure_preserved_without_retry |
| T15 | Two simulated challenges, hashes, no score | preflight_no_model_no_verdict_and_hash_inventory |
| T16 | Changed choices or unexpected authority refused | preflight_refuses_changed_choice_or_authority |
| T17 | Challenge modification detected | protected_workspace_write_stops |
| T18 | Reasoning excluded, visible text intact | reasoning_excluded_visible_text_unchanged |
| T19 | Thread reuse rejected | reused_thread_stops |
| T20 | Reviewer write detected; no final phase | reviewer_write_stops_before_final |
| T21 | Simulation CLI for both challenges; no overwrite | simulation_cli_both_challenges_and_no_overwrite |
| T22 | Symlinks, hardlinks and binary files rejected | snapshot_rejects_symlinks_hardlinks_and_binary |
| T23 | Symlink workspace rejected | symlink_workspace_rejected |
| T24 | Order, full handover, snapshots, usage and timing | three_phases_full_handover_and_snapshots |
| T25 | Explicit truncation marker blocks | truncated_output_marker_stops |
| T26 | Word overrun retained without truncation or recall | word_overrun_recorded_without_truncation_or_retry |

## Choices and steps before freeze

Proposal awaiting approval: exploratory pilot, one attempt per calculator, Astra medium, three sessions, one 1200-word review; publish simple before separate scientific authorisation. No new overall cap, stop on quota, no automatic wait/retry. This does not guarantee Plus quota sufficiency. The 18 confirmation runs are a separate, uncommitted proposal. A numerical budget changes the design: decide before freezing and treat references comparably.

After choices are approved, prepare/qualify live transport and isolation without a benchmark candidate; any trivial model probe requires separate authorisation. Only then freeze hashes and request simple-challenge launch approval. Hashes inventory the current draft, not a freeze or model-access preflight.

OpenAI Docs informed separation of JSONL events from visible messages and preparation of ephemeral/sandbox flags. See [official documentation](https://learn.chatgpt.com/docs/non-interactive-mode). Local codex exec --help and version 0.153.4 were inspected without model calls; valid TOML proves neither server acceptance, Astra access nor quota.

[V2.2 protocol](../governance/V2_2_PROTOCOL.en.md) · [JSON](v2-2-preflight.json) · [README](../README.en.md)
