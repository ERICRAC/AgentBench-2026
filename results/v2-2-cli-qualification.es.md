# Cualificación del CLI V2.2

[Français](v2-2-cli-qualification.md) · [English (UK)](v2-2-cli-qualification.en.md) · **Español** · [Português](v2-2-cli-qualification.pt.md)

**Conclusión: cambiar de instalación no elimina el bloqueo.**

Tres ejecuciones de la misma sonda sin modelo: CLI autónomo 0.153.4, paquete npm oficial 0.153.4 instalado aparte y binario de extensión 0.154.0-alpha.6.1. Cada uno supera 7/8 controles; catálogo fuera de lista permitida. Ambos binarios 0.153.4 tienen SHA-256 idéntico. Sin cambios de PATH, cuenta ni extensión.

El catálogo incluido asigna a gpt-6-astra y gpt-5.6-sol tool_mode=code_mode_only y multi_agent_version=v2. Indicio compatible con las herramientas observadas, no prueba causal interna. No alteramos metadatos para forzar éxito. Pasar a Sol alto no es solución demostrada; Astra medio sigue activo, Astra alto solo histórico.

57 tests correctos: 52 anteriores y 5 controles del catálogo (formato clásico, additional_tools anidado, ambas ubicaciones, vacío/duplicados, herramienta desconocida). Vacío no equivale a restricción válida.

Preflight acepta --cli y registra versión, hash del binario y campos públicos del catálogo incluido. Proveedor HTTP ficticio local, HOME/CODEX_HOME vacíos, sin autenticación ni inferencia. Errores HTTP intencionales, sin coste modelo medido.

Siguiente paso útil: probar encaminamiento real y rechazo de capacidades prohibidas con llamadas ficticias no mutativas. Anunciar no demuestra ejecución. Sin congelación, sonda autenticada ni benchmark hasta demostrar esa frontera. Reinstalar otra vez la misma versión no añade evidencia.

Instalación de prueba conservada fuera del repositorio en directorio temporal dedicado; ningún helper/paquete publicado. OpenAI Docs orientó selección del paquete oficial; conclusiones basadas en sondas locales.

[JSON](v2-2-cli-qualification.json) · [MCP](v2-2-bridge.es.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/codex/cli) · [README](../README.es.md)
