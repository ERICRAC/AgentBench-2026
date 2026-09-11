# Public governance

[Français](README.md) · **English (UK)** · [Español](README.es.md) · [Português](README.pt.md)

**V2.2: confined bridge tested; 52 maintenance tests passed.** Integration blocked: CLI still advertises tools outside the allowlist. No model calls. **Astra high: historical only, no new runs planned.** [MCP / CLI](../results/v2-2-bridge.en.md)

This directory exposes enough method to make the experiment understandable and
reproducible without publishing raw conversations or the author's private
configuration.

- [`RESPONSE_FORMAT.en.md`](RESPONSE_FORMAT.en.md) defines report structure.
- [`LOGGING.en.md`](LOGGING.en.md) defines public logging.
- [`EXPERIMENTAL_DESIGN.en.md`](EXPERIMENTAL_DESIGN.en.md) defines the matrix,
  observation gates and rerun rules.
- [`V2_PROTOCOL.en.md`](V2_PROTOCOL.en.md) pre-registers the multi-agent
  organisation, context limits and measurements.
- [`PV_TEMPLATE.en.md`](PV_TEMPLATE.en.md) defines inter-agent text, decision,
  social relationship and efficiency records.
- [`../logs/history.en.md`](../logs/history.en.md) contains the concise history.

Decision precedence is: repository rules, attempt brief, mode prompt,
orchestrator decision, then independent verifier verdict. Local instructions
cannot weaken security, modify tests or permit access to another solution.

Governance evolves only when a clarification or error yields a useful,
verifiable and reusable rule. It never rewrites a completed run after the fact.
A new verifier is calibrated before freeze; any bias discovered after the first
candidate is documented rather than silently removed.

Public editorial documentation is available in French, UK English, Spanish and
Portuguese. Agent instructions, prompts, frozen challenges, traces and run
deliverables remain canonical and immutable evidence.

The global Git rule applies to the orchestrator after a run. Candidates write
only to `solution/` and neither commit nor push, preventing publication duties
from contaminating the experiment.
