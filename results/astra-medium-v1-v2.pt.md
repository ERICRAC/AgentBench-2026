# Astra médio — balanço V1/V2 e execução científica V1

[Français](astra-medium-v1-v2.md) · [English (UK)](astra-medium-v1-v2.en.md) · [Español](astra-medium-v1-v2.es.md) · **Português**

## Conclusão num minuto

**Nas duas calculadoras, V1 solo atinge a mesma pontuação oficial de V2 consultiva, com menos tempo e tokens.** No total, V2 utiliza **×3,56 o tempo e ×4,49 os tokens**. Estas medidas não mostram uma inversão favorável ao coletivo.

Pontuação igual não significa robustez igual. A revisão científica V2 corrigiu limites de comprimento/profundidade que a nova V1 mantém. A coordenação tem uma contribuição técnica observável, mas os testes oficiais atuais não valorizam esse benefício. Não significa que os consultores sejam inúteis.

## Mesmo modelo e esforço pedidos

gpt-6-astra / medium; contexto 200000, compactação 180000, âmbito total. V1 = um programador numa sessão. V2 = um escritor, três consultores, sete sessões por desafio; não programadores paralelos.

| Calculadora | Pontuação final V1 = V2 | Tempo V1 | Tempo V2 | V2/V1 | Tokens V1 | Tokens V2 | V2/V1 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Simples | 6/6 grupos · 14/14 controlos | 98.572 s | 375.169 s | ×3,81 | 98496 | 408616 | ×4,15 |
| Científica | 9/9 grupos · 57/57 controlos | 188.560 s | 648.008 s | ×3,44 | 119388 | 570382 | ×4,78 |
| Ambos os desafios | 15/15 grupos · 71/71 controlos | 287.132 s | 1023.177 s | ×3,56 | 217884 | 978998 | ×4,49 |

Todas as primeiras passagens oficiais têm sucesso; em V2 seguem a crítica obrigatória. Totais: soma destes dois runs terminados por organização, não de toda a campanha ou subscrição. Tokens = entrada + saída, incluindo cache e raciocínio. V2 científica acrescenta 459,448 s e 450 994 tokens face a V1.

De simples para científica, a razão temporal desce ligeiramente (3,81 → 3,44), mas a de tokens sobe (4,15 → 4,78). A dificuldade adicional não torna esta organização rentável segundo os indicadores oficiais. Dois exercícios e uma observação por célula não permitem extrapolar um limiar.

## Nova V1 científica — tratamento

Tentativa astra-medium-scientific-v1-001, autorizada após publicação Core. Diretório novo, prompt histórico, nenhuma solução anterior lida pelo candidato, nenhum consultor ou conselho V2. Lê o contrato, constrói um analisador recursivo restrito, reutiliza a árvore para amostrar, exporta SVG escapado e segmentado, acrescenta CLI, histórico e documentação.

Um controlo manual da CLI precede a única execução oficial: potências 512, -4 e 0,25; recuperação após divisão por zero; histórico apenas de sucessos. **9/9, confirmados independentemente 9/9, sem correção funcional posterior.** Código intacto em aaa83de. Ficheiros: 295 linhas Python, README 83, ata candidata 51; não é medida de manutenibilidade.

Duração: 188,560 s. Entrada: 113 746, cache incluída 98 944; saída: 5 642, raciocínio incluído 164. Total: 119 388. Cinco mensagens visíveis, seis comandos terminados, sem delegação. rg não encontra ficheiros no diretório vazio; ata extra além de dois entregáveis; redireções shell em vez de apply_patch: factos preservados, não penalizados pelo verificador.

## Lista científica — nove grupos, 57 controlos

- [x] S01 · Entregáveis e documentação — 7 controlos.
- [x] S02 · Biblioteca padrão e sem execução dinâmica proibida — 2.
- [x] S03 · Prioridades, parênteses, potências e sinais — 10.
- [x] S04 · Funções, constantes e notação científica — 6.
- [x] S05 · Variável x e nomes proibidos — 5.
- [x] S06 · Sintaxe, domínios e divisão por zero — 6.
- [x] S07 · Amostragem, extremos e descontinuidades — 8.
- [x] S08 · SVG válido, eixos, curva, título escapado e conteúdo inerte — 7.
- [x] S09 · CLI, curvas, histórico, recuperação e saída — 6.

[Cada caso e resultado esperado](../docs/acceptance-tests.pt.md) · [Seis grupos simples](astra-medium-v1-core.pt.md). Controlos exploratórios e candidatos não são acrescentados aos 71 oficiais.

## Contributo do coletivo apesar do sobrecusto

Na simples, V2 precisou sobretudo documentação, sem alteração funcional. Na científica, **SA-03 = subagente 3, revisor crítico**: MAIN eliminou limites de comprimento/recursão, protegeu a saída do terminal e tratou canais CLI com falhas. As revisões cruzadas corrigiram propostas sobre composição de funções e expressões indefinidas em todos os pontos. [Análise V2 e provas](astra-medium-v2.pt.md).

Após concluir V1, duas sondas exploratórias do orquestrador confirmam as restrições: `"1" + " " * 10000` deveria dar matematicamente 1 e `"+".join(["1"] * 1500)` deveria dar 1500; ambas produzem ValueError. Resultados na trace. **Sondas posteriores, apenas V1, não pré-registadas e fora da pontuação.** A prova V2 vem do relatório e controlos registados; não há repetição V2 idêntica aqui. Revelam uma limitação da pontuação, não uma estimativa exaustiva de superioridade V2.

## Limites e próxima decisão

Uma observação por célula; V1 posterior a V2; mesmo alias sem garantia de snapshot servidor; carga/cache variáveis. Tempo V1 inclui início/fim CLI, V2 também o relé; preparação, verificação posterior e publicação excluídas. O contexto configurado não é um limite de consumo total, nem a sua aplicação fica demonstrada. Custo monetário fiável não registado.

A referência Astra médio V1/V2 cobre agora ambos os exercícios. Proposta: pré-registar V2.2 (par leve), depois V2.1 (desenvolvimento paralelo), com orçamentos, repetições e robustez explícitos. Paralelismo real requer um desafio divisível. Sem outro lançamento ou alteração de governação aqui. [Conclusão central](CONCLUSIONS.pt.md).

## Auditoria — resumo e provas

[Ata científica: papéis, sequência e textos visíveis](../runs/astra-medium-scientific-v1-001/PV.md) · [Trace e sondas](../runs/astra-medium-scientific-v1-001/trace.json) · [Metadados](../runs/astra-medium-scientific-v1-001/run.json) · [Código](../runs/astra-medium-scientific-v1-001/solution/scientific_calculator.py) · [README candidato](../runs/astra-medium-scientific-v1-001/solution/README.md)

[V1 simples](astra-medium-v1-core.pt.md) · [V2 e atas](astra-medium-v2.pt.md) · [Preflight histórico](astra-medium-v1-preflight.pt.md) · [Índice](README.pt.md) · [Projeto](../README.pt.md)

## Verificação da publicação

Controlos de manutenção separados do benchmark: 12 testes unitários sem chamadas a modelos; ligações de 152 documentos editoriais e 64 hashes históricos; reprodutibilidade de cinco resumos V2; linter Markdown e git diff --check. Auditoria de 11 hashes da tentativa e contadores face à captura privada. Soluções anteriores, desafios, scripts, prompts e governação intactos. Removidas quatro linhas vazias duplicadas detetadas pelo linter; nenhuma correção do candidato.
