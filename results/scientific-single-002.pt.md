# Resultado detalhado — `scientific-single-002`

[Français](scientific-single-002.md) · [English (UK)](scientific-single-002.en.md) · [Español](scientific-single-002.es.md) · **Português**

## Resumo executivo

A segunda referência V1 da **Calculadora Scientific** alcançou **9 testes de
9**. O orquestrador experimental encarregou uma sessão candidata Codex
distinta; esse único candidato entregou análise segura, amostragem, SVG e CLI
sem consultores, dependências externas nem ajuda funcional humana.

O primeiro verificador oficial parou ao carregar o módulo devido à interação
conhecida entre `dataclass` e o carregador dinâmico em Python 3.13. Uma correção
específica bastou. Esta execução é a referência atual para V2;
`scientific-single-001` continua publicada.

| Dado | Valor |
| --- | --- |
| Modo / objetivo | V1 · Codex sozinho / Calculadora Scientific |
| Modelo / esforço | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Contexto / compactação | 200.000 / 180.000 tokens, escopo `total` |
| Consultores ou subagentes do candidato / ajuda funcional humana | 0 / 0 |
| Primeira passagem | falha ao carregar o módulo |
| Resultado final candidato / independente | **9/9 / 9/9** |

A solução usa tokenizer de lista branca e parser recursivo. Funções são
mapeadas explicitamente, a amostragem separa valores indefinidos e o SVG
passivo escapa o título. A CLI recupera após erros.

| Métrica | Valor observado |
| --- | ---: |
| Duração arredondada | 541 s |
| Entrada / cache | 587.315 / 541.312 tokens |
| Saída / raciocínio incluído | 16.177 / 6.289 tokens |
| Entrada + saída | 603.492 tokens |
| Comandos / lotes de alterações | 16 / 2 |
| Código / documentação | 487 / 97 linhas |

A entrada é cumulativa e inclui cache. O verificador mantém um viés de
carregamento para certas `dataclass`; a amostragem uniforme também pode perder
uma descontinuidade entre pontos. A tentativa Git do candidato não alterou o
remoto.

Consulte a [ata](../runs/scientific-single-002/PV.md), o
[traço](../runs/scientific-single-002/trace.md) e os
[metadados](../runs/scientific-single-002/run.json).
