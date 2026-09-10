# Balanço documental e de observabilidade

**Português** · [Français](documentation-audit.md) · [English (UK)](documentation-audit.en.md) · [Español](documentation-audit.es.md)

[Guia](reading-guide.pt.md) · [Cinco resumos V2](../results/run-summaries/index.pt.md) · [Instrumentação](observability.pt.md)

## Resultado e âmbito

Percurso: README → guia → capa de dois minutos → ata/verbatim → trace/run.json. Quatro línguas, cinco V2 completas, nenhum benchmark relançado. O guia explica profissões, transmissão, paralelismo, barreiras, correções e limites comparativos. Interpretações separadas dos factos gerados.

Capas fora de runs/: editar atas históricas invalidaria hashes. Novos resumos levam ao detalhe intacto. Governação e protocolo não mudam.

## Controlos executados

| Controlo | Resultado e âmbito |
| --- | --- |
| Manutenção Python | 12/12 métodos passaram, sem chamadas ao modelo; lista abaixo. |
| Geração | summarize_runs.py e --check: saída reproduzível e atual. |
| Ligações e línguas | check_documentation.py: ligações locais de README/docs/results/logs/governance, navegação recíproca das novas famílias; 64 hashes históricos verificados. |
| Markdown | markdownlint '**/*.md' correto com exclusões históricas existentes. |
| Soluções existentes | Nove V1/V2 verificadas: 66 execuções de grupos corretas. São os 15 métodos distintos habituais repetidos, não 66 testes novos. |
| Controlos candidatos Scientific médio | 4/4 métodos de controle_final.py corretos, separados da pontuação oficial. |
| Preservação | git diff 1dd93a7 -- runs challenges prompts governance scripts/run_v2.py scripts/publish_v2.py: sem diferenças. Nenhum contador, texto de run, configuração ou solução alterado. |

## Os doze testes de manutenção

| Teste em tests/test_observability.py | Cobertura |
| --- | --- |
| test_success_passes_arguments_and_return_unchanged | Mesmos argumentos/retorno, tempos relativos exatos, sem prompt/caminho nas medidas. |
| test_failure_is_persisted_and_propagated | Mesma exceção propagada; estado failed sem texto privado. |
| test_arbitrary_parallel_agents_are_not_serialised | Cinco sessões passam barreira comum; intervalos medidos sobrepostos no teste local. |
| test_original_frozen_runner_and_publisher_hashes | Scripts históricos atuais preservam hashes. |
| test_full_sequence_prompts_arguments_and_barriers_unchanged | Sete sessões falsas nos dois lançadores: mesmos prompts/argumentos, dependências, dois grupos concorrentes, função original restaurada. |
| test_allowlist_and_original_duration_preserved | Fusão em cópia, campos privados excluídos, duração CLI preservada. |
| test_rejects_missing_duplicate_or_mismatched_sessions | Rejeita captura parcial, duplicados, papéis incoerentes. |
| test_rejects_invalid_times_and_dependencies | Rejeita tempos negativos/não finitos/incoerentes, dependências inválidas, fontes desconhecidas. |
| test_merge_cli_does_not_overwrite | Destino existente intacto. |
| test_missing_metrics_are_not_zero_and_no_fake_timing | Ausentes não são zero; sem cronologia inventada. |
| test_measured_timing_generic_role_and_no_counter_double_count | Papel local arbitrário, intervalos, sem dupla soma de cache/raciocínio. |
| test_generated_pages_are_current | Cinco capas e índice, quatro línguas, conformes ao gerador. |

Comandos reproduzíveis no [guia técnico](observability.pt.md). Nunca chamam Codex: verificam software de medição, não inteligência candidata.

## Verificadores existentes repetidos

| Soluções preservadas | Grupos aprovados por solução |
| --- | ---: |
| astra-medium-core-v2-001, astra-core-v2-001, sol-core-v2-001 | 6 cada |
| astra-medium-scientific-v2-001, sol-scientific-v2-001 | 9 cada |
| astra-core-v1-002, sol-core-v1-001 | 6 cada |
| astra-scientific-v1-002, sol-scientific-v1-001 | 9 cada |

Comando: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --solution runs/IDENTIFICADOR/solution, com --challenge scientific-calculator para científicos. Manutenção, **não novas tentativas nem custos de benchmark**. [Os 71 controlos nomeados](acceptance-tests.pt.md) não mudam.

## Auditoria de incoerências históricas

«V2 não lançado» em protocolo/preflight descreve estado no congelamento. O guia distingue esse estado dos resultados publicados; não reescreve provas. «contradiction croisée» e «MAIN/RELAY» históricos são explicados, não substituídos nas traces. V2.x continua proposto, sem lançamento ou ganho supostos.

Três runs referenciam publishers anteriores: Sol usa ad7e234; Core Astra elevado, 63f9b92. Hashes verificados a partir de Git, não alinhados artificialmente com ficheiro atual. Um clone sem histórico deve recuperar esses commits para este controlo. Lançador experimental comum intacto.

## Limites e próximos passos

- Wrapper testado com sessões falsas, **ainda não com modelo real**; custo de medição não quantificado.
- Mermaid usa tema do leitor, sem paleta clara forçada. Apresentação GitHub clara/escura não verificada visualmente aqui por falta de navegador disponível; verificar no GitHub.
- Ligações: ficheiros locais, não disponibilidade Web nem todos os fragmentos de âncoras GitHub.
- Textos/decisões observados; novidade absoluta, ruído e causalidade não quantificados artificialmente.
- V1 Astra médio e protocolos V2.1/V2.2 ficam para trabalho experimental separado.

Sem nova dependência Python de execução, mudança de governação ou publicação de segredos. Edição local preexistente de .gitignore excluída da entrega.
