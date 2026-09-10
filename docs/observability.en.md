# Instrumentation and summary publication

**English (UK)** · [Français](observability.md) · [Español](observability.es.md) · [Português](observability.pt.md)

[Reading guide and V2 diagram](reading-guide.en.md) · [Summaries](../results/run-summaries/index.en.md) · [Audit](documentation-audit.en.md)

## Scope

Maintenance outside runs. No benchmark rerun or historical solution edited. [run_v2.py](../scripts/run_v2.py), historical publisher, prompts, permissions, roles, barriers and criteria are unchanged. The guide’s diagram explains the frozen protocol; it does not create new orchestration.

[run_v2_observed.py](../scripts/run_v2_observed.py) invokes the existing runner and wraps only run_session. Activation is **optional** and must be declared and preregistered before the next campaign. Measurement writes add small unquantified overhead; do not claim identical timing to old runs. Fake-session tests do not validate future real model calls.

## Generic schema

[observe_sessions.py](../scripts/observe_sessions.py) does not schedule work. It accepts N sessions, roles and groups. Only v2_topology describes frozen V2; future V2.x/V3 requires its own approved graph.

| Field | Kind and definition |
| --- | --- |
| session_id, role | Canonical identity, not a model name. |
| parallel_group | Specified concurrent group; null for sequential phases. |
| depends_on | Sessions that must finish before starting; specified barriers. |
| receives_from | Source session identifiers for texts or artefacts, not evidence of adoption. External challenge/mandate explained in guide. |
| writes_solution | Specified permission, not evidence of actual writing. |
| started_at_seconds, ended_at_seconds | Monotonic measurements relative to wrapper entry, before runner preparation. Never civil clock times. |
| duration_seconds inside observation | End minus start around the entire invocation: configuration, CLI, capture and event parsing; excludes observation writing. |
| Historical duration_seconds | Original CLI measurement preserved in place, not replaced by invocation duration. |
| outcome | returned or failed, not an acceptance verdict. |

Wrapper origin differs from historical wall_duration_seconds origin. Do not subtract across these frames. Only overlapping measured intervals establish overlap. Historical consultations have durations but no start/end: no invented exact timeline.

## Future workflow — only after run authorisation

First preregister a fresh directory, challenge and configurations under the approved protocol. NEW-RUN below is a placeholder, not a run created here:

```bash
python3 -B scripts/run_v2_observed.py --run runs/NEW-RUN --challenge calculator
```

The announced private capture directory contains observations.json, updated at each session completion, including failure. A hard stop may leave a session absent: absence is not zero. The observer adds no prompts, error text, private reasoning or absolute paths.

After reviewing captures and normal publication through publish_v2.py, enrich a **new copy** of the trace:

```bash
python3 -B scripts/attach_observations.py --trace runs/NEW-RUN/trace.json --observations /tmp/CAPTURE/observations.json --output runs/NEW-RUN/trace-observed.json
```

Merge rejects existing destinations, missing/duplicate identifiers, role mismatches, non-finite values and barrier violations. It preserves original metrics and exports an allowlist. Partial captures need a separate interruption report; never bulk-publish private captures. The historical filter is not a complete secret detector: prior review remains mandatory.

In **future** run metadata, reference trace-observed.json and its hash, wrapper, observer, adapter, their hashes and the historical runner used. Never alter published run metadata. The original publisher remains usable; enrichment and summary generation are outside the candidate.

## Editorial generation

```bash
python3 -B scripts/summarize_runs.py
python3 -B scripts/summarize_runs.py --check
python3 -B -m unittest discover -s tests -v
python3 -B scripts/check_documentation.py
markdownlint '**/*.md'
```

The first call regenerates five V2 covers and the index in four languages. Facts: run.json/trace.json; manually reviewed analysis: [run-interpretations.json](run-interpretations.json). Edit that source, not generated pages. Missing values remain missing; cache/reasoning are never counted twice.

A future topology supplies run.json with run_id, challenge, mode, status, model/effort, verification, usage and trace; trace contains roles and sessions, each with phase or session_id, role, counters and optional observation. Verification keys follow historical files. Local roles and unknown phases are supported without inventing V2.

```bash
python3 -B scripts/summarize_runs.py --run runs/NEW-RUN --interpretation /tmp/interpretation-reviewed.json
```

Editorial JSON uses fr/en/es/pt keys; missing text remains unrecorded. Output stays in results/run-summaries, never runs/. Add the future cover to an appropriate campaign index: the current index lists only five complete V2 runs. Generic code is not approval of V3 protocol.

## Checks and limits

Tests cover unchanged returns/arguments, preserved failures, five parallel roles, equality of seven prompts/arguments between runners, barriers, simulated timing, missing counters, overwrite refusal, a local role and reproducible generation. They measure neither network latency nor future model consumption.

[Executed checks and rendering limits](documentation-audit.en.md). Real validation of the new runner awaits an explicitly authorised run.
