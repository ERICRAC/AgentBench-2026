# AgentBench 2026

[Français](README.md) · **English (UK)** · [Español](README.es.md) · [Português](README.pt.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-social-agents.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-social-agents-light.png">
  <img alt="AgentBench 2026 — one agent facing a network of agents" src="assets/agentbench-social-agents-light.png">
</picture>

> An open R&D laboratory for the social behaviour of AI agents: when several
> agents collaborate, do they create more intelligence — or merely more noise?

![Campaign](https://img.shields.io/badge/campaign-4%2F6_validations-22c55e)
![Progress](https://img.shields.io/badge/progress-67%25-06b6d4)
![Next step](https://img.shields.io/badge/next-V2_observation_gate-8b5cf6)
![Licence](https://img.shields.io/badge/licence-MIT-f97316)

AgentBench 2026 compares three agent organisations across two related
challenges. It measures the outcome as well as elapsed time, tokens,
corrections, human interventions and coordination noise.

The project was conceived and steered **entirely through a microphone with
Codex** by [Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/).
The human–agent conversation is therefore part of the experiment, just as much
as the software it produces.

Active campaign: **Sol high · `sol-high-control-001`**. [71-check catalogue](docs/acceptance-tests.en.md) · [Sol V1 control](results/sol-vs-astra-v1.en.md) · [V2 synthesis](results/sol-v2.en.md) · [V1 archive](results/ARCHIVE_V1.en.md).

[Node.js / WSL / Markdown](docs/node-wsl.en.md) · [V2 preflight](results/astra-v2-preflight.en.md).

## Dashboard — current state

| Main campaign | V1 · Codex alone | Next run | Protocols |
| :---: | :---: | :---: | :---: |
| **4 / 6 validated** | **2 / 2 replicated** | **V2 observation gate** | **Challenges and V2 protocol frozen** |
| `████████░░░░` **67%** | Core **6 groups · 14 checks** · Scientific **9 groups · 57 checks** | Compare gain and noise | Independent verifiers |

```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#0f2a4a",
  "primaryTextColor": "#f8fafc",
  "primaryBorderColor": "#22d3ee",
  "secondaryColor": "#3b1d67",
  "tertiaryColor": "#431f2b",
  "fontFamily": "system-ui",
  "lineColor": "#8b5cf6",
  "clusterBkg": "#0b1220",
  "clusterBorder": "#475569"
}}}%%
flowchart LR
    subgraph V1["V1 · Codex alone · 2/2"]
      V1C["✓ Core Calculator<br/>6 groups · 14 checks"]
      V1S["✓ Scientific Calculator<br/>9 groups · 57 checks"]
    end
    G1{"V1 observations<br/>solo baseline"}
    subgraph V2["V2 · Codex team · 2/2"]
      V2C["✓ Core Calculator<br/>6 groups · 14 checks"]
      V2S["✓ Scientific Calculator<br/>9 groups · 57 checks"]
    end
    G2{"V2 observations<br/>possible refinement"}
    V21["V2.1 · optimised variant<br/>optional"]
    subgraph V3["V3 · Codex + Ollama · 0/2"]
      V3C["○ Core Calculator<br/>pending"]
      V3S["○ Scientific Calculator<br/>pending"]
    end
    G3{"V3 observations<br/>final comparison"}
    V4["V4 · AutoGen control<br/>optional"]

    V1C & V1S --> G1
    G1 --> V2C & V2S
    V2C & V2S --> G2
    G2 -. "if gain is testable" .-> V21
    G2 --> V3C & V3S
    V3C & V3S --> G3
    G3 -. "historical control" .-> V4

    classDef done fill:#14532d,stroke:#4ade80,color:#f0fdf4,stroke-width:3px;
    classDef next fill:#4c1d95,stroke:#c084fc,color:#faf5ff,stroke-width:3px;
    classDef todo fill:#172554,stroke:#38bdf8,color:#f0f9ff,stroke-width:2px;
    classDef gate fill:#7c2d12,stroke:#fb923c,color:#fff7ed,stroke-width:2px;
    classDef optional fill:#0f2a4a,stroke:#94a3b8,color:#f8fafc;
    class V1C,V1S,V2C,V2S done;
    class V3C,V3S todo;
    class G1,G3 gate;
    class G2 next;
    class V21,V4 optional;
```

**How to read it:** the six V1–V3 × Core Calculator–Scientific Calculator cells
form the mandatory campaign. V2.1 and V4 are not included in the 4/6 count: they are explicitly
optional extensions.

## The research question

> Does a team of agents produce a better result than one capable agent once
> time, token use, coordination noise and added complexity are taken into
> account?

Every organisation tackling the same challenge receives the same
specification, constraints, independent tests and clean working directory. It
may neither inspect nor reuse another attempt's solution. **Agents propose;
the independent verifier decides.**

The score is therefore only part of the picture:

```math
\text{experimental value}
=
\frac{\text{delivered quality}}
{\text{time} + \text{tokens} + \text{coordination}}
```

This expression illustrates the project's intuition; it is not a computed score adding incompatible units. Reports compare quality, seconds, tokens and coordination separately.

## What is actually tested

The `6/6` and `9/9` verdicts count **`unittest` groups**, not every assertion.
On a passing run, the 15 groups execute **71 elementary checks: 14 Core and 57
Scientific**.

### Core Calculator — 6 groups / 14 checks

- [x] C01 · Required files — 2 checks.
- [x] C02 · No dynamic execution — 1 check.
- [x] C03 · Addition, subtraction, multiplication and division — 4 checks.
- [x] C04 · Unknown operator — 1 check.
- [x] C05 · Division by zero — 1 check.
- [x] C06 · Recovering CLI with no traceback — 5 checks.

### Scientific Calculator — 9 groups / 57 checks

- [x] S01 · Deliverables and documentation — 7 checks.
- [x] S02 · Safety and standard library — 2 checks.
- [x] S03 · Precedence, parentheses, powers and signs — 10 checks.
- [x] S04 · Functions, constants and scientific notation — 6 checks.
- [x] S05 · Variable `x` and forbidden names — 5 checks.
- [x] S06 · Syntax, domains and division by zero — 6 checks.
- [x] S07 · Sampling, bounds and discontinuities — 8 checks.
- [x] S08 · Valid, passive SVG with a curve — 7 checks.
- [x] S09 · CLI, plot, history and recovery — 6 checks.

**Audit path:** [all 71 checks](docs/acceptance-tests.en.md) →
[source specifications and tests](challenges/) → [results](results/README.en.md)
→ each run's minutes and trace. This coverage is not an absolute quality score.

## Published results

| Run | Organisation | Challenge | Verdict | Time | Observed tokens |
| --- | --- | --- | ---: | ---: | ---: |
| [`astra-core-v1-002`](results/astra-v1.en.md) | V1 · Astra baseline | Core Calculator | **6/6 groups · 14/14 checks** | 100.175 s | 120 478¹ |
| [`astra-scientific-v1-002`](results/astra-v1.en.md) | V1 · Astra baseline | Scientific Calculator | **9/9 groups · 57/57 checks** | 399.478 s | 220 510¹ |
| [`sol-core-v1-001`](results/sol-vs-astra-v1.en.md) | V1 · Sol control | Core Calculator | **6/6 groups · 14/14 checks** | 189.964 s | 158 101¹ |
| [`sol-scientific-v1-001`](results/sol-vs-astra-v1.en.md) | V1 · Sol control | Scientific Calculator | **9/9 groups · 57/57 checks** | 1,009.468 s | 296 275¹ |
| [`sol-core-v2-001`](results/sol-v2-core.en.md) | V2 · Sol team | Core Calculator | **6/6 groups · 14/14 checks** | 796.534 s | 559 088¹ |
| [`sol-scientific-v2-001`](results/sol-v2.en.md) | V2 · Sol team | Scientific Calculator | **9/9 groups · 57/57 checks** | 1,587.605 s | 916 538¹ |

¹ Cumulative input + output; detailed reports separate cache, reasoning and
corrections. Missing data is never reconstructed after the event.

## V1, V2, V3… and the case for V2.1 or V4

- **V1 — solo baseline:** the experimental orchestrator commissions a separate
  Codex candidate session; that candidate works alone, with no consultant or
  delegation. Both difficulty levels are complete.
- **V2 — Codex society:** an orchestrator and specialists with bounded
  assignments, with only one writer. It measures the benefit and cost of
  coordination.
- **V2.1 — optional optimisation:** considered only after full V2 analysis. It
  may test a refined organisation without replacing or polishing V2.
- **V3 — local hybrid:** Codex orchestrates, decides and writes; local Ollama
  models analyse or critique within limited context.
- **V4 — optional historical control:** a comparable reproduction of Yann
  Pointud's multi-agent project, named AutoGen but independent of Microsoft's
  namesake framework, after the main matrix.

“Refinement” may concern model version, prompt, roles, context or parameters;
it does not necessarily mean training model weights. Observations are recorded
at every gate before any decision. A substantial change opens a **new
campaign**, and the V1-to-current cells needed for comparison are rerun under
the same configuration. Earlier results remain published.

The comparison and versioning rules are defined in
[`governance/EXPERIMENTAL_DESIGN.en.md`](governance/EXPERIMENTAL_DESIGN.en.md).

## Experimental TODO

- [x] Freeze the **Calculator Core** and **Scientific Calculator** challenges and verifiers.
- [x] Preserve the first `001` V1 observations without rewriting them.
- [x] Replicate V1 with pinned model, effort and context: Core `astra-core-v1-002` **6/6**, Scientific `astra-scientific-v1-002` **9/9**.
- [x] Control V1 like for like with Sol/high: **15/15 groups and 71/71 elementary checks**, with [comparison published](results/sol-vs-astra-v1.en.md).
- [x] Decide and freeze V2 roles, exchanges, budgets and [metrics](governance/V2_PROTOCOL.en.md).
- [x] Validate the V2 preflight: isolation, per-role configuration, visible traces and counters. [PV](results/astra-v2-preflight.en.md).
- [x] Run and publish **V2 Core Calculator**: **6/6 groups and 14/14 checks**, with [report and minutes](results/sol-v2-core.en.md).
- [x] Run and publish **V2 Scientific Calculator** without changing the protocol: **9/9 groups and 57/57 checks**, with [V2 synthesis](results/sol-v2.en.md).
- [ ] Hold the V2 observation gate; decide against written criteria whether V2.1 adds a testable hypothesis.
- [ ] If activated, run V2.1 separately on both difficulty levels.
- [ ] Freeze V3's Ollama integration, local models and context limits.
- [ ] Run and publish **V3 Core Calculator**, then **V3 Scientific Calculator**.
- [ ] Compare the six main runs: quality, cost, corrections, interventions and social noise.
- [ ] Decide after the synthesis whether the historical V4 control is worthwhile.
- [ ] After any substantial refinement, open a new campaign and rerun comparable V1…Vn baselines.

## Two difficulty levels

**Calculator Core** is short and repeatable. **Scientific Calculator** raises
the bar with safe expression parsing without `eval()`, scientific functions
and constants, an `x` variable, domain handling, sampling and dependency-free
SVG plots.

<details>
<summary><strong>What is measured</strong></summary>

- functional compliance and robustness;
- code readability and documentation quality;
- elapsed time, tokens, calls and corrections;
- human interventions;
- disagreement, decisions and coordination noise;
- visible inter-agent text and influence by profession, recorded in
  [experimental minutes](governance/PV_TEMPLATE.en.md);
- agents' ability to detect their own errors;
- delivered quality relative to organisational complexity.

</details>

<details>
<summary><strong>Reproduce a V1 baseline</strong></summary>

Requirements: Linux, Python 3.10 or later, Git and Codex CLI connected through
a ChatGPT subscription. No OpenAI API key is required.

```bash
python3 scripts/new_run.py my-v1-run
cd runs/my-v1-run
python3 ../../scripts/capture_session.py --cwd solution --prompt ../../prompts/codex-single.md --config ../../governance/astra-v1.toml
cd ../..
python3 scripts/verify.py --solution runs/my-v1-run/solution
```

Every attempt uses a unique identifier and a clean directory. Select the
scientific challenge with `--challenge scientific-calculator`.

</details>

<details>
<summary><strong>Governance, transparency and repository layout</strong></summary>

The [`governance/`](governance/README.en.md) package defines instruction hierarchy,
experimental design, reporting and public logging. The [public history](logs/history.en.md)
records decisions without work times, secrets or raw personal transcripts.
Failures remain visible alongside successes.

```text
challenges/   specifications and independent tests
prompts/      exact prompts given to candidates
runs/         clean workspaces and produced solutions
results/      detailed results and future comparisons
governance/   conduct and reporting rules
logs/         concise public history
scripts/      run creation and verification
```

A [SSH note for VS Code and WSL](docs/ssh-vscode.en.md) explains how to use
a dedicated key through `ssh-agent` without storing its passphrase in the
repository.

</details>

## About the author

[Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/) is an
information systems architect and IT leader with more than thirty years of
experience spanning software development, industry, infrastructure, cloud,
cybersecurity, project leadership and organisational change.

AgentBench 2026 is his first substantial public proof of concept built with
Codex operating as an AI agent and a CI/CD-style Git workflow: versioned
specifications, isolated runs, independent tests, reports, history and
continuous publication.

[LinkedIn profile](https://www.linkedin.com/in/eric-racineux-75475a7/)
· [Online CV](https://ericrac.github.io/CV-Eric-RACINEUX/)

## Licence

MIT. Yann Pointud's AutoGen remains an independent project owned by its author;
it is neither included nor forked here and does not use Microsoft's namesake
framework.

## Bonus — AgentBench in 3D

This small octahedral crystal represents the six main experiments around one
decision centre. Its preview automatically follows the visitor's theme.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-crystal-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-crystal-light.png">
  <img alt="AgentBench octahedral crystal as a 3D render" src="assets/agentbench-crystal-light.png">
</picture>

<details>
<summary><strong>Manipulate the interactive STL model</strong></summary>

GitHub controls the interactive viewer background, so it does not follow the
README theme. The model remains [available to download as STL](assets/agentbench-crystal.stl).

```stl
solid agentbench_crystal
  facet normal 0.577350 0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 10 0 0
      vertex 0 10 0
    endloop
  endfacet
  facet normal -0.577350 0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 0 10 0
      vertex -10 0 0
    endloop
  endfacet
  facet normal -0.577350 -0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex -10 0 0
      vertex 0 -10 0
    endloop
  endfacet
  facet normal 0.577350 -0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 0 -10 0
      vertex 10 0 0
    endloop
  endfacet
  facet normal 0.577350 0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 0 10 0
      vertex 10 0 0
    endloop
  endfacet
  facet normal -0.577350 0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex -10 0 0
      vertex 0 10 0
    endloop
  endfacet
  facet normal -0.577350 -0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 0 -10 0
      vertex -10 0 0
    endloop
  endfacet
  facet normal 0.577350 -0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 10 0 0
      vertex 0 -10 0
    endloop
  endfacet
endsolid agentbench_crystal
```

</details>
