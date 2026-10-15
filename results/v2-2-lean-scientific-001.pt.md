# Ensaio científico reduzido — interrupção OBS-002

[Français](v2-2-lean-scientific-001.md) · [English (UK)](v2-2-lean-scientific-001.en.md) · [Español](v2-2-lean-scientific-001.es.md) · [Português](v2-2-lean-scientific-001.pt.md)

O ensaio real parou antes de produzir código: **11 968 tokens, 12,811 s, sem resultado de calculadora**. Não houve esgotamento de quota. Sem repetição.

## O que aconteceu

O acordo humano foi recebido e o lançador iniciou uma sessão MAIN. Contudo, o mandato dizia que congelar o protocolo não autorizava o lançamento, sem confirmar ao candidato que o acordo já existia. MAIN pediu confirmação e terminou sem ferramentas. A CLI devolveu 0; o relé detetou entregáveis ausentes e terminou com código 1. Nem o revisor nem MAIN final foram iniciados.

É um defeito de transmissão da autorização no dispositivo preparado pelo orquestrador. Os 135 testes sem modelo verificavam caminhos técnicos; candidatos fictícios não interpretavam a condição linguística. OBS-002 fica preservado sem alterar retroativamente o protocolo.

## Medições e verificação

Uma sessão CLI iniciada e terminada, zero fases validadas. Entrada: 11 810; saída: 158; total: 11 968. Cache: 0, incluída na entrada; raciocínio: 89, incluído na saída. Duração total: 12,810581794 s; sessão: 12,809085513 s. Limiar 150 000 não atingido; envelope inicial: 5 023 de 24 000 caracteres. Saldo de quota e custo do orquestrador: não registados.

Inspeção independente: solução vazia, contrato, verificador e suite copiados sem alterações. Suite científica não executada: não se atribui 9/9 nem 0/9. Estado bruto mantém usage_complete=false, definido pelo relé na exceção; os contadores do único processo concluído estão presentes e publicados.

## Conclusão e próxima ação

Não permite comparar eficiência individual e coletiva: a colaboração não começou. Resultados históricos intactos; estes 11 968 tokens pertencem a ensaios interrompidos, não a referências concluídas.

Correção recomendada numa nova versão: após validar o acordo, dizer explicitamente ao candidato que o orquestrador autoriza esta fase agora e deve começar. Remover reservas ambíguas da mensagem, manter a autorização no lançador e testar a confirmação. Nenhuma correção nem novo ensaio aplicado: exige ID novo e autorização de repetição.

## Artefacts

- [PV / messages](../runs/astra-medium-scientific-v2-2-lean-001/PV.md).
- [Run](../runs/astra-medium-scientific-v2-2-lean-001/run.json) · [State](../runs/astra-medium-scientific-v2-2-lean-001/state.json).
- [Prompt](../runs/astra-medium-scientific-v2-2-lean-001/prompts.json) · [Trace](../runs/astra-medium-scientific-v2-2-lean-001/trace.json).
- [Checks](../runs/astra-medium-scientific-v2-2-lean-001/verifications.json) · [Snapshots](../runs/astra-medium-scientific-v2-2-lean-001/snapshots.json).
- [Manifest](../governance/v2-2-lean-scientific-001.json) · [Preflight](v2-2-lean-scientific-preflight.pt.md).
