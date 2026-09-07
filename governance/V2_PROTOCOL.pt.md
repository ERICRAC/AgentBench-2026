# Protocolo V2 — Codex multiagente governado

[Français](V2_PROTOCOL.md) · [English (UK)](V2_PROTOCOL.en.md) · [Español](V2_PROTOCOL.es.md) · **Português**

## Estado e hipótese

O protocolo está congelado: o patrocinador aprovou A-01 a A-08. O [preflight mínimo](../results/astra-v2-preflight.pt.md) passou nos quatro
papéis após publicar V1. O benchmark V2 ainda não começou. Testa se três revisões
especializadas melhoram qualidade ou convergência de um único escritor depois
de contabilizar a coordenação. As referências atuais são `astra-core-v1-002` e
`astra-scientific-v1-002`; os runs `001` continuam históricos.

## Decisões congeladas

Foram aprovados: A-01 contexto 200k/compactação 180k (100k obriga a repetir V1);
A-02 três papéis; A-03 análises cegas e uma contradição cruzada; A-04 1.200
palavras por análise, 600 por réplica e 1.200 para crítica; A-05 o mesmo
`gpt-6-astra`/`high`; A-06 textos visíveis completos após filtrar segredos;
A-07 painel qualidade/tempo/tokens e dominância de Pareto, sem pesos arbitrários.
A-08 usa subagentes nativos apenas se expuserem configuração e contadores por
thread; caso contrário, sessões `codex exec --json` separadas. Um preflight
trivial fora do benchmark verifica papel, isolamento, texto e uso JSON antes de
ler um desafio. A campanha `astra-high-001` repete ambas as referências V1 com Astra antes do
preflight V2. A-01 a A-08 mantêm-se; A-05 migra explicitamente para Astra em
todos os papéis. O protocolo Sol fica no commit `158d087`.

| Parâmetro | Referência e V2 congelada |
| --- | --- |
| Modelo / esforço | `gpt-6-astra` / `high` |
| Contexto declarado por agente | 200.000 tokens |
| Compactação automática | 180.000 tokens, escopo `total` |
| Sessões | novas e efémeras |
| Desafios e verificadores | versões atualmente congeladas |
| Dependências / ajuda humana | biblioteca padrão / nenhuma |

## O que significa «limite de contexto validado»

Capacidade ativa, limiar de compactação e consumo acumulado são distintos.
Cada ficheiro de papel fixa janela de 200.000 e compactação `total` a 180.000;
a validação estrita deve aceitá-lo. Cada consultor começa num thread novo sem
conversa herdada. `run.json` guarda papel, ID, valores e SHA-256 do ficheiro, e
a ata associa textos e contadores ao thread.

Isto prova a configuração cliente e o isolamento de entradas, não um limite
interno do servidor. Se a delegação nativa não o demonstrar, usam-se sessões
`codex exec` efémeras separadas; caso contrário o run é interrompido.

Consulte a [configuração Codex](https://developers.openai.com/codex/config-reference)
e a [documentação de subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents).

O candidato principal é o único orquestrador/escritor. SA-01 analisa requisitos
e segurança; SA-02, arquitetura e testabilidade; SA-03 é crítico QA adversarial.
Todos são apenas de leitura, sem subdelegação nem acesso a outros runs.

SA-01 e SA-02 respondem primeiro de modo independente. Os textos visíveis são
trocados integralmente e cada um dispõe de uma réplica para confirmar,
contradizer ou rever. O candidato arbitra e implementa. SA-03 recebe desafio,
solução e tabela de decisões para uma crítica final. Cada recomendação fica
aceite, rejeitada ou não verificável, com motivo.

Registam-se primeira passagem, resultado independente, duração, tokens reais
por agente quando disponíveis, chamadas, contradições, conselhos aceites ou
rejeitados, correções e incidentes. Uma [ata numerada](PV_TEMPLATE.pt.md) conserva literalmente
cada mensagem visível após controlo de segredos e regista a decisão fundamentada
por papel.

A qualidade é publicada para primeira passagem e resultado final. Tempo e
tokens são comparados como rácios V2/V1, com tempo mural, soma de tempos-agente,
custo por papel, acordos, contradições, duplicados e conselhos aceites. V2 só
domina se não perder qualidade, não aumentar custos e melhorar estritamente uma
dimensão. V2 Core é publicada antes de V2 Scientific, sem afinação intermédia.
