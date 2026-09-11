# Préflight technique V2.2 — simulations, aucun modèle

**Français** · [English (UK)](v2-2-preflight.en.md) · [Español](v2-2-preflight.es.md) · [Português](v2-2-preflight.pt.md)

**Préflight statique et simulé réussi : 2 défis × 3 phases ; 26 nouveaux tests, 38 tests de maintenance au total. Aucun appel modèle, aucun score de calculatrice, aucun run historique modifié.** Le protocole reste non gelé et non autorisé au lancement.

## Ce qui est livré

Le [relais](../scripts/run_v2_2.py) exécute MAIN initial → REV-01 → MAIN final avec un transport déterministe injecté. Le [préflight](../scripts/preflight_v2_2.py) vérifie les choix, les deux configurations et inventorie 15 empreintes ; il simule les deux défis dans des dossiers temporaires neufs. Les trois [mandats](../governance/V2_2_PROTOCOL.md) restent inchangés. [Configurations et choix proposés](../governance/v2-2-draft/choices.json).

Les captures privées contiennent prompts exacts, événements JSONL, réponses visibles, commandes/sorties, compteurs, état par phase et instantanés initiaux/finals avec texte et SHA-256. Pas de filtre de publication automatique : ne pas pousser ces dossiers bruts. La capture du raisonnement reste privée et n’entre pas dans les transmissions. Un échec conserve les preuves disponibles et bloque la phase suivante, sans relance. Si le parseur ne peut extraire des compteurs d’une capture incomplète, le brut reste disponible et le total demeure inconnu.

**Simulation ≠ validation du transport réel.** Le module construit les arguments Codex pour inspection mais ne lance aucun processus modèle ; --live échoue avant toute création de capture. Les sessions factices produisent des fichiers marqués SIMULATION ONLY, pas des solutions. Les compteurs de test sont synthétiques (39 entrée + sortie par scénario nominal), jamais une consommation réelle. Le préflight public ne publie aucun score ni compteur fictif comme résultat de benchmark.

Les empreintes détectent des écritures interdites persistantes à l’intérieur du workspace ; elles n’empêchent ni ne détectent toutes les lectures ou écritures transitoires à l’extérieur. Les règles read-only/workspace-write sont vérifiées dans les configurations, pas appliquées par un bac à sable réel pendant ces tests Python. La déclaration de troncature et les marqueurs reconnus entraînent un arrêt ; l’absence de marqueur ne prouve pas que le CLI n’a rien tronqué. Un SIGKILL ne peut pas être intercepté : seul le dernier checkpoint est garanti. Permissions effectives, transport réel/arrêt de ses processus, vérification indépendante des instantanés et publication filtrée restent à qualifier avant un benchmark.

## Reproduire sans modèle

```bash
python3 -B scripts/preflight_v2_2.py
python3 -B -m unittest discover -s tests -v
```

```bash
sim_root=$(mktemp -d /tmp/agentbench-lean-demo-XXXXXX)
python3 -B scripts/run_v2_2.py --simulate --challenge calculator --output "$sim_root/simple"
python3 -B scripts/run_v2_2.py --simulate --challenge scientific-calculator --output "$sim_root/scientific"
```

## Checklist des 26 tests V2.2

Chaque ligne correspond à une méthode test_ du [fichier de tests](../tests/test_v2_2.py), dans l’ordre alphabétique. Les 12 tests de maintenance antérieurs s’y ajoutent ; aucun ne remplace les 6/9 groupes des calculatrices. Les tests V2.2 interdisent les appels subprocess.Popen et socket via doublures qui échouent si elles sont sollicitées.

| ID | Contrôle | test_… |
| --- | --- | --- |
| T01 | Capture séparée du dossier candidat | capture_cannot_be_nested_in_workspace |
| T02 | Configurations et commande construite sans exécution | configuration_and_unexecuted_argv |
| T03 | Changement d’effort refusé | configuration_drift_rejected |
| T04 | Enveloppes d’événements invalides refusées | invalid_event_envelope |
| T05 | JSON incomplet conservé, phase arrêtée | invalid_json_capture_preserved |
| T06 | Interruption clavier enregistrée | keyboard_interrupt_checkpointed |
| T07 | Lancement réel refusé avant transport ou écriture | live_rejected_before_transport_or_capture |
| T08 | Livrable manquant bloque la suite | missing_deliverable_stops |
| T09 | Livrable supplémentaire bloque la suite | missing_or_extra_deliverable_stops |
| T10 | Compteurs absents restent inconnus | missing_usage_is_not_zero |
| T11 | Refus de réutiliser solution ou capture | nonempty_solution_and_existing_capture_refused |
| T12 | Échec avec capture et compteurs conservés | nonzero_process_retains_raw_and_metrics |
| T13 | Sorties manquantes, troncatures, événements inconnus, compteurs invalides | parser_rejects_incomplete_unsupported_events_and_bad_usage |
| T14 | Échec de revue : aucune relance ni phase finale | phase_failure_preserved_without_retry |
| T15 | Deux défis simulés, inventaire SHA, aucun score | preflight_no_model_no_verdict_and_hash_inventory |
| T16 | Choix divergent ou autorisation inattendue refusés | preflight_refuses_changed_choice_or_authority |
| T17 | Modification du défi détectée | protected_workspace_write_stops |
| T18 | Raisonnement exclu, texte visible intact | reasoning_excluded_visible_text_unchanged |
| T19 | Réutilisation d’un thread refusée | reused_thread_stops |
| T20 | Écriture du relecteur détectée, pas de finale | reviewer_write_stops_before_final |
| T21 | CLI simulée sur deux défis, refus d’écrasement | simulation_cli_both_challenges_and_no_overwrite |
| T22 | Liens symboliques, liens physiques, binaires refusés | snapshot_rejects_symlinks_hardlinks_and_binary |
| T23 | Dossier candidat symbolique refusé | symlink_workspace_rejected |
| T24 | Ordre, dossiers transmis, instantanés, compteurs et durées | three_phases_full_handover_and_snapshots |
| T25 | Marqueur explicite de troncature bloque | truncated_output_marker_stops |
| T26 | Dépassement de mots conservé sans tronquer ni rappeler | word_overrun_recorded_without_truncation_or_retry |

## Choix et étapes avant gel

Proposition à valider : pilote exploratoire, une tentative par calculatrice, Astra moyen, trois sessions, une revue de 1200 mots ; simple publiée avant autorisation scientifique. Aucun nouveau plafond global, arrêt sur quota, aucune attente ou relance automatique. Ce choix ne garantit pas le quota Plus. Les 18 runs de confirmation sont une proposition distincte, non engagée. Choisir un budget chiffré modifierait le cadrage : le décider avant gel et traiter les références de manière comparable.

Après validation des choix : préparer et éprouver le transport réel et l’isolation sans candidat de benchmark ; tout test modèle trivial demande une autorisation distincte. Ensuite seulement figer les empreintes et demander l’autorisation du défi simple. Le présent inventaire d’empreintes est celui du brouillon courant, pas un gel ni un préflight d’accès modèle.

OpenAI Docs a guidé la séparation entre événements JSONL et messages visibles, ainsi que la préparation des options de session éphémère et de sandbox. Ces options sont décrites dans la [documentation officielle](https://learn.chatgpt.com/docs/non-interactive-mode). L’aide locale codex exec --help et la version 0.153.4 ont été consultées sans appel modèle ; TOML valide ne prouve ni acceptation par le serveur, ni accès à Astra, ni quota.

[Protocole V2.2](../governance/V2_2_PROTOCOL.md) · [JSON](v2-2-preflight.json) · [README](../README.md)
