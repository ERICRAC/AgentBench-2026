# V2.2 — puente de herramientas y catálogo bloqueante

[Français](v2-2-bridge.md) · [English (UK)](v2-2-bridge.en.md) · **Español** · [Português](v2-2-bridge.pt.md)

## Decisión y resultado

**Astra alto queda solo como histórico: sin nuevos runs previstos; resultados conservados.** Astra medio sigue activo. Sol alto requiere autorización separada para comparaciones futuras. [Decisión](../governance/v2-2-draft/model-policy.json).

El puente confinado funciona, pero **el catálogo efectivo del CLI bloquea la integración**, no los créditos. Sin llamadas modelo, autenticación real, congelación ni benchmark.

## Trabajo y verificación

El [puente MCP](../scripts/v2_2_tool_bridge.py) solo acepta una orden. El orquestador fija rol, workspace y captura privada; no se pueden cambiar mediante argumentos. Bubblewrap permite escribir solution/ a MAIN, no a REV-01. Entrada vacía y entorno limpio en el proceso confinado, sin credenciales Codex.

**52 tests correctos**, incluidos [6 nuevos](../tests/test_v2_2_tool_bridge.py): inicialización/herramienta única; rechazo de cambios de rol/rutas/permisos; órdenes inválidas; capturas separadas no reutilizables; notificaciones sin ejecución; protocolo/métodos inválidos.

[Preflight real sin modelo](../scripts/preflight_v2_2_bridge.py): **7/8 controles**.

- [x] MAIN: inicialización/listado, salidas completas, escritura permitida.
- [x] REV-01: inicialización/listado, salidas completas, escritura denegada.
- [x] Petición CLI recibida por el servidor HTTP local ficticio.
- [ ] Catálogo limitado a la herramienta confinada.

[Observaciones y hashes](v2-2-bridge.json) · [Aislamiento anterior](v2-2-transport.es.md)

## Bloqueo

CLI real con HOME/CODEX_HOME temporales vacíos y sin token heredado; proveedor loopback que rechaza inferencia con error HTTP controlado. No se publican cabeceras, prompts ni identificadores de sesión.

Negociación MCP 2025-06-18 y tools/list observados. Catálogo enviado en input/additional_tools, no en tools: la inspección inicial vacía era incompleta.

Aparecen functions.exec y collaboration.spawn_agent pese a features.shell_tool=false y features.multi_agent=false. Anunciar herramientas no demuestra que funcionen, pero **impide certificar el paso exclusivo por el puente**. MCP no aparece como herramienta directa única; su disponibilidad mediante el ejecutor queda pendiente.

La sonda falla deliberadamente hasta cumplir el criterio. La salida CLI no nula es esperada por el rechazo de inferencia; no mide cuota ni acceso al cuenta.

## Límites y continuación

OpenAI Docs orientó configuración y desactivaciones; aceptar opciones no demuestra su efecto. [Referencia](https://learn.chatgpt.com/docs/config-file/config-reference).

La interfaz MCP cambia el tratamiento histórico: nueva campaña, sin retroactividad. Capturas privadas; UTF-8 inválido o fallo de infraestructura detiene el puente. Pendientes: timeout MCP del cliente, truncado, ejecutor y cierre completo de procesos. Ningún nuevo presupuesto candidato aprobado.

Siguiente: configuración efectivamente restrictiva o CLI separado sin sustituir VS Code; después solicitar sonda autenticada Astra medio. Sin secretos en el repositorio.

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py
```

La segunda orden necesita autorización para namespaces Linux y actualmente debe fallar por catálogo. Testigos temporales retirados; soluciones históricas no utilizadas.

[Protocolo](../governance/V2_2_PROTOCOL.es.md) · [Conclusiones](CONCLUSIONS.es.md) · [README](../README.es.md)
