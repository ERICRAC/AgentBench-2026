# V2.2 — encaminhamento real após atualização

[Français](v2-2-dispatch.md) · [English (UK)](v2-2-dispatch.en.md) · [Español](v2-2-dispatch.es.md) · **Português**

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
