# Preflight científico — dupla reduzida

[Français](v2-2-lean-scientific-preflight.md) · [English (UK)](v2-2-lean-scientific-preflight.en.md) · [Español](v2-2-lean-scientific-preflight.es.md) · [Português](v2-2-lean-scientific-preflight.pt.md)

Apenas preparação: nenhum candidato iniciado nem chamada a modelos. Os resultados simples permanecem intactos.

## Constatação e proposta

O contrato integral ocupa um envelope inicial de 5 023 caracteres. Os perfis usam apenas texto sintético, nunca soluções anteriores: README de 1 000 caracteres, relatório MAIN de 150 palavras, revisão de 300 palavras e saída de controlo de 1 000 caracteres. Não estimam o tamanho do futuro código nem representam tokens.

| Código sintético | Revisão | Transmissão final | 12 000 | 24 000 propostos |
| ---: | ---: | ---: | :---: | :---: |
| 4 000 | 12 527 | 16 791 | ✗ | ✓ |
| 8 000 | 17 073 | 21 337 | ✗ | ✓ |
| 16 000 | 26 165 | 30 429 | ✗ | ✗ |

Nenhum perfil cabe em 12 000; mesmo sem código estas transmissões fictícias excedem o limite. Com 24 000, o limite desta fixture é 10 342 caracteres de código. Conta-se o escape JSON; excluem-se mandatos e contexto do cliente. Uma revisão maior pode exceder o limite. Não haverá truncagem silenciosa.

## Protocolo proposto

Astra médio, um programador e um revisor, três sessões distintas, sem repetição. Paragem entre sessões aos 150 000 tokens observados de entrada + saída; uma sessão pode ultrapassar o limite. Sem promessa de menos de 100 000 para a científica. A medir: 9 grupos / 57 controlos, não um resultado obtido.

Novos mandatos esclarecem OBS-001: controlos locais explicitamente permitidos sem consultar um manifesto ausente. Nova campanha proposta astra-medium-lean-002; comparação histórica exploratória, não causal. Comparações homogéneas exigirão controlos autorizados separadamente.

## Próximos passos e limites

O motor congelado 001 continua limitado à simples; não se entrega adaptação real. Após aprovação de 24 000: versionar desafio, entregáveis, suite copiada e comando científico; testar as três fases, fronteiras de ficheiros e paragens sem modelos, depois congelar. Lançamento real sujeito a aprovação explícita. Sem mudança de governança geral.

## Artefacts

- [JSON](v2-2-lean-scientific-size.json) · [Script](../scripts/preflight_lean_scientific.py) · [Tests](../tests/test_lean_scientific_preflight.py).
- [Draft](../governance/v2-2-lean-scientific-draft.json).
- [MAIN initial](../prompts/v2-2-lean-scientific-initial-draft.md) · [REV-01](../prompts/v2-2-lean-scientific-review-draft.md) · [MAIN final](../prompts/v2-2-lean-scientific-final-draft.md).
- [OBS-001](v2-2-lean-001.pt.md).

```bash
python3 -B scripts/preflight_lean_scientific.py
python3 -B -m unittest discover -s tests -q
```
