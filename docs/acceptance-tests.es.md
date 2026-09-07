# Catálogo de pruebas de aceptación

[Français](acceptance-tests.md) · [English (UK)](acceptance-tests.en.md) · **Español** · [Português](acceptance-tests.pt.md)

## Cómo leer los veredictos

`unittest` cuenta una unidad por **método de prueba**. AgentBench tiene seis
grupos Core y nueve Scientific. En una ejecución totalmente correcta, estos
15 grupos realizan **71 aserciones elementales**: 14 Core y 57 Scientific.
El resultado debe mostrar ambos niveles: **6/6 grupos Core — 14/14 controles
superados**.

Ruta de auditoría: [especificación Core](../challenges/calculator/SPEC.md) →
[tests Core](../challenges/calculator/tests/test_acceptance.py) →
[especificación Scientific](../challenges/scientific-calculator/SPEC.md) →
[tests Scientific](../challenges/scientific-calculator/tests/test_acceptance.py) →
[resultados](../results/README.es.md).

## Calculadora Core — 6 grupos, 14 controles

- [ ] **C01 · Entregables (2):** existen `calculator.py` y `README.md`.
- [ ] **C02 · Ejecución dinámica (1):** no hay `eval()` ni `exec()`.
- [ ] **C03 · Aritmética (4):** suma, resta negativa, multiplicación decimal
  y división fraccionaria se verifican por separado.
- [ ] **C04 · Operador desconocido (1):** `%` produce `ValueError`.
- [ ] **C05 · División por cero (1):** produce `ZeroDivisionError`.
- [ ] **C06 · Resiliencia CLI (5):** código 0, sin traceback, resultados 5 y
  -8 antes y después de errores, y mensaje comprensible.

[Ver los seis métodos](../challenges/calculator/tests/test_acceptance.py#L23).

## Calculadora Scientific — 9 grupos, 57 controles

- [ ] **S01 · Entregables y documentación (7):** dos archivos y cinco términos
  obligatorios en el README.
- [ ] **S02 · Seguridad y dependencias (2):** sin ejecución dinámica y solo
  biblioteca estándar.
- [ ] **S03 · Operadores (10):** cinco expresiones; tipo `float` y valor para
  cada una.
- [ ] **S04 · Lenguaje matemático (6):** trigonometría, inversas, funciones,
  constantes y notación científica.
- [ ] **S05 · Variables y nombres prohibidos (5):** `x` válido y cuatro casos
  inseguros o desconocidos rechazados.
- [ ] **S06 · Errores (6):** vacío, sintaxis, dominios, overflow y división por
  cero.
- [ ] **S07 · Muestreo (8):** cantidad, extremos, centro, discontinuidad y tres
  parámetros inválidos.
- [ ] **S08 · SVG pasivo (7):** raíz, ejes, curva, ausencia de contenido activo,
  escape y ausencia de puntos finitos.
- [ ] **S09 · CLI (6):** salida limpia, recuperación, resultado, error,
  historial y archivo SVG.

[Ver los nueve métodos](../challenges/scientific-calculator/tests/test_acceptance.py#L28).
El [catálogo francés](acceptance-tests.md) detalla las 71 entradas y resultados.

## Límites

Los 71 controles describen la cobertura actual, no una calidad absoluta. No
sustituyen análisis exploratorios ni repeticiones estadísticas. Una nueva
aserción oficial definiría otra suite y otra campaña.
