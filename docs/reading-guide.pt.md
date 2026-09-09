# Compreender AgentBench

[Français](reading-guide.md) · [English (UK)](reading-guide.en.md) · [Español](reading-guide.es.md) · **Português**

[Conclusões — quando compensa colaborar?](../results/CONCLUSIONS.pt.md)

Os nomes são **calculadora simples** (Core) e **calculadora científica** (Scientific). Identificadores técnicos e provas históricas inalterados.

Laboratório I&D sobre colaboração de agentes: as calculadoras são exercícios comuns. V1 = um candidato sozinho; V2 = um escritor e três consultores; V3 = futuros consultores locais. Medem-se qualidade, tempo e tokens: não se promete que V2 seja melhor.

| ID | Role |
| --- | --- |
| RELAY | Orquestrador experimental |
| MAIN | Programador principal, único escritor e decisor |
| SA-01 | Subagente 1 — requisitos e segurança |
| SA-02 | Subagente 2 — arquitetura e testabilidade |
| SA-03 | Subagente 3 — revisor crítico de qualidade, defeitos e casos limite |

Nos PV, abrir « Texte envoyé, mot pour mot » e ler « Texte retourné ». MSG-003/004: respostas cruzadas; MSG-006: crítica SA-03; MSG-007: decisão final. Sete sessões representam quatro papéis candidatos. O verificador é um programa independente. `trace.json` regista comandos e contadores; `DECISIONS.md`, decisões. Textos visíveis filtrados, sem raciocínio interno.

[Sol Core PV](../runs/sol-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Sol Scientific PV](../runs/sol-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium](../results/astra-medium-v2.pt.md)

[Astra medium Core PV](../runs/astra-medium-core-v2-001/PV.md#messages-visibles--verbatim-filtré) · [Astra medium Scientific PV](../runs/astra-medium-scientific-v2-001/PV.md#messages-visibles--verbatim-filtré)

Vx futura, não ativada: atribuir uma evolução fixada a um novo responsável com apenas código e documentação; medir sucesso, regressões, tempo, tokens e esclarecimentos. Os testes atuais não medem manutenibilidade (Scientific verifica cinco palavras documentais). Avaliar explicações úteis, não contar comentários. Trabalhar numa nova ramificação ou pasta para conservar a prova.

[README](../README.pt.md) → [Tests](acceptance-tests.pt.md) → [Results](../results/README.pt.md)

## Trabalho documental anexo — pendente

Estes pontos vêm do documento recebido; aprovar nomes V2.x não significa concluí-los.

- [ ] Guia de dois níveis e tabela de fontes, reutilizando este guia sem o duplicar.
- [ ] Diagrama de sequência: paralelismo, barreiras, destinatários e informação; distinguir RELAY mecânico de MAIN candidato.
- [ ] Resumos automáticos de dois minutos fora dos runs, separados do verbatim histórico: equipa, veredicto, métricas e interação decisiva.
- [ ] Anotações interpretativas explícitas: proposta → transmissão → decisão → alteração → efeito; distinguir confirmação, rejeição e ausência de efeito observável, sem lhe chamar ruído automaticamente.
- [ ] Instrumentação futura: tempos relativos medidos, dependências e grupos paralelos, estrutura genérica N agentes/V3. Nunca inventar tempos históricos; verificar impactos antes de aplicar alterações.
- [ ] Auditoria multilingue: protocolo congelado separado do estado atual; verificar provas históricas, métricas, testes e comportamento do runner sem repetir benchmarks por documentação.
