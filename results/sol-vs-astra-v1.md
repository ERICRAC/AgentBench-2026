# V1 Sol vs Astra — contrôle à périmètre constant

**Français** · [English (UK)](sol-vs-astra-v1.en.md) · [Español](sol-vs-astra-v1.es.md) · [Português](sol-vs-astra-v1.pt.md)

## Réponse directe

Les quatre solutions atteignent leur verdict officiel final : Core 6/6 et
Scientific 9/9. Sur ces deux observations, `gpt-5.6-sol/high` consomme pourtant
**2,40 fois le temps** et **1,33 fois les tokens** de `gpt-6-astra/high`.
Scientific Sol nécessite aussi une correction après un premier passage à 3/9,
alors qu'Astra atteint 9/9 au premier passage officiel.

Ces résultats favorisent Astra sur l'efficacité observée, mais ne suffisent pas
à établir une supériorité générale : il n'existe qu'une répétition par cellule
et les générations restent stochastiques.

## Périmètre contrôlé

Le contrôle `sol-high-control-001` a été préenregistré dans le commit `a616b2d`
avant lancement. Face à `astra-high-001`, les éléments suivants sont identiques :

- cahiers des charges et tests d'acceptation, vérifiés par SHA-256 ;
- prompts Core et Scientific, vérifiés par SHA-256 ;
- Codex CLI `0.153.4`, Python `3.13.5` et même lanceur de capture ;
- effort `high`, fenêtre client 200 000 et compaction 180 000, portée `total` ;
- sessions neuves et éphémères, configuration utilisateur et règles locales
  ignorées, web désactivé, sandbox `workspace-write` ;
- candidat solo, aucun sous-agent, aucune aide humaine fonctionnelle et aucune
  opération Git pendant le run.

Le diff des fichiers de configuration contient une seule variable volontaire :
`model = "gpt-6-astra"` devient `model = "gpt-5.6-sol"`. Les deux modèles
acceptent l'effort `high` et la même fenêtre maximale déclarée dans la
[documentation OpenAI](https://developers.openai.com/api/docs/models/gpt-5.6-sol).

Le contrôle ne peut pas figer l'infrastructure serveur, la variabilité de
génération ou un éventuel déploiement interne entre les sessions. « Périmètre
constant » décrit donc le protocole client observable, pas une identité absolue
de toutes les conditions cachées.

## Résultats détaillés

| Défi | Indicateur | Astra/high | Sol/high | Écart Sol |
| --- | --- | ---: | ---: | ---: |
| Core | Premier / final / indépendant | 6/6 · 6/6 · 6/6 | 6/6 · 6/6 · 6/6 | égalité |
| Core | Durée | 100,175 s | 189,964 s | +89,6 % |
| Core | Entrée + sortie | 120 478 | 158 101 | +31,2 % |
| Scientific | Premier / final / indépendant | 9/9 · 9/9 · 9/9 | 3/9 · 9/9 · 9/9 | correction Sol |
| Scientific | Durée | 399,478 s | 1 009,468 s | +152,7 % |
| Scientific | Entrée + sortie | 220 510 | 296 275 | +34,4 % |
| **Total** | **Verdict final officiel** | **15/15** | **15/15** | **égalité** |
| **Total** | **Durée** | **499,653 s** | **1 199,432 s** | **+140,1 %** |
| **Total** | **Entrée + sortie** | **340 988** | **454 376** | **+33,3 %** |

Le cache est déjà inclus dans l'entrée et le raisonnement dans la sortie ; ils
ne sont pas additionnés une seconde fois. Détail des compteurs :

| Run | Entrée | Cache inclus | Sortie | Raisonnement inclus |
| --- | ---: | ---: | ---: | ---: |
| Astra Core | 117 769 | 96 896 | 2 709 | 195 |
| Sol Core | 152 902 | 122 112 | 5 199 | 2 149 |
| Astra Scientific | 208 078 | 167 808 | 12 432 | 1 429 |
| Sol Scientific | 280 773 | 245 888 | 15 502 | 5 408 |

## Parcours et qualité

Core produit dans les deux cas une séparation simple entre API et CLI. Les deux
modèles atteignent le plafond officiel sans correction fonctionnelle. Sol prend
presque deux fois plus de temps et 31 % de tokens supplémentaires ; aucun gain
de qualité mesuré ne compense cet écart sur ce petit défi.

Scientific distingue davantage les parcours. Sol écrit un parseur récursif,
des contrôles ciblés, l'échantillonnage, le SVG et la CLI, mais son premier
chargement par l'arbitre échoue dans six tests à cause d'un `dataclass`. Il
diagnostique puis corrige seul ce défaut et termine à 9/9. Astra obtient 9/9 au
premier passage officiel, puis découvre seul un défaut d'interpolation aux
flottants extrêmes grâce à quatre tests supplémentaires, le corrige et conserve
ces régressions.

Après clôture, l'orchestrateur a exécuté cette même suite supplémentaire sur
les deux solutions Scientific, sans les modifier : Astra réussit 4/4, Sol
échoue les quatre méthodes avec six assertions. Ce résultat reste exploratoire,
car la suite a été créée par le candidat Astra après son premier 9/9 et n'était
pas préenregistrée pour Sol. Une assertion exige en outre que les axes SVG
soient enfants directs de la racine, alors que le contrat permet leur
regroupement : elle est couplée à l'implémentation et ne constitue pas un défaut
officiel. Les autres écarts signalent néanmoins des pistes crédibles de
robustesse hors suite : grands flottants, complexité et expression inconnue
pendant l'échantillonnage.

## Enseignements recevables

- **Conformité finale :** égalité au plafond de la suite officielle.
- **Efficacité observée :** avantage Astra net sur les deux défis, en temps et
  en tokens.
- **Autocorrection :** les deux modèles détectent et corrigent un défaut sur
  Scientific, mais à des étapes différentes.
- **Couverture hors suite :** signal favorable à Astra, à traiter comme une
  hypothèse et non comme un score de benchmark.
- **Statistique :** aucune inférence générale avec `n = 1` par modèle et défi.

La prochaine comparaison réellement renforcée consisterait à figer **avant**
les runs une suite de robustesse neutre, puis à exécuter plusieurs répétitions
par cellule. Cela ouvrirait une nouvelle campagne ; les présents résultats
resteraient inchangés.

[PV Core Sol](../runs/sol-core-v1-001/PV.md) · [JSON Core Sol](../runs/sol-core-v1-001/run.json) · [PV Scientific Sol](../runs/sol-scientific-v1-001/PV.md) · [JSON Scientific Sol](../runs/sol-scientific-v1-001/run.json) · [Rapport Astra](astra-v1.md)
