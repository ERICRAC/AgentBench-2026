# Detailed result — `codex-single-001`

[Français](codex-single-001.md) · **English (UK)** · [Español](codex-single-001.es.md) · [Português](codex-single-001.pt.md)

## Executive summary

One Codex agent handled the complete Core Calculator objective: contract
analysis, design, implementation, documentation and validation. No sub-agent or
external dependency was used. The first known verifier pass succeeded on all
six checks, with no recorded functional correction cycle.

This establishes the V1 compliance baseline. It is insufficient on its own to
judge efficiency because duration, reasoning level and detailed iterations
were not captured during the run.

## Run identity

| Field | Value |
| --- | --- |
| Identifier | `codex-single-001` |
| Objective | Core Calculator |
| Mode | Codex alone |
| Architecture | One general-purpose agent, no sub-agent |
| Observed model | `gpt-5.6-sol` |
| Authentication | ChatGPT Plus, no OpenAI API key |
| Prompt | [`prompts/codex-single.md`](../prompts/codex-single.md) |
| Creation and verification | 2 September 2026 — time not published |
| Observed consumption | Approximately 18,086 tokens |
| Total duration | Not recorded |
| Reasoning level | Not recorded |
| Environment | Codex CLI 0.152.1, Python 3.13.5, WSL2 x86_64 |

## Governance and implementation

[`AGENTS.md`](../AGENTS.md), the frozen
[`CHALLENGE.md`](../runs/codex-single-001/CHALLENGE.md), the exact prompt and the
independent verifier separated responsibilities. The single agent acted as
analyst, designer, developer, writer and checker.

The implementation separates `calculate(left, operator, right)`,
`parse_expression(expression)` and `main()`. Four explicit operator branches
avoid dynamic execution. Division by zero raises `ZeroDivisionError`; an
unknown operator raises `ValueError`. The CLI parses three space-separated
elements, accepts integers, decimals and negative values, recovers without a
traceback and exits cleanly on `quit`, `exit`, end-of-file or interruption.

## Independent validation

```bash
python3 scripts/verify.py --solution runs/codex-single-001/solution
```

| Check | Result |
| --- | --- |
| Required files | Passed |
| Four operations and numeric variants | Passed |
| Invalid operator | Passed |
| Division by zero | Passed |
| No `eval()` or `exec()` in the AST | Passed |
| Recoverable CLI session | Passed |

First known pass: **6/6**. Final independently rechecked result: **6/6**.

## Observed indicators

| Indicator | Value |
| --- | --- |
| Agents / sub-agents | 1 / 0 |
| Delivered files | 2 |
| `calculator.py` / solution README | 79 / 42 lines |
| External runtime dependencies | 0 |
| Corrections after first known pass | 0 |
| Tokens | Approximately 18,086 |

## Incidents, quality and limits

No human implementation intervention is recorded. Post-run metadata, SSH and
publication work are preservation activities, not candidate assistance. There
is no raw log from which to verify the exact number of calls or earlier errors.

The result is readable, small, robust for covered errors and free of
coordination noise. Limits remain: only six targeted checks, spaces required
around the CLI operator, unrecorded duration and reasoning level, approximate
token consumption, and no proof that a solo organisation is generally
superior.

## Comparison conclusion

V1 provides a short, documented and fully conforming solution with no
coordination cost. V2 must deliver an observable benefit beyond the same final
score to justify additional time, tokens and exchanges.
