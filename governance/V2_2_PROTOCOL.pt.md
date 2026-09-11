# Protocolo V2.2 — par leve Astra médio

[Français](V2_2_PROTOCOL.md) · [English (UK)](V2_2_PROTOCOL.en.md) · [Español](V2_2_PROTOCOL.es.md) · **Português**

## Num minuto

**Preparado para validação, não congelado; nenhum lançamento autorizado.** V2.2 testa se uma revisão preserva o contributo útil de V2 com menos coordenação. Não é desenvolvimento paralelo: um programador mantém-se único escritor. Variante opcional fora das seis células principais; não substitui V2 histórica nem V2.1.

O [balanço Astra médio](../results/astra-medium-v1-v2.pt.md) motiva a hipótese: pontuação V1/V2 igual, V2 custa ×3,56 tempo e ×4,49 tokens; algumas correções de robustez ficam fora da pontuação. Hipótese, não promessa: **V2.2 custa menos que V2 sem perder qualidade e a revisão produz correções verificáveis.**

## Organização proposta

| Organização | Papéis candidatos | Sessões por desafio | Relação |
| --- | ---: | ---: | --- |
| V1 | 1 | 1 | Programador solo |
| V2 histórica | 4 | 7 | Duas análises, duas revisões cruzadas, implementação, crítica, correções |
| V2.2 | 2 | 3 | Programador → revisor → programador |

MAIN desenvolve, arbitra e escreve sozinho em solution/. REV-01 é o único revisor crítico, só leitura, para contrato, segurança, funcionamento e documentação, sem delegação. RELAY é o orquestrador experimental externo: prepara, captura, transmite sem conselho ou síntese, verifica e publica. O verificador independente é a suite congelada, não um LLM.

MAIN inicial e final são **duas sessões novas do mesmo papel**, não uma conversa retomada: três threads, dois papéis. REV-01 aproxima-se da função SA-03 de V2, com identidade distinta. Sem consultores prévios, revisão cruzada ou segunda opinião.

## Sequência e entradas exatas

| Fase | Entradas autorizadas | Saída / barreira |
| --- | --- | --- |
| P1 · MAIN inicial | Desafio ativo + mandato inicial; solução vazia | Código/README completos; passagem ≤600 palavras; comandos/saídas de controlos próprios |
| P2 · REV-01 | Desafio + instantâneo P1 completo + passagem P1 + comandos/saídas P1 | Uma revisão ≤1200 palavras; constatações REV-001… com prova e gravidade |
| P3 · MAIN final | Desafio + solução P1 + passagem/controlos P1 + revisão/controlos P2 integrais | Arbitragem por ID, correções, verificador oficial; resposta ≤1200 palavras |

Cada fase espera o fecho anterior. RELAY copia todos os ficheiros com caminhos relativos e hashes, sem seleção nem ler outra tentativa. Transmite textos visíveis literalmente, nunca pensamentos privados. Saídas completas; truncamentos, omissões e filtragem declarados. Entrada ausente bloqueia a fase seguinte: não improvisar resumo. Artefactos candidatos não são instruções de papel.

P1 e REV podem fazer controlos próprios não destrutivos; **primeira passagem oficial em P3 após revisão**, como V2. MAIN final pode corrigir falhas oficiais na sessão sem chamar REV novamente. Revisão sem constatações é válida. Excesso de palavras registado sem truncar provas ou pedir reformulação. Contagem proposta: elementos separados por espaços na resposta final, código/tabelas incluídos; mensagens intermédias capturadas e contadas à parte.

Mandatos canónicos franceses, rascunhos: [MAIN inicial](../prompts/v2-2-developer-initial.md), [REV-01](../prompts/v2-2-reviewer.md), [MAIN final](../prompts/v2-2-developer-final.md). Iguais nos dois desafios, CHALLENGE ativo fornecido à parte. Sem balanços humanos, conclusões anteriores ou defeitos históricos para candidatos.

## Parâmetros e fronteiras

**gpt-6-astra / medium nas três sessões**, contexto 200000, compactação 180000, âmbito total; sessões efémeras. Usar parâmetros registados, não seleção do chat. Acesso ao modelo, aceitação estrita da configuração e quota ficam para preflight, sem garantia documental.

Desafios/suites intactos: [simples](../challenges/calculator/SPEC.md), 6 grupos / 14 controlos; [científica](../challenges/scientific-calculator/SPEC.md), 9 grupos / 57 controlos. [Lista completa](../docs/acceptance-tests.pt.md). Sem alterar ou ampliar pontuação.

MAIN escreve apenas entregáveis pedidos em solution/. REV só leitura, controlos sem ficheiros/cache. Sem Git, rede, delegação ou dependências extra nos candidatos. RELAY gere atas, instantâneos e medidas fora dos entregáveis, em privado durante o run; publica após fecho com commits separados de código/manutenção. Diretório de trabalho não prova isolamento: testar permissões efetivas.

## Orçamentos, interrupções e ordem

Piloto proposto: **uma tentativa por calculadora, máximo três sessões cada**, uma revisão, sem repetição automática. Simples primeiro, verificação/publicação, autorização científica separada; sem refinamento intermédio.

Proposta comparável: nenhum novo teto global de tokens/tempo, pois referências não tinham. **Não garante caber na quota de subscrição.** Contexto e palavras não são orçamento acumulado. Somar custos das três sessões, falhas incluídas; separar RELAY/publicação.

Quota esgotada, captura incompleta, escrita proibida, falha de infraestrutura ou excesso de sessões: parar, preservar estado, fase, artefactos e contadores disponíveis. Sem espera automática de renovação, continuação oculta ou substituição de modelo. Reinício do zero exige novo ID sem ler a solução anterior. Teto numérico de segurança deve ser acordado/implementado antes do congelamento e aplicado de forma comparável.

## Qualidade e contributo da revisão

Preservar P1 antes de corrigir. **Após o run**, RELAY executa a suite congelada numa cópia P1 e na entrega final. Rotular P1 «diagnóstico retrospetivo do instantâneo», nunca «primeira passagem candidata»; não transmitir durante o run. Permite observar antes/depois sem acrescentar feedback ao programador inicial.

Por constatação: ID, cláusula, gravidade, prova/reprodução, executado/não executado, aceite/rejeitado/não verificável, alteração e controlo final. Separar correções por REV, espontâneas MAIN e pelo verificador. Reproduzir constatações aplicáveis nos dois instantâneos após run pode confirmar correções/regressões: controlos **exploratórios**, fora dos 71 oficiais.

Suite comum de robustez ainda exige conceção, calibração e congelamento numa nova campanha antes dos candidatos. Não transformar retroativamente as duas sondas V1 em testes pré-registados. Asserção proposta não prova nada sem execução.

## Ata social e medidas

Aplicar o [modelo de ata](PV_TEMPLATE.pt.md), apenas MAIN e REV-01 como papéis candidatos. Preservar mandatos/respostas visíveis integrais filtrados, MSG-001…, threads e hashes; sem segredos, horas públicas ou raciocínio privado. Analisar quem assinala, aceita/rejeita e que prova liga conselho, alteração e efeito; não inferir emoções ou pensamentos.

Publicar acordos explícitos, contradições, duplicados, constatações únicas, decisões, correções confirmadas, regressões e pontos não verificáveis. Ausência de segundo intercâmbio não significa consenso; aceitar não prova necessidade. Novidade apenas face ao estado/textos P1 observáveis.

Tempo mural antes de preparar primeira chamada até fecho/captura final; durações por sessão e soma; tokens entrada/cache/saída/raciocínio; palavras e volume de artefactos. Cache incluída na entrada, raciocínio na saída. Separar verificação/publicação posteriores. Dados ausentes ou tokens exatos de coordenação não expostos: não registados, não estimados por palavras. Instrumentação/fronteiras congeladas no preflight; não reutilizar grafo V2 de sete fases.

Comparar V2.2/V1 e V2.2/V2 **na mesma calculadora**, depois agregar pares completos. Vitória oficial: pontuação não inferior, tempo/tokens não superiores e alguma melhoria estrita. Robustez adicional com sobrecusto: compromisso. Pontuação igual não equivale a qualidade exaustiva; um antes/depois não demonstra causalidade.

## Campanha e nível de prova

Nova topologia/prompts são alteração substancial: **nova campanha**, ID proposto astra-medium-lean-001, sem alterar astra-medium-001. Piloto face às referências existentes permite apenas **comparação histórica exploratória explicitamente qualificada** (ordem, cache/carga, prompts, sessões, instrumentação).

Confirmação homogénea: repetir V1, V2 e V2.2 na nova campanha, ambos os desafios, regras comuns. Proposta, não compromisso de consumo: três repetições por célula, ordem contrabalançada, **18 runs**; dispersão/medianas, não só melhor resultado. Sem alegar significância ou limiar universal com esta amostra. Preparar não autoriza repetições ou piloto.

## Preflight antes de congelar e lançar

- [x] Hipótese, papéis, três fases, mandatos, critérios e interrupções documentados.
- [x] FR, UK, ES, PT ligados; protocolos/runs anteriores intactos.
- [ ] Validar piloto sem novo teto ou campanha com orçamento; decidir repetições à parte.
- [x] Relé de três fases testado com candidatos fictícios: transmissões, auditoria de escrita, limites, paragem, capturas, instantâneos e bloqueio real. Não valida isolamento OS.
- [x] Duas configurações rascunho e inventário de 15 hashes; simulações temporárias novas. Diretórios benchmark e hashes congelados pendentes.
- [ ] Verificar isolamento/acesso real; teste trivial real consome tokens e exige autorização separada.
- [ ] Congelar protocolo, mandatos e executante; publicar preflight estático, autorizar explicitamente calculadora simples.

**Pronto: executante simulado, preflight estático e 26 testes V2.2. Pendente: transporte real qualificado, isolamento OS, acesso modelo, congelamento e benchmark.** Nenhum candidato lançado.

Validação atual: 38 testes de manutenção (12 existentes + 26 V2.2), duas simulações de três fases, zero chamadas modelo. O [relatório técnico](../results/v2-2-preflight.pt.md) distingue propriedades testadas e garantias pendentes.

[README](../README.pt.md) · [Conclusões](../results/CONCLUSIONS.pt.md) · [V2 congelada](V2_PROTOCOL.pt.md) · [Plano experimental](EXPERIMENTAL_DESIGN.pt.md) · [Instrumentação](../docs/observability.pt.md)
