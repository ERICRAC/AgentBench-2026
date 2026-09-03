# Trace synthétique — `scientific-single-001`

Cette trace conserve les décisions et résultats utiles sans transcript brut ni
heure de travail. Les événements JSONL complets sont restés temporaires et ne
sont pas publiés.

## Événement 001 — cadrage

Le candidat annonce un fonctionnement solo, lit `CHALLENGE.md` et confirme que
ses écritures resteront dans `solution/`.

## Événement 002 — gouvernance locale absente

La tentative de lire `governance/RESPONSE_FORMAT.md` depuis le dossier du run
échoue : le fichier global n'est pas copié localement. Le candidat poursuit à
partir du cahier des charges sans demander d'intervention.

## Événement 003 — inventaire

Le candidat inventorie uniquement `CHALLENGE.md`, `run.json` et le dossier
`solution/` vide. Aucune autre solution n'est consultée.

## Événement 004 — première implémentation

Deux fichiers sont produits : un moteur scientifique complet et son README.
Le parseur est récursif et repose sur une liste blanche de symboles.

## Événement 005 — contrôles ciblés

Le candidat compile le module et teste notamment les puissances, les domaines,
la séparation SVG autour d'une discontinuité, l'échappement du titre et la
récupération de la CLI. Ces contrôles ciblés sont annoncés réussis.

## Événement 006 — premier passage officiel

Le vérificateur exécute neuf groupes : trois réussissent et six terminent en
erreur avant leurs assertions fonctionnelles. La cause commune est
`@dataclass`, qui suppose que le module est présent dans `sys.modules`, alors
que le chargeur dynamique du test ne l'y inscrit pas.

## Événement 007 — première correction

Le candidat remplace la dataclass interne représentant un token par une petite
classe à `__slots__`. Il conserve la même API publique.

## Événement 008 — passe intermédiaire

Une commande de compilation et vérification quitte avec le code 1, sans sortie
capturée dans la trace. Le candidat déclare avoir atteint 8/9 et identifie le
découpage de `log10` en `log` puis `10`. Ce score intermédiaire est une
déclaration du candidat, pas une mesure vérifiable dans le journal brut.

## Événement 009 — seconde correction

Le tokenizer autorise les chiffres après la première lettre d'un identifiant.
La liste blanche continue de refuser tout nom inconnu.

## Événement 010 — passage final

Le vérificateur officiel réussit les neuf groupes. Le candidat revoit les deux
livrables, supprime son cache Python et confirme n'avoir modifié aucun fichier
extérieur à `solution/`.

## Événement 011 — clôture

Le candidat tente d'appliquer la règle de livraison Git, mais l'index parent
est en lecture seule dans son bac à sable. Il termine avec un compte rendu
structuré et un code de sortie nul. L'orchestrateur réalise ensuite la
vérification indépendante, les métadonnées et la publication.
