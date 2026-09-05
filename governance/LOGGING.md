# Politique de journalisation publique

**Français** · [English (UK)](LOGGING.en.md) · [Español](LOGGING.es.md) · [Português](LOGGING.pt.md)

Le journal rend le processus auditable sans exposer la conversation complète.
Chaque entrée reçoit un numéro séquentiel stable, sans date ni heure.

## Contenu conservé

- demande humaine reformulée en une phrase ;
- réponse ou action de l'agent résumée ;
- rôle des agents impliqués ;
- décision et justification utiles à l'expérience ;
- fichiers affectés et résultat des contrôles ;
- erreurs, corrections et interventions humaines significatives ;
- métriques disponibles, explicitement qualifiées si elles sont approximatives.

## Contenu exclu

- prompts ou réponses bruts contenant des éléments personnels ;
- secrets, jetons, phrases secrètes, clés privées et chemins d'authentification ;
- détails de compte sans intérêt expérimental ;
- raisonnement interne ou verbatim inutile ;
- horodatages dans l'historique conversationnel public.

Les Markdown publics peuvent conserver une date ou une durée utile au
protocole, mais pas l'heure de travail de l'auteur. Une information masquée est
omise ou indiquée comme non publiée ; elle n'est jamais remplacée par une heure
fictive.

## Forme d'une entrée

```markdown
## Échange 000

**Demande synthétique** — …

**Réponse synthétique** — …

**Trace utile** — acteurs, décisions, fichiers et contrôles.
```

Les métadonnées techniques propres à un run peuvent conserver leurs dates et
durées lorsqu'elles font partie du protocole de mesure. Cette exception ne
s'applique pas à l'historique synthétique des échanges.

## Procès-verbal par run

Chaque run publié possède un `PV.md` distinct du journal général. Il nomme le
commanditaire, l'orchestrateur expérimental, l'agent candidat, les consultants
et le vérificateur. Il numérote les mandats, avis, réponses, arbitrages,
corrections et verdicts observables.

Le PV est une synthèse probante, pas une transcription intégrale. Il relie les
décisions aux fichiers, tests et métriques disponibles, indique les sorties
non capturées et exclut le raisonnement interne brut. À partir de V2, chaque
recommandation de consultant est associée à son rôle et à la décision motivée
de l'orchestrateur : retenue, écartée ou non vérifiable.

Après chaque échange modifiant le dépôt, l'entrée correspondante est ajoutée
avant le commit. Le titre du commit reste court ; son corps résume l'objectif,
les changements et les contrôles. Le commit est poussé sauf instruction
contraire explicite.
