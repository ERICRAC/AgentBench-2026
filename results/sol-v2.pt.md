# V2 Sol — síntese Core e Scientific

[Français](sol-v2.md) · [English (UK)](sol-v2.en.md) · [Español](sol-v2.es.md) · **Português**

## Resposta direta

A V2 Sol/high conclui ambos os desafios no máximo oficial: **15/15 grupos
`unittest`, ou 71/71 controlos elementares**. Core passa 6 grupos e 14
controlos à primeira. Scientific passa de 3/9 para 9/9 após uma correção do
carregamento Python 3.13; o verificador independente confirma os 57 controlos.

A conformidade final iguala a V1 Sol. Contudo, a V2 usa **2 384,139 segundos**
e **1 475 626 tokens de entrada + saída**, contra 1 199,432 segundos e 454 376
tokens da V1. Pela regra de Pareto pré-registada, **a V1 domina a V2 nos dois
desafios**: qualidade medida igual com menos tempo e tokens.

[Catálogo dos 71 controlos](../docs/acceptance-tests.pt.md) · [Relatório V2
Core](sol-v2-core.pt.md) · [Comparação V1 Sol/Astra](sol-vs-astra-v1.pt.md)

## Tabela de vereditos

| Célula | Primeira passagem | Veredito final independente | Tempo | Entrada + saída |
| --- | ---: | ---: | ---: | ---: |
| V1 Sol · Core | 6/6 grupos · 14/14 controlos | 6/6 · 14/14 | 189,964 s | 158 101 |
| V2 Sol · Core | 6/6 grupos · 14/14 controlos | 6/6 · 14/14 | 796,534 s | 559 088 |
| V1 Sol · Scientific | 3/9 grupos | 9/9 · 57/57 | 1 009,468 s | 296 275 |
| V2 Sol · Scientific | 3/9 grupos | 9/9 · 57/57 | 1 587,605 s | 916 538 |
| **V1 total** | **9/15 grupos** | **15/15 · 71/71** | **1 199,432 s** | **454 376** |
| **V2 total** | **9/15 grupos** | **15/15 · 71/71** | **2 384,139 s** | **1 475 626** |

A V2 representa ×1,99 o tempo da V1 (+98,8 %) e ×3,25 os seus tokens
(+224,8 %). Apenas em Scientific, as razões são ×1,57 e ×3,09. A cache já
está incluída na entrada e o raciocínio na saída.

## Percurso Scientific

| Fase | Duração | Entrada | Saída | Palavras visíveis |
| --- | ---: | ---: | ---: | ---: |
| SA-01 · análise | 78,281 s | 14 402 | 2 015 | 915 / 1 200 máx. |
| SA-02 · análise | 73,029 s | 14 404 | 1 860 | 1 065 / 1 200 máx. |
| SA-01 · contradição | 41,247 s | 16 295 | 996 | 413 / 600 máx. |
| SA-02 · contradição | 38,271 s | 16 297 | 917 | 466 / 600 máx. |
| MAIN · primeira solução | 810,863 s | 394 075 | 21 975 | 429 |
| SA-03 · crítica | 226,117 s | 26 664 | 6 122 | 666 / 1 200 máx. |
| MAIN · arbitragem final | 431,056 s | 389 108 | 11 408 | 555 |
| **Total** | **1 698,864 s-agente** | **871 245** | **45 293** | **4 509** |

As fases parcialmente paralelas explicam que a soma das sessões exceda o
tempo de parede. Os sete threads são distintos e usam Sol/high, janela
declarada de 200 000 tokens e compactação a 180 000.

## Relação social e correções

SA-01 trata contrato e segurança; SA-02 arquitetura e testabilidade. As
análises cegas e a contradição cruzada tornam visíveis três decisões: limites
de recursos não contratuais, chaves adicionais de variáveis e segurança dos
caminhos. MAIN agrupa 16 recomendações: retém 15 e rejeita uma.

SA-03 apresenta 15 pontos: quatro defeitos, sete riscos e quatro preferências.
MAIN retém 10 e rejeita 5. Antes do verificador, a crítica origina seis
correções: Ctrl-C completo, saída numérica fiel, AST profundo iterativo,
exemplo README, controlos de terminal e taxonomia de `0^-1`.

A primeira passagem oficial falha em seis grupos antes dos testes funcionais.
A causa única é que o `dataclass` do token depende de `sys.modules`, ao
contrário do carregador Python 3.13 do verificador. MAIN substitui-o por uma
classe simples e alcança 9/9. A V1 Sol teve o mesmo percurso 3/9 → 9/9; a V2
não melhorou a convergência oficial.

## Conclusão defensável

A V2 acrescenta rastreabilidade social e correções precoces observáveis, mas
**nenhuma melhoria nos 71 controlos congelados e um sobrecusto claro**. Core
mostra muita redundância; Scientific, um debate mais rico que não evita o
defeito decisivo de carregamento. Uma só observação por célula não permite
generalização estatística. Segue-se o marco de observação V2, antes de decidir
uma hipótese V2.1 distinta.

## Provas auditáveis

- Core: [ata](../runs/sol-core-v2-001/PV.md) · [trace](../runs/sol-core-v2-001/trace.json) · [metadados](../runs/sol-core-v2-001/run.json).
- Scientific: [ata](../runs/sol-scientific-v2-001/PV.md) · [trace](../runs/sol-scientific-v2-001/trace.json) · [metadados](../runs/sol-scientific-v2-001/run.json) · [decisões](../runs/sol-scientific-v2-001/solution/DECISIONS.md).

O protocolo e o runner não mudaram entre desafios. Não são publicados
raciocínio interno bruto, segredos ou horas de trabalho.
