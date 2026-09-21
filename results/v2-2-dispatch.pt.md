# V2.2 — encaminhamento real após atualização

[Français](v2-2-dispatch.md) · [English (UK)](v2-2-dispatch.en.md) · [Español](v2-2-dispatch.es.md) · **Português**

## Veredicto final de qualificação — não pronto para congelar

**A qualificação termina com NO-GO para o dispositivo automatizado atual. Nenhum benchmark foi lançado.** Não é uma falha da calculadora ou do Astra: faltam integração do lançador e garantias completas de isolamento. Encerram-se as pequenas qualificações sucessivas; a próxima decisão é qual dispositivo utilizar.

| Requisito | Veredicto e prova |
| --- | --- |
| Programador → revisor → programador | Duas simulações repetidas, três sessões cada; sem pontuação candidata |
| Captura local de saídas | Aprovada: stdin, stdout, stderr, saída não nula, 2 MB sem truncagem e bytes não UTF-8 preservados |
| Interrupção do transporte local | Aprovada: timeout e SIGINT real; rastos parciais preservados, filho parado, estado interrupted |
| Isolamento de ferramentas | Parcial: provas anteriores Bubblewrap e oito recusas preservadas; sem nova certificação da cadeia completa |
| Proibição de delegação | Não demonstrada tecnicamente; nenhum spawn_agent tentado, listagem nativa anteriormente disponível |
| Lançador real completo | Não pronto: run_relay recusa simulation=False; ponte MCP testada separadamente, sem adaptador real ligado |
| Captura/paragem CLI → MCP → processo e acesso ao modelo | Não qualificados de ponta a ponta; sem chamada autenticada nem garantia de quota |

**68 testes de manutenção aprovados**, não 68 testes da calculadora. Dois testes novos cobrem captura binária exata e SIGINT com verificação da paragem do filho. O comando preparado de `codex exec` usa agora `-c default_permissions=...` em vez de `-P`; o caminho sandbox existente mantém `-P`. A análise de argumentos com `--help` termina com código zero: não comprova carregamento do perfil nem isolamento efetivo.

OpenAI Docs orientou esta correção; configuração presumida não substitui provas de execução. [Permissões oficiais](https://learn.chatgpt.com/docs/permissions). [Avaliação estruturada](v2-2-qualification.json) · [Testes do transporte](../tests/test_v2_2_transport.py) · [Lançador bloqueado](../scripts/run_v2_2.py).

### Simplificação proposta — por aprovar, não aplicada

Um **piloto supervisionado** com três sessões CLI novas, Astra médio: programador, revisão de instantâneo, correções. Uma pasta nova fora do repositório apenas com o desafio e entregáveis; captura de mensagens visíveis, métricas disponíveis, diferenças e veredicto independente. Sem ponte MCP personalizada nem framework adicional.

**Compromisso explícito:** pastas separadas e instruções não equivalem a isolamento técnico completo. Não delegação e acessos seriam controlados por instruções e auditoria dos rastos disponíveis, sem afirmar ausência de acessos não observados. Qualquer infração observada invalidaria o run; nenhuma proteção de segredos seria removida automaticamente. Documentar as permissões exatas antes do lançamento.

Piloto exploratório com diferenças publicadas; sem comparação histórica estritamente homogénea sem referência V1 nas mesmas condições. Alternativa: manter o isolamento forte e aceitar um projeto de integração separado antes do benchmark.

**Decisão solicitada: aceitar o piloto supervisionado em vez de continuar o dispositivo automático reforçado?** Isto não autorizaria o lançamento: primeiro rever e congelar explicitamente o âmbito. Governação geral, desafios e resultados históricos intactos.

## Provas anteriores preservadas

## Continuação — verificação de escritas nativas

**Oito sondas adicionais: quatro destinos × dois binários, oito recusas explícitas e todos os ficheiros testemunha intactos.** `apply_patch` está disponível, mas não permite estas escritas com `sandbox_mode="read-only"` e `approval_policy="never"`. Esta dúvida específica fica resolvida, não todo o preflight V2.2.

| Destino sintético da alteração | CLI 0.153.4 | Extensão 0.154.0-alpha.6.2 |
| --- | --- | --- |
| Ficheiro em solution/ | Recusado, intacto | Recusado, intacto |
| CHALLENGE.md fictício na pasta superior | Recusado, intacto | Recusado, intacto |
| Ficheiro fora do workspace | Recusado, intacto | Recusado, intacto |
| Ligação simbólica ao ficheiro externo | Recusado, destino e ligação intactos | Recusado, destino e ligação intactos |

Cada sonda cria uma pasta temporária nova, três ficheiros testemunha e uma ligação. O fornecedor local devolve uma única instrução fixa de alteração. Depois, o verificador compara os bytes dos três ficheiros e o destino da ligação; a pasta temporária é então eliminada. O ficheiro «externo» continua na nossa árvore temporária: nenhum dado do utilizador é visado. Não é utilizado modelo candidato, conta, segredo ou subagente.

**66 testes de manutenção aprovados**, incluindo três novos: destinos relativos fixos; recusa de ampliar a aprovação MCP aos patches; reconhecimento estrito da recusa observada. As oito sondas CLI são distintas destes testes unitários. [Provas JSON das oito sondas](v2-2-native-patch.json) · [Fontes dos testes](../tests/test_v2_2_dispatch.py).

O estado global continua `blocked_tool_catalog`, não «preflight validado». Os resultados anteriores e o respetivo JSON são preservados. A recusa nativa é testada com uma ponte REV-01; não valida a integração final MAIN, leituras nativas, interrupções, captura completa ou proibição de criar agentes. Não foi tentada nenhuma chamada a `spawn_agent`.

OpenAI Docs orientou a manutenção de dois controlos: sandbox de leitura e política sem aprovação. A integridade é comprovada pelas sondas locais, não pela documentação. [Documentação oficial](https://learn.chatgpt.com/docs/agent-approvals-security).

Reprodução sem modelo, um destino de cada vez; outras fixtures: `patch_contract`, `patch_outside`, `patch_symlink`. Selecionar outra instalação com `--cli CAMINHO_DO_BINARIO`, sem alterar PATH. A saída não nula continua esperada: paragem voluntária do fornecedor e catálogo não conforme.

```bash
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture patch_solution --enable-code-mode-host-for-probe
```

**Seguinte:** qualificar o bloqueio de delegação sem iniciar um candidato; depois, interrupções e captura. Astra médio mantido; sem congelamento nem lançamento automático.

## Etapa anterior — encaminhamento MCP

Atualização da extensão visível: 0.154.0-alpha.6.2, antes 0.154.0-alpha.6.1. CLI do terminal mantém 0.153.4 com hash igual. Não alterámos configurações globais, PATH, conta ou ficheiros VS Code.

**Percurso CLI → executor → MCP → Bubblewrap → resposta demonstrado com printf fixo. Funciona nas duas versões após ativar o host Code Mode e aprovar apenas a ferramenta MCP da sonda. Sucesso não atribuível apenas à atualização.**

63 testes de manutenção aprovados, 6 novos de fixtures/respostas. Oito sondas diagnósticas distintas: não oito benchmarks nem validações globais.

| Sonda | Versão | Observação |
| --- | --- | --- |
| Host desativado | 0.153.4 | Execução recusada: code-mode host is disabled |
| Inventário real | 0.153.4 | Seis ferramentas disponíveis |
| Ponte aprovada | 0.153.4 | printf executado, saída exata, código zero |
| Inventário atualizado | 0.154.0-alpha.6.2 | Mesmo inventário de seis ferramentas |
| Ponte sem aprovação | 0.154.0-alpha.6.2 | Aprovação recusada; sem tools/call MCP |
| Ponte atualizada aprovada | 0.154.0-alpha.6.2 | printf executado; tools/call MCP observado |
| Terminal nativo | 0.154.0-alpha.6.2 | tools.exec_command ausente; sem execução |
| Lista de agentes | 0.154.0-alpha.6.2 | Leitura executada: um orquestrador /root, sem subagente |

## Correção da análise

Uma ferramenta anunciada pode ser recusada ao executar. O controlo anterior do catálogo continua a falhar, mas não provava que todas as desativações fossem ineficazes. Evidência histórica preservada; esclarecimento acrescentado sem reinterpretar runs retroativamente.

Inventário: apply_patch, clock__curr_time, list_mcp_resource_templates, list_mcp_resources, mcp__agentbench__confined_command e read_mcp_resource. A função separada collaboration.list_agents também responde. Não tentámos spawn_agent nem escrita por apply_patch.

## Limites e continuação

Apenas demonstrado o comando fixo da ponte. Faltam permissões nativas, escritas MAIN/REV por todas as vias, proibição efetiva de criar agentes, interrupções e captura completa antes de congelar. apply_patch presente não prova fuga ou escrita; listar não prova que criar agentes funcionaria. Sem mudança de modelo necessária: Astra médio ativo, Astra elevado histórico.

OpenAI Docs orientou eventos e aprovação MCP por ferramenta. A opção de aprovação é recusada para outra fixture; não altera política global nem autoriza benchmark. Respostas fictícias fixas, loopback e HOME/CODEX_HOME vazios; sem serviço modelo ou segredos reais.

Novos testes: eventos SSE coincidentes; rejeição de fixture arbitrária/aprovação alargada; captura só do call_id conhecido; saída ausente/duplicada não validada; eco exato; distinção recusa/inventário/lista.

As sondas mantêm saída não nula: catálogo global não conforme e fornecedor fictício para após a resposta da ferramenta. Não invalida o eco confirmado nem autoriza lançamento.

[Tests](../tests/test_v2_2_dispatch.py) · [JSON](v2-2-dispatch.json) · [CLI](v2-2-cli-qualification.pt.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/extend/mcp)

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture inventory
python3 -B scripts/preflight_v2_2_bridge.py --dispatch-fixture bridge_echo --enable-code-mode-host-for-probe --approve-bridge-echo-for-probe
```

[README](../README.pt.md) · [V2.2](../governance/V2_2_PROTOCOL.pt.md)
