Réalise le défi décrit dans CHALLENGE.md en mode V2 multi-agent gouverné.

Contraintes particulières pour cette tentative :

- ne lis aucune autre tentative, solution ou résultat du dépôt ;
- utilise exactement trois consultants sans délégation imbriquée :
  1. analyste du contrat et de la sécurité,
  2. analyste de conception et de testabilité,
  3. critique final des cas limites ;
- les deux premiers interviennent avant l'implémentation et le critique après
  une première solution ;
- leurs missions sont consultatives et en lecture seule ; toi seul écris ;
- écris exclusivement dans `solution/` et ne modifie ni spécification, ni
  tests, ni scripts, ni gouvernance ;
- ne lance aucune opération Git (`git add`, `git commit`, `git push`) ;
- utilise uniquement la bibliothèque standard Python ;
- n'utilise jamais `eval()`, `exec()` ou `compile()` ;
- arbitre explicitement les recommandations retenues ou écartées ;
- lance le vérificateur indiqué dans CHALLENGE.md, corrige les défauts
  confirmés et termine avec une solution complète, documentée et sans
  placeholder ;
- résume les rôles, avis, arbitrages, tests, corrections et limites sans
  exposer de raisonnement interne brut.
