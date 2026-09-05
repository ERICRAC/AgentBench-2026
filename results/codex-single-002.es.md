# Resultado detallado — `codex-single-002`

[Français](codex-single-002.md) · [English (UK)](codex-single-002.en.md) · **Español** · [Português](codex-single-002.pt.md)

## Resumen ejecutivo

La segunda referencia V1 de la **Calculadora Core** superó **6 pruebas de 6**
en la primera ejecución oficial y en la verificación independiente. El
orquestador experimental encargó el trabajo a una sesión candidata Codex
distinta; esta trabajó sin consultores, subagentes ni ayuda funcional humana,
con modelo, esfuerzo y contexto fijados. Es la referencia actual para V2;
`codex-single-001` se conserva como primera observación histórica.

## Identidad y resultado

| Dato | Valor |
| --- | --- |
| Modo / objetivo | V1 · Codex solo / Calculadora Core |
| Modelo / esfuerzo | `gpt-5.6-sol` / `high` |
| Codex CLI | `0.152.1` |
| Contexto / compactación | 200.000 / 180.000 tokens, alcance `total` |
| Candidato / sus consultores o subagentes | sesión `codex exec` distinta / 0 |
| Ayuda funcional humana | 0 |
| Primera pasada / veredicto independiente | **6/6 / 6/6** |

El candidato implementó cuatro operaciones explícitas, análisis de entrada y
una CLI resistente. Tras el primer 6/6, un control manual solo detectó una
ubicación de lanzamiento ambigua en el README; se corrigió la documentación
sin cambiar el comportamiento.

## Medidas

| Métrica | Valor observado |
| --- | ---: |
| Duración redondeada | 193 s |
| Entrada / entrada en caché | 549.279 / 480.384 tokens |
| Salida / razonamiento incluido | 7.182 / 2.881 tokens |
| Entrada + salida | 556.461 tokens |
| Comandos / lotes de cambios | 17 / 2 |
| Código / documentación | 84 / 44 líneas |

Los tokens de entrada son acumulados e incluyen la caché. El candidato también
aplicó por error la regla Git global y trató de publicar; el remoto no cambió.
Los futuros prompts excluyen expresamente las operaciones Git.

Comando independiente: `python3 scripts/verify.py --solution
runs/codex-single-002/solution`. Véanse el [acta](../runs/codex-single-002/PV.md),
la [traza](../runs/codex-single-002/trace.md) y los
[metadatos](../runs/codex-single-002/run.json).
