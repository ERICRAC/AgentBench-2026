# Trace synthétique — `scientific-single-002`

## Cadre

- mode : V1, Codex seul ;
- objectif : Calculatrice Scientific ;
- modèle : `gpt-5.6-sol` ;
- effort de raisonnement : `high` ;
- contexte déclaré : 200 000 tokens ;
- compaction automatique : 180 000 tokens, portée `total` ;
- sous-agents : aucun ;
- intervention humaine fonctionnelle : aucune.

La session était éphémère et utilisait les mêmes paramètres que le run Core.

## Parcours observable

1. Le candidat a relu `CHALLENGE.md` et a poursuivi malgré l'échec initial du
   chemin relatif vers le format de restitution.
2. Il a construit un tokenizer à liste blanche, un parseur récursif, les
   fonctions scientifiques, l'échantillonnage, le SVG et la CLI documentée.
3. Des contrôles ciblés du moteur, des erreurs, des discontinuités, du SVG et
   de la CLI ont réussi.
4. Le premier vérificateur officiel a quitté avec le code 1 pendant le
   chargement du module. Le candidat a attribué l'échec à l'interaction entre
   `dataclass` et le chargeur dynamique sous Python 3.13.
5. Il a remplacé la dataclass interne par une classe légère. La relance
   officielle a réussi : **9/9**.
6. L'orchestrateur a reproduit le verdict après le run : **9/9**.

## Mesures

| Indicateur | Valeur observée |
| --- | ---: |
| Durée murale arrondie | 541 s |
| Entrée | 587 315 tokens |
| Entrée servie depuis le cache | 541 312 tokens |
| Sortie | 16 177 tokens |
| Raisonnement inclus dans la sortie | 6 289 tokens |
| Entrée + sortie | 603 492 tokens |
| Commandes terminées | 16 |
| Lots de modifications | 2 |
| Messages du candidat | 11 |

Les compteurs d'entrée sont cumulés sur les tours et incluent le cache. Ils ne
représentent pas une fenêtre de contexte simultanée de 587 315 tokens.

## Limite et incident de gouvernance

L'échantillonnage uniforme peut manquer une discontinuité située strictement
entre deux points. Les valeurs effectivement indéfinies interrompent la
courbe comme demandé.

Comme dans le run Core, le candidat a appliqué la règle Git globale : il a
créé un commit limité aux deux livrables, puis tenté un push. L'authentification
SSH a bloqué la publication et le candidat n'a pas modifié le distant. Le
protocole V2 devra neutraliser explicitement cette collision de périmètre.
