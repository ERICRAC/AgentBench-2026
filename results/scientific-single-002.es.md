# Resultado detallado — `scientific-single-002`

[Français](scientific-single-002.md) · [English (UK)](scientific-single-002.en.md) · **Español** · [Português](scientific-single-002.pt.md)

## Resumen ejecutivo

La segunda referencia V1 de la **Calculadora Scientific** alcanzó **9 pruebas
de 9**. Un solo agente entregó análisis seguro, muestreo, SVG y CLI sin
dependencias externas ni ayuda funcional humana.

El primer verificador oficial se detuvo al cargar el módulo por la interacción
conocida entre `dataclass` y el cargador dinámico bajo Python 3.13. Bastó una
corrección específica. Esta ejecución es la referencia actual para V2;
`scientific-single-001` sigue publicada.

| Dato | Valor |
| --- | --- |
| Modo / objetivo | V1 · Codex solo / Calculadora Scientific |
| Modelo / esfuerzo | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Contexto / compactación | 200.000 / 180.000 tokens, alcance `total` |
| Subagentes / ayuda funcional humana | 0 / 0 |
| Primera pasada | fallo al cargar el módulo |
| Resultado final candidato / independiente | **9/9 / 9/9** |

La solución usa un tokenizer de lista blanca y un parser recursivo. Las
funciones se mapean explícitamente, el muestreo separa valores indefinidos y el
SVG pasivo escapa el título. La CLI recupera el control tras los errores.

| Métrica | Valor observado |
| --- | ---: |
| Duración redondeada | 541 s |
| Entrada / caché | 587.315 / 541.312 tokens |
| Salida / razonamiento incluido | 16.177 / 6.289 tokens |
| Entrada + salida | 603.492 tokens |
| Comandos / lotes de cambios | 16 / 2 |
| Código / documentación | 487 / 97 líneas |

La entrada es acumulada e incluye caché. El verificador conserva un sesgo de
carga con ciertas `dataclass`; el muestreo uniforme también puede omitir una
discontinuidad entre puntos. El intento Git del candidato no cambió el remoto.

Véanse la [traza](../runs/scientific-single-002/trace.md) y los
[metadatos](../runs/scientific-single-002/run.json).
