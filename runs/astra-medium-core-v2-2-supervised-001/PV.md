# PV — astra-medium-core-v2-2-supervised-001

## Identification

Pilote V2.2 supervisé, calculatrice simple, campagne astra-medium-supervised-001.
Commanditaire : Éric Racineux. RELAY : orchestrateur expérimental hors candidat.
Gel : 2e64065. Code candidat intact : ce3cb63. Statut : interruption par quota.

| Rôle | Métier | État | Modèle / effort demandés | Droits |
| --- | --- | --- | --- | --- |
| MAIN P1 | Développeur seul écrivain | Lancé, non terminé | gpt-6-astra / medium | solution/ |
| REV-01 P2 | Relecteur critique | Non lancé | gpt-6-astra / medium | Lecture seule prévue |
| MAIN P3 | Développeur / arbitre | Non lancé | gpt-6-astra / medium | solution/ prévu |
| Vérificateur | Suite indépendante, sans LLM | Diagnostic après interruption | Sans objet | Contrôle des livrables |

## MSG-001 — RELAY → MAIN

Mandat complet transmis : [PROMPT.md](PROMPT.md), incluant le défi actif et
l'enveloppe initiale sans historique candidat. Configuration et empreinte du
prompt conservées dans le [manifeste](../../governance/v2-2-supervised.json)
et les [preuves de phase](phase-evidence.json).
La publication Markdown ajoute uniquement un saut de ligne final ; les deux
empreintes (prompt original et fichier public) sont distinguées dans run.json.

## MSG-002 — MAIN → RELAY, texte visible

> Je vais lire le contrat actif, puis créer les deux livrables et effectuer des contrôles locaux sans lancer le vérificateur officiel.

Aucune réponse finale reçue. La [trace JSONL](trace.jsonl) conserve les commandes,
leurs sorties, les événements de fichiers et l'erreur. Seuls le chemin temporaire
et les liens/heure de réinitialisation du message de quota sont retirés.
Le raisonnement interne n'est pas publié.

## EVT-003 — actions observées

Lecture du CHALLENGE réussie. Inventaire rg vide, code 1 attendu pour cette
recherche sans résultat : ce n'est pas la cause finale de l'arrêt.
Création de calculator.py et README.md signalée puis confirmée sur disque.
Aucun contrôle candidat après écriture n'est enregistré.

## EVT-004 — arrêt

La CLI signale « You've hit your usage limit. », puis turn.failed.
Processus : 48,639 s, code 1. Temps mural du relais : 48,641 s.
Compteurs de tokens : non enregistrés ; nombre de requêtes modèle :
non enregistré. Ces valeurs manquantes ne valent pas zéro.
Le relais s'arrête sans lancer REV-01 ni MAIN final, sans réessai.

## CTRL-005 — contrôles après clôture

Les empreintes des livrables publiés correspondent aux fichiers privés.
Contrat, vérificateur et tests du workspace sont intacts ; entrées gelées vérifiées.
Le vérificateur indépendant passe 6/6 groupes, soit 14 contrôles élémentaires,
sur les fichiers récupérés. Ce diagnostic rétrospectif n'est pas un premier
passage officiel candidat P3 et n'a pas été renvoyé au candidat.

Couverture : deux livrables ; absence d'eval/exec ; quatre opérations ;
opérateur invalide ; division par zéro ; cinq contrôles CLI de récupération.
[Checklist détaillée](../../docs/acceptance-tests.md).

## Analyse sociale et conclusion

Aucun échange MAIN ↔ REV-01 : le relecteur n'a pas été lancé. Aucune recommandation
ou décision d'arbitrage à analyser, aucun gain collaboratif mesurable.
Ce n'est ni un échec fonctionnel de la calculatrice, ni une V2.2 achevée.
Ne pas inclure 48,641 s comme temps total V2.2 ni calculer un ratio de tokens.
Le coût incomplet de l'essai reste séparé des références terminées.
Une nouvelle tentative exige un nouvel ID et une solution vide ; aucune reprise
silencieuse ou réutilisation du code présent.
