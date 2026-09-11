# V2.2 — transporte, isolamento e modelos

[Français](v2-2-transport.md) · [English (UK)](v2-2-transport.en.md) · [Español](v2-2-transport.es.md) · **Português**

## Resumo

**Piloto aprovado; lançamento bloqueado.** Uma tentativa por calculadora, sem novo limite global, paragem por quota e sem repetição automática. Astra médio permanece ativo. Nem 18 repetições nem uma sonda modelo estão autorizadas.

Transporte por processos reais e isolamento local testados; integração modelo autenticada ainda não qualificada. Sem congelamento, chamadas modelo ou novas pontuações.

## Verificação

- [x] 46 testes de manutenção: 38 anteriores e 8 novos.
- [x] Bubblewrap: **30/30 controlos** com testemunhos descartáveis.
- [x] Duas simulações do relé, três processos Python isolados por desafio: MAIN inicial, REV-01 e MAIN final. Respostas fictícias, consumo modelo e veredicto ausentes.
- [x] Contraprova Codex nativo: **26/30**, quatro desvios preservados.
- [ ] Qualificar transporte autenticado e todas as ferramentas candidatas.
- [ ] Congelar e pedir autorização separada para calculadora simples.

[Observações e hashes](v2-2-transport.json) · [Preflight estático atualizado](v2-2-preflight-approved.json) · [Etapa anterior](v2-2-preflight.pt.md)

Catorze controlos por papel: ler contrato/solução; criar, alterar, renomear e apagar solução (MAIN permitido, REV proibido); negar leitura/escrita exterior direta e por ligação simbólica, escrita do contrato e ligação loopback ao anfitrião; preservar contrato/testemunho do anfitrião. Dois controlos sem sandbox confirmam acesso ao testemunho e ligação antes do isolamento.

Apenas testemunhos próprios são criados e removidos, sem segredos reais nem Internet. Bubblewrap monta diretórios de execução e workspace só de leitura, solução escrevível apenas para MAIN, raiz sintética só de leitura, rede separada e ambiente limpo.

**Desvio nativo:** leitura do testemunho anfitrião negada e ficheiros anfitriões intactos, mas criação permitida nesse caminho na camada sintética, diretamente e por ligação: dois desvios por papel. Não demonstra fuga do ficheiro anfitrião; viola a regra estrita de não escrever fora de solution/. Um ensaio anterior em /tmp perdeu leituras necessárias ao proibir o diretório pai; a prova retida reproduz a localização real dos runs fora de /tmp.

Bubblewrap não envolve o CLI autenticado: não tem credenciais nem rede modelo. Isto não valida todas as ferramentas Codex. Nenhuma alternativa permissiva ativada.

## Transporte e limites

[Implementação](../scripts/v2_2_transport.py): ficheiros privados exclusivos de entrada/saída/erro, sem shell, truncagem aplicativa ou repetição; estados em falha de criação, saída não nula e expiração. Grupo de processos parado após execução/interrupção; SIGKILL do pai ou falha de máquina pode impedir fecho. Os 30 segundos são das sondas, não orçamento candidato.

[Oito testes](../tests/test_v2_2_transport.py): fluxos exatos/permissões privadas; saída 7 parcial; expiração/paragem; saída de 2 MB; reutilização recusada; executável ausente; comando sem sandbox_mode antigo; papel/ligação inválidos.

OpenAI Docs orientou a separação de perfis e sandbox_mode. Prevalece a sintaxe local: codex sandbox, sem subcomando linux. [Permissões](https://learn.chatgpt.com/docs/permissions). Construtor nativo experimental, não ligado ao lançamento.

## Modelo, esforço e organização

Totais concluídos das duas calculadoras; tokens entrada + saída, cache já incluída. Pontuação final igual: 15 grupos / 71 controlos.

| Organização | Modelo / esforço | Tempo total (s) | Tokens |
| --- | --- | ---: | ---: |
| V1 | Sol elevado | 1199,432 | 454376 |
| V1 | Astra elevado | 499,653 | 340988 |
| V1 | Astra médio | 287,132 | 217884 |
| V2 | Sol elevado | 2384,139 | 1475626 |
| V2 | Astra médio | 1023,177 | 978998 |

[Sol/Astra V1](sol-vs-astra-v1.pt.md) · [Sol V2](sol-v2.pt.md) · [Astra médio](astra-medium-v1-v2.pt.md) · [V2 elevado interrompido](astra-v2-retired.pt.md)

V1 Astra elevado: **56,5 % mais tokens e 74,0 % mais tempo** que médio. Uma observação com correções diferentes não prova causalidade. V2 científica elevado interrompida: sem total completo comparável; consumo ausente não é zero.

Esgotamento rápido da quota: observação do utilizador, não medida de cobrança Plus. Faltam leituras de quota antes/depois por run; não se garante que médio caiba nem que elevado seja sempre impossível.

Preservar Sol elevado e Astra elevado. Comparar organização fixando modelo/esforço; comparar modelo fixando organização/esforço. Astra médio contra Sol elevado mistura fatores. Futura V2.2 Sol elevado requer outra autorização.

## Reproduzir e continuar

```bash
python3 -B -m unittest discover -s tests -v
python3 -B scripts/preflight_v2_2_isolation.py --backend bwrap
python3 -B scripts/preflight_v2_2_isolation.py --backend native
```

O último comando deve falhar atualmente. Sondas executadas com autorização fora da sandbox aninhada, sem enfraquecer proteção candidata.

Próximo: ligar autenticação do orquestrador e ferramentas confinadas; sonda modelo só autorizada. Sem novos pacotes necessários: bubblewrap 0.12.0 presente. Evidências históricas, desafios e testes intactos.

[Protocolo](../governance/V2_2_PROTOCOL.pt.md) · [Conclusões](CONCLUSIONS.pt.md) · [README](../README.pt.md)
