# Instrumentación y publicación de resúmenes

**Español** · [Français](observability.md) · [English (UK)](observability.en.md) · [Português](observability.pt.md)

[Guía y diagrama V2](reading-guide.es.md) · [Resúmenes](../results/run-summaries/index.es.md) · [Auditoría](documentation-audit.es.md)

## Alcance

Mantenimiento fuera de runs. Ningún benchmark relanzado ni solución histórica editada. [run_v2.py](../scripts/run_v2.py), publisher histórico, prompts, permisos, roles, barreras y criterios intactos. El diagrama explica el protocolo congelado; no crea orquestación nueva.

[run_v2_observed.py](../scripts/run_v2_observed.py) llama al lanzador existente y envuelve solo run_session. Activación **opcional**, declarada y prerregistrada antes de la próxima campaña. Las escrituras de medición añaden un pequeño coste no cuantificado; no afirmar tiempos idénticos a runs antiguos. Tests de sesiones falsas no validan llamadas reales futuras.

## Esquema genérico

[observe_sessions.py](../scripts/observe_sessions.py) no planifica trabajo. Acepta N sesiones, roles y grupos. Solo v2_topology describe V2 congelada; V2.x/V3 requiere su propio grafo aprobado.

| Campo | Naturaleza y definición |
| --- | --- |
| session_id, role | Identidad canónica, no nombre de modelo. |
| parallel_group | Grupo concurrente especificado; null para fases secuenciales. |
| depends_on | Sesiones que deben terminar antes del inicio; barreras especificadas. |
| receives_from | Identificadores de sesiones fuente de textos o artefactos, no prueba de adopción. Desafío/mandato externo explicados en guía. |
| writes_solution | Permiso especificado, no prueba de escritura efectiva. |
| started_at_seconds, ended_at_seconds | Medidas monotónicas relativas a entrada del wrapper, antes de preparar el lanzador; nunca horas civiles. |
| duration_seconds en observation | Fin menos inicio de toda invocación: configuración, CLI, captura y análisis de eventos; excluye escritura de observación. |
| duration_seconds histórico | Medida CLI original conservada, no sustituida. |
| outcome | returned o failed, no veredicto de aceptación. |

El origen del wrapper difiere del de wall_duration_seconds histórico. No restar entre referencias. Solo intervalos medidos superpuestos prueban solapamiento. Consultas históricas tienen duración, no inicio/fin: ninguna cronología exacta inventada.

## Flujo futuro — solo tras autorizar un run

Prerregistrar primero directorio nuevo, desafío y configuraciones del protocolo aprobado. NEW-RUN es un marcador, no una tentativa creada aquí:

```bash
python3 -B scripts/run_v2_observed.py --run runs/NEW-RUN --challenge calculator
```

El directorio privado anunciado contiene observations.json, actualizado al terminar cada sesión, incluido fallo. Una parada abrupta puede dejar sesiones ausentes: no equivalen a cero. El observador no añade prompts, errores textuales, razonamiento privado ni rutas absolutas.

Tras revisar capturas y publicar normalmente con publish_v2.py, enriquecer una **copia nueva**:

```bash
python3 -B scripts/attach_observations.py --trace runs/NEW-RUN/trace.json --observations /tmp/CAPTURE/observations.json --output runs/NEW-RUN/trace-observed.json
```

La fusión rechaza destinos existentes, identificadores ausentes/duplicados, roles incoherentes, valores no finitos y barreras incumplidas. Conserva métricas originales y exporta campos permitidos explícitos. Capturas parciales requieren informe de interrupción; nunca publicar capturas privadas en bloque. El filtro histórico no detecta todos los secretos: revisión previa obligatoria.

En metadatos del run **futuro**, referenciar trace-observed.json y hash, wrapper, observador, adaptador, sus hashes y lanzador histórico. Nunca alterar metadatos ya publicados. Publisher original sigue disponible; enriquecimiento y resumen fuera del candidato.

## Generación editorial

```bash
python3 -B scripts/summarize_runs.py
python3 -B scripts/summarize_runs.py --check
python3 -B -m unittest discover -s tests -v
python3 -B scripts/check_documentation.py
markdownlint '**/*.md'
```

Primera llamada: regenera cinco portadas V2 e índice en cuatro idiomas. Hechos: run.json/trace.json; análisis revisado manualmente: [run-interpretations.json](run-interpretations.json). Editar fuente, no páginas generadas. Ausentes siguen ausentes; caché/razonamiento no se suman dos veces.

Topología futura: run.json con run_id, challenge, mode, status, modelo/esfuerzo, verification, usage y trace; trace contiene roles y sessions con phase o session_id, role, contadores y observation opcional. Claves de verificación como en archivos históricos. Admite roles locales y fases desconocidas sin inventar V2.

```bash
python3 -B scripts/summarize_runs.py --run runs/NEW-RUN --interpretation /tmp/interpretation-reviewed.json
```

JSON editorial con fr/en/es/pt; sin texto, interpretación no registrada. Salida en results/run-summaries, nunca runs/. Añadir futura portada a un índice apropiado: el actual lista solo cinco V2 completas. Código genérico no aprueba protocolo V3.

## Verificaciones y límites

Tests: argumentos/retornos intactos, fallos conservados, cinco roles paralelos, igualdad de siete prompts/argumentos, barreras, tiempos simulados, contadores ausentes, rechazo de sobrescritura, rol local y generación reproducible. No miden latencia de red ni consumo futuro del modelo.

[Verificaciones ejecutadas y límites de renderizado](documentation-audit.es.md). Validación real pendiente de un run autorizado explícitamente.
