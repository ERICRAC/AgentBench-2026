# Sol V2 — Core Calculator report

[Français](sol-v2-core.md) · **English (UK)** · [Español](sol-v2-core.es.md) · [Português](sol-v2-core.pt.md)

## Verdict

`sol-core-v2-001` passes **6/6 `unittest` groups and 14/14 elementary checks**
on both its first official pass and independent replay. The
[catalogue](../docs/acceptance-tests.en.md) names every check.

Official quality equals the Sol V1 reference, while V2 uses 4.19× wall time
and 3.54× tokens. Under the preregistered Pareto rule, **V1 dominates V2 on
Core**: equal measured conformity at lower cost. This small challenge shows no
multi-agent gain.

| Measure | Solo V1 | Multi-agent V2 | V2 difference |
| --- | ---: | ---: | ---: |
| First / independent | 6/6 groups · 14/14 checks | 6/6 · 14/14 | tie |
| Wall time | 189.964 s | 796.534 s | ×4.19 · +319.3% |
| Input + output | 158,101 | 559,088 | ×3.54 · +253.6% |
| Post-verifier fixes | 0 | 0 | tie |

Seven ephemeral sessions across four roles total 898.229 agent-seconds. SA-01
and SA-02 produced blind analyses and one cross-response each; SA-03 reviewed
the first solution; MAIN alone wrote and verified it. All response limits were
met. Visible output totals 4,347 words, including 3,507 consultant words.

The first analysts mostly agree. Their useful disagreement concerns CLI
grammar and converges on exactly three whitespace-separated fields. MAIN
retains 19 of 23 initial recommendations. SA-03 raises three defects, six risks
and six preferences; MAIN retains 10 of 15 points and makes three pre-verifier
changes. The official suite does not quantify those additions.

SA-03 also flags `DECISIONS.md` as a third deliverable; MAIN retains it because
V2 requires an arbitration table. The verifier accepts it but does not resolve
the textual ambiguity. With one observation per mode, this supports no gain in
this cell, not a general conclusion about multi-agent systems.

[Screened verbatim minutes](../runs/sol-core-v2-001/PV.md) · [JSON trace](../runs/sol-core-v2-001/trace.json) · [Metadata](../runs/sol-core-v2-001/run.json)
