# V2.2 ligera — lanzador preparado, ejecución real bloqueada

[Français](v2-2-lean-preflight.md) · [English (UK)](v2-2-lean-preflight.en.md) · **Español** · [Português](v2-2-lean-preflight.pt.md)

**Preparación autorizada y terminada; ningún candidato real ejecutado.** Se mantiene Astra medio. El motor encadena tres fases con mandatos y sobres reducidos, no solo calcula tamaños.

## Parámetros de preparación

| Parámetro | Valor |
| --- | --- |
| Modelo / esfuerzo futuro | gpt-6-astra / medium |
| Sesiones máximas | MAIN inicial → REV-01 revisor → MAIN final |
| Sobre JSON por fase | 12 000 caracteres Unicode, sin mandato |
| Objetivo experimental | Menos de 100 000 tokens, no es una previsión |
| Parada entre sesiones | A partir de 150 000 tokens entrada + salida observados |
| Límite estricto dentro de una sesión | Ninguno |
| Informes finales | 150 / 300 / 300 palabras; exceso registrado, sin truncar |
| Retry / científica / ejecución real | No autorizados |

Los 60 000 propuestos anteriormente se sustituyen en esta preparación por 150 000 acordados. Caché y razonamiento no se cuentan dos veces. Métricas ausentes o inválidas detienen la secuencia y marcan el total incompleto, no cero.

## Conexión y comprobaciones

Directorio privado nuevo, copias intactas de contrato/verificador, solución vacía. Prompts reducidos, configuraciones de roles existentes, captura completa de respuestas sintéticas, control de archivos protegidos/solo lectura, instantáneas y checkpoints. Las órdenes iniciales se archivan sin retransmitir; se conservan las pruebas de órdenes del revisor.

**100 tests de mantenimiento pasan**, con 18 nuevos de integración: captura, transmisiones, directorios exclusivos, rechazo del modo real antes de escribir, límites, métricas ausentes/inválidas, costes registrados tras fallo, escrituras prohibidas, thread reutilizado, salida truncada, límites de palabras y manifiesto bloqueado.

Simulación completa: tres fases, 39 tokens **ficticios**, sobres de 1 652 / 2 078 / 2 280 caracteres, sin veredicto de calculadora. Dos sesiones sintéticas de 75 000 tokens bloquean la tercera. Los contadores históricos como fixtures terminan en 113 774, bajo el umbral pero sobre el objetivo; no es otra medida del modelo.

## Límites y siguiente entrega

El umbral impide una fase posterior, no limita la sesión activa. Una fase final completada con exceso conserva su estado completo y registra el exceso. Los límites de palabras se auditan, no se fuerzan en el modelo.

El CLI solo admite simulación; cambiar el manifiesto no activa el modo real. El callback inyectable es para tests. **Antes del benchmark faltan adaptador de transporte real, autorización de intento y congelación de campaña nueva.** Control de alteraciones no equivale a aislamiento completo. Sin garantía de ahorro de cuota ni ventana de abono. Histórico, gobernanza general y directorio .github/ no seguido del usuario intactos.

[JSON — CLI simulation](v2-2-lean-preflight.json) · [Manifest](../governance/v2-2-lean-draft.json) · [Launcher](../scripts/run_v2_2_lean.py) · [Tests](../tests/test_v2_2_lean.py) · [Audit](v2-2-cost-audit.es.md) · [README](../README.es.md)
