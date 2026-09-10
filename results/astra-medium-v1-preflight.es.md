# Preflight V1 Astra medio — preparado, no iniciado

[Français](astra-medium-v1-preflight.md) · [English (UK)](astra-medium-v1-preflight.en.md) · **Español** · [Português](astra-medium-v1-preflight.pt.md)

Documento histórico: ambas V1 ya terminaron. El control 44/44 siguiente describe la preparación y debe rechazar estos directorios ejecutados. El resto conserva las autorizaciones y observaciones de aquella etapa. [Balance completo y pruebas](astra-medium-v1-v2.es.md)

Dos tentativas solo nuevas preparadas. **44/44 controles estáticos correctos; ningún candidato, llamada de prueba al modelo ni resultado.** Solo se autorizó preparación. El modelo del chat no sustituye configuraciones explícitas de futuros candidatos.

## Tentativas reservadas

- Calculadora simple : [astra-medium-core-v1-001](../runs/astra-medium-core-v1-001/run.json) · [configuration](../runs/astra-medium-core-v1-001/config.toml) · [challenge](../runs/astra-medium-core-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-core-v2-001/run.json)
- Calculadora científica : [astra-medium-scientific-v1-001](../runs/astra-medium-scientific-v1-001/run.json) · [configuration](../runs/astra-medium-scientific-v1-001/config.toml) · [challenge](../runs/astra-medium-scientific-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-scientific-v2-001/run.json)

Cada directorio contiene CHALLENGE.md, config.toml y run.json. Ambos solution/ locales están vacíos, sin .gitkeep ni solución anterior consultada/copiada. Git no conserva directorios vacíos: recrearlos después de clonar con comandos siguientes.

## Comparabilidad y medición

Campaña asociada astra-medium-001: **extensión V1 preparada después de las V2 completas**, sin alterar metadatos. Candidato solo nuevo, sin delegación; orquestador de preparación/publicación fuera de medidas. Publicar Core antes de Scientific, sin refinamiento intermedio.

| Elemento | Decisión y prueba |
| --- | --- |
| Modelo / esfuerzo | gpt-6-astra / medium; igualdad comprobada con cuatro roles V2. |
| Contexto / compacción | 200 000 / 180 000, alcance total como V2; no es límite de consumo acumulado. |
| Configuración V1 | Copia de governance/astra-v1.toml; solo high → medium. Gobernanza intacta. |
| Permisos | workspace-write para V1/MAIN V2; read-only para consultores. Web desactivada, approval never, sin delegación. Escritura limitada a solution/ por instrucciones, no prueba de aislamiento real. |
| Prompts | codex-single.md y scientific-single.md históricos, hashes congelados; sin consejos V2 añadidos. |
| Desafíos / árbitros | Hashes iguales a V2; simple 6 grupos/14 controles; científica 9/57. [Lista explícita](../docs/acceptance-tests.es.md). |
| Captura | scripts/capture_session.py histórico intacto, sin wrapper nuevo. Duración CLI; V2 incluye además relevo, diferencia organizativa documentada. |
| Entorno observado | CLI 0.153.4, Python 3.13.5, Node 20.19.2, npm 9.2.0. Misma CLI V2; otros detalles históricos no certificados aquí. |
| Resultados futuros | Primer/final/independiente, correcciones antes/después, duración, entrada/caché/salida/razonamiento, intervenciones y textos. Actualmente null, no cero. |

V2 usa siete sesiones/cuatro roles; V1 prevé una. Primer pase V2 tras crítica obligatoria, no así V1. Diferencias del tratamiento experimental, no parámetros a igualar retroactivamente.

## Checklist del preflight

El [control reproducible](../scripts/preflight_v1_medium.py) realiza **22 aserciones por directorio, 44 en total**:

- [x] Configuración V1 igual salvo esfuerzo; identidad/modo; preparado y lanzamiento no autorizado.
- [x] Sin resultados inventados; solución presente, vacía y declarada escribible.
- [x] Seis hashes: configuración, prompt, desafío, tests, captura y verificador.
- [x] Desafío igual a SPEC; referencia V2 completa en campaña asociada.
- [x] Hashes de desafío/tests comunes; parámetros y permisos de cuatro roles verificados.
- [x] Recuento sintáctico de métodos (6/9), sin ejecutarlos; CLI registrada igual.

codex --version y codex exec --help correctos y muestran opciones. Advertencia local: alias PATH no creados por sistema de archivos de solo lectura; ambos comandos funcionan. TOML analizado, **no validado mediante lanzamiento Codex con estas configuraciones**.

```bash
mkdir -p runs/astra-medium-core-v1-001/solution runs/astra-medium-scientific-v1-001/solution
python3 -B scripts/preflight_v1_medium.py
```

## Ejecución futura — no autorizada aquí

Solo tras nueva autorización: comprobar entorno, hashes, cuota y directorios; ejecutar Core nuevo con configuración propia y prompt histórico; verificar y publicar antes de Scientific. Conservar interrupciones; reinicio desde cero recibe identificador nuevo.

Captura privada fuera del repositorio; publicar acta filtrada con rol, mandato exacto, mensajes visibles, comandos, controles y decisiones. Sin razonamiento privado, secretos ni horas en Markdown. No atribuir nuevas anotaciones/contadores a los históricos.

## Límites, presupuesto y continuación

**Preparación estática lista; lanzamiento no autorizado.** Acceso Astra, autenticación, cuota y aplicación real de contexto/esfuerzo sin probar. Sin instalaciones adicionales identificadas. Configuración explícita según [documentación oficial Codex](https://learn.chatgpt.com/docs/config-file/config-reference), sin garantía de acceso de la cuenta.

Coste exacto desconocido; ningún nuevo límite de tokens totales/tiempo. Añadirlo cambia condiciones frente a V2 y exige arbitraje distinto. Tokens de preparación no son coste candidato.

Mismo alias no prueba snapshot servidor inmutable; V1 posterior a V2, sin aleatorización/repeticiones, variación de carga/caché y posibles defectos del cargador científico congelado limitan causalidad. **Comparación cualificada, no identidad perfecta.** Se conserva dominancia calidad/tiempo/tokens.

Próxima decisión: autorizar V1 simple por separado, publicar antes de científica. Sin V2.1/V2.2 ni cambio de gobernanza.

[V2 Astra medium](astra-medium-v2.es.md) · [Conclusions](CONCLUSIONS.es.md) · [README](../README.es.md)
