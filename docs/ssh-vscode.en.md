# SSH key, passphrase, WSL and VS Code

[Français](ssh-vscode.md) · **English (UK)** · [Español](ssh-vscode.es.md) · [Português](ssh-vscode.pt.md)

## Objective

Allow Git, VS Code and Codex to push to GitHub through the project's dedicated
key without storing its passphrase in the repository, a script or an
environment variable.

## Observed problem

The repository uses an SSH alias and a distinct key to keep GitHub accounts
separate. An interactive `git push` may request the protected key's passphrase
and succeed, while a non-interactive process reports `Permission denied
(publickey)` or an `ssh-askpass` error.

The passphrase must not become an environment variable. `ssh-agent` is designed
to retain the decrypted key in memory after manual entry and exposes only a
socket identified by `SSH_AUTH_SOCK`.

Under WSL, VS Code inherits its environment when it starts. If the agent starts
later, the VS Code server, extensions and Codex sessions may not see the new
socket even when another terminal does.

## Recommended solution

From a WSL terminal, before opening VS Code:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/agentbench-2026
ssh-add -l
code /path/to/AgentBench-2026
```

Enter the passphrase only at the `ssh-add` prompt. Then verify in the new VS
Code integrated terminal:

```bash
test -n "$SSH_AUTH_SOCK" && ssh-add -l
git ls-remote origin refs/heads/main
```

If no agent is visible, fully close the WSL VS Code window and reopen it from
the terminal where the key is loaded. A new terminal tab may retain the old VS
Code server environment.

- [GitHub — Working with SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
- [VS Code — Remote Development troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting)

## Do not

- put the passphrase in `SSH-Helper.sh`;
- export it as `SSH_PASSPHRASE`;
- add it to VS Code settings, `.env` or Git;
- remove key protection merely to automate a push;
- share one generic GitHub key across accounts that should remain isolated.

The local helper may start or query the agent and invoke `ssh-add`, but should
contain only the key path and remain excluded by `.gitignore`.

## Prompt for ChatGPT

```text
I use VS Code on Windows connected to WSL2. My Git repository uses a dedicated,
passphrase-protected ED25519 SSH key to isolate this project from my other
GitHub accounts. Interactive pushes work after manual entry, but VS Code or
Codex sometimes cannot see the key because SSH_AUTH_SOCK is absent or inherited
from an older session.

Explain how to start a persistent ssh-agent before VS Code, load the key
manually, verify ssh-add -l in the integrated terminal and avoid conflicts
between Windows OpenSSH, Git for Windows and WSL OpenSSH. Do not suggest storing
the passphrase in plain text anywhere.
```
