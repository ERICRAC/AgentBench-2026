# Peritaje intermedio — qué demuestra AgentBench

[Français](intermediate-review.md) · [English (UK)](intermediate-review.en.md) · [Español](intermediate-review.es.md) · [Português](intermediate-review.pt.md)

## Respuesta a la pregunta

> ¿En qué condiciones un equipo de agentes resulta más eficiente que uno solo, con modelo y esfuerzo solicitados idénticos, contando calidad, tiempo, tokens y coordinación?

**El proyecto demuestra cooperación observable y correcciones útiles en algunos ensayos. Todavía no demuestra una ventaja colectiva neta y reproducible.** Las calculadoras sirven principalmente para calibrar el experimento; el umbral sigue desconocido.

V2 consultiva histórica logra el mismo resultado oficial que el solo con mayor coste. La pareja reduce mucho el sobrecoste, pero su último ensayo científico usa +18,8 % de tokens y +10,1 % de tiempo sin correcciones tras revisión. La simple reducida mejora tiempo y tokens brutos frente al solo histórico, pero OBS-001 cambia el trabajo realizado: no demuestra superioridad.

Este peritaje examina artefactos existentes con dos revisiones separadas, metodológica y social, fuera de los candidatos. Ningún benchmark ni nueva campaña de modelos iniciado. Coste del peritaje no registrado ni incluido en costes candidatos.

## Medidas verificadas

| Desafío, Astra medio | Organización | Tiempo (s) | Tokens entrada + salida |
| --- | --- | ---: | ---: |
| Simple | Solo V1 | 98,572 | 98 496 |
| Simple | V2 consultiva | 375,169 | 408 616 |
| Simple | Pareja supervisada | 159,977 | 113 774 |
| Simple | Pareja reducida, OBS-001 | 65,964 | 87 775 |
| Científica | Solo V1 | 188,560 | 119 388 |
| Científica | V2 consultiva | 648,008 | 570 382 |
| Científica | Pareja reducida | 207,630 | 141 794 |

Todos pasan su suite final: simple 6 grupos / 14 controles; científica 9 / 57. Las filas no forman una única campaña controlada. Un ensayo por condición no mide variabilidad.

[Datos y huellas](intermediate-review-data.json) · [V1/V2](astra-medium-v1-v2.es.md) · [OBS-001](v2-2-lean-001.es.md) · [Científica 002](v2-2-lean-scientific-002.es.md).

## El resultado oculta diferencias de calidad

Dos sondas ya conocidas se aplicaron idénticamente a las tres soluciones científicas archivadas, en solo lectura con Python 3.13.5:

| Sonda | Esperado | Solo V1 | V2 consultiva | Pareja reducida |
| --- | ---: | --- | --- | --- |
| P1: 1 seguido de 10 000 espacios | 1 | Rechazo por longitud | 1 | 1 |
| P2: suma de 1 500 unos | 1 500 | Rechazo por complejidad | 1 500 | Rechazo por complejidad |

V2 histórica resuelve ambos casos. Su traza vincula la crítica SA-03 con correcciones de longitud/profundidad: contribución verificable en casos concretos, no efecto medio de la organización.

Sondas posteriores, elegidas con conocimiento de defectos: no son evaluación oculta, nueva puntuación oficial, examen exhaustivo ni obligación de recursos ilimitados. Un rechazo revela una limitación de uso; por sí solo no demuestra incumplimiento general.

Para una nueva campaña: congelar controles discriminantes de robustez, integración y mantenimiento, con casos independientes desconocidos por candidatos. Conservar la suite actual. Los 71 controles no son 71 repeticiones experimentales ni calidad completa.

## Qué demuestran las interacciones

V2 científica muestra desacuerdos, arbitrajes y cambios tras crítica QA: circulación de información e influencia observables. No demuestra que el mismo desarrollador con más tiempo o autorrevisión no hubiera corregido esos defectos.

En la última pareja, el revisor no confirma defectos, no ejecuta controles y el código queda idéntico. Distingue correctamente los 78 controles anunciados por MAIN de las pruebas recibidas. Buena disciplina de evidencia, sin ganancia de calidad observada. Ausencia de correcciones no prueba inutilidad universal ni prevención invisible.

El colectivo también puede introducir restricciones discutibles: MAIN adoptó 10 000 caracteres máximos antes de retirarlos tras SA-03. Contar solo correcciones finales ocultaría esta trayectoria. [Decisiones](../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md).

Las actas permiten estudiar acuerdos, contradicciones, adopción y cambios. Consejos aceptados cuentan decisiones, no eficiencia. Consenso entre instancias del mismo modelo no garantiza experiencia independiente; las trazas no establecen complacencia ni psicología humana.

Vincular **cláusula → prueba → decisión → modificación → control antes/después**. Medir defectos confirmados, falsas alarmas, regresiones, duplicaciones y puntos no verificables. Una calibración separada con defectos inyectados conocidos podría medir detección y precisión.

[Acta V2](../runs/astra-medium-scientific-v2-001/PV.md) · [Acta pareja](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).

## Principales sesgos

| Prioridad | Problema | Mejora |
| --- | --- | --- |
| Alta | Un ensayo, orden y entorno variables | Diferencias descriptivas; repeticiones equilibradas antes de generalizar |
| Alta | Solo ya alcanza resultado máximo | Separar conformidad mínima, robustez, integración y mantenibilidad |
| Alta | Solo una sesión, pareja tres sesiones nuevas | Cambian rol social, reinicio y cálculo; añadir control solo segmentado |
| Alta | OBS-001 y nuevas campañas | No atribuir la diferencia simple solo a coordinación |
| Media | Alias de modelo y esfuerzos distintos entre algunas series | Registrar metadatos expuestos; no clasificar aisladamente modelos/esfuerzos |
| Media | Pruebas oficiales V2 después de revisión | Separar primer borrador retrospectivo y primer paso oficial |
| Media | Costes excluidos e interrupciones incompletas | Delimitar candidatos, ensayos interrumpidos y mantenimiento |

¿Qué organización completa ofrece mejor compromiso práctico? ¿Qué añade el consultor con sesiones y presupuesto comparables? Son preguntas diferentes.

## Optimizaciones recomendadas

Científica actual: MAIN inicial 65 015 tokens, revisor 16 696, MAIN final 60 083. La reanudación representa aproximadamente 42,4 % e incluye lectura y verificación: no es coordinación pura medida.

Revisión y reanudación añaden unos 47,72 s. Restarlos no simula otra organización. Reutilizar el hilo del desarrollador o reducir contexto son hipótesis de una nueva condición, no cambios históricos.

En simple, tokens brutos bajan de 98 496 a 87 775, pero entrada no almacenada en caché + salida sube de 21 696 a 39 647. Esta medida es diagnóstico, no precio ni cuota Plus. Publicar caché, salida, total y tiempo separados.

Umbral 150 000 comprobado entre sesiones: no limita una sesión activa. Sobre de 24 000 caracteres tampoco limita tokens con herramientas. Ante fallo, conservar estado de archivos y distinguir contadores completos de protocolo terminado: actualmente cualquier excepción pone usage_complete=false.

Agrupar preparación y mantener un punto editorial actual. Informes y documento de relevo acumulan instrucciones históricas; panel mezcla Sol y Astra. Eso consume atención y favorece reinicios innecesarios. Mejorar navegación conservando pruebas.

## Estrategia para buscar el umbral

**Matizar la propuesta de cuatro roles: comenzar con variante paralela ligera.** Dos desarrolladores poseen componentes aislados; uno integra después en sesión distinta. Tres sesiones, dos profesiones y verificación independiente. Registrar integración; añadir revisor dedicado más tarde si se justifica. Nueva subcondición propuesta, no redefinición retroactiva de V2.1.

Preparar en un lote desafío modular y control V1 contemporáneo, interfaces y requisitos idénticos. El solo puede usar igual descomposición. Incluir pruebas de integración: piezas totalmente independientes favorecen al equipo sin medir interacción; dependencia total elimina paralelismo.

Medir camino crítico: preparación, máximo de tareas paralelas, integración y validación. Registrar inicios/finales relativos, solapamiento, tiempo total y acumulado, tokens de cada agente y retrabajo. Menor demora con más tokens es compromiso.

Para explicar la pareja actual, control más preciso: solo en tres sesiones con autorrevisión. Para explorar velocidad colaborativa, siguiente recomendado: piloto paralelo ligero. Son complementarios; no lanzar todas las variantes juntas.

Un piloto comprueba viabilidad, no reproducibilidad. Fijar objetivo principal — tiempo, tokens o calidad —, paradas y presupuesto global. Repetir condiciones prometedoras en orden equilibrado. El umbral será región de tareas y restricciones, no número universal de líneas.

## Preguntas y peritaje de hito

- ¿Prioridad: demora, economía de tokens o defectos caros?
- ¿Integración y dificultad distinguen las organizaciones?
- ¿Crítica ajena supera autorrevisión con recursos comparables?
- ¿La ventaja persiste con repeticiones e interrupciones?

Estas preguntas orientan decisiones técnicas sin confirmaciones humanas repetidas. Nueva campaña requiere alcance y presupuesto definidos.

Se incorporan ambas revisiones: método pide controlar sesiones y separar caché; revisión social pide contar restricciones introducidas y empezar con dos desarrolladores, uno integrando. Difieren en orden experimental: explicar pareja con solo segmentado o explorar paralelismo. Aquí se prioriza paralelismo ligero; control segmentado sigue necesario para aislar efecto del consultor. Ningún revisor es candidato.

**Recordatorio solicitado: peritaje del protocolo acordado por el modelo más capaz disponible antes de nuevos ensayos, y de resultados en el hito.** Este informe usa sesión actual y dos revisiones; no certifica clasificación de modelos disponibles. Costes de revisores del peritaje no expuestos.

## Verificación y pruebas

Costes recalculados de siete metadatos con huellas; seis ejecuciones comunes en tres soluciones; ningún candidato ni archivo de run modificado. Diagnóstico solo escribe en salida estándar y desactiva bytecode al iniciarse.

```bash
python3 -B scripts/audit_intermediate.py
```

[Script](../scripts/audit_intermediate.py) · [Datos](intermediate-review-data.json) · [Conclusión central](CONCLUSIONS.es.md) · [Controles](../docs/acceptance-tests.es.md).
