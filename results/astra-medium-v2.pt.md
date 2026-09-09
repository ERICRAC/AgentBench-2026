# V2 Astra médio — resultados Core e Scientific

[Français](astra-medium-v2.md) · [English (UK)](astra-medium-v2.en.md) · [Español](astra-medium-v2.es.md) · **Português**

Ambas as tentativas terminadas e confirmadas independentemente: **15/15 grupos, 71/71 controlos**, na primeira passagem oficial. Total: **1 023.177 s e 978 998 tokens entrada + saída**. Sem interrupções nesta série. Excluem-se manutenção, publicação e tentativas anteriores.

## Veredictos

| Run | Primeira passagem | Veredicto final | Tempo de parede | Tokens |
| --- | ---: | ---: | ---: | ---: |
| Core | 6/6 | 6/6 · 14/14 | 375.169 s | 408 616 |
| Scientific | 9/9 | 9/9 · 57/57 | 648.008 s | 570 382 |
| **Total** | **15/15** | **15/15 · 71/71** | **1 023.177 s** | **978 998** |

[Tests](../docs/acceptance-tests.pt.md) · [Guide](../docs/reading-guide.pt.md)

## Observações sociais

Core: SA-01 retira a preferência por números finitos após respostas cruzadas. MAIN regista 21 decisões iniciais e 11 disposições de revisão. SA-03 apenas motiva esclarecimentos documentais; nenhuma correção funcional.

Scientific: respostas cruzadas corrigem duas propostas iniciais (composição de funções e expressão constante indefinida em todos os pontos). MAIN regista 22 decisões. Após SA-03, 13 pontos: 10 aceites, 2 rejeitados e 1 não verificável no seu dossier. Três grupos de correções: retirar limites de comprimento/recursão, escapar a saída do terminal e gerir falhas de canais CLI. Passam quatro testes candidatos reproduzíveis, separados dos 71 controlos oficiais.

As 131 asserções iniciais continuam controlos candidatos. O programa está no comando registado de MAIN inicial, mas não foi fornecido a SA-03 nem MAIN final: a reserva « não verificável » refere-se ao seu dossier, não à falta de captura do relé. Nenhuma correção após o primeiro veredicto oficial.

## Métricas e limites

| Metric | Core | Scientific | Total |
| --- | ---: | ---: | ---: |
| Input | 395 814 | 548 369 | 944 183 |
| Cache (included) | 302 080 | 409 216 | 711 296 |
| Output | 12 802 | 22 013 | 34 815 |
| Reasoning (included) | 122 | 955 | 1 077 |
| Session time sum | 451.039 s | 730.595 s | 1 181.634 s |

Cinco respostas consultoras somam 3 480 palavras Core e 3 625 Scientific, todas dentro do limite; mensagens visíveis totais: 3 818 e 4 061. Sete threads novos por tentativa; consultores sem ferramentas, um escritor, nenhuma ajuda humana funcional. Astra/medium, contexto 200k, compactação 180k, CLI 0.153.4; runner, prompts e verificadores inalterados. Core publicado em 5c143cd antes de Scientific.

A soma dos tempos-sessão supera o tempo de parede devido às consultas paralelas. Cache incluída na entrada e raciocínio na saída: não somar duas vezes. Contadores e textos por sessão nos PV e JSON.

## Comparação válida

Face a V2 Sol/high, esta série usa menos 57,1 % de tempo e 33,7 % de tokens, com igual veredicto final. Primeira passagem: 15/15 contra 9/15 de Sol, cujo Scientific encontrou uma falha documentada do carregador Python 3.13. Mudam modelo **e** esforço: nenhuma prova causal de superioridade de Astra ou medium.

Core medium usa menos 46,5 % de tempo e 28,6 % de tokens que Core high com igual resultado oficial. Core high completo está reposto. Scientific high chegou a 9/9 antes da interrupção final, mas os custos são incompletos: não se calcula comparação de custos totais high/medium.

Sem V1 Astra/medium não se demonstra dominância V1/V2 com esforço constante. Uma observação por célula não permite generalização estatística. Sol continua a campanha completa do painel (4/6); a série V2 medium termina 2/2.

[Sol V2](sol-v2.pt.md) · [Core high](astra-v2-core.pt.md) · [Scientific high](astra-v2-retired.pt.md)

## Retomar o código

Os módulos contêm 4 docstrings Core e 10 Scientific, com 0 e 1 comentários lexicais: « nenhum comentário » omite parte da documentação. Não mede manutenibilidade. Scientific tem 348 linhas e README 127; decisões e controlos ligados abaixo. Vx de passagem de código continua uma proposta por fixar, não pontuação retroativa.

## Provas

- Core : [PV](../runs/astra-medium-core-v2-001/PV.md) · [trace](../runs/astra-medium-core-v2-001/trace.json) · [metadata](../runs/astra-medium-core-v2-001/run.json) · [DECISIONS](../runs/astra-medium-core-v2-001/solution/DECISIONS.md).
- Scientific : [PV](../runs/astra-medium-scientific-v2-001/PV.md) · [trace](../runs/astra-medium-scientific-v2-001/trace.json) · [metadata](../runs/astra-medium-scientific-v2-001/run.json) · [README](../runs/astra-medium-scientific-v2-001/solution/README.md) · [DECISIONS](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md) · [CONTROLES](../runs/astra-medium-scientific-v2-001/solution/CONTROLES.md) · [controle_final.py](../runs/astra-medium-scientific-v2-001/solution/controle_final.py).
