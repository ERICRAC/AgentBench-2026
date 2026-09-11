# Governação pública

[Français](README.md) · [English (UK)](README.en.md) · [Español](README.es.md) · **Português**

**V2.2: ponte confinada testada; 52 testes aprovados.** Integração bloqueada: CLI anuncia ferramentas fora da lista permitida. Sem chamadas modelo. **Astra elevado: apenas histórico, sem novos runs previstos.** [MCP / CLI](../results/v2-2-bridge.pt.md)

Este diretório publica o método necessário para compreender e reproduzir a
experiência sem expor conversas completas nem a configuração privada do autor.

- [`RESPONSE_FORMAT.pt.md`](RESPONSE_FORMAT.pt.md) define as restituições.
- [`LOGGING.pt.md`](LOGGING.pt.md) define o registo público.
- [`EXPERIMENTAL_DESIGN.pt.md`](EXPERIMENTAL_DESIGN.pt.md) define a matriz, os
  marcos de observação e as repetições.
- [`V2_PROTOCOL.pt.md`](V2_PROTOCOL.pt.md) pré-regista a organização
  multiagente, os limites de contexto e as medições.
- [`PV_TEMPLATE.pt.md`](PV_TEMPLATE.pt.md) define textos entre agentes,
  decisões, relação social e eficiência.
- [`../logs/history.pt.md`](../logs/history.pt.md) preserva o histórico resumido.

A precedência é: regras do repositório, contrato da tentativa, prompt do modo,
decisão do orquestrador e veredicto do verificador independente. Uma instrução
local não pode enfraquecer a segurança, alterar os testes nem permitir a leitura
de outra solução.

A governação evolui apenas quando um esclarecimento ou erro produz uma regra
útil, verificável e reutilizável. Nunca reescreve uma execução concluída. Um
novo verificador é calibrado antes de ser congelado; um viés descoberto depois
do primeiro candidato é documentado, não removido silenciosamente.

A documentação editorial pública existe em francês, inglês britânico,
espanhol e português. Instruções de agentes, prompts, desafios congelados,
traces e entregáveis dos runs permanecem provas canónicas e imutáveis.

A regra Git global pertence ao orquestrador depois do run. Os candidatos só
escrevem em `solution/` e não criam commits nem fazem push.
