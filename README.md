# AgentBench 2026

**Français** · [English (UK)](README.en.md) · [Español](README.es.md) · [Português](README.pt.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-social-agents.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-social-agents-light.png">
  <img alt="AgentBench 2026 — un agent face à un collectif d'agents" src="assets/agentbench-social-agents-light.png">
</picture>

> Un laboratoire R&D ouvert sur le comportement social des agents IA : quand
> plusieurs agents collaborent, produisent-ils davantage d'intelligence… ou
> surtout davantage de bruit ?

![Campagne](https://img.shields.io/badge/campagne-2%2F6_validations-22c55e)
![Progression](https://img.shields.io/badge/progression-33%25-06b6d4)
![Prochaine étape](https://img.shields.io/badge/prochaine-V2_Calculatrice_Core-8b5cf6)
![Licence](https://img.shields.io/badge/licence-MIT-f97316)

AgentBench 2026 compare trois organisations d'agents sur deux défis de même
famille. Il mesure le résultat, mais aussi le temps, les tokens, les
corrections, les interventions humaines et le bruit de coordination.

Le projet a été imaginé et piloté **entièrement au microphone avec Codex** par
[Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/). Le dialogue
humain–agent fait donc partie de l'expérience autant que le code produit.

## Tableau de bord — état actuel

| Campagne principale | V1 · Codex seul | Prochain run | Protocoles |
| :---: | :---: | :---: | :---: |
| **2 / 6 validés** | **2 / 2 répliqués** | **V2 · Calculatrice Core** | **Défis figés · V2 à arbitrer** |
| `██████░░░░░░` **33 %** | Calculatrice Core **6/6** · Calculatrice Scientific **9/9** | Multi-agent gouverné | Vérificateurs indépendants |

```mermaid
%%{init: {"theme": "base", "themeVariables": {
  "primaryColor": "#0f2a4a",
  "primaryTextColor": "#f8fafc",
  "primaryBorderColor": "#22d3ee",
  "secondaryColor": "#3b1d67",
  "tertiaryColor": "#431f2b",
  "fontFamily": "system-ui",
  "lineColor": "#8b5cf6",
  "clusterBkg": "#0b1220",
  "clusterBorder": "#475569"
}}}%%
flowchart LR
    subgraph V1["V1 · Codex seul · 2/2"]
      V1C["✓ Calculatrice Core<br/>6/6"]
      V1S["✓ Calculatrice Scientific<br/>9/9"]
    end
    G1{"Observations V1<br/>référence solo"}
    subgraph V2["V2 · Équipe Codex · 0/2"]
      V2C["▶ Calculatrice Core<br/>prochain"]
      V2S["○ Calculatrice Scientific<br/>à faire"]
    end
    G2{"Observations V2<br/>affinage éventuel"}
    V21["V2.1 · variante optimisée<br/>facultative"]
    subgraph V3["V3 · Codex + Ollama · 0/2"]
      V3C["○ Calculatrice Core<br/>à faire"]
      V3S["○ Calculatrice Scientific<br/>à faire"]
    end
    G3{"Observations V3<br/>comparaison finale"}
    V4["V4 · témoin AutoGen<br/>facultatif"]

    V1C & V1S --> G1
    G1 --> V2C & V2S
    V2C & V2S --> G2
    G2 -. "si gain testable" .-> V21
    G2 --> V3C & V3S
    V3C & V3S --> G3
    G3 -. "contrôle historique" .-> V4

    classDef done fill:#14532d,stroke:#4ade80,color:#f0fdf4,stroke-width:3px;
    classDef next fill:#4c1d95,stroke:#c084fc,color:#faf5ff,stroke-width:3px;
    classDef todo fill:#172554,stroke:#38bdf8,color:#f0f9ff,stroke-width:2px;
    classDef gate fill:#7c2d12,stroke:#fb923c,color:#fff7ed,stroke-width:2px;
    classDef optional fill:#0f2a4a,stroke:#94a3b8,color:#f8fafc;
    class V1C,V1S done;
    class V2C next;
    class V2S,V3C,V3S todo;
    class G1,G2,G3 gate;
    class V21,V4 optional;
```

**Lecture :** les six cases V1–V3 × Calculatrice Core–Calculatrice Scientific
constituent la campagne obligatoire. V2.1 et V4 n'entrent pas dans le calcul
des 2/6 : ce sont des
extensions facultatives, annoncées comme telles.

## La question expérimentale

> Une équipe d'agents produit-elle un meilleur résultat qu'un seul bon agent,
> une fois comptés le temps, les tokens, le bruit de coordination et la
> complexité ajoutée ?

Toutes les variantes d'un même défi reçoivent la même spécification, les mêmes
contraintes, les mêmes tests indépendants et un répertoire vierge. Elles ne
peuvent ni lire ni réutiliser la solution d'une autre tentative. **Les agents
proposent ; le vérificateur tranche.**

La lecture ne se limite donc pas au score :

```math
\text{valeur expérimentale}
=
\frac{\text{qualité obtenue}}
{\text{temps} + \text{tokens} + \text{coordination}}
```

## Résultats publiés

| Run | Organisation | Défi | Verdict | Temps | Tokens observés |
| --- | --- | --- | ---: | ---: | ---: |
| [`codex-single-002`](results/codex-single-002.md) | V1 · référence courante | Calculatrice Core | **6/6** | 193 s | 556 461¹ |
| [`scientific-single-002`](results/scientific-single-002.md) | V1 · référence courante | Calculatrice Scientific | **9/9** | 541 s | 603 492¹ |
| [`codex-single-001`](results/codex-single-001.md) | V1 · historique | Calculatrice Core | **6/6** | non enregistré | ≈ 18 086 |
| [`scientific-single-001`](results/scientific-single-001.md) | V1 · historique | Calculatrice Scientific | **9/9** | 331 s | 332 696¹ |

¹ Entrée + sortie cumulées ; les rapports détaillent cache, raisonnement et
corrections. Aucune donnée manquante n'est reconstruite après coup.

## V1, V2, V3… et pourquoi V2.1 ou V4

- **V1 — référence solo :** l'orchestrateur expérimental mandate une session
  candidate Codex distincte ; celle-ci travaille seule, sans consultant ni
  délégation. Les deux niveaux sont terminés.
- **V2 — société Codex :** orchestrateur et spécialistes aux missions bornées,
  avec un seul écrivain. Elle mesure le bénéfice et le coût de la coordination.
- **V2.1 — optimisation facultative :** seulement après l'analyse complète de
  V2. Elle peut tester une organisation affinée, sans remplacer ni embellir V2.
- **V3 — hybride local :** Codex orchestre, décide et écrit ; des modèles
  Ollama locaux analysent ou critiquent dans un contexte limité.
- **V4 — témoin historique facultatif :** reproduction comparable de
  l'approche multi-agent de Yann Pointud, baptisée AutoGen mais indépendante
  du framework Microsoft du même nom, après la matrice principale.

L'« affinage » peut porter sur la version du modèle, le prompt, les rôles, le
contexte ou les paramètres. Il ne signifie pas nécessairement entraîner les
poids d'un modèle. À chaque jalon, les observations sont consignées avant toute
décision. Si un changement substantiel est retenu, il ouvre une **nouvelle
campagne** et les cellules V1 jusqu'au mode courant sont rejouées avec la même
configuration ; les anciens résultats restent publiés.

Le protocole complet de comparaison et de versionnement est décrit dans
[`governance/EXPERIMENTAL_DESIGN.md`](governance/EXPERIMENTAL_DESIGN.md).

## TODO expérimental

- [x] Figer les défis et vérificateurs **Calculatrice Core** et **Calculatrice Scientific**.
- [x] Conserver les premières observations V1 `001` sans les réécrire.
- [x] Répliquer V1 avec modèle, effort et contexte épinglés : Core `002` **6/6**, Scientific `002` **9/9**.
- [ ] Arbitrer puis figer les rôles, échanges, budgets et [métriques V2](governance/V2_PROTOCOL.md).
- [ ] Exécuter et publier **V2 Calculatrice Core**, puis **V2 Calculatrice Scientific**.
- [ ] Tenir le jalon d'observation V2 ; décider avec des critères écrits si V2.1 apporte une hypothèse testable.
- [ ] Si elle est activée, exécuter V2.1 séparément sur les deux difficultés.
- [ ] Figer l'intégration Ollama, les modèles locaux et les limites de contexte de V3.
- [ ] Exécuter et publier **V3 Calculatrice Core**, puis **V3 Calculatrice Scientific**.
- [ ] Comparer les six runs principaux : qualité, coût, corrections, interventions et bruit social.
- [ ] Décider après la synthèse si le témoin historique V4 mérite d'être exécuté.
- [ ] Lors de tout affinage substantiel, ouvrir une nouvelle campagne et rejouer les références comparables V1…Vn.

## Deux niveaux de difficulté

**Calculatrice Core** est une expérience courte et répétable. **Calculatrice
Scientific** monte d'un cran : analyse sûre d'expressions sans `eval()`,
fonctions et constantes scientifiques, variable `x`, domaines,
échantillonnage et courbes SVG sans dépendance externe.

<details>
<summary><strong>Ce qui est mesuré</strong></summary>

- conformité fonctionnelle et robustesse ;
- lisibilité du code et qualité de la documentation ;
- durée, tokens, appels et corrections ;
- interventions humaines ;
- contradictions, décisions et bruit de coordination ;
- textes inter-agents visibles et influence de chaque métier, consignés dans
  un [PV expérimental](governance/PV_TEMPLATE.md) ;
- capacité des agents à détecter leurs propres erreurs ;
- rapport entre qualité obtenue et complexité organisationnelle.

</details>

<details>
<summary><strong>Reproduire une référence V1</strong></summary>

Prérequis : Linux, Python 3.10 ou supérieur, Git et Codex CLI connecté avec un
abonnement ChatGPT. Aucune clé API OpenAI n'est nécessaire.

```bash
python3 scripts/new_run.py mon-run-v1
cd runs/mon-run-v1
codex "$(cat ../../prompts/codex-single.md)"
cd ../..
python3 scripts/verify.py --solution runs/mon-run-v1/solution
```

Chaque tentative utilise un identifiant inédit et un répertoire neuf. Le défi
scientifique se sélectionne avec l'option `--challenge scientific-calculator`.

</details>

<details>
<summary><strong>Gouvernance, transparence et structure du dépôt</strong></summary>

Le paquet [`governance/`](governance/) définit la hiérarchie des consignes, le
plan expérimental, le format de restitution et la journalisation publique. Le
[journal synthétique](logs/history.md) conserve les décisions sans heure,
secret ni transcription personnelle brute. Les échecs restent publiés autant
que les réussites.

```text
challenges/   spécifications et tests indépendants
prompts/      prompts exacts remis aux candidats
runs/         espaces vierges et solutions produites
results/      résultats détaillés et futures comparaisons
governance/   règles de conduite et de restitution
logs/         historique public synthétique
scripts/      création des runs et vérification
```

La [note SSH pour VS Code et WSL](docs/ssh-vscode.md) explique comment employer
une clé dédiée via `ssh-agent` sans stocker sa phrase secrète dans le dépôt.

</details>

## À propos de l'auteur

[Éric Racineux](https://www.linkedin.com/in/eric-racineux-75475a7/) est
architecte SI et responsable informatique, avec plus de trente ans de terrain
entre développement, industrie, infrastructures, cloud, cybersécurité,
pilotage de projets et conduite du changement.

AgentBench 2026 est son premier véritable POC public réalisé avec Codex en mode
agent IA et une chaîne Git de type CI/CD : spécifications versionnées, runs
isolés, tests indépendants, rapports, historique et publication continue.

[Consulter son profil LinkedIn](https://www.linkedin.com/in/eric-racineux-75475a7/)
· [Parcourir son CV en ligne](https://ericrac.github.io/CV-Eric-RACINEUX/)

## Licence

MIT. Le projet AutoGen de Yann Pointud reste indépendant et appartient à son
auteur ; il n'est ni inclus ni forké dans ce dépôt et ne repose pas sur le
framework Microsoft homonyme.

## Bonus — AgentBench en 3D

Un petit cristal octaédrique représente les six expériences principales autour
d'un même centre de décision. Son aperçu s'adapte automatiquement au thème du
visiteur.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agentbench-crystal-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="assets/agentbench-crystal-light.png">
  <img alt="Cristal octaédrique AgentBench en rendu 3D" src="assets/agentbench-crystal-light.png">
</picture>

<details>
<summary><strong>Manipuler le modèle STL interactif</strong></summary>

Le fond du lecteur interactif est imposé par GitHub et ne suit pas le thème du
README. Le modèle reste [téléchargeable au format STL](assets/agentbench-crystal.stl).

```stl
solid agentbench_crystal
  facet normal 0.577350 0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 10 0 0
      vertex 0 10 0
    endloop
  endfacet
  facet normal -0.577350 0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 0 10 0
      vertex -10 0 0
    endloop
  endfacet
  facet normal -0.577350 -0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex -10 0 0
      vertex 0 -10 0
    endloop
  endfacet
  facet normal 0.577350 -0.577350 0.577350
    outer loop
      vertex 0 0 14
      vertex 0 -10 0
      vertex 10 0 0
    endloop
  endfacet
  facet normal 0.577350 0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 0 10 0
      vertex 10 0 0
    endloop
  endfacet
  facet normal -0.577350 0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex -10 0 0
      vertex 0 10 0
    endloop
  endfacet
  facet normal -0.577350 -0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 0 -10 0
      vertex -10 0 0
    endloop
  endfacet
  facet normal 0.577350 -0.577350 -0.577350
    outer loop
      vertex 0 0 -14
      vertex 10 0 0
      vertex 0 -10 0
    endloop
  endfacet
endsolid agentbench_crystal
```

</details>
