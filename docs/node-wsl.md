# Node.js et Markdown dans WSL Debian

**Français** · [English (UK)](node-wsl.en.md) · [Español](node-wsl.es.md) · [Português](node-wsl.pt.md)

Une extension de lint VS Code ne fournit pas nécessairement le runtime Node.js au terminal Linux. Le paquet `nodejs` installe le runtime et la commande `node`; `npm` fournit le gestionnaire de paquets. Ces outils servent à la documentation, pas à l'exécution des calculatrices.

## Installation dans Debian 13

Depuis un terminal WSL Debian, hors ou dans le projet :

```bash
sudo apt update
sudo apt install -y nodejs npm
hash -r
node --version
npm --version
```

[Debian nodejs](https://packages.debian.org/trixie/nodejs)

## Contrôle Markdown

Depuis la racine du projet :

```bash
npx --yes markdownlint-cli@0.47.0 "**/*.md"
```

Le CLI est épinglé pour rendre ce contrôle reproductible. `.markdownlint.json` accepte les longues lignes et les éléments HTML nécessaires aux visuels GitHub. `.markdownlintignore` exclut les défis figés, prompts et preuves historiques : leur contenu ne doit pas être réécrit par un correcteur automatique.

## Diagnostic observé

Le lanceur Windows de markdownlint était trouvé dans le PATH WSL, mais appelait un `node` Linux absent. Node Windows 24.19.0 et markdownlint-cli 0.47.0 ont permis un contrôle complet explicite. L'installation Debian évite cette dépendance au runtime Windows. Vérifier `command -v node` et `command -v npm` : les chemins Linux sont attendus.

## Audit du projet

Les anciennes V1 sont indexées et protégées par empreintes SHA-256. Les essais interrompus ne sont pas convertis en succès. Les rapports séparent les métriques disponibles, les coûts d'infrastructure et les données absentes. La formule du README reste conceptuelle ; les indicateurs mesurés ont leurs unités propres. Le biais historique du chargeur de tests reste documenté sans modification de la suite figée.

[V1 Astra](../results/astra-v1.md) · [V1 archives](../results/ARCHIVE_V1.md)
