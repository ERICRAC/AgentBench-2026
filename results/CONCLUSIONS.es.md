# Conclusiones — ¿cuándo compensa colaborar?

[Français](CONCLUSIONS.md) · [English (UK)](CONCLUSIONS.en.md) · **Español** · [Português](CONCLUSIONS.pt.md)

[Cinco runs V2, dos minutos cada uno](run-summaries/index.es.md) · [📖 Cómo leer e interpretar un run AgentBench](../docs/reading-guide.es.md)

> En las tareas estudiadas, el coste de coordinación supera el beneficio medido. AgentBench busca las condiciones donde se invierte esta relación: dificultad, especialización, paralelismo y coste de los errores.

Esto se refiere a comparaciones disponibles con modelo y esfuerzo idénticos y la V2 consultiva actual, no a todos los equipos. Las pruebas oficiales no miden todas las correcciones adicionales observadas.

**V1 frente a V2, Astra medio: igual puntuación oficial en ambos desafíos.** V2 utiliza ×3,56 tiempo y ×4,49 tokens en total. La revisión aporta correcciones de robustez fuera de la puntuación. [Balance completo y pruebas](astra-medium-v1-v2.es.md)

## Qué muestran las experiencias

| Comparación | Tiempo V2 / V1 | Tokens V2 / V1 |
| --- | ---: | ---: |
| Sol alto · calculadora simple | ×4,19 | ×3,54 |
| Sol alto · calculadora científica | ×1,57 | ×3,09 |
| Astra alto · calculadora simple | ×7,00 | ×4,75 |
| Astra medio · calculadora simple | ×3,81 | ×4,15 |
| Astra medio · calculadora científica | ×3,44 | ×4,78 |

Las cinco comparaciones alcanzan el mismo resultado oficial final: V1 consume menos tiempo y tokens. En Sol disminuye el sobrecoste relativo en la científica, sin convertirse en ganancia. Dos dificultades y una observación por celda no permiten situar ni extrapolar el umbral.

[Sol V1/V2](sol-v2.es.md) · [Astra Core V1/V2](astra-v2-core.es.md)

V1/V2 designan organizaciones, no generaciones de calculadora. **Calculadora simple** = identificador histórico Core; **calculadora científica** = Scientific. Comparar V1/V2 en cada ejercicio idéntico y después comparar esas diferencias. V1 simple frente a V2 científica mezclaría dificultad y organización.

En Astra medio, la relación temporal baja de 3,81 a 3,44 entre simple y científica, pero la de tokens sube de 4,15 a 4,78. No se observa umbral. La nueva V1 científica conserva límites de expresiones largas corregidos tras SA-03 (subagente 3, revisor crítico) en V2: contribución real no valorada por la puntuación; sondas V1 posteriores y no prerregistradas.

## Organizaciones propuestas — no lanzadas

| Organización | Reparto | Hipótesis |
| --- | --- | --- |
| Solo (V1) | Un candidato hace todo. | Ambas calculadoras terminadas. |
| Consultiva (V2 actual) | Un escritor y tres consultores. | Consejos y revisión evitan errores. |
| **V2.1** — Desarrollo paralelo | Dos desarrolladores, integrador y revisor; contribuciones aisladas e interfaces fijadas previamente. | El trabajo simultáneo compensa comunicación e integración. |
| **V2.2** — Pareja ligera | Un desarrollador y un revisor, una revisión acotada. | Conservar crítica útil con menos coordinación. |

**Nombres acordados: V2** sigue siendo el equipo consultivo histórico; **V2.1** es desarrollo paralelo; **V2.2** la pareja ligera; **V2.x** la familia de variantes futuras, no otro intento. V1 sigue como referencia solo. Comparaciones futuras en Astra medio, con calculadoras simple y científica. Nombres aprobados; protocolos detallados y lanzamientos pendientes.

**V2.2: 57 tests correctos; tres sondas CLI siguen en 7/8.** Paquete oficial separado reproduce el bloqueo. Sin modelo ni cambios de instalaciones existentes. **Astra alto: solo histórico.** [CLI](v2-2-cli-qualification.es.md)

Todas las variantes propuestas usan Astra medio. El mismo modelo no implica contexto, competencias reales ni coste total idénticos: registrar roles, información y presupuestos. La pareja cambia también el tamaño del equipo, no solo la topología.

Variantes separadas de V2 congelada; no reescribir benchmarks existentes. El protocolo actual no autoriza escritura paralela. Prerregistrar protocolo nuevo, permisos por archivo o rama, interfaces, integración y conflictos antes de lanzar.

## Buscar el umbral

V1 Astra medio está completa. Prerregistrar las variantes y comparar organizaciones en ambos ejercicios idénticos. Las calculadoras monofichero ofrecen poco trabajo divisible. Después ampliar a un reto modular o evolución de código con más interacciones; fijar nuevas pruebas antes de ejecutar.

Medir separadamente calidad, plazo hasta validación, tokens de todos, retrabajo de integración e intercambios. Repetir con orden equilibrado; fijar presupuestos, parada y tratamiento de cuotas. Separar esperas impuestas de ejecución. Quedan por decidir repeticiones y nuevo reto.

Puede haber umbrales distintos para plazo, tokens y calidad. Más rápido pero más caro es un compromiso. El umbral será un intervalo observado de condiciones, no un número mágico de líneas. No encontrarlo también es útil.

## Límites y pruebas

V1 y V2 Astra medio terminadas en ambas calculadoras. Astra medio V2 frente a Sol alto cambia modelo y esfuerzo; Scientific Astra alto tiene costes incompletos. No aíslan el efecto organizativo. Los PV muestran correcciones útiles, pero 71/71 no mide toda la calidad ni mantenibilidad.

[Astra medium](astra-medium-v2.es.md) · [Guide](../docs/reading-guide.es.md) · [README](../README.es.md) · [Tests](../docs/acceptance-tests.es.md)
