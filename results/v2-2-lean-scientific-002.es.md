# V2.2 científica reducida — ensayo 002 terminado

[Français](v2-2-lean-scientific-002.md) · [English (UK)](v2-2-lean-scientific-002.en.md) · [Español](v2-2-lean-scientific-002.es.md) · [Português](v2-2-lean-scientific-002.pt.md)

**Ensayo científico 002 aprobado: 9/9 grupos, 57/57 controles, 141 794 tokens, 207,630 s.** Sin cambios tras revisión. La pareja sigue siendo más costosa que el agente solo científico histórico; comparación exploratoria.

## Resultado y desarrollo

Tres sesiones Astra medio: MAIN implementa y ejecuta 78 controles locales, REV-01 revisa estáticamente sin defecto confirmado, MAIN final arbitra y supera el verificador oficial a la primera. El orquestador confirma independientemente 9 grupos / 57 controles sobre versiones inicial y final idénticas. Los 78 controles del candidato no son pruebas independientes adicionales.

Se transmitió la confirmación explícita: OBS-002 no se repitió. Sin interrupción por cuota ni reintento. Sobres de 5 023, 21 226 y 22 569 caracteres, dentro de 24 000. Informes finales dentro de sus límites.

## Coste y eficiencia

| Condición | Tokens entrada + salida | Duración (s) | Resultado |
| --- | ---: | ---: | --- |
| Solo V1 histórico | 119 388 | 188,560 | 9/9 · 57/57 |
| V2 histórico | 570 382 | 648,008 | 9/9 · 57/57 |
| Pareja reducida 002 | 141 794 | 207,630 | 9/9 · 57/57 |

Frente al solo histórico: **+18,8 % de tokens, +10,1 % de tiempo**, sin mejora de resultado ni correcciones. Frente a V2 histórico: **−75,1 % de tokens, −68,0 % de tiempo**. La pareja reduce mucho el sobrecoste colectivo, pero no supera al solo en este caso.

Entrada: 134 416, con 77 440 en caché; salida: 7 378, con 397 de razonamiento. Subconjuntos no sumados dos veces. No se alcanzó el umbral entre sesiones de 150 000; no hay techo estricto garantizado. Tiempo total 207,630 s; suma de sesiones 207,620 s. Cuota disponible y costes de orquestación, preparación y publicación no registrados.

Ensayo 001 interrumpido separado: 11 968 tokens, 12,811 s. Subtotal de los ensayos científicos reducidos 001+002 únicamente: **153 762 tokens, 220,441 s**. No es el coste de toda la campaña.

## Aportación y límites de la revisión

REV-01 confirma la estructura y distingue los 78 controles declarados de las pruebas no disponibles. Señala singularidades entre muestras, límite ya documentado. MAIN final acepta tres observaciones y marca una como no verificable porque no recibió las salidas. Ningún defecto confirmado, corrección ni ganancia de calidad demostrada; revisión adicional explícita cuya prevención de errores no se mide aquí.

## Límites y siguiente paso

Nueva campaña astra-medium-lean-003: mismo modelo solicitado y esfuerzo, pero prompts, transmisión, entorno y caché distintos. Un ensayo por condición; revisión exacta del servidor y versión CLI al lanzamiento no registradas. No se pueden atribuir diferencias solo a la organización ni considerar simple y científica una pareja estrictamente homogénea.

Sin lanzamiento automático. Recomendación: analizar antes de gastar más. El umbral de rentabilidad colectiva sigue desconocido; un desafío paralelizable o un control solo contemporáneo necesitarían protocolo y presupuesto aprobados por separado.

## Artefacts

- [PV / messages / metrics](../runs/astra-medium-scientific-v2-2-lean-002/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-002/run.json) · [Prompts](../runs/astra-medium-scientific-v2-2-lean-002/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-002/trace.json).
- [Solution](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md) · [Code](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py) · [Checks](../runs/astra-medium-scientific-v2-2-lean-002/verifications.json).
- [V1/V2](astra-medium-v1-v2.es.md) · [OBS-002 / 001](v2-2-lean-scientific-001.es.md).
- [57 checks](../docs/acceptance-tests.es.md) · [Manifest](../governance/v2-2-lean-scientific-002.json).

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/astra-medium-scientific-v2-2-lean-002/solution
```
