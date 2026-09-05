# Protocolo V2 — Codex multiagente governado

[Français](V2_PROTOCOL.md) · [English (UK)](V2_PROTOCOL.en.md) · [Español](V2_PROTOCOL.es.md) · **Português**

## Estado e hipótese

O protocolo fica congelado antes do primeiro run V2. Testa se três revisões
especializadas melhoram qualidade ou convergência de um único escritor depois
de contabilizar a coordenação. As referências atuais são `codex-single-002` e
`scientific-single-002`; os runs `001` continuam históricos.

| Parâmetro | Referência e V2 planeada |
| --- | --- |
| Modelo / esforço | `gpt-5.6-sol` / `high` |
| Contexto declarado por agente | 200.000 tokens |
| Compactação automática | 180.000 tokens, escopo `total` |
| Sessões | novas e efémeras |
| Desafios e verificadores | versões atualmente congeladas |
| Dependências / ajuda humana | biblioteca padrão / nenhuma |

Antes do lançamento deve ser provado que o limite se aplica a cada agente. Se
a delegação não o expuser, o run não pertence a esta campanha.

Um orquestrador é o único escritor. Dois consultores apenas de leitura analisam
contrato/segurança e desenho/testabilidade antes da implementação; um crítico
apenas de leitura revê a primeira solução. São exatamente três consultores,
sem subdelegação nem acesso a outros runs. Só `solution/` recebe escritas e os
candidatos não executam operações Git.

Registam-se primeira passagem, resultado independente, duração, tokens reais
por agente quando disponíveis, chamadas, contradições, conselhos aceites ou
rejeitados, correções e incidentes. Um `PV.md` numerado regista cada mandato,
parecer, resposta e decisão fundamentada por papel. V2 Core é publicada antes
de V2 Scientific, sem afinação intermédia. Qualquer mudança abre outra campanha.
