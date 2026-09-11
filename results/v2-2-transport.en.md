# V2.2 — transport, isolation and model comparison

[Français](v2-2-transport.md) · **English (UK)** · [Español](v2-2-transport.es.md) · [Português](v2-2-transport.pt.md)

## Summary

**Pilot choices approved; launch remains locked.** One attempt per calculator, no new aggregate cap, stop on quota, no automatic retry. Astra medium remains active. Neither 18 repetitions nor a model probe is authorised.

Real subprocess transport and local isolation were tested. **Authenticated model integration remains unqualified; no protocol freeze.** No preflight model calls or new calculator scores.

## Evidence and checklist

- [x] 46 maintenance tests: 38 existing plus 8 transport tests.
- [x] Bubblewrap: **30/30 checks**, with disposable canaries.
- [x] Two relay simulations, each using three genuinely isolated Python processes: MAIN initial, REV-01, MAIN final. Synthetic replies, no model usage or technical verdict.
- [x] Native Codex countercheck: **26/30**; four deviations retained.
- [ ] Qualify authenticated transport and all candidate tool surfaces.
- [ ] Freeze, then request separate simple-calculator launch approval.

[Raw observations and hashes](v2-2-transport.json) · [Updated static preflight](v2-2-preflight-approved.json) · [Previous stage](v2-2-preflight.en.md)

Fourteen checks per role: read contract/solution; create, overwrite, rename and delete solution files (MAIN allowed, reviewer denied); deny outside read/write directly and through symlinks, contract write and connection to the host loopback server; preserve host contract/canary. Two host controls establish that canary access and loopback connection work before isolation.

Only disposable fixtures are created and removed; no real secrets are inspected, no Internet probe. Bubblewrap exposes read-only runtime directories and workspace, writable solution only for MAIN, read-only synthetic root, separate network and cleared environment.

**Native deviation:** host reads are denied and host files remain intact, but the corresponding path can be created in the sandbox’s synthetic layer, directly and through its symlink: two deviations per role. This is not demonstrated disclosure of the host file, but violates our strict no-writes-outside-solution rule. An earlier /tmp fixture also lost required read access when its parent was denied; the retained probe uses the home-backed location of actual runs.

Bubblewrap does not wrap the authenticated CLI: credentials and model network are absent. Passing local probes does not establish isolation of every Codex tool. No permissive fallback is enabled.

## Transport

[Implementation](../scripts/v2_2_transport.py): exclusive private stdin/stdout/stderr files, no shell, application truncation or retry; checkpoints for spawn failure, non-zero exit and probe timeout. Process groups are stopped after execution/interruption; parent SIGKILL or power loss can prevent finalisation. The 30-second probe timeout is not a candidate budget.

[Eight tests](../tests/test_v2_2_transport.py): exact streams/private permissions; exit 7 with partial evidence; timeout/termination; 2 MB output; capture reuse rejected; executable missing; prepared command without legacy sandbox_mode; invalid role/solution link rejected.

OpenAI Docs informed the separation of permission profiles and sandbox_mode. Installed CLI syntax takes precedence: codex sandbox, without linux subcommand. [Permissions documentation](https://learn.chatgpt.com/docs/permissions). The native command builder remains experimental, disconnected from live launch.

## Keep model, effort and organisation separate

Completed totals across both calculators; input plus output tokens, cache already included. Identical final score: 15 groups / 71 checks.

| Organisation | Model / effort | Total wall time (s) | Tokens |
| --- | --- | ---: | ---: |
| V1 | Sol high | 1199.432 | 454376 |
| V1 | Astra high | 499.653 | 340988 |
| V1 | Astra medium | 287.132 | 217884 |
| V2 | Sol high | 2384.139 | 1475626 |
| V2 | Astra medium | 1023.177 | 978998 |

[Sol/Astra V1](sol-vs-astra-v1.en.md) · [Sol V2](sol-v2.en.md) · [Astra medium](astra-medium-v1-v2.en.md) · [Interrupted Astra high V2](astra-v2-retired.en.md)

V1 Astra high used **56.5% more tokens** and **74.0% more time** than medium. One observation with different correction work is not causal proof. Scientific V2 high was interrupted: no comparable complete total; missing usage is not zero.

Rapid quota exhaustion is retained as a user observation. Token counters do not measure Plus quota charging; per-run before/after quota readings are unavailable. Neither medium fitting nor high being universally impossible is established.

Keep Sol high and Astra high references. To compare organisations, hold model/effort fixed; to compare models, hold organisation/effort fixed. Astra medium versus Sol high changes two factors. Future Sol-high V2.2 needs separate authorisation.

## Reproduction and next step

```bash
python3 -B -m unittest discover -s tests -v
python3 -B scripts/preflight_v2_2_isolation.py --backend bwrap
python3 -B scripts/preflight_v2_2_isolation.py --backend native
```

The native command currently must fail: it is a countercheck. OS probes required authorised execution outside the nested sandbox, not weakened candidate protections.

Next: connect orchestrator-side authentication to confined candidate tools, then qualify a model probe only with permission. No additional package currently needed; bubblewrap 0.12.0 is installed. Historical evidence, challenges and tests are unchanged.

[Protocol](../governance/V2_2_PROTOCOL.en.md) · [Conclusions](CONCLUSIONS.en.md) · [README](../README.en.md)
