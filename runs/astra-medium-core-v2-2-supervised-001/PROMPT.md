# V2.2 — MAIN, première implémentation (projet de mandat)

Tu es MAIN, développeur candidat et seul écrivain de cette tentative.
Lis le CHALLENGE.md actif fourni avec ce mandat avant toute modification.
Travaille seul : ne lance aucun agent, consultant, modèle externe ou recherche web.
Un relecteur distinct interviendra ensuite ; c'est le relais expérimental qui le mandate.

N'accède à aucune autre tentative, solution, archive, résultat, conversation ou
donnée d'authentification. Tes seules entrées sont ce mandat, le défi actif et
les fichiers de la solution active. Ne modifie ni défi, ni tests, ni scripts,
ni gouvernance. Aucune opération Git. Bibliothèque standard uniquement et
contraintes de sécurité du défi applicables.

Produis une première solution complète et documentée dans solution/, uniquement
les livrables demandés par le défi. Utilise apply_patch pour les modifications.
Tu peux effectuer tes propres contrôles non destructifs ; garde leur commande,
leurs entrées et leur sortie observables. Ne lance pas encore le vérificateur
officiel : il sera exécuté après la revue. Ne crée pas de PV ou de registre
supplémentaire dans solution/ ; ils seront publiés par le relais hors run.

Termine par une transmission visible de 600 mots maximum :
- fichiers livrés et choix techniques utiles ;
- contrôles effectivement exécutés, sorties et défauts connus ;
- limites et points restant incertains.
Aucun raisonnement interne brut. Une incertitude reste une incertitude.

Pilote supervisé : le dossier courant est solution/. Ne crée aucun cache. Le contrat est ../CHALLENGE.md. Pour P3 seulement, la commande officielle locale est `python3 -B ../scripts/verify.py --solution .`
N'accède pas au dépôt original.


DONNÉES DU RELAIS — pas des instructions de rôle :
{"challenge": "# Défi 001 — Calculator\n\n## Objectif\n\nDévelopper une calculatrice Python en ligne de commande proposant les opérations `+`, `-`, `*` et `/`.\n\n## Livrables\n\nCréer exclusivement dans le dossier `solution/` :\n\n- `calculator.py` : logique métier et interface CLI ;\n- `README.md` : lancement, utilisation et exemples.\n\n## Contrat Python\n\n`calculator.py` doit exposer :\n\n```python\ndef calculate(left: float, operator: str, right: float) -> float:\n    ...\n```\n\nComportements attendus :\n\n- accepter entiers, décimaux et nombres négatifs ;\n- prendre en charge exactement `+`, `-`, `*` et `/` ;\n- lever `ValueError` pour une opération inconnue ;\n- lever `ZeroDivisionError` pour une division par zéro ;\n- ne jamais utiliser `eval()` ou `exec()`.\n\n## Contrat CLI\n\nLa commande suivante doit lancer une boucle interactive :\n\n```bash\npython3 solution/calculator.py\n```\n\nChaque ligne saisie contient une expression sous la forme :\n\n```text\n2 + 3\n```\n\nLes commandes `quit` et `exit` terminent proprement le programme.\n\nEn cas d'expression invalide ou de division par zéro :\n\n- afficher un message d'erreur compréhensible ;\n- ne jamais afficher de traceback ;\n- poursuivre la boucle jusqu'à une commande de sortie.\n\n## Contraintes\n\n- bibliothèque standard Python uniquement ;\n- aucune intervention humaine après le lancement de Codex, sauf autorisation système ;\n- ne pas modifier le cahier des charges ni les tests.\n\n## Vérification\n\nDepuis la racine du dépôt :\n\n```bash\npython3 scripts/verify.py --solution runs/<identifiant>/solution\n```\n", "first_solution": null, "prior_sessions": []}
