# Auditoría de costes V2.2 — variante ligera sin modelo

[Français](v2-2-cost-audit.md) · [English (UK)](v2-2-cost-audit.en.md) · **Español** · [Português](v2-2-cost-audit.pt.md)

**Ningún candidato ejecutado.** El run 002 terminado sigue intacto. Reducir transmisiones no demuestra conservar la calidad ni ahorrar cuota.

## Medidas exactas

Caracteres Unicode, no tokens, de las capturas públicas normalizadas. Solo se compara el sobre JSON con la misma serialización; los nuevos mandatos quedan fuera del cálculo.

| Fase | Prompt histórico completo | Datos históricos | Datos propuestos |
| --- | ---: | ---: | ---: |
| MAIN inicial | 3 430 | 1 652 | 1 652 |
| REV-01 | 13 927 | 12 084 | 6 886 |
| MAIN final | 16 388 | 14 347 | 9 149 |

Se eliminan **10 396 caracteres, el 37,0 %** de 28 083 caracteres acumulados. Las órdenes/salidas iniciales ocupan 5 062 caracteres JSON retransmitidos en cada fase posterior. El resto eliminado es el mensaje intermedio y su serialización. Se conservan contrato, archivos completos, mensajes finales y pruebas de órdenes del revisor.

Entrada histórica: 110 511 tokens acumulados, incluidos 65 280 en caché; salida: 3 263. No es el tamaño de un solo prompt. Las capturas no permiten atribuir todos los tokens al sistema, herramientas o transmisiones. **No se estima ahorro de tokens ni de cuota.**

## Variante propuesta, sin congelar

Tres sesiones, dos oficios y Astra medio. Límites finales propuestos: 150 / 300 / 300 palabras frente a 600 / 1 200 / 1 200; ahorro no incluido en la tabla. Las pruebas completas siguen archivadas, pero las órdenes iniciales dejan de inyectarse en las fases posteriores.

Contrapartida: el revisor tiene menos pruebas de los tests iniciales y debe distinguir declaraciones de MAIN de ejecuciones observadas. Una revisión más breve puede omitir hallazgos; señalar excesos necesarios, nunca truncar silenciosamente. Es una condición experimental nueva, no un cambio del protocolo histórico.

## Paradas comprobadas y límites

El simulador carece de transporte real. Diez tests nuevos cubren tres respuestas sintéticas, rechazo del modo real, exceso de tamaño, umbral exacto, sobrepaso visible, métricas ausentes, fallo sin retry, límites inválidos, conservación de datos y cálculo.

Propuesta a validar: **12 000 caracteres por sobre**, rechazo completo sin truncamiento; parada entre sesiones a **60 000 tokens acumulados observados**. No son límites congelados ni del abono. Con los costes históricos se pararía tras la revisión a 66 038 tokens: exceso de 6 038 y sin veredicto final. No se limita una sesión en curso; no hay watchdog ni límite nativo validado implementado.

Los 100 tokens/1 000 caracteres de los tests son valores sintéticos, no presupuestos recomendados. Pasan 82 tests de mantenimiento; no hay nueva puntuación de calculadora. Decidir sobre pérdida de información y parada antes de cualquier autorización distinta para científica o solo de referencia.

[JSON](v2-2-cost-audit.json) · [Audit / simulation](../scripts/audit_v2_2_cost.py) · [Tests](../tests/test_v2_2_cost.py) · [MAIN initial](../prompts/v2-2-lean-initial-draft.md) · [REV-01](../prompts/v2-2-lean-review-draft.md) · [MAIN final](../prompts/v2-2-lean-final-draft.md) · [Run 002](v2-2-supervised-core-002.es.md)
