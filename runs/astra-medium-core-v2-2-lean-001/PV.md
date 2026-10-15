# PV — V2.2 allégée simple 001

## Identification et métiers

Commanditaire : Éric Racineux. RELAY : orchestrateur expérimental hors candidat,
chargé du transport et de la publication. Run `astra-medium-core-v2-2-lean-001`,
campagne exploratoire `astra-medium-lean-001`. Gel : `7219f54`.
Code candidat conservé séparément : `5cfa81d`.

| Rôle | Métier et mission | Droits | Modèle / effort |
| --- | --- | --- | --- |
| MAIN initial | Développeur seul, implémentation | Livrables solution uniquement | gpt-6-astra / medium |
| REV-01 | Relecteur critique, une revue statique | Lecture seule | gpt-6-astra / medium |
| MAIN final | Développeur et arbitre, nouvelle session | Livrables solution uniquement | gpt-6-astra / medium |

Trois sessions indépendantes ; identifiants, configurations, durées et compteurs
dans [run.json](run.json). Contexte 200 000, compaction 180 000 total ; aucun
plafond strict de tokens en cours de session. CLI locale annoncée : 0.153.4.
Version exacte du modèle servi non vérifiée ; modèle et effort demandés enregistrés.
Défi, fichiers, transmissions finales et revue fournis selon les mandats figés.
Aucune solution antérieure fournie. Isolation supervisée, pas confinement complet.

## Messages visibles

Trois mandats complets dans [prompts.json](prompts.json), champs de chaque phase.
Commandes et sorties intégrales dans [trace.json](trace.json), événements de
raisonnement privé exclus. Chemins temporaires normalisés en `<private-run-root>`.
Cette normalisation est la seule réécriture des textes visibles ci-dessous.

### MSG-001 — RELAY → MAIN, main_initial

Texte intégral envoyé : [prompts.json](prompts.json), champ `main_initial.text`.
Coût de session : 32.158 s ; 22624 tokens
entrée, 10624 cache inclus, 1165 sortie,
dont 0 raisonnement. Pas de mesure par message.

### MSG-002 — MAIN → RELAY, main_initial

> J’ai lu le défi intégral. Je vais créer les deux livrables avec `apply_patch`. Aucun manifeste approuvé n’étant fourni, je ne lancerai ni contrôle local ni vérificateur.

### MSG-003 — MAIN → RELAY, main_initial

> Créés dans `solution/` avec `apply_patch` :
>
> - `calculator.py` : fonction `calculate`, quatre opérations, boucle interactive, gestion des erreurs et sorties propres.
> - `README.md` : lancement, utilisation, exemples et contrat Python.
>
> Aucun contrôle local ni vérificateur officiel exécuté : le mandat exige un manifeste approuvé définissant le dossier et la commande, absent des éléments fournis.
>
> Aucun défaut identifié à la relecture ; fonctionnement non confirmé par exécution. Les calculs restent soumis à la précision des flottants Python.

### MSG-004 — RELAY → REV-01, review

Texte intégral envoyé : [prompts.json](prompts.json), champ `review.text`.
Coût de session : 13.368 s ; 11707 tokens
entrée, 0 cache inclus, 271 sortie,
dont 47 raisonnement. Pas de mesure par message.

### MSG-005 — REV-01 → RELAY, review

> Aucun défaut confirmé trouvé dans l’instantané fourni.
>
> Relecture intégrale du défi, de `calculator.py`, de `README.md` et de la transmission de MAIN :
>
> - `calculate` expose la signature demandée, prend en charge les quatre opérateurs et lève les exceptions prévues.
> - La CLI traite les expressions mal formées, les opérandes invalides, les opérateurs inconnus et les divisions par zéro avec un message compréhensible, puis poursuit la boucle.
> - `quit` et `exit` terminent proprement le programme.
> - Aucun usage de `eval()` ou `exec()`, ni dépendance externe.
> - Le README fournit les commandes de lancement, l’utilisation et des exemples cohérents avec le code.
>
> Limites de vérification : revue statique exclusivement, sans exécution ni vérificateur officiel. La transmission de MAIN ne constitue pas une preuve d’exécution. Le respect du périmètre des modifications hors instantané n’est pas vérifiable avec les données fournies.
>
> Aucune correction requise sur la base de cette revue.

### MSG-006 — RELAY → MAIN, main_final

Texte intégral envoyé : [prompts.json](prompts.json), champ `main_final.text`.
Coût de session : 20.427 s ; 51528 tokens
entrée, 37504 cache inclus, 480 sortie,
dont 0 raisonnement. Pas de mesure par message.

### MSG-007 — MAIN → RELAY, main_final

> J’ai lu le défi intégral et la revue fournie. Je vais comparer les livrables présents aux constats de REV, puis exécuter le vérificateur P3 autorisé.

### MSG-008 — MAIN → RELAY, main_final

> Arbitrage des constats REV :
>
> - **Retenu — contrat Python respecté** : signature, quatre opérations et exceptions conformes à la lecture ; tests correspondants réussis.
> - **Retenu — CLI conforme** : gestion des erreurs avec poursuite de la boucle, sorties `quit` et `exit` présentes ; test de récupération et sortie réussi.
> - **Retenu — absence d’`eval()`/`exec()` et de dépendance externe** : confirmée par lecture ; contrôle d’exécution dynamique réussi.
> - **Retenu — README cohérent** : lancement, utilisation et exemples correspondent au code.
> - **Retenu — revue antérieure uniquement statique** : aucune commande fournie pour REV. Les anciennes commandes MAIN ne sont pas disponibles et je ne prétends pas les avoir examinées.
> - **Non vérifiable — périmètre historique des modifications hors instantané** : les éléments fournis ne permettent pas de l’établir.
>
> Aucun défaut confirmé : **aucune modification nécessaire ni effectuée**.
>
> Vérificateur officiel exécuté :
> ```bash
> python3 -B ../scripts/verify.py --solution .
> ```
>
> **Verdict : 6 tests réussis, `OK`, code de sortie 0.** Aucune interruption ni contrôle restant en échec. Cette validation couvre les tests officiels exécutés, sans constituer une vérification exhaustive de toutes les entrées possibles.

## Registre d'arbitrage et observation du protocole

Aucun défaut numéroté REV-001 reçu ; REV-01 désigne le métier de relecteur.
MAIN final arbitre néanmoins les observations générales dans MSG-008.

| Décision de synthèse | Source | Avis et décision finale | Effet observable |
| --- | --- | --- | --- |
| DEC-001 | MSG-005 → MSG-008 | Contrat Python conforme, retenu ; tests réussis | Aucun changement |
| DEC-002 | MSG-005 → MSG-008 | CLI conforme, retenu ; test de récupération réussi | Aucun changement |
| DEC-003 | MSG-005 → MSG-008 | Pas d'exécution dynamique/dépendance, retenu | Aucun changement |
| DEC-004 | MSG-005 → MSG-008 | Documentation cohérente, retenu | Aucun changement |
| DEC-005 | MSG-005 → MSG-008 | Revue uniquement statique, retenu ; pas de fausse preuve d'exécution | Limite explicitée |
| DEC-006 | MSG-005 → MSG-008 | Écritures hors instantané historiquement non vérifiables par MAIN | Non vérifiable par candidat ; audit distinct du relais |

**OBS-001 — ambiguïté du mandat initial.** MAIN interprète la référence à un
manifeste approuvé absent de ses entrées comme interdisant même ses contrôles
locaux facultatifs. Il crée néanmoins les fichiers. Le relais avait un manifeste
autorisé, mais n'en a pas fourni le contenu comme artefact candidat.
MAIN final accepte la commande P3 explicitement fournie et exécute le vérificateur.
C'est une différence de travail réellement effectué, pas une économie pure de
transmission. Pas de correction du mandat ou du run après coup ; une clarification
nécessiterait une nouvelle condition documentée.

## Analyse sociale

Huit messages recensés : trois mandats, cinq messages retournés. Un relecteur,
une revue, aucun retour au relecteur. Zéro défaut confirmé, zéro correction,
cinq observations retenues et une limite non vérifiable reconnue dans l'arbitrage.
Aucune contradiction utile observée. Le recoupement statique ne démontre ni gain
de score ni inutilité universelle de la revue. Bruit et doublons non quantifiés.

MAIN initial se restreint à cause du texte d'autorité ; REV-01 distingue bien
affirmations et preuves, MAIN final respecte cette distinction et teste.
L'effet d'autorité du mandat est observable dans les messages, pas inféré d'un
raisonnement privé. Aucun consensus psychologique n'est revendiqué.

## Qualité et coûts

| Phase | Secondes | Entrée | Sortie | Total |
| --- | ---: | ---: | ---: | ---: |
| MAIN initial | 32,158 | 22 624 | 1 165 | 23 789 |
| REV-01 | 13,368 | 11 707 | 271 | 11 978 |
| MAIN final | 20,427 | 51 528 | 480 | 52 008 |
| Total sessions | 65,953 | 85 859 | 1 916 | 87 775 |

Temps mural : **65,964 s**. Cache 48 128 inclus dans l'entrée ; raisonnement 47
inclus dans la sortie. Cible < 100 000 atteinte ; seuil 150 000 non atteint.
Enveloppes 1 652 / 5 603 / 6 673 caractères, sous 12 000.
Rapports finaux 76 / 146 / 184 mots, sous les plafonds 150 / 300 / 300.
Coût direct de revue : 11 978 tokens ; coût complet de coordination non isolé.
Nombre de requêtes modèle et soldes de quota non enregistrés. Coûts du présent
chat, de maintenance, publication et vérification indépendante exclus.

Premier officiel en MAIN final : **6/6 groupes, 14 contrôles**.
Après run, vérification indépendante finale et diagnostic initial : même verdict.
Diagnostic initial jamais renvoyé au candidat. [Sorties complètes](verifications.json).
Instantanés initial et final identiques octet pour octet ; [preuves](snapshots.json).
Aucune écriture hors frontières de rôle détectée par le moteur.

## Conclusion

Run terminé et résultat technique confirmé ; aucune correction après revue.
Le coût est inférieur au pilote supervisé 002, mais OBS-001, les différences de
prompts et les conditions historiques empêchent une attribution causale.
La baisse de tokens ne se convertit pas en économie de quota mesurée.

[Rapport synthétique et comparaison](../../results/v2-2-lean-001.md).
Aucune nouvelle tentative ni scientifique autorisée par la clôture de ce run.
