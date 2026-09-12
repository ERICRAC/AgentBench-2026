# V2.2 — encaminamiento real tras actualizar

[Français](v2-2-dispatch.md) · [English (UK)](v2-2-dispatch.en.md) · **Español** · [Português](v2-2-dispatch.pt.md)

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
