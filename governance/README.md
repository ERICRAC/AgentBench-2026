# Gouvernance publique

Ce dossier expose juste assez de méthode pour rendre l'expérience lisible et
reproductible sans publier les conversations brutes ni la configuration privée
de son auteur.

- [`RESPONSE_FORMAT.md`](RESPONSE_FORMAT.md) définit la forme des restitutions.
- [`LOGGING.md`](LOGGING.md) définit ce qui entre dans le journal public.
- [`../logs/history.md`](../logs/history.md) conserve l'historique synthétique.

La hiérarchie de décision est : règles globales du dépôt, cahier des charges de
la tentative, prompt du mode, arbitrage de l'orchestrateur, puis verdict du
vérificateur. Une consigne locale ne peut pas assouplir la sécurité, modifier
les tests ou autoriser la lecture d'une autre solution.

Cette gouvernance évolue avec l'expérience. Une clarification ou une erreur
peut devenir une règle générale lorsqu'elle est utile, contrôlable et
applicable aux runs suivants. Elle n'est jamais utilisée pour réécrire a
posteriori les conditions d'un run déjà terminé.
