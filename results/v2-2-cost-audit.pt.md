# Auditoria de custos V2.2 — variante leve sem modelo

[Français](v2-2-cost-audit.md) · [English (UK)](v2-2-cost-audit.en.md) · [Español](v2-2-cost-audit.es.md) · **Português**

**Nenhum candidato executado.** O run 002 concluído permanece intacto. Reduzir transmissões não demonstra preservar a qualidade nem poupar quota.

## Medições exatas

Caracteres Unicode, não tokens, das capturas públicas normalizadas. Compara-se apenas o envelope JSON com serialização idêntica; o texto dos novos mandatos fica fora do cálculo.

| Fase | Prompt histórico completo | Dados históricos | Dados propostos |
| --- | ---: | ---: | ---: |
| MAIN inicial | 3 430 | 1 652 | 1 652 |
| REV-01 | 13 927 | 12 084 | 6 886 |
| MAIN final | 16 388 | 14 347 | 9 149 |

Remoção: **10 396 caracteres, 37,0%** dos 28 083 caracteres acumulados. Comandos/saídas iniciais ocupam 5 062 caracteres JSON retransmitidos em cada fase seguinte. O restante removido é a mensagem intermédia e a sua serialização. Conservam-se contrato, ficheiros completos, mensagens finais e provas dos comandos do revisor.

Entrada histórica: 110 511 tokens acumulados, incluindo 65 280 em cache; saída: 3 263. Não corresponde ao tamanho de um único prompt. As capturas não permitem atribuir todos os tokens ao sistema, ferramentas ou transmissões. **Não se estima redução de tokens ou quota.**

## Variante proposta, não congelada

Três sessões, duas profissões e Astra médio. Limites finais propostos: 150 / 300 / 300 palavras, em vez de 600 / 1 200 / 1 200; poupança não incluída na tabela. As provas completas continuam arquivadas, mas os comandos iniciais deixam de ser injetados nas fases seguintes.

Contrapartida: o revisor dispõe de menos provas dos testes iniciais e deve distinguir afirmações MAIN de execuções observadas. Uma revisão breve pode omitir problemas; sinalizar excessos necessários, nunca truncar silenciosamente. Nova condição experimental, sem alterar o protocolo histórico.

## Paragens testadas e limites

O simulador não tem transporte real. Dez testes novos cobrem três respostas sintéticas, recusa do modo real, excesso de tamanho, limiar exato, ultrapassagem visível, métricas ausentes, falha sem retry, limites inválidos, conservação de dados e cálculo.

Proposta a validar: **12 000 caracteres por envelope**, recusa integral sem truncar; paragem entre sessões aos **60 000 tokens acumulados observados**. Não são valores congelados nem limites do plano. Com os custos históricos, pararia após revisão aos 66 038 tokens: excesso de 6 038 e sem veredicto final. Não limita uma sessão em curso; nenhum watchdog ou limite nativo validado foi implementado.

Os 100 tokens/1 000 caracteres dos testes são fixtures, não orçamentos recomendados. Passam 82 testes de manutenção; nenhuma nova pontuação da calculadora. Decidir sobre perda de informação e paragem antes de autorizar separadamente científica ou solo de referência.

[JSON](v2-2-cost-audit.json) · [Audit / simulation](../scripts/audit_v2_2_cost.py) · [Tests](../tests/test_v2_2_cost.py) · [MAIN initial](../prompts/v2-2-lean-initial-draft.md) · [REV-01](../prompts/v2-2-lean-review-draft.md) · [MAIN final](../prompts/v2-2-lean-final-draft.md) · [Run 002](v2-2-supervised-core-002.pt.md)
