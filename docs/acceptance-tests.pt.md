# Catálogo de testes de aceitação

[Français](acceptance-tests.md) · [English (UK)](acceptance-tests.en.md) · [Español](acceptance-tests.es.md) · **Português**

## Como ler os vereditos

O `unittest` conta uma unidade por **método de teste**. O AgentBench tem seis
grupos Core e nove Scientific. Numa execução totalmente bem-sucedida, estes
15 grupos realizam **71 asserções elementares**: 14 Core e 57 Scientific. O
resultado deve mostrar os dois níveis: **6/6 grupos Core — 14/14 controlos
aprovados**.

Percurso de auditoria: [especificação Core](../challenges/calculator/SPEC.md) →
[testes Core](../challenges/calculator/tests/test_acceptance.py) →
[especificação Scientific](../challenges/scientific-calculator/SPEC.md) →
[testes Scientific](../challenges/scientific-calculator/tests/test_acceptance.py) →
[resultados](../results/README.pt.md).

## Calculadora Core — 6 grupos, 14 controlos

- [ ] **C01 · Entregáveis (2):** existem `calculator.py` e `README.md`.
- [ ] **C02 · Execução dinâmica (1):** não existe `eval()` nem `exec()`.
- [ ] **C03 · Aritmética (4):** soma, subtração negativa, multiplicação decimal
  e divisão fracionária são verificadas separadamente.
- [ ] **C04 · Operador desconhecido (1):** `%` produz `ValueError`.
- [ ] **C05 · Divisão por zero (1):** produz `ZeroDivisionError`.
- [ ] **C06 · Resiliência CLI (5):** código 0, sem traceback, resultados 5 e -8
  antes e depois dos erros, e mensagem compreensível.

[Ver os seis métodos](../challenges/calculator/tests/test_acceptance.py#L23).

## Calculadora Scientific — 9 grupos, 57 controlos

- [ ] **S01 · Entregáveis e documentação (7):** dois ficheiros e cinco termos
  obrigatórios no README.
- [ ] **S02 · Segurança e dependências (2):** sem execução dinâmica e apenas
  biblioteca padrão.
- [ ] **S03 · Operadores (10):** cinco expressões; tipo `float` e valor para
  cada uma.
- [ ] **S04 · Linguagem matemática (6):** trigonometria, inversas, funções,
  constantes e notação científica.
- [ ] **S05 · Variáveis e nomes proibidos (5):** `x` válido e quatro casos
  inseguros ou desconhecidos rejeitados.
- [ ] **S06 · Erros (6):** vazio, sintaxe, domínios, overflow e divisão por zero.
- [ ] **S07 · Amostragem (8):** quantidade, extremos, centro, descontinuidade e
  três parâmetros inválidos.
- [ ] **S08 · SVG passivo (7):** raiz, eixos, curva, ausência de conteúdo ativo,
  escape e ausência de pontos finitos.
- [ ] **S09 · CLI (6):** saída limpa, recuperação, resultado, erro, histórico e
  ficheiro SVG.

[Ver os nove métodos](../challenges/scientific-calculator/tests/test_acceptance.py#L28).
O [catálogo francês](acceptance-tests.md) detalha as 71 entradas e resultados.

## Limites

Os 71 controlos descrevem a cobertura atual, não uma qualidade absoluta. Não
substituem análises exploratórias nem repetições estatísticas. Uma nova asserção
oficial definiria outra suite e outra campanha.
