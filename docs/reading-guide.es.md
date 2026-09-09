# Comprender AgentBench

[Français](reading-guide.md) · [English (UK)](reading-guide.en.md) · **Español** · [Português](reading-guide.pt.md)

[Conclusiones — ¿cuándo compensa colaborar?](../results/CONCLUSIONS.es.md)

Los nombres son **calculadora simple** (Core) y **calculadora científica** (Scientific). Identificadores técnicos y pruebas históricas sin cambios.

Laboratorio I+D sobre colaboración de agentes: las calculadoras son ejercicios comunes. V1 = un candidato solo; V2 = un escritor y tres consultores; V3 = futuros consultores locales. Se miden calidad, tiempo y tokens: no se promete que V2 sea mejor.

| ID | Role |
| --- | --- |
| RELAY | Orquestador experimental |
| MAIN | Desarrollador principal, único escritor y decisor |
| SA-01 | Subagente 1 — requisitos y seguridad |
| SA-02 | Subagente 2 — arquitectura y testabilidad |
| SA-03 | Subagente 3 — revisor crítico de calidad, defectos y casos límite |

En los PV, abrir « Texte envoyé, mot pour mot » y leer « Texte retourné ». MSG-003/004: respuestas cruzadas; MSG-006: crítica SA-03; MSG-007: decisión final. Siete sesiones representan cuatro roles candidatos. El verificador es un programa independiente. `trace.json` registra comandos y contadores; `DECISIONS.md`, decisiones. Textos visibles filtrados, sin razonamiento interno.

[Sol Core PV](../runs/sol-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Sol Scientific PV](../runs/sol-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium](../results/astra-medium-v2.es.md)

[Astra medium Core PV](../runs/astra-medium-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium Scientific PV](../runs/astra-medium-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré)

Vx futura, no activada: asignar una evolución fijada a un nuevo mantenedor con solo código y documentación; medir éxito, regresiones, tiempo, tokens y aclaraciones. Las pruebas actuales no miden mantenibilidad (Scientific verifica cinco palabras documentales). Evaluar explicaciones útiles, no contar comentarios. Trabajar en una nueva rama o carpeta para conservar la prueba.

[README](../README.es.md) → [Tests](acceptance-tests.es.md) → [Results](../results/README.es.md)

## Trabajo documental adjunto — pendiente

Estos puntos proceden del documento recibido; aprobar nombres V2.x no significa completarlos.

- [ ] Guía de dos niveles y tabla de fuentes, reutilizando esta guía sin duplicarla.
- [ ] Diagrama de secuencia: paralelismo, barreras, destinatarios e información; distinguir RELAY mecánico de MAIN candidato.
- [ ] Resúmenes automáticos de dos minutos fuera del run, separados del verbatim histórico: equipo, veredicto, métricas e interacción decisiva.
- [ ] Anotaciones interpretativas explícitas: propuesta → transmisión → decisión → modificación → efecto; distinguir confirmación, rechazo y ausencia de efecto observable, sin llamarla ruido automáticamente.
- [ ] Instrumentación futura: tiempos relativos medidos, dependencias y grupos paralelos, estructura genérica N agentes/V3. Nunca inventar tiempos históricos; verificar impactos antes de aplicar cambios.
- [ ] Auditoría multilingüe: protocolo congelado separado del estado actual; verificar pruebas históricas, métricas, tests y comportamiento del runner sin repetir benchmarks por documentación.
