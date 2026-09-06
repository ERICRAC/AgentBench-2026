# Modelo de ata multiagente

[Français](PV_TEMPLATE.md) · [English (UK)](PV_TEMPLATE.en.md) · [Español](PV_TEMPLATE.es.md) · **Português**

Obrigatório a partir da V2, preserva os textos visíveis entre agentes e liga-os
a decisões, custo e resultado.

## Identificação e equipa

Registar run, campanha, objetivo, patrocinador, orquestrador experimental,
candidato principal/único escritor, verificador e resultado inicial/final.

| ID | Agente e profissão | Missão limitada | Entradas | Escrita | Modelo / esforço | Contexto / compactação |
| --- | --- | --- | --- | --- | --- | --- |
| MAIN | Orquestrador candidato / escritor | decidir, produzir, verificar | desafio, mensagens, solução | `solution/` | … | … |
| SA-01 | Analista de requisitos e segurança | obrigações, ambiguidades, ameaças | desafio | nenhuma | … | … |
| SA-02 | Arquiteto e especialista em testabilidade | estrutura, invariantes, testes | desafio | nenhuma | … | … |
| SA-03 | Crítico QA adversarial | omissões, regressões, limites | desafio, decisões, solução | nenhuma | … | … |

`run.json` guarda ID do thread, impressão da configuração e métricas disponíveis.

## Mensagens visíveis

Criar uma ficha numerada por mensagem. Preservar o texto integral após controlo
de segredos e declarar qualquer omissão.

### MSG-001 — título

Registar direção, fase, duração e contadores disponíveis de entrada/cache/saída/
raciocínio.

**Texto enviado literalmente**

> …

**Texto devolvido literalmente**

> …

**Síntese analítica** — propostas verificáveis, novidade, acordo, contradição
ou duplicado, risco detetado e decisão esperada de MAIN.

## Registo de decisões

| ID | Fonte | Proposta | Decisão | Motivo de MAIN | Prova | Efeito |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | MSG-… | … | aceite / rejeitada / não verificável | … | ficheiro, teste ou controlo | ganho, neutro ou regressão |

Cada recomendação exige decisão; decisões espontâneas de MAIN também recebem ID.

## Relação social e eficiência

Registar mensagens, acordos, conflitos úteis/não resolvidos, duplicados,
recomendações únicas, decisões, defeitos antes/depois do verificador e volume
de coordenação. Explicar influência, consenso, desacordo útil e ruído.

Comparar V1/V2 em qualidade inicial/final, tempo mural, soma dos tempos-agente,
tokens de entrada + saída, tokens de coordenação e correções. Concluir
separadamente ganhos de qualidade, tempo e tokens: domínio, compromisso, sem
ganho ou inconclusivo. Não reconstruir raciocínio oculto.
