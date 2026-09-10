# El run en 2 minutos — astra-core-v2-001

[Français](astra-core-v2-001.md) · [English (UK)](astra-core-v2-001.en.md) · **Español** · [Português](astra-core-v2-001.pt.md)

Esta capa precede al acta detallada en la lectura; el acta original no cambia. Los datos ausentes no equivalen a cero.

Calculadora simple · codex-multi · completed

## Hechos observados

| | |
| --- | --- |
| Modelo / esfuerzo | gpt-6-astra / high |
| Primera verificación oficial | 6/6 unittest groups; 14/14 elementary checks |
| Resultado final del candidato | 6/6 unittest groups; 14/14 elementary checks |
| Veredicto independiente | 6/6 unittest groups; 14/14 elementary checks |
| Duración total (s) | 700.994 |
| Tokens entrada + salida | 572168 |
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
| sa01_initial | No registrado | P1 | — | — | No | 48.093 | 15602 | No registrado | No registrado |
| sa02_initial | No registrado | P1 | — | — | No | 46.555 | 15491 | No registrado | No registrado |
| sa01_cross | No registrado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 27.954 | 16949 | No registrado | No registrado |
| sa02_cross | No registrado | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 33.817 | 16980 | No registrado | No registrado |
| main_first | No registrado | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sí | 393.690 | 213048 | No registrado | No registrado |
| sa03_critic | No registrado | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 44.659 | 27115 | No registrado | No registrado |
| main_final | No registrado | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sí | 180.712 | 266983 | No registrado | No registrado |

Las invocaciones tienen un origen distinto de la duración total histórica; véase la guía de instrumentación.

</details>

## Análisis interpretativo

[CONFIRMÉ] Consenso y aclaración del contrato: 17 decisiones iniciales. Tras MSG-006, MAIN decide 14 puntos (7 aceptados, 3 rechazados, 4 no verificables) y solo cambia documentación. Ningún defecto funcional confirmado ni interacción que cambie la puntuación. Repetir consultas en DECISIONS amplía los prompts posteriores: coste observable, no prueba de inutilidad de cada repetición. Véase el [informe Core elevado](../astra-v2-core.es.md), DECISIONS y MSG-007. Sin forzar [NOUVEAU] o [BRUIT].

## Pruebas y próximos pasos

[PV / verbatim](../../runs/astra-core-v2-001/PV.md) · [trace.json](../../runs/astra-core-v2-001/trace.json) · [run.json](../../runs/astra-core-v2-001/run.json) · [Decisiones](../../runs/astra-core-v2-001/solution/DECISIONS.md)

[Guía de lectura](../../docs/reading-guide.es.md) · [Tests](../../docs/acceptance-tests.es.md) · [Conclusiones](../CONCLUSIONS.es.md) · [Index](index.es.md)
