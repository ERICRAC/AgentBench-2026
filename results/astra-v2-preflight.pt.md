# Preflight V2 Astra — resultado

[Français](astra-v2-preflight.md) · [English (UK)](astra-v2-preflight.en.md) · [Español](astra-v2-preflight.es.md) · **Português**

Preflight mínimo **aprovado nos 4 papéis**, após publicar V1 em `c959216`. Não é uma célula do benchmark: a campanha mantém **2/6**.

| Papel | Profissão | Entrada + saída | Duração |
| --- | --- | ---: | ---: |
| MAIN | Orquestrador / escritor | 12673 | 8.406 s |
| SA-01 | Requisitos e segurança | 12512 | 8.7 s |
| SA-02 | Arquitetura e testabilidade | 12514 | 7.134 s |
| SA-03 | Crítico QA adversarial | 12320 | 7.383 s |

## Controlos observados

Quatro configurações TOML aceites com validação estrita, threads novos distintos, sem histórico fornecido, respostas exatas e SHA-256 coincidentes. Todos terminaram com código 0 e contadores. Nenhum comando ou escrita observado no diretório temporário vazio.

[JSON](../governance/astra-v2-preflight/run.json)

## Âmbito e limites

Motor A-08: sessões `codex exec --json` separadas. O contrato nativo disponível não expõe contexto/compactação e contadores individuais. Não é uma comparação de motores.

`gpt-6-astra/high`, contexto 200.000, compactação 180.000 (`total`), CLI 0.153.4. Consultores configurados apenas para leitura. Instruções da plataforma e definições de ferramentas continuam presentes.

Não se força compactação nem se medem limites do servidor; também não se testa escrita proibida ou o ciclo social completo. Estes TOML contêm instruções de diagnóstico, não missões prontas para o benchmark.

## Medições e análise

49.961 tokens de entrada + 58 de saída = **50.019**; cache 36.352 já incluída. Raciocínio devolvido: 0 em respostas triviais com high. Soma de durações **31,623 s**, não tempo mural: as sessões sobrepõem-se e o tempo global não foi registado.

Custo de diagnóstico, não desempenho social ou de calculadora. O contexto de infraestrutura reforça a necessidade de contar cada chamada V2.

## Textos observáveis

Cada bloco associa pedido e resposta exatos. Não houve resolução conjunta; não se infere influência entre agentes.

### 1 · MAIN

[Config](../governance/astra-v2-preflight/MAIN.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est MAIN — Orchestrateur candidat et écrivain unique.
Réponds exactement : MAIN | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
MAIN | READY | ASTRA-PREFLIGHT
```

### 2 · SA-01

[Config](../governance/astra-v2-preflight/SA-01.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-01 — Analyste exigences et sécurité.
Réponds exactement : SA-01 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-01 | READY | ASTRA-PREFLIGHT
```

### 3 · SA-02

[Config](../governance/astra-v2-preflight/SA-02.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-02 — Architecte logiciel et testabilité.
Réponds exactement : SA-02 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-02 | READY | ASTRA-PREFLIGHT
```

### 4 · SA-03

[Config](../governance/astra-v2-preflight/SA-03.toml)

```text
Préflight technique AgentBench, extérieur au benchmark.
Ton rôle est SA-03 — Critique QA adversarial.
Réponds exactement : SA-03 | READY | ASTRA-PREFLIGHT
N'utilise aucun outil, ne lis aucun fichier, ne résous aucun défi et ne délègue rien.
```

```text
SA-03 | READY | ASTRA-PREFLIGHT
```

## Próximo passo

V1 publicada e preflight mínimo concluído. Próxima experiência: V2 Core com pareceres e decisões completos, seguida de relatório antes de Scientific. Benchmark V2 ainda não iniciado.
