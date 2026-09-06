# Node.js y Markdown en WSL Debian

[Français](node-wsl.md) · [English (UK)](node-wsl.en.md) · **Español** · [Português](node-wsl.pt.md)

Una extensión de lint VS Code no proporciona necesariamente Node.js al terminal Linux. `nodejs` instala el runtime y la orden `node`; `npm` proporciona el gestor de paquetes. Son herramientas de documentación, no dependencias de las calculadoras.

## Instalación en Debian 13

En un terminal WSL Debian:

```bash
sudo apt update
sudo apt install -y nodejs npm
hash -r
node --version
npm --version
```

[Debian nodejs](https://packages.debian.org/trixie/nodejs)

## Control Markdown

Desde la raíz del proyecto:

```bash
npx --yes markdownlint-cli@0.47.0 "**/*.md"
```

Versión CLI fijada para reproducibilidad. `.markdownlint.json` acepta líneas largas y HTML necesario para GitHub. `.markdownlintignore` excluye retos fijados, prompts y pruebas históricas; no deben reescribirse automáticamente.

## Diagnóstico observado

WSL encontraba un lanzador Windows que llamaba a un node Linux ausente. Node Windows 24.19.0 y markdownlint-cli 0.47.0 ejecutaron el control completo. Instalar en Debian elimina esa dependencia. Comprobar rutas Linux con `command -v node` y `command -v npm`.

## Auditoría del proyecto

V1 anteriores indexadas con SHA-256. Intentos interrumpidos separados de los éxitos. Informes distinguen medidas, costes de infraestructura y datos ausentes. Fórmula README conceptual, con indicadores medidos por separado. Sesgo histórico del cargador documentado sin alterar pruebas fijadas.

[V1 Astra](../results/astra-v1.es.md) · [V1 archives](../results/ARCHIVE_V1.es.md)
