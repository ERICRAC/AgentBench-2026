# Node.js e Markdown no WSL Debian

[Français](node-wsl.md) · [English (UK)](node-wsl.en.md) · [Español](node-wsl.es.md) · **Português**

Uma extensão de lint VS Code não fornece necessariamente Node.js ao terminal Linux. `nodejs` instala o runtime e comando `node`; `npm` fornece o gestor de pacotes. São ferramentas de documentação, não dependências das calculadoras.

## Instalação no Debian 13

Num terminal WSL Debian:

```bash
sudo apt update
sudo apt install -y nodejs npm
hash -r
node --version
npm --version
```

[Debian nodejs](https://packages.debian.org/trixie/nodejs)

## Controlo Markdown

Na raiz do projeto:

```bash
npx --yes markdownlint-cli@0.47.0 "**/*.md"
```

Versão CLI fixada para reprodutibilidade. `.markdownlint.json` aceita linhas longas e HTML necessário ao GitHub. `.markdownlintignore` exclui desafios fixos, prompts e provas históricas; não devem ser reescritos automaticamente.

## Diagnóstico observado

WSL encontrava um lançador Windows que chamava um node Linux ausente. Node Windows 24.19.0 e markdownlint-cli 0.47.0 executaram o controlo completo. Instalar no Debian remove essa dependência. Confirmar caminhos Linux com `command -v node` e `command -v npm`.

## Auditoria do projeto

V1 anteriores indexadas com SHA-256. Tentativas interrompidas separadas dos sucessos. Relatórios distinguem medições, custos de infraestrutura e dados ausentes. Fórmula README conceptual, com indicadores medidos separadamente. Viés histórico do carregador documentado sem alterar testes fixos.

[V1 Astra](../results/astra-v1.pt.md) · [V1 archives](../results/ARCHIVE_V1.pt.md)
