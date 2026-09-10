# Balance documental y de observabilidad

**Español** · [Français](documentation-audit.md) · [English (UK)](documentation-audit.en.md) · [Português](documentation-audit.pt.md)

[Guía](reading-guide.es.md) · [Cinco resúmenes V2](../results/run-summaries/index.es.md) · [Instrumentación](observability.es.md)

## Resultado y alcance

Recorrido: README → guía → portada de dos minutos → acta/verbatim → trace/run.json. Cuatro idiomas, cinco V2 completas, ningún benchmark relanzado. La guía explica profesiones, transmisión, paralelismo, barreras, correcciones y límites comparativos. Interpretaciones separadas de hechos generados.

Portadas fuera de runs/: editar actas históricas invalidaría sus hashes. Nuevos resúmenes llevan al detalle intacto. Gobernanza y protocolo no cambian.

## Controles ejecutados

| Control | Resultado y alcance |
| --- | --- |
| Mantenimiento Python | 12/12 métodos pasados, sin llamadas al modelo; lista abajo. |
| Generación | summarize_runs.py y --check: salida reproducible y actual. |
| Enlaces e idiomas | check_documentation.py: enlaces locales de README/docs/results/logs/governance, navegación recíproca de familias nuevas; 64 hashes históricos verificados. |
| Markdown | markdownlint '**/*.md' correcto con exclusiones históricas existentes. |
| Soluciones existentes | Nueve V1/V2 verificadas: 66 ejecuciones de grupos correctas. Son los 15 métodos distintos habituales repetidos, no 66 tests nuevos. |
| Controles candidatos Scientific medio | 4/4 métodos de controle_final.py correctos, aparte de puntuación oficial. |
| Conservación | git diff 1dd93a7 -- runs challenges prompts governance scripts/run_v2.py scripts/publish_v2.py: sin diferencias. Ningún contador, texto de run, configuración o solución modificado. |

## Los doce tests de mantenimiento

| Test en tests/test_observability.py | Cobertura |
| --- | --- |
| test_success_passes_arguments_and_return_unchanged | Mismos argumentos/retorno, tiempos relativos exactos, sin prompt/ruta en medidas. |
| test_failure_is_persisted_and_propagated | Misma excepción propagada; estado failed sin texto privado. |
| test_arbitrary_parallel_agents_are_not_serialised | Cinco sesiones cruzan barrera común; intervalos medidos superpuestos en test local. |
| test_original_frozen_runner_and_publisher_hashes | Scripts históricos actuales conservan hashes. |
| test_full_sequence_prompts_arguments_and_barriers_unchanged | Siete sesiones falsas en ambos lanzadores: mismos prompts/argumentos, dependencias, dos grupos concurrentes, función original restaurada. |
| test_allowlist_and_original_duration_preserved | Fusión sobre copia, campos privados excluidos, duración CLI conservada. |
| test_rejects_missing_duplicate_or_mismatched_sessions | Rechaza captura parcial, duplicados, roles incoherentes. |
| test_rejects_invalid_times_and_dependencies | Rechaza tiempos negativos/no finitos/incoherentes, dependencias inválidas, fuentes desconocidas. |
| test_merge_cli_does_not_overwrite | Destino existente intacto. |
| test_missing_metrics_are_not_zero_and_no_fake_timing | Ausentes no son cero; sin cronología inventada. |
| test_measured_timing_generic_role_and_no_counter_double_count | Rol local arbitrario, intervalos, sin doble suma de caché/razonamiento. |
| test_generated_pages_are_current | Cinco portadas e índice, cuatro idiomas, conformes al generador. |

Comandos reproducibles en la [guía técnica](observability.es.md). Nunca llaman a Codex: verifican software de medida, no inteligencia candidata.

## Verificadores existentes repetidos

| Soluciones preservadas | Grupos pasados por solución |
| --- | ---: |
| astra-medium-core-v2-001, astra-core-v2-001, sol-core-v2-001 | 6 cada una |
| astra-medium-scientific-v2-001, sol-scientific-v2-001 | 9 cada una |
| astra-core-v1-002, sol-core-v1-001 | 6 cada una |
| astra-scientific-v1-002, sol-scientific-v1-001 | 9 cada una |

Comando: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --solution runs/IDENTIFICADOR/solution, con --challenge scientific-calculator para científicos. Mantenimiento, **no nuevas tentativas ni costes de benchmark**. [Los 71 controles nombrados](acceptance-tests.es.md) no cambian.

## Auditoría de incoherencias históricas

«V2 no lanzado» en protocolo/preflight describe estado al congelar. La guía distingue ese estado de resultados publicados; no reescribe pruebas. «contradiction croisée» y «MAIN/RELAY» históricos se explican, no se sustituyen en trazas. V2.x sigue propuesto, sin lanzamiento o mejora supuestos.

Tres runs referencian publishers anteriores: Sol usa ad7e234; Core Astra elevado, 63f9b92. Hashes verificados desde Git, no alineados artificialmente al archivo actual. Un clon sin historial debe recuperar esos commits para este control. Lanzador experimental común intacto.

## Límites y próximos pasos

- Wrapper probado con sesiones falsas, **todavía no con un modelo real**; coste de medida no cuantificado.
- Mermaid usa tema del lector, sin paleta clara forzada. Renderizado GitHub claro/oscuro no verificado visualmente aquí por falta de navegador disponible; comprobar en GitHub.
- Enlaces: archivos locales, no disponibilidad Web ni todos los fragmentos de anclas GitHub.
- Textos/decisiones observados; novedad absoluta, ruido y causalidad no cuantificados artificialmente.
- V1 Astra medio y protocolos V2.1/V2.2 quedan para trabajos experimentales separados.

Sin nueva dependencia Python de ejecución, cambio de gobernanza ni publicación de secretos. Edición local preexistente de .gitignore excluida de entrega.
