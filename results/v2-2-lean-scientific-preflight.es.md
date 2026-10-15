# Preflight científico — pareja reducida

[Français](v2-2-lean-scientific-preflight.md) · [English (UK)](v2-2-lean-scientific-preflight.en.md) · [Español](v2-2-lean-scientific-preflight.es.md) · [Português](v2-2-lean-scientific-preflight.pt.md)

## Intercambio 051

Transporte conectado y protocolo científico congelado. 135 pruebas de mantenimiento superadas; seis nuevas cubren adaptador, captura exacta, huellas, rechazo sin autorización y cadena completa con procesos ficticios seguida de rechazo de relanzamiento.

Ninguna llamada a modelos ni directorio de candidato real creado. ID previsto: astra-medium-scientific-v2-2-lean-001; campaña astra-medium-lean-002. Astra medio, tres sesiones, sobres de 24 000 caracteres, parada entre sesiones a 150 000 tokens sin límite estricto. Condiciones simples históricas intactas.

El manifiesto congelado no autoriza el lanzamiento. Tras acuerdo humano explícito, el orquestador usará --run con directorio externo nuevo y --approve-run con el ID exacto. Es confirmación del operador, no prueba automática de consentimiento ni barrera contra código arbitrario. Reserva persistente desde el lanzamiento incluso si falla; sin reintento. Siguiente: un ensayo real, verificación independiente y publicación del acta y costes.

[Manifest](../governance/v2-2-lean-scientific-001.json) · [Adapter](../scripts/run_v2_2_lean_scientific_live.py) · [Tests](../tests/test_lean_scientific_live.py).

[OpenAI Docs — non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) : CLI JSONL.

```bash
python3 -B scripts/run_v2_2_lean_scientific_live.py --check
```

## Actualización — intercambio 050

Límite de 24 000 caracteres aprobado. Motor científico versionado y validado sin modelos: tres fases simuladas completadas, 39 tokens ficticios, sin veredicto de calculadora. 129 pruebas de mantenimiento superadas, 21 de este motor. Huellas del lanzador simple congelado intactas.

Pruebas de archivos científicos, contrato y suite copiados idénticamente, comando --challenge scientific-calculator, capturas completas, REV-01 de solo lectura, escrituras prohibidas, sobres excesivos, contadores ausentes, parada a 150 000, exceso, sesiones distintas y ausencia de reintento. PYTHONDONTWRITEBYTECODE=1 explícito en el comando final para procesos hijos.

Quedan transporte real y congelación nominal antes de autorizar el lanzamiento. El motor rechaza el modo real incluso por su entrada interna. Sin ahorro, cuota suficiente ni resultado científico demostrado. La preparación anterior conserva el análisis de tamaño; su límite propuesto ya está aprobado.

[Script](../scripts/run_v2_2_lean_scientific.py) · [Tests](../tests/test_v2_2_lean_scientific.py) · [JSON](v2-2-lean-scientific-simulation.json).

Solo preparación: ningún candidato lanzado ni llamada a modelos. Los resultados simples se conservan.

## Hallazgo y propuesta

El contrato íntegro ocupa una envoltura inicial de 5 023 caracteres. Los perfiles solo usan texto sintético, nunca soluciones anteriores: README de 1 000 caracteres, informe MAIN de 150 palabras, revisión de 300 palabras y salida de control de 1 000 caracteres. No predicen el tamaño del futuro código ni representan tokens.

| Código sintético | Revisión | Transmisión final | 12 000 | 24 000 propuestos |
| ---: | ---: | ---: | :---: | :---: |
| 4 000 | 12 527 | 16 791 | ✗ | ✓ |
| 8 000 | 17 073 | 21 337 | ✗ | ✓ |
| 16 000 | 26 165 | 30 429 | ✗ | ✗ |

Ningún perfil cabe en 12 000; incluso sin código estas transmisiones ficticias superan el límite. Con 24 000, el límite de esta fixture es 10 342 caracteres de código. Se cuenta el escape JSON; se excluyen mandatos y contexto del cliente. Una revisión más larga puede superar el límite. No habrá truncamiento silencioso.

## Protocolo propuesto

Astra medio, un desarrollador y un revisor, tres sesiones distintas, sin reintento. Parada entre sesiones a 150 000 tokens observados de entrada + salida; una sesión puede superar el umbral. Sin promesa de menos de 100 000 para la científica. A medir: 9 grupos / 57 controles, no un resultado obtenido.

Los nuevos mandatos aclaran OBS-001: controles locales explícitamente autorizados sin consultar un manifiesto ausente. Nueva campaña propuesta astra-medium-lean-002; comparación histórica exploratoria, no causal. Una comparación homogénea requerirá controles autorizados por separado.

## Siguiente paso y límites

El motor congelado 001 sigue limitado a la simple; no se entrega adaptación real. Tras aprobar 24 000: versionar desafío, entregables, suite copiada y comando científico; probar las tres fases, límites de archivos y paradas sin modelos, y congelar. Lanzamiento real sujeto a aprobación explícita. Sin cambios de gobernanza general.

## Artefacts

- [JSON](v2-2-lean-scientific-size.json) · [Script](../scripts/preflight_lean_scientific.py) · [Tests](../tests/test_lean_scientific_preflight.py).
- [Draft](../governance/v2-2-lean-scientific-draft.json).
- [MAIN initial](../prompts/v2-2-lean-scientific-initial-draft.md) · [REV-01](../prompts/v2-2-lean-scientific-review-draft.md) · [MAIN final](../prompts/v2-2-lean-scientific-final-draft.md).
- [OBS-001](v2-2-lean-001.es.md).

```bash
python3 -B scripts/preflight_lean_scientific.py
python3 -B -m unittest discover -s tests -q
```
