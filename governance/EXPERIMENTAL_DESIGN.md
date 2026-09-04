# Plan expérimental et comparabilité

**Français** · [English (UK)](EXPERIMENTAL_DESIGN.en.md) · [Español](EXPERIMENTAL_DESIGN.es.md) · [Português](EXPERIMENTAL_DESIGN.pt.md)

Ce document fixe la structure de la campagne AgentBench 2026. Il sépare les
comparaisons obligatoires des variantes exploratoires et empêche qu'un affinage
ultérieur réécrive les conditions d'un résultat déjà publié.

## Matrice principale

La campagne principale contient six cellules : trois modes d'organisation
croisés avec deux niveaux de difficulté.

| Mode | Objectif Calculatrice Core | Objectif Calculatrice Scientific |
| --- | --- | --- |
| V1 · Codex seul | obligatoire | obligatoire |
| V2 · Codex multi-agent gouverné | obligatoire | obligatoire |
| V3 · Codex + Ollama | obligatoire | obligatoire |

Une cellule correspond à une tentative isolée, un prompt identifié, une
configuration enregistrée et le verdict du vérificateur indépendant. V1, V2 et
V3 désignent des **modes d'organisation**, pas des versions successives du
même logiciel.

## Jalon d'observation

Après chaque mode, un jalon sépare l'observation de l'optimisation :

- publier d'abord les deux résultats du mode sans les retoucher ;
- consolider score, durée, tokens, corrections, interventions et événements de
  coordination effectivement observés ;
- formuler les constats et limites avant de proposer un changement ;
- associer tout affinage à une hypothèse mesurable et à un critère de décision.

L'affinage peut concerner la version du modèle, le prompt, la répartition des
rôles, le contexte ou les paramètres. Le terme ne suppose pas un entraînement
des poids du modèle.

## Campagnes et relances

Une campagne est définie par les versions des défis et vérificateurs, les
modèles, les paramètres structurants et les prompts de mode. Une modification
substantielle de l'un de ces éléments ouvre une nouvelle campagne identifiée.

Dans une nouvelle campagne, les cellules nécessaires à la comparaison sont
rejouées de V1 jusqu'au mode étudié. Les résultats antérieurs restent publiés
et ne sont ni remplacés ni agrégés silencieusement avec les nouveaux. Une
correction du vérificateur crée de même une nouvelle version du défi dès lors
qu'un premier candidat a été évalué.

Une correction locale du code candidat au cours d'un run n'ouvre pas une
campagne : elle fait partie du run et doit être tracée.

## Variantes facultatives

**V2.1** est une variante exploratoire possible après la publication et
l'analyse de V2. Elle sert à tester une hypothèse d'organisation affinée sur
les deux difficultés. Elle ne remplace pas V2 et ne compte pas parmi les six
cellules principales.

**V4** est réservé à un témoin historique AutoGen comparable, exécuté si la
synthèse V1–V3 montre qu'il apporte une information utile. Il reste extérieur
à la matrice principale. Une autre architecture future recevra un autre nom
afin de ne pas surcharger ce rôle de contrôle.

## Comparaison finale

Le verdict fonctionnel reste celui des vérificateurs. La synthèse rapproche au
minimum : conformité, durée, tokens, corrections, interventions humaines,
contradictions, décisions et coût de coordination. Une amélioration n'est
attribuée au mode d'organisation que si les conditions comparées appartiennent
à la même campagne ou si leur différence est explicitement qualifiée.
