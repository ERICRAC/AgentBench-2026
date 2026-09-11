# V2.2 — tool bridge and catalogue blocker

[Français](v2-2-bridge.md) · **English (UK)** · [Español](v2-2-bridge.es.md) · [Português](v2-2-bridge.pt.md)

## Decision and outcome

**Astra high is historical only: no new runs planned; all results retained.** Astra medium stays active. Sol high remains a separately authorised comparison option. [Recorded decision](../governance/v2-2-draft/model-policy.json).

The confined tool bridge works. **CLI integration is blocked by its actual tool catalogue**, not credits. No model calls, real authentication, freeze or benchmark launch.

## Implementation and checks

The [MCP bridge](../scripts/v2_2_tool_bridge.py) accepts only a command. The orchestrator fixes role, workspace and private capture; arguments cannot override roles, paths, permissions or environment. Bubblewrap allows MAIN to write solution/ and keeps REV-01 read-only. Confined commands receive empty stdin and a cleared environment, without Codex credentials.

**52 maintenance tests passed**, including [6 new tests](../tests/test_v2_2_tool_bridge.py): initialisation/one tool; override rejection; invalid commands; separate non-reusable captures; notifications cannot execute; invalid protocol/methods.

[Real no-model preflight](../scripts/preflight_v2_2_bridge.py): **7 of 8 checks passed**.

- [x] MAIN: handshake/listing, complete stdout/stderr, allowed write.
- [x] REV-01: handshake/listing, complete stdout/stderr, denied write.
- [x] CLI request reaches the local HTTP stub.
- [ ] Candidate catalogue restricted to the confined tool.

[Observations and hashes](v2-2-bridge.json) · [Previous isolation stage](v2-2-transport.en.md)

## Observed blocker

The real CLI uses empty temporary HOME/CODEX_HOME with no inherited token. Its provider points only to a loopback stub rejecting inference with a controlled HTTP error. Headers, prompts and session identifiers are not published.

Codex negotiates MCP 2025-06-18 and calls tools/list. It sends its catalogue in input/additional_tools rather than the usual tools field. The initial empty-list inspection was incomplete, not evidence of absent tools.

The effective catalogue includes functions.exec and collaboration.spawn_agent despite features.shell_tool=false and features.multi_agent=false. Advertisement does not prove every operation would succeed, but it **does not establish exclusive routing through the confined bridge**. MCP is not advertised as the sole direct tool; possible availability through the executor remains unqualified.

The preflight fails until this criterion passes. The CLI's non-zero exit is expected because the stub refuses inference; it is not a quota or account-access check.

## Limits and next step

OpenAI Docs informed MCP configuration and tool-disable settings; accepted configuration is not proof of effective restrictions. [Configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

The MCP interface differs from historical runs and belongs in the new campaign, never retroactively. Raw captures remain private; invalid UTF-8 or infrastructure failure stops the bridge. Client MCP timeouts, truncation, executor routing and full process-tree shutdown still need qualification. Probe timeouts do not approve a new candidate budget.

Next: qualify an effectively restricted configuration or a separate CLI without replacing VS Code's installation; only then request an authenticated Astra-medium probe. No secret belongs in the repository.

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py
```

The second command needs authorised Linux namespace execution and currently must fail the catalogue check. Disposable fixtures are removed; historical solutions are not used.

[Protocol](../governance/V2_2_PROTOCOL.en.md) · [Conclusions](CONCLUSIONS.en.md) · [README](../README.en.md)
