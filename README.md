# AgentBench 2026

Expérience reproductible inspirée du projet [AutoGen de Yann Pointud](https://github.com/yannpointud/AutoGen).

## Question étudiée

Un agent Codex unique produit-il un résultat plus fiable et plus efficace qu'une orchestration multi-agent spécialisée pour un même petit projet logiciel ?

La V1 établit la référence **Codex seul**. Les variantes multi-agents et Ollama seront ajoutées seulement après validation de ce premier protocole.

## V1 : Calculator

Le premier défi reprend le template `Calculator` d'AutoGen. Le contrat complet se trouve dans `challenges/calculator/SPEC.md` et les contrôles indépendants dans `challenges/calculator/tests/`.

### Prérequis

- Debian ou une autre distribution Linux ;
- Python 3.10 ou supérieur ;
- Git ;
- Codex CLI connecté avec un abonnement ChatGPT (`codex login`).

Aucune clé API OpenAI n'est nécessaire pour cette V1 interactive.

### Lancer une tentative

```bash
python3 scripts/new_run.py codex-single-001
cd runs/codex-single-001
codex "$(cat ../../prompts/codex-single.md)"
cd ../..
python3 scripts/verify.py --solution runs/codex-single-001/solution
```

Chaque tentative doit partir d'un nouveau répertoire. Ne réutilisez pas une solution précédente.

## Principes du protocole

- même spécification pour tous les candidats ;
- aucun sous-agent dans la V1 ;
- aucune modification des tests ou de la spécification pendant une tentative ;
- tests déterministes comme arbitre technique ;
- conservation des échecs autant que des réussites ;
- publication des limites et des interventions humaines.

## Statut

La tentative de référence `codex-single-001` est terminée : les 6 contrôles
d'acceptation passent. Le détail reproductible est publié dans
[`results/codex-single-001.md`](results/codex-single-001.md).

Ce résultat constitue un point de référence, pas encore une comparaison. Le
benchmark multi-agent sera publié séparément afin de conserver des conditions
d'exécution clairement identifiables.

## Licence

MIT. AutoGen reste un projet indépendant appartenant à son auteur et n'est ni inclus ni forké dans ce dépôt.
