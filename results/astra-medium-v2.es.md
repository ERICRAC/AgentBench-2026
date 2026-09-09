# V2 Astra medium — serie exploratoria

[Français](astra-medium-v2.md) · [English (UK)](astra-medium-v2.en.md) · **Español** · [Português](astra-medium-v2.pt.md)

Core terminado: 6/6 grupos y 14/14 controles al primer paso, confirmados independientemente. Scientific pendiente de lanzamiento.

`astra-medium-001` · `gpt-6-astra` · `medium` (MAIN, SA-01, SA-02, SA-03).

- Core : `astra-medium-core-v2-001`.
- Scientific : `astra-medium-scientific-v2-001`.

| Core | Value |
| --- | ---: |
| Wall time | 375.169 s |
| Session time sum | 451.039 s |
| Input | 395 814 |
| Cached input (included) | 302 080 |
| Output | 12 802 |
| Reasoning (included) | 122 |
| Input + output | **408 616** |

SA-01 revisa su preferencia por números finitos tras las respuestas cruzadas. MAIN registra 21 decisiones iniciales; SA-03 solo motiva aclaraciones numéricas del README, sin correcciones funcionales. 3 480 palabras de consultores, todas dentro del límite; 3 818 palabras visibles totales. Siete hilos distintos, consultores sin herramientas. Código: 50 líneas; README: 83; decisiones: 148.

Core medium consume 46,5 % menos tiempo y 28,6 % menos tokens que Core high (700.994 s, 572 168 tokens), con igual resultado oficial. Una observación no demuestra que menor esfuerzo sea mejor. Los costes de Scientific high interrumpido siguen incompletos.

[Core PV](../runs/astra-medium-core-v2-001/PV.md) · [Trace](../runs/astra-medium-core-v2-001/trace.json) · [Metadata](../runs/astra-medium-core-v2-001/run.json) · [Decisions](../runs/astra-medium-core-v2-001/solution/DECISIONS.md) · [Core high](astra-v2-core.es.md)

No existe V1 Astra/medium: no hay comparación causal V1/V2 con esfuerzo constante. Sol/high sigue siendo la campaña completa del panel (4/6). Ninguna V1 adicional sin petición.

[Guide](../docs/reading-guide.es.md) · [Astra/high](astra-v2-retired.es.md) · [Sol V2](sol-v2.es.md)
