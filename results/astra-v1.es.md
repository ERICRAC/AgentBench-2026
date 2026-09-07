# V1 Astra — informe completo

[Français](astra-v1.md) · [English (UK)](astra-v1.en.md) · **Español** · [Português](astra-v1.pt.md)

Los dos candidatos solo de `astra-high-001` finalizaron con verificación separada. Las V1 anteriores quedan [archivadas](ARCHIVE_V1.es.md), fuera de esta campaña.

| Indicador | Core · astra-core-v1-002 | Scientific · astra-scientific-v1-002 |
| --- | ---: | ---: |
| Primero / final / independiente | 6/6 · 6/6 · 6/6 | 9/9 · 9/9 · 9/9 |
| Duración | 100.175 s | 399.478 s |
| Entrada | 117769 | 208078 |
| Caché incluida | 96896 | 167808 |
| Salida | 2709 | 12432 |
| Razonamiento incluido | 195 | 1429 |
| Entrada + salida | 120478 | 220510 |
| Controles adicionales | — | 4/4 |

## Tratamiento y recorrido

Core separa las cuatro operaciones de la CLI y recupera errores de entrada. Supera la primera verificación sin corrección funcional; el acta conserva un error inicial de ruta.

Scientific emplea un analizador dedicado y representación aritmética posfija con límites de tamaño y profundidad. Reutiliza el análisis para muestrear, corta la curva en puntos indefinidos, serializa SVG mediante XML y conserva historial. Tras el primer 9/9, los controles propios detectaron interpolación fuera del intervalo cerca del mayor flotante. El candidato corrigió el cálculo según el signo de los extremos y conservó cuatro pruebas. El orquestador repitió la suite y esas pruebas tras el cierre.

## Protocolo, pruebas y límites

`gpt-6-astra/high`, CLI `0.153.4`, Python `3.13.5`, ventana declarada 200.000 y compactación 180.000 (`total`). Sesiones efímeras nuevas, sin consultores ni ayuda funcional humana; ninguna operación Git del candidato observada. Configuración de usuario ignorada y autenticación externa.

Los contadores JSON incluyen caché en entrada y razonamiento en salida. Las sesiones terminadas suman 340.988 tokens y 499,653 s; no es el coste completo de campaña. La duración incluye arranque/cierre CLI, no preparación, publicación ni preflight.

Algunas salidas Scientific están vacías en el JSON. El primer 9/9 se apoya en el mensaje visible y código 0; el resultado final se verificó separadamente. Configurar el cliente no mide la ventana del servidor. No se ejecutó una matriz de versiones Python ni revisión visual de navegador.

[Core PV](../runs/astra-core-v1-002/PV.md) · [Core JSON](../runs/astra-core-v1-002/run.json)

[Scientific PV](../runs/astra-scientific-v1-002/PV.md) · [Scientific JSON](../runs/astra-scientific-v1-002/run.json)

## Incidentes conservados

`astra-core-v1-001`: CLI antiguo rechazado antes del trabajo, 5,301 s, tokens no registrados. CLI actualizado y nueva tentativa.

`astra-scientific-v1-001`: interrupción por cuota tras la primera escritura, antes de verificar, 216,929 s, tokens no registrados. Código conservado sin reutilización. No puede calcularse el coste total de campaña.

[Core incident](../runs/astra-core-v1-001/run.json) · [Scientific incident](../runs/astra-scientific-v1-001/PV.md)

## Observaciones y siguiente paso

Las comparaciones históricas con runs Sol anteriores siguen archivadas, pero ya
no son el control del modelo. Una [V1 Sol con el mismo perímetro](sol-vs-astra-v1.es.md)
ejecuta ambos desafíos con el mismo CLI, prompts y parámetros: veredicto final
igual, pero +140,1 % de tiempo y +33,3 % de tokens para Sol en las dos sesiones.

El defecto posterior al 9/9 evidencia el techo de la suite. La interacción del
cargador `dataclass` permanece documentada y la suite no cambia. El preflight
V2 está terminado; el siguiente benchmark preparado es Astra V2 Core.
