# Supervised V2.2 — simple pilot interrupted by quota

[Français](v2-2-supervised-core.md) · **English (UK)** · [Español](v2-2-supervised-core.es.md) · [Português](v2-2-supervised-core.pt.md)

**The Astra medium trial really started, then the CLI reported a usage limit.** MAIN created both deliverables but did not finish its session. REV-01 and final MAIN were not started. No retry.

| Measure | Observation |
| --- | --- |
| Attempt | astra-medium-core-v2-2-supervised-001 |
| Sessions | 1 started, 0 completed out of 3 planned |
| Candidate process time | 48.639 s |
| Interrupted trial wall time | 48.641 s |
| Tokens / model request count | Not recorded, not zero |
| Complete V2.2 verdict | None |
| Post-interruption diagnostic | 6/6 groups, 14 checks passed |

Files are archived **without orchestrator corrections**. After closure, the independent verifier confirmed both deliverables, no dynamic execution, four operations, operator/division errors and CLI recovery. [Test checklist](../docs/acceptance-tests.en.md). This is not an official final-phase candidate pass and was not fed back to the candidate.

**Finding:** real transport enabled reading and writing. This trial stopped for quota, not the earlier MCP blocker. It says nothing about pair efficiency: no review, arbitration or token total. Do not compare these 48.641 s with a completed V1/V2 run. Supervised-pilot limits still apply; full isolation is not claimed.

[Minutes and social analysis](../runs/astra-medium-core-v2-2-supervised-001/PV.md) · [Full mandate](../runs/astra-medium-core-v2-2-supervised-001/PROMPT.md) · [Visible events](../runs/astra-medium-core-v2-2-supervised-001/trace.jsonl) · [Metadata](../runs/astra-medium-core-v2-2-supervised-001/run.json) · [Unchanged code](../runs/astra-medium-core-v2-2-supervised-001/solution/calculator.py) · [Frozen protocol](../governance/V2_2_SUPERVISED.en.md).

Raw captures remain private. Public events remove the temporary path and quota-message links/reset time; missing data is not invented. Protected workspace files and frozen hashes verified.

**Next:** if the user confirms available quota and a restart, create a new simple attempt with a new ID and empty solution. Do not resume or reuse this code; Scientific remains unauthorised.

[README](../README.en.md) · [Conclusions](CONCLUSIONS.en.md)
