# PV — astra-medium-scientific-v2-2-lean-002

## Identification et verdict

Commanditaire : Éric Racineux. Orchestrateur expérimental : assistant principal,
hors candidat. RELAY : lanceur mécanique, hors équipe candidate.
Campagne astra-medium-lean-003 ; gel 4b3f887 ; code candidat 140cae6.

**9/9 groupes unittest, 57/57 contrôles élémentaires**, au premier passage
officiel du candidat, puis à la vérification indépendante.
L'instantané initial passe également lors du contrôle rétrospectif.
Initial et final sont identiques octet pour octet : aucune correction après revue.

Livrables : [code final](solution/scientific_calculator.py) et
[documentation candidate](solution/README.md). Les liens relatifs dans les
messages verbatim ci-dessous étaient destinés au dossier solution/ du candidat.

## Équipe et métiers

| ID | Métier et mission | Droits | Modèle / effort |
| --- | --- | --- | --- |
| MAIN initial | Développeur : implémenter et contrôler localement | Deux livrables dans solution/ | gpt-6-astra / medium |
| REV-01 | Relecteur critique : défauts, risques, conformité | Lecture seule, aucun fichier modifié | gpt-6-astra / medium |
| MAIN final | Développeur : arbitrer puis vérifier | Deux livrables dans solution/ | gpt-6-astra / medium |

Trois sessions distinctes, aucun sous-agent supplémentaire. Fenêtre configurée
200 000, compaction 180 000 total. Révision serveur et version CLI au lancement :
non enregistrées. Threads et configurations dans [run.json](run.json).

## Déroulement

1. L'accord humain est validé et transmis explicitement dans chaque mandat :
   l'obstacle OBS-002 de l'essai 001 ne se reproduit pas.
2. MAIN initial crée les deux fichiers et exécute un script de contrôles locaux :
   sortie capturée « 78 contrôles locaux réussis ». Il ne lance pas l'arbitre.
3. REV-01 relit statiquement ; aucun outil, aucun défaut confirmé. Il distingue
   correctement le rapport MAIN des preuves d'exécution auxquelles il n'a pas accès.
4. MAIN final arbitre quatre points, ne modifie rien et exécute l'arbitre :
   9 groupes réussis au premier passage.
5. Après clôture, l'orchestrateur contrôle indépendamment initial et final :
   9 groupes / 57 contrôles chacun, puis livre sans retoucher les fichiers.

La commande initiale pwd/rg termine à 1 dans le dossier vide ; ce constat
n'empêche pas le développement. Aucune interruption quota ni relance observée.

## Coûts par session

| Phase | Durée (s) | Entrée | Cache inclus | Sortie | Raisonnement inclus | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| MAIN initial | 159,910 | 58 692 | 39 936 | 6 323 | 130 | 65 015 |
| REV-01 | 23,739 | 16 153 | 0 | 543 | 267 | 16 696 |
| MAIN final | 23,971 | 59 571 | 37 504 | 512 | 0 | 60 083 |
| Total | 207,620 | 134 416 | 77 440 | 7 378 | 397 | 141 794 |

Temps mural du lanceur : **207,630343123 s**. Cache et raisonnement sont des
sous-ensembles, jamais ajoutés deux fois. Seuil intersession 150 000 non atteint ;
aucune garantie de plafond strict n'en découle. Enveloppes JSON : 5 023,
21 226 et 22 569 caractères ; toutes sous 24 000. Rapports finaux : 101, 184 et
191 mots, sous les limites 150/300/300.

Solde d'abonnement, coût de maintenance, de publication et d'orchestration :
non enregistrés. Les 11 968 tokens et 12,811 s de l'essai interrompu 001 restent
séparés. Le sous-total des seuls essais scientifiques allégés 001+002 est
153 762 tokens et 220,441 s, **pas le coût de toute la campagne**.

## Messages visibles, sans raisonnement privé

Chaque mandat intégral, contrat et transmission JSON est conservé dans
[prompts.json](prompts.json). Les réponses ci-dessous sont intégrales.
Les chemins privés présents dans les événements d'outils sont normalisés dans
[trace.json](trace.json), avec empreintes des captures originales.

### MSG-001 — RELAY → MAIN, main_initial

Mandat exact : [initial](../../prompts/v2-2-lean-scientific-002-initial.md).
Entrées exactes : champ main_initial de [prompts.json](prompts.json).
Durée et métriques : ligne correspondante du tableau ci-dessus.

### MSG-002 — MAIN → RELAY, main_initial

> Je vais créer les deux livrables selon le défi fourni, puis effectuer des contrôles locaux en mémoire, sans lancer le vérificateur officiel ni créer de cache.

### MSG-003 — MAIN → RELAY, main_initial

> Les deux fichiers sont créés : analyseur d’expressions, échantillonnage, export SVG et CLI. Je vais contrôler les priorités, les erreurs, les coupures de courbe, la validité XML et l’historique, avec les écritures SVG simulées en mémoire.

### MSG-004 — MAIN → RELAY, main_initial

> Créés : [scientific_calculator.py](scientific_calculator.py) et [README.md](README.md).
> 
> Implémentation avec bibliothèque standard uniquement : expressions sûres, échantillonnage, SVG autonome et CLI avec historique.
> 
> Contrôles réellement exécutés avec `python3 -B` : **78 contrôles réussis**, couvrant priorités, fonctions, entrées interdites, erreurs numériques, bornes, discontinuités, validité XML, échappement et récupération de la CLI. Les écritures SVG ont été simulées en mémoire ; aucun fichier supplémentaire ni cache créé.
> 
> Aucun défaut détecté par ces contrôles. Limites documentées : précision flottante et discontinuités entre échantillons potentiellement non détectées. L’écriture physique sur disque n’a pas été testée.
> 
> Le vérificateur officiel n’a pas été lancé, conformément à la phase MAIN initial.

### MSG-005 — RELAY → REV-01, review

Mandat exact : [review](../../prompts/v2-2-lean-scientific-002-review.md).
Entrées exactes : champ review de [prompts.json](prompts.json).
Durée et métriques : ligne correspondante du tableau ci-dessus.

### MSG-006 — REV-01 → RELAY, review

> Aucun défaut confirmé dans les deux livrables du snapshot fourni, après lecture intégrale du défi, du code et du README.
> 
> La revue statique confirme la structure attendue pour les priorités et l’associativité, la restriction des noms et appels, le traitement des erreurs numériques, l’échantillonnage avec bornes incluses et la séparation des segments aux points invalides. Le SVG échappe le titre et filtre les caractères interdits par XML. La CLI conserve les opérations réussies et intercepte les erreurs usuelles prévues. Aucune exécution dynamique interdite ni dépendance externe relevée.
> 
> **Risques et limites :**
> - Une singularité située entre deux échantillons peut être reliée. Cette limite est explicitement documentée ; le défi ne prescrit pas de détection analytique.
> - L’écriture physique et les comportements à l’exécution ne sont pas établis par cette revue statique.
> 
> **Preuves consultées :** uniquement le défi, les deux livrables fournis et le rapport MAIN. Les « 78 contrôles réussis » sont une affirmation de MAIN, sans commandes ni sorties disponibles ; ils ne constituent pas une validation indépendante consultée.
> 
> Aucune commande exécutée, aucun vérificateur officiel lancé. Aucune préférence bloquante ni correction requise identifiée.

### MSG-007 — RELAY → MAIN, main_final

Mandat exact : [final](../../prompts/v2-2-lean-scientific-002-final.md).
Entrées exactes : champ main_final de [prompts.json](prompts.json).
Durée et métriques : ligne correspondante du tableau ci-dessus.

### MSG-008 — MAIN → RELAY, main_final

> Je vais lire les livrables présents, arbitrer les constats de REV, puis exécuter le vérificateur officiel avec `PYTHONDONTWRITEBYTECODE=1`. Les 78 contrôles annoncés par MAIN restent non vérifiables sans leurs commandes et sorties.

### MSG-009 — MAIN → RELAY, main_final

> Défi intégral et deux livrables lus. Aucun défaut confirmé ; aucun changement effectué.
> 
> Arbitrages REV :
> 
> - **Retenu — conformité statique** : priorités, noms autorisés, erreurs numériques, échantillonnage, SVG et historique sont cohérents avec le contrat. Preuves : lecture du code et réussite des neuf tests officiels.
> - **Retenu — singularités entre échantillons** : elles peuvent rester reliées ; l’échantillonnage ne comporte aucune détection analytique. Cette limite figure dans le README.
> - **Retenu pour la revue initiale — exécution et écriture physique non établies** : REV n’avait exécuté aucune commande. La vérification officielle apporte désormais une validation des scénarios CLI et SVG couverts.
> - **Non vérifiable — 78 contrôles initiaux** : leurs commandes et sorties ne sont pas disponibles ; je ne les ai pas examinées.
> - Aucun constat écarté.
> 
> Contrôle exécuté depuis `solution/` :
> 
> ```bash
> PYTHONDONTWRITEBYTECODE=1 python3 -B ../scripts/verify.py --challenge scientific-calculator --solution .
> ```
> 
> Résultat : **9 tests réussis, code de sortie 0**, sans échec ni interruption.
> 
> Limites restantes : arrondis des flottants et singularités non échantillonnées. Les tests réussis ne constituent pas une preuve exhaustive pour toutes les entrées. Aucun contrat, test ou script modifié ; aucune publication effectuée.

## Registre des arbitrages

| ID | Source | Proposition / limite | Décision de MAIN final | Preuve et effet |
| --- | --- | --- | --- | --- |
| DEC-001 | MSG-006, REV-01 | Conformité statique observée | Retenue | Lecture puis 9/9 officiels ; aucun changement |
| DEC-002 | MSG-006, REV-01 | Singularités entre échantillons | Retenue comme limite documentée | README et absence de détection analytique ; pas d'exigence ajoutée |
| DEC-003 | MSG-006, REV-01 | Exécution et écriture physique non établies par la revue | Retenue pour la revue, puis couverture partielle par l'arbitre | Tests CLI/SVG réussis ; aucune preuve exhaustive |
| DEC-004 | MSG-006, REV-01 | 78 contrôles initiaux non consultables par REV | Non vérifiable pour MAIN final également | Commandes absentes de la transmission ; elles sont disponibles à l'auditeur dans run.json/trace.json |
| DEC-005 | MSG-009, MAIN final | Ne pas modifier de code sans défaut confirmé | Retenue | Instantanés initial/final identiques |

## Analyse sociale

Neuf messages visibles en comptant trois mandats et six réponses ; parmi les
réponses, trois sont des transmissions finales et trois des messages intermédiaires.
Les transmissions finales totalisent 476 mots ; les réponses complètes 570 mots.
Les tokens propres à la coordination ne sont pas isolables des lectures et outils.

Le relecteur émet quatre constats/limites arbitrés : trois retenus, un non
vérifiable pour le destinataire ; aucun écarté, aucun défaut confirmé, aucune
contradiction résolue par une correction. Il ne prétend pas avoir vérifié les
78 contrôles dont il ne reçoit pas la preuve : bonne discipline de preuve.
L'orchestrateur peut, lui, consulter la commande et sa sortie enregistrées ;
ces 78 contrôles restent des tests du candidat, pas 78 tests indépendants.

Le consensus ne produit ici aucune amélioration fonctionnelle observable.
Il apporte une relecture explicite et une clarification des limites ; sa valeur
de prévention d'erreurs sur d'autres tâches n'est pas mesurée par cet essai.
REV-01 coûte 16 696 tokens ; MAIN final coûte 60 083 tokens, incluant aussi
lecture et vérification, donc pas uniquement de la coordination.

## Comparaison exploratoire et conclusion

Référence V1 scientifique Astra moyen : 119 388 tokens, 188,560 s, même score.
Ce binôme emploie **18,8 % de tokens et 10,1 % de temps supplémentaires**,
sans correction ni gain de score. Par rapport à V2 historique scientifique
(570 382 tokens, 648,008 s), baisse observée de 75,1 % et 68,0 %.

Sources : [comparaison historique](../../results/astra-medium-v1-v2.md).
Prompts, transmission, environnement et cache diffèrent ; un seul essai par
condition. Ces écarts ne démontrent pas un effet causal de l'organisation.
Ils ne sont pas une comparaison homogène avec la calculatrice simple allégée.

**Le binôme allégé se rapproche du solo historique, sans le dépasser sur ce
cas scientifique. Le seuil de rentabilité du collectif reste non établi.**
Aucun nouveau run lancé ; résultats historiques et tentative 001 préservés.
