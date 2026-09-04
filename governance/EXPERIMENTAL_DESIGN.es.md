# Diseño experimental y comparabilidad

[Français](EXPERIMENTAL_DESIGN.md) · [English (UK)](EXPERIMENTAL_DESIGN.en.md) · **Español** · [Português](EXPERIMENTAL_DESIGN.pt.md)

Este documento fija la estructura de la campaña AgentBench 2026. Separa las
comparaciones obligatorias de las variantes exploratorias e impide que un
ajuste posterior reescriba condiciones ya publicadas.

## Matriz principal

| Modo | Objetivo Calculadora Core | Objetivo Calculadora Scientific |
| --- | --- | --- |
| V1 · Codex solo | obligatorio | obligatorio |
| V2 · Codex multiagente gobernado | obligatorio | obligatorio |
| V3 · Codex + Ollama | obligatorio | obligatorio |

Cada celda es un intento aislado con prompt identificado, configuración
registrada y veredicto independiente. V1, V2 y V3 son **modos de organización**,
no versiones del software.

## Hito de observación

Después de cada modo:

- publicar ambos resultados antes de modificarlos;
- consolidar puntuación, duración, tokens, correcciones, intervenciones y
  eventos de coordinación observados;
- formular conclusiones y límites antes de proponer cambios;
- asociar cada ajuste a una hipótesis medible y un criterio de decisión.

El ajuste puede afectar a modelo, prompt, roles, contexto o parámetros; no
implica necesariamente entrenar los pesos del modelo.

## Campañas y repeticiones

Una campaña queda identificada por las versiones de retos y verificadores, los
modelos, parámetros estructurales y prompts. Un cambio sustancial abre una
nueva campaña. Se repiten las celdas V1 hasta el modo estudiado necesarias para
comparar. Los resultados anteriores siguen publicados y nunca se sustituyen o
mezclan en silencio. Corregir un verificador tras el primer candidato crea una
nueva versión del reto.

Una corrección del candidato durante un run pertenece a ese run y no abre otra
campaña.

## Presupuesto cognitivo y escala

La versión exacta del modelo, el esfuerzo, la ventana de contexto y el umbral
de compactación son variables experimentales. Se fijan por agente antes del
run. El consumo acumulado de tokens se distingue del contexto disponible al
mismo tiempo.

Las dos calculadoras calibran el protocolo y pueden producir un efecto techo.
Un futuro reto mayor formará otra campaña, repetida en cada organización con
los mismos presupuestos, sin añadirse retroactivamente a las seis celdas.

## Variantes opcionales

**V2.1** puede probar una organización ajustada, en ambas dificultades, después
de publicar y analizar V2. No reemplaza V2 ni cuenta entre las seis celdas.

**V4** es un control histórico comparable del proyecto multiagente de Yann
Pointud llamado AutoGen, independiente del framework homónimo de Microsoft.
Solo se ejecuta si la síntesis V1–V3 aporta información útil y queda fuera de
la matriz principal.

## Comparación final

Los verificadores independientes dictan el veredicto funcional. La síntesis
compara como mínimo conformidad, duración, tokens, correcciones, intervenciones
humanas, desacuerdos, decisiones y coste de coordinación. Una mejora solo se
atribuye a la organización dentro de la misma campaña o calificando
explícitamente las diferencias de configuración.
