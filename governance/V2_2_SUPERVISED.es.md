# V2.2 — piloto supervisado congelado

[Français](V2_2_SUPERVISED.md) · [English (UK)](V2_2_SUPERVISED.en.md) · **Español** · [Português](V2_2_SUPERVISED.pt.md)

**Nueva autorización: intento 002**, calculadora simple Astra medio, desde cero. Mismo motor, mandatos y tests que 001; sin solución anterior. Saldo inicial no medido; go del usuario tras solicitar cuota completa. Sin retry ni científica autorizados. [Manifiesto 002](v2-2-supervised-002.json).

El usuario autoriza **solo la calculadora simple**, Astra medio, ID astra-medium-core-v2-2-supervised-001. Científica y repeticiones requieren otro acuerdo. [Manifiesto congelado y hashes](v2-2-supervised.json).

Dos roles, tres sesiones nuevas: MAIN implementa, REV-01 revisa, MAIN arbitra y corrige. Se conservan los [mandatos V2.2](V2_2_PROTOCOL.es.md); el lanzador añade únicamente contexto del directorio y orden local del verificador. Sin ayuda humana al código ni consultor adicional. Primera verificación oficial en la fase final; diagnóstico retrospectivo inicial después del cierre.

Directorio temporal nuevo fuera del repositorio, copias intactas de desafío/verificador/tests, solución vacía. CLI nativo: MAIN workspace-write, REV-01 read-only, approval never, web desactivada. Sin eludir el sandbox. Delegación prohibida por mandato y desactivada por configuración, **sin garantía técnica absoluta**. Auditar archivos/eventos no prueba ausencia de lecturas externas. Sin secretos proporcionados ni soluciones anteriores consultadas; protecciones globales intactas.

Contexto 200000, compactación 180000 total; límites finales 600/1200/1200 palabras. Sin nuevo límite acumulado ni garantía de cuota. Parada sin reintento ante fallo, cuota, captura ilegible o infracción observada. Trazas brutas privadas; publicación solo de textos visibles auditados y métricas reales, sin razonamiento privado. Captura local probada; parada si el analizador rechaza eventos CLI.

El dispositivo MCP reforzado sigue NO-GO. Es **otra campaña exploratoria**, no certificación retroactiva del aislamiento ni comparación causal con V1/V2 históricas. Comparación homogénea requiere V1 bajo las mismas condiciones.

72 tests de mantenimiento correctos antes del lanzamiento: cuatro nuevos sobre secuencia, no reinicio, parada ante fallo, autorización y argumentos TOML. [Lanzador](../scripts/run_v2_2_supervised.py) · [Tests](../tests/test_v2_2_supervised.py).

OpenAI Docs orientó CLI no interactivo y captura JSONL. El login local indica ChatGPT; acceso real a Astra y consumo pendientes de observar. [Documentación oficial](https://learn.chatgpt.com/docs/non-interactive-mode).

[README](../README.es.md) · [Cualificación anterior](../results/v2-2-dispatch.es.md)
