# V2 Sol — síntesis Core y Scientific

[Français](sol-v2.md) · [English (UK)](sol-v2.en.md) · **Español** · [Português](sol-v2.pt.md)

## Respuesta directa

V2 Sol/high completa ambos retos al máximo oficial: **15/15 grupos `unittest`,
es decir, 71/71 controles elementales**. Core supera 6 grupos y 14 controles en
la primera pasada. Scientific pasa de 3/9 a 9/9 tras corregir la carga con
Python 3.13; el verificador independiente confirma después los 57 controles.

La conformidad final es igual a V1 Sol. V2 consume **2 384,139 segundos** y
**1 475 626 tokens de entrada + salida**, frente a 1 199,432 segundos y 454 376
tokens de V1. Según la regla de Pareto preinscrita, **V1 domina V2 en ambos
retos**: igual calidad medida con menos tiempo y tokens.

[Catálogo de 71 controles](../docs/acceptance-tests.es.md) · [Informe V2
Core](sol-v2-core.es.md) · [Comparación V1 Sol/Astra](sol-vs-astra-v1.es.md)

## Tabla de veredictos

| Celda | Primera pasada | Veredicto final independiente | Tiempo | Entrada + salida |
| --- | ---: | ---: | ---: | ---: |
| V1 Sol · Core | 6/6 grupos · 14/14 controles | 6/6 · 14/14 | 189,964 s | 158 101 |
| V2 Sol · Core | 6/6 grupos · 14/14 controles | 6/6 · 14/14 | 796,534 s | 559 088 |
| V1 Sol · Scientific | 3/9 grupos | 9/9 · 57/57 | 1 009,468 s | 296 275 |
| V2 Sol · Scientific | 3/9 grupos | 9/9 · 57/57 | 1 587,605 s | 916 538 |
| **V1 total** | **9/15 grupos** | **15/15 · 71/71** | **1 199,432 s** | **454 376** |
| **V2 total** | **9/15 grupos** | **15/15 · 71/71** | **2 384,139 s** | **1 475 626** |

V2 equivale a ×1,99 el tiempo de V1 (+98,8 %) y ×3,25 sus tokens (+224,8 %).
Solo en Scientific, las razones son ×1,57 y ×3,09. La caché ya está incluida
en la entrada y el razonamiento en la salida.

## Recorrido Scientific

| Fase | Duración | Entrada | Salida | Palabras visibles |
| --- | ---: | ---: | ---: | ---: |
| SA-01 · análisis | 78,281 s | 14 402 | 2 015 | 915 / 1 200 máx. |
| SA-02 · análisis | 73,029 s | 14 404 | 1 860 | 1 065 / 1 200 máx. |
| SA-01 · contradicción | 41,247 s | 16 295 | 996 | 413 / 600 máx. |
| SA-02 · contradicción | 38,271 s | 16 297 | 917 | 466 / 600 máx. |
| MAIN · primera solución | 810,863 s | 394 075 | 21 975 | 429 |
| SA-03 · crítica | 226,117 s | 26 664 | 6 122 | 666 / 1 200 máx. |
| MAIN · arbitraje final | 431,056 s | 389 108 | 11 408 | 555 |
| **Total** | **1 698,864 s-agente** | **871 245** | **45 293** | **4 509** |

Las fases parcialmente paralelas explican que la suma de sesiones supere el
tiempo mural. Los siete hilos son distintos y usan Sol/high, ventana declarada
de 200 000 tokens y compactación a 180 000.

## Relación social y correcciones

SA-01 estudia contrato y seguridad; SA-02 arquitectura y testabilidad. Sus
análisis ciegos y la contradicción cruzada hacen visibles tres decisiones:
límites de recursos no contractuales, claves de variables adicionales y
seguridad de rutas. MAIN agrupa 16 recomendaciones: conserva 15 y rechaza una.

SA-03 plantea 15 puntos: cuatro defectos, siete riesgos y cuatro preferencias.
MAIN conserva 10 y rechaza 5. Antes del verificador, la crítica provoca seis
correcciones: Ctrl-C completo, salida numérica fiel, AST profundo iterativo,
ejemplo README, controles de terminal y taxonomía de `0^-1`.

La primera pasada oficial falla en seis grupos antes de sus pruebas
funcionales. La causa única es que el `dataclass` del token depende de
`sys.modules`, a diferencia del cargador Python 3.13 del verificador. MAIN lo
sustituye por una clase simple y alcanza 9/9. V1 Sol ya tuvo el mismo recorrido
3/9 → 9/9; V2 no mejora la convergencia oficial.

## Conclusión defendible

V2 aporta trazabilidad social y correcciones tempranas observables, pero
**ninguna mejora en los 71 controles congelados y un sobrecoste claro**. Core
muestra mucha redundancia; Scientific, un debate más rico que no evita el
defecto decisivo de carga. Con una sola observación por celda no existe base
estadística para generalizar. El siguiente paso es el hito de observación V2,
antes de decidir una hipótesis V2.1 distinta.

## Pruebas auditables

- Core: [acta](../runs/sol-core-v2-001/PV.md) · [traza](../runs/sol-core-v2-001/trace.json) · [metadatos](../runs/sol-core-v2-001/run.json).
- Scientific: [acta](../runs/sol-scientific-v2-001/PV.md) · [traza](../runs/sol-scientific-v2-001/trace.json) · [metadatos](../runs/sol-scientific-v2-001/run.json) · [decisiones](../runs/sol-scientific-v2-001/solution/DECISIONS.md).

El protocolo y el runner no cambiaron entre retos. No se publican razonamiento
interno bruto, secretos ni horas de trabajo.
