# V2.2 supervisada — pareja simple completada

[Français](v2-2-supervised-core-002.md) · [English (UK)](v2-2-supervised-core-002.en.md) · **Español** · [Português](v2-2-supervised-core-002.pt.md)

**V2.2 simple completada con Astra medio: 3 sesiones, 6/6 grupos (14 controles), 159,977 s y 113 774 tokens.** Sin cambios tras la revisión. Menor coste que la V2 histórica, pero mayor que el agente solo histórico; comparación exploratoria.

La pareja terminó sin interrupción por cuota ni reintento. MAIN desarrolla, REV-01 revisa en modo de solo lectura y una nueva sesión MAIN decide y verifica. Se conserva el intento interrumpido 001; 002 empezó desde cero.

## Resultados y comparación

| Organización | Tiempo (s) | Tokens entrada + salida | Calidad |
| --- | ---: | ---: | --- |
| V1 solo histórica | 98.572 | 98 496 | 6/6 grupos, 14 controles |
| V2 histórica, tres consultores | 375.169 | 408 616 | 6/6 grupos, 14 controles |
| V2.2 supervisada 002, un revisor | 159.977 | 113 774 | 6/6 grupos, 14 controles |

**La pareja no aporta una mejora de calidad medida en esta calculadora simple.** Los archivos iniciales y finales son idénticos y ambos superan las comprobaciones independientes. El revisor no encuentra defectos confirmados. Frente al agente solo histórico: **+62,3 % de tiempo, +15,5 % de tokens**. Frente a la V2 histórica: **−57,4 % de tiempo, −72,2 % de tokens**. La organización reducida cuesta menos que el equipo anterior, pero no supera al agente solo.

Diferencias exploratorias, no un efecto causal aislado: pueden variar las versiones CLI, la versión servida del modelo, la caché, la carga, los prompts y la instrumentación. Las referencias históricas usan la fila Simple, no los totales simple + científica. Una observación por organización no permite determinar el umbral de rentabilidad de la colaboración.

[V1 / V2 Astra medium](astra-medium-v1-v2.es.md)

## Medidas y límites

Entrada: 110 511 tokens; salida: 3 263. Los 65 280 tokens de caché ya están incluidos en la entrada y los 165 de razonamiento en la salida. Tres sesiones no equivalen a tres peticiones al modelo. Suma de duraciones: 159,958 s; tiempo total: 159,977 s. Mantenimiento, publicación y controles independientes excluidos del coste candidato.

**Este intento terminó.** No se midieron los saldos inicial y final de cuota: no podemos cuantificar la fracción de una ventana Plus consumida ni garantizar el siguiente intento. Los 48,641 s y los tokens desconocidos de 001 permanecen separados; el coste total de la campaña en tokens sigue incompleto.

## Pruebas y análisis social

Primer verificador oficial: 6/6; confirmación final independiente: 6/6; diagnóstico inicial retrospectivo: 6/6, no comunicado al candidato. Los 14 controles no son 14 operaciones aritméticas. Coste directo de revisión: 29,177 s y 14 489 tokens; un acuerdo explícito, ningún defecto confirmado y ninguna corrección. El coste total de coordinación no está aislado. El acta identifica los oficios y publica cinco mensajes de respuesta, tres mandatos completos y decisiones, sin razonamiento interno.

[PV — MAIN / REV-01](../runs/astra-medium-core-v2-2-supervised-002/PV.md) · [Prompts](../runs/astra-medium-core-v2-2-supervised-002/prompts.json) · [Trace](../runs/astra-medium-core-v2-2-supervised-002/trace.json) · [JSON](../runs/astra-medium-core-v2-2-supervised-002/run.json) · [Tests](../docs/acceptance-tests.es.md) · [001](v2-2-supervised-core.es.md) · [Protocol](../governance/V2_2_SUPERVISED.es.md)

## Siguiente paso

La calculadora científica sigue sin autorización. Propuesta: decidir si se lanza un nuevo intento supervisado con Astra medio, sin reintento automático. No se lanzó otro candidato.

[README](../README.es.md) · [Conclusions](CONCLUSIONS.es.md)
