# V1 Astra — rapport complet

**Français** · [English (UK)](astra-v1.en.md) · [Español](astra-v1.es.md) · [Português](astra-v1.pt.md)

Campagne `astra-high-001` : les deux candidats solo sont terminés et vérifiés séparément. Les anciennes V1 sont [archivées](ARCHIVE_V1.md) et ne sont pas additionnées à cette campagne.

| Indicateur | Core · astra-core-v1-002 | Scientific · astra-scientific-v1-002 |
| --- | ---: | ---: |
| Premier / dernier / indépendant | 6/6 · 6/6 · 6/6 | 9/9 · 9/9 · 9/9 |
| Durée session | 100.175 s | 399.478 s |
| Entrée | 117769 | 208078 |
| Cache inclus | 96896 | 167808 |
| Sortie | 2709 | 12432 |
| Raisonnement inclus | 195 | 1429 |
| Total entrée + sortie | 120478 | 220510 |
| Contrôles supplémentaires | — | 4/4 |

## Traitement et parcours

Core sépare les quatre opérations de la CLI, conserve les exceptions métier et récupère après les erreurs de saisie. Le premier passage officiel réussit sans correction fonctionnelle. Une erreur de chemin lors de la navigation initiale est consignée dans le PV.

Scientific utilise un analyseur dédié et une représentation arithmétique postfixée, avec limites de taille et de profondeur. L'expression est analysée une seule fois pour l'échantillonnage. Les points indéfinis coupent la courbe ; le SVG est sérialisé en XML et la CLI gère l'historique. Après un premier 9/9 officiel, les tests complémentaires du candidat révèlent un arrondi hors intervalle près du plus grand flottant. Le candidat corrige l'interpolation selon le signe des bornes et conserve quatre tests de régression, tous réussis. L'orchestrateur relance la suite figée et ces tests après clôture.

## Protocole, preuves et limites

Même modèle `gpt-6-astra`, effort `high`, CLI `0.153.4`, Python `3.13.5`, fenêtre déclarée 200 000 et compaction 180 000 (`total`). Sessions éphémères neuves, aucun consultant, aucune aide humaine fonctionnelle et aucune opération Git du candidat observée. Les configurations utilisateur sont ignorées ; l'authentification reste extérieure au dépôt.

Les compteurs proviennent des événements JSON finaux. Le cache est inclus dans l'entrée et le raisonnement dans la sortie : aucun double comptage. Les 340 988 tokens et 499,653 s sont la somme des deux sessions terminées, pas le coût total de la campagne. Le temps comprend le lancement et la clôture CLI, mais exclut la préparation, la publication et le préflight.

Les PV distinguent suite officielle exécutée par le candidat et vérification séparée par l'orchestrateur. Certaines sorties d'outils Scientific sont vides dans l'export JSON : le premier 9/9 repose sur la déclaration visible et le code 0 ; le verdict final a été relancé séparément. La configuration du client n'est pas une mesure de la fenêtre serveur. Aucun essai multi-version Python ni contrôle visuel navigateur n'est revendiqué.

[Core PV](../runs/astra-core-v1-002/PV.md) · [Core JSON](../runs/astra-core-v1-002/run.json)

[Scientific PV](../runs/astra-scientific-v1-002/PV.md) · [Scientific JSON](../runs/astra-scientific-v1-002/run.json)

## Incidents conservés

`astra-core-v1-001` : refus serveur du CLI 0.152.1 avant travail candidat, 5,301 s, compteurs absents. Mise à jour en 0.153.4 puis nouvelle tentative.

`astra-scientific-v1-001` : interruption par quota après la première écriture, avant vérification, 216,929 s, tokens non enregistrés. Code conservé, jamais réutilisé par le nouveau candidat. Ces essais restent visibles et hors références terminées ; leur coût token manquant empêche de donner le coût complet de campagne.

[Core incident](../runs/astra-core-v1-001/run.json) · [Scientific incident](../runs/astra-scientific-v1-001/PV.md)

## Observations et suite

Les comparaisons historiques avec les anciens runs Sol restent archivées mais
ne servent plus de contrôle modèle. Une [V1 Sol à périmètre client constant](sol-vs-astra-v1.md)
mesure désormais les deux défis avec le même CLI, les mêmes prompts et les
mêmes paramètres : verdict final égal, mais +140,1 % de temps et +33,3 % de
tokens pour Sol sur les deux sessions observées.

Le défaut trouvé après 9/9 confirme l'effet plafond des suites courtes. Le biais
du chargeur `dataclass` reste documenté ; la suite figée n'a pas été retouchée.
Le préflight V2 est terminé et le prochain benchmark prêt est V2 Core Astra.
