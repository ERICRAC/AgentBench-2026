# O run em 2 minutos — astra-core-v2-001

[Français](astra-core-v2-001.md) · [English (UK)](astra-core-v2-001.en.md) · [Español](astra-core-v2-001.es.md) · **Português**

Esta camada precede a ata detalhada na leitura; a ata original não muda. Dados ausentes não significam zero.

Calculadora simples · codex-multi · completed

## Factos observados

| | |
| --- | --- |
| Modelo / esforço | gpt-6-astra / high |
| Primeira verificação oficial | 6/6 unittest groups; 14/14 elementary checks |
| Resultado final do candidato | 6/6 unittest groups; 14/14 elementary checks |
| Veredicto independente | 6/6 unittest groups; 14/14 elementary checks |
| Duração total (s) | 700.994 |
| Tokens entrada + saída | 572168 |
| Sessões registadas (não chamadas API) | 7 |
| Correções funcionais após a primeira passagem | 0 |

A cache está incluída na entrada; o raciocínio, na saída. Não somar novamente. Uma sessão CLI pode conter várias chamadas ao modelo. A primeira verificação oficial ocorre após a crítica.

## Equipa e sequência

MAIN: árbitro e único escritor; SA-01: requisitos/segurança; SA-02: arquitetura/testabilidade; SA-03: revisão crítica. RELAY é o supervisor mecânico externo, não um candidato.

P1: análises independentes e barreira. P2: revisões cruzadas e barreira. Depois MAIN → SA-03 → MAIN e verificador. O paralelismo histórico está especificado, não é sobreposição medida.

<details>
<summary>Sessões registadas (não chamadas API)</summary>

| Sessão | Papel | Grupo paralelo especificado | Depende de | receives_from | Escritor | Duração CLI (s) | Tokens entrada + saída | Início / fim medidos (s) | Duração de invocação medida (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | Não registado | P1 | — | — | Não | 48.093 | 15602 | Não registado | Não registado |
| sa02_initial | Não registado | P1 | — | — | Não | 46.555 | 15491 | Não registado | Não registado |
| sa01_cross | Não registado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 27.954 | 16949 | Não registado | Não registado |
| sa02_cross | Não registado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 33.817 | 16980 | Não registado | Não registado |
| main_first | Não registado | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sim | 393.690 | 213048 | Não registado | Não registado |
| sa03_critic | Não registado | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Não | 44.659 | 27115 | Não registado | Não registado |
| main_final | Não registado | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sim | 180.712 | 266983 | Não registado | Não registado |

As invocações têm uma origem distinta da duração total histórica; ver o guia de instrumentação.

</details>

## Análise interpretativa

[CONFIRMÉ] Consenso e clarificação do contrato: 17 decisões iniciais. Após MSG-006, MAIN decide 14 pontos (7 aceites, 3 rejeitados, 4 não verificáveis) e altera apenas documentação. Nenhum defeito funcional confirmado nem interação que mude a pontuação. Repetir consultas em DECISIONS aumenta os prompts seguintes: custo observável, não prova de inutilidade de cada repetição. Ver o [relatório Core elevado](../astra-v2-core.pt.md), DECISIONS e MSG-007. Sem forçar [NOUVEAU] ou [BRUIT].

## Provas e próximos passos

[PV / verbatim](../../runs/astra-core-v2-001/PV.md) · [trace.json](../../runs/astra-core-v2-001/trace.json) · [run.json](../../runs/astra-core-v2-001/run.json) · [Decisões](../../runs/astra-core-v2-001/solution/DECISIONS.md)

[Guia de leitura](../../docs/reading-guide.pt.md) · [Testes](../../docs/acceptance-tests.pt.md) · [Conclusões](../CONCLUSIONS.pt.md) · [Index](index.pt.md)
