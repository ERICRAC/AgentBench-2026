# Clave SSH, frase de contraseña, WSL y VS Code

[Français](ssh-vscode.md) · [English (UK)](ssh-vscode.en.md) · **Español** · [Português](ssh-vscode.pt.md)

## Objetivo

Permitir que Git, VS Code y Codex publiquen en GitHub mediante la clave dedicada
del proyecto sin guardar la frase de contraseña en el repositorio, un script o
una variable de entorno.

## Problema observado

El repositorio utiliza un alias SSH y una clave distinta para aislar las
cuentas GitHub. Un `git push` interactivo puede pedir la frase y funcionar,
mientras un proceso no interactivo muestra `Permission denied (publickey)` o
un error de `ssh-askpass`.

La frase no debe convertirse en variable de entorno. `ssh-agent` mantiene la
clave descifrada en memoria tras la introducción manual y solo expone un socket
identificado por `SSH_AUTH_SOCK`.

Bajo WSL, VS Code hereda su entorno al arrancar. Si el agente se inicia después,
el servidor VS Code, sus extensiones y Codex pueden no ver el nuevo socket.

## Solución recomendada

Desde WSL, antes de abrir VS Code:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/agentbench-2026
ssh-add -l
code /ruta/a/AgentBench-2026
```

Introducir la frase únicamente en el prompt de `ssh-add`. Comprobar después en
el terminal integrado nuevo:

```bash
test -n "$SSH_AUTH_SOCK" && ssh-add -l
git ls-remote origin refs/heads/main
```

Si no se ve el agente, cerrar por completo la ventana WSL de VS Code y abrirla
desde el terminal donde está cargada la clave. Una pestaña nueva puede conservar
el entorno antiguo del servidor.

- [GitHub — frases de contraseña SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
- [VS Code — resolución de problemas remotos](https://code.visualstudio.com/docs/remote/troubleshooting)

## Qué no hacer

- guardar la frase en `SSH-Helper.sh`, `.env`, Git o VS Code;
- exportarla como `SSH_PASSPHRASE`;
- retirar la protección para automatizar un push;
- compartir una clave genérica entre cuentas que deben permanecer aisladas.

El helper local puede iniciar o consultar el agente y llamar a `ssh-add`, pero
solo contiene la ruta de la clave y permanece excluido por `.gitignore`.

## Prompt para ChatGPT

```text
Uso VS Code en Windows conectado a WSL2. Mi repositorio utiliza una clave SSH
ED25519 dedicada y protegida para aislar este proyecto de mis otras cuentas
GitHub. Los pushes interactivos funcionan tras introducir la frase, pero VS
Code o Codex a veces no ven la clave porque SSH_AUTH_SOCK está ausente o procede
de una sesión antigua.

Explica cómo iniciar ssh-agent antes de VS Code, cargar la clave manualmente,
verificar ssh-add -l en el terminal integrado y evitar conflictos entre
OpenSSH Windows, Git for Windows y OpenSSH WSL. No propongas guardar la frase en
texto claro.
```
