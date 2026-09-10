# Instrumentação e publicação de resumos

**Português** · [Français](observability.md) · [English (UK)](observability.en.md) · [Español](observability.es.md)

[Guia e diagrama V2](reading-guide.pt.md) · [Resumos](../results/run-summaries/index.pt.md) · [Auditoria](documentation-audit.pt.md)

## Âmbito

Manutenção fora de runs. Nenhum benchmark relançado nem solução histórica editada. [run_v2.py](../scripts/run_v2.py), publisher histórico, prompts, permissões, papéis, barreiras e critérios intactos. O diagrama explica o protocolo congelado; não cria nova orquestração.

[run_v2_observed.py](../scripts/run_v2_observed.py) chama o lançador existente e envolve apenas run_session. Ativação **opcional**, declarada e pré-registada antes da próxima campanha. As escritas de medição acrescentam pequeno custo não quantificado; não afirmar tempos idênticos aos runs antigos. Testes com sessões falsas não validam futuras chamadas reais.

## Esquema genérico

[observe_sessions.py](../scripts/observe_sessions.py) não agenda trabalho. Aceita N sessões, papéis e grupos. Só v2_topology descreve V2 congelada; V2.x/V3 exige grafo próprio aprovado.

| Campo | Natureza e definição |
| --- | --- |
| session_id, role | Identidade canónica, não nome de modelo. |
| parallel_group | Grupo concorrente especificado; null em fases sequenciais. |
| depends_on | Sessões que devem terminar antes do início; barreiras especificadas. |
| receives_from | Identificadores das sessões fonte de textos ou artefactos, não prova de adoção. Desafio/mandato externo explicados no guia. |
| writes_solution | Permissão especificada, não prova de escrita efetiva. |
| started_at_seconds, ended_at_seconds | Medições monotónicas relativas à entrada do wrapper, antes da preparação do lançador; nunca horas civis. |
| duration_seconds em observation | Fim menos início da invocação completa: configuração, CLI, captura e análise de eventos; exclui escrita da observação. |
| duration_seconds histórico | Medida CLI original preservada, não substituída. |
| outcome | returned ou failed, não veredicto de aceitação. |

A origem do wrapper difere da de wall_duration_seconds histórico. Não subtrair entre referenciais. Só intervalos medidos sobrepostos provam sobreposição. Consultas históricas têm duração, não início/fim: nenhuma cronologia exata inventada.

## Fluxo futuro — só após autorização de run

Pré-registar primeiro diretório novo, desafio e configurações do protocolo aprovado. NEW-RUN é marcador, não tentativa criada aqui:

```bash
python3 -B scripts/run_v2_observed.py --run runs/NEW-RUN --challenge calculator
```

O diretório privado anunciado contém observations.json, atualizado no fim de cada sessão, incluindo falha. Uma paragem abrupta pode deixar sessões ausentes: não equivalem a zero. O observador não acrescenta prompts, texto de erros, raciocínio privado nem caminhos absolutos.

Após rever capturas e publicar normalmente com publish_v2.py, enriquecer uma **cópia nova**:

```bash
python3 -B scripts/attach_observations.py --trace runs/NEW-RUN/trace.json --observations /tmp/CAPTURE/observations.json --output runs/NEW-RUN/trace-observed.json
```

A fusão rejeita destinos existentes, identificadores ausentes/duplicados, papéis incoerentes, valores não finitos e barreiras violadas. Preserva métricas originais e exporta campos explicitamente permitidos. Capturas parciais exigem relatório de interrupção; nunca publicar capturas privadas em bloco. O filtro histórico não deteta todos os segredos: revisão prévia obrigatória.

Nos metadados do run **futuro**, referenciar trace-observed.json e hash, wrapper, observador, adaptador, seus hashes e lançador histórico. Nunca alterar metadados publicados. Publisher original disponível; enriquecimento e resumo fora do candidato.

## Geração editorial

```bash
python3 -B scripts/summarize_runs.py
python3 -B scripts/summarize_runs.py --check
python3 -B -m unittest discover -s tests -v
python3 -B scripts/check_documentation.py
markdownlint '**/*.md'
```

Primeira chamada: regenera cinco capas V2 e índice em quatro línguas. Factos: run.json/trace.json; análise revista manualmente: [run-interpretations.json](run-interpretations.json). Editar fonte, não páginas geradas. Ausentes continuam ausentes; cache/raciocínio não são somados duas vezes.

Topologia futura: run.json com run_id, challenge, mode, status, modelo/esforço, verification, usage e trace; trace contém roles e sessions com phase ou session_id, role, contadores e observation opcional. Chaves de verificação como nos ficheiros históricos. Aceita papéis locais e fases desconhecidas sem inventar V2.

```bash
python3 -B scripts/summarize_runs.py --run runs/NEW-RUN --interpretation /tmp/interpretation-reviewed.json
```

JSON editorial com fr/en/es/pt; sem texto, interpretação não registada. Saída em results/run-summaries, nunca runs/. Acrescentar futura capa a um índice adequado: o atual lista só cinco V2 completas. Código genérico não aprova protocolo V3.

## Verificações e limites

Testes: argumentos/retornos intactos, falhas preservadas, cinco papéis paralelos, igualdade de sete prompts/argumentos, barreiras, tempos simulados, contadores ausentes, rejeição de sobreposição de ficheiro, papel local e geração reproduzível. Não medem latência de rede nem consumo futuro do modelo.

[Verificações executadas e limites de apresentação](documentation-audit.pt.md). Validação real pendente de um run explicitamente autorizado.
