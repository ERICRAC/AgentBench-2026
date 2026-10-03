# V2.2 supervisionada — dupla simples concluída

[Français](v2-2-supervised-core-002.md) · [English (UK)](v2-2-supervised-core-002.en.md) · [Español](v2-2-supervised-core-002.es.md) · **Português**

**V2.2 simples concluída com Astra médio: 3 sessões, 6/6 grupos (14 controlos), 159,977 s e 113 774 tokens.** Sem alterações após revisão. Menor custo que a V2 histórica, mas maior que o agente a solo histórico; comparação exploratória.

A dupla terminou sem interrupção por quota nem nova tentativa automática. MAIN desenvolve, REV-01 revê em modo só de leitura e uma nova sessão MAIN decide e verifica. A tentativa interrompida 001 é preservada; 002 começou do zero.

## Resultados e comparação

| Organização | Tempo (s) | Tokens entrada + saída | Qualidade |
| --- | ---: | ---: | --- |
| V1 a solo histórica | 98.572 | 98 496 | 6/6 grupos, 14 controlos |
| V2 histórica, três consultores | 375.169 | 408 616 | 6/6 grupos, 14 controlos |
| V2.2 supervisionada 002, um revisor | 159.977 | 113 774 | 6/6 grupos, 14 controlos |

**A dupla não apresenta ganho de qualidade medido nesta calculadora simples.** Os ficheiros iniciais e finais são idênticos e ambos passam os controlos independentes. O revisor não encontra defeitos confirmados. Face ao agente a solo histórico: **+62,3 % de tempo, +15,5 % de tokens**. Face à V2 histórica: **−57,4 % de tempo, −72,2 % de tokens**. A organização reduzida diminui o custo observado da equipa, sem superar o agente a solo.

Diferenças exploratórias, não um efeito causal isolado: versões CLI, versão servida do modelo, cache, carga, prompts e instrumentação podem variar. As referências históricas usam a linha Simples, não os totais simples + científica. Uma observação por organização não determina o limiar de rentabilidade da colaboração.

[V1 / V2 Astra medium](astra-medium-v1-v2.pt.md)

## Medições e limites

Entrada: 110 511 tokens; saída: 3 263. Os 65 280 tokens em cache já estão incluídos na entrada e os 165 de raciocínio na saída. Três sessões não equivalem a três pedidos ao modelo. Soma das durações: 159,958 s; tempo total: 159,977 s. Manutenção, publicação e controlos independentes excluídos do custo candidato.

**Esta tentativa terminou.** Saldos inicial e final de quota não medidos: não podemos quantificar a fração de uma janela Plus consumida nem garantir a próxima tentativa. Os 48,641 s e tokens desconhecidos de 001 ficam separados; o custo total da campanha em tokens continua incompleto.

## Provas e análise social

Primeiro verificador oficial: 6/6; confirmação final independente: 6/6; diagnóstico inicial retrospetivo: 6/6, não transmitido ao candidato. Os 14 controlos não são 14 operações aritméticas. Custo direto de revisão: 29,177 s e 14 489 tokens; um acordo explícito, nenhum defeito confirmado e nenhuma correção. O custo total de coordenação não está isolado. A ata identifica as profissões e publica cinco mensagens de resposta, três mandatos completos e decisões, sem raciocínio interno.

[PV — MAIN / REV-01](../runs/astra-medium-core-v2-2-supervised-002/PV.md) · [Prompts](../runs/astra-medium-core-v2-2-supervised-002/prompts.json) · [Trace](../runs/astra-medium-core-v2-2-supervised-002/trace.json) · [JSON](../runs/astra-medium-core-v2-2-supervised-002/run.json) · [Tests](../docs/acceptance-tests.pt.md) · [001](v2-2-supervised-core.pt.md) · [Protocol](../governance/V2_2_SUPERVISED.pt.md)

## Próximo passo

A calculadora científica continua sem autorização. Proposta: decidir se será lançada uma nova tentativa supervisionada com Astra médio, sem repetição automática. Nenhum outro candidato foi lançado.

[README](../README.pt.md) · [Conclusions](CONCLUSIONS.pt.md)
