# Chave SSH, frase secreta, WSL e VS Code

[Français](ssh-vscode.md) · [English (UK)](ssh-vscode.en.md) · [Español](ssh-vscode.es.md) · **Português**

## Objetivo

Permitir que Git, VS Code e Codex façam push para o GitHub através da chave
dedicada do projeto sem guardar a frase secreta no repositório, num script ou
numa variável de ambiente.

## Problema observado

O repositório usa um alias SSH e uma chave distinta para isolar contas GitHub.
Um `git push` interativo pode pedir a frase e funcionar, enquanto um processo
não interativo apresenta `Permission denied (publickey)` ou erro `ssh-askpass`.

A frase não deve tornar-se uma variável de ambiente. O `ssh-agent` mantém a
chave decifrada em memória após introdução manual e expõe apenas um socket
identificado por `SSH_AUTH_SOCK`.

No WSL, o VS Code herda o ambiente ao arrancar. Se o agente começar depois, o
servidor VS Code, extensões e Codex podem não ver o novo socket.

## Solução recomendada

No WSL, antes de abrir o VS Code:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/agentbench-2026
ssh-add -l
code /caminho/para/AgentBench-2026
```

Introduza a frase apenas no prompt do `ssh-add`. Depois verifique no novo
terminal integrado:

```bash
test -n "$SSH_AUTH_SOCK" && ssh-add -l
git ls-remote origin refs/heads/main
```

Se o agente não aparecer, feche totalmente a janela WSL do VS Code e reabra-a
a partir do terminal onde a chave está carregada. Um novo separador pode manter
o ambiente antigo do servidor.

- [GitHub — frases secretas de chaves SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
- [VS Code — resolução de problemas remotos](https://code.visualstudio.com/docs/remote/troubleshooting)

## O que não fazer

- guardar a frase em `SSH-Helper.sh`, `.env`, Git ou VS Code;
- exportá-la como `SSH_PASSPHRASE`;
- remover a proteção apenas para automatizar um push;
- partilhar uma chave genérica entre contas que devem permanecer isoladas.

O helper local pode iniciar ou consultar o agente e chamar `ssh-add`, mas deve
conter apenas o caminho da chave e permanecer excluído por `.gitignore`.

## Prompt para o ChatGPT

```text
Uso o VS Code no Windows ligado ao WSL2. O meu repositório utiliza uma chave SSH
ED25519 dedicada e protegida para isolar este projeto das minhas outras contas
GitHub. Os pushes interativos funcionam após introduzir a frase, mas o VS Code
ou Codex por vezes não veem a chave porque SSH_AUTH_SOCK está ausente ou foi
herdado de uma sessão antiga.

Explica como iniciar ssh-agent antes do VS Code, carregar a chave manualmente,
verificar ssh-add -l no terminal integrado e evitar conflitos entre OpenSSH do
Windows, Git for Windows e OpenSSH do WSL. Não proponhas guardar a frase em
texto simples.
```
