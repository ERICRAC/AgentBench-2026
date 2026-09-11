# AgentBench 2026

[Français](README.md) · [English (UK)](README.en.md) · **Español** · [Português](README.pt.md)

> Un agente sabe escribir código. ¿Qué sucede cuando varios agentes tienen que trabajar juntos?

**AgentBench 2026 es un laboratorio abierto de I+D sobre colaboración y comportamiento social de agentes IA.** Les damos los mismos problemas y cambiamos su organización: un desarrollador solo, un equipo de especialistas o, en el futuro, agentes locales.

No buscamos únicamente comprobar que el programa funciona. Queremos entender **quién aporta qué, cómo circulan los consejos, qué errores se evitan y cuánto cuesta en tiempo y tokens**. Los primeros ejercicios son una calculadora simple y una científica: problemas accesibles para observar estos mecanismos.

La pregunta que guía el proyecto: **¿a partir de cuándo trabajar juntos resulta más eficiente que trabajar solos?**

Una experiencia concebida y dirigida **íntegramente mediante micrófono con Codex** por [Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/), con intercambios, resultados y límites publicados para examinarlos.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-social-agents.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-social-agents-light.png">
  <img alt="AgentBench 2026: un agente frente a una red de agentes" src="assets/agentbench-social-agents-light.png">
</picture>

[📖 Descubrir el proyecto y leer un run](docs/reading-guide.es.md) · [Ver runs en 2 minutos](results/run-summaries/index.es.md) · [Leer conclusiones](results/CONCLUSIONS.es.md)

Para orientarse: **V1 = solo**, **V2 = un desarrollador escritor y tres consultores**, **V3 = futuros consultores locales**. Las versiones describen organizaciones, no niveles de dificultad de calculadoras.

![Campaña](https://img.shields.io/badge/campa%C3%B1a-4%2F6_validaciones-22c55e)
![Progreso](https://img.shields.io/badge/progreso-67%25-06b6d4)
![Siguiente paso](https://img.shields.io/badge/siguiente-observaciones_V2-8b5cf6)
![Licencia](https://img.shields.io/badge/licencia-MIT-f97316)

## Panel de control — estado actual

**Astra medio: V1 y V2 terminadas en ambas calculadoras**, 4/6 celdas de campaña; cada organización alcanza 15/15 grupos y 71/71 controles. V3 pendiente.

**V1 frente a V2, Astra medio: igual puntuación oficial en ambos desafíos.** V2 utiliza ×3,56 tiempo y ×4,49 tokens en total. La revisión aporta correcciones de robustez fuera de la puntuación. [Balance completo y pruebas](results/astra-medium-v1-v2.es.md)

**V2.2 — pareja ligera: protocolo preparado, no congelado.** Dos roles, tres sesiones, una revisión. Ningún candidato lanzado; faltan preflight técnico y autorización. [Protocolo V2.2](governance/V2_2_PROTOCOL.es.md)

Campaña de referencia del panel: **Sol high · `sol-high-control-001`**. [Catálogo de 71 controles](docs/acceptance-tests.es.md) · [Control V1 Sol](results/sol-vs-astra-v1.es.md) · [Síntesis V2](results/sol-v2.es.md) · [Archivo V1](results/ARCHIVE_V1.es.md).

| Campaña principal | V1 · Codex solo | Próxima ejecución | Protocolos |
| :---: | :---: | :---: | :---: |
| **4 / 6 validadas** | **2 / 2 replicadas** | **Hito de observación V2** | **Retos y protocolo V2 fijados** |
| `████████░░░░` **67 %** | simple **6 grupos · 14 controles** · científica **9 grupos · 57 controles** | Comparar mejora y ruido | Verificadores independientes |

```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#0f2a4a", "primaryTextColor": "#f8fafc",
  "primaryBorderColor": "#22d3ee", "secondaryColor": "#3b1d67",
  "tertiaryColor": "#431f2b", "fontFamily": "system-ui",
  "lineColor": "#8b5cf6", "clusterBkg": "#0b1220",
  "clusterBorder": "#475569"
}}}%%
flowchart LR
    subgraph V1["V1 · Codex solo · 2/2"]
      V1C["✓ Calculadora simple<br/>6 grupos · 14 controles"]
      V1S["✓ Calculadora científica<br/>9 grupos · 57 controles"]
    end
    G1{"Observaciones V1<br/>referencia individual"}
    subgraph V2["V2 · Equipo Codex · 2/2"]
      V2C["✓ Calculadora simple<br/>6 grupos · 14 controles"]
      V2S["✓ Calculadora científica<br/>9 grupos · 57 controles"]
    end
    G2{"Observaciones V2<br/>posible ajuste"}
    V21["V2.x · variante optimizada<br/>opcional"]
    subgraph V3["V3 · Codex + Ollama · 0/2"]
      V3C["○ Calculadora simple<br/>pendiente"]
      V3S["○ Calculadora científica<br/>pendiente"]
    end
    G3{"Observaciones V3<br/>comparación final"}
    V4["V4 · control AutoGen<br/>opcional"]
    V1C & V1S --> G1
    G1 --> V2C & V2S
    V2C & V2S --> G2
    G2 -. "si la mejora es medible" .-> V21
    G2 --> V3C & V3S
    V3C & V3S --> G3
    G3 -. "control histórico" .-> V4
    classDef done fill:#14532d,stroke:#4ade80,color:#f0fdf4,stroke-width:3px;
    classDef next fill:#4c1d95,stroke:#c084fc,color:#faf5ff,stroke-width:3px;
    classDef todo fill:#172554,stroke:#38bdf8,color:#f0f9ff,stroke-width:2px;
    classDef gate fill:#7c2d12,stroke:#fb923c,color:#fff7ed,stroke-width:2px;
    classDef optional fill:#0f2a4a,stroke:#94a3b8,color:#f8fafc;
    class V1C,V1S,V2C,V2S done;
    class V3C,V3S todo;
    class G1,G3 gate;
    class G2 next;
    class V21,V4 optional;
```

Las seis celdas V1–V3 × Calculadora simple–Calculadora científica forman la
campaña obligatoria. V2.x y V4 son extensiones opcionales.

## Qué nos enseñan los primeros experimentos

> En las tareas estudiadas, el coste de coordinación supera el beneficio medido. AgentBench busca las condiciones donde se invierte esta relación: dificultad, especialización, paralelismo y coste de los errores.

[Conclusiones — ¿cuándo compensa colaborar?](results/CONCLUSIONS.es.md) — Esto se refiere a comparaciones disponibles con modelo y esfuerzo idénticos y la V2 consultiva actual, no a todos los equipos. Las pruebas oficiales no miden todas las correcciones adicionales observadas.

## Pregunta experimental

> ¿Un equipo de agentes produce un resultado mejor que un único buen agente
> cuando se contabilizan el tiempo, los tokens, el ruido de coordinación y la
> complejidad añadida?

Cada organización recibe la misma especificación, restricciones, pruebas
independientes y un directorio limpio. No puede consultar ni reutilizar la
solución de otro intento. **Los agentes proponen; el verificador decide.**

```math
\text{valor experimental}
=
\frac{\text{calidad obtenida}}
{\text{tiempo} + \text{tokens} + \text{coordinación}}
```

La fórmula ilustra la intuición del proyecto; no es una puntuación que sume unidades incompatibles. Los informes comparan calidad, segundos, tokens y coordinación por separado.

## Qué se prueba realmente

`6/6` y `9/9` cuentan **grupos `unittest`**, no todas las aserciones. En una
ejecución correcta, los 15 grupos realizan **71 controles: 14 simple y 57
científica**.

### simple — 6 grupos / 14 controles

- [x] C01 archivos (2); C02 sin ejecución dinámica (1).
- [x] C03 cuatro operaciones verificadas por separado (4).
- [x] C04 operador desconocido (1); C05 división por cero (1).
- [x] C06 CLI, errores y recuperación (5).

### científica — 9 grupos / 57 controles

- [x] S01 entregables y documentación (7); S02 seguridad (2).
- [x] S03 operadores y prioridades (10); S04 lenguaje matemático (6).
- [x] S05 variable y nombres prohibidos (5); S06 errores (6).
- [x] S07 muestreo (8); S08 SVG pasivo (7); S09 CLI (6).

**Auditoría:** [71 controles detallados](docs/acceptance-tests.es.md) →
[especificaciones y tests](challenges/) → [resultados](results/README.es.md) →
actas y trazas. La cobertura no es una nota absoluta de calidad.

## V2 de un vistazo

[📖 Cómo leer e interpretar un run AgentBench](docs/reading-guide.es.md) · [Cinco runs V2, dos minutos cada uno](results/run-summaries/index.es.md)

```mermaid
flowchart TB
    X["Desafío"] --> A["SA-01 · requisitos"]
    X --> B["SA-02 · arquitectura"]
    A --> W["Barrera · ambas respuestas recibidas"]
    B --> W
    W --> C["SA-01 + SA-02 · revisiones cruzadas paralelas"]
    C --> D["Barrera · ambas revisiones recibidas"]
    D --> M["MAIN · único desarrollador escritor"]
    M --> Q["SA-03 · revisión de calidad"]
    Q --> F["MAIN · correcciones y verificador"]
```

RELAY lanza y transmite mecánicamente, fuera del equipo candidato. Cuatro roles candidatos, siete sesiones; las dos primeras fases son paralelas, la escritura es secuencial.

[Instrumentación y publicación](docs/observability.es.md) · [Dependencias](requirements.txt) · [Node.js / WSL / Markdown](docs/node-wsl.es.md)

## Resultados publicados

| Ejecución | Organización | Objetivo | Veredicto | Tiempo | Tokens observados |
| --- | --- | --- | ---: | ---: | ---: |
| [`astra-medium-core-v1-001`](results/astra-medium-v1-core.es.md) | V1 · Astra medium | Simple | **6/6 grupos · 14/14 controles** | 98.572 s | 98 496¹ |
| [`astra-medium-scientific-v1-001`](results/astra-medium-v1-v2.es.md) | V1 · Astra medium | Científica | **9/9 grupos · 57/57 controles** | 188.560 s | 119 388¹ |
| [`astra-core-v1-002`](results/astra-v1.es.md) | V1 · Referencia Astra | Calculadora simple | **6/6 grupos · 14/14 controles** | 100.175 s | 120 478¹ |
| [`astra-scientific-v1-002`](results/astra-v1.es.md) | V1 · Referencia Astra | Calculadora científica | **9/9 grupos · 57/57 controles** | 399.478 s | 220 510¹ |
| [`sol-core-v1-001`](results/sol-vs-astra-v1.es.md) | V1 · Control Sol | Calculadora simple | **6/6 grupos · 14/14 controles** | 189.964 s | 158 101¹ |
| [`sol-scientific-v1-001`](results/sol-vs-astra-v1.es.md) | V1 · Control Sol | Calculadora científica | **9/9 grupos · 57/57 controles** | 1 009.468 s | 296 275¹ |
| [`sol-core-v2-001`](results/sol-v2-core.es.md) | V2 · Equipo Sol | Calculadora simple | **6/6 grupos · 14/14 controles** | 796.534 s | 559 088¹ |
| [`sol-scientific-v2-001`](results/sol-v2.es.md) | V2 · Equipo Sol | Calculadora científica | **9/9 grupos · 57/57 controles** | 1 587.605 s | 916 538¹ |
| [`astra-core-v2-001`](results/astra-v2-core.es.md) | V2 · Equipo Astra | Calculadora simple | **6/6 grupos · 14/14 controles** | 700.994 s | 572 168¹ |
| [`astra-medium-core-v2-001`](results/astra-medium-v2.es.md) | V2 · Equipo Astra medium | Calculadora simple | **6/6 grupos · 14/14 controles** | 375.169 s | 408 616¹ |
| [`astra-medium-scientific-v2-001`](results/astra-medium-v2.es.md) | V2 · Equipo Astra medium | Calculadora científica | **9/9 grupos · 57/57 controles** | 648.008 s | 570 382¹ |

¹ Entrada + salida acumuladas. Los informes separan caché, razonamiento y
correcciones; los datos ausentes nunca se reconstruyen a posteriori.

## V1, V2, V3… V2.x y V4

**Nombres acordados: V2** sigue siendo el equipo consultivo histórico; **V2.1** es desarrollo paralelo; **V2.2** la pareja ligera; **V2.x** la familia de variantes futuras, no otro intento. V1 sigue como referencia solo. Comparaciones futuras en Astra medio, con calculadoras simple y científica. Nombres aprobados; protocolos detallados y lanzamientos pendientes.

- **V1:** el orquestador experimental encarga el trabajo a una sesión candidata
  Codex distinta; esta trabaja sola, sin consultores ni delegación.
- **V2:** orquestador Codex y especialistas con misiones acotadas y un solo redactor.
- **V2.x:** optimización exploratoria opcional, únicamente tras analizar V2.
- **V3:** Codex orquesta, decide y escribe; modelos Ollama locales analizan o critican.
- **V4:** control histórico opcional del proyecto multiagente de Yann Pointud,
  llamado AutoGen pero independiente del framework homónimo de Microsoft.

Un cambio sustancial de modelo, prompt, roles, contexto o parámetros abre una
**nueva campaña**. Se repiten las referencias comparables V1…Vn y se conservan
los resultados anteriores. Véase el [plan experimental](governance/EXPERIMENTAL_DESIGN.es.md).

## Tareas experimentales

- [x] Congelar las pruebas de Calculadora simple y Calculadora científica.
- [x] Conservar las primeras observaciones V1 `001` sin reescribirlas.
- [x] Replicar V1 con modelo, esfuerzo y contexto fijados: simple `astra-core-v1-002` **6/6**, científica `astra-scientific-v1-002` **9/9**.
- [x] Controlar V1 con Sol/high: **15/15 grupos y 71/71 controles elementales**, con [comparación publicada](results/sol-vs-astra-v1.es.md).
- [x] Decidir y fijar roles, intercambios, presupuestos y [métricas V2](governance/V2_PROTOCOL.es.md).
- [x] Validar el preflight V2: aislamiento, configuración por rol, trazas visibles y contadores. [PV](results/astra-v2-preflight.es.md).
- [x] Ejecutar y publicar V2 Calculadora simple: **6/6 grupos y 14/14 controles**, con [informe y acta](results/sol-v2-core.es.md).
- [x] Ejecutar y publicar V2 Calculadora científica sin cambiar el protocolo: **9/9 grupos y 57/57 controles**, con [síntesis V2](results/sol-v2.es.md).
- [ ] Analizar V2 y decidir si V2.x aporta una hipótesis medible.
- [ ] Congelar los modelos Ollama y los límites de contexto de V3.
- [ ] Ejecutar V3 para ambos objetivos.
- [ ] Comparar las seis ejecuciones principales.
- [ ] Decidir si el control histórico V4 aporta información útil.

<details>
<summary><strong>Medidas y reproducción</strong></summary>

Se observan conformidad, robustez, calidad del código y la documentación,
duración, tokens, llamadas, correcciones, intervención humana, desacuerdos,
ruido de coordinación y textos visibles entre profesiones, conservados en un
[acta experimental](governance/PV_TEMPLATE.es.md).

```bash
python3 scripts/new_run.py mi-run-v1
cd runs/mi-run-v1
python3 ../../scripts/capture_session.py --cwd solution --prompt ../../prompts/codex-single.md --config ../../governance/astra-v1.toml
cd ../..
python3 scripts/verify.py --solution runs/mi-run-v1/solution
```

Cada intento utiliza un identificador nuevo y un directorio limpio.

</details>

<details>
<summary><strong>Gobernanza y transparencia</strong></summary>

El directorio [`governance/`](governance/) define las instrucciones, el plan
experimental, las respuestas y el registro público. El
[historial](logs/history.es.md) conserva decisiones sin horarios de trabajo,
secretos ni transcripciones personales completas.

</details>

## Sobre el autor

[Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/) es
arquitecto de sistemas de información y responsable de TI con más de treinta
años de experiencia. AgentBench 2026 es su primer POC público sustancial con
Codex como agente de IA y una cadena Git de estilo CI/CD.

[Perfil de LinkedIn](https://www.linkedin.com/in/eric-racineux-75475a7/)
· [CV en línea](https://ericrac.github.io/CV-Eric-RACINEUX/)

## Licencia

MIT. El AutoGen de Yann Pointud es un proyecto independiente; no está incluido
ni bifurcado aquí y no usa el framework homónimo de Microsoft.

## Bonus — AgentBench en 3D

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-crystal-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-crystal-light.png">
  <img alt="Cristal octaédrico AgentBench en 3D" src="assets/agentbench-crystal-light.png">
</picture>

[Descargar y manipular el modelo STL](assets/agentbench-crystal.stl).
