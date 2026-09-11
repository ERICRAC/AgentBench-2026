# V2.2 CLI qualification

[Français](v2-2-cli-qualification.md) · **English (UK)** · [Español](v2-2-cli-qualification.es.md) · [Português](v2-2-cli-qualification.pt.md)

**Conclusion: changing installation does not remove the blocker.**

Three runs of the same no-model probe: standalone CLI 0.153.4, separately installed official npm 0.153.4, and extension binary 0.154.0-alpha.6.1. Each passes 7/8 checks; the catalogue remains outside the allowlist. Both 0.153.4 binaries have identical SHA-256 hashes. No PATH, account or extension file was changed.

The bundled catalogue assigns gpt-6-astra and gpt-5.6-sol tool_mode=code_mode_only and multi_agent_version=v2. This structural clue is consistent with the observed tools, not causal proof of internals. We do not alter model metadata to force a pass. Switching to Sol high is not a demonstrated fix; Astra medium remains active, Astra high historical only.

57 maintenance tests passed: 52 previous plus 5 catalogue checks (legacy format, nested additional_tools, both locations, empty/duplicate catalogues, unknown tool). Empty does not mean successfully restricted.

The preflight now accepts --cli for an explicit executable and records version, binary hash and public bundled profile fields. Its HTTP provider is local and synthetic, with empty HOME/CODEX_HOME, no authentication or inference. HTTP failures are intentional; no counters represent model cost.

Useful next step: test actual dispatch and denial of prohibited capabilities using non-mutating synthetic calls. Advertisement does not prove executability. No freeze, authenticated probe or benchmark until that boundary is demonstrated. Reinstalling the same version again would not add evidence.

The test installation remains outside the repository in a dedicated temporary directory; no helper/package is published. OpenAI Docs guided official-package selection; conclusions come from local probes.

[JSON](v2-2-cli-qualification.json) · [MCP](v2-2-bridge.en.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/codex/cli) · [README](../README.en.md)
