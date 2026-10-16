# V2.2 científica reduzida — ensaio 002 concluído

[Français](v2-2-lean-scientific-002.md) · [English (UK)](v2-2-lean-scientific-002.en.md) · [Español](v2-2-lean-scientific-002.es.md) · [Português](v2-2-lean-scientific-002.pt.md)

**Ensaio científico 002 aprovado: 9/9 grupos, 57/57 controlos, 141 794 tokens, 207,630 s.** Sem alterações após revisão. A dupla continua mais dispendiosa do que o agente individual científico histórico; comparação exploratória.

## Resultado e sequência

Três sessões Astra médio: MAIN implementa e executa 78 controlos locais, REV-01 revê estaticamente sem defeito confirmado, MAIN final arbitra e passa o verificador oficial à primeira. O orquestrador confirma independentemente 9 grupos / 57 controlos nas versões inicial e final, idênticas. Os 78 controlos do candidato não são testes independentes adicionais.

Confirmação explícita transmitida: OBS-002 não se repetiu. Sem interrupção por quota nem repetição. Envelopes de 5 023, 21 226 e 22 569 caracteres, dentro de 24 000. Relatórios finais dentro dos limites.

## Custo e eficiência

| Condição | Tokens entrada + saída | Duração (s) | Resultado |
| --- | ---: | ---: | --- |
| Individual V1 histórico | 119 388 | 188,560 | 9/9 · 57/57 |
| V2 histórico | 570 382 | 648,008 | 9/9 · 57/57 |
| Dupla reduzida 002 | 141 794 | 207,630 | 9/9 · 57/57 |

Face ao individual histórico: **+18,8 % de tokens, +10,1 % de tempo**, sem melhoria de resultado nem correções. Face a V2 histórico: **−75,1 % de tokens, −68,0 % de tempo**. A dupla reduz muito o custo adicional coletivo, mas não supera o individual neste caso.

Entrada: 134 416, incluindo 77 440 em cache; saída: 7 378, incluindo 397 de raciocínio. Subconjuntos não somados duas vezes. Limiar entre sessões de 150 000 não atingido; sem teto rígido garantido. Tempo total 207,630 s; soma das sessões 207,620 s. Quota disponível e custos de orquestração, preparação e publicação não registados.

Ensaio 001 interrompido separado: 11 968 tokens, 12,811 s. Subtotal apenas dos ensaios científicos reduzidos 001+002: **153 762 tokens, 220,441 s**. Não é o custo da campanha inteira.

## Contributo e limites da revisão

REV-01 confirma a estrutura e distingue os 78 controlos declarados das provas indisponíveis. Assinala singularidades entre amostras, limite já documentado. MAIN final aceita três observações e marca uma como não verificável porque não recebeu as saídas. Nenhum defeito confirmado, correção ou ganho de qualidade demonstrado; revisão adicional explícita cuja prevenção de erros não é medida aqui.

## Limites e próximo passo

Nova campanha astra-medium-lean-003: mesmo modelo solicitado e esforço, mas prompts, transmissão, ambiente e cache diferentes. Um ensaio por condição; revisão exata do servidor e versão CLI no lançamento não registadas. Não se podem atribuir diferenças apenas à organização nem tratar simples/científica como par estritamente homogéneo.

Sem lançamento automático. Recomendação: analisar antes de gastar mais. O limiar de rentabilidade coletiva permanece desconhecido; um desafio paralelizável ou controlo individual contemporâneo exigiria protocolo e orçamento aprovados separadamente.

## Artefacts

- [PV / messages / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-002/run.json) · [Prompts](../runs/astra-medium-scientific-v2-2-lean-002/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-002/trace.json).
- [Solution](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md) · [Code](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py) · [Checks](../runs/astra-medium-scientific-v2-2-lean-002/verifications.json).
- [V1/V2](astra-medium-v1-v2.pt.md) · [OBS-002 / 001](v2-2-lean-scientific-001.pt.md).
- [57 checks](../docs/acceptance-tests.pt.md) · [Manifest](../governance/v2-2-lean-scientific-002.json).

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-2-lean-002/solution
```
