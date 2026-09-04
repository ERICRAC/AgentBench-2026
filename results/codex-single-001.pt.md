# Resultado detalhado — `codex-single-001`

[Français](codex-single-001.md) · [English (UK)](codex-single-001.en.md) · [Español](codex-single-001.es.md) · **Português**

## Resumo executivo

Um único agente Codex realizou todo o objetivo Calculadora Core: análise do
contrato, desenho, implementação, documentação e validação. Não usou subagentes
nem dependências externas. A primeira passagem conhecida superou os seis
controlos sem ciclo de correção funcional registado.

Isto estabelece a referência V1 de conformidade. Não basta para avaliar a
eficiência, pois duração, nível de raciocínio e iterações detalhadas não foram
capturados.

## Identidade do run

| Dado | Valor |
| --- | --- |
| Identificador | `codex-single-001` |
| Objetivo | Calculadora Core |
| Modo | Codex sozinho |
| Arquitetura | Um agente generalista, sem subagente |
| Modelo observado | `gpt-5.6-sol` |
| Autenticação | ChatGPT Plus, sem chave API OpenAI |
| Prompt | [`prompts/codex-single.md`](../prompts/codex-single.md) |
| Criação e verificação | 2 de setembro de 2026 — hora não publicada |
| Consumo observado | Aproximadamente 18 086 tokens |
| Duração total / raciocínio | Não registados |
| Ambiente | Codex CLI 0.152.1, Python 3.13.5, WSL2 x86_64 |

## Governação e implementação

[`AGENTS.md`](../AGENTS.md), o
[`CHALLENGE.md`](../runs/codex-single-001/CHALLENGE.md) congelado, o prompt exato
e o verificador independente separaram as responsabilidades. O agente acumulou
os papéis de analista, arquiteto, programador e redator.

A solução separa `calculate`, `parse_expression` e `main`. Ramos explícitos
evitam execução dinâmica. Divisão por zero gera `ZeroDivisionError` e um
operador desconhecido gera `ValueError`. A CLI processa três elementos
separados por espaços, recupera sem traceback e termina corretamente.

## Validação independente

```bash
python3 scripts/verify.py --solution runs/codex-single-001/solution
```

| Controlo | Resultado |
| --- | --- |
| Ficheiros exigidos | Aprovado |
| Quatro operações e variantes numéricas | Aprovado |
| Operador inválido | Aprovado |
| Divisão por zero | Aprovado |
| Ausência de `eval()` e `exec()` | Aprovado |
| Sessão CLI recuperável | Aprovado |

Primeira passagem conhecida: **6/6**. Resultado final reverificado: **6/6**.

## Indicadores

| Indicador | Valor |
| --- | --- |
| Agentes / subagentes | 1 / 0 |
| Ficheiros entregues | 2 |
| `calculator.py` / README | 79 / 42 linhas |
| Dependências externas | 0 |
| Correções após a primeira passagem | 0 |
| Tokens | Aproximadamente 18 086 |

Não há intervenção humana registada durante a implementação. As tarefas Git,
SSH e de publicação posteriores não são ajuda funcional. Os limites são seis
controlos específicos, espaços obrigatórios na sintaxe CLI, duração e
raciocínio ausentes, tokens aproximados e nenhuma prova de superioridade geral
do modo individual.

V2 terá de fornecer um benefício observável além do mesmo resultado final para
justificar tempo, tokens e trocas adicionais.
