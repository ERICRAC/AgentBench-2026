# Preflight V2 Astra — resultado

[Français](astra-v2-preflight.md) · [English (UK)](astra-v2-preflight.en.md) · **Español** · [Português](astra-v2-preflight.pt.md)

Preflight mínimo **superado por los 4 roles**, después de publicar V1 en `c959216`. No es una celda de benchmark: la campaña sigue en **2/6**.

| Rol | Profesión | Entrada + salida | Duración |
| --- | --- | ---: | ---: |
| MAIN | Orquestador / escritor | 12673 | 8.406 s |
| SA-01 | Requisitos y seguridad | 12512 | 8.7 s |
| SA-02 | Arquitectura y testabilidad | 12514 | 7.134 s |
| SA-03 | Crítico QA adversarial | 12320 | 7.383 s |

## Controles observados

Cuatro configuraciones TOML aceptadas con validación estricta, threads nuevos distintos, sin historial proporcionado, respuestas exactas y SHA-256 coincidentes. Todos terminaron con código 0 y contadores. Ninguna llamada de comando ni escritura observada en el directorio temporal vacío.

[JSON](../governance/astra-v2-preflight/run.json)

## Alcance y límites

Motor A-08: sesiones `codex exec --json` separadas. El contrato nativo disponible no expone contexto/compactación y contadores individuales. No es una comparación de motores.

`gpt-6-astra/high`, contexto 200.000, compactación 180.000 (`total`), CLI 0.153.4. Consultores configurados como solo lectura. Siguen presentes instrucciones de plataforma y definiciones de herramientas.

No se fuerza compactación ni se miden límites del servidor; tampoco se prueba escritura prohibida o el ciclo social completo. Estos TOML contienen consignas de diagnóstico, no misiones listas para el benchmark.

## Medidas y análisis

49.961 tokens de entrada + 58 de salida = **50.019**; caché 36.352 ya incluida. Razonamiento devuelto: 0 en respuestas triviales con high. Suma de duraciones **31,623 s**, no tiempo mural: las sesiones se solapan y el tiempo global no se registró.

Coste del diagnóstico, no rendimiento social o de calculadora. El contexto de infraestructura refuerza la necesidad de contar cada llamada V2.

## Textos observables

Cada bloque vincula petición y respuesta exactas. No hubo resolución conjunta; no se infiere influencia entre agentes.

### 1 · MAIN

[Config](../governance/astra-v2-preflight/MAIN.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est MAIN — Orchestrateur candidat et écrivain unique.
Réponds exactement : MAIN | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
MAIN | READY | ASTRA-PREFLIGHT
```

### 2 · SA-01

[Config](../governance/astra-v2-preflight/SA-01.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-01 — Analyste exigences et sécurité.
Réponds exactement : SA-01 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-01 | READY | ASTRA-PREFLIGHT
```

### 3 · SA-02

[Config](../governance/astra-v2-preflight/SA-02.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-02 — Architecte logiciel et testabilité.
Réponds exactement : SA-02 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-02 | READY | ASTRA-PREFLIGHT
```

### 4 · SA-03

[Config](../governance/astra-v2-preflight/SA-03.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-03 — Critique QA adversarial.
Réponds exactement : SA-03 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-03 | READY | ASTRA-PREFLIGHT
```

## Siguiente paso

V1 publicada y preflight mínimo terminado. Próximo experimento: V2 Core con avisos y decisiones completos, seguido de informe antes de Scientific. Benchmark V2 aún no lanzado.
