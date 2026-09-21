# V2.2 — encaminamiento real tras actualizar

[Français](v2-2-dispatch.md) · [English (UK)](v2-2-dispatch.en.md) · **Español** · [Português](v2-2-dispatch.pt.md)

## Veredicto final de cualificación — no listo para congelar

**La cualificación termina con NO-GO para el dispositivo automatizado actual. No se lanzó ningún benchmark.** No es un fallo de la calculadora ni de Astra: faltan integración del lanzador y garantías completas de aislamiento. Cerramos las pequeñas cualificaciones sucesivas; la próxima decisión es qué dispositivo utilizar.

| Requisito | Veredicto y prueba |
| --- | --- |
| Desarrollador → revisor → desarrollador | Dos simulaciones repetidas, tres sesiones cada una; sin puntuación candidata |
| Captura local de salidas | Correcta: stdin, stdout, stderr, salida no nula, 2 MB sin truncar y bytes no UTF-8 preservados |
| Interrupción del transporte local | Correcta: timeout y SIGINT real; trazas parciales conservadas, hijo detenido, estado interrupted |
| Aislamiento de herramientas | Parcial: pruebas anteriores de Bubblewrap y ocho rechazos conservados; sin nueva certificación de toda la cadena |
| Prohibición de delegación | No demostrada técnicamente; ningún spawn_agent intentado, listado nativo previamente disponible |
| Lanzador real completo | No listo: run_relay rechaza simulation=False; puente MCP probado aparte, sin adaptador real conectado |
| Captura/parada CLI → MCP → proceso y acceso al modelo | Sin cualificación integral; sin llamada autenticada ni garantía de cuota |

**68 tests de mantenimiento correctos**, no 68 tests de calculadora. Dos nuevos tests cubren captura binaria exacta y SIGINT con comprobación de parada del hijo. La orden preparada de `codex exec` usa ahora `-c default_permissions=...` en lugar de `-P`; la ruta sandbox existente conserva `-P`. El análisis de argumentos con `--help` termina con código cero: no demuestra carga del perfil ni aislamiento efectivo.

OpenAI Docs orientó esta corrección; una configuración supuesta no sustituye pruebas de ejecución. [Permisos oficiales](https://learn.chatgpt.com/docs/permissions). [Evaluación estructurada](v2-2-qualification.json) · [Tests del transporte](../tests/test_v2_2_transport.py) · [Lanzador bloqueado](../scripts/run_v2_2.py).

### Simplificación propuesta — pendiente de aprobación, no aplicada

Un **piloto supervisado** con tres sesiones CLI nuevas, Astra medio: desarrollador, revisión de instantánea, correcciones. Directorio nuevo fuera del repositorio con solo el desafío y entregables; captura de mensajes visibles, métricas disponibles, diferencias y veredicto independiente. Sin puente MCP personalizado ni framework adicional.

**Compromiso explícito:** directorios separados e instrucciones no equivalen a aislamiento técnico completo. La no delegación y los accesos se controlarían mediante instrucciones y auditoría de trazas disponibles, sin afirmar ausencia de accesos no observados. Cualquier infracción observada invalidaría el run; ninguna protección de secretos se eliminaría automáticamente. Documentar los permisos exactos antes del lanzamiento.

Piloto exploratorio con diferencias publicadas; sin comparación histórica estrictamente homogénea salvo referencia V1 bajo idénticas condiciones. Alternativa: conservar el aislamiento fuerte y aceptar un proyecto de integración separado antes del benchmark.

**Decisión solicitada: aceptar el piloto supervisado en vez de continuar el dispositivo automático reforzado?** Esto no autorizaría el lanzamiento: primero revisar y congelar explícitamente el alcance. Gobernanza general, desafíos y resultados históricos intactos.

## Pruebas anteriores conservadas

## Continuación — comprobación de escrituras nativas

**Ocho sondas adicionales: cuatro destinos × dos binarios, ocho rechazos explícitos y todos los testigos intactos.** `apply_patch` está disponible, pero no permite estas escrituras con `sandbox_mode="read-only"` y `approval_policy="never"`. Se resuelve esta duda concreta, no todo el preflight V2.2.

| Destino sintético de modificación | CLI 0.153.4 | Extensión 0.154.0-alpha.6.2 |
| --- | --- | --- |
| Archivo en solution/ | Rechazado, intacto | Rechazado, intacto |
| CHALLENGE.md ficticio en el padre | Rechazado, intacto | Rechazado, intacto |
| Archivo fuera del workspace | Rechazado, intacto | Rechazado, intacto |
| Enlace simbólico al archivo externo | Rechazado, destino y enlace intactos | Rechazado, destino y enlace intactos |

Cada sonda crea un directorio temporal nuevo, tres archivos testigo y un enlace. El proveedor local devuelve una sola instrucción fija de modificación. Después, el verificador compara los bytes de los tres archivos y el destino del enlace; finalmente elimina el directorio temporal. El archivo «externo» sigue dentro del árbol temporal propio: no se apunta a datos del usuario. No se utiliza modelo candidato, cuenta, secreto ni subagente.

**66 tests de mantenimiento correctos**, con tres nuevos: destinos relativos fijos; prohibición de ampliar la aprobación MCP a los parches; reconocimiento estricto del rechazo observado. Las ocho sondas CLI son independientes de estos tests unitarios. [Pruebas JSON de las ocho sondas](v2-2-native-patch.json) · [Tests fuente](../tests/test_v2_2_dispatch.py).

El estado global sigue siendo `blocked_tool_catalog`, no «preflight validado». Se conservan los resultados anteriores y su JSON. El rechazo nativo se prueba con un puente REV-01; no valida la integración final MAIN, las lecturas nativas, las interrupciones, la captura completa ni la prohibición de crear agentes. No se intentó llamar a `spawn_agent`.

OpenAI Docs orientó el mantenimiento de dos controles: sandbox de solo lectura y política sin aprobación. La integridad se comprueba mediante sondas locales, no mediante la documentación. [Documentación oficial](https://learn.chatgpt.com/docs/agent-approvals-security).

Reproducción sin modelo, un destino por vez; otras fixtures: `patch_contract`, `patch_outside`, `patch_symlink`. Seleccionar otra instalación con `--cli RUTA_DEL_BINARIO`, sin cambiar PATH. La salida no nula sigue siendo esperada: parada voluntaria del proveedor y catálogo no conforme.

```bash
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture patch_solution --enable-code-mode-host-for-probe
```

**Siguiente:** comprobar el bloqueo de delegación sin iniciar un candidato; después, interrupciones y captura. Astra medio se mantiene; sin congelación ni lanzamiento automático.

## Etapa anterior — enrutamiento MCP

Actualización de extensión visible: 0.154.0-alpha.6.2, antes 0.154.0-alpha.6.1. CLI del terminal sigue en 0.153.4 con idéntico hash. Sin cambios nuestros de configuración global, PATH, cuenta o archivos VS Code.

**Trayecto CLI → ejecutor → MCP → Bubblewrap → respuesta demostrado con printf fijo. Funciona en ambas versiones tras habilitar el host Code Mode y aprobar solo la herramienta MCP de la sonda. No es un éxito atribuible únicamente a actualizar.**

63 tests de mantenimiento correctos, 6 nuevos de fixtures/respuestas. Ocho sondas diagnósticas distintas: no ocho benchmarks ni validaciones globales.

| Sonda | Versión | Observación |
| --- | --- | --- |
| Host desactivado | 0.153.4 | Ejecución rechazada: code-mode host is disabled |
| Inventario real | 0.153.4 | Seis herramientas disponibles |
| Puente aprobado | 0.153.4 | printf ejecutado, salida exacta, código cero |
| Inventario actualizado | 0.154.0-alpha.6.2 | Mismo inventario de seis herramientas |
| Puente sin aprobación | 0.154.0-alpha.6.2 | Aprobación rechazada; sin tools/call MCP |
| Puente actualizado aprobado | 0.154.0-alpha.6.2 | printf ejecutado; tools/call MCP observado |
| Terminal nativo | 0.154.0-alpha.6.2 | tools.exec_command ausente; sin ejecución |
| Lista de agentes | 0.154.0-alpha.6.2 | Lectura ejecutada: un orquestador /root, sin subagente |

## Corrección del análisis

Una herramienta anunciada puede rechazarse al ejecutarla. El control anterior de catálogo sigue fallando, pero no probaba que toda desactivación fuese ineficaz. Evidencia histórica conservada; aclaración añadida sin reinterpretar runs retroactivamente.

Inventario: apply_patch, clock__curr_time, list_mcp_resource_templates, list_mcp_resources, mcp__agentbench__confined_command y read_mcp_resource. La función separada collaboration.list_agents también responde. No se intentó spawn_agent ni escribir mediante apply_patch.

## Límites y continuación

Solo demostrada la orden fija del puente. Faltan permisos nativos, escrituras MAIN/REV por todas las rutas, prohibición efectiva de crear agentes, interrupciones y captura completa antes de congelar. apply_patch presente no prueba fuga o escritura; listar no prueba que crear agentes funcione. Sin cambio de modelo necesario: Astra medio activo, Astra alto histórico.

OpenAI Docs orientó eventos y aprobación MCP por herramienta. La opción de aprobación se rechaza para otra fixture; no cambia política global ni autoriza benchmark. Respuestas ficticias fijas, loopback y HOME/CODEX_HOME vacíos; sin servicio modelo ni secretos reales.

Nuevos tests: eventos SSE coincidentes; rechazo de fixture arbitraria/aprobación ampliada; captura solo call_id conocido; salida ausente/duplicada no validada; eco exacto; distinción rechazo/inventario/lista.

Las sondas mantienen salida no nula: catálogo global no conforme y proveedor ficticio detiene la conversación tras la respuesta de herramienta. No invalida el eco confirmado ni autoriza lanzamiento.

[Tests](../tests/test_v2_2_dispatch.py) · [JSON](v2-2-dispatch.json) · [CLI](v2-2-cli-qualification.es.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/extend/mcp)

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture inventory
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture bridge_echo --enable-code-mode-host-for-probe --approve-bridge-echo-for-probe
```

[README](../README.es.md) · [V2.2](../governance/V2_2_PROTOCOL.es.md)
