# V2.2 — transporte, aislamiento y modelos

[Français](v2-2-transport.md) · [English (UK)](v2-2-transport.en.md) · **Español** · [Português](v2-2-transport.pt.md)

## Resumen

**Piloto aprobado; lanzamiento bloqueado.** Un intento por calculadora, sin nuevo límite global, parada al agotar cuota, sin reintento automático. Astra medio sigue activo. Ni 18 repeticiones ni una prueba modelo están autorizadas.

Transporte mediante procesos reales y aislamiento local probados; integración modelo autenticada aún no cualificada. Sin congelar protocolo, llamadas modelo ni nuevas puntuaciones.

## Verificación

- [x] 46 tests de mantenimiento: 38 anteriores y 8 nuevos.
- [x] Bubblewrap: **30/30 controles** con testigos desechables.
- [x] Dos simulaciones del relé, tres procesos Python aislados por desafío: MAIN inicial, REV-01 y MAIN final. Respuestas ficticias; consumo modelo y veredicto ausentes.
- [x] Contraprueba Codex nativo: **26/30**, cuatro desviaciones conservadas.
- [ ] Cualificar transporte autenticado y todas las herramientas candidatas.
- [ ] Congelar y solicitar autorización separada para la calculadora simple.

[Observaciones y hashes](v2-2-transport.json) · [Preflight estático actualizado](v2-2-preflight-approved.json) · [Etapa anterior](v2-2-preflight.es.md)

Catorce controles por rol: leer contrato/solución; crear, modificar, renombrar y borrar solución (permitido MAIN, prohibido REV); denegar lectura/escritura exterior directa y por enlace simbólico, escritura del contrato y conexión loopback al host; preservar contrato/testigo del host. Dos controles sin sandbox confirman acceso al testigo y conexión antes de aislar.

Solo se crean y retiran testigos propios, sin secretos reales ni Internet. Bubblewrap monta directorios de ejecución y workspace en lectura, solución escribible solo para MAIN, raíz sintética de solo lectura, red separada y entorno limpio.

**Desviación nativa:** lectura del testigo host denegada, archivos host intactos, pero se permite crear esa ruta en la capa sintética, directamente y por enlace: dos desviaciones por rol. No demuestra fuga del archivo host; incumple nuestra prohibición estricta de escribir fuera de solution/. Un ensayo anterior en /tmp perdió lecturas necesarias al prohibir su padre; la prueba conservada reproduce la ubicación real de runs fuera de /tmp.

Bubblewrap no envuelve el CLI autenticado: no dispone de credenciales ni red modelo. Esto no valida todas las herramientas Codex. Sin alternativa permisiva.

## Transporte y límites

[Implementación](../scripts/v2_2_transport.py): archivos privados exclusivos de entrada/salida/error, sin shell, truncado aplicativo ni reintentos; estados ante fallo de creación, salida no nula y expiración. Se detiene el grupo de procesos al finalizar/interrumpir; SIGKILL del padre o fallo de máquina puede impedir cierre. Los 30 segundos pertenecen a las sondas, no al presupuesto candidato.

[Ocho tests](../tests/test_v2_2_transport.py): flujos exactos/permisos privados; salida 7 parcial; expiración/parada; salida de 2 MB; rechazo de reutilización; ejecutable ausente; comando sin sandbox_mode antiguo; rol/enlace inválidos.

OpenAI Docs orientó la separación de perfiles y sandbox_mode. Prima la sintaxis local: codex sandbox, sin subcomando linux. [Permisos](https://learn.chatgpt.com/docs/permissions). Constructor nativo experimental, no conectado al lanzamiento.

## Modelo, esfuerzo y organización

Totales terminados de ambas calculadoras; tokens entrada + salida, caché ya incluida. Puntuación final idéntica: 15 grupos / 71 controles.

| Organización | Modelo / esfuerzo | Tiempo total (s) | Tokens |
| --- | --- | ---: | ---: |
| V1 | Sol alto | 1199,432 | 454376 |
| V1 | Astra alto | 499,653 | 340988 |
| V1 | Astra medio | 287,132 | 217884 |
| V2 | Sol alto | 2384,139 | 1475626 |
| V2 | Astra medio | 1023,177 | 978998 |

[Sol/Astra V1](sol-vs-astra-v1.es.md) · [Sol V2](sol-v2.es.md) · [Astra medio](astra-medium-v1-v2.es.md) · [V2 alto interrumpido](astra-v2-retired.es.md)

V1 Astra alto: **56,5 % más tokens y 74,0 % más tiempo** que medio. Una observación y correcciones distintas no prueban causalidad. V2 científica alto interrumpida: sin total completo comparable; consumo ausente no es cero.

Agotamiento rápido de cuota: observación del usuario, no medida de cargo Plus. Faltan lecturas de cuota antes/después por run; no se garantiza que medio quepa ni que alto sea siempre imposible.

Conservar Sol alto y Astra alto. Comparar organización fijando modelo/esfuerzo; comparar modelo fijando organización/esfuerzo. Astra medio frente a Sol alto mezcla factores. V2.2 Sol alto futura requiere otra autorización.

## Reproducir y continuar

```bash
python3 -B -m unittest discover -s tests -v
python3 -B scripts/preflight_v2_2_isolation.py --backend bwrap
python3 -B scripts/preflight_v2_2_isolation.py --backend native
```

El último comando debe fallar actualmente. Sondas ejecutadas con autorización fuera de sandbox anidada, sin debilitar protección candidata.

Siguiente: conectar autenticación del orquestador y herramientas confinadas; prueba modelo solo autorizada. Sin nuevos paquetes necesarios: bubblewrap 0.12.0 presente. Evidencias históricas, desafíos y tests intactos.

[Protocolo](../governance/V2_2_PROTOCOL.es.md) · [Conclusiones](CONCLUSIONS.es.md) · [README](../README.es.md)
