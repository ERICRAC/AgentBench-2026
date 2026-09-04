# Experimental design and comparability

[Français](EXPERIMENTAL_DESIGN.md) · **English (UK)** · [Español](EXPERIMENTAL_DESIGN.es.md) · [Português](EXPERIMENTAL_DESIGN.pt.md)

This document fixes the AgentBench 2026 campaign structure. It separates
mandatory comparisons from exploratory variants and prevents later refinement
from rewriting already published conditions.

## Main matrix

| Mode | Core Calculator objective | Scientific Calculator objective |
| --- | --- | --- |
| V1 · Codex alone | mandatory | mandatory |
| V2 · governed Codex multi-agent | mandatory | mandatory |
| V3 · Codex + Ollama | mandatory | mandatory |

A cell is one isolated attempt with an identified prompt, recorded
configuration and independent verifier verdict. V1, V2 and V3 are
**organisational modes**, not software releases.

## Observation gate

After each mode:

- publish both results before alteration;
- consolidate observed scores, duration, tokens, corrections, interventions
  and coordination events;
- state findings and limitations before suggesting a change;
- link every refinement to a measurable hypothesis and decision criterion.

Refinement may concern model version, prompt, roles, context or parameters. It
does not necessarily mean training model weights.

## Campaigns and reruns

A campaign is identified by challenge and verifier versions, models,
structural parameters and mode prompts. A substantial change opens a new named
campaign. The V1-to-current cells required for comparison are rerun under the
new conditions. Previous results remain published and are never silently
replaced or merged. Correcting a verifier after its first candidate likewise
creates a new challenge version.

A candidate code correction during one run remains part of that run and does
not open a campaign.

## Cognitive budget and scale

The exact model version, reasoning effort, context window and compaction
threshold are experimental variables rather than environment details. They
are fixed per agent and recorded before a run. Cumulative token use remains
distinct from simultaneously available context.

The two calculators calibrate the protocol and may create a ceiling effect. A
future larger challenge must therefore form a separate campaign, rerun across
all organisations under equal budgets; it will not be added retrospectively
to the current six cells.

## Optional variants

**V2.1** may test a refined organisation after V2 has been published and
analysed, on both difficulty levels. It neither replaces V2 nor counts among
the six main cells.

**V4** is a comparable historical control for Yann Pointud's multi-agent
project named AutoGen, which is independent of Microsoft's namesake framework.
It runs only if the V1–V3 synthesis adds useful evidence and remains outside
the main matrix.

## Final comparison

Independent verifiers own the functional verdict. The synthesis compares at
least compliance, duration, tokens, corrections, human interventions,
disagreements, decisions and coordination cost. An improvement is attributed
to organisation only within the same campaign, or with the configuration
difference explicitly qualified.
