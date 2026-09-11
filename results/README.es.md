# Resultados

[Français](README.md) · [English (UK)](README.en.md) · **Español** · [Português](README.pt.md)

**V2.2: ejecutor simulado y preflight estático correctos, sin llamadas a modelos.** 26 tests nuevos, 38 en total; modo real bloqueado, decisiones y aislamiento pendientes antes de congelar. [Preflight y lista](v2-2-preflight.es.md)

[Cinco runs V2, dos minutos cada uno](run-summaries/index.es.md) · [📖 Cómo leer e interpretar un run AgentBench](../docs/reading-guide.es.md)

[Conclusiones — ¿cuándo compensa colaborar?](CONCLUSIONS.es.md)

Las V1 anteriores están [archivadas](ARCHIVE_V1.es.md). «Referencia actual» en sus informes describe su estado histórico, no la campaña Astra.

**Recorrido aconsejado:** [entender los 15 grupos y 71 controles](../docs/acceptance-tests.es.md)
→ [ver resultados](#resultados-publicados) → abrir el informe, el acta y la
traza. Los antiguos `6/6` y `9/9` cuentan grupos `unittest`, no cada aserción.

[V2 Astra medium](astra-medium-v2.es.md) · [Astra/high](astra-v2-retired.es.md) · [Guide](../docs/reading-guide.es.md)

## Referencia V1 Astra medio — ambas calculadoras terminadas

**V1 frente a V2, Astra medio: igual puntuación oficial en ambos desafíos.** V2 utiliza ×3,56 tiempo y ×4,49 tokens en total. La revisión aporta correcciones de robustez fuera de la puntuación. [Balance completo y pruebas](astra-medium-v1-v2.es.md)

## Resultados publicados

| Intento | Mode | Objetivo | Resultado | Estado | Detalles |
| --- | --- | --- | --- | --- | --- |
| `astra-medium-core-v1-001` | V1 solo Astra medium | Simple | 6/6 grupos · 14/14 controles | completed | [Report](astra-medium-v1-core.es.md) |
| `astra-medium-scientific-v1-001` | V1 solo Astra medium | Científica | 9/9 grupos · 57/57 controles | completed | [Balance completo y pruebas](astra-medium-v1-v2.es.md) |
| `astra-core-v1-002` | Codex solo | Calculadora Core | 6/6 grupos · 14/14 controles | Referencia Astra | [Informe completo](astra-v1.es.md) |
| `astra-scientific-v1-002` | Codex solo | Calculadora Scientific | 9/9 grupos · 57/57 controles | Referencia Astra | [Informe completo](astra-v1.es.md) |
| `sol-core-v1-001` | Codex solo | Calculadora Core | 6/6 grupos · 14/14 controles | Control de modelo | [Comparación](sol-vs-astra-v1.es.md) |
| `sol-scientific-v1-001` | Codex solo | Calculadora Scientific | 9/9 grupos · 57/57 controles | Control de modelo | [Comparación](sol-vs-astra-v1.es.md) |
| `sol-core-v2-001` | Equipo Codex | Calculadora Core | 6/6 grupos · 14/14 controles | V2 Sol publicada | [Informe, acta y traza](sol-v2-core.es.md) |
| `sol-scientific-v2-001` | Equipo Codex | Calculadora Scientific | 9/9 grupos · 57/57 controles | V2 Sol publicada | [Síntesis, acta y traza](sol-v2.es.md) |
| `astra-core-v2-001` | Equipo Astra | Calculadora Core | 6/6 grupos · 14/14 controles | V2 Astra | [Informe](astra-v2-core.es.md) |
| `astra-medium-core-v2-001` | Equipo Astra medium | Calculadora Core | 6/6 grupos · 14/14 controles | V2 Astra medium | [Informe](astra-medium-v2.es.md) |
| `astra-medium-scientific-v2-001` | Equipo Astra medium | Calculadora Scientific | 9/9 grupos · 57/57 controles | V2 Astra medium | [Informe](astra-medium-v2.es.md) |

## Datos conservados

Para cada intento se conservan como mínimo: identificador y modo; fecha,
entorno y versión de Codex; primera pasada; resultado final; duración total;
intervenciones humanas; observaciones y límites.
