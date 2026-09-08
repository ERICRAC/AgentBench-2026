# V2 Astra — Calculadora Core

[Français](astra-v2-core.md) · [English (UK)](astra-v2-core.en.md) · **Español** · [Português](astra-v2-core.pt.md)

## Veredicto y comparación

Core supera la primera pasada y el control independiente: **6/6 grupos y 14/14 controles**. Con igual calidad oficial, V1 Astra domina V2 Astra: V2 usa ×7,00 el tiempo y ×4,75 los tokens. Frente a V2 Sol, Astra tarda 12,0 % menos pero usa 2,3 % más tokens: compromiso sin dominancia.

| Run | grupos · controles | Tiempo | Entrada + salida |
| --- | ---: | ---: | ---: |
| Astra V1 Core | 6/6 · 14/14 | 100.175 s | 120 478 |
| Sol V2 Core | 6/6 · 14/14 | 796.534 s | 559 088 |
| Astra V2 Core | 6/6 · 14/14 | 700.994 s | 572 168 |

[Catalogue](../docs/acceptance-tests.es.md) · [V1 Astra](astra-v1.es.md) · [V2 Sol](sol-v2-core.es.md)

## Observaciones sociales

SA-01 cubre contrato/seguridad, SA-02 arquitectura/testabilidad y SA-03 crítica QA. MAIN es el único redactor en dos sesiones nuevas. Los análisis convergen en una gramática CLI simple; MAIN produce 17 decisiones iniciales. SA-03 no confirma defectos funcionales. MAIN separa 14 decisiones finales: 7 retenidas, 3 rechazadas y 4 no verificables en su sesión; solo cambia documentación y trazabilidad.

Las cinco respuestas consultoras suman 2 995 palabras dentro de los límites; todos los mensajes visibles suman 3 446. MAIN copia los avisos en DECISIONS.md (386 líneas), retransmitido por el runner: esta repetición aumenta el contexto y su coste.

Siete hilos distintos, mismos roles, prompts y runner que V2 Sol, gpt-6-astra/high, contexto 200k/compactación 180k. Caché incluida: 430 848 tokens; razonamiento incluido: 1 261. Tiempo-sesiones: 775,480 s. Consultores sin herramientas y cambios en la solución activa. Una observación por celda, sin generalización estadística.

El relé captura los contadores no disponibles para el candidato. Las reservas de MAIN se refieren a su propio contexto; el acta conserva mandatos y trazas. El estado no iniciado del protocolo congelado describe su estado original; este informe registra la ejecución.

## Pruebas

[PV](../runs/astra-core-v2-001/PV.md) · [Trace JSON](../runs/astra-core-v2-001/trace.json) · [Run JSON](../runs/astra-core-v2-001/run.json) · [DECISIONS](../runs/astra-core-v2-001/solution/DECISIONS.md)
