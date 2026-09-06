# Plantilla de acta multiagente

[Français](PV_TEMPLATE.md) · [English (UK)](PV_TEMPLATE.en.md) · **Español** · [Português](PV_TEMPLATE.pt.md)

Obligatoria desde V2, conserva los textos visibles entre agentes y los vincula
con decisiones, coste y resultado.

## Identificación y equipo

Registrar run, campaña, objetivo, patrocinador, orquestador experimental,
candidato principal/único escritor, verificador y resultado inicial/final.

| ID | Agente y profesión | Misión acotada | Entradas | Escritura | Modelo / esfuerzo | Contexto / compactación |
| --- | --- | --- | --- | --- | --- | --- |
| MAIN | Orquestador candidato / escritor | decidir, producir, verificar | reto, mensajes, solución | `solution/` | … | … |
| SA-01 | Analista de requisitos y seguridad | obligaciones, ambigüedades, amenazas | reto | ninguna | … | … |
| SA-02 | Arquitecto y especialista en testabilidad | estructura, invariantes, pruebas | reto | ninguna | … | … |
| SA-03 | Crítico QA adversarial | omisiones, regresiones, límites | reto, decisiones, solución | ninguna | … | … |

`run.json` conserva ID de thread, huella de configuración y métricas disponibles.

## Mensajes visibles

Crear una ficha numerada por mensaje. Conservar el texto íntegro después del
control de secretos y declarar toda omisión.

### MSG-001 — título

Registrar dirección, fase, duración y contadores de entrada/caché/salida/
razonamiento disponibles.

#### Texto enviado literalmente

> …

#### Texto devuelto literalmente

> …

**Síntesis analítica** — propuestas verificables, novedad, acuerdo,
contradicción o duplicado, riesgo detectado y decisión esperada de MAIN.

## Registro de decisiones

| ID | Fuente | Propuesta | Decisión | Motivo de MAIN | Prueba | Efecto |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | MSG-… | … | aceptada / rechazada / no verificable | … | archivo, prueba o control | ganancia, neutro o regresión |

Cada recomendación necesita decisión; las decisiones espontáneas de MAIN
también reciben ID.

## Relación social y eficiencia

Registrar mensajes, acuerdos, conflictos útiles/no resueltos, duplicados,
recomendaciones únicas, decisiones, defectos antes/después del verificador y
volumen de coordinación. Explicar influencia, consenso, desacuerdo útil y ruido.

Comparar V1/V2 en calidad inicial/final, tiempo mural, suma de tiempos-agente,
tokens de entrada + salida, tokens de coordinación y correcciones. Concluir por
separado los ganancias de calidad, tiempo y tokens: dominio, compromiso, sin
ganancia o no concluyente. No reconstruir razonamiento oculto.
