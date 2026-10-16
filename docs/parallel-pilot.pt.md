# Próximo piloto — calculadora modular e desenvolvimento paralelo

[Français](parallel-pilot.md) · [English (UK)](parallel-pilot.en.md) · [Español](parallel-pilot.es.md) · [Português](parallel-pilot.pt.md)

## Decisão de preparação

**Preparação sem modelos; protocolo proposto, não congelado. Nenhum novo candidato executado.**
A comparação procura **menor tempo de entrega com qualidade comparável**. Tokens são uma restrição e um resultado separado; maior rapidez com mais tokens será uma contrapartida.
[Análise que fundamenta a decisão](../results/intermediate-review.pt.md).

Nome proposto: **V2.1 leve**, dois programadores, um dos quais integra depois. Substitui a proposta de quatro papéis apenas neste piloto. A V2 histórica não muda. O seu protocolo de escritor único não autoriza esta organização; a nova campanha terá de fixar as permissões.

## Âmbito proposto

Nova **calculadora científica modular com processamento por lotes**, apenas biblioteca padrão Python, sem dependências de execução, `eval` ou `exec`. Uma expressão inválida gera um erro local e as seguintes continuam.

| Ficheiro | Responsabilidade | Responsável durante o paralelo |
| --- | --- | --- |
| `engine.py` | Expressões seguras e amostragem com descontinuidades | DEV-A, motor |
| `presentation.py` | SVG, lotes JSON e resultados de erro | DEV-B, apresentação |
| `cli.py` | Comandos, entradas, saídas e erros | DEV-B |
| `README.md` | Uso, contratos, limites e exemplos | DEV-B |
| Todos | Integração, correções e verificação final | DEV-A, sessão INT |

O solo recebe as mesmas interfaces, decomposição, exemplo de lote e comandos de teste, escolhendo a ordem do trabalho. Nenhum esqueleto funcional fica reservado à equipa.

Interfaces a especificar:

- `engine.evaluate(expression, variables=None) -> float`: sintaxe científica e precedências explícitas no novo contrato, sem importar soluções históricas.
- `engine.sample_curve(expression, x_min, x_max, samples=201)`: pares com `None` para valores indefinidos.
- `presentation.write_svg(points, output_path, title="")`: XML válido, texto escapado e segmentos separados.
- `presentation.run_batch(jobs)`: resultados ordenados `{"ok": true, "value": número}` ou `{"ok": false, "error": texto}`. Cada tarefa inclui `expression` e opcionalmente `variables`.
- `python cli.py batch INPUT.json OUTPUT.json`: estrutura inválida produz saída não nula e mensagem sem traceback. Erros de expressões ficam nos resultados; as restantes continuam.
- `python cli.py plot EXPRESSION OUTPUT.svg --min A --max B --samples N`: amostragem e exportação para o ficheiro escolhido.

Antes do congelamento: fixar tipos, números não finitos, limites numéricos e de tamanho, códigos de saída, substituição de ficheiros e erros de domínio. O verificador não deve inventar estas escolhas.

## Controlos independentes previstos

Caixas por marcar: **requisitos previstos, não testes executados nem pontuação**.

- [ ] M01: importação padrão, entregáveis e mecanismos proibidos.
- [ ] M02: quatro operações, precedências, parênteses, potências e sinais.
- [ ] M03: funções, constantes, variável e nomes proibidos.
- [ ] M04: sintaxe inválida, domínios e resultados não finitos.
- [ ] M05: limites, número de pontos e descontinuidades.
- [ ] M06: SVG analisável, título escapado e ausência de pontes sobre descontinuidades.
- [ ] M07: lote misto, ordem preservada e continuação após erro.
- [ ] M08: estrutura JSON inválida e erros da CLI.
- [ ] M09: integração real motor → lote e motor → curva → SVG.
- [ ] M10: API documentada, exemplos executáveis e responsabilidades.

Publicar casos elementares e contagens após implementar a suite. Calibrar o carregador com construções Python padrão e implementações equivalentes; injetar defeitos conhecidos para testar a deteção. Reservar avaliação independente de robustez sem chamar ocultos aos testes públicos. Os 6/9 grupos históricos não mudam.

## Organização e observação

V1: uma sessão nova, um candidato, todo o âmbito. V2.1 leve: duas sessões simultâneas em diretórios isolados, com contrato comum e missão própria. Nenhum lê os ficheiros ativos do outro. O orquestrador reúne instantâneos terminados sem os editar e inicia INT com ambas as entregas e notas. INT pode corrigir todos os ficheiros; atribuir cada alteração.

A integração aguarda ambos os programadores. Ficheiros fora do âmbito, entregáveis ausentes ou falhas de transporte interrompem a tentativa com preservação de provas, sem repetição automática. Validar isolamento com candidatos fictícios antes de modelos reais.

Guardar mandatos, respostas visíveis e mensagens de integração. Numerar constatações e ligar cláusula, prova, decisão, alteração e controlo. Medir defeitos corrigidos, regressões, falsos positivos e duplicação. Melhor documentação só constitui ganho medido com uma grelha prévia.

Medir tempo total, sobreposição real, soma dos tempos dos agentes, integração e verificação separadamente. Publicar tokens de entrada, cache e saída por sessão, custos das interrupções e preparação fora do candidato.

## Orçamento proposto e revisão

Astra médio para ambas as organizações. Proposta para aprovação no congelamento: **um piloto solo seguido de um paralelo**, limiar **entre sessões de 150 000 tokens por organização**, **300 000 nominais para o par**, sem repetições. As sessões paralelas podem ultrapassar conjuntamente o limiar antes do controlo seguinte; não é um teto rígido nem garante a quota Plus.

O solo pode exceder o limiar na única sessão. Publicar qualidade e custo antes da equipa; não a iniciar automaticamente se o orçamento disponível ou a medição impedirem cumprir o acordo. Equilibrar a ordem nas repetições. Um par continua exploratório.

**Lembrete: revisão especializada do protocolo final pelo modelo mais potente disponível antes do congelamento e lançamento.** Não se certifica aqui a classificação nem a capacidade efetiva. Preparação autorizada; âmbito e orçamento da execução dependem de aprovação sobre artefactos prontos.

## Navegação e diagnóstico de ligações

Os quatro ficheiros existem. URLs com o domínio interno `vscode-cdn.net` vêm da apresentação do editor e não estão nos Markdown. O cliente WSL não pode ser verificado aqui. Abrir com **Ctrl+P** a partir da raiz:

```text
scripts/audit_intermediate.py
results/intermediate-review-data.json
results/CONCLUSIONS.md
docs/acceptance-tests.md
```

`python3 -B scripts/check_links.py` percorre Markdown versionados, ligações relativas, referências, imagens HTML e âncoras de títulos. As âncoras GitHub são aproximadas; não substitui um navegador nem consulta sites externos.

Quatro ligações indisponíveis permanecem em mensagens históricas imutáveis. Alternativas publicadas: [código simples](../runs/astra-medium-core-v2-2-supervised-002/solution/calculator.py), [documentação simples](../runs/astra-medium-core-v2-2-supervised-002/solution/README.md), [código científico](../runs/astra-medium-scientific-v2-2-lean-002/solution/scientific_calculator.py), [documentação científica](../runs/astra-medium-scientific-v2-2-lean-002/solution/README.md).

## Estado

Âmbito e orçamento propostos; nenhuma nova suite congelada, lançador paralelo pronto ou chamada a modelos. Próxima entrega técnica conjunta: especificação completa, suite calibrada e transporte isolado simulado antes do lançamento.
