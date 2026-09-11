# V2.2 — ponte de ferramentas e catálogo bloqueante

[Français](v2-2-bridge.md) · [English (UK)](v2-2-bridge.en.md) · [Español](v2-2-bridge.es.md) · **Português**

## Decisão e resultado

**Astra elevado fica apenas como histórico: sem novos runs previstos; resultados preservados.** Astra médio permanece ativo. Sol elevado exige autorização separada para comparações futuras. [Decisão](../governance/v2-2-draft/model-policy.json).

A ponte confinada funciona, mas **o catálogo efetivo do CLI bloqueia a integração**, não os créditos. Sem chamadas modelo, autenticação real, congelamento ou benchmark.

## Trabalho e verificação

A [ponte MCP](../scripts/v2_2_tool_bridge.py) aceita apenas um comando. O orquestrador fixa papel, workspace e captura privada; argumentos não podem alterá-los. Bubblewrap permite escrever solution/ a MAIN, não a REV-01. Entrada vazia e ambiente limpo no processo confinado, sem credenciais Codex.

**52 testes aprovados**, incluindo [6 novos](../tests/test_v2_2_tool_bridge.py): inicialização/ferramenta única; rejeição de alterações de papel/caminhos/permissões; comandos inválidos; capturas separadas não reutilizáveis; notificações sem execução; protocolo/métodos inválidos.

[Preflight real sem modelo](../scripts/preflight_v2_2_bridge.py): **7/8 controlos**.

- [x] MAIN: inicialização/listagem, saídas completas, escrita permitida.
- [x] REV-01: inicialização/listagem, saídas completas, escrita negada.
- [x] Pedido CLI recebido pelo servidor HTTP local fictício.
- [ ] Catálogo limitado à ferramenta confinada.

[Observações e hashes](v2-2-bridge.json) · [Isolamento anterior](v2-2-transport.pt.md)

## Bloqueio

CLI real com HOME/CODEX_HOME temporários vazios e sem token herdado; fornecedor loopback que recusa inferência com erro HTTP controlado. Não se publicam cabeçalhos, prompts ou identificadores de sessão.

Negociação MCP 2025-06-18 e tools/list observados. Catálogo enviado em input/additional_tools, não em tools: a inspeção inicial vazia era incompleta.

Aparecem functions.exec e collaboration.spawn_agent apesar de features.shell_tool=false e features.multi_agent=false. Anunciar ferramentas não prova que funcionem, mas **impede certificar passagem exclusiva pela ponte**. MCP não aparece como ferramenta direta única; disponibilidade pelo executor por qualificar.

A sonda falha deliberadamente até cumprir o critério. A saída CLI não nula é esperada pela recusa de inferência; não mede quota ou acesso à conta.

## Limites e continuação

OpenAI Docs orientou configuração e desativações; aceitar opções não prova o efeito. [Referência](https://learn.chatgpt.com/docs/config-file/config-reference).

A interface MCP altera o tratamento histórico: nova campanha, sem retroatividade. Capturas privadas; UTF-8 inválido ou falha de infraestrutura para a ponte. Pendentes: timeout MCP do cliente, truncagem, executor e encerramento completo dos processos. Nenhum novo orçamento candidato aprovado.

Próximo: configuração efetivamente restritiva ou CLI separado sem substituir VS Code; depois pedir sonda autenticada Astra médio. Sem segredos no repositório.

```bash
python3 -B -m unittest discover -s tests -q
python3 -B scripts/preflight_v2_2_bridge.py
```

O segundo comando precisa de autorização para namespaces Linux e atualmente deve falhar pelo catálogo. Testemunhos temporários removidos; soluções históricas não utilizadas.

[Protocolo](../governance/V2_2_PROTOCOL.pt.md) · [Conclusões](CONCLUSIONS.pt.md) · [README](../README.pt.md)
