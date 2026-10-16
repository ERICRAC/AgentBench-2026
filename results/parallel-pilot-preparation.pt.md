# Preparação técnica — piloto V1 / V2.1 leve

[Français](parallel-pilot-preparation.md) · [English (UK)](parallel-pilot-preparation.en.md) · [Español](parallel-pilot-preparation.es.md) · [Português](parallel-pilot-preparation.pt.md)

**Preparação sem modelos entregue; campanha não congelada e nenhum candidato executado.**
A questão mantém-se: o desenvolvimento paralelo reduz o prazo com qualidade comparável, incluindo a integração?

## Entregas

- [Especificação completa](../challenges/modular-calculator-draft/SPEC.md): quatro ficheiros, sintaxe científica, limites explícitos, curvas, lotes, erros CLI e documentação. Instrução canónica em francês.
- [Catálogo detalhado de dez grupos](../challenges/modular-calculator-draft/catalogue.json) e [suite independente](../challenges/modular-calculator-draft/tests/test_acceptance.py). M01 restrições; M02 cálculo; M03 funções; M04 erros/limites; M05 amostragem; M06 SVG; M07 lotes; M08 erros CLI; M09 integração; M10 documentação.
- [Calibração](../tests/test_modular_acceptance.py): duas variantes sintéticas aceites e dez defeitos injetados detetados, um por grupo. As fixtures são ferramentas de manutenção, nunca referências entregues aos candidatos.
- [Simulação paralela](../scripts/preflight_parallel_pilot.py): dois processos fictícios isolados, barreira de arranque, montagem sem alterações e integrador fictício.
- [Provas, durações relativas e hashes](parallel-pilot-preparation.json). Sete testes de manutenção passaram; doze execuções da suite na calibração (duas variantes e dez mutantes).

## O que os controlos estabelecem

O carregador aceita imports Python normais, dataclass e imports entre módulos. Passam as duas representações autorizadas, polyline e path M/L. Cada mutação falha no grupo previsto. Isto calibra a suite, sem provar exaustividade.

DEV-A e DEV-B leem o seu contrato, mas não o alteram nem leem/escrevem o canário do outro, incluindo por ligações simbólicas. Seis controlos por programador passam. Ambos estão prontos antes da libertação; INT começa após recolha dos dois resultados. Os hashes acompanham a montagem e atribuem uma correção fictícia a INT.

O isolamento exterior bloqueou a primeira tentativa. Uma execução local elevada autorizada passou mantendo o confinamento dos filhos. Sem credenciais ou chamadas a modelos. Os tempos finais são observações do processo pai, não saídas exatas do núcleo nem ganhos colaborativos medidos.

## Limites e próxima entrega

M10 verifica nomes de API, limites e docstrings; qualidade explicativa e execução dos exemplos ainda não são avaliadas automaticamente. A análise AST não é uma defesa contra candidatos maliciosos. O catálogo publica os limites de cobertura, sem alegar testes ocultos.

O simulador não recebe modelos nem oferece modo real. Antes do lançamento: transporte autenticado para dois escritores, mensagens e contadores reais, validação de todas as ferramentas, mandatos finais e manifesto congelado. A simulação isolada não tem credenciais e não constitui um lançador Codex pronto.

O [protocolo proposto](../docs/parallel-pilot.pt.md) mantém Astra médio, solo seguido de equipa e limiar entre sessões de 150 000 tokens por organização: proposta, não teto rígido. Solo segmentado continua como controlo posterior separado. Rever antes do congelamento; **lembrete pedido: usar o modelo mais potente disponível nesse ponto**. A preparação não implica autorização de lançamento ou novo orçamento.

## Reproduzir sem modelos

```bash
python3 -B -m unittest tests/test_modular_acceptance.py tests/test_parallel_pilot.py
python3 -B scripts/preflight_parallel_pilot.py --simulate
```

O segundo comando exige espaços de nomes Linux permitidos para bubblewrap. Uma recusa deve ser declarada bloqueio, nunca sucesso.
