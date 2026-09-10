# Préflight V1 Astra moyen — préparé, non lancé

**Français** · [English (UK)](astra-medium-v1-preflight.en.md) · [Español](astra-medium-v1-preflight.es.md) · [Português](astra-medium-v1-preflight.pt.md)

Document historique : les deux V1 sont désormais terminées. Le contrôle 44/44 ci-dessous décrit la préparation et doit refuser ces dossiers déjà exécutés. Le reste du document conserve les autorisations et constats de cette étape. [Bilan complet et preuves](astra-medium-v1-v2.md)

Deux tentatives solo vierges sont préparées. **44/44 contrôles statiques réussis ; aucun candidat, aucun appel modèle de test, aucun score produit.** Autorisation reçue : préparer seulement. Le choix de modèle dans cette conversation ne remplace pas les configurations explicites des futurs candidats.

## Tentatives réservées

- Calculatrice simple : [astra-medium-core-v1-001](../runs/astra-medium-core-v1-001/run.json) · [configuration](../runs/astra-medium-core-v1-001/config.toml) · [challenge](../runs/astra-medium-core-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-core-v2-001/run.json)
- Calculatrice scientifique : [astra-medium-scientific-v1-001](../runs/astra-medium-scientific-v1-001/run.json) · [configuration](../runs/astra-medium-scientific-v1-001/config.toml) · [challenge](../runs/astra-medium-scientific-v1-001/CHALLENGE.md) · [V2](../runs/astra-medium-scientific-v2-001/run.json)

Chaque dossier contient CHALLENGE.md, config.toml et run.json. Les deux solution/ existent localement et sont vides : aucun .gitkeep, aucune ancienne solution consultée ou copiée. Git ne conserve pas les dossiers vides ; après un nouveau clone, les recréer avec les commandes ci-dessous avant le contrôle.

## Comparabilité et choix de mesure

Campagne associée : astra-medium-001, **extension V1 préparée après les V2 terminées**, sans modifier leurs métadonnées. Candidat solo neuf, aucune délégation ; orchestrateur de préparation/publication hors mesure. Publier Core avant Scientific, sans affinage entre les deux.

| Élément | Choix et preuve |
| --- | --- |
| Modèle / effort | gpt-6-astra / medium dans chaque config.toml ; égalité avec les quatre métiers V2 vérifiée. |
| Contexte / compaction | 200 000 / 180 000, portée total, comme V2. Ce n’est pas un plafond de consommation cumulée. |
| Configuration V1 | Copie de governance/astra-v1.toml ; seule différence : high → medium. Gouvernance inchangée. |
| Permissions | workspace-write pour V1 et MAIN V2 ; read-only pour les consultants. Web désactivé, approbation never, instructions de non-délégation. Les instructions bornent l’écriture à solution/ ; ce contrôle statique ne prouve pas l’isolation réelle. |
| Prompts | codex-single.md et scientific-single.md historiques, empreintes figées. Pas d’ajout de conseils issus des V2. |
| Défis / arbitres | Empreintes identiques à V2 ; simple : 6 groupes/14 contrôles ; scientifique : 9 groupes/57 contrôles. [Liste explicite](../docs/acceptance-tests.md). |
| Capture | scripts/capture_session.py historique inchangé. Pas de wrapper observé nouveau. Durée autour de CLI ; V2 mesure aussi le relais, différence organisationnelle documentée. |
| Environnement observé | Codex CLI 0.153.4, Python 3.13.5, Node 20.19.2, npm 9.2.0. CLI identique aux références V2 ; autres détails historiques non certifiés ici. |
| Résultats attendus | Premier/final/indépendant, corrections avant/après premier passage, durée, entrée/cache/sortie/raisonnement, interventions et textes visibles. Valeurs actuellement null, pas zéro. |

La V2 comporte sept sessions pour quatre métiers ; la V1 en prévoit une. Le premier passage V2 suit obligatoirement la critique, contrairement à V1. Ce sont des différences du traitement expérimental, pas des paramètres à égaliser rétroactivement.

## Checklist du préflight

Le [contrôle reproductible](../scripts/preflight_v1_medium.py) effectue **22 assertions par dossier, soit 44** :

- [x] Configuration V1 identique sauf effort ; identité/mode ; statut préparé et lancement non autorisé.
- [x] Aucun résultat inventé ; solution existante, vide et déclarée accessible en écriture.
- [x] Six empreintes : configuration, prompt, challenge, tests, capture et vérificateur.
- [x] Challenge identique à SPEC ; référence V2 terminée dans la campagne associée.
- [x] Empreintes challenge/tests communes avec V2 ; paramètres et permissions des quatre métiers vérifiés.
- [x] Nombre de méthodes d’acceptation contrôlé par lecture syntaxique (6 ou 9), sans les exécuter ; version CLI enregistrée identique.

codex --version et codex exec --help ont réussi et exposent les options du lanceur. Avertissement local : création d’alias PATH impossible en lecture seule ; les deux commandes restent fonctionnelles. Le TOML a été analysé, **pas validé par un lancement Codex avec ces configurations**.

```bash
mkdir -p runs/astra-medium-core-v1-001/solution runs/astra-medium-scientific-v1-001/solution
python3 -B scripts/preflight_v1_medium.py
```

## Exécution future — pas autorisée ici

Uniquement après une nouvelle autorisation : contrôler à nouveau environnement, empreintes, quota et dossiers ; lancer Core dans une session neuve avec sa configuration dédiée et le prompt historique. Contrôler et publier son résultat avant Scientific. Toute interruption reste conservée ; une reprise depuis zéro reçoit un nouvel identifiant.

Capture privée hors dépôt ; publier ensuite un PV filtré avec rôle candidat, mandat exact, messages visibles, commandes, contrôles et arbitrages. Aucun raisonnement interne, secret ou horaire de travail dans les Markdown. Ne pas appliquer les nouvelles annotations ou compteurs comme s’ils avaient existé dans les anciens runs.

## Limites, budget et suite

**Préparation statique prête ; feu vert expérimental non donné.** Accès effectif à Astra, authentification, quota disponible et enforcement du contexte/effort restent non testés. Aucun besoin d’installation supplémentaire identifié. Les paramètres sont explicités conformément à la [documentation officielle Codex](https://learn.chatgpt.com/docs/config-file/config-reference) ; celle-ci ne garantit pas l’accès de ce compte.

Le coût exact reste inconnu : ni budget total de tokens ni délai maximal nouvellement imposé. Ajouter un plafond maintenant changerait les conditions face à V2 ; cela demanderait un arbitrage distinct. Ne pas confondre tokens du préflight et coût candidat.

Même alias ne prouve pas un snapshot serveur immuable ; exécution après V2, absence de randomisation/répétitions, variations de charge/cache et éventuels défauts du chargeur scientifique figé limitent la conclusion causale. **Comparaison encadrée, pas identité parfaite de toutes les conditions.** La dominance qualité/temps/tokens reste la règle existante.

Prochaine décision : autoriser séparément la V1 simple, puis publication avant la scientifique. Aucune V2.1/V2.2 ni modification de gouvernance dans ce chantier.

[V2 Astra medium](astra-medium-v2.md) · [Conclusions](CONCLUSIONS.md) · [README](../README.md)
