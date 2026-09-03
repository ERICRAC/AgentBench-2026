# Résultat détaillé — `codex-single-001`

## Résumé exécutif

La tentative de référence a confié tout le cycle de réalisation à un seul
agent Codex : lecture du contrat, conception, implémentation, documentation et
validation. Aucun sous-agent et aucune dépendance externe n'ont été utilisés.
Le premier passage connu du vérificateur a réussi les six contrôles, sans cycle
de correction fonctionnelle consigné.

Ce résultat établit une référence de conformité pour les variantes suivantes.
Il ne suffit pas, à lui seul, à conclure sur l'efficacité : la durée, le niveau
de raisonnement et le détail des itérations n'ont pas été capturés pendant le
run.

## Identité du run

| Donnée | Valeur |
| --- | --- |
| Identifiant | `codex-single-001` |
| Mode | Codex seul |
| Architecture | Un agent généraliste, aucun sous-agent |
| Modèle observé | `gpt-5.6-sol` |
| Authentification | ChatGPT Plus, sans clé API OpenAI |
| Prompt | [`prompts/codex-single.md`](../prompts/codex-single.md) |
| Création | 2 septembre 2026 — heure non publiée |
| Vérification enregistrée | 2 septembre 2026 — heure non publiée |
| Consommation observée | Environ 18 086 tokens |
| Durée totale | Non enregistrée |
| Niveau de raisonnement | Non enregistré |
| Environnement | Codex CLI 0.152.1, Python 3.13.5, WSL2 x86_64 |

## Gouvernance appliquée

Le run a été encadré par quatre documents séparant les responsabilités :

1. [`AGENTS.md`](../AGENTS.md) imposait un agent unique, interdisait la
   délégation et limitait les écritures à la solution active.
2. [`CHALLENGE.md`](../runs/codex-single-001/CHALLENGE.md) fixait le contrat
   fonctionnel et la commande de vérification.
3. [`prompts/codex-single.md`](../prompts/codex-single.md) rappelait le rôle de
   l'agent et l'interdiction de modifier la spécification ou les tests.
4. Le vérificateur indépendant décidait du résultat ; la déclaration de
   l'agent ne constituait pas une preuve.

L'agent unique cumulait les rôles d'analyste, de concepteur, de développeur,
de rédacteur et de vérificateur. Cette absence de coordination constitue à la
fois la simplicité de la référence V1 et le point de comparaison avec la V2.

## Traitement réalisé

### 1. Traduction du contrat en composants

Le livrable a été séparé en trois responsabilités simples :

- `calculate(left, operator, right)` porte le contrat Python public ;
- `parse_expression(expression)` transforme une ligne en deux nombres et un
  opérateur autorisé ;
- `main()` gère la boucle interactive, les sorties et la récupération après
  erreur.

Cette séparation permet aux tests d'appeler directement la logique métier
sans passer par la CLI, tout en conservant une interface interactive réduite.

### 2. Implémentation de la logique métier

Les quatre opérateurs sont traités par des branches explicites. Ce choix évite
toute exécution dynamique et rend visible le comportement de chaque opération.
La division vérifie explicitement un diviseur nul et lève
`ZeroDivisionError`. Un opérateur non reconnu lève `ValueError`, conformément
au contrat.

### 3. Analyse des entrées

La CLI attend trois éléments séparés par des espaces : opérande gauche,
opérateur et opérande droite. Les opérandes sont convertis avec `float`, ce qui
couvre les entiers, décimaux et valeurs négatives demandés. Les erreurs de
forme, de nombre et d'opérateur sont converties en messages compréhensibles.

### 4. Boucle interactive et robustesse

La boucle accepte `quit` et `exit` sans distinction de casse. Elle traite les
lignes vides, les expressions invalides et la division par zéro sans afficher
de traceback, puis attend la saisie suivante. La fin de flux et
`KeyboardInterrupt` terminent également proprement le programme.

### 5. Documentation utilisateur

Le README de la solution documente le lancement, la syntaxe attendue, des
exemples couvrant plusieurs opérations, la poursuite après erreur et
l'utilisation de `calculate` comme fonction importable.

## Validation indépendante

Commande exécutée depuis la racine :

```bash
python3 scripts/verify.py --solution runs/codex-single-001/solution
```

| Contrôle | Ce qu'il vérifie | Résultat |
| --- | --- | --- |
| Fichiers requis | Présence de `calculator.py` et `README.md` | Réussi |
| Opérations et nombres | `+`, `-`, `*`, `/`, négatifs et décimaux | Réussi |
| Opérateur invalide | Levée de `ValueError` | Réussi |
| Division par zéro | Levée de `ZeroDivisionError` | Réussi |
| Sécurité statique | Aucun appel à `eval()` ou `exec()` dans l'AST | Réussi |
| Session CLI | Erreurs sans traceback, reprise, résultats et sortie propre | Réussi |

Résultat du premier passage connu : **6/6**. Résultat final revérifié lors de
la publication : **6/6**.

## Indicateurs observables

| Indicateur | Valeur |
| --- | --- |
| Agents | 1 |
| Sous-agents | 0 |
| Fichiers livrés | 2 |
| Taille de `calculator.py` | 79 lignes |
| Taille du README de solution | 42 lignes |
| Dépendances d'exécution externes | 0 |
| Tests réussis | 6/6 |
| Corrections après le premier passage connu | 0 |
| Tokens | Environ 18 086 |

## Interventions et incidents

Aucune intervention humaine pendant l'implémentation n'est consignée. Les
actions humaines et techniques réalisées après le run — enregistrement des
métadonnées, configuration Git/SSH et publication — relèvent de la
conservation de l'expérience et non de la production de la solution. Elles ne
sont donc pas comptées comme aide fonctionnelle au candidat.

Aucun défaut fonctionnel n'est attesté par le premier passage connu. En
revanche, l'absence de journal brut empêche de vérifier indépendamment le
nombre exact d'appels, de décisions intermédiaires ou d'éventuelles erreurs
survenues avant ce passage.

## Évaluation qualitative

- **Conformité fonctionnelle :** complète sur le contrat testé.
- **Lisibilité :** responsabilités séparées, branches explicites et messages
  d'erreur localisés.
- **Robustesse :** récupération correcte sur les erreurs couvertes et absence
  de traceback dans la session testée.
- **Documentation :** suffisante pour lancer la CLI et importer la fonction.
- **Complexité ajoutée :** faible ; aucune abstraction ou dépendance non
  nécessaire.
- **Bruit de coordination :** nul par construction, puisqu'il n'y a qu'un
  agent.

## Limites de l'expérience

- La suite contient six contrôles ciblés ; elle ne mesure pas tous les cas
  possibles d'une calculatrice.
- La grammaire CLI exige des espaces autour de l'opérateur, conformément à la
  forme documentée, mais ne reconnaît pas `2+3`.
- La durée totale, le niveau de raisonnement et le nombre précis d'itérations
  n'ont pas été capturés et ne doivent pas être reconstruits a posteriori.
- La consommation de tokens est approximative.
- Aucun transcript brut horodaté ne permet une analyse fine du cheminement de
  l'agent.
- Un score de 6/6 établit la conformité aux tests, pas une supériorité générale
  du mode mono-agent.

## Conclusion pour la comparaison

La V1 fournit une solution courte, documentée et entièrement conforme aux
contrôles, sans coût de coordination. La V2 devra donc apporter un bénéfice
observable autre que le même score final — meilleure détection de limites,
qualité accrue ou robustesse supplémentaire — pour justifier son temps, ses
tokens et ses échanges additionnels.
