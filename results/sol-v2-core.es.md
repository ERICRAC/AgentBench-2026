# V2 Sol — informe Calculadora Core

[Français](sol-v2-core.md) · [English (UK)](sol-v2-core.en.md) · **Español** · [Português](sol-v2-core.pt.md)

## Veredicto

`sol-core-v2-001` supera **6/6 grupos `unittest` y 14/14 controles
elementales** en el primer pase oficial y en la repetición independiente. El
[catálogo](../docs/acceptance-tests.es.md) describe cada control.

La calidad oficial iguala V1 Sol, pero V2 consume 4,19 veces el tiempo y 3,54
veces los tokens. Según Pareto, **V1 domina V2 en Core**: la misma conformidad
medida con menor coste. Este reto pequeño no demuestra ganancia multiagente.

| Medida | V1 solo | V2 multiagente | Diferencia V2 |
| --- | ---: | ---: | ---: |
| Primero / independiente | 6/6 grupos · 14/14 controles | 6/6 · 14/14 | empate |
| Tiempo | 189,964 s | 796,534 s | ×4,19 · +319,3 % |
| Entrada + salida | 158 101 | 559 088 | ×3,54 · +253,6 % |
| Correcciones tras verificar | 0 | 0 | empate |

Siete sesiones efímeras para cuatro roles suman 898,229 segundos-agente. SA-01
y SA-02 producen análisis ciegos y una contradicción cada uno; SA-03 revisa la
primera solución; solo MAIN escribe y verifica. Se respetan todos los límites y
se publican 4 347 palabras visibles, 3 507 de consultores.

El desacuerdo útil trata la gramática CLI y converge en tres elementos
separados por espacios. MAIN conserva 19 de 23 recomendaciones iniciales.
SA-03 formula 3 defectos, 6 riesgos y 6 preferencias; MAIN conserva 10 de 15
puntos y realiza tres cambios antes del verificador. La suite oficial no mide
esa robustez adicional.

SA-03 también cuestiona `DECISIONS.md` como tercer entregable; MAIN lo conserva
porque V2 exige una tabla de arbitraje. El verificador lo acepta sin resolver la
ambigüedad textual. Una sola observación no permite generalizar.

[Acta literal filtrada](../runs/sol-core-v2-001/PV.md) · [Traza JSON](../runs/sol-core-v2-001/trace.json) · [Metadatos](../runs/sol-core-v2-001/run.json)
