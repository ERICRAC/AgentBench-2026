# Astra medium V1 preflight — prepared, not launched

[Français](astra-medium-v1-preflight.md) · **English (UK)** · [Español](astra-medium-v1-preflight.es.md) · [Português](astra-medium-v1-preflight.pt.md)

Historical document: both V1 runs are now complete. The 44/44 check below describes preparation and must reject these already executed directories. The remaining text preserves authorisations and observations from that stage. [Full comparison and evidence](astra-medium-v1-v2.en.md)

Two fresh solo attempts are prepared. **44/44 static checks pass; no candidate, no test model call, no score produced.** Preparation only was authorised. This conversation’s model selection does not replace explicit future candidate configurations.

## Reserved attempts

- Simple calculator : [astra-medium-core-v1-001](../runs/astra-medium-core-v1-001/run.json) · [configuration](../runs/astra-medium-core-v1-001/config.toml) · [challenge](../runs/astra-medium-core-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-core-v2-001/run.json)
- Scientific calculator : [astra-medium-scientific-v1-001](../runs/astra-medium-scientific-v1-001/run.json) · [configuration](../runs/astra-medium-scientific-v1-001/config.toml) · [challenge](../runs/astra-medium-scientific-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-scientific-v2-001/run.json)

Each directory contains CHALLENGE.md, config.toml and run.json. Both local solution/ directories are empty: no .gitkeep, no previous solution inspected or copied. Git does not retain empty directories; recreate them after cloning with the commands below before checking.

## Comparability and measurement

Associated campaign: astra-medium-001, **V1 extension prepared after completed V2 runs**, without changing their metadata. Fresh solo candidate, no delegation; preparation/publication orchestrator outside measurements. Publish Core before Scientific, with no refinement between them.

| Item | Choice and evidence |
| --- | --- |
| Model / effort | gpt-6-astra / medium in each config.toml; checked against all four V2 roles. |
| Context / compaction | 200,000 / 180,000, total scope, as in V2. Not a cumulative token cap. |
| V1 configuration | Copy of governance/astra-v1.toml; only high → medium changes. Governance unchanged. |
| Permissions | workspace-write for V1 and V2 MAIN; read-only for consultants. Web disabled, approval never, no-delegation instructions. Writing restricted to solution/ by instructions; static checks do not prove actual isolation. |
| Prompts | Historical codex-single.md and scientific-single.md, frozen hashes. No advice from V2 added. |
| Challenges / verifiers | Hashes identical to V2; simple: 6 groups/14 checks; scientific: 9 groups/57 checks. [Explicit list](../docs/acceptance-tests.en.md). |
| Capture | Historical scripts/capture_session.py unchanged. No new observer wrapper. CLI duration; V2 also measures relay work, a documented organisational difference. |
| Observed environment | Codex CLI 0.153.4, Python 3.13.5, Node 20.19.2, npm 9.2.0. Same CLI as V2; other historical environment details not certified here. |
| Future results | First/final/independent passes, fixes before/after first pass, duration, input/cache/output/reasoning, interventions and visible texts. Currently null, not zero. |

V2 has seven sessions for four roles; V1 plans one. V2’s first official pass necessarily follows criticism, unlike V1. These differences are the experimental treatment, not parameters to equalise retroactively.

## Preflight checklist

The [reproducible check](../scripts/preflight_v1_medium.py) performs **22 assertions per directory, 44 total**:

- [x] V1 config identical except effort; identity/mode; prepared status and launch not authorised.
- [x] No invented results; solution present, empty and reported writable.
- [x] Six hashes: configuration, prompt, challenge, tests, capture and verifier.
- [x] Challenge matches SPEC; completed V2 reference in associated campaign.
- [x] Shared challenge/test hashes with V2; parameters and permissions checked for four roles.
- [x] Acceptance method count checked syntactically (6 or 9), without execution; recorded CLI version matches.

codex --version and codex exec --help succeeded and expose the runner’s options. Local warning: PATH aliases could not be created on a read-only filesystem; both commands work. TOML parsed, **not validated by launching Codex with these configurations**.

```bash
mkdir -p runs/astra-medium-core-v1-001/solution runs/astra-medium-scientific-v1-001/solution
python3 -B scripts/preflight_v1_medium.py
```

## Future execution — not authorised here

Only after new authorisation: recheck environment, hashes, quota and directories; launch Core in a fresh session with its own configuration and historical prompt. Check and publish its result before Scientific. Keep interruptions; restarting from scratch needs a new identifier.

Private capture outside repository; then publish screened minutes with candidate role, exact mandate, visible replies, commands, checks and decisions. No private reasoning, secrets or working clock times in Markdown. Do not pretend new annotations or counters existed in historical runs.

## Limits, budget and next steps

**Static preparation ready; experimental launch not authorised.** Actual Astra access, authentication, quota and runtime enforcement of context/effort are untested. No further installation requirement identified. Explicit settings follow [official Codex documentation](https://learn.chatgpt.com/docs/config-file/config-reference), which does not guarantee account access.

Exact cost unknown: no new total-token or wall-time cap. Adding a cap would change conditions versus V2 and require a separate decision. Preflight tokens are not candidate cost.

The same alias does not prove an immutable server snapshot; V1 after V2, no randomisation/repeats, load/cache variation and possible frozen scientific loader defects limit causality. **Qualified comparison, not perfectly identical conditions.** Existing quality/time/token dominance remains the decision rule.

Next decision: separately authorise simple V1, then publication before scientific. No V2.1/V2.2 or governance change here.

[V2 Astra medium](astra-medium-v2.en.md) · [Conclusions](CONCLUSIONS.en.md) · [README](../README.en.md)
