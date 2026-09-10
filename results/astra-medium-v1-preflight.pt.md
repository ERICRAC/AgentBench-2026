# Preflight V1 Astra médio — preparado, não iniciado

[Français](astra-medium-v1-preflight.md) · [English (UK)](astra-medium-v1-preflight.en.md) · [Español](astra-medium-v1-preflight.es.md) · **Português**

Duas tentativas solo novas preparadas. **44/44 controlos estáticos corretos; nenhum candidato, chamada de teste ao modelo ou resultado.** Só preparação autorizada. O modelo do chat não substitui configurações explícitas dos futuros candidatos.

## Tentativas reservadas

- Calculadora simples : [astra-medium-core-v1-001](../runs/astra-medium-core-v1-001/run.json) · [configuration](../runs/astra-medium-core-v1-001/config.toml) · [challenge](../runs/astra-medium-core-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-core-v2-001/run.json)
- Calculadora científica : [astra-medium-scientific-v1-001](../runs/astra-medium-scientific-v1-001/run.json) · [configuration](../runs/astra-medium-scientific-v1-001/config.toml) · [challenge](../runs/astra-medium-scientific-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-scientific-v2-001/run.json)

Cada diretório contém CHALLENGE.md, config.toml e run.json. Ambos solution/ locais estão vazios, sem .gitkeep nem solução anterior consultada/copiada. Git não preserva diretórios vazios: recriá-los após clonar com comandos abaixo.

## Comparabilidade e medição

Campanha associada astra-medium-001: **extensão V1 preparada após as V2 completas**, sem alterar metadados. Candidato solo novo, sem delegação; orquestrador de preparação/publicação fora das medidas. Publicar Core antes de Scientific, sem refinamento intermédio.

| Elemento | Decisão e prova |
| --- | --- |
| Modelo / esforço | gpt-6-astra / medium; igualdade verificada com quatro papéis V2. |
| Contexto / compactação | 200 000 / 180 000, âmbito total como V2; não é limite de consumo acumulado. |
| Configuração V1 | Cópia de governance/astra-v1.toml; apenas high → medium. Governação intacta. |
| Permissões | workspace-write para V1/MAIN V2; read-only para consultores. Web desativada, approval never, sem delegação. Escrita limitada a solution/ por instruções, não prova de isolamento real. |
| Prompts | codex-single.md e scientific-single.md históricos, hashes congelados; sem conselhos V2 acrescentados. |
| Desafios / árbitros | Hashes iguais a V2; simples 6 grupos/14 controlos; científica 9/57. [Lista explícita](../docs/acceptance-tests.pt.md). |
| Captura | scripts/capture_session.py histórico intacto, sem wrapper novo. Duração CLI; V2 inclui também retransmissão, diferença organizativa documentada. |
| Ambiente observado | CLI 0.153.4, Python 3.13.5, Node 20.19.2, npm 9.2.0. Mesma CLI V2; outros detalhes históricos não certificados aqui. |
| Resultados futuros | Primeiro/final/independente, correções antes/depois, duração, entrada/cache/saída/raciocínio, intervenções e textos. Atualmente null, não zero. |

V2 usa sete sessões/quatro papéis; V1 prevê uma. Primeira passagem V2 após crítica obrigatória, não assim V1. Diferenças do tratamento experimental, não parâmetros a igualar retroativamente.

## Checklist do preflight

O [controlo reproduzível](../scripts/preflight_v1_medium.py) realiza **22 asserções por diretório, 44 no total**:

- [x] Configuração V1 igual salvo esforço; identidade/modo; preparado e lançamento não autorizado.
- [x] Sem resultados inventados; solução presente, vazia e declarada acessível para escrita.
- [x] Seis hashes: configuração, prompt, desafio, testes, captura e verificador.
- [x] Desafio igual a SPEC; referência V2 completa na campanha associada.
- [x] Hashes de desafio/testes comuns; parâmetros e permissões dos quatro papéis verificados.
- [x] Contagem sintática de métodos (6/9), sem execução; CLI registada igual.

codex --version e codex exec --help corretos e mostram opções. Aviso local: aliases PATH não criados por sistema de ficheiros só de leitura; ambos comandos funcionam. TOML analisado, **não validado por lançamento Codex com estas configurações**.

```bash
mkdir -p runs/astra-medium-core-v1-001/solution runs/astra-medium-scientific-v1-001/solution
python3 -B scripts/preflight_v1_medium.py
```

## Execução futura — não autorizada aqui

Só após nova autorização: verificar ambiente, hashes, quota e diretórios; executar Core novo com configuração própria e prompt histórico; verificar e publicar antes de Scientific. Preservar interrupções; reinício de raiz recebe identificador novo.

Captura privada fora do repositório; publicar ata filtrada com papel, mandato exato, mensagens visíveis, comandos, controlos e decisões. Sem raciocínio privado, segredos ou horas em Markdown. Não atribuir novas anotações/contadores aos históricos.

## Limites, orçamento e continuação

**Preparação estática pronta; lançamento não autorizado.** Acesso Astra, autenticação, quota e aplicação real do contexto/esforço não testados. Sem instalações adicionais identificadas. Configuração explícita segundo [documentação oficial Codex](https://learn.chatgpt.com/docs/config-file/config-reference), sem garantia de acesso da conta.

Custo exato desconhecido; nenhum novo limite de tokens totais/tempo. Acrescentá-lo altera condições face a V2 e exige arbitragem distinta. Tokens de preparação não são custo candidato.

Mesmo alias não prova snapshot servidor imutável; V1 posterior a V2, sem aleatorização/repetições, variação de carga/cache e possíveis defeitos do carregador científico congelado limitam causalidade. **Comparação qualificada, não identidade perfeita.** Mantém-se dominância qualidade/tempo/tokens.

Próxima decisão: autorizar V1 simples separadamente, publicar antes da científica. Sem V2.1/V2.2 nem alteração de governação.

[V2 Astra medium](astra-medium-v2.pt.md) · [Conclusions](CONCLUSIONS.pt.md) · [README](../README.pt.md)
