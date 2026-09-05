# Política de registo público

[Français](LOGGING.md) · [English (UK)](LOGGING.en.md) · [Español](LOGGING.es.md) · **Português**

O registo torna o processo auditável sem expor conversas completas. Cada
entrada recebe um número sequencial estável, sem data nem hora.

## Conteúdo preservado

- resumo do pedido humano;
- resumo da resposta ou ação do agente;
- papéis dos agentes participantes;
- decisões e justificações úteis à experiência;
- ficheiros afetados e resultados dos controlos;
- erros, correções e intervenções humanas relevantes;
- métricas disponíveis, qualificadas quando aproximadas.

## Conteúdo excluído

- prompts ou respostas brutas com dados pessoais;
- segredos, tokens, frases secretas, chaves privadas e caminhos de autenticação;
- detalhes de conta irrelevantes;
- raciocínio interno ou texto literal desnecessário;
- marcas temporais no histórico público.

Um Markdown público pode preservar uma data ou duração do protocolo, mas não o
horário de trabalho do autor. Um dado ocultado é omitido ou marcado como não
publicado; nunca é substituído por uma hora inventada.

## Forma de uma entrada

```markdown
## Interação 000

**Pedido resumido** — …

**Resposta resumida** — …

**Trace útil** — atores, decisões, ficheiros e controlos.
```

Os metadados de um run podem preservar datas e durações exigidas pelo protocolo.
Após cada interação que altere o repositório, a entrada é adicionada antes do
commit. O corpo do commit resume objetivo, alterações e controlos, seguindo-se
o push salvo instrução explícita em contrário.

## Ata de cada run

Cada run publicado possui um `PV.md` separado do histórico geral. Identifica o
patrocinador, o orquestrador experimental, o agente candidato, os consultores e
o verificador, numerando mandatos, pareceres, respostas, decisões, correções e
vereditos observáveis.

A ata é uma síntese probatória, não uma transcrição integral. Liga decisões a
ficheiros, testes e métricas, assinala saídas não capturadas e exclui raciocínio
interno bruto. A partir de V2, cada recomendação indica o papel e a decisão
fundamentada do orquestrador: aceite, rejeitada ou não verificável.
