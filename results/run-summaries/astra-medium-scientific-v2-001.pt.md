# O run em 2 minutos — astra-medium-scientific-v2-001

[Français](astra-medium-scientific-v2-001.md) · [English (UK)](astra-medium-scientific-v2-001.en.md) · [Español](astra-medium-scientific-v2-001.es.md) · **Português**

Esta camada precede a ata detalhada na leitura; a ata original não muda. Dados ausentes não significam zero.

Calculadora científica · codex-multi · completed

## Factos observados

| | |
| --- | --- |
| Modelo / esforço | gpt-6-astra / medium |
| Primeira verificação oficial | 9/9 groups; 57/57 checks |
| Resultado final do candidato | 9/9 groups; 57/57 checks |
| Veredicto independente | 9/9 groups; 57/57 checks |
| Duração total (s) | 648.008 |
| Tokens entrada + saída | 570382 |
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
| sa01_initial | SA-01 | P1 | — | — | Não | 55.127 | 16718 | Não registado | Não registado |
| sa02_initial | SA-02 | P1 | — | — | Não | 54.314 | 16698 | Não registado | Não registado |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 28.439 | 17845 | Não registado | Não registado |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | Não | 28.315 | 17903 | Não registado | Não registado |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sim | 311.551 | 198505 | Não registado | Não registado |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | Não | 48.689 | 27934 | Não registado | Não registado |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sim | 204.160 | 274779 | Não registado | Não registado |

As invocações têm uma origem distinta da duração total histórica; ver o guia de instrumentação.

</details>

## Análise interpretativa

[CONTESTÉ → RETENU] As revisões cruzadas corrigem os conselhos sobre sin(cos(x)) e a amostragem de sqrt(-1). [IMPACT] SA-03 aponta limites de comprimento/profundidade → RELAY transmite MSG-006 → MAIN aceita → remove o limite e substitui recursão por pilha explícita → passa o teste candidato de expressões longas. Outros dois grupos corrigem terminal e canais CLI. [REJETÉ] Limites arbitrários de amostras e escrita atómica não exigidos. Dez aceites, dois rejeitados, um não verificável no dossier recebido. O script das 131 asserções iniciais está na trace de MAIN, não no dossier de SA-03: não está globalmente ausente. Ver arbitragem final e provas finais em DECISIONS. Contributo observável, sem ganho isolado de pontuação: o primeiro verificador vem depois. Novidade absoluta e [BRUIT] não estabelecidos.

## Provas e próximos passos

[PV / verbatim](../../runs/astra-medium-scientific-v2-001/PV.md) · [trace.json](../../runs/astra-medium-scientific-v2-001/trace.json) · [run.json](../../runs/astra-medium-scientific-v2-001/run.json) · [Decisões](../../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md)

[Guia de leitura](../../docs/reading-guide.pt.md) · [Testes](../../docs/acceptance-tests.pt.md) · [Conclusões](../CONCLUSIONS.pt.md) · [Index](index.pt.md)
