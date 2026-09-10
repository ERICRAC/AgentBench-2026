# El run en 2 minutos — astra-medium-core-v2-001

[Français](astra-medium-core-v2-001.md) · [English (UK)](astra-medium-core-v2-001.en.md) · **Español** · [Português](astra-medium-core-v2-001.pt.md)

Esta capa precede al acta detallada en la lectura; el acta original no cambia. Los datos ausentes no equivalen a cero.

Calculadora simple · codex-multi · completed

## Hechos observados

| | |
| --- | --- |
| Modelo / esfuerzo | gpt-6-astra / medium |
| Primera verificación oficial | 6/6 groups; 14/14 checks |
| Resultado final del candidato | 6/6 groups; 14/14 checks |
| Veredicto independiente | 6/6 groups; 14/14 checks |
| Duración total (s) | 375.169 |
| Tokens entrada + salida | 408616 |
| Sesiones registradas (no llamadas API) | 7 |
| Correcciones funcionales después del primer pase | No registrado |

La caché está incluida en la entrada; el razonamiento, en la salida. No sumarlos otra vez. Una sesión CLI puede contener varias llamadas al modelo. La primera verificación oficial ocurre después de la crítica.

## Equipo y secuencia

MAIN: árbitro y único escritor; SA-01: requisitos/seguridad; SA-02: arquitectura/testabilidad; SA-03: revisión crítica. RELAY es el supervisor mecánico externo, no un candidato.

P1: análisis independientes y barrera. P2: revisiones cruzadas y barrera. Después MAIN → SA-03 → MAIN y verificador. El paralelismo histórico está especificado, no es solapamiento medido.

<details>
<summary>Sesiones registradas (no llamadas API)</summary>

| Sesión | Rol | Grupo paralelo especificado | Depende de | receives_from | Escritor | Duración CLI (s) | Tokens entrada + salida | Inicio / fin medidos (s) | Duración de invocación medida (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | SA-01 | P1 | — | — | No | 51.054 | 15919 | No registrado | No registrado |
| sa02_initial | SA-02 | P1 | — | — | No | 47.764 | 15812 | No registrado | No registrado |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.390 | 17485 | No registrado | No registrado |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.140 | 17483 | No registrado | No registrado |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sí | 146.611 | 144301 | No registrado | No registrado |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 37.223 | 22386 | No registrado | No registrado |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sí | 111.857 | 175230 | No registrado | No registrado |

Las invocaciones tienen un origen distinto de la duración total histórica; véase la guía de instrumentación.

</details>

## Análisis interpretativo

[CONTESTÉ → RETENU] SA-01 retira su preferencia por números finitos durante la revisión cruzada (MSG-003/004); MAIN decide 21 puntos antes de programar. [CONFIRMÉ] SA-03 señala límites numéricos; MAIN los comprueba y aclara el README sin modificar calculator.py. Once decisiones finales, ninguna corrección funcional. Ninguna interacción demuestra un cambio de puntuación. Aceptar un consejo no prueba que MAIN habría fallado solo; no se asigna [BRUIT] automáticamente. Véanse DECISIONS, tabla final y puntos 9–12, y PV MSG-006/007.

## Pruebas y próximos pasos

[PV / verbatim](../../runs/astra-medium-core-v2-001/PV.md) · [trace.json](../../runs/astra-medium-core-v2-001/trace.json) · [run.json](../../runs/astra-medium-core-v2-001/run.json) · [Decisiones](../../runs/astra-medium-core-v2-001/solution/DECISIONS.md)

[Guía de lectura](../../docs/reading-guide.es.md) · [Tests](../../docs/acceptance-tests.es.md) · [Conclusiones](../CONCLUSIONS.es.md) · [Index](index.es.md)
