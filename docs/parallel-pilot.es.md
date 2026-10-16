# Próximo piloto — calculadora modular y desarrollo paralelo

[Français](parallel-pilot.md) · [English (UK)](parallel-pilot.en.md) · [Español](parallel-pilot.es.md) · [Português](parallel-pilot.pt.md)

## Decisión de preparación

**Preparación sin modelos; protocolo propuesto, no congelado. Ningún candidato nuevo ejecutado.**
La comparación busca **menor tiempo de entrega con calidad comparable**. Los tokens son una restricción y un resultado separado: mayor rapidez con más tokens será un compromiso.
[Análisis que fundamenta la decisión](../results/intermediate-review.es.md).

Nombre propuesto: **V2.1 ligera**, dos desarrolladores y uno integra después. Sustituye la propuesta de cuatro roles solo para este piloto. La V2 histórica no cambia. Su protocolo de escritor único no autoriza esta organización; la nueva campaña deberá fijar los permisos.

## Alcance propuesto

Nueva **calculadora científica modular con procesamiento por lotes**, solo biblioteca estándar Python, sin dependencias de ejecución, `eval` ni `exec`. Una expresión inválida genera un error local y las siguientes continúan.

| Archivo | Responsabilidad | Propietario durante el paralelo |
| --- | --- | --- |
| `engine.py` | Expresiones seguras y muestreo con discontinuidades | DEV-A, motor |
| `presentation.py` | SVG, lotes JSON y resultados de error | DEV-B, presentación |
| `cli.py` | Comandos, entradas, salidas y errores | DEV-B |
| `README.md` | Uso, contratos, límites y ejemplos | DEV-B |
| Todos | Integración, correcciones y verificación final | DEV-A, sesión INT |

El solo recibe las mismas interfaces, descomposición, ejemplo de lote y comandos de prueba; elige su orden de trabajo. Ningún esqueleto funcional es exclusivo del equipo.

Interfaces por especificar:

- `engine.evaluate(expression, variables=None) -> float`: sintaxis científica y prioridades explícitas en el nuevo contrato, sin importar soluciones históricas.
- `engine.sample_curve(expression, x_min, x_max, samples=201)`: pares con `None` para valores indefinidos.
- `presentation.write_svg(points, output_path, title="")`: XML válido, texto escapado y segmentos separados.
- `presentation.run_batch(jobs)`: resultados ordenados `{"ok": true, "value": número}` o `{"ok": false, "error": texto}`. Cada tarea contiene `expression` y opcionalmente `variables`.
- `python cli.py batch INPUT.json OUTPUT.json`: estructura inválida, salida no nula y mensaje sin traceback. Los errores de expresiones individuales permanecen en los resultados; las demás continúan.
- `python cli.py plot EXPRESSION OUTPUT.svg --min A --max B --samples N`: muestreo y exportación al archivo solicitado.

Antes del cierre: fijar tipos, números no finitos, límites numéricos y de tamaño, códigos de salida, sobrescritura y errores de dominio. El verificador no debe inventar estas decisiones.

## Controles independientes previstos

Casillas pendientes: **requisitos previstos, no pruebas ejecutadas ni puntuación**.

- [ ] M01: importación estándar, entregables y mecanismos prohibidos.
- [ ] M02: cuatro operaciones, prioridades, paréntesis, potencias y signos.
- [ ] M03: funciones, constantes, variable y nombres prohibidos.
- [ ] M04: sintaxis inválida, dominios y resultados no finitos.
- [ ] M05: límites, número de puntos y discontinuidades.
- [ ] M06: SVG analizable, título escapado y sin puente sobre discontinuidades.
- [ ] M07: lote mixto, orden conservado y continuación tras error.
- [ ] M08: estructura JSON inválida y errores de CLI.
- [ ] M09: integración real motor → lote y motor → curva → SVG.
- [ ] M10: API documentada, ejemplos ejecutables y responsabilidades.

Publicar casos elementales y recuentos tras implementar la suite. Calibrar su cargador con construcciones Python estándar e implementaciones equivalentes; inyectar fallos conocidos para comprobar detección. Reservar una evaluación independiente de robustez sin presentar las pruebas públicas como ocultas. Los 6/9 grupos históricos no cambian.

## Organización y observación

V1: una sesión nueva, un candidato y todo el alcance. V2.1 ligera: dos sesiones simultáneas en directorios aislados con contrato común y misión propia. Ninguno lee los archivos activos del otro. El orquestador reúne las instantáneas terminadas sin editarlas e inicia INT con ambas entregas y notas. INT puede corregir todos los archivos; atribuir cada cambio.

La integración espera a ambos desarrolladores. Archivos fuera de alcance, entregables ausentes o errores de transporte detienen el intento preservando pruebas, sin reintentos automáticos. Validar aislamiento con candidatos ficticios antes de ejecutar modelos.

Guardar mandatos, respuestas visibles y mensajes de integración. Numerar hallazgos y enlazar cláusula, prueba, decisión, cambio y control. Medir defectos corregidos, regresiones, falsos positivos y duplicaciones. La mejora documental solo cuenta como ganancia medida con una rúbrica previa.

Medir tiempo total, solapamiento real, suma de tiempos de agentes, integración y verificación por separado. Publicar tokens de entrada, caché y salida por sesión, costes de interrupciones y preparación fuera del candidato.

## Presupuesto propuesto y revisión

Astra medio para ambas organizaciones. Propuesta para aprobar al congelar: **un piloto solo y después uno paralelo**, umbral **entre sesiones de 150 000 tokens por organización**, **300 000 nominales para la pareja**, sin reintentos. Las sesiones paralelas pueden superar conjuntamente el umbral antes del siguiente control; no es un límite estricto ni garantiza el cupo Plus.

El solo puede superar el umbral en su única sesión. Publicar calidad y coste antes del equipo; no iniciarlo automáticamente si el presupuesto disponible o la medición impiden cumplir el acuerdo. Equilibrar el orden en repeticiones. Una pareja sigue siendo exploratoria.

**Recordatorio: revisión experta del protocolo final por el modelo más potente disponible antes de congelar y ejecutar.** Aquí no se certifica su clasificación ni capacidad efectiva. Preparación autorizada; alcance y presupuesto de ejecución pendientes de aprobación sobre artefactos listos.

## Navegación y diagnóstico de enlaces

Los cuatro archivos existen. Las URL con el dominio interno `vscode-cdn.net` proceden del renderizado del editor y no están en los Markdown. No podemos comprobar aquí el cliente WSL. Abrir con **Ctrl+P** desde la raíz:

```text
scripts/audit_intermediate.py
results/intermediate-review-data.json
results/CONCLUSIONS.md
docs/acceptance-tests.md
```

`python3 -B scripts/check_links.py` recorre Markdown versionados, enlaces relativos, referencias, imágenes HTML y anclas de títulos. Las anclas GitHub son aproximadas; no sustituye al navegador ni consulta sitios externos.

Cuatro enlaces inaccesibles permanecen en mensajes históricos inmutables. Alternativas publicadas: [código simple](../runs/astra-medium-core-v2-2-supervised-002/solution/calculator.py), [documentación simple](../runs/astra-medium-core-v2-2-supervised-002/solution/README.md), [código científico](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py), [documentación científica](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md).

## Estado

Alcance y presupuesto propuestos; sin nueva suite congelada, lanzador paralelo listo ni llamadas a modelos. Próxima entrega técnica conjunta: especificación completa, suite calibrada y transporte aislado simulado antes del punto de lanzamiento.
