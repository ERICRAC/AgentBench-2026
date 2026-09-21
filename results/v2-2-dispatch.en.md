# V2.2 — actual dispatch after the update

[Français](v2-2-dispatch.md) · **English (UK)** · [Español](v2-2-dispatch.es.md) · [Português](v2-2-dispatch.pt.md)

## Final qualification verdict — not ready to freeze

**Qualification closes with NO-GO for the current automated setup. No benchmark was launched.** This is not a calculator or Astra failure: launcher integration and isolation guarantees remain incomplete. Incremental qualification stops here; the next decision concerns which setup to use.

| Requirement | Verdict and evidence |
| --- | --- |
| Developer → reviewer → developer | Two simulations rerun, three sessions each; no candidate score |
| Local output capture | Passed: stdin, stdout, stderr, non-zero exit, 2 MB without truncation and non-UTF-8 bytes preserved |
| Local transport interruption | Passed: timeout and real SIGINT; partial traces retained, child stopped, interrupted checkpoint |
| Tool isolation | Partial: earlier Bubblewrap evidence and eight patch refusals preserved; no new whole-chain certification |
| Delegation prohibition | Not technically demonstrated; no spawn_agent attempted, native listing previously callable |
| Complete live launcher | Not ready: run_relay rejects simulation=False; MCP bridge tested separately, no connected live adapter |
| CLI → MCP → process capture/termination and model access | Not qualified end to end; no authenticated call or quota guarantee |

**68 maintenance tests passed**, not 68 calculator tests. Two new tests cover exact binary capture and SIGINT with child termination verification. The prepared `codex exec` command now uses `-c default_permissions=...` instead of `-P`; the existing sandbox path retains `-P`. Argument parsing with `--help` succeeds (exit zero), which proves neither profile loading nor effective isolation.

OpenAI Docs informed this profile-selection correction; assumed configuration is no substitute for runtime evidence. [Official permissions](https://learn.chatgpt.com/docs/permissions). [Structured assessment](v2-2-qualification.json) · [Transport tests](../tests/test_v2_2_transport.py) · [Locked launcher](../scripts/run_v2_2.py).

### Proposed simplification — pending approval, not applied

A **supervised pilot** with three fresh CLI sessions, Astra medium: developer, snapshot review, corrections. A new directory outside the repository containing only the challenge and deliverables; capture visible messages, available metrics, file differences and independent verdict. No custom MCP bridge or extra framework for this pilot.

**Explicit trade-off:** separate directories and instructions are not complete technical isolation. Non-delegation and access would be governed by instructions and audits of available traces, without claiming to prove the absence of unobserved access. Any observed breach would invalidate the run; no secret protection would automatically be removed. Exact permissions must be documented before launch.

Label this pilot exploratory and disclose setup differences; do not claim strict historical comparability without a V1 reference under identical conditions. Alternatively, retain strong isolation as a requirement and accept a separate integration project before benchmarking.

**Decision requested: accept this supervised pilot instead of pursuing the reinforced automated setup?** Approval would not itself authorise a launch: revise the scope and explicitly freeze it first. General governance, challenges and historical results remain unchanged.

## Earlier evidence preserved

## Follow-up — native write checks

**Eight additional probes: four targets × two binaries, eight explicit refusals, all canaries unchanged.** `apply_patch` is available but cannot perform these writes with `sandbox_mode="read-only"` and `approval_policy="never"`. This resolves that specific doubt, not the entire V2.2 preflight.

| Synthetic modification target | CLI 0.153.4 | Extension 0.154.0-alpha.6.2 |
| --- | --- | --- |
| File inside solution/ | Refused, unchanged | Refused, unchanged |
| Parent dummy CHALLENGE.md | Refused, unchanged | Refused, unchanged |
| File outside workspace | Refused, unchanged | Refused, unchanged |
| Symbolic link to that outside file | Refused, target and link unchanged | Refused, target and link unchanged |

Each probe creates a fresh temporary directory, three canary files and a link. The local provider returns one fixed patch instruction. Afterwards, the verifier compares all three files' bytes and the link destination; the temporary directory is then removed. The “outside” file remains inside our owned temporary tree: no user data is targeted. No candidate model, account, secret or sub-agent is used.

**66 maintenance tests passed**, including three additions: fixed relative targets; refusal to extend MCP approval to patches; strict recognition of the observed refusal. The eight CLI probes are separate from these unit tests. [Eight-probe JSON evidence](v2-2-native-patch.json) · [Test sources](../tests/test_v2_2_dispatch.py).

Overall status remains `blocked_tool_catalog`, not “preflight passed”. The earlier results below and their JSON remain preserved. Native refusal is tested with a REV-01 bridge; this does not qualify final MAIN integration, native reads, interruptions, complete capture or prevention of agent creation. No `spawn_agent` call was attempted.

OpenAI Docs informed the use of two distinct controls: a read-only sandbox and a no-approval policy. Integrity findings come from local probes, not documentation. [Official documentation](https://learn.chatgpt.com/docs/agent-approvals-security).

Reproduce without a model, one target at a time; other fixtures: `patch_contract`, `patch_outside`, `patch_symlink`. Select another installation with `--cli BINARY_PATH` without changing PATH. A non-zero exit remains expected: deliberate provider stop and non-compliant catalogue.

```bash
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture patch_solution --enable-code-mode-host-for-probe
```

**Next:** qualify delegation blocking without starting a candidate, then interruptions and capture. Keep Astra medium; no freeze or automatic launch.

## Previous stage — MCP dispatch

The extension update is visible: 0.154.0-alpha.6.2, previously 0.154.0-alpha.6.1. Terminal CLI remains 0.153.4 with the same hash. This work changed no global settings, PATH, account or VS Code files.

**The CLI → executor → MCP → Bubblewrap → response path is demonstrated for a fixed printf. It works on both tested versions after enabling the Code Mode host and explicitly approving only the probe's MCP tool. Success is therefore not attributable solely to the update.**

63 maintenance tests passed, including 6 new fixture/response tests. Eight distinct diagnostic probes below: not eight benchmarks or eight overall validations.

| Probe | Version | Observation |
| --- | --- | --- |
| Host disabled | 0.153.4 | Execution refused: code-mode host is disabled |
| Runtime inventory | 0.153.4 | Six tools available inside the executor |
| Approved bridge | 0.153.4 | printf executed, exact output, exit zero |
| Updated inventory | 0.154.0-alpha.6.2 | Same six-tool inventory |
| Bridge without approval | 0.154.0-alpha.6.2 | Approval refusal; no MCP tools/call |
| Updated approved bridge | 0.154.0-alpha.6.2 | printf executed; MCP tools/call observed |
| Native terminal | 0.154.0-alpha.6.2 | tools.exec_command absent; no command executed |
| Agent listing | 0.154.0-alpha.6.2 | Read executed: one /root orchestrator, no subagent |

## Correction to our interpretation

An advertised tool can be refused at execution. The old catalogue check still fails but could not establish that all disable settings were ineffective. Historical text and measurements remain intact; this is an added clarification, not retroactive reinterpretation of runs.

The runtime inventory includes apply_patch, clock__curr_time, list_mcp_resource_templates, list_mcp_resources, mcp__agentbench__confined_command and read_mcp_resource. The separate collaboration.list_agents function is also callable. We did not attempt spawn_agent or an apply_patch write.

## Limits and next step

Only the probe's fixed command is demonstrated through the bridge. Native permissions, MAIN/REV writes through every route, effective prevention of agent creation, interruptions and complete capture require qualification before freeze. Presence of apply_patch proves neither disclosure nor successful write; listing does not prove that spawning would work. No model switch needed: Astra medium active, Astra high historical only.

OpenAI Docs informed streaming events and per-tool MCP approval. The probe approval option is rejected for any other fixture; it does not alter global policy or authorise a benchmark. Model-like responses are fixed and served on loopback with empty HOME/CODEX_HOME; no real model service or secret is used.

New tests: matching SSE events; arbitrary fixture/broader approval rejected; only known call_id captured; missing/duplicate outputs unverified; exact echo required; refusal/inventory/listing distinguished.

Probes retain a non-zero exit: the overall catalogue remains non-compliant and the stub deliberately stops after the tool response. This does not invalidate the confirmed echo, but is not launch approval.

[Tests](../tests/test_v2_2_dispatch.py) · [JSON](v2-2-dispatch.json) · [CLI](v2-2-cli-qualification.en.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/extend/mcp)

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture inventory
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture bridge_echo --enable-code-mode-host-for-probe --approve-bridge-echo-for-probe
```

[README](../README.en.md) · [V2.2](../governance/V2_2_PROTOCOL.en.md)
