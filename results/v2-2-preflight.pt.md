# Preflight técnico V2.2 — simulações, nenhum modelo

[Français](v2-2-preflight.md) · [English (UK)](v2-2-preflight.en.md) · [Español](v2-2-preflight.es.md) · **Português**

**V2.2: piloto aprovado; 46 testes e isolamento local 30/30.** Seis processos fictícios, sem chamadas modelo. Perfil nativo 26/30: integração modelo não qualificada, lançamento bloqueado. Comparação Sol/Astra e esforço preservada. [Transport / isolation](v2-2-transport.pt.md)

**Preflight estático/simulado concluído: 2 desafios × 3 fases; 26 testes novos, 38 de manutenção no total. Sem chamada a modelo, pontuação de calculadora ou alteração histórica.** Protocolo não congelado, lançamento não autorizado.

## Entregue

O [relé](../scripts/run_v2_2.py) executa MAIN inicial → REV-01 → MAIN final com transporte determinista injetado. O [preflight](../scripts/preflight_v2_2.py) verifica escolhas, duas configurações, inventaria 15 hashes e simula ambos os desafios em diretórios temporários novos. Três [mandatos](../governance/V2_2_PROTOCOL.pt.md) intactos. [Configurações e escolhas](../governance/v2-2-draft/choices.json).

Capturas privadas: prompts exatos, JSONL, respostas visíveis, comandos/saídas, contadores, estado por fase e instantâneos inicial/final com texto/SHA-256. Sem filtro automático de publicação: não publicar diretórios brutos. Raciocínio privado excluído das transmissões. Falhas preservam provas disponíveis e param sem repetição. Se contadores não puderem ser extraídos da captura incompleta, bruto preservado e total desconhecido.

**Simulação não valida transporte real.** Argumentos Codex são construídos sem processos modelo; --live falha antes de criar capturas. Sessões fictícias escrevem SIMULATION ONLY, não soluções. Contadores sintéticos (39 entrada + saída por cenário nominal), nunca consumo real. Preflight público sem pontuação/consumo fictícios como resultados.

Hashes detetam escritas proibidas persistentes dentro do workspace; não impedem nem detetam todas as leituras externas ou escritas transitórias. Permissões read-only/workspace-write verificadas na configuração, sem isolamento OS real nos testes Python. Truncamento declarado/marcador reconhecido bloqueia; ausência não prova integridade CLI. SIGKILL não pode ser capturado: apenas último checkpoint garantido. Faltam permissões efetivas, transporte/paragem de processos, verificação independente de instantâneos e publicação filtrada.

## Reproduzir sem modelo

```bash
python3 -B scripts/preflight_v2_2.py
python3 -B -m unittest discover -s tests -v
```

```bash
sim_root=$(mktemp -d /tmp/agentbench-lean-demo-XXXXXX)
python3 -B scripts/run_v2_2.py --simulate --challenge calculator --output "$sim_root/simple"
python3 -B scripts/run_v2_2.py --simulate --challenge scientific-calculator --output "$sim_root/scientific"
```

## Lista de 26 testes V2.2

Cada linha corresponde a método test_ do [ficheiro](../tests/test_v2_2.py), alfabeticamente. Acrescem 12 testes anteriores; nenhum substitui grupos de calculadora. Testes V2.2 bloqueiam subprocess.Popen e socket com duplos que falham se chamados.

| ID | Controlo | test_… |
| --- | --- | --- |
| T01 | Captura separada do candidato | capture_cannot_be_nested_in_workspace |
| T02 | Configuração e comando sem execução | configuration_and_unexecuted_argv |
| T03 | Alteração de esforço recusada | configuration_drift_rejected |
| T04 | Eventos inválidos recusados | invalid_event_envelope |
| T05 | JSON incompleto preservado; paragem | invalid_json_capture_preserved |
| T06 | Interrupção de teclado registada | keyboard_interrupt_checkpointed |
| T07 | Modo real recusado antes de executar | live_rejected_before_transport_or_capture |
| T08 | Entregável ausente bloqueia | missing_deliverable_stops |
| T09 | Entregável extra bloqueia | missing_or_extra_deliverable_stops |
| T10 | Contadores ausentes não são zero | missing_usage_is_not_zero |
| T11 | Reutilização de solução/captura recusada | nonempty_solution_and_existing_capture_refused |
| T12 | Falha preserva captura e contadores | nonzero_process_retains_raw_and_metrics |
| T13 | Saídas ausentes, truncadas, eventos/contadores inválidos | parser_rejects_incomplete_unsupported_events_and_bad_usage |
| T14 | Falha de revisão: sem repetição ou fase final | phase_failure_preserved_without_retry |
| T15 | Dois desafios simulados, hashes, sem pontuação | preflight_no_model_no_verdict_and_hash_inventory |
| T16 | Alteração de escolhas/autorização recusada | preflight_refuses_changed_choice_or_authority |
| T17 | Alteração do desafio detetada | protected_workspace_write_stops |
| T18 | Raciocínio excluído, texto visível intacto | reasoning_excluded_visible_text_unchanged |
| T19 | Reutilização de thread recusada | reused_thread_stops |
| T20 | Escrita do revisor detetada; sem final | reviewer_write_stops_before_final |
| T21 | CLI simulada nos dois desafios; sem sobrescrita | simulation_cli_both_challenges_and_no_overwrite |
| T22 | Ligações simbólicas/físicas e binários recusados | snapshot_rejects_symlinks_hardlinks_and_binary |
| T23 | Diretório simbólico recusado | symlink_workspace_rejected |
| T24 | Ordem, transmissão integral, instantâneos e medidas | three_phases_full_handover_and_snapshots |
| T25 | Marcador de truncamento bloqueia | truncated_output_marker_stops |
| T26 | Excesso de palavras preservado sem truncar ou repetir | word_overrun_recorded_without_truncation_or_retry |

## Escolhas antes de congelar

Proposta por validar: piloto exploratório, uma tentativa por calculadora, Astra médio, três sessões, revisão de 1200 palavras; publicar simples antes da autorização científica. Sem novo teto global, parar por quota, sem espera/repetição automáticas. Sem garantia de quota Plus. Os 18 runs de confirmação são proposta separada, não comprometida. Orçamento numérico altera desenho: decidir antes de congelar e comparar referências coerentemente.

Após validar escolhas: preparar/qualificar transporte real e isolamento sem candidato benchmark; teste modelo trivial exige autorização separada. Depois congelar hashes e pedir autorização simples. Inventário do rascunho atual, não congelamento nem preflight de acesso.

OpenAI Docs orientou JSONL/textos visíveis e opções efémeras/sandbox. [Documentação oficial](https://learn.chatgpt.com/docs/non-interactive-mode). Ajuda local codex exec --help e versão 0.153.4 consultadas sem chamada modelo; TOML válido não prova aceitação, acesso Astra ou quota.

[Protocolo V2.2](../governance/V2_2_PROTOCOL.pt.md) · [JSON](v2-2-preflight.json) · [README](../README.pt.md)
