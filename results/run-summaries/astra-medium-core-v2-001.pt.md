# O run em 2 minutos — astra-medium-core-v2-001

[Français](astra-medium-core-v2-001.md) · [English (UK)](astra-medium-core-v2-001.en.md) · [Español](astra-medium-core-v2-001.es.md) · **Português**

Esta camada precede a ata detalhada na leitura; a ata original não muda. Dados ausentes não significam zero.

Calculadora simples · codex-multi · completed

## Factos observados

| | |
| --- | --- |
| Modelo / esforço | gpt-6-astra / medium |
| Primeira verificação oficial | 6/6 groups; 14/14 checks |
| Resultado final do candidato | 6/6 groups; 14/14 checks |
| Veredicto independente | 6/6 groups; 14/14 checks |
| Duração total (s) | 375.169 |
| Tokens entrada + saída | 408616 |
| Sessões registadas (não chamadas API) | 7 |
| Correções funcionais após a primeira passagem | Não registado |

A cache está incluída na entrada; o raciocínio, na saída. Não somar novamente. Uma sessão CLI pode conter várias chamadas ao modelo. A primeira verificação oficial ocorre após a crítica.

## Equipa e sequência

MAIN: árbitro e único escritor; SA-01: requisitos/segurança; SA-02: arquitetura/testabilidade; SA-03: revisão crítica. RELAY é o supervisor mecânico externo, não um candidato.

P1: análises independentes e barreira. P2: revisões cruzadas e barreira. Depois MAIN → SA-03 → MAIN e verificador. O paralelismo histórico está especificado, não é sobreposição medida.

<details>
<summary>Sessões registadas (não chamadas API)</summary>

| Sessão | Papel | Grupo paralelo especificado | Depende de | receives_from | Escritor | Duração CLI (s) | Tokens entrada + saída | Início / fim medidos (s) | Duração de invocação medida (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | SA-01 | P1 | — | — | Não | 51.054 | 15919 | Não registado | Não registado |
| sa02_initial | SA-02 | P1 | — | — | Não | 47.764 | 15812 | Não registado | Não registado |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 28.390 | 17485 | Não registado | Não registado |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 28.140 | 17483 | Não registado | Não registado |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sim | 146.611 | 144301 | Não registado | Não registado |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Não | 37.223 | 22386 | Não registado | Não registado |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sim | 111.857 | 175230 | Não registado | Não registado |

As invocações têm uma origem distinta da duração total histórica; ver o guia de instrumentação.

</details>

## Análise interpretativa

[CONTESTÉ → RETENU] SA-01 retira a preferência por números finitos na revisão cruzada (MSG-003/004); MAIN decide 21 pontos antes de programar. [CONFIRMÉ] SA-03 aponta limites numéricos; MAIN verifica-os e clarifica o README sem alterar calculator.py. Onze decisões finais, nenhuma correção funcional. Nenhuma interação demonstra mudança de pontuação. Aceitar um conselho não prova que MAIN falharia sozinho; não se atribui [BRUIT] automaticamente. Ver DECISIONS, tabela final e pontos 9–12, e PV MSG-006/007.

## Provas e próximos passos

[PV / verbatim](../../runs/astra-medium-core-v2-001/PV.md) · [trace.json](../../runs/astra-medium-core-v2-001/trace.json) · [run.json](../../runs/astra-medium-core-v2-001/run.json) · [Decisões](../../runs/astra-medium-core-v2-001/solution/DECISIONS.md)

[Guia de leitura](../../docs/reading-guide.pt.md) · [Testes](../../docs/acceptance-tests.pt.md) · [Conclusões](../CONCLUSIONS.pt.md) · [Index](index.pt.md)
