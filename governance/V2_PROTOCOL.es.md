# Protocolo V2 — Codex multiagente gobernado

[Français](V2_PROTOCOL.md) · [English (UK)](V2_PROTOCOL.en.md) · **Español** · [Português](V2_PROTOCOL.pt.md)

## Estado e hipótesis

El protocolo está preparado pero espera arbitraje antes de fijarse y lanzar V2.
Prueba si tres revisiones
especializadas mejoran la calidad o convergencia de un único escritor después
de contabilizar la coordinación. Las referencias actuales son
`codex-single-002` y `scientific-single-002`; los runs `001` siguen históricos.

## Decisiones por confirmar

Se recomiendan: A-01 contexto 200k/compactación 180k (100k obliga a repetir
V1); A-02 tres roles; A-03 análisis ciegos y una contradicción cruzada; A-04
1.200 palabras por análisis, 600 por réplica y 1.200 para crítica; A-05 mismo
`gpt-5.6-sol`/`high`; A-06 textos visibles completos tras filtrar secretos;
A-07 panel calidad/tiempo/tokens y dominio de Pareto, sin pesos arbitrarios.
A-08 usa subagentes nativos solo si exponen configuración y contadores por
thread; en caso contrario, sesiones `codex exec --json` separadas. Un preflight
trivial ajeno al benchmark verifica rol, aislamiento, texto y uso JSON antes de
leer un reto. A-06 ya está decidido; V2 espera las demás confirmaciones.

| Parámetro | Valor de referencia y V2 previsto |
| --- | --- |
| Modelo / esfuerzo | `gpt-5.6-sol` / `high` |
| Contexto declarado por agente | 200.000 tokens |
| Compactación automática | 180.000 tokens, alcance `total` |
| Sesiones | nuevas y efímeras |
| Retos y verificadores | versiones actualmente fijadas |
| Dependencias / ayuda humana | biblioteca estándar / ninguna |

## Qué significa «límite de contexto validado»

Capacidad activa, umbral de compactación y consumo acumulado son distintos.
Cada fichero de rol fija ventana de 200.000 y compactación `total` a 180.000;
la validación estricta debe aceptarlo. Cada consultor arranca en un thread
nuevo sin conversación heredada. `run.json` conserva rol, ID, valores y
SHA-256 del fichero, y el acta asocia textos y contadores con ese thread.

Esto prueba la configuración cliente y el aislamiento de entradas, no un
límite interno del servidor. Si la delegación nativa no lo demuestra, se usan
sesiones `codex exec` efímeras separadas; de lo contrario el run se detiene.

Véanse la [configuración Codex](https://developers.openai.com/codex/config-reference)
y la [documentación de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).

El candidato principal es el único orquestador/escritor. SA-01 analiza
requisitos y seguridad; SA-02, arquitectura y testabilidad; SA-03 actúa como
crítico QA adversarial. Todos son de solo lectura, sin subdelegación ni acceso
a otros runs.

SA-01 y SA-02 responden primero de forma independiente. Sus textos visibles se
intercambian íntegramente y cada uno dispone de una réplica para confirmar,
contradecir o revisar. El candidato arbitra e implementa. SA-03 recibe reto,
solución y tabla de decisiones para una crítica final. Cada recomendación se
marca aceptada, rechazada o no verificable con motivo.

Se registran primera pasada, resultado independiente, duración, tokens reales
por agente cuando estén disponibles, llamadas, contradicciones, consejos
aceptados o rechazados, correcciones e incidentes. Un [acta numerada](PV_TEMPLATE.es.md) conserva
literalmente cada mensaje visible tras controlar secretos y registra la
decisión motivada por rol.

La calidad se publica para primera pasada y resultado final. Tiempo y tokens
se comparan como ratios V2/V1, junto con tiempo mural, suma de tiempos-agente,
coste por rol, acuerdos, contradicciones, duplicados y consejos aceptados. V2
solo domina si no pierde calidad, no aumenta costes y mejora estrictamente una
dimensión. V2 Core se publica antes de V2 Scientific, sin ajuste intermedio.
