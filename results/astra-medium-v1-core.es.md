# V1 Astra medio — calculadora simple

[Français](astra-medium-v1-core.md) · [English (UK)](astra-medium-v1-core.en.md) · **Español** · [Português](astra-medium-v1-core.pt.md)

Navegación actualizada: este informe conserva su estado de publicación original. V1 Astra medio ya cubre ambos ejercicios; véase el balance actual. [Balance completo y pruebas](astra-medium-v1-v2.es.md)

astra-medium-core-v1-001 terminada: **6/6 grupos, 14/14 controles**, al primer pase y confirmados independientemente. **98,572 s y 98 496 tokens entrada + salida.** Ningún candidato científico lanzado.

## El run en dos minutos

Un candidato desarrollador en sesión nueva Astra medio, sin consultores ni subagentes. El orquestador externo lanza, captura y publica sin resolver.

Lee el desafío, implementa ramas aritméticas explícitas, separa calculate de CLI y analiza tres elementos separados por espacios. Documenta inicio, ejemplos, errores y precisión flotante. Falla una búsqueda de rutas relativas y utiliza después rutas correctas. Escribe código/README, pasa verificador, añade acta y termina. Sin corrección funcional posterior al primer pase ni tests adicionales registrados.

51 líneas de código y tres docstrings (módulo, calculate, main), README de 72 líneas, acta de 29. Legibilidad no equivale a test de mantenibilidad. PV adicional excede los dos entregables enumerados: tensión documental preservada, no penalizada por la suite. Sin retoques después.

## Qué se verificó

- [x] calculator.py y README.md presentes — 2 controles.
- [x] Sin llamadas directas eval/exec — 1 control sintáctico, no seguridad exhaustiva.
- [x] 2 + 3 = 5; -2 - 3 = -5; 1.5 * 2 = 3; 7 / 2 = 3.5 — 4 casos en un grupo.
- [x] % rechazado con ValueError — 1 control.
- [x] División por cero: ZeroDivisionError — 1 control.
- [x] CLI: salida 0, sin traceback, resultados 5 y -8, diagnóstico — 5 controles.

Seis métodos unittest, catorce controles. Candidato y orquestador ejecutaron la misma suite congelada con éxito. Cuatro operaciones no equivalen a un único cálculo. [Catálogo](../docs/acceptance-tests.es.md).

## V1 frente a V2 — mismo modelo y esfuerzo, calculadora simple

| Medida | V1 solo | V2 consultiva |
| --- | ---: | ---: |
| Primer / final | 6/6 / 6/6 | 6/6 / 6/6 |
| Controles finales | 14/14 | 14/14 |
| Tiempo | 98.572 s | 375.169 s |
| Entrada + salida | 98496 | 408616 |
| Sesiones / roles | 1 / 1 | 7 / 4 |
| Correcciones funcionales tras primer pase | 0 | 0 |

**En esta celda, V1 domina V2 en medidas oficiales: mismo resultado, menos tiempo y tokens.** V2 usa ×3,81 tiempo y ×4,15 tokens: +276,597 s y +310 120 tokens. La revisión V2 aclaró principalmente documentación, sin correcciones funcionales. Modelo solicitado y esfuerzo idénticos; cambia organización.

Refuerza el sobrecoste consultivo en este ejercicio pequeño, no condena cualquier equipo ni evalúa desarrolladores paralelos. No inventamos intercambios interagentes para V1.

## Costes y límites

Entrada 96 182; caché 76 800 incluida; salida 2 314; razonamiento 104 incluido. Total 98 496 sin duplicar. Duración incluye inicio/cierre CLI, excluye preparación, revisión independiente y publicación. Sin nuevo límite ni instrumentación.

Contexto 200k, compacción 180k configurados, CLI 0.153.4. Éxito con configuración enviada no prueba pesos inmutables ni aplicación del límite. V1 posterior a V2; una observación, carga/caché variables. Límites temporales ligeramente distintos; V2 incluye relevo y primer pase tras crítica. [Reservas](astra-medium-v1-preflight.es.md).

Conformidad limitada a estos tests. Defectos no cubiertos y mantenibilidad no cuantificados.

## Pruebas y continuación

[PV / verbatim](../runs/astra-medium-core-v1-001/PV.md) · [trace.json](../runs/astra-medium-core-v1-001/trace.json) · [run.json](../runs/astra-medium-core-v1-001/run.json) · [Code](../runs/astra-medium-core-v1-001/solution/calculator.py) · [README](../runs/astra-medium-core-v1-001/solution/README.md) · [V2](astra-medium-v2.es.md) · [Conclusions](CONCLUSIONS.es.md)

Scientific sigue prepared_not_started, solution/ vacío y autorización false. Requiere nuevo acuerdo tras publicar este informe.
