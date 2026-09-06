# V1 Astra — relatório completo

[Français](astra-v1.md) · [English (UK)](astra-v1.en.md) · [Español](astra-v1.es.md) · **Português**

Os dois candidatos solo de `astra-high-001` terminaram com verificação separada. As V1 anteriores estão [arquivadas](ARCHIVE_V1.pt.md), fora desta campanha.

| Indicador | Core · astra-core-v1-002 | Scientific · astra-scientific-v1-002 |
| --- | ---: | ---: |
| Primeiro / final / independente | 6/6 · 6/6 · 6/6 | 9/9 · 9/9 · 9/9 |
| Duração | 100.175 s | 399.478 s |
| Entrada | 117769 | 208078 |
| Cache incluída | 96896 | 167808 |
| Saída | 2709 | 12432 |
| Raciocínio incluído | 195 | 1429 |
| Entrada + saída | 120478 | 220510 |
| Controlos adicionais | — | 4/4 |

## Tratamento e percurso

Core separa as quatro operações da CLI e recupera de erros de entrada. Passa a primeira verificação sem correção funcional; a ata conserva um erro inicial de caminho.

Scientific usa um analisador dedicado e representação aritmética pós-fixa com limites de tamanho e profundidade. Reutiliza a análise na amostragem, interrompe curvas em pontos indefinidos, serializa SVG com XML e mantém histórico. Após o primeiro 9/9, os testes próprios detetaram interpolação fora do intervalo perto do maior número flutuante. O candidato corrigiu o cálculo segundo o sinal dos extremos e conservou quatro testes. O orquestrador repetiu a suite e esses testes após o fecho.

## Protocolo, provas e limites

`gpt-6-astra/high`, CLI `0.153.4`, Python `3.13.5`, janela declarada 200.000 e compactação 180.000 (`total`). Sessões efémeras novas, sem consultores ou ajuda funcional humana; nenhuma operação Git do candidato observada. Configuração do utilizador ignorada e autenticação externa.

Os contadores JSON incluem cache na entrada e raciocínio na saída. As sessões concluídas somam 340.988 tokens e 499,653 s; não é o custo completo da campanha. A duração inclui início/fecho CLI, não preparação, publicação ou preflight.

Algumas saídas Scientific estão vazias no JSON. O primeiro 9/9 apoia-se na mensagem visível e código 0; o resultado final foi verificado separadamente. A configuração cliente não mede a janela do servidor. Não houve matriz de versões Python nem revisão visual no navegador.

[Core PV](../runs/astra-core-v1-002/PV.md) · [Core JSON](../runs/astra-core-v1-002/run.json)

[Scientific PV](../runs/astra-scientific-v1-002/PV.md) · [Scientific JSON](../runs/astra-scientific-v1-002/run.json)

## Incidentes preservados

`astra-core-v1-001`: CLI antigo recusado antes do trabalho, 5,301 s, tokens não registados. CLI atualizado e tentativa nova.

`astra-scientific-v1-001`: interrupção por quota após a primeira escrita, antes da verificação, 216,929 s, tokens não registados. Código preservado sem reutilização. Não é possível calcular o custo total da campanha.

[Core incident](../runs/astra-core-v1-001/run.json) · [Scientific incident](../runs/astra-scientific-v1-001/PV.md)

## Observações e próximo passo

Core: 100,175 s / 120.478 tokens contra Sol 193 s / 556.461. Scientific: 399,478 s / 220.510 contra 541 s / 603.492. Diferenças descritivas, não causais: mudaram modelo, CLI e instruções, com apenas um run completo por célula.

O defeito descoberto após 9/9 evidencia o teto da suite. O viés histórico do carregador dataclass permanece documentado sem alterar os testes fixados. Publicar V1 antes do preflight V2; ainda não executar o benchmark V2.
