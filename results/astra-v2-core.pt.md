# V2 Astra — Calculadora Core

[Français](astra-v2-core.md) · [English (UK)](astra-v2-core.en.md) · [Español](astra-v2-core.es.md) · **Português**

## Veredito e comparação

Core passa à primeira e no controlo independente: **6/6 grupos e 14/14 controlos**. Com qualidade oficial igual, V1 Astra domina V2 Astra: V2 usa ×7,00 o tempo e ×4,75 os tokens. Face à V2 Sol, Astra demora menos 12,0 % mas usa mais 2,3 % de tokens: compromisso sem dominância.

| Run | grupos · controlos | Tempo | Entrada + saída |
| --- | ---: | ---: | ---: |
| Astra V1 Core | 6/6 · 14/14 | 100.175 s | 120 478 |
| Sol V2 Core | 6/6 · 14/14 | 796.534 s | 559 088 |
| Astra V2 Core | 6/6 · 14/14 | 700.994 s | 572 168 |

[Catalogue](../docs/acceptance-tests.pt.md) · [V1 Astra](astra-v1.pt.md) · [V2 Sol](sol-v2-core.pt.md)

## Observações sociais

SA-01 cobre contrato/segurança, SA-02 arquitetura/testabilidade e SA-03 crítica QA. MAIN é o único redator em duas sessões novas. As análises convergem numa gramática CLI simples; MAIN produz 17 decisões iniciais. SA-03 não confirma defeitos funcionais. MAIN separa 14 decisões finais: 7 retidas, 3 rejeitadas e 4 não verificáveis na sessão; apenas documentação e rastreabilidade mudam.

As cinco respostas consultoras somam 2 995 palavras dentro dos limites; todas as mensagens visíveis somam 3 446. MAIN copia os pareceres para DECISIONS.md (386 linhas), retransmitido pelo runner: a repetição aumenta o contexto e o custo.

Sete threads distintos, mesmos papéis, prompts e runner da V2 Sol, gpt-6-astra/high, contexto 200k/compactação 180k. Cache incluída: 430 848 tokens; raciocínio incluído: 1 261. Tempo-sessões: 775,480 s. Consultores sem ferramentas e alterações na solução ativa. Uma observação por célula, sem generalização estatística.

O relé captura os contadores indisponíveis ao candidato. As reservas de MAIN referem-se ao seu contexto; a ata preserva mandatos e traces. O estado não iniciado do protocolo congelado descreve o estado original; este relatório regista a execução.

## Provas

[PV](../runs/astra-core-v2-001/PV.md) · [Trace JSON](../runs/astra-core-v2-001/trace.json) · [Run JSON](../runs/astra-core-v2-001/run.json) · [DECISIONS](../runs/astra-core-v2-001/solution/DECISIONS.md)
