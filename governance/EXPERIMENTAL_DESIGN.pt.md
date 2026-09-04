# Plano experimental e comparabilidade

[Français](EXPERIMENTAL_DESIGN.md) · [English (UK)](EXPERIMENTAL_DESIGN.en.md) · [Español](EXPERIMENTAL_DESIGN.es.md) · **Português**

Este documento fixa a estrutura da campanha AgentBench 2026. Separa as
comparações obrigatórias das variantes exploratórias e impede que uma afinação
posterior reescreva condições já publicadas.

## Matriz principal

| Modo | Objetivo Calculadora Core | Objetivo Calculadora Scientific |
| --- | --- | --- |
| V1 · Codex sozinho | obrigatório | obrigatório |
| V2 · Codex multiagente governado | obrigatório | obrigatório |
| V3 · Codex + Ollama | obrigatório | obrigatório |

Cada célula é uma tentativa isolada com prompt identificado, configuração
registada e veredicto independente. V1, V2 e V3 são **modos de organização**,
não versões do software.

## Marco de observação

Depois de cada modo:

- publicar ambos os resultados antes de qualquer alteração;
- consolidar pontuação, duração, tokens, correções, intervenções e eventos de
  coordenação observados;
- formular conclusões e limites antes de propor mudanças;
- associar cada afinação a uma hipótese mensurável e critério de decisão.

A afinação pode afetar modelo, prompt, papéis, contexto ou parâmetros; não
implica necessariamente treinar os pesos do modelo.

## Campanhas e repetições

Uma campanha é identificada pelas versões dos desafios e verificadores,
modelos, parâmetros estruturais e prompts. Uma alteração substancial abre uma
nova campanha. Repetem-se as células V1 até ao modo estudado necessárias à
comparação. Resultados anteriores permanecem publicados e nunca são
substituídos ou agregados silenciosamente. Corrigir um verificador após o
primeiro candidato cria uma nova versão do desafio.

Uma correção do candidato durante um run pertence a esse run e não abre outra
campanha.

## Variantes opcionais

**V2.1** pode testar uma organização afinada, nas duas dificuldades, depois de
V2 ser publicada e analisada. Não substitui V2 nem conta entre as seis células.

**V4** fica reservado a um controlo histórico AutoGen comparável caso a síntese
V1–V3 demonstre a sua utilidade. Outras arquiteturas futuras recebem outro nome.

## Comparação final

Os verificadores independentes determinam o veredicto funcional. A síntese
compara no mínimo conformidade, duração, tokens, correções, intervenções
humanas, divergências, decisões e custo de coordenação. Uma melhoria só é
atribuída à organização dentro da mesma campanha ou qualificando explicitamente
as diferenças de configuração.
