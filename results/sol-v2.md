# V2 Sol — synthèse Core et Scientific

**Français** · [English (UK)](sol-v2.en.md) · [Español](sol-v2.es.md) · [Português](sol-v2.pt.md)

## Réponse directe

V2 Sol/high termine les deux défis au plafond officiel : **15/15 groupes
`unittest`, soit 71/71 contrôles élémentaires**. Core réussit 6 groupes et
14 contrôles dès le premier passage. Scientific passe de 3/9 groupes à 9/9
après une correction du chargement Python 3.13, puis le vérificateur
indépendant confirme les 57 contrôles.

La conformité finale est identique à V1 Sol. V2 demande toutefois **2 384,139
secondes** et **1 475 626 tokens entrée + sortie**, contre 1 199,432 secondes
et 454 376 tokens pour V1. Avec la règle de Pareto préenregistrée, **V1 domine
V2 sur les deux défis** : qualité mesurée égale, temps et tokens inférieurs.

[Catalogue explicite des 71 contrôles](../docs/acceptance-tests.md) · [Rapport
V2 Core](sol-v2-core.md) · [Comparaison V1 Sol/Astra](sol-vs-astra-v1.md)

## Tableau de verdict

| Cellule | Premier passage | Verdict final indépendant | Temps mural | Entrée + sortie |
| --- | ---: | ---: | ---: | ---: |
| V1 Sol · Core | 6/6 groupes · 14/14 contrôles | 6/6 · 14/14 | 189,964 s | 158 101 |
| V2 Sol · Core | 6/6 groupes · 14/14 contrôles | 6/6 · 14/14 | 796,534 s | 559 088 |
| V1 Sol · Scientific | 3/9 groupes | 9/9 · 57/57 | 1 009,468 s | 296 275 |
| V2 Sol · Scientific | 3/9 groupes | 9/9 · 57/57 | 1 587,605 s | 916 538 |
| **V1 total** | **9/15 groupes** | **15/15 · 71/71** | **1 199,432 s** | **454 376** |
| **V2 total** | **9/15 groupes** | **15/15 · 71/71** | **2 384,139 s** | **1 475 626** |

V2 représente ×1,99 le temps mural de V1 (+98,8 %) et ×3,25 ses tokens
(+224,8 %). Sur Scientific seul, les rapports sont ×1,57 et ×3,09. Le cache
est inclus dans l'entrée et le raisonnement dans la sortie ; ils ne sont pas
additionnés une seconde fois.

## Scientific — parcours observé

| Phase | Durée session | Entrée | Sortie | Mots visibles |
| --- | ---: | ---: | ---: | ---: |
| SA-01 · analyse | 78,281 s | 14 402 | 2 015 | 915 / 1 200 max |
| SA-02 · analyse | 73,029 s | 14 404 | 1 860 | 1 065 / 1 200 max |
| SA-01 · contradiction | 41,247 s | 16 295 | 996 | 413 / 600 max |
| SA-02 · contradiction | 38,271 s | 16 297 | 917 | 466 / 600 max |
| MAIN · première solution | 810,863 s | 394 075 | 21 975 | 429 |
| SA-03 · critique | 226,117 s | 26 664 | 6 122 | 666 / 1 200 max |
| MAIN · arbitrage final | 431,056 s | 389 108 | 11 408 | 555 |
| **Total** | **1 698,864 s-agents** | **871 245** | **45 293** | **4 509** |

Les phases partiellement parallèles expliquent que la somme des temps-sessions
soit supérieure au temps mural. Les sept sessions ont des identifiants de
thread distincts et utilisent Sol/high, une fenêtre déclarée de 200 000 tokens
et une compaction à 180 000.

## Relation sociale et corrections

SA-01 traite le contrat et la sécurité ; SA-02 l'architecture et la
testabilité. Après leurs analyses aveugles, la contradiction croisée rend
visibles trois arbitrages utiles : plafonds de ressources non contractuels,
politique des clés de variables supplémentaires et sécurité des chemins de
sortie. MAIN regroupe 16 recommandations initiales : 15 retenues et une
écartée.

SA-03 examine ensuite la première solution et formule 15 points : quatre
défauts, sept risques et quatre préférences. MAIN en retient 10 et en écarte 5.
Avant le premier vérificateur, cette critique provoque six corrections :
gestion complète de Ctrl-C, affichage numérique fidèle, évaluation itérative
des AST profonds, exemple README cohérent, neutralisation des contrôles du
terminal et taxonomie de `0^-1`.

Le premier passage officiel échoue néanmoins dans six groupes avant leurs
tests fonctionnels. Une cause unique est identifiée : le décorateur
`dataclass` du jeton dépend de `sys.modules`, contrairement au mode de
chargement du vérificateur sous Python 3.13. MAIN remplace ce conteneur par une
classe simple puis atteint 9/9. V1 Sol avait rencontré le même profil 3/9 →
9/9 ; V2 n'a donc pas amélioré la convergence officielle sur cette cellule.

## Ce que V2 permet — et ne démontre pas

- La critique spécialisée a bien détecté des défauts avant l'arbitre et laisse
  une chaîne décisionnelle auditable.
- Ces améliorations concernent surtout des comportements non distingués par la
  suite officielle ; elles ne constituent pas un gain de qualité quantifié.
- Sur Core, les avis sont largement redondants et le coût de coordination est
  particulièrement défavorable.
- Sur Scientific, le débat est plus riche, mais n'évite pas le défaut de
  chargement qui détermine le premier score.
- Une seule observation par cellule ne permet aucune conclusion statistique
  générale sur Sol ni sur le multi-agent.

Le résultat recevable est donc : **V2 apporte de la traçabilité sociale et des
corrections précoces observables, mais aucun gain sur les 71 contrôles figés ;
son surcoût est net.** Le jalon d'observation doit maintenant décider si une
V2.1 porte une hypothèse différente et testable, sans réécrire V2.

## Preuves auditables

- Core : [PV verbatim](../runs/sol-core-v2-001/PV.md) · [trace](../runs/sol-core-v2-001/trace.json) · [métadonnées](../runs/sol-core-v2-001/run.json).
- Scientific : [PV verbatim](../runs/sol-scientific-v2-001/PV.md) · [trace](../runs/sol-scientific-v2-001/trace.json) · [métadonnées](../runs/sol-scientific-v2-001/run.json) · [décisions](../runs/sol-scientific-v2-001/solution/DECISIONS.md).

Le protocole et le runner n'ont pas changé entre Core et Scientific. Les
textes visibles sont publiés après filtrage ; aucun raisonnement interne brut,
secret ou horaire de travail n'est exposé.
