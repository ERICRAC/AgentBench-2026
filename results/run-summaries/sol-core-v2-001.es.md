# El run en 2 minutos — sol-core-v2-001

[Français](sol-core-v2-001.md) · [English (UK)](sol-core-v2-001.en.md) · **Español** · [Português](sol-core-v2-001.pt.md)

Esta capa precede al acta detallada en la lectura; el acta original no cambia. Los datos ausentes no equivalen a cero.

Calculadora simple · codex-multi · completed

## Hechos observados

| | |
| --- | --- |
| Modelo / esfuerzo | gpt-5.6-sol / high |
| Primera verificación oficial | 6/6 unittest groups; 14/14 elementary checks |
| Resultado final del candidato | 6/6 unittest groups; 14/14 elementary checks |
| Veredicto independiente | 6/6 unittest groups; 14/14 elementary checks |
| Duración total (s) | 796.534 |
| Tokens entrada + salida | 559088 |
| Sesiones registradas (no llamadas API) | 7 |
| Correcciones funcionales después del primer pase | 0 |

La caché está incluida en la entrada; el razonamiento, en la salida. No sumarlos otra vez. Una sesión CLI puede contener varias llamadas al modelo. La primera verificación oficial ocurre después de la crítica.

## Equipo y secuencia

MAIN: árbitro y único escritor; SA-01: requisitos/seguridad; SA-02: arquitectura/testabilidad; SA-03: revisión crítica. RELAY es el supervisor mecánico externo, no un candidato.

P1: análisis independientes y barrera. P2: revisiones cruzadas y barrera. Después MAIN → SA-03 → MAIN y verificador. El paralelismo histórico está especificado, no es solapamiento medido.

<details>
<summary>Sesiones registradas (no llamadas API)</summary>

| Sesión | Rol | Grupo paralelo especificado | Depende de | receives_from | Escritor | Duración CLI (s) | Tokens entrada + salida | Inicio / fin medidos (s) | Duración de invocación medida (s) |
| --- | --- | --- | --- | --- | --- | ---: | ---: | --- | ---: |
| sa01_initial | No registrado | P1 | — | — | No | 62.931 | 15125 | No registrado | No registrado |
| sa02_initial | No registrado | P1 | — | — | No | 72.214 | 15401 | No registrado | No registrado |
| sa01_cross | No registrado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 48.026 | 17385 | No registrado | No registrado |
| sa02_cross | No registrado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 38.788 | 17142 | No registrado | No registrado |
| main_first | No registrado | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sí | 236.374 | 159299 | No registrado | No registrado |
| sa03_critic | No registrado | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 118.418 | 23556 | No registrado | No registrado |
| main_final | No registrado | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sí | 321.478 | 311180 | No registrado | No registrado |

Las invocaciones tienen un origen distinto de la duración total histórica; véase la guía de instrumentación.

</details>

## Análisis interpretativo

[CONTESTÉ → RETENU] Acuerdo sobre tres elementos separados por espacios y rechazo de 2+3. MAIN decide 23 recomendaciones (19 aceptadas, 4 rechazadas). [IMPACT] Tras SA-03: ejemplo de importación corregido, Ctrl-C en todo el bucle, anotación compatible con Python antiguo. [REJETÉ] MAIN conserva DECISIONS pese a la objeción de SA-03, siguiendo el protocolo. Diez puntos finales aceptados y cinco rechazados. Véase [informe Core Sol](../sol-v2-core.es.md), DECISIONS y MSG-006/007. Sin mejora del resultado oficial ni prueba de que MAIN fallaría solo. Consejos a menudo redundantes, sin cuantificación fiable de [BRUIT].

## Pruebas y próximos pasos

[PV / verbatim](../../runs/sol-core-v2-001/PV.md) · [trace.json](../../runs/sol-core-v2-001/trace.json) · [run.json](../../runs/sol-core-v2-001/run.json) · [Decisiones](../../runs/sol-core-v2-001/solution/DECISIONS.md)

[Guía de lectura](../../docs/reading-guide.es.md) · [Tests](../../docs/acceptance-tests.es.md) · [Conclusiones](../CONCLUSIONS.es.md) · [Index](index.es.md)
