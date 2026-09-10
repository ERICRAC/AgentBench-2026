# Astra medio — balance V1/V2 y ejecución científica V1

[Français](astra-medium-v1-v2.md) · [English (UK)](astra-medium-v1-v2.en.md) · **Español** · [Português](astra-medium-v1-v2.pt.md)

## Conclusión en un minuto

**En ambas calculadoras, V1 solo alcanza la misma puntuación oficial que V2 consultiva, con menos tiempo y tokens.** En total, V2 utiliza **×3,56 el tiempo y ×4,49 los tokens**. Estas medidas no muestran una inversión favorable al colectivo.

Igual puntuación no significa igual robustez. La revisión científica V2 corrigió límites de longitud/profundidad que la nueva V1 conserva. La coordinación tiene una contribución técnica observable, pero los tests oficiales actuales no valoran ese beneficio. No significa que los consultores sean inútiles.

## Mismo modelo y esfuerzo solicitados

gpt-6-astra / medium; contexto 200000, compactación 180000, alcance total. V1 = un desarrollador en una sesión. V2 = un escritor, tres consultores, siete sesiones por desafío; no desarrolladores paralelos.

| Calculadora | Puntuación final V1 = V2 | Tiempo V1 | Tiempo V2 | V2/V1 | Tokens V1 | Tokens V2 | V2/V1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Simple | 6/6 grupos · 14/14 controles | 98.572 s | 375.169 s | ×3,81 | 98496 | 408616 | ×4,15 |
| Científica | 9/9 grupos · 57/57 controles | 188.560 s | 648.008 s | ×3,44 | 119388 | 570382 | ×4,78 |
| Ambos desafíos | 15/15 grupos · 71/71 controles | 287.132 s | 1023.177 s | ×3,56 | 217884 | 978998 | ×4,49 |

Todos los primeros pases oficiales tienen éxito; en V2 siguen a la crítica obligatoria. Totales: suma de estos dos runs terminados por organización, no de toda la campaña ni suscripción. Tokens = entrada + salida, incluyendo caché y razonamiento. V2 científica añade 459,448 s y 450 994 tokens frente a V1.

De simple a científica, la relación temporal baja ligeramente (3,81 → 3,44), pero la de tokens sube (4,15 → 4,78). La dificultad adicional no hace rentable esta organización según los indicadores oficiales. Dos ejercicios y una observación por celda no permiten extrapolar un umbral.

## Nueva V1 científica — tratamiento

Intento astra-medium-scientific-v1-001, autorizado tras publicar Core. Directorio nuevo, prompt histórico, ninguna solución anterior leída por el candidato, ningún consultor ni consejo V2. Lee el contrato, construye un analizador recursivo restringido, reutiliza el árbol para muestrear, exporta SVG escapado y segmentado, añade CLI, historial y documentación.

Un control manual de CLI precede a la única ejecución oficial: potencias 512, -4 y 0,25; recuperación tras división por cero; historial solo de éxitos. **9/9, confirmados independientemente 9/9, sin corrección funcional posterior.** Código intacto en aaa83de. Archivos: 295 líneas Python, README 83, acta candidata 51; no es una medida de mantenibilidad.

Duración: 188,560 s. Entrada: 113 746, caché incluida 98 944; salida: 5 642, razonamiento incluido 164. Total: 119 388. Cinco mensajes visibles, seis comandos terminados, sin delegación. rg no encuentra archivos en el directorio vacío; acta extra además de dos entregables; redirecciones shell en lugar de apply_patch: hechos conservados, no penalizados por el verificador.

## Lista científica — nueve grupos, 57 controles

- [x] S01 · Entregables y documentación — 7 controles.
- [x] S02 · Biblioteca estándar y sin ejecución dinámica prohibida — 2.
- [x] S03 · Prioridades, paréntesis, potencias y signos — 10.
- [x] S04 · Funciones, constantes y notación científica — 6.
- [x] S05 · Variable x y nombres prohibidos — 5.
- [x] S06 · Sintaxis, dominios y división por cero — 6.
- [x] S07 · Muestreo, extremos y discontinuidades — 8.
- [x] S08 · SVG válido, ejes, curva, título escapado y contenido inerte — 7.
- [x] S09 · CLI, curvas, historial, recuperación y salida — 6.

[Cada caso y resultado esperado](../docs/acceptance-tests.es.md) · [Seis grupos simples](astra-medium-v1-core.es.md). Los controles exploratorios y candidatos no se añaden a los 71 oficiales.

## Aportación del colectivo pese al sobrecoste

En simple, V2 precisó principalmente documentación, sin cambio funcional. En científica, **SA-03 = subagente 3, revisor crítico**: MAIN eliminó límites de longitud/recursión, protegió la salida del terminal y gestionó canales CLI fallidos. Las revisiones cruzadas corrigieron propuestas sobre composición de funciones y expresiones indefinidas en todas partes. [Análisis V2 y pruebas](astra-medium-v2.es.md).

Tras completar V1, dos sondas exploratorias del orquestador confirman sus restricciones: `"1" + " " * 10000` debería dar matemáticamente 1 y `"+".join(["1"] * 1500)` debería dar 1500; ambas producen ValueError. Resultados en la traza. **Sondas posteriores, solo V1, no prerregistradas y fuera de puntuación.** La prueba V2 procede de su informe y controles registrados; no hay repetición V2 idéntica aquí. Revelan una limitación de la puntuación, no una estimación exhaustiva de superioridad V2.

## Límites y próxima decisión

Una observación por celda; V1 posterior a V2; mismo alias sin garantía de snapshot del servidor; carga/caché variables. Tiempo V1 incluye inicio/cierre CLI, V2 también el relé; preparación, verificación posterior y publicación excluidas. El contexto configurado no es un límite de consumo total, ni su aplicación queda demostrada. Coste monetario fiable no registrado.

La referencia Astra medio V1/V2 ya cubre ambos ejercicios. Propuesta: prerregistrar V2.2 (pareja ligera), después V2.1 (desarrollo paralelo), con presupuestos, repeticiones y robustez explícitos. El paralelismo real requiere un desafío divisible. Sin otro lanzamiento ni cambio de gobernanza aquí. [Conclusión central](CONCLUSIONS.es.md).

## Auditoría — resumen y pruebas

[Acta científica: roles, secuencia y textos visibles](../runs/astra-medium-scientific-v1-001/PV.md) · [Traza y sondas](../runs/astra-medium-scientific-v1-001/trace.json) · [Metadatos](../runs/astra-medium-scientific-v1-001/run.json) · [Código](../runs/astra-medium-scientific-v1-001/solution/scientific_calculator.py) · [README candidato](../runs/astra-medium-scientific-v1-001/solution/README.md)

[V1 simple](astra-medium-v1-core.es.md) · [V2 y actas](astra-medium-v2.es.md) · [Preflight histórico](astra-medium-v1-preflight.es.md) · [Índice](README.es.md) · [Proyecto](../README.es.md)

## Verificación de la publicación

Controles de mantenimiento separados del benchmark: 12 tests unitarios sin llamadas a modelos; enlaces de 152 documentos editoriales y 64 huellas históricas; reproducibilidad de cinco resúmenes V2; linter Markdown y git diff --check. Auditoría de 11 huellas del intento y contadores frente a la captura privada. Soluciones anteriores, desafíos, scripts, prompts y gobernanza intactos. Eliminadas cuatro líneas vacías duplicadas detectadas por el linter; sin corregir al candidato.
