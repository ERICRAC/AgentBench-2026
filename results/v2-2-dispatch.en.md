# V2.2 — actual dispatch after the update

[Français](v2-2-dispatch.md) · **English (UK)** · [Español](v2-2-dispatch.es.md) · [Português](v2-2-dispatch.pt.md)

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
