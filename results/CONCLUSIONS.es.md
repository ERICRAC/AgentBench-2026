# Conclusiones — ¿cuándo compensa colaborar?

[Français](CONCLUSIONS.md) · [English (UK)](CONCLUSIONS.en.md) · **Español** · [Português](CONCLUSIONS.pt.md)

[Peritaje intermedio](intermediate-review.es.md) — El colectivo aporta correcciones de robustez observables, pero no hay ventaja neta reproducible establecida. Seis sondas comunes confirman un punto ciego del resultado. Próxima exploración: dos desarrolladores paralelos, uno integrando, con control solo contemporáneo.

## Decisión — qué hacemos ahora

**Cerrar la exploración V2.2 actual.** Ambos niveles están realizados con límites documentados. No se recomienda repetir el mismo ensayo ni optimizar más el lanzador por ahora. Esto no homogeneiza las campañas ni resuelve la pregunta científica.

### Resumen en un minuto

| Organización | Observación | Decisión propuesta |
| --- | --- | --- |
| V2 consultiva histórica | Mismo resultado, mayor coste que el solo en las comparaciones disponibles | Conservar como referencia; no repetir sin nueva hipótesis |
| Pareja V2.2 reducida | Científica: +18,8 % tokens, +10,1 % tiempo; sin correcciones tras revisión | Revisión explícita, rentabilidad no demostrada |
| V2.1 paralela | No medida todavía | Próxima hipótesis, no ganancia adquirida |

### Destino del tiempo y los tokens

En científica 002, MAIN inicial tarda 159,910 s; revisión y MAIN final añaden 47,711 s, más unos 0,010 s del relé. Solo histórico: 188,560 s; diferencia final: 19,070 s. Igualarlo exigiría quitar **9,2 % del tiempo total y 15,8 % de los tokens de la pareja** (22 406 tokens), con igual calidad. Umbrales aritméticos frente a una referencia histórica, no ahorros realizables demostrados.

La revisión consume 16 696 tokens. Restarlos dejaría 125 098, más que los 119 388 del solo. No equivale a un ensayo sin revisor: cambiaría también contexto y comportamiento de MAIN final. Solo indica que el consultor no explica todo el sobrecoste; también cuentan la reanudación y relectura del desarrollador.

[PV / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md) · [V1/V2](astra-medium-v1-v2.es.md).

### Siguiente experimento útil

**Propuesta: V2.1 con desafío modular y nuevo control V1, Astra medio.** Ejemplo de alcance por aprobar: motor de cálculo por un lado, curvas e interfaz por otro, contrato de integración previo. Dos desarrolladores paralelos, integrador y revisor; contribuciones aisladas y permisos limitados. Ambas organizaciones reciben requisitos, interfaces y pruebas idénticos. El solo puede usar la misma descomposición.

No cambiar retroactivamente el desafío monofichero. El modular abre nueva campaña; resultados anteriores son contexto, no control causal. Preparar en un lote contrato, pruebas independientes, fronteras de escritura, integración y medidas; ejecutar después el piloto autorizado. Sin cadena de preflights con modelos.

Fijar antes: calidad al menos igual al solo, tiempo hasta veredicto y tokens acumulados de todos los agentes; incluir integración y correcciones, separando ensayos interrumpidos. Menor tiempo con más tokens es un compromiso explícito. Un piloto no sitúa el umbral: decide si merece financiar repeticiones equilibradas.

**Pendiente de aprobación: alcance nuevo y presupuesto del par V1/V2.1.** No se deduce un techo fiable de cuota Plus. Esta síntesis no lanzó candidatos ni llamadas a modelos. No iniciar el piloto sin ese acuerdo global.

**Ensayo científico 002 aprobado: 9/9 grupos, 57/57 controles, 141 794 tokens, 207,630 s.** Sin cambios tras revisión. La pareja sigue siendo más costosa que el agente solo científico histórico; comparación exploratoria. [V2.2 científica reducida — ensayo 002 terminado](v2-2-lean-scientific-002.es.md).

Frente al solo histórico: **+18,8 % de tokens, +10,1 % de tiempo**, sin mejora de resultado ni correcciones. Frente a V2 histórico: **−75,1 % de tokens, −68,0 % de tiempo**. La pareja reduce mucho el sobrecoste colectivo, pero no supera al solo en este caso.

**V2.2 ligera real terminada: 6/6 grupos, 14 controles, 87 775 tokens, 65,964 s.** Objetivo < 100 000 alcanzado. Reducción observada, pero ambigüedad de mandato OBS-001: sin conclusión causal. [Rapport / Report / Informe / Relatório](v2-2-lean-001.es.md)

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

**V2.2 simple completada con Astra medio: 3 sesiones, 6/6 grupos (14 controles), 159,977 s y 113 774 tokens.** Sin cambios tras la revisión. Menor coste que la V2 histórica, pero mayor que el agente solo histórico; comparación exploratoria. [Rapport / Report / Informe / Relatório](v2-2-supervised-core-002.es.md).

Todas las variantes propuestas usan Astra medio. El mismo modelo no implica contexto, competencias reales ni coste total idénticos: registrar roles, información y presupuestos. La pareja cambia también el tamaño del equipo, no solo la topología.

Variantes separadas de V2 congelada; no reescribir benchmarks existentes. El protocolo actual no autoriza escritura paralela. Prerregistrar protocolo nuevo, permisos por archivo o rama, interfaces, integración y conflictos antes de lanzar.

## Buscar el umbral

V1 Astra medio está completa. Prerregistrar las variantes y comparar organizaciones en ambos ejercicios idénticos. Las calculadoras monofichero ofrecen poco trabajo divisible. Después ampliar a un reto modular o evolución de código con más interacciones; fijar nuevas pruebas antes de ejecutar.

Medir separadamente calidad, plazo hasta validación, tokens de todos, retrabajo de integración e intercambios. Repetir con orden equilibrado; fijar presupuestos, parada y tratamiento de cuotas. Separar esperas impuestas de ejecución. Quedan por decidir repeticiones y nuevo reto.

Puede haber umbrales distintos para plazo, tokens y calidad. Más rápido pero más caro es un compromiso. El umbral será un intervalo observado de condiciones, no un número mágico de líneas. No encontrarlo también es útil.

## Límites y pruebas

V1 y V2 Astra medio terminadas en ambas calculadoras. Astra medio V2 frente a Sol alto cambia modelo y esfuerzo; Scientific Astra alto tiene costes incompletos. No aíslan el efecto organizativo. Los PV muestran correcciones útiles, pero 71/71 no mide toda la calidad ni mantenibilidad.

[Astra medium](astra-medium-v2.es.md) · [Guide](../docs/reading-guide.es.md) · [README](../README.es.md) · [Tests](../docs/acceptance-tests.es.md)
