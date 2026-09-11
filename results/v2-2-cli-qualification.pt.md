# Qualificação do CLI V2.2

[Français](v2-2-cli-qualification.md) · [English (UK)](v2-2-cli-qualification.en.md) · [Español](v2-2-cli-qualification.es.md) · **Português**

**Conclusão: mudar de instalação não elimina o bloqueio.**

Três execuções da mesma sonda sem modelo: CLI autónomo 0.153.4, pacote npm oficial 0.153.4 instalado separadamente e binário da extensão 0.154.0-alpha.6.1. Cada um passa 7/8 controlos; catálogo fora da lista permitida. Os dois binários 0.153.4 têm SHA-256 idêntico. Sem alterações de PATH, conta ou extensão.

O catálogo incluído atribui a gpt-6-astra e gpt-5.6-sol tool_mode=code_mode_only e multi_agent_version=v2. Indício compatível com as ferramentas observadas, não prova causal interna. Não alteramos metadados para forçar aprovação. Passar a Sol elevado não é solução demonstrada; Astra médio ativo, Astra elevado apenas histórico.

57 testes aprovados: 52 anteriores e 5 controlos do catálogo (formato clássico, additional_tools aninhado, ambas localizações, vazio/duplicados, ferramenta desconhecida). Vazio não equivale a restrição válida.

Preflight aceita --cli e regista versão, hash do binário e campos públicos do catálogo incluído. Fornecedor HTTP fictício local, HOME/CODEX_HOME vazios, sem autenticação ou inferência. Erros HTTP intencionais, sem custo modelo medido.

Próximo passo útil: testar encaminhamento efetivo e recusa de capacidades proibidas com chamadas fictícias não mutativas. Anunciar não prova execução. Sem congelamento, sonda autenticada ou benchmark até demonstrar essa fronteira. Reinstalar novamente a mesma versão não acrescenta evidência.

Instalação de teste conservada fora do repositório em diretório temporário dedicado; nenhum helper/pacote publicado. OpenAI Docs orientou seleção do pacote oficial; conclusões baseadas nas sondas locais.

[JSON](v2-2-cli-qualification.json) · [MCP](v2-2-bridge.pt.md) · [OpenAI Docs](https://learn.chatgpt.com/docs/codex/cli) · [README](../README.pt.md)
