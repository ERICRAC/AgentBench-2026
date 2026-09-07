# Node.js and Markdown in WSL Debian

[Français](node-wsl.md) · **English (UK)** · [Español](node-wsl.es.md) · [Português](node-wsl.pt.md)

A VS Code lint extension does not necessarily provide Node.js to the Linux terminal. Debian's `nodejs` package installs the runtime and `node` command; `npm` supplies the package manager. These are documentation tools, not calculator runtime dependencies.

## Install on Debian 13

Run in a WSL Debian terminal:

```bash
sudo apt update
sudo apt install -y nodejs npm
hash -r
node --version
npm --version
```

[Debian nodejs](https://packages.debian.org/trixie/nodejs)

## Markdown check

From the repository root:

```bash
npx --yes markdownlint-cli@0.47.0 "**/*.md"
```

The CLI version is pinned for reproducibility. `.markdownlint.json` allows long lines and the HTML needed by GitHub visuals. `.markdownlintignore` excludes frozen challenges, prompts and historical evidence; automatic style fixes must not rewrite them.

## Observed diagnosis

WSL found a Windows markdownlint wrapper that called a missing Linux node. Explicit Windows Node 24.19.0 and markdownlint-cli 0.47.0 ran the full check successfully. Debian installation removes this Windows-runtime dependency. Check `command -v node` and `command -v npm` for Linux paths.

## Project audit

Earlier V1 evidence is indexed and SHA-256 protected. Interrupted attempts are not recast as successes. Reports separate available measurements, infrastructure costs and missing data. The README formula is conceptual, while measured indicators retain distinct units. The historical test-loader bias stays documented without modifying frozen tests.

[V1 Astra](../results/astra-v1.en.md) · [V1 archives](../results/ARCHIVE_V1.en.md)

Final WSL check: Node.js `20.19.2` at `/usr/bin/node`, npm `9.2.0` at `/usr/bin/npm`, and markdownlint `0.47.0`. All editorial Markdown now passes lint directly with the Linux runtime.
