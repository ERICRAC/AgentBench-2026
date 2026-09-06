# Política de registro público

[Français](LOGGING.md) · [English (UK)](LOGGING.en.md) · **Español** · [Português](LOGGING.pt.md)

El registro permite auditar el proceso sin exponer conversaciones completas.
Cada entrada recibe un número secuencial estable, sin fecha ni hora.

## Contenido conservado

- resumen de la petición humana;
- resumen de la respuesta o acción del agente;
- roles participantes;
- decisiones y motivos útiles para el experimento;
- archivos afectados y resultados de controles;
- errores, correcciones e intervenciones humanas relevantes;
- métricas disponibles, calificadas si son aproximadas.

## Contenido excluido

- prompts o respuestas sin filtrar con datos personales;
- secretos, tokens, frases de contraseña, claves privadas y rutas de autenticación;
- detalles de cuenta irrelevantes;
- razonamiento interno o citas innecesarias;
- marcas de tiempo en el historial público.

Un Markdown público puede conservar una fecha o duración del protocolo, pero no
el horario de trabajo del autor. Un dato oculto se omite o se marca como no
publicado; nunca se sustituye por una hora inventada.

## Forma de una entrada

```markdown
## Intercambio 000

**Petición resumida** — …

**Respuesta resumida** — …

**Traza útil** — actores, decisiones, archivos y controles.
```

Los metadatos de un run pueden conservar fechas y duraciones exigidas por el
protocolo. Tras cada intercambio que cambie el repositorio, se añade la entrada
antes del commit. El cuerpo del commit resume objetivo, cambios y controles, y
se publica salvo orden contraria explícita.

## Acta de cada run

Cada run publicado tiene un `PV.md` separado del historial general. Identifica
patrocinador, orquestador experimental, agente candidato, consultores y
verificador, y numera mandatos, consejos, respuestas, decisiones, correcciones
y veredictos observables.

El acta es una síntesis probatoria, no una transcripción completa. Relaciona
decisiones con archivos, pruebas y métricas, señala salidas no capturadas y
excluye razonamiento interno bruto. Desde V2, cada recomendación indica su rol
y la decisión motivada del orquestador: aceptada, rechazada o no verificable.

Desde V2, los **mensajes visibles entre agentes** se conservan literalmente
tras filtrar secretos, según [`PV_TEMPLATE.es.md`](PV_TEMPLATE.es.md).
