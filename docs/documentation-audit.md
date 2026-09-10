# Bilan du chantier documentaire et d’observabilité

**Français** · [English (UK)](documentation-audit.en.md) · [Español](documentation-audit.es.md) · [Português](documentation-audit.pt.md)

[Guide](reading-guide.md) · [Résumés des cinq V2](../results/run-summaries/index.md) · [Instrumentation](observability.md)

## Résultat et périmètre

Le parcours est README → guide → couverture « run en 2 minutes » → PV/verbatim → trace/run.json. Quatre langues, cinq V2 terminées couvertes, aucun benchmark relancé. Le guide explique métiers, transmissions, parallélisme, barrières, corrections et limites des comparaisons. Les interprétations sont séparées des faits générés.

Les couvertures restent hors runs/ : modifier le début d’un PV historique aurait invalidé son empreinte. Les nouveaux résumés donnent accès au détail intact. La gouvernance et le protocole ne changent pas.

## Contrôles exécutés

| Contrôle | Résultat et portée |
| --- | --- |
| Maintenance Python | 12/12 méthodes de tests réussies, sans appel modèle ; liste ci-dessous. |
| Génération | summarize_runs.py puis --check : sorties reproductibles et actuelles. |
| Liens et langues | check_documentation.py : liens locaux de README/docs/results/logs/governance, navigation réciproque des nouvelles familles ; 64 empreintes historiques contrôlées. |
| Markdown | markdownlint '**/*.md' réussi avec les exclusions historiques déjà en place. |
| Solutions existantes | Neuf solutions V1/V2 revérifiées : 66 exécutions de groupes réussies. Ce sont les 15 méthodes distinctes habituelles répétées, pas 66 nouveaux tests. |
| Contrôles candidats Scientific moyen | 4/4 méthodes de controle_final.py réussies, distinctes du score officiel. |
| Conservation | git diff 1dd93a7 -- runs challenges prompts governance scripts/run_v2.py scripts/publish_v2.py : aucune différence. Aucun compteur, texte de run, configuration ou solution modifié. |

## Les douze tests de maintenance, explicitement

| Test dans tests/test_observability.py | Ce qu’il vérifie |
| --- | --- |
| test_success_passes_arguments_and_return_unchanged | Arguments/retour intacts, temps relatifs exacts, absence de prompt/chemin dans la mesure. |
| test_failure_is_persisted_and_propagated | Même exception propagée ; état failed enregistré sans texte d’erreur privé. |
| test_arbitrary_parallel_agents_are_not_serialised | Cinq sessions passent une barrière commune ; intervalles réellement superposés dans ce test local. |
| test_original_frozen_runner_and_publisher_hashes | Empreintes des deux scripts historiques actuels inchangées. |
| test_full_sequence_prompts_arguments_and_barriers_unchanged | Les deux lanceurs appellent sept fausses sessions : mêmes prompts/arguments, dépendances respectées, deux groupes concurrents, fonction d’origine restaurée. |
| test_allowlist_and_original_duration_preserved | Fusion sur copie ; champs privés exclus ; durée CLI initiale préservée. |
| test_rejects_missing_duplicate_or_mismatched_sessions | Capture partielle, doublon ou rôle incohérent refusé. |
| test_rejects_invalid_times_and_dependencies | Temps négatif/non fini/incohérent, dépendance invalide, source inconnue refusés. |
| test_merge_cli_does_not_overwrite | Un fichier de sortie existant reste intact. |
| test_missing_metrics_are_not_zero_and_no_fake_timing | Données manquantes non remplacées par zéro ; pas de timeline fabriquée. |
| test_measured_timing_generic_role_and_no_counter_double_count | Rôle local arbitraire, rendu des intervalles, cache et raisonnement non recomptés. |
| test_generated_pages_are_current | Cinq couvertures et index, quatre langues, conformes au générateur. |

Commandes reproductibles dans le [guide technique](observability.md). Les tests n’appellent jamais Codex : ils testent le programme de mesure, pas l’intelligence des candidats.

## Vérificateurs existants rejoués

| Solutions conservées | Groupes réussis par solution |
| --- | ---: |
| astra-medium-core-v2-001, astra-core-v2-001, sol-core-v2-001 | 6 chacune |
| astra-medium-scientific-v2-001, sol-scientific-v2-001 | 9 chacune |
| astra-core-v1-002, sol-core-v1-001 | 6 chacune |
| astra-scientific-v1-002, sol-scientific-v1-001 | 9 chacune |

Commande : PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify.py --solution runs/IDENTIFIANT/solution, avec --challenge scientific-calculator pour les scientifiques. Ce sont des contrôles de maintenance, **pas de nouvelles tentatives ni de nouveaux coûts de benchmark**. [Les 71 contrôles nommés](acceptance-tests.md) restent inchangés.

## Audit des incohérences historiques

Les mentions « V2 pas encore lancé » du protocole et de l’ancien préflight étaient un état au gel. Le guide sépare désormais explicitement cet état des résultats publiés ; les preuves ne sont pas réécrites. Les expressions historiques « contradiction croisée » et « MAIN/RELAY » sont expliquées, pas remplacées dans les traces. V2.x reste une proposition ; aucun lancement ou gain supposé.

Trois runs référencent des publishers antérieurs : Sol utilise la version du commit ad7e234 ; Core Astra élevé celle de 63f9b92. Leurs empreintes sont confirmées depuis Git, pas artificiellement alignées sur le fichier actuel. Un clone sans cet historique devra récupérer les commits pour effectuer ce contrôle. Le runner expérimental commun reste identique.

## Limites et suite

- Le nouveau wrapper est testé avec de fausses sessions, **pas encore en run modèle réel** ; son petit surcoût de mesure n’est pas quantifié.
- Les Mermaid utilisent le thème du lecteur, sans palette claire forcée. Leur rendu GitHub clair/sombre n’a pas été validé visuellement ici faute de navigateur de rendu disponible ; à vérifier côté GitHub.
- Le contrôle de liens couvre les fichiers locaux, pas l’accessibilité Web ni tous les fragments d’ancre GitHub.
- Les textes et décisions sont des observations ; nouveauté absolue, bruit et causalité ne sont pas quantifiés artificiellement.
- V1 Astra moyen et protocoles V2.1/V2.2 restent à traiter dans des travaux expérimentaux séparés.

Aucune nouvelle dépendance d’exécution Python, aucune mise à jour de gouvernance, aucun secret publié. La modification locale préexistante de .gitignore est laissée hors livraison.
