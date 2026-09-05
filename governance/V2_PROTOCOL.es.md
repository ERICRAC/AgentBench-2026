# Protocolo V2 — Codex multiagente gobernado

[Français](V2_PROTOCOL.md) · [English (UK)](V2_PROTOCOL.en.md) · **Español** · [Português](V2_PROTOCOL.pt.md)

## Estado e hipótesis

El protocolo queda fijado antes del primer run V2. Prueba si tres revisiones
especializadas mejoran la calidad o convergencia de un único escritor después
de contabilizar la coordinación. Las referencias actuales son
`codex-single-002` y `scientific-single-002`; los runs `001` siguen históricos.

| Parámetro | Valor de referencia y V2 previsto |
| --- | --- |
| Modelo / esfuerzo | `gpt-5.6-sol` / `high` |
| Contexto declarado por agente | 200.000 tokens |
| Compactación automática | 180.000 tokens, alcance `total` |
| Sesiones | nuevas y efímeras |
| Retos y verificadores | versiones actualmente fijadas |
| Dependencias / ayuda humana | biblioteca estándar / ninguna |

Antes del lanzamiento se debe demostrar que el límite se aplica a cada
agente. Si la delegación no lo expone, el run no pertenece a esta campaña.

Un orquestador es el único escritor. Dos consultores de solo lectura analizan
contrato/seguridad y diseño/testabilidad antes de implementar; un crítico de
solo lectura revisa la primera solución. Son exactamente tres consultores, sin
subdelegación ni acceso a otros runs. Solo se escribe en `solution/` y los
candidatos no ejecutan operaciones Git.

Se registran primera pasada, resultado independiente, duración, tokens reales
por agente cuando estén disponibles, llamadas, contradicciones, consejos
aceptados o rechazados, correcciones e incidentes. Un `PV.md` numerado registra
cada mandato, recomendación, respuesta y decisión motivada por rol. V2 Core se
publica antes de V2 Scientific y no hay ajuste entre ambas. Cualquier cambio
abre otra campaña.
