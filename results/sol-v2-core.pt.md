# V2 Sol — relatório Calculadora Core

[Français](sol-v2-core.md) · [English (UK)](sol-v2-core.en.md) · [Español](sol-v2-core.es.md) · **Português**

## Veredito

`sol-core-v2-001` passa **6/6 grupos `unittest` e 14/14 controlos elementares**
na primeira passagem oficial e na repetição independente. O
[catálogo](../docs/acceptance-tests.pt.md) descreve cada controlo.

A qualidade oficial iguala a V1 Sol, mas a V2 consome 4,19 vezes o tempo e
3,54 vezes os tokens. Segundo Pareto, **V1 domina V2 em Core**: a mesma
conformidade medida com menor custo. Este pequeno desafio não demonstra ganho
multiagente.

| Medida | V1 individual | V2 multiagente | Diferença V2 |
| --- | ---: | ---: | ---: |
| Primeiro / independente | 6/6 grupos · 14/14 controlos | 6/6 · 14/14 | empate |
| Tempo | 189,964 s | 796,534 s | ×4,19 · +319,3 % |
| Entrada + saída | 158 101 | 559 088 | ×3,54 · +253,6 % |
| Correções após verificação | 0 | 0 | empate |

Sete sessões efémeras para quatro papéis somam 898,229 segundos-agente. SA-01
e SA-02 produzem análises cegas e uma contradição cada; SA-03 revê a primeira
solução; apenas MAIN escreve e verifica. Todos os limites são respeitados e são
publicadas 4 347 palavras visíveis, 3 507 dos consultores.

O desacordo útil trata a gramática CLI e converge em três elementos separados
por espaços. MAIN retém 19 de 23 recomendações iniciais. SA-03 formula 3
defeitos, 6 riscos e 6 preferências; MAIN retém 10 de 15 pontos e faz três
alterações antes do verificador. A suite oficial não mede essa robustez extra.

SA-03 também questiona `DECISIONS.md` como terceiro entregável; MAIN conserva-o
porque a V2 exige uma tabela de arbitragem. O verificador aceita-o sem resolver
a ambiguidade textual. Uma única observação não permite generalizar.

[Ata literal filtrada](../runs/sol-core-v2-001/PV.md) · [Trace JSON](../runs/sol-core-v2-001/trace.json) · [Metadados](../runs/sol-core-v2-001/run.json)
