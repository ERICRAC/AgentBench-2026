# Ensayo científico reducido — interrupción OBS-002

[Français](v2-2-lean-scientific-001.md) · [English (UK)](v2-2-lean-scientific-001.en.md) · [Español](v2-2-lean-scientific-001.es.md) · [Português](v2-2-lean-scientific-001.pt.md)

## Corrección OBS-002 preparada, sin nuevo ensayo

La versión 002 comunica explícitamente a cada fase que el orquestador validó el acuerdo humano y autoriza comenzar ahora. El lanzamiento sigue exigiendo confirmación del ID exacto; el mensaje solo se transmite después de ese control. Restricciones de rol y prohibición de delegación intactas.

141 pruebas superadas. Las seis pruebas del adaptador 002 comprueban los tres prompts enviados al proceso ficticio, su igualdad con las capturas, ID y fase, eliminación de reservas ambiguas, rechazo sin acuerdo y rechazo de repetición. Comprobar la transmisión no garantiza por sí solo la interpretación futura del modelo.

Ensayo previsto: astra-medium-scientific-v2-2-lean-002; nueva campaña astra-medium-lean-003. Astra medio, 24 000 caracteres, parada entre sesiones a 150 000 tokens sin techo estricto. Sin llamada a modelos ni directorio del run 002. Run 001, costes y archivos congelados idénticos. El lanzamiento real requiere acuerdo humano; no se prevé otra preparación antes del acuerdo.

[Manifest 002](../governance/v2-2-lean-scientific-002.json) · [Adapter 002](../scripts/run_v2_2_lean_scientific_live_002.py) · [Tests 002](../tests/test_lean_scientific_live_002.py).

El ensayo real se detuvo antes de crear código: **11 968 tokens, 12,811 s, sin resultado de calculadora**. No fue agotamiento de cuota. Sin reintento.

## Qué ocurrió

El acuerdo humano fue recibido y el lanzador inició una sesión MAIN. Pero el mandato indicaba que congelar el protocolo no autorizaba el lanzamiento, sin confirmar al candidato que el acuerdo ya existía. MAIN pidió confirmación y terminó sin herramientas. La CLI devolvió 0; el relé detectó entregables ausentes y terminó con código 1. No se iniciaron el revisor ni MAIN final.

Es un defecto de transmisión de autorización del dispositivo preparado por el orquestador. Las 135 pruebas sin modelo comprobaban rutas técnicas; los candidatos ficticios no interpretaban la condición lingüística. Se conserva OBS-002 sin modificar retroactivamente el protocolo.

## Medidas y verificación

Una sesión CLI iniciada y terminada, cero fases validadas. Entrada: 11 810; salida: 158; total: 11 968. Caché: 0, incluida en entrada; razonamiento: 89, incluido en salida. Duración total: 12,810581794 s; sesión: 12,809085513 s. No se alcanzó el umbral 150 000; sobre inicial: 5 023 de 24 000 caracteres. Saldo de cuota y coste del orquestador: no registrados.

Inspección independiente: solución vacía, contrato, verificador y suite copiados sin cambios. Suite científica no ejecutada: no se asigna 9/9 ni 0/9. El estado conserva usage_complete=false, impuesto por el relé ante la excepción; los contadores del único proceso completado están presentes y publicados.

## Conclusión y siguiente acción

No permite comparar eficiencia individual y colectiva: la colaboración no empezó. Resultados históricos intactos; estos 11 968 tokens son coste de ensayo interrumpido, no de referencia terminada.

Corrección recomendada en nueva versión: tras validar el acuerdo, comunicar explícitamente al candidato que el orquestador autoriza esta fase ahora y debe comenzar. Eliminar reservas ambiguas del mensaje, conservar el control de autorización en el lanzador y probar la confirmación. No se aplica corrección ni nuevo ensayo: hacen falta ID nuevo y autorización de reintento.

## Artefacts

- [PV / messages](../runs/astra-medium-scientific-v2-2-lean-001/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-001/run.json) · [State](../runs/astra-medium-scientific-v2-2-lean-001/state.json).
- [Prompt](../runs/astra-medium-scientific-v2-2-lean-001/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-001/trace.json).
- [Checks](../runs/astra-medium-scientific-v2-2-lean-001/verifications.json) · [Snapshots](../runs/astra-medium-scientific-v2-2-lean-001/snapshots.json).
- [Manifest](../governance/v2-2-lean-scientific-001.json) · [Preflight](v2-2-lean-scientific-preflight.es.md).
