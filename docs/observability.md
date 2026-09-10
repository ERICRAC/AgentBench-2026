# Instrumentation et publication des résumés

**Français** · [English (UK)](observability.en.md) · [Español](observability.es.md) · [Português](observability.pt.md)

[Guide de lecture et diagramme V2](reading-guide.md) · [Résumés](../results/run-summaries/index.md) · [Audit](documentation-audit.md)

## Périmètre

Maintenance hors run. Aucun benchmark relancé, aucune solution historique retouchée. Le lanceur [run_v2.py](../scripts/run_v2.py), le publisher historique, les prompts, permissions, rôles, barrières et critères restent inchangés. Le diagramme du guide est une explication non normative du protocole figé, pas une nouvelle orchestration.

[run_v2_observed.py](../scripts/run_v2_observed.py) appelle le lanceur existant et enveloppe seulement run_session. L’activation est **optionnelle**, à déclarer et préenregistrer avant la prochaine campagne. Les écritures de mesure ajoutent un faible surcoût non quantifié ; ne pas déclarer une identité parfaite de temps avec les anciens runs. Tester le comportement avec de fausses sessions ne valide pas un futur appel modèle réel.

## Schéma générique

[observe_sessions.py](../scripts/observe_sessions.py) ne décide pas du planning. Il accepte N sessions, rôles et groupes. Seul v2_topology décrit la V2 figée ; une future V2.x/V3 doit fournir son propre graphe approuvé.

| Champ | Nature et définition |
| --- | --- |
| session_id, role | Identité canonique, pas un nom de modèle. |
| parallel_group | Groupe concurrent spécifié ; null pour une phase séquentielle. |
| depends_on | Sessions dont la fin est nécessaire au départ ; barrières spécifiées. |
| receives_from | Identifiants de sessions sources des textes ou artefacts ; pas preuve d’adoption. Challenge/mandat externe expliqués dans le guide. |
| writes_solution | Permission spécifiée, pas constat d’écriture effective. |
| started_at_seconds, ended_at_seconds | Mesures monotones relatives à l’entrée du wrapper, avant la préparation du lanceur. Jamais des heures civiles. |
| duration_seconds dans observation | Fin moins début autour de l’invocation entière : configuration, lancement CLI, capture et analyse des événements inclus ; écriture de l’observation exclue. |
| duration_seconds historique | Ancienne mesure CLI, conservée à son emplacement initial ; pas remplacée par la durée d’invocation. |
| outcome | returned ou failed ; pas un verdict d’acceptation. |

L’origine relative du wrapper diffère de celle de wall_duration_seconds du lanceur historique. Ne pas soustraire des mesures entre ces deux référentiels. Un chevauchement est établi uniquement si les intervalles mesurés se recouvrent. Les consultations historiques ont des durées mais aucun début/fin : aucune timeline exacte reconstruite.

## Flux de travail futur — uniquement après autorisation de run

Créer/préenregistrer d’abord un dossier vierge, challenge et configurations selon le protocole approuvé. Exemple de commande (NEW-RUN est un nom à remplacer, pas une tentative créée ici) :

```bash
python3 -B scripts/run_v2_observed.py --run runs/NEW-RUN --challenge calculator
```

Le dossier privé annoncé par le lanceur contient observations.json, mis à jour à chaque fin de session, échec compris. Un arrêt brutal avant la fin peut laisser une session absente : ne pas l’interpréter comme zéro. Aucun prompt, texte d’erreur, raisonnement interne ou chemin absolu n’est ajouté par l’observateur.

Après revue des captures et publication habituelle via publish_v2.py, enrichir une **nouvelle copie** de trace :

```bash
python3 -B scripts/attach_observations.py --trace runs/NEW-RUN/trace.json --observations /tmp/CAPTURE/observations.json --output runs/NEW-RUN/trace-observed.json
```

La fusion refuse un fichier de sortie existant, les identifiants manquants/doublons, rôles incohérents, valeurs non finies et violations de barrière. Elle conserve les métriques originales et exporte une liste explicite de champs. Une capture partielle demande un bilan d’interruption distinct ; ne pas publier les captures privées en bloc. Le filtre historique n’est pas une garantie complète de détection de secrets : revue préalable obligatoire.

Dans les métadonnées du **futur** run, référencer trace-observed.json et son empreinte, le wrapper, l’observateur, l’adaptateur, leurs empreintes et le runner historique utilisé. Ne jamais changer les métadonnées des runs déjà publiés. Le publisher historique reste utilisable ; l’enrichissement et le résumé sont des étapes hors candidat.

## Génération éditoriale

```bash
python3 -B scripts/summarize_runs.py
python3 -B scripts/summarize_runs.py --check
python3 -B -m unittest discover -s tests -v
python3 -B scripts/check_documentation.py
markdownlint '**/*.md'
```

Le premier appel régénère les cinq couvertures V2 et leur index, en quatre langues. Faits : run.json/trace.json ; analyses revues manuellement : [run-interpretations.json](run-interpretations.json). Modifier cette source, pas les pages générées. Données manquantes affichées comme telles ; cache/raisonnement jamais recomptés.

Pour une future topologie, fournir run.json avec run_id, challenge, mode, statut, modèle/effort, verification, usage et trace ; trace contient roles et sessions, chacune avec phase ou session_id, role, compteurs et observation facultative. Les clés de vérification suivent les fichiers historiques. Un rôle local et une phase inconnue sont acceptés sans inventer la V2.

```bash
python3 -B scripts/summarize_runs.py --run runs/NEW-RUN --interpretation /tmp/interpretation-reviewed.json
```

Le JSON éditorial contient les quatre clés fr/en/es/pt ; sans texte, l’interprétation reste non enregistrée. La sortie reste dans results/run-summaries, sans toucher runs/. Ajouter ensuite la future couverture à un index adapté à sa campagne : l’index actuel liste seulement les cinq V2 complètes. Le code générique n’est pas une approbation du protocole V3.

## Vérifications et limites

Les tests couvrent retours/arguments intacts, échec conservé, cinq rôles parallèles, égalité des sept prompts/arguments entre lanceurs, barrières, temps réels simulés, compteurs manquants, refus d’écrasement, rendu d’un rôle local et génération reproductible. Ils ne mesurent ni latence réseau ni consommation d’un futur modèle.

[Bilan exécuté et limites de rendu](documentation-audit.md). La validation réelle du nouveau lanceur reste à faire lors d’un run explicitement autorisé.
