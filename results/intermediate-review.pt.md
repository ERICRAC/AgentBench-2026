# Perícia intermédia — o que mostra AgentBench

[Français](intermediate-review.md) · [English (UK)](intermediate-review.en.md) · [Español](intermediate-review.es.md) · [Português](intermediate-review.pt.md)

[Próximo piloto e ajuda com ligações WSL](../docs/parallel-pilot.pt.md)

## Resposta à pergunta

> Em que condições uma equipa de agentes se torna mais eficiente do que um agente, com modelo e esforço pedidos idênticos, contando qualidade, tempo, tokens e coordenação?

**O projeto demonstra cooperação observável e correções úteis nalguns ensaios. Ainda não demonstra vantagem coletiva líquida e reproduzível.** As calculadoras servem sobretudo para calibrar a experiência; o limiar permanece desconhecido.

V2 consultiva histórica obtém a mesma pontuação oficial que o individual com maior custo. A dupla reduz muito esse custo adicional, mas a última científica usa +18,8 % tokens e +10,1 % tempo sem correções após revisão. A simples reduzida melhora tempo e tokens brutos face ao individual histórico, mas OBS-001 altera o trabalho realizado: não demonstra superioridade.

Esta perícia examina artefactos existentes com duas revisões separadas, metodológica e social, fora dos candidatos. Nenhum benchmark nem nova campanha de modelos iniciado. Custo da perícia não registado nem incluído nos custos candidatos.

## Medições verificadas

| Desafio, Astra médio | Organização | Tempo (s) | Tokens entrada + saída |
| --- | --- | ---: | ---: |
| Simples | Individual V1 | 98,572 | 98 496 |
| Simples | V2 consultiva | 375,169 | 408 616 |
| Simples | Dupla supervisionada | 159,977 | 113 774 |
| Simples | Dupla reduzida, OBS-001 | 65,964 | 87 775 |
| Científica | Individual V1 | 188,560 | 119 388 |
| Científica | V2 consultiva | 648,008 | 570 382 |
| Científica | Dupla reduzida | 207,630 | 141 794 |

Todos passam a suite final: simples 6 grupos / 14 controlos; científica 9 / 57. Linhas não formam uma única campanha controlada. Um ensaio por condição não mede variabilidade.

[Dados e hashes](intermediate-review-data.json) · [V1/V2](astra-medium-v1-v2.pt.md) · [OBS-001](v2-2-lean-001.pt.md) · [Científica 002](v2-2-lean-scientific-002.pt.md).

## A pontuação oculta diferenças de qualidade

Duas sondas conhecidas aplicadas identicamente às três soluções científicas arquivadas, só leitura com Python 3.13.5:

| Sonda | Esperado | Individual V1 | V2 consultiva | Dupla reduzida |
| --- | ---: | --- | --- | --- |
| P1: 1 seguido de 10 000 espaços | 1 | Rejeita: comprimento | 1 | 1 |
| P2: soma de 1 500 uns | 1 500 | Rejeita: complexidade | 1 500 | Rejeita: complexidade |

V2 histórica resolve ambos. A sua trace liga crítica SA-03 às correções de comprimento/profundidade: contributo verificável em casos concretos, não efeito médio da organização.

Sondas posteriores, escolhidas conhecendo defeitos: não são avaliação oculta, nova pontuação oficial, análise exaustiva nem obrigação de recursos ilimitados. Uma rejeição revela limite de utilização; por si só não demonstra incumprimento geral.

Para nova campanha, congelar controlos discriminantes de robustez, integração e manutenção, incluindo casos independentes desconhecidos dos candidatos. Conservar suite atual. Os 71 controlos não são 71 repetições experimentais nem qualidade completa.

## O que demonstram as interações

V2 científica mostra discordâncias, arbitragem e alterações após crítica QA: circulação de informação e influência observáveis. Não demonstra que o mesmo programador com mais tempo ou autorrevisão não corrigisse os defeitos.

Na última dupla, revisor não confirma defeitos, não executa controlos e código fica idêntico. Distingue os 78 controlos anunciados por MAIN das provas recebidas. Boa disciplina de evidência, sem ganho de qualidade observado. Ausência de correções não prova inutilidade universal nem prevenção invisível.

O coletivo também introduz restrições discutíveis: MAIN adotou limite de 10 000 caracteres antes de o remover após SA-03. Contar apenas correções finais ocultaria essa trajetória. [Decisões](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md).

Atas permitem estudar acordos, contradições, adoção e alterações. Conselhos aceites contam decisões, não eficiência. Consenso entre instâncias do mesmo modelo não garante perícia independente; traces não demonstram complacência nem psicologia humana.

Ligar **cláusula → prova → decisão → alteração → controlo antes/depois**. Medir defeitos confirmados, falsos alarmes, regressões, duplicações e pontos não verificáveis. Calibração separada com defeitos injetados conhecidos poderia medir deteção e precisão.

[Ata V2](../runs/astra-medium-scientific-v2-001/PV.md) · [Ata dupla](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).

## Principais vieses

| Prioridade | Problema | Melhoria |
| --- | --- | --- |
| Alta | Um ensaio, ordem e ambiente variáveis | Diferenças descritivas; repetições equilibradas antes de generalizar |
| Alta | Individual já atinge pontuação máxima | Separar conformidade mínima, robustez, integração e manutenção |
| Alta | Individual uma sessão, dupla três novas | Mudam papel social, reinício e cálculo; acrescentar controlo individual segmentado |
| Alta | OBS-001 e novas campanhas | Não atribuir diferença simples apenas à coordenação |
| Média | Aliases e esforços diferentes em algumas séries | Registar metadados expostos; não classificar modelos/esforços isoladamente |
| Média | Testes oficiais V2 após revisão | Distinguir primeiro rascunho retrospetivo da primeira execução oficial |
| Média | Custos excluídos e interrupções incompletas | Delimitar candidatos, ensaios interrompidos e manutenção |

Que organização completa oferece melhor compromisso prático? Que acrescenta o consultor com sessões e orçamento comparáveis? São perguntas diferentes.

## Otimizações recomendadas

Científica atual: MAIN inicial 65 015 tokens, revisor 16 696, MAIN final 60 083. Retoma representa cerca de 42,4 %, incluindo leitura e verificação: não é coordenação pura medida.

Revisão e retoma acrescentam cerca de 47,72 s. Subtraí-las não simula outra organização. Reutilizar thread do programador ou reduzir contexto são hipóteses de nova condição, não alterações históricas.

Na simples, tokens brutos descem de 98 496 para 87 775, mas entrada sem cache + saída sobe de 21 696 para 39 647. Esta medida é diagnóstico, não preço nem quota Plus. Publicar cache, saída, total e tempo separadamente.

Limiar 150 000 verificado entre sessões não limita sessão ativa. Envelope 24 000 caracteres não limita tokens de ferramentas. Em falha, conservar estado dos ficheiros e distinguir contadores completos de protocolo concluído: atualmente qualquer exceção define usage_complete=false.

Agrupar preparação e manter entrada editorial atual. Relatórios e documento de retoma acumulam instruções históricas; painel mistura Sol e Astra. Consomem atenção e favorecem reinícios desnecessários. Melhorar navegação preservando provas.

## Estratégia para procurar o limiar

**Afinar proposta de quatro papéis: começar por variante paralela leve.** Dois programadores possuem componentes isolados; um integra depois numa sessão distinta. Três sessões, duas profissões e verificação independente. Registar integração; acrescentar revisor dedicado mais tarde se justificado. Nova subcondição proposta, não redefinição retroativa de V2.1.

Preparar num lote desafio modular e controlo V1 contemporâneo, interfaces e requisitos idênticos. O individual pode usar igual decomposição. Incluir testes de integração: peças totalmente independentes favorecem equipa sem medir interação; dependência total retira paralelismo.

Medir caminho crítico: preparação, máximo dos trabalhos paralelos, integração e validação. Registar inícios/finais relativos, sobreposição, tempo total e acumulado, tokens por agente e retrabalho. Menor demora com mais tokens é compromisso.

Para explicar dupla atual, controlo mais específico é individual em três sessões com autorrevisão. Para explorar velocidade colaborativa, próximo recomendado é piloto paralelo leve. São complementares; não iniciar todas as variantes juntas.

Piloto verifica viabilidade, não reprodutibilidade. Fixar objetivo principal — tempo, tokens ou qualidade —, paragens e orçamento global. Repetir condições promissoras em ordem equilibrada. Limiar será região de tarefas e restrições, não número universal de linhas.

## Perguntas e perícia de marco

- Prioridade: demora, economia de tokens ou defeitos caros?
- Integração e dificuldade distinguem organizações?
- Crítica de outro agente supera autorrevisão com recursos comparáveis?
- Vantagem mantém-se em repetições e contando interrupções?

Estas perguntas orientam decisões técnicas sem confirmações humanas repetidas. Nova campanha exige âmbito e orçamento definidos.

Ambas as revisões foram incorporadas: método pede controlar sessões e separar cache; revisão social pede contar restrições introduzidas e iniciar dois programadores, um integrando. Diferem na ordem experimental: explicar dupla com individual segmentado ou explorar paralelismo. Aqui prioriza-se paralelismo leve; controlo segmentado continua necessário para isolar efeito do consultor. Nenhum revisor é candidato.

**Lembrete pedido: perícia do protocolo acordado pelo modelo mais capaz disponível antes dos novos ensaios, e dos resultados no marco.** Este relatório usa sessão atual e duas revisões; não certifica classificação dos modelos disponíveis. Custos dos revisores da perícia não expostos.

## Verificação e provas

Custos recalculados de sete metadados com hashes; seis execuções comuns em três soluções; nenhum candidato nem ficheiro de run alterado. Diagnóstico apenas escreve em saída padrão e desativa bytecode ao iniciar.

```bash
python3 -B scripts/audit_intermediate.py
```

[Script](../scripts/audit_intermediate.py) · [Dados](intermediate-review-data.json) · [Conclusão central](CONCLUSIONS.pt.md) · [Controlos](../docs/acceptance-tests.pt.md).
