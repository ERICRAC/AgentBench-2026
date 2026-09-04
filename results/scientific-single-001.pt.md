# Resultado detalhado — `scientific-single-001`

[Français](scientific-single-001.md) · [English (UK)](scientific-single-001.en.md) · [Español](scientific-single-001.es.md) · **Português**

## Resumo executivo

A primeira tentativa individual da Calculadora Scientific terminou com **9
testes em 9**. Um agente Codex entregou um analisador seguro, funções
científicas, amostragem de curvas, SVG autónomo e uma CLI documentada sem
dependências externas.

A primeira passagem oficial validou 3/9 grupos. Uma correção removeu uma
incompatibilidade com o carregador de testes e outra corrigiu a tokenização de
`log10`. O candidato convergiu sem ajuda funcional humana.

![Curva sin(x) produzida pela solução](assets/scientific-single-001-sine.svg)

O SVG é uma demonstração posterior ao run, não uma alteração do candidato.

## Identidade do run

| Dado | Valor |
| --- | --- |
| Identificador | `scientific-single-001` |
| Objetivo | Calculadora Scientific |
| Modo / arquitetura | Codex sozinho / um agente sem subagente |
| Modelo / raciocínio | `gpt-5.6-sol` / não exposto |
| Prompt | [`prompts/scientific-single.md`](../prompts/scientific-single.md) |
| Duração | 5 min 31 s |
| Intervenção humana funcional | Nenhuma |
| Primeira passagem | 3 êxitos, 6 erros |
| Resultado final / correções | 9/9 / 2 |

## Protocolo e implementação

Especificação, prompt e testes foram congelados em `71ae527` antes do run. O
candidato trabalhou num diretório limpo, não consultou outra solução e apenas
escreveu os dois entregáveis de `solution/`.

Um tokenizador de lista branca e analisador recursivo gerem notação científica,
parênteses, sinais unários, cinco operadores e potência associativa à direita.
Doze funções, `pi`, `e` e apenas `x` são ligados explicitamente a `math`.
Resultados complexos, não finitos ou fora do domínio geram `ValueError`; a
divisão por zero mantém `ZeroDivisionError`.

A amostragem divide pontos indefinidos e o SVG desenha eixos e segmentos,
escapa o título e não contém scripts nem recursos externos. A CLI avalia,
desenha, gere o histórico e recupera sem traceback.

## Percurso de validação

| Passagem | Resultado | Diagnóstico | Ação |
| --- | --- | --- | --- |
| Controlos dirigidos | Aprovados na trace | Casos sensíveis | Nenhuma |
| Verificador oficial 1 | 3/9, 6 erros | Interação `dataclass` / carregador | Substituir dataclass |
| Intermédia | Código 1, saída ausente | `log10` dividido | Alargar identificadores |
| Oficial final | 9/9 | Sem falha restante | Encerrar |
| Independente | 9/9 | Resultado reproduzido | Sem alteração |

O 8/9 intermédio referido pelo candidato não é uma medição segura porque a
saída não foi capturada. A [trace](../runs/scientific-single-001/trace.md)
preserva essa precisão.

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/scientific-single-001/solution
```

## Medições

| Indicador | Valor |
| --- | --- |
| Duração real | 331 segundos |
| Entrada / cache / sem cache | 324 237 / 303 360 / 20 877 tokens |
| Saída / raciocínio comunicado | 8 459 / 941 tokens |
| Comandos / lotes / mensagens | 8 / 3 / 9 |
| Ficheiros | 2 |
| Código / documentação | 352 / 64 linhas |
| Funções / classes | 16 / 2 |
| Dependências externas | 0 |

A entrada contém muita cache e não pode ser comparada diretamente com a
estimativa da Calculadora Core sem harmonizar o método.

## Incidentes, limites e conclusão

Um lançamento anterior falhou antes do modelo devido ao armazenamento Codex em
modo só de leitura e não entra na duração. O carregador rejeitou um `dataclass`
válido em uso normal; os testes não foram alterados. A amostragem uniforme pode
omitir descontinuidades, os testes SVG não avaliam todos os motores e faltam o
nível de raciocínio e a saída intermédia bruta.

V1 Scientific cumpre o contrato em 331 segundos e duas correções autónomas. A
futura V2 deverá superar o mero 9/9 com convergência mais rápida, menos correções
ou melhor relação qualidade/complexidade.
