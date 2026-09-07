# PV — sol-core-v1-001

## Acteurs et mandat

Le commanditaire demande une V1 de contrôle strictement comparable à Astra.
L'orchestrateur expérimental préenregistre, lance et vérifie une session Codex
distincte. Le candidat est l'unique écrivain : aucun consultant, sous-agent,
message humain fonctionnel ou modèle externe n'intervient pendant le run.

Modèle : `gpt-5.6-sol`, effort `high`, CLI `0.153.4`, Python `3.13.5`.
Fenêtre client déclarée : 200 000 tokens ; compaction : 180 000, portée
`total`. Le prompt, le défi, les tests, les instructions candidates, le
sandbox et le lanceur sont identiques au contrôle Astra. Seul le modèle change.

Le [prompt exact](../../prompts/codex-single.md), la
[configuration](config.toml), les empreintes et l'identifiant de session sont
conservés. Le préenregistrement a été publié avant lancement dans `a616b2d`.

## Messages visibles du candidat

### Message 1

> Je commence par lire la spécification de la tentative active, puis
> j'inspecterai uniquement les fichiers nécessaires avant d'implémenter dans
> `solution/`. Je travaillerai seul et exécuterai le vérificateur prescrit
> avant de conclure.

### Message 2

> La spécification demande deux livrables (`calculator.py` et `README.md`) et
> une boucle interactive robuste. Je vérifie maintenant l'état du dossier de
> solution ainsi que le contrat réellement contrôlé par le vérificateur, sans
> modifier les tests ni les scripts.

### Message 3

> Le dossier est vide. Le vérificateur contrôle six comportements, dont
> l'absence d'exécution dynamique et la reprise de la CLI après deux erreurs
> successives. J'implémente une API explicite, un parseur à trois éléments, une
> gestion propre de `EOF`/interruption et une documentation d'utilisation.

### Messages 4 à 6 — synthèse fidèle

Le candidat annonce les deux livrables, exécute le vérificateur, constate 6/6,
clarifie les chemins de lancement dans le README et relance la même suite. Sa
restitution finale confirme 6/6, l'absence de sous-agent et d'opération Git.
Les textes complets et l'ordre des événements figurent dans
[trace.json](trace.json).

## Contrôles, corrections et résultat

- Premier passage candidat : 6/6, code 0.
- Dernier passage candidat : 6/6, code 0.
- Relance indépendante après clôture : 6/6, code 0.
- Correction fonctionnelle après le premier passage : aucune.
- Correction documentaire : chemins de lancement explicités.
- Écriture observée : deux fichiers, exclusivement dans `solution/`.
- Durée murale de la session CLI : 189,964 s.
- Entrée : 152 902 ; cache inclus : 122 112 ; sortie : 5 199 ; raisonnement
  inclus : 2 149 tokens.
- Total entrée + sortie : 158 101 tokens, sans double comptage du cache ou du
  raisonnement.

## Analyse et limites

Le contrat Core est satisfait dès le premier passage. Le score officiel est au
plafond pour Sol comme pour Astra : sur ce défi, la comparaison porte donc
surtout sur le coût observé et non sur une différence de conformité.

Il s'agit d'une seule observation stochastique par modèle. Le temps inclut le
lancement et la clôture CLI, mais pas la préparation, le contrôle indépendant
ni la publication. La configuration fixe une fenêtre côté client ; elle ne
prouve pas la capacité réellement consommée côté serveur.
