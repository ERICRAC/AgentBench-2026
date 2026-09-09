# V2 Astra medium — série exploratória

[Français](astra-medium-v2.md) · [English (UK)](astra-medium-v2.en.md) · [Español](astra-medium-v2.es.md) · **Português**

Core terminado: 6/6 grupos e 14/14 controlos na primeira passagem, confirmados independentemente. Scientific aguarda lançamento.

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

SA-01 revê a preferência por números finitos após respostas cruzadas. MAIN regista 21 decisões iniciais; SA-03 apenas motiva esclarecimentos numéricos no README, sem correções funcionais. 3 480 palavras de consultores, todas dentro do limite; 3 818 palavras visíveis totais. Sete threads distintos, consultores sem ferramentas. Código: 50 linhas; README: 83; decisões: 148.

Core medium consome menos 46,5 % de tempo e 28,6 % de tokens que Core high (700.994 s, 572 168 tokens), com igual resultado oficial. Uma observação não demonstra que menor esforço seja melhor. Os custos de Scientific high interrompido continuam incompletos.

[Core PV](../runs/astra-medium-core-v2-001/PV.md) · [Trace](../runs/astra-medium-core-v2-001/trace.json) · [Metadata](../runs/astra-medium-core-v2-001/run.json) · [Decisions](../runs/astra-medium-core-v2-001/solution/DECISIONS.md) · [Core high](astra-v2-core.pt.md)

Não existe V1 Astra/medium: nenhuma comparação causal V1/V2 com esforço constante. Sol/high continua a campanha completa do painel (4/6). Nenhuma V1 adicional sem pedido.

[Guide](../docs/reading-guide.pt.md) · [Astra/high](astra-v2-retired.pt.md) · [Sol V2](sol-v2.pt.md)
