# Resultados

[Français](README.md) · [English (UK)](README.en.md) · [Español](README.es.md) · **Português**

[Cinco runs V2, dois minutos cada](run-summaries/index.pt.md) · [📖 Como ler e interpretar um run AgentBench](../docs/reading-guide.pt.md)

[Conclusões — quando compensa colaborar?](CONCLUSIONS.pt.md)

As V1 anteriores estão [arquivadas](ARCHIVE_V1.pt.md). «Referência atual» nesses relatórios descreve o estado histórico, não a campanha Astra.

**Percurso recomendado:** [compreender os 15 grupos e 71 controlos](../docs/acceptance-tests.pt.md)
→ [ver resultados](#resultados-publicados) → abrir o relatório, a ata e o
trace. Os antigos `6/6` e `9/9` contam grupos `unittest`, não cada asserção.

[V2 Astra medium](astra-medium-v2.pt.md) · [Astra/high](astra-v2-retired.pt.md) · [Guide](../docs/reading-guide.pt.md)

## Referência V1 Astra médio — simples terminada

**V1 simples Astra médio: 98,572 s, 98 496 tokens, 6/6 grupos e 14/14 controlos.** V2 usa ×3,81 tempo e ×4,15 tokens com resultado oficial igual. [Relatório e provas](astra-medium-v1-core.pt.md)

## Resultados publicados

| Tentativa | Mode | Objetivo | Resultado | Estado | Detalhes |
| --- | --- | --- | --- | --- | --- |
| `astra-medium-core-v1-001` | V1 solo Astra medium | Core | 6/6 · 14/14 | completed | [Report](astra-medium-v1-core.pt.md) |
| `astra-core-v1-002` | Codex sozinho | Calculadora Core | 6/6 grupos · 14/14 controlos | Referência Astra | [Relatório completo](astra-v1.pt.md) |
| `astra-scientific-v1-002` | Codex sozinho | Calculadora Scientific | 9/9 grupos · 57/57 controlos | Referência Astra | [Relatório completo](astra-v1.pt.md) |
| `sol-core-v1-001` | Codex sozinho | Calculadora Core | 6/6 grupos · 14/14 controlos | Controlo de modelo | [Comparação](sol-vs-astra-v1.pt.md) |
| `sol-scientific-v1-001` | Codex sozinho | Calculadora Scientific | 9/9 grupos · 57/57 controlos | Controlo de modelo | [Comparação](sol-vs-astra-v1.pt.md) |
| `sol-core-v2-001` | Equipa Codex | Calculadora Core | 6/6 grupos · 14/14 controlos | V2 Sol publicada | [Relatório, ata e trace](sol-v2-core.pt.md) |
| `sol-scientific-v2-001` | Equipa Codex | Calculadora Scientific | 9/9 grupos · 57/57 controlos | V2 Sol publicada | [Síntese, ata e trace](sol-v2.pt.md) |
| `astra-core-v2-001` | Equipa Astra | Calculadora Core | 6/6 grupos · 14/14 controlos | V2 Astra | [Relatório](astra-v2-core.pt.md) |
| `astra-medium-core-v2-001` | Equipa Astra medium | Calculadora Core | 6/6 grupos · 14/14 controlos | V2 Astra medium | [Relatório](astra-medium-v2.pt.md) |
| `astra-medium-scientific-v2-001` | Equipa Astra medium | Calculadora Scientific | 9/9 grupos · 57/57 controlos | V2 Astra medium | [Relatório](astra-medium-v2.pt.md) |

## Dados preservados

Para cada tentativa preservam-se, no mínimo: identificador e modo; data,
ambiente e versão do Codex; primeira passagem; resultado final; duração total;
intervenções humanas; observações e limites.
