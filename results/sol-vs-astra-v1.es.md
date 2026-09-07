# V1 Sol vs Astra — control con el mismo perímetro

[Français](sol-vs-astra-v1.md) · [English (UK)](sol-vs-astra-v1.en.md) · **Español** · [Português](sol-vs-astra-v1.pt.md)

## Respuesta directa

Las cuatro soluciones alcanzan el veredicto oficial final: Core 6/6 y
Scientific 9/9. Sin embargo, en estas dos observaciones `gpt-5.6-sol/high`
consume **2,40 veces el tiempo** y **1,33 veces los tokens** de
`gpt-6-astra/high`. Scientific Sol también necesita una corrección después de
un primer 3/9, mientras Astra alcanza 9/9 en el primer pase oficial.

Esto favorece a Astra en eficiencia observada, pero no demuestra una
superioridad general: solo hay una repetición por celda y la generación es
estocástica.

## Perímetro controlado

La campaña `sol-high-control-001` se prerregistró en el commit `a616b2d`.
Especificaciones, tests, prompts, CLI `0.153.4`, Python `3.13.5`, capturador,
esfuerzo `high`, contexto cliente de 200k, compactación total a 180k, sesiones
efímeras nuevas, sandbox, red y topología en solitario coinciden con
`astra-high-001`. Las huellas SHA-256 validan las entradas.

El diff de configuración solo cambia el modelo. OpenAI documenta el esfuerzo
`high` y la misma ventana máxima para
[gpt-5.6-sol](https://developers.openai.com/api/docs/models/gpt-5.6-sol).
La infraestructura del servidor y la variabilidad no pueden congelarse: el
perímetro constante describe el protocolo cliente observable.

## Resultados

| Desafío | Medida | Astra/high | Sol/high | Diferencia Sol |
| --- | --- | ---: | ---: | ---: |
| Core | Primero / final / independiente | 6/6 · 6/6 · 6/6 | 6/6 · 6/6 · 6/6 | empate |
| Core | Duración | 100,175 s | 189,964 s | +89,6 % |
| Core | Entrada + salida | 120 478 | 158 101 | +31,2 % |
| Scientific | Primero / final / independiente | 9/9 · 9/9 · 9/9 | 3/9 · 9/9 · 9/9 | Sol corregido |
| Scientific | Duración | 399,478 s | 1 009,468 s | +152,7 % |
| Scientific | Entrada + salida | 220 510 | 296 275 | +34,4 % |
| **Total** | **Veredicto oficial final** | **15/15** | **15/15** | **empate** |
| **Total** | **Duración** | **499,653 s** | **1 199,432 s** | **+140,1 %** |
| **Total** | **Entrada + salida** | **340 988** | **454 376** | **+33,3 %** |

La caché ya está incluida en la entrada y el razonamiento en la salida.

## Calidad e interpretación

Core llega al techo oficial con ambos modelos sin corrección funcional. En
Scientific, Sol diagnostica y corrige una interacción del cargador Python 3.13
tras seis errores de importación. Astra obtiene 9/9 primero y después detecta y
corrige un defecto con flotantes extremos mediante controles suplementarios.

La misma suite de cuatro métodos creada por Astra se ejecutó después sobre
ambas soluciones: Astra 4/4; Sol 0/4 con seis aserciones fallidas. Es un dato
exploratorio, no oficial: no estaba prerregistrado y una aserción SVG impone una
estructura más estricta que el contrato. Los demás hallazgos sugieren hipótesis
sobre flotantes extremos, límites de complejidad y expresiones no válidas.

Conclusiones defendibles: igualdad oficial final, clara ventaja observada de
Astra en tiempo y tokens, autocorrección de ambos modelos en etapas distintas y
ninguna inferencia general con `n = 1`. Una campaña futura deberá prerregistrar
controles neutrales y repetir cada celda.

[PV Core Sol](../runs/sol-core-v1-001/PV.md) · [PV Scientific Sol](../runs/sol-scientific-v1-001/PV.md) · [Informe Astra](astra-v1.es.md)
