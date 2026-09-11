# Protocolo V2.2 — pareja ligera Astra medio

[Français](V2_2_PROTOCOL.md) · [English (UK)](V2_2_PROTOCOL.en.md) · **Español** · [Português](V2_2_PROTOCOL.pt.md)

**V2.2: puente confinado probado; 52 tests correctos.** Integración bloqueada: CLI anuncia herramientas fuera de la lista permitida. Sin llamadas modelo. **Astra alto: solo histórico, sin nuevos runs previstos.** [MCP / CLI](../results/v2-2-bridge.es.md)

## En un minuto

**Preparado para validar, no congelado; ningún lanzamiento autorizado.** V2.2 estudia si una revisión conserva la aportación útil de V2 con menos coordinación. No es desarrollo paralelo: un desarrollador sigue siendo el único escritor. Variante opcional fuera de las seis celdas principales; no sustituye V2 histórica ni V2.1.

El [balance Astra medio](../results/astra-medium-v1-v2.es.md) motiva la hipótesis: igual puntuación V1/V2, V2 cuesta ×3,56 tiempo y ×4,49 tokens; algunas correcciones de robustez quedan fuera de puntuación. Hipótesis, no promesa: **V2.2 cuesta menos que V2 sin perder calidad y su revisión produce correcciones verificables.**

## Organización propuesta

| Organización | Roles candidatos | Sesiones por desafío | Relación |
| --- | ---: | ---: | --- |
| V1 | 1 | 1 | Desarrollador solo |
| V2 histórica | 4 | 7 | Dos análisis, dos revisiones cruzadas, implementación, crítica, correcciones |
| V2.2 | 2 | 3 | Desarrollador → revisor → desarrollador |

MAIN desarrolla, arbitra y escribe solo en solution/. REV-01 es el único revisor crítico, de solo lectura, para contrato, seguridad, funcionamiento y documentación, sin delegación. RELAY es el orquestador experimental externo: prepara, captura, transmite sin consejo ni síntesis, verifica y publica. El verificador independiente es la suite congelada, no un LLM.

MAIN inicial y final son **dos sesiones nuevas del mismo rol**, no una conversación retomada: tres threads, dos roles. REV-01 se parece a la función SA-03 de V2, con identidad distinta. Sin consultores previos, revisión cruzada ni segunda opinión.

## Secuencia y entradas exactas

| Fase | Entradas autorizadas | Salida / barrera |
| --- | --- | --- |
| P1 · MAIN inicial | Desafío activo + mandato inicial; solución vacía | Código/README completos; entrega ≤600 palabras; comandos/salidas de controles propios |
| P2 · REV-01 | Desafío + instantánea P1 completa + entrega P1 + comandos/salidas P1 | Una revisión ≤1200 palabras; hallazgos REV-001… con prueba y gravedad |
| P3 · MAIN final | Desafío + solución P1 + entrega/controles P1 + revisión/controles P2 íntegros | Arbitra cada ID, corrige, ejecuta verificador oficial; respuesta ≤1200 palabras |

Cada fase espera el cierre anterior. RELAY copia todos los archivos con rutas relativas y hashes, sin selección ni leer otro intento. Transmite textos visibles literalmente, nunca pensamientos privados. Salidas completas; truncamientos, omisiones y filtrado declarados. Una entrada ausente bloquea la fase siguiente: no se improvisa resumen. Los artefactos candidatos no son instrucciones de rol.

P1 y REV pueden hacer controles propios no destructivos; **el primer pase oficial ocurre en P3 tras la revisión**, como en V2. MAIN final puede corregir fallos oficiales en su sesión sin volver a consultar REV. Una revisión sin hallazgos es válida. Excesos de palabras se registran sin truncar pruebas ni pedir reformulación. Recuento propuesto: elementos separados por espacios en la respuesta final, código/tablas incluidos; mensajes intermedios capturados y contados aparte.

Mandatos canónicos franceses, borradores: [MAIN inicial](../prompts/v2-2-developer-initial.md), [REV-01](../prompts/v2-2-reviewer.md), [MAIN final](../prompts/v2-2-developer-final.md). Iguales para ambos desafíos, CHALLENGE activo aparte. No transmitir balances humanos, conclusiones anteriores o defectos históricos.

## Parámetros y límites

**gpt-6-astra / medium en las tres sesiones**, contexto 200000, compactación 180000, alcance total; sesiones efímeras. Usar parámetros registrados, no la selección del chat. Acceso al modelo, aceptación estricta de configuración y cuota quedan para preflight, sin garantía documental.

Desafíos/suites intactos: [simple](../challenges/calculator/SPEC.md), 6 grupos / 14 controles; [científica](../challenges/scientific-calculator/SPEC.md), 9 grupos / 57 controles. [Lista completa](../docs/acceptance-tests.es.md). Sin cambiar ni ampliar puntuación.

MAIN escribe solo entregables del desafío en solution/. REV solo lectura, controles sin archivos ni caché. Sin Git, red, delegación o dependencias adicionales para candidatos. RELAY gestiona actas, instantáneas y medidas fuera de entregables, en privado durante el run; publica después con commits separados de código/mantenimiento. Un directorio de trabajo no demuestra aislamiento: probar permisos efectivos.

## Presupuestos, interrupciones y orden

Piloto propuesto: **un intento por calculadora, máximo tres sesiones cada uno**, una revisión, sin reintento automático. Simple primero, verificación/publicación, autorización científica separada; sin ajustes intermedios.

Propuesta comparable: ningún nuevo límite global de tokens/tiempo, pues las referencias no lo tenían. **No garantiza caber en la cuota de suscripción.** Contexto y palabras no son presupuesto acumulado. Sumar costes de las tres sesiones, incluidos fallos; separar RELAY/publicación.

Cuota agotada, captura incompleta, escritura prohibida, fallo de infraestructura o exceso de sesiones: parar, preservar estado, fase, artefactos y contadores disponibles. Sin espera automática de renovación, continuación oculta ni sustitución de modelo. Reiniciar desde cero exige nuevo ID sin leer la solución anterior. Un límite numérico de seguridad debe acordarse e implementarse antes del congelado y aplicarse de forma comparable.

## Calidad y aportación de revisión

Preservar P1 antes de corregir. **Después del run**, RELAY ejecuta la suite congelada sobre una copia P1 y la entrega final. Etiquetar P1 «diagnóstico retrospectivo de instantánea», nunca «primer pase candidato»; no transmitirlo durante el run. Permite observar antes/después sin añadir feedback al desarrollador inicial.

Por hallazgo: ID, cláusula, gravedad, prueba/reproducción, ejecutado/no ejecutado, aceptado/rechazado/no verificable, cambio y control final. Separar correcciones por REV, espontáneas MAIN y por verificador. Reproducir hallazgos aplicables sobre ambas instantáneas después puede confirmar correcciones/regresiones: controles **exploratorios**, fuera de los 71 oficiales.

La suite común de robustez aún requiere diseño, calibración y congelado en una nueva campaña antes de los candidatos. No convertir retrospectivamente las dos sondas V1 en tests prerregistrados. Una aserción propuesta no prueba nada sin ejecutarse.

## Acta social y medidas

Aplicar la [plantilla de acta](PV_TEMPLATE.es.md), solo MAIN y REV-01 como roles candidatos. Conservar mandatos/respuestas visibles íntegros filtrados, MSG-001…, threads y hashes; sin secretos, horas públicas o razonamiento privado. Analizar quién señala, acepta/rechaza y qué prueba vincula consejo, cambio y efecto; no inferir emociones o pensamientos.

Publicar acuerdos explícitos, contradicciones, duplicados, hallazgos únicos, decisiones, correcciones confirmadas, regresiones y puntos no verificables. Ausencia de segundo intercambio no significa consenso; aceptar no prueba necesidad. Novedad solo frente al estado/textos P1 observables.

Tiempo mural desde antes de preparar primera llamada hasta cierre/captura final; duraciones por sesión y suma; tokens entrada/caché/salida/razonamiento; palabras y volumen de artefactos. Caché incluida en entrada, razonamiento en salida. Separar verificación/publicación posteriores. Datos ausentes o tokens exactos de coordinación no expuestos: no registrados, no estimados desde palabras. Instrumentación y fronteras se congelarán en preflight; no reutilizar el grafo V2 de siete fases.

Comparar V2.2/V1 y V2.2/V2 **por misma calculadora**, luego agregar pares completos. Victoria oficial: puntuación no inferior, tiempo/tokens no superiores y alguna mejora estricta. Robustez adicional con sobrecoste: compromiso. Igual puntuación no equivale a calidad exhaustiva; un antes/después no demuestra causalidad.

## Campaña y nivel de prueba

Topología/prompts nuevos son un cambio sustancial: **nueva campaña**, ID propuesto astra-medium-lean-001, sin alterar astra-medium-001. El piloto frente a referencias existentes solo permite **comparación histórica exploratoria explícitamente cualificada** (orden, caché/carga, prompts, sesiones e instrumentación).

Confirmación homogénea: repetir V1, V2 y V2.2 en nueva campaña, ambos desafíos, reglas comunes. Propuesta, no compromiso de consumo: tres repeticiones por celda, orden contrabalanceado, **18 runs**; dispersión/medianas, no solo mejor resultado. Sin afirmar significación ni umbral universal con esa muestra. Preparar no autoriza repeticiones ni piloto.

## Preflight antes de congelar y lanzar

- [x] Hipótesis, roles, tres fases, mandatos, criterios e interrupciones documentados.
- [x] FR, UK, ES, PT enlazados; protocolos/runs anteriores intactos.
- [x] Aprobado: piloto sin nuevo límite global; repeticiones no autorizadas.
- [x] Relé de tres fases probado con candidatos ficticios: transmisión, auditoría de escritura, límites, parada, capturas, instantáneas y bloqueo real. No valida aislamiento OS.
- [x] Dos configuraciones borrador e inventario de 15 hashes; simulaciones temporales nuevas. Directorios benchmark y hashes congelados pendientes.
- [ ] Verificar aislamiento/acceso real; prueba trivial real consume tokens y necesita autorización separada.
- [ ] Congelar protocolo, mandatos y ejecutor; publicar preflight estático, autorizar explícitamente calculadora simple.

**Etapa actual: transporte local y aislamiento Bubblewrap probados; integración modelo no cualificada, sin congelar ni benchmark.** Ningún candidato lanzado.

Validación de la etapa simulada anterior: 38 tests de mantenimiento (12 existentes + 26 V2.2), dos simulaciones de tres fases, cero llamadas modelo. El [informe técnico](../results/v2-2-preflight.es.md) distingue propiedades probadas y garantías pendientes.

[README](../README.es.md) · [Conclusiones](../results/CONCLUSIONS.es.md) · [V2 congelada](V2_PROTOCOL.es.md) · [Plan experimental](EXPERIMENTAL_DESIGN.es.md) · [Instrumentación](../docs/observability.es.md)
