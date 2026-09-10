# El run en 2 minutos — astra-medium-scientific-v2-001

[Français](astra-medium-scientific-v2-001.md) · [English (UK)](astra-medium-scientific-v2-001.en.md) · **Español** · [Português](astra-medium-scientific-v2-001.pt.md)

Esta capa precede al acta detallada en la lectura; el acta original no cambia. Los datos ausentes no equivalen a cero.

Calculadora científica · codex-multi · completed

## Hechos observados

| | |
| --- | --- |
| Modelo / esfuerzo | gpt-6-astra / medium |
| Primera verificación oficial | 9/9 groups; 57/57 checks |
| Resultado final del candidato | 9/9 groups; 57/57 checks |
| Veredicto independiente | 9/9 groups; 57/57 checks |
| Duración total (s) | 648.008 |
| Tokens entrada + salida | 570382 |
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
| sa01_initial | SA-01 | P1 | — | — | No | 55.127 | 16718 | No registrado | No registrado |
| sa02_initial | SA-02 | P1 | — | — | No | 54.314 | 16698 | No registrado | No registrado |
| sa01_cross | SA-01 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.439 | 17845 | No registrado | No registrado |
| sa02_cross | SA-02 | P2 | sa01_initial, sa02_initial | sa01_initial, sa02_initial | No | 28.315 | 17903 | No registrado | No registrado |
| main_first | MAIN | — | sa01_initial, sa02_initial, sa01_cross, sa02_cross | sa01_initial, sa02_initial, sa01_cross, sa02_cross | Sí | 311.551 | 198505 | No registrado | No registrado |
| sa03_critic | SA-03 | — | main_first | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first | No | 48.689 | 27934 | No registrado | No registrado |
| main_final | MAIN | — | sa03_critic | sa01_initial, sa02_initial, sa01_cross, sa02_cross, main_first, sa03_critic | Sí | 204.160 | 274779 | No registrado | No registrado |

Las invocaciones tienen un origen distinto de la duración total histórica; véase la guía de instrumentación.

</details>

## Análisis interpretativo

[CONTESTÉ → RETENU] Las revisiones cruzadas corrigen los consejos sobre sin(cos(x)) y el muestreo de sqrt(-1). [IMPACT] SA-03 señala límites de longitud/profundidad → RELAY transmite MSG-006 → MAIN acepta → elimina el límite y sustituye la recursión por una pila explícita → pasa el test candidato de expresiones largas. Otros dos grupos corrigen terminal y canales CLI. [REJETÉ] Límites arbitrarios de muestras y escritura atómica no exigidos. Diez aceptados, dos rechazados, uno no verificable en el dossier recibido. El script de 131 aserciones iniciales está en la traza de MAIN, no en el dossier de SA-03: no falta globalmente. Véanse arbitraje final y pruebas finales en DECISIONS. Aporte observable, sin mejora aislada de puntuación: el primer verificador viene después. Novedad absoluta y [BRUIT] no establecidos.

## Pruebas y próximos pasos

[PV / verbatim](../../runs/astra-medium-scientific-v2-001/PV.md) · [trace.json](../../runs/astra-medium-scientific-v2-001/trace.json) · [run.json](../../runs/astra-medium-scientific-v2-001/run.json) · [Decisiones](../../runs/astra-medium-scientific-v2-001/solution/DECISIONS.md)

[Guía de lectura](../../docs/reading-guide.es.md) · [Tests](../../docs/acceptance-tests.es.md) · [Conclusiones](../CONCLUSIONS.es.md) · [Index](index.es.md)
