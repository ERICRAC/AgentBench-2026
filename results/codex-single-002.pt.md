# Resultado detalhado — `codex-single-002`

[Français](codex-single-002.md) · [English (UK)](codex-single-002.en.md) · [Español](codex-single-002.es.md) · **Português**

## Resumo executivo

A segunda referência V1 da **Calculadora Core** passou em **6 testes de 6** na
primeira execução oficial e na verificação independente. O orquestrador
experimental encarregou uma sessão candidata Codex distinta; esta trabalhou
sem consultores, subagentes nem ajuda funcional humana, com modelo, esforço e
contexto fixados. Ela é a referência atual para V2;
`codex-single-001` permanece como primeira observação histórica.

## Identidade e resultado

| Dado | Valor |
| --- | --- |
| Modo / objetivo | V1 · Codex sozinho / Calculadora Core |
| Modelo / esforço | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Contexto / compactação | 200.000 / 180.000 tokens, escopo `total` |
| Candidato / seus consultores ou subagentes | sessão `codex exec` distinta / 0 |
| Ajuda funcional humana | 0 |
| Primeira passagem / veredito independente | **6/6 / 6/6** |

O candidato implementou quatro operações explícitas, análise de entrada e uma
CLI resiliente. Depois do primeiro 6/6, um controlo manual encontrou apenas
uma localização de arranque ambígua no README; a documentação foi corrigida
sem alteração funcional.

## Medidas

| Métrica | Valor observado |
| --- | ---: |
| Duração arredondada | 193 s |
| Entrada / entrada em cache | 549.279 / 480.384 tokens |
| Saída / raciocínio incluído | 7.182 / 2.881 tokens |
| Entrada + saída | 556.461 tokens |
| Comandos / lotes de alterações | 17 / 2 |
| Código / documentação | 84 / 44 linhas |

Os tokens de entrada são cumulativos e incluem cache. O candidato também
aplicou indevidamente a regra Git global e tentou publicar; o remoto não foi
alterado. Os próximos prompts excluem explicitamente operações Git.

Comando independente: `python3 scripts/verify.py --solution
runs/codex-single-002/solution`. Consulte a [ata](../runs/codex-single-002/PV.md),
o [traço](../runs/codex-single-002/trace.md) e os
[metadados](../runs/codex-single-002/run.json).
