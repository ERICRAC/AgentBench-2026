# V2.2 supervisada — ensayo simple interrumpido por cuota

[Français](v2-2-supervised-core.md) · [English (UK)](v2-2-supervised-core.en.md) · **Español** · [Português](v2-2-supervised-core.pt.md)

**El ensayo Astra medio comenzó realmente; después la CLI indicó límite de uso.** MAIN creó ambos entregables, pero no terminó su sesión. REV-01 y MAIN final no se iniciaron. Sin reintento.

| Medida | Observación |
| --- | --- |
| Intento | astra-medium-core-v2-2-supervised-001 |
| Sesiones | 1 iniciada, 0 terminadas de 3 previstas |
| Tiempo del proceso candidato | 48,639 s |
| Tiempo total del ensayo interrumpido | 48,641 s |
| Tokens / número de peticiones al modelo | No registrados, no cero |
| Veredicto V2.2 completo | Ninguno |
| Diagnóstico tras interrupción | 6/6 grupos, 14 controles correctos |

Archivos conservados **sin correcciones del orquestador**. Después del cierre, el verificador confirmó entregables, ausencia de ejecución dinámica, cuatro operaciones, errores de operador/división y recuperación CLI. [Checklist](../docs/acceptance-tests.es.md). No es una pasada oficial de fase final ni se comunicó al candidato.

**Conclusión:** el transporte real permitió leer y escribir. Este ensayo se detuvo por cuota, no por el bloqueo MCP anterior. No permite juzgar eficiencia del binomio: sin revisión, arbitraje ni total de tokens. No comparar 48,641 s con V1/V2 completas. Se mantienen las limitaciones del piloto supervisado, sin afirmar aislamiento completo.

[PV y análisis social](../runs/astra-medium-core-v2-2-supervised-001/PV.md) · [Mandato completo](../runs/astra-medium-core-v2-2-supervised-001/PROMPT.md) · [Eventos visibles](../runs/astra-medium-core-v2-2-supervised-001/trace.jsonl) · [Metadatos](../runs/astra-medium-core-v2-2-supervised-001/run.json) · [Código intacto](../runs/astra-medium-core-v2-2-supervised-001/solution/calculator.py) · [Protocolo](../governance/V2_2_SUPERVISED.es.md).

Capturas brutas privadas. La traza pública omite ruta temporal y enlaces/hora de reinicio del mensaje de cuota. Sin datos inventados. Archivos protegidos y hashes congelados verificados.

**Siguiente:** si el usuario confirma cuota y relanzamiento, nuevo intento simple, ID nuevo y solución vacía. No reanudar ni reutilizar este código; científica no autorizada.

[README](../README.es.md) · [Conclusiones](CONCLUSIONS.es.md)
