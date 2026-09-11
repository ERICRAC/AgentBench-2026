# Conclusões — quando compensa colaborar?

[Français](CONCLUSIONS.md) · [English (UK)](CONCLUSIONS.en.md) · [Español](CONCLUSIONS.es.md) · **Português**

[Cinco runs V2, dois minutos cada](run-summaries/index.pt.md) · [📖 Como ler e interpretar um run AgentBench](../docs/reading-guide.pt.md)

> Nas tarefas estudadas, o custo de coordenação supera o benefício medido. O AgentBench procura as condições em que esta relação se inverte: dificuldade, especialização, paralelismo e custo dos erros.

Isto refere-se às comparações disponíveis com modelo e esforço idênticos e à V2 consultiva atual, não a todas as equipas. Os testes oficiais não medem todas as correções adicionais observadas.

**V1 versus V2, Astra médio: pontuação oficial igual nos dois desafios.** V2 utiliza ×3,56 tempo e ×4,49 tokens no total. A revisão contribui com correções de robustez fora da pontuação. [Balanço completo e provas](astra-medium-v1-v2.pt.md)

## O que mostram as experiências

| Comparação | Tempo V2 / V1 | Tokens V2 / V1 |
| --- | ---: | ---: |
| Sol elevado · calculadora simples | ×4,19 | ×3,54 |
| Sol elevado · calculadora científica | ×1,57 | ×3,09 |
| Astra elevado · calculadora simples | ×7,00 | ×4,75 |
| Astra médio · calculadora simples | ×3,81 | ×4,15 |
| Astra médio · calculadora científica | ×3,44 | ×4,78 |

As cinco comparações atingem o mesmo resultado oficial final: V1 consome menos tempo e tokens. Em Sol diminui o sobrecusto relativo na científica, sem se tornar ganho. Duas dificuldades e uma observação por célula não permitem localizar nem extrapolar o limiar.

[Sol V1/V2](sol-v2.pt.md) · [Astra Core V1/V2](astra-v2-core.pt.md)

V1/V2 designam organizações, não gerações da calculadora. **Calculadora simples** = identificador histórico Core; **calculadora científica** = Scientific. Comparar V1/V2 em cada exercício idêntico e depois comparar essas diferenças. V1 simples contra V2 científica misturaria dificuldade e organização.

Em Astra médio, a razão temporal desce de 3,81 para 3,44 entre simples e científica, mas a de tokens sobe de 4,15 para 4,78. Nenhum limiar observado. A nova V1 científica mantém limites de expressões longas corrigidos após SA-03 (subagente 3, revisor crítico) em V2: contribuição real não valorizada pela pontuação; sondas V1 posteriores e não pré-registadas.

## Organizações — referências e variantes propostas

| Organização | Distribuição | Hipótese |
| --- | --- | --- |
| Solo (V1) | Um candidato faz tudo. | Ambas as calculadoras terminadas. |
| Consultiva (V2 atual) | Um escritor e três consultores. | Conselhos e revisão evitam erros. |
| **V2.1** — Desenvolvimento paralelo | Dois programadores, integrador e revisor; contribuições isoladas e interfaces previamente fixadas. | O trabalho simultâneo compensa comunicação e integração. |
| **V2.2** — Par leve | Um programador e um revisor, uma revisão limitada. | Manter crítica útil com menos coordenação. |

**Nomes acordados: V2** continua a equipa consultiva histórica; **V2.1** é desenvolvimento paralelo; **V2.2** o par leve; **V2.x** a família de variantes futuras, não outra tentativa. V1 continua a referência solo. Comparações futuras em Astra médio, com calculadoras simples e científica. Nomes aprovados; protocolos detalhados e lançamentos pendentes.

**V2.2 — par leve: protocolo preparado, não congelado.** Dois papéis, três sessões, uma revisão. Nenhum candidato lançado; faltam preflight técnico e autorização. [Protocolo V2.2](../governance/V2_2_PROTOCOL.pt.md)

Todas as variantes propostas usam Astra médio. O mesmo modelo não implica contexto, competências reais ou custo total idênticos: registar papéis, informação e orçamentos. O par também muda o tamanho da equipa, não só a topologia.

Variantes separadas da V2 congelada; não reescrever benchmarks existentes. O protocolo atual não autoriza escrita paralela. Pré-registar novo protocolo, permissões por ficheiro ou ramo, interfaces, integração e conflitos antes de lançar.

## Procurar o limiar

V1 Astra médio está completa. Pré-registar variantes e comparar organizações nos dois exercícios idênticos. As calculadoras de ficheiro único oferecem pouco trabalho divisível. Depois ampliar para um desafio modular ou evolução de código com mais interações; fixar novos testes antes das execuções.

Medir separadamente qualidade, prazo até validação, tokens de todos, retrabalho de integração e trocas. Repetir com ordem equilibrada; fixar orçamentos, paragem e tratamento de quotas. Separar esperas impostas da execução. Ficam por decidir repetições e novo desafio.

Podem existir limiares distintos para prazo, tokens e qualidade. Mais rápido mas mais caro é um compromisso. O limiar será um intervalo observado de condições, não um número mágico de linhas. Não o encontrar também é útil.

## Limites e provas

V1 e V2 Astra médio terminadas nas duas calculadoras. Astra médio V2 contra Sol elevado muda modelo e esforço; Scientific Astra elevado tem custos incompletos. Não isolam o efeito organizativo. Os PV mostram correções úteis, mas 71/71 não mede toda a qualidade nem manutenibilidade.

[Astra medium](astra-medium-v2.pt.md) · [Guide](../docs/reading-guide.pt.md) · [README](../README.pt.md) · [Tests](../docs/acceptance-tests.pt.md)
