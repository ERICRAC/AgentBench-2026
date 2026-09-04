# Résultat détaillé — `scientific-single-001`

**Français** · [English (UK)](scientific-single-001.en.md) · [Español](scientific-single-001.es.md) · [Português](scientific-single-001.pt.md)

## Résumé exécutif

La première tentative solo de la Calculatrice Scientific est terminée avec un
résultat final de **9 tests sur 9**. Un seul agent Codex a produit un parseur
d'expressions sécurisé, les fonctions scientifiques, l'échantillonnage de
courbes, un export SVG autonome et une CLI documentée, sans dépendance externe.

Le résultat final est complet, mais le chemin est instructif : le premier
passage officiel n'a validé que 3/9 groupes, une première correction a supprimé
une incompatibilité avec le chargeur du test, puis une seconde a corrigé la
reconnaissance de `log10`. Le candidat a convergé sans aide fonctionnelle
humaine.

![Courbe sin(x) produite par la solution](assets/scientific-single-001-sine.svg)

Cette courbe SVG est un artefact de démonstration généré après le run avec la
solution publiée. Elle ne compte pas comme modification du candidat.

## Identité du run

| Donnée | Valeur |
| --- | --- |
| Identifiant | `scientific-single-001` |
| Objectif | Calculatrice Scientific |
| Mode | Codex seul |
| Architecture | Un agent généraliste, aucun sous-agent |
| Modèle | `gpt-5.6-sol` |
| Niveau de raisonnement | Non exposé |
| Prompt | [`prompts/scientific-single.md`](../prompts/scientific-single.md) |
| Durée mesurée | 5 min 31 s |
| Intervention humaine fonctionnelle | Aucune |
| Premier passage officiel | 3 réussites, 6 erreurs |
| Résultat final | 9/9 |
| Corrections de code | 2 |

## Protocole

La spécification, le prompt et les tests ont été figés et poussés dans le
commit `71ae527` avant la création du run. Le candidat a travaillé dans un
dossier vierge et n'a consulté aucune autre solution. Ses écritures ont été
limitées aux deux livrables de `solution/`.

L'orchestrateur n'a fourni aucune indication fonctionnelle entre le lancement
et la réponse finale. Une autorisation système a été nécessaire avant le vrai
run afin que Codex CLI puisse accéder à sa base d'état locale. Le lancement
avorté n'a atteint ni le modèle ni la solution et n'est pas inclus dans la
durée.

## Traitement réalisé

### Moteur d'expressions

La solution utilise un tokenizer à liste blanche et un parseur récursif. Elle
gère la notation scientifique, les parenthèses, les signes unaires, les cinq
opérateurs demandés et l'associativité à droite de la puissance. Aucune chaîne
n'est remise à l'interpréteur Python.

### Fonctions et domaines

Les douze fonctions prévues et les constantes `pi` et `e` sont reliées
explicitement à `math`. Seule la variable `x` est acceptée. Les résultats
complexes, non finis ou hors du domaine réel deviennent des `ValueError`,
tandis que la division par zéro conserve `ZeroDivisionError`.

### Courbes et SVG

`sample_curve` échantillonne uniformément un intervalle inclusif et transforme
les points non définis en séparations. `write_svg` normalise l'échelle, trace
les axes, produit une polyline par segment continu et échappe le titre. Le SVG
ne contient ni script, ni lien, ni ressource externe.

### Interface utilisateur

La CLI évalue les expressions, produit un fichier avec `plot`, mémorise les
opérations réussies, affiche et efface l'historique, fournit une aide et
continue après une erreur sans traceback.

## Parcours de validation

| Passe | Résultat observable | Diagnostic | Action du candidat |
| --- | --- | --- | --- |
| Contrôles ciblés | Réussis selon la trace | Cas sensibles testés avant l'arbitre | Aucune |
| Vérificateur officiel 1 | 3/9, 6 erreurs | Interaction `dataclass` / chargeur dynamique | Remplacement de la dataclass interne |
| Passe intermédiaire | Code 1, sortie non capturée | Candidat : `log10` découpé incorrectement | Extension lexicale des identifiants |
| Vérificateur officiel final | 9/9 | Aucun défaut restant dans le contrat | Clôture |
| Vérification indépendante | 9/9 | Résultat reproduit par l'orchestrateur | Aucune modification |

Le score intermédiaire 8/9 mentionné par le candidat n'est pas présenté comme
une mesure certaine : la commande a bien échoué, mais sa sortie n'a pas été
capturée. La [trace synthétique](../runs/scientific-single-001/trace.md) conserve
cette nuance.

## Détail des contrôles finaux

| Contrôle | Résultat |
| --- | --- |
| Livrables et documentation | Réussi |
| Bibliothèque standard et absence d'exécution dynamique | Réussi |
| Priorités, parenthèses, puissances et signes | Réussi |
| Constantes, fonctions et notation scientifique | Réussi |
| Variable `x` et noms hostiles ou inconnus | Réussi |
| Syntaxe, domaines et division par zéro | Réussi |
| Échantillonnage et discontinuités | Réussi |
| SVG valide, inerte, avec axes et courbe | Réussi |
| CLI, tracé, historique et reprise après erreur | Réussi |

Commande indépendante :

```bash
python3 scripts/verify.py \
  --challenge scientific-calculator \
  --solution runs/scientific-single-001/solution
```

## Mesures

| Indicateur | Valeur |
| --- | --- |
| Durée du vrai run | 331 secondes |
| Entrée rapportée | 324 237 tokens |
| Entrée servie depuis le cache | 303 360 tokens |
| Entrée non mise en cache | 20 877 tokens |
| Sortie | 8 459 tokens |
| Raisonnement rapporté | 941 tokens |
| Commandes exécutées | 8 |
| Lots de modifications | 3 |
| Messages agent | 9 |
| Fichiers livrés | 2 |
| Taille du code | 352 lignes |
| Taille de la documentation | 64 lignes |
| Fonctions Python | 16 |
| Classes | 2 |
| Dépendances externes | 0 |

Les compteurs d'entrée incluent une part très importante de cache. Ils ne
doivent donc pas être comparés à la seule estimation globale de la première V1
Core sans harmoniser la méthode de comptage.

## Incidents et gouvernance

- Un lancement préalable a échoué avant le modèle à cause d'une base d'état
  Codex en lecture seule. Il a été relancé avec une autorisation système.
- La lecture du format de restitution global depuis le run a échoué car le
  fichier n'était pas copié localement. Le candidat a poursuivi sans aide.
- Le premier échec officiel expose un biais du chargeur de tests envers
  `dataclass`. Les tests n'ont pas été corrigés après le run afin de préserver
  l'intégrité du protocole figé.
- Le candidat ne pouvait pas écrire dans l'index Git parent. La livraison Git
  est donc réalisée après le run par l'orchestrateur et n'affecte pas le score.

## Évaluation qualitative

- **Conformité :** complète sur les neuf groupes d'acceptation.
- **Sécurité :** grammaire explicite, liste blanche et aucune exécution
  dynamique.
- **Robustesse :** erreurs numériques normalisées, discontinuités isolées et
  CLI récupérable.
- **Lisibilité :** structure claire, mais 352 lignes représentent un saut de
  complexité réel par rapport à la Calculatrice Core.
- **Documentation :** API, syntaxe, sécurité et limites sont explicitées.
- **Autocorrection :** deux corrections ciblées ont permis de converger vers
  9/9 sans orientation humaine.
- **Bruit de coordination :** nul par construction dans ce mode solo.

## Limites

- Le tracé repose sur un échantillonnage uniforme et peut manquer une
  discontinuité située entre deux points.
- Le test SVG vérifie sa structure et son innocuité, pas sa qualité visuelle
  sur plusieurs moteurs de rendu.
- Le niveau de raisonnement du modèle n'a pas été exposé.
- La passe intermédiaire ne possède pas de sortie brute exploitable.
- Le chargeur dynamique des tests a rejeté une construction `dataclass` valide
  en usage Python normal ; cela réduit la pureté fonctionnelle du premier score.
- Ce résultat est une référence solo du défi scientifique, pas encore une
  preuve sur l'intérêt d'une organisation multi-agent.

## Conclusion

La V1 scientifique atteint le contrat complet en un peu plus de cinq minutes et
deux corrections autonomes. Elle fixe une référence plus exigeante que
la Calculatrice Core : la future équipe multi-agent devra faire mieux qu'un simple
9/9, par exemple réussir plus tôt, détecter le biais du vérificateur, réduire
les corrections ou améliorer le rapport qualité/complexité.
