# PV — sol-scientific-v1-001

## Acteurs et mandat

Le commanditaire demande une V1 de contrôle strictement comparable à Astra.
L'orchestrateur expérimental préenregistre, lance et vérifie une session Codex
distincte. Le candidat est l'unique écrivain : aucun consultant, sous-agent,
message humain fonctionnel ou modèle externe n'intervient pendant le run.

Modèle : `gpt-5.6-sol`, effort `high`, CLI `0.153.4`, Python `3.13.5`.
Fenêtre client déclarée : 200 000 tokens ; compaction : 180 000, portée
`total`. Le prompt, le défi, les tests, les instructions candidates, le
sandbox et le lanceur sont identiques au contrôle Astra. Seul le modèle change.

Le [prompt exact](../../prompts/scientific-single.md), la
[configuration](config.toml), les empreintes et l'identifiant de session sont
conservés. Le préenregistrement a été publié avant lancement dans `a616b2d`.

## Messages visibles du candidat

### Message 1

> Je commence par lire la spécification de la tentative active, puis
> j'inspecterai uniquement le contenu autorisé de `solution/`. J'implémenterai
> avec la bibliothèque standard et validerai avec le vérificateur exact indiqué.

### Message 2

> La solution est vide. Je mets en place un analyseur syntaxique dédié, avec la
> grammaire de puissance demandée, puis un échantillonneur tolérant aux
> singularités et un SVG passif dont les textes sont échappés.

### Message 3

> Le cœur est implémenté. Je vérifie maintenant les cas de priorité délicats,
> les erreurs de sécurité et de domaine, les coupures de courbe, ainsi que la
> validité XML et l'innocuité du SVG avant de lancer l'arbitre officiel.

### Message 4

> Les contrôles ciblés passent, y compris la reprise de la CLI après une
> division par zéro et l'historique des seules commandes réussies. Je lance à
> présent le vérificateur scientifique depuis le répertoire de la tentative
> active, sans ouvrir ni modifier ses tests.

### Message 5

> Le premier passage révèle un défaut unique et confirmé : le chargeur
> indépendant importe le module sans l'enregistrer dans `sys.modules`, ce qui
> fait échouer le décorateur `dataclass` sous Python 3.13 avant tout test
> fonctionnel. Je remplace ce simple conteneur interne par une classe à
> emplacements, sans changer le moteur ni contourner les assertions.

### Messages 6 et 7 — synthèse fidèle

Le candidat annonce la correction et le 9/9 final, inventorie ses deux
livrables, puis restitue l'analyseur, l'échantillonnage, le SVG, la CLI et les
limites numériques. Il confirme l'absence de sous-agent et d'opération Git.
Les textes complets et l'ordre des événements figurent dans
[trace.json](trace.json).

## Contrôles, corrections et résultat

- Contrôles ciblés candidat avant arbitre : réussis.
- Premier passage officiel candidat : 3/9, avec six erreurs d'import.
- Correction : remplacement du `dataclass` interne par une classe à
  `__slots__` compatible avec le chargeur Python 3.13 de la suite figée.
- Dernier passage candidat : 9/9, code 0.
- Relance indépendante après clôture : 9/9, code 0.
- Écriture observée : deux fichiers, exclusivement dans `solution/`.
- Durée murale de la session CLI : 1 009,468 s.
- Entrée : 280 773 ; cache inclus : 245 888 ; sortie : 15 502 ; raisonnement
  inclus : 5 408 tokens.
- Total entrée + sortie : 296 275 tokens, sans double comptage du cache ou du
  raisonnement.

## Contrôle exploratoire commun après clôture

L'orchestrateur a ensuite rejoué, sans corriger les solutions, les quatre
méthodes supplémentaires conservées par le candidat Astra. Empreinte du fichier
exécuté : `66680c1a…641a`.

- Astra : 4/4 méthodes réussies.
- Sol : 0/4 méthodes réussies, six assertions en échec.
- Écarts observés : interpolation sur des flottants extrêmes, limites de
  complexité, rejet d'une expression entièrement inconnue lors de
  l'échantillonnage, et hypothèse de structure SVG.

Ce résultat est **exploratoire, pas un verdict officiel** : cette suite a été
écrite après le run Astra et n'avait pas été préenregistrée pour Sol. De plus,
l'assertion exigeant les axes SVG directement sous la racine impose une
structure plus précise que le contrat, qui autorise leur présence dans un
groupe. Elle ne doit donc pas être assimilée à un défaut de conformité.

## Analyse et limites

Sol atteint finalement le même plafond officiel qu'Astra, mais après une
correction confirmée. Son contrôle préalable n'a pas anticipé le mode de
chargement de l'arbitre. Les échecs postérieurs suggèrent aussi une robustesse
hors suite plus faible, sans permettre un classement causal puisque le contrôle
complémentaire est postérieur et partiellement couplé à l'implémentation Astra.

Il s'agit d'une seule observation stochastique par modèle. Le temps inclut le
lancement et la clôture CLI, mais pas la préparation, le contrôle indépendant
ni la publication. Aucun essai multi-version Python ou contrôle visuel
navigateur n'est revendiqué.
