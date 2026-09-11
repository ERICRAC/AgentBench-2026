# Gobernanza pública

[Français](README.md) · [English (UK)](README.en.md) · **Español** · [Português](README.pt.md)

**V2.2: 57 tests correctos; tres sondas CLI siguen en 7/8.** Paquete oficial separado reproduce el bloqueo. Sin modelo ni cambios de instalaciones existentes. **Astra alto: solo histórico.** [CLI](../results/v2-2-cli-qualification.es.md)

Este directorio publica el método necesario para entender y reproducir el
experimento sin exponer conversaciones completas ni la configuración privada
del autor.

- [`RESPONSE_FORMAT.es.md`](RESPONSE_FORMAT.es.md) define las restituciones.
- [`LOGGING.es.md`](LOGGING.es.md) define el registro público.
- [`EXPERIMENTAL_DESIGN.es.md`](EXPERIMENTAL_DESIGN.es.md) define la matriz,
  los hitos de observación y las repeticiones.
- [`V2_PROTOCOL.es.md`](V2_PROTOCOL.es.md) preinscribe la organización
  multiagente, los límites de contexto y las medidas.
- [`PV_TEMPLATE.es.md`](PV_TEMPLATE.es.md) define textos interagente,
  decisiones, relación social y eficiencia.
- [`../logs/history.es.md`](../logs/history.es.md) conserva el historial resumido.

La precedencia es: reglas del repositorio, contrato del intento, prompt del
modo, decisión del orquestador y veredicto del verificador independiente. Una
instrucción local no puede debilitar la seguridad, modificar las pruebas ni
permitir la lectura de otra solución.

La gobernanza evoluciona únicamente cuando una aclaración o un error produce
una regla útil, verificable y reutilizable. Nunca reescribe un run terminado.
Un verificador nuevo se calibra antes de congelarlo; un sesgo descubierto
después del primer candidato se documenta y no se elimina en silencio.

La documentación editorial pública existe en francés, inglés británico,
español y portugués. Las instrucciones de agentes, prompts, retos congelados,
trazas y entregables de runs siguen siendo pruebas canónicas e inmutables.

La regla Git global corresponde al orquestador después del run. Los candidatos
solo escriben en `solution/` y no crean commits ni hacen push.
