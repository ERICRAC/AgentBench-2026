# V2.2 leve — lançador preparado, execução real bloqueada

[Français](v2-2-lean-preflight.md) · [English (UK)](v2-2-lean-preflight.en.md) · [Español](v2-2-lean-preflight.es.md) · **Português**

**Preparação autorizada e concluída; nenhum candidato real executado.** Astra médio mantido. O motor encadeia três fases com mandatos e envelopes reduzidos, em vez de apenas medir tamanhos.

## Parâmetros de preparação

| Parâmetro | Valor |
| --- | --- |
| Modelo / esforço futuro | gpt-6-astra / medium |
| Sessões máximas | MAIN inicial → REV-01 revisor → MAIN final |
| Envelope JSON por fase | 12 000 caracteres Unicode, sem mandato |
| Objetivo experimental | Menos de 100 000 tokens, não é previsão |
| Paragem entre sessões | A partir de 150 000 tokens entrada + saída observados |
| Limite estrito dentro da sessão | Nenhum |
| Relatórios finais | 150 / 300 / 300 palavras; excesso registado, sem truncar |
| Retry / científica / execução real | Não autorizados |

A proposta anterior de 60 000 é substituída nesta preparação pelo limiar acordado de 150 000. Cache e raciocínio não são contados duas vezes. Contadores ausentes/inválidos param a sequência e marcam o total incompleto, não zero.

## Integração e verificações

Diretório privado novo, cópias intactas do contrato/verificador, solução vazia. Prompts reduzidos, configurações existentes dos papéis, captura integral de respostas sintéticas, controlo de ficheiros protegidos/só leitura, instantâneos e checkpoints. Comandos iniciais ficam arquivados sem retransmissão; provas dos comandos do revisor são conservadas.

**100 testes de manutenção passam**, incluindo 18 novos de integração: captura, transmissões, diretórios exclusivos, recusa do real antes da escrita, limites, métricas ausentes/inválidas, custos disponíveis após falha, escritas proibidas, thread reutilizado, saída truncada, limites de palavras e manifesto bloqueado.

Simulação completa: três fases, 39 tokens **fictícios**, envelopes de 1 652 / 2 078 / 2 280 caracteres, sem veredicto de calculadora. Duas sessões sintéticas de 75 000 tokens bloqueiam a terceira. Contadores históricos como fixtures terminam em 113 774, abaixo do limiar mas acima do objetivo; não é nova medição do modelo.

## Limites e próxima entrega

O limiar impede a fase seguinte, não limita a sessão em curso. Uma fase final concluída acima do limiar mantém o estado concluído e regista o excesso. Limites de palavras são auditados, não impostos ao modelo.

O CLI só permite simulação; editar o manifesto não desbloqueia o real. O callback injetável serve para testes. **Antes do benchmark faltam adaptador de transporte real, autorização da tentativa e congelamento de nova campanha.** Controlo de alterações não equivale a isolamento completo. Sem garantia de poupança de quota ou janela de subscrição. Histórico, governação geral e diretório .github/ não seguido do utilizador intactos.

[JSON — CLI simulation](v2-2-lean-preflight.json) · [Manifest](../governance/v2-2-lean-draft.json) · [Launcher](../scripts/run_v2_2_lean.py) · [Tests](../tests/test_v2_2_lean.py) · [Audit](v2-2-cost-audit.pt.md) · [README](../README.pt.md)
