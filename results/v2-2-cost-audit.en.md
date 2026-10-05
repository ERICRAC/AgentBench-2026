# V2.2 cost audit — offline lean draft

[Français](v2-2-cost-audit.md) · **English (UK)** · [Español](v2-2-cost-audit.es.md) · [Português](v2-2-cost-audit.pt.md)

**No candidate launched.** Completed run 002 is unchanged. The prototype reduces transmitted data; it does not demonstrate quality preservation or quota savings.

## Exact measurements

Counts use Unicode characters, not tokens, from normalised public captures. Only the JSON envelope is compared with identical serialisation; new mandate text is excluded.

| Phase | Full historical prompt | Historical data | Proposed data |
| --- | ---: | ---: | ---: |
| MAIN initial | 3,430 | 1,652 | 1,652 |
| REV-01 | 13,927 | 12,084 | 6,886 |
| MAIN final | 16,388 | 14,347 | 9,149 |

Removal: **10,396 characters, 37.0%** of 28,083 cumulative envelope characters. Initial MAIN commands/outputs account for 5,062 JSON characters repeated in each later phase. The remainder removed is the intermediate message and its serialisation. Full contract/files, final handovers and reviewer command evidence remain.

Historical input is 110,511 cumulative tokens, including 65,280 cached tokens; output is 3,263. This is not one prompt's length. Captures cannot precisely attribute all input to system context, tools or handovers. **No token or subscription-quota reduction is estimated.**

## Proposed variant, not frozen

Keep three sessions, two roles and Astra medium. Proposed final word limits: 150 / 300 / 300 instead of 600 / 1,200 / 1,200; this change is not included in measured savings. Archive full evidence but stop injecting initial command logs into subsequent phases.

Trade-off: the reviewer has less evidence for initial tests and must distinguish MAIN claims from observed execution. A shorter review might omit findings; necessary excess must be reported, never silently truncated. This is a new experimental condition, not a historical protocol edit.

## Tested stops and limits

The simulator has no real transport. Ten new tests cover three synthetic replies, live refusal, pre-session size rejection, exact threshold, visible overshoot, missing usage, failure without retry, invalid limits, data preservation and audit arithmetic.

Proposal for approval: **12,000 envelope characters per phase**, whole-payload refusal rather than truncation; stop between sessions at **60,000 observed cumulative tokens**. Neither value is frozen or a subscription limit. Unchanged historical costs would stop after review at 66,038 tokens, overshooting by 6,038 with no final verdict. A between-session gate cannot cap an ongoing session; no watchdog or verified native cap is implemented.

Test limits of 100 tokens/1,000 characters are fixtures, not recommended budgets. All 82 maintenance tests pass; no new calculator score. Next decision: accept the information trade-off and stopping policy. No scientific or reference solo launch without separate approval.

[JSON](v2-2-cost-audit.json) · [Audit / simulation](../scripts/audit_v2_2_cost.py) · [Tests](../tests/test_v2_2_cost.py) · [MAIN initial](../prompts/v2-2-lean-initial-draft.md) · [REV-01](../prompts/v2-2-lean-review-draft.md) · [MAIN final](../prompts/v2-2-lean-final-draft.md) · [Run 002](v2-2-supervised-core-002.en.md)
