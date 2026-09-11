# Gouvernance publique

**Français** · [English (UK)](README.en.md) · [Español](README.es.md) · [Português](README.pt.md)

**V2.2 : 57 tests de maintenance réussis ; trois sondes de CLI restent à 7/8.** Le paquet officiel séparé reproduit le blocage du catalogue. Aucun modèle lancé ; installations existantes inchangées. **Astra élevé : historique uniquement.** [CLI](../results/v2-2-cli-qualification.md)

Ce dossier expose juste assez de méthode pour rendre l'expérience lisible et
reproductible sans publier les conversations brutes ni la configuration privée
de son auteur.

- [`RESPONSE_FORMAT.md`](RESPONSE_FORMAT.md) définit la forme des restitutions.
- [`LOGGING.md`](LOGGING.md) définit ce qui entre dans le journal public.
- [`EXPERIMENTAL_DESIGN.md`](EXPERIMENTAL_DESIGN.md) fixe la matrice, les
  jalons d'observation et les règles de relance après affinage.
- [`V2_PROTOCOL.md`](V2_PROTOCOL.md) préenregistre l'organisation, les limites
  de contexte et les mesures de la campagne multi-agent.
- [`PV_TEMPLATE.md`](PV_TEMPLATE.md) fixe le relevé des textes inter-agents,
  des arbitrages, de la relation sociale et de l'efficacité.
- [`../logs/history.md`](../logs/history.md) conserve l'historique synthétique.

La hiérarchie de décision est : règles globales du dépôt, cahier des charges de
la tentative, prompt du mode, arbitrage de l'orchestrateur, puis verdict du
vérificateur. Une consigne locale ne peut pas assouplir la sécurité, modifier
les tests ou autoriser la lecture d'une autre solution.

Cette gouvernance évolue avec l'expérience. Une clarification ou une erreur
peut devenir une règle générale lorsqu'elle est utile, contrôlable et
applicable aux runs suivants. Elle n'est jamais utilisée pour réécrire a
posteriori les conditions d'un run déjà terminé.

Avant son gel, un nouvel arbitre doit être calibré contre plusieurs formes
d'implémentation conformes, notamment les constructions usuelles de la
bibliothèque standard. Un biais découvert après le premier candidat est
documenté ; il n'est pas effacé silencieusement du protocole publié.

Les documents éditoriaux publics sont proposés en français, anglais
britannique, espagnol et portugais. Les instructions agent, prompts, défis
figés, traces et livrables de runs restent dans leur langue canonique : ils
constituent le protocole ou la preuve historique et ne sont pas réécrits.

La règle Git globale concerne l'orchestrateur hors run. Un candidat n'écrit
que dans `solution/` et ne prépare ni commit ni push ; cette précision évite
qu'une règle de publication déborde sur la mesure expérimentale.
