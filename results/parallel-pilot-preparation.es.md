# Preparación técnica — piloto V1 / V2.1 ligera

[Français](parallel-pilot-preparation.md) · [English (UK)](parallel-pilot-preparation.en.md) · [Español](parallel-pilot-preparation.es.md) · [Português](parallel-pilot-preparation.pt.md)

**Preparación sin modelos entregada; campaña no congelada y ningún candidato ejecutado.**
La pregunta sigue siendo si el desarrollo paralelo reduce el plazo con calidad comparable, incluida la integración.

## Entregables

- [Especificación completa](../challenges/modular-calculator-draft/SPEC.md): cuatro archivos, sintaxis científica, límites explícitos, curvas, lotes, errores CLI y documentación. Instrucción canónica en francés.
- [Catálogo detallado de diez grupos](../challenges/modular-calculator-draft/catalogue.json) y [suite independiente](../challenges/modular-calculator-draft/tests/test_acceptance.py). M01 restricciones; M02 cálculo; M03 funciones; M04 errores/límites; M05 muestreo; M06 SVG; M07 lotes; M08 errores CLI; M09 integración; M10 documentación.
- [Calibración](../tests/test_modular_acceptance.py): dos variantes sintéticas admitidas y diez defectos inyectados detectados, uno por grupo. Las fixtures son herramientas de mantenimiento, nunca referencias entregadas a candidatos.
- [Simulación paralela](../scripts/preflight_parallel_pilot.py): dos procesos ficticios aislados, barrera de inicio, ensamblaje sin cambios e integrador ficticio.
- [Pruebas, duraciones relativas y huellas](parallel-pilot-preparation.json). Siete tests de mantenimiento aprobados; doce ejecuciones de la suite durante la calibración (dos variantes y diez mutantes).

## Qué demuestran los controles

El cargador admite imports Python normales, una dataclass e imports entre módulos. Pasan las dos representaciones autorizadas, polyline y path M/L. Cada mutación falla en el grupo previsto. Es calibración, no prueba de exhaustividad.

DEV-A y DEV-B leen su contrato pero no pueden modificarlo ni leer/escribir el canario del otro, tampoco mediante enlaces simbólicos. Seis controles por desarrollador pasan. Ambos procesos están listos antes de liberarlos; INT empieza después de recoger ambos resultados. Las huellas siguen el ensamblaje y atribuyen una corrección ficticia a INT.

El aislamiento exterior bloqueó el primer intento. Una ejecución local elevada autorizada pasó conservando el confinamiento de los hijos. Sin credenciales ni llamadas a modelos. Los tiempos finales son observaciones del padre, no salidas exactas del núcleo ni ganancias colaborativas medidas.

## Límites y próxima entrega

M10 comprueba nombres de API, límites y docstrings; la calidad explicativa y ejecución de ejemplos no se evalúan automáticamente todavía. El análisis AST no defiende contra candidatos maliciosos. El catálogo publica límites de cobertura y no afirma tener pruebas ocultas.

El simulador no acepta modelos ni ofrece modo real. Antes de ejecutar: transporte autenticado con dos escritores, mensajes y contadores reales, validación de todas las herramientas, mandatos finales y manifiesto congelado. La simulación aislada carece de credenciales y no es un lanzador Codex listo.

El [protocolo propuesto](../docs/parallel-pilot.es.md) mantiene Astra medio, solo seguido de equipo y umbral entre sesiones de 150 000 tokens por organización: propuesta, no techo estricto. Solo segmentado queda como control posterior separado. Revisar antes del cierre; **recordatorio solicitado: utilizar el modelo más potente disponible en ese punto**. Esta preparación no implica autorización de ejecución ni presupuesto nuevo.

## Reproducción sin modelos

```bash
python3 -B -m unittest tests/test_modular_acceptance.py tests/test_parallel_pilot.py
python3 -B scripts/preflight_parallel_pilot.py --simulate
```

La segunda orden necesita espacios de nombres Linux autorizados para bubblewrap. Un rechazo se declara bloqueado, nunca aprobado.
