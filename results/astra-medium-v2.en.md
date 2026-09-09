# Astra medium V2 — exploratory series

[Français](astra-medium-v2.md) · **English (UK)** · [Español](astra-medium-v2.es.md) · [Português](astra-medium-v2.pt.md)

Core complete: 6/6 groups and 14/14 checks on the first pass, independently confirmed. Scientific is still to launch.

`astra-medium-001` · `gpt-6-astra` · `medium` (MAIN, SA-01, SA-02, SA-03).

- Core : `astra-medium-core-v2-001`.
- Scientific : `astra-medium-scientific-v2-001`.

| Core | Value |
| --- | ---: |
| Wall time | 375.169 s |
| Session time sum | 451.039 s |
| Input | 395 814 |
| Cached input (included) | 302 080 |
| Output | 12 802 |
| Reasoning (included) | 122 |
| Input + output | **408 616** |

SA-01 revises its finite-only preference after cross-replies. MAIN records 21 initial decisions; SA-03 only prompts numerical README clarifications, without functional fixes. Consultant replies total 3 480 words, all within limits; 3 818 visible words overall. Seven distinct threads; consultants used no tools. Code: 50 lines, README: 83, decisions: 148.

Core medium uses 46.5% less time and 28.6% fewer tokens than Core high (700.994 s, 572 168 tokens), at equal official outcome. One observation: not general evidence that lower effort is better. Interrupted Scientific high costs remain incomplete.

[Core PV](../runs/astra-medium-core-v2-001/PV.md) · [Trace](../runs/astra-medium-core-v2-001/trace.json) · [Metadata](../runs/astra-medium-core-v2-001/run.json) · [Decisions](../runs/astra-medium-core-v2-001/solution/DECISIONS.md) · [Core high](astra-v2-core.en.md)

No Astra/medium V1: no causal V1/V2 comparison at constant effort. Sol/high remains the complete dashboard campaign (4/6). No extra V1 without a request.

[Guide](../docs/reading-guide.en.md) · [Astra/high](astra-v2-retired.en.md) · [Sol V2](sol-v2.en.md)
