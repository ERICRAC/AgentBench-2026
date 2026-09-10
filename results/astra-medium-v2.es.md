# V2 Astra medio — resultados Core y Scientific

[Français](astra-medium-v2.md) · [English (UK)](astra-medium-v2.en.md) · **Español** · [Português](astra-medium-v2.pt.md)

Navegación actualizada: este informe conserva su estado de publicación original. V1 Astra medio ya cubre ambos ejercicios; véase el balance actual. [Balance completo y pruebas](astra-medium-v1-v2.es.md)

[Conclusiones — ¿cuándo compensa colaborar?](CONCLUSIONS.es.md)

Ambos intentos terminados y confirmados independientemente: **15/15 grupos, 71/71 controles**, al primer paso oficial. Total: **1 023.177 s y 978 998 tokens entrada + salida**. Sin interrupciones en esta serie. Se excluyen mantenimiento, publicación e intentos anteriores.

## Veredictos

| Run | Primer paso | Veredicto final | Tiempo mural | Tokens |
| --- | ---: | ---: | ---: | ---: |
| Core | 6/6 | 6/6 · 14/14 | 375.169 s | 408 616 |
| Scientific | 9/9 | 9/9 · 57/57 | 648.008 s | 570 382 |
| **Total** | **15/15** | **15/15 · 71/71** | **1 023.177 s** | **978 998** |

[Tests](../docs/acceptance-tests.es.md) · [Guide](../docs/reading-guide.es.md)

## Observaciones sociales

Core: SA-01 retira su preferencia por números finitos tras las respuestas cruzadas. MAIN registra 21 decisiones iniciales y 11 disposiciones de revisión. SA-03 solo motiva aclaraciones documentales; ninguna corrección funcional.

Scientific: las respuestas cruzadas corrigen dos propuestas iniciales (composición de funciones y expresión constante indefinida en todos los puntos). MAIN registra 22 decisiones. Tras SA-03, 13 puntos: 10 aceptados, 2 rechazados y 1 no verificable en su expediente. Tres grupos de correcciones: eliminar límites de longitud/recursión, escapar la salida del terminal y gestionar fallos de canales CLI. Pasan cuatro pruebas candidatas reproducibles, separadas de los 71 controles oficiales.

Las 131 aserciones iniciales siguen siendo controles candidatos. Su programa está en el comando registrado de MAIN inicial, pero no se entregó a SA-03 ni MAIN final: su reserva « no verificable » se refiere a su expediente, no a falta de captura del relé. Ninguna corrección tras el primer veredicto oficial.

## Métricas y límites

| Metric | Core | Scientific | Total |
| --- | ---: | ---: | ---: |
| Input | 395 814 | 548 369 | 944 183 |
| Cache (included) | 302 080 | 409 216 | 711 296 |
| Output | 12 802 | 22 013 | 34 815 |
| Reasoning (included) | 122 | 955 | 1 077 |
| Session time sum | 451.039 s | 730.595 s | 1 181.634 s |

Cinco respuestas consultoras suman 3 480 palabras Core y 3 625 Scientific, todas dentro del límite; mensajes visibles totales: 3 818 y 4 061. Siete hilos nuevos por intento; consultores sin herramientas, un escritor, ninguna ayuda humana funcional. Astra/medium, contexto 200k, compactación 180k, CLI 0.153.4; runner, prompts y verificadores sin cambios. Core publicado en 5c143cd antes de Scientific.

La suma de tiempos de sesión supera el tiempo mural por las consultas paralelas. Caché incluida en entrada y razonamiento en salida: no sumarlos dos veces. Contadores y textos por sesión en PV y JSON.

## Comparación válida

Frente a V2 Sol/high, esta serie usa 57,1 % menos tiempo y 33,7 % menos tokens, con igual veredicto final. Primer paso: 15/15 frente a 9/15 de Sol, cuyo Scientific encontró un fallo documentado del cargador Python 3.13. Cambian modelo **y** esfuerzo: ninguna prueba causal de superioridad de Astra o medium.

Core medium usa 46,5 % menos tiempo y 28,6 % menos tokens que Core high con igual resultado oficial. Core high completo está restablecido. Scientific high llegó a 9/9 antes de la interrupción final, pero sus costes son incompletos: no se calcula comparación de costes totales high/medium.

Sin V1 Astra/medium no se demuestra dominio V1/V2 a esfuerzo constante. Una observación por celda no permite generalización estadística. Sol sigue siendo la campaña completa del panel (4/6); la serie V2 medium termina 2/2.

[Sol V2](sol-v2.es.md) · [Core high](astra-v2-core.es.md) · [Scientific high](astra-v2-retired.es.md)

## Retomar el código

Los módulos contienen 4 docstrings Core y 10 Scientific, con 0 y 1 comentarios léxicos: « ningún comentario » omite parte de su documentación. No mide mantenibilidad. Scientific tiene 348 líneas y README 127; decisiones y controles enlazados abajo. Vx de relevo sigue como propuesta por fijar, no puntuación retroactiva.

## Pruebas

- Core : [PV](../runs/astra-medium-core-v2-001/PV.md) · [trace](../runs/astra-medium-core-v2-001/trace.json) · [metadata](../runs/astra-medium-core-v2-001/run.json) · [DECISIONS](../runs/astra-medium-core-v2-001/solution/DECISIONS.md).
- Scientific : [PV](../runs/astra-medium-scientific-v2-001/PV.md) · [trace](../runs/astra-medium-scientific-v2-001/trace.json) · [metadata](../runs/astra-medium-scientific-v2-001/run.json) · [README](../runs/astra-medium-scientific-v2-001/solution/README.md) · [DECISIONS](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md) · [CONTROLES](../runs/astra-medium-scientific-v2-001/solution/CONTROLES.md) · [controle_final.py](../runs/astra-medium-scientific-v2-001/solution/controle_final.py).
