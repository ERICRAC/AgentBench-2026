# Clé SSH, phrase secrète, WSL et VS Code

## Objectif

Permettre à Git, VS Code et Codex de pousser vers GitHub avec la clé dédiée au
projet, sans écrire sa phrase secrète dans le dépôt, un script ou une variable
d'environnement.

## Le problème observé

Le dépôt utilise un alias SSH et une clé distincte afin de ne pas mélanger les
comptes GitHub. La clé privée est protégée par une phrase secrète. Un `git push`
exécuté dans un terminal interactif peut donc demander cette phrase et réussir,
alors qu'un processus non interactif affiche `Permission denied (publickey)` ou
une erreur liée à `ssh-askpass`.

La phrase secrète n'est pas destinée à devenir une variable d'environnement.
Le composant prévu pour la retenir temporairement est `ssh-agent`. Celui-ci
déchiffre la clé en mémoire après une saisie manuelle et expose seulement un
socket, désigné par `SSH_AUTH_SOCK`, aux processus autorisés.

Le point délicat avec VS Code sous WSL est l'héritage de l'environnement. Si
l'agent est démarré dans un terminal après le lancement de VS Code, le serveur
VS Code et ses extensions peuvent ne pas connaître le nouveau
`SSH_AUTH_SOCK`. Un terminal et un agent Codex ouverts depuis cette ancienne
session ne voient alors pas la clé, même si un autre terminal la voit.

## Solution recommandée

Depuis un terminal WSL, avant d'ouvrir le dossier dans VS Code :

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/agentbench-2026
ssh-add -l
code /chemin/vers/AgentBench-2026
```

La phrase secrète est saisie uniquement à l'invite de `ssh-add`. Elle reste en
mémoire dans l'agent pendant sa durée de vie. `ssh-add -l` doit afficher la clé
dédiée avant le lancement de VS Code.

Dans le terminal intégré de la nouvelle fenêtre VS Code, contrôler ensuite :

```bash
test -n "$SSH_AUTH_SOCK" && ssh-add -l
git ls-remote origin refs/heads/main
```

Si `ssh-add -l` ne voit aucun agent, fermer complètement la fenêtre WSL de VS
Code puis la relancer depuis le terminal où l'agent est chargé. Un simple nouvel
onglet de terminal ne suffit pas toujours, car le serveur VS Code conserve son
ancien environnement.

GitHub recommande `ssh-agent` pour mettre en cache une clé protégée, et la
documentation VS Code recommande de vérifier `ssh-add -l` dans l'environnement
réel où Git s'exécute :

- [GitHub — Working with SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)
- [VS Code — Remote Development troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting)

## Ce qu'il ne faut pas faire

- ne pas inscrire la phrase secrète dans `SSH-Helper.sh` ;
- ne pas l'exporter dans une variable telle que `SSH_PASSPHRASE` ;
- ne pas l'ajouter aux paramètres VS Code, au fichier `.env` ou à Git ;
- ne pas retirer la protection de la clé uniquement pour automatiser un push ;
- ne pas employer une clé GitHub générique partagée par plusieurs comptes si
  l'objectif est précisément de les isoler.

Le helper local peut démarrer ou interroger l'agent et appeler `ssh-add`, mais
il ne doit contenir que le chemin de la clé. Il reste exclu par `.gitignore`.

## Prompt prêt à transmettre à ChatGPT

```text
Je travaille sous Windows avec VS Code connecté à WSL2. Mon dépôt Git utilise
une clé SSH ED25519 dédiée, protégée par une phrase secrète, afin d'isoler ce
projet de mes autres comptes GitHub. Un git push fonctionne dans un terminal
interactif après saisie de la phrase secrète, mais les commandes lancées par
VS Code ou un agent Codex ne voient parfois pas la clé. SSH_AUTH_SOCK est absent
ou pointe vers un agent qui n'est pas hérité par le serveur VS Code.

Je veux une configuration ssh-agent persistante au niveau de ma session WSL,
sans mettre la phrase secrète dans un script, une variable d'environnement, le
projet, Git Credential Manager ou les paramètres VS Code. Explique-moi comment
démarrer l'agent avant VS Code, charger la clé manuellement, vérifier ssh-add -l
dans le terminal intégré et éviter les conflits entre l'OpenSSH Windows, Git
for Windows et l'OpenSSH WSL. Ne propose aucune solution qui stocke la phrase
secrète en clair.
```
