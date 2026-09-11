# Preflight técnico V2.2 — simulaciones, ningún modelo

[Français](v2-2-preflight.md) · [English (UK)](v2-2-preflight.en.md) · **Español** · [Português](v2-2-preflight.pt.md)

**Preflight estático/simulado correcto: 2 desafíos × 3 fases; 26 tests nuevos, 38 de mantenimiento en total. Sin llamada a modelo, puntuación de calculadora ni cambio histórico.** Protocolo no congelado, lanzamiento no autorizado.

## Entregado

El [relé](../scripts/run_v2_2.py) ejecuta MAIN inicial → REV-01 → MAIN final con transporte determinista inyectado. El [preflight](../scripts/preflight_v2_2.py) verifica decisiones, dos configuraciones, inventaría 15 hashes y simula ambos desafíos en directorios temporales nuevos. Tres [mandatos](../governance/V2_2_PROTOCOL.es.md) intactos. [Configuraciones y decisiones](../governance/v2-2-draft/choices.json).

Capturas privadas: prompts exactos, JSONL, respuestas visibles, comandos/salidas, contadores, estado por fase e instantáneas inicial/final con texto/SHA-256. Sin filtro automático de publicación: no publicar directorios brutos. Razonamiento privado excluido de transmisiones. Fallos conservan pruebas disponibles y paran sin reintento. Si no pueden extraerse contadores de captura incompleta, queda el bruto y el total desconocido.

**Simulación no valida transporte real.** Se construyen argumentos Codex sin ejecutar procesos modelo; --live falla antes de crear capturas. Sesiones ficticias escriben SIMULATION ONLY, no soluciones. Contadores sintéticos (39 entrada + salida por escenario nominal), nunca consumo real. Preflight público sin puntuación ni consumo ficticios como resultados.

Hashes detectan escrituras prohibidas persistentes dentro del workspace, no previenen ni detectan todas las lecturas externas o escrituras transitorias. Permisos read-only/workspace-write verificados en configuración, sin aislamiento OS real en tests Python. Truncamiento declarado/marcador reconocido bloquea; ausencia de marcador no demuestra integridad CLI. SIGKILL no puede capturarse: solo último checkpoint garantizado. Quedan permisos efectivos, transporte/parada de procesos, verificación independiente de instantáneas y publicación filtrada.

## Reproducir sin modelo

```bash
python3 -B scripts/preflight_v2_2.py
python3 -B -m unittest discover -s tests -v
```

```bash
sim_root=$(mktemp -d /tmp/agentbench-lean-demo-XXXXXX)
python3 -B scripts/run_v2_2.py --simulate --challenge calculator --output "$sim_root/simple"
python3 -B scripts/run_v2_2.py --simulate --challenge scientific-calculator --output "$sim_root/scientific"
```

## Lista de 26 tests V2.2

Cada fila corresponde a método test_ del [archivo](../tests/test_v2_2.py), alfabéticamente. Se añaden 12 tests anteriores; ninguno reemplaza grupos de calculadora. Tests V2.2 bloquean subprocess.Popen y socket con dobles que fallan si se llaman.

| ID | Control | test_… |
| --- | --- | --- |
| T01 | Captura separada del candidato | capture_cannot_be_nested_in_workspace |
| T02 | Configuración y comando sin ejecución | configuration_and_unexecuted_argv |
| T03 | Cambio de esfuerzo rechazado | configuration_drift_rejected |
| T04 | Eventos inválidos rechazados | invalid_event_envelope |
| T05 | JSON incompleto conservado; parada | invalid_json_capture_preserved |
| T06 | Interrupción de teclado registrada | keyboard_interrupt_checkpointed |
| T07 | Modo real rechazado antes de ejecutar | live_rejected_before_transport_or_capture |
| T08 | Entregable ausente bloquea | missing_deliverable_stops |
| T09 | Entregable extra bloquea | missing_or_extra_deliverable_stops |
| T10 | Contadores ausentes no son cero | missing_usage_is_not_zero |
| T11 | Reutilización de solución/captura rechazada | nonempty_solution_and_existing_capture_refused |
| T12 | Fallo conserva captura y contadores | nonzero_process_retains_raw_and_metrics |
| T13 | Salidas ausentes, truncadas, eventos/contadores inválidos | parser_rejects_incomplete_unsupported_events_and_bad_usage |
| T14 | Fallo de revisión: sin reintento ni fase final | phase_failure_preserved_without_retry |
| T15 | Dos desafíos simulados, hashes, sin puntuación | preflight_no_model_no_verdict_and_hash_inventory |
| T16 | Cambios de decisiones/autorización rechazados | preflight_refuses_changed_choice_or_authority |
| T17 | Modificación del desafío detectada | protected_workspace_write_stops |
| T18 | Razonamiento excluido, texto visible intacto | reasoning_excluded_visible_text_unchanged |
| T19 | Reutilización de thread rechazada | reused_thread_stops |
| T20 | Escritura del revisor detectada; sin final | reviewer_write_stops_before_final |
| T21 | CLI simulada en ambos desafíos; sin sobrescritura | simulation_cli_both_challenges_and_no_overwrite |
| T22 | Enlaces simbólicos/físicos y binarios rechazados | snapshot_rejects_symlinks_hardlinks_and_binary |
| T23 | Directorio simbólico rechazado | symlink_workspace_rejected |
| T24 | Orden, transmisión completa, instantáneas y medidas | three_phases_full_handover_and_snapshots |
| T25 | Marcador de truncamiento bloquea | truncated_output_marker_stops |
| T26 | Exceso de palabras conservado sin truncar ni repetir | word_overrun_recorded_without_truncation_or_retry |

## Decisiones antes de congelar

Propuesta por validar: piloto exploratorio, un intento por calculadora, Astra medio, tres sesiones, revisión de 1200 palabras; publicar simple antes de autorización científica. Sin nuevo techo global, parar por cuota, sin espera/reintento automáticos. Sin garantía de cuota Plus. Los 18 runs de confirmación son propuesta separada, no comprometida. Presupuesto numérico cambia diseño: decidir antes de congelar y comparar referencias coherentemente.

Tras validar decisiones: preparar/calificar transporte real y aislamiento sin candidato benchmark; prueba modelo trivial necesita autorización separada. Después congelar hashes y pedir autorización simple. Inventario del borrador actual, no congelado ni preflight de acceso.

OpenAI Docs orientó JSONL/textos visibles y opciones efímeras/sandbox. [Documentación oficial](https://learn.chatgpt.com/docs/non-interactive-mode). Ayuda local codex exec --help y versión 0.153.4 consultadas sin llamada modelo; TOML válido no prueba aceptación, acceso Astra ni cuota.

[Protocolo V2.2](../governance/V2_2_PROTOCOL.es.md) · [JSON](v2-2-preflight.json) · [README](../README.es.md)
