# V2.2 supervisionada — ensaio simples interrompido por quota

[Français](v2-2-supervised-core.md) · [English (UK)](v2-2-supervised-core.en.md) · [Español](v2-2-supervised-core.es.md) · **Português**

**O ensaio Astra médio começou realmente; depois a CLI indicou limite de utilização.** MAIN criou ambos os entregáveis, mas não terminou a sessão. REV-01 e MAIN final não foram iniciados. Sem repetição.

| Medida | Observação |
| --- | --- |
| Tentativa | astra-medium-core-v2-2-supervised-001 |
| Sessões | 1 iniciada, 0 concluídas de 3 previstas |
| Tempo do processo candidato | 48,639 s |
| Tempo total do ensaio interrompido | 48,641 s |
| Tokens / número de pedidos ao modelo | Não registados, não zero |
| Veredicto V2.2 completo | Nenhum |
| Diagnóstico após interrupção | 6/6 grupos, 14 controlos aprovados |

Ficheiros preservados **sem correções do orquestrador**. Após encerramento, o verificador confirmou entregáveis, ausência de execução dinâmica, quatro operações, erros de operador/divisão e recuperação CLI. [Checklist](../docs/acceptance-tests.pt.md). Não é uma passagem oficial da fase final nem foi comunicada ao candidato.

**Conclusão:** o transporte real permitiu leitura e escrita. O ensaio parou por quota, não pelo bloqueio MCP anterior. Não permite julgar eficiência do binómio: sem revisão, arbitragem ou total de tokens. Não comparar 48,641 s com V1/V2 completas. Mantêm-se as limitações do piloto supervisionado, sem afirmar isolamento completo.

[PV e análise social](../runs/astra-medium-core-v2-2-supervised-001/PV.md) · [Mandato completo](../runs/astra-medium-core-v2-2-supervised-001/PROMPT.md) · [Eventos visíveis](../runs/astra-medium-core-v2-2-supervised-001/trace.jsonl) · [Metadados](../runs/astra-medium-core-v2-2-supervised-001/run.json) · [Código intacto](../runs/astra-medium-core-v2-2-supervised-001/solution/calculator.py) · [Protocolo](../governance/V2_2_SUPERVISED.pt.md).

Capturas brutas privadas. O rasto público omite caminho temporário e ligações/hora de reposição do aviso de quota. Sem dados inventados. Ficheiros protegidos e hashes congelados verificados.

**Seguinte:** se o utilizador confirmar quota e novo lançamento, nova tentativa simples, ID novo e solução vazia. Não retomar nem reutilizar este código; científica não autorizada.

[README](../README.pt.md) · [Conclusões](CONCLUSIONS.pt.md)
