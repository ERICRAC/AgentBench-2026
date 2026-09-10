# V1 Astra médio — calculadora simples

[Français](astra-medium-v1-core.md) · [English (UK)](astra-medium-v1-core.en.md) · [Español](astra-medium-v1-core.es.md) · **Português**

astra-medium-core-v1-001 terminada: **6/6 grupos, 14/14 controlos**, à primeira passagem e confirmados independentemente. **98,572 s e 98 496 tokens entrada + saída.** Nenhum candidato científico lançado.

## O run em dois minutos

Um candidato programador em sessão nova Astra médio, sem consultores nem subagentes. Orquestrador externo lança, captura e publica sem resolver.

Lê desafio, implementa ramos aritméticos explícitos, separa calculate da CLI e analisa três elementos separados por espaços. Documenta início, exemplos, erros e precisão flutuante. Falha pesquisa de caminhos relativos e usa depois os corretos. Escreve código/README, passa verificador, acrescenta ata e termina. Sem correção funcional após primeira passagem nem testes adicionais registados.

51 linhas de código e três docstrings (módulo, calculate, main), README de 72 linhas, ata de 29. Legibilidade não é teste de manutenção. PV adicional excede os dois entregáveis enumerados: tensão documental preservada, não penalizada pela suite. Sem alterações posteriores.

## O que foi verificado

- [x] calculator.py e README.md presentes — 2 controlos.
- [x] Sem chamadas diretas eval/exec — 1 controlo sintático, não segurança exaustiva.
- [x] 2 + 3 = 5; -2 - 3 = -5; 1.5 * 2 = 3; 7 / 2 = 3.5 — 4 casos num grupo.
- [x] % rejeitado com ValueError — 1 controlo.
- [x] Divisão por zero: ZeroDivisionError — 1 controlo.
- [x] CLI: saída 0, sem traceback, resultados 5 e -8, diagnóstico — 5 controlos.

Seis métodos unittest, catorze controlos. Candidato e orquestrador executaram a mesma suite congelada com sucesso. Quatro operações não equivalem a um único cálculo. [Catálogo](../docs/acceptance-tests.pt.md).

## V1 face a V2 — mesmo modelo e esforço, calculadora simples

| Medida | V1 solo | V2 consultiva |
| --- | ---: | ---: |
| Primeira / final | 6/6 / 6/6 | 6/6 / 6/6 |
| Controlos finais | 14/14 | 14/14 |
| Tempo | 98.572 s | 375.169 s |
| Entrada + saída | 98496 | 408616 |
| Sessões / papéis | 1 / 1 | 7 / 4 |
| Correções funcionais após primeira passagem | 0 | 0 |

**Nesta célula, V1 domina V2 nas medidas oficiais: mesmo resultado, menos tempo e tokens.** V2 usa ×3,81 tempo e ×4,15 tokens: +276,597 s e +310 120 tokens. A revisão V2 clarificou sobretudo documentação, sem correções funcionais. Modelo pedido e esforço idênticos; organização muda.

Reforça sobrecusto consultivo neste pequeno exercício, não condena todas as equipas nem avalia programadores paralelos. Não inventamos trocas interagentes para V1.

## Custos e limites

Entrada 96 182; cache 76 800 incluída; saída 2 314; raciocínio 104 incluído. Total 98 496 sem duplicar. Duração inclui início/fim CLI, exclui preparação, verificação independente e publicação. Sem novo limite ou instrumentação.

Contexto 200k, compactação 180k configurados, CLI 0.153.4. Sucesso com configuração enviada não prova pesos imutáveis nem aplicação do limite. V1 posterior a V2; uma observação, carga/cache variáveis. Fronteiras temporais ligeiramente diferentes; V2 inclui retransmissão e primeira passagem após crítica. [Reservas](astra-medium-v1-preflight.pt.md).

Conformidade limitada a estes testes. Defeitos não cobertos e manutenção não quantificados.

## Provas e continuação

[PV / verbatim](../runs/astra-medium-core-v1-001/PV.md) · [trace.json](../runs/astra-medium-core-v1-001/trace.json) · [run.json](../runs/astra-medium-core-v1-001/run.json) · [Code](../runs/astra-medium-core-v1-001/solution/calculator.py) · [README](../runs/astra-medium-core-v1-001/solution/README.md) · [V2](astra-medium-v2.pt.md) · [Conclusions](CONCLUSIONS.pt.md)

Scientific continua prepared_not_started, solution/ vazio e autorização false. Requer novo acordo após publicação deste relatório.
