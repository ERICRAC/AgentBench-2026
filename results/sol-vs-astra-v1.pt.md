# V1 Sol vs Astra — controlo no mesmo perímetro

[Français](sol-vs-astra-v1.md) · [English (UK)](sol-vs-astra-v1.en.md) · [Español](sol-vs-astra-v1.es.md) · **Português**

## Resposta direta

As quatro soluções atingem o veredito oficial final: Core 6/6 e Scientific
9/9. Contudo, nestas duas observações, `gpt-5.6-sol/high` consome **2,40 vezes o
tempo** e **1,33 vezes os tokens** de `gpt-6-astra/high`. Scientific Sol também
precisa de uma correção após um primeiro resultado de 3/9, enquanto Astra
atinge 9/9 logo na primeira passagem oficial.

Isto favorece Astra na eficiência observada, mas não demonstra superioridade
geral: existe apenas uma repetição por célula e a geração é estocástica.

## Perímetro controlado

A campanha `sol-high-control-001` foi pré-registada no commit `a616b2d`.
Especificações, testes, prompts, CLI `0.153.4`, Python `3.13.5`, capturador,
esforço `high`, contexto cliente de 200k, compactação total a 180k, sessões
efémeras novas, sandbox, rede e topologia individual coincidem com
`astra-high-001`. As impressões SHA-256 confirmam as entradas.

O diff da configuração só altera o modelo. A OpenAI documenta o esforço `high`
e a mesma janela máxima para
[gpt-5.6-sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
A infraestrutura do servidor e a variabilidade não podem ser congeladas; o
mesmo perímetro descreve o protocolo cliente observável.

## Resultados

| Desafio | Medida | Astra/high | Sol/high | Diferença Sol |
| --- | --- | ---: | ---: | ---: |
| Core | Primeiro / final / independente | 6/6 · 6/6 · 6/6 | 6/6 · 6/6 · 6/6 | empate |
| Core | Duração | 100,175 s | 189,964 s | +89,6 % |
| Core | Entrada + saída | 120 478 | 158 101 | +31,2 % |
| Scientific | Primeiro / final / independente | 9/9 · 9/9 · 9/9 | 3/9 · 9/9 · 9/9 | Sol corrigido |
| Scientific | Duração | 399,478 s | 1 009,468 s | +152,7 % |
| Scientific | Entrada + saída | 220 510 | 296 275 | +34,4 % |
| **Total** | **Veredito oficial final** | **15/15** | **15/15** | **empate** |
| **Total** | **Duração** | **499,653 s** | **1 199,432 s** | **+140,1 %** |
| **Total** | **Entrada + saída** | **340 988** | **454 376** | **+33,3 %** |

A cache já está incluída na entrada e o raciocínio na saída.

## Qualidade e interpretação

Core atinge o teto oficial com ambos os modelos, sem correção funcional. Em
Scientific, Sol diagnostica e corrige uma interação do carregador Python 3.13
após seis erros de importação. Astra obtém 9/9 primeiro e depois deteta e
corrige uma falha de interpolação com floats extremos através de controlos
suplementares.

A mesma suite de quatro métodos criada por Astra foi executada depois sobre as
duas soluções: Astra 4/4; Sol 0/4 com seis asserções falhadas. É um dado
exploratório, não oficial: não foi pré-registado e uma asserção SVG exige uma
estrutura mais restrita do que o contrato. Os restantes achados sugerem
hipóteses sobre floats extremos, limites de complexidade e expressões inválidas.

Conclusões defensáveis: igualdade oficial final, vantagem observada clara de
Astra em tempo e tokens, autocorreção dos dois modelos em fases diferentes e
nenhuma inferência geral com `n = 1`. Uma campanha futura deverá pré-registar
controlos neutros e repetir cada célula.

[PV Core Sol](../runs/sol-core-v1-001/PV.md) · [PV Scientific Sol](../runs/sol-scientific-v1-001/PV.md) · [Relatório Astra](astra-v1.pt.md)
