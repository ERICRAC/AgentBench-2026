# V2.2 — transport, isolation et comparaison des modèles

**Français** · [English (UK)](v2-2-transport.en.md) · [Español](v2-2-transport.es.md) · [Português](v2-2-transport.pt.md)

## En bref

**Pilote approuvé, lancement toujours verrouillé.** Une tentative par calculatrice, sans nouveau plafond global, arrêt sur quota et aucune relance automatique. Astra moyen reste le choix actif. Ni les 18 répétitions ni un essai modèle ne sont autorisés ici.

Transport par vrais processus et isolation locale testés ; **intégration à une session modèle non qualifiée**, protocole non gelé. Aucun appel modèle de préflight, aucun nouveau score de calculatrice.

## Ce qui a été exécuté

- [x] 46 tests de maintenance : 38 existants et 8 nouveaux tests de transport.
- [x] Bubblewrap : **30/30 contrôles** sur des témoins jetables ; deux contrôles hôtes puis 14 par métier.
- [x] Deux simulations du relais, chacune avec trois processus Python réellement isolés : MAIN initial, REV-01, MAIN final. Réponses factices, compteurs modèle absents, aucun verdict technique.
- [x] Contre-épreuve Codex natif : **26/30**, quatre écarts conservés, pas masqués.
- [ ] Raccorder et qualifier le transport modèle authentifié, toutes les surfaces d’outils comprises.
- [ ] Geler, puis demander séparément le lancement de la calculatrice simple.

[Mesures brutes et empreintes](v2-2-transport.json) · [Préflight statique actualisé](v2-2-preflight-approved.json) · [Étape simulée précédente](v2-2-preflight.md)

## Checklist d’isolation

Chaque métier doit lire le contrat et la solution. MAIN peut créer, modifier, renommer et supprimer dans solution/ ; REV-01 ne peut faire aucune de ces quatre opérations. Les deux doivent échouer à lire/écrire le témoin extérieur, directement ou par lien symbolique, modifier le contrat ou joindre le serveur loopback hôte. Contrat et témoin hôtes doivent rester intacts : 14 contrôles par métier. Les deux contrôles hors sandbox prouvent que lecture/écriture du témoin et connexion loopback sont possibles avant confinement.

La sonde ne consulte aucun secret réel. Elle crée puis retire ses propres témoins. Le réseau est testé contre un serveur local jetable, pas contre Internet. L’isolation Bubblewrap monte seulement les répertoires d’exécution système en lecture seule, le workspace en lecture seule et solution/ en écriture pour MAIN ; racine synthétique en lecture seule, réseau séparé, environnement nettoyé.

**Écart natif précis :** lecture du témoin hôte refusée et fichiers hôtes intacts, mais création possible à son chemin dans la couche synthétique de la sandbox, directement puis via le lien. Deux écarts par métier. Ce n’est pas une fuite démontrée du fichier hôte ; cela enfreint notre critère strict « aucune écriture hors solution/ ». Un premier essai sous /tmp a aussi montré que le refus de ce parent empêchait les lectures nécessaires. Le contrôle retenu reproduit donc l’emplacement des runs hors /tmp.

Bubblewrap n’est **pas** utilisé pour enfermer aveuglément le CLI authentifié : il n’a ni accès aux identifiants ni réseau modèle. Sa réussite ne valide pas tous les outils d’une session Codex. Aucun mode permissif de secours n’est activé.

## Transport et limites

[scripts/v2_2_transport.py](../scripts/v2_2_transport.py) capture stdin, stdout et stderr en fichiers privés exclusifs ; pas de shell, de troncature applicative ou de relance. Échec de création, sortie non nulle et expiration de sonde laissent un état. Le groupe de processus est arrêté après exécution/interruption ; SIGKILL du parent ou panne machine peut empêcher la clôture. Les délais de 30 secondes sont propres aux sondes, pas un plafond candidat.

Les [8 tests](../tests/test_v2_2_transport.py) couvrent : entrée/sorties exactes et droits privés ; sortie 7 avec capture partielle ; expiration et arrêt ; sortie de 2 Mo ; refus de réutilisation ; exécutable absent ; commande préparée sans ancien sandbox_mode ; rôle/lien de solution invalides. Ils ne constituent pas des tests d’accès au modèle.

OpenAI Docs a guidé la séparation des profils de permissions et de sandbox_mode ; le CLI installé impose toutefois sa syntaxe observée : codex sandbox, sans sous-commande linux. [Documentation des permissions](https://learn.chatgpt.com/docs/permissions). Le constructeur de commande native reste expérimental et non raccordé au lancement.

## Modèle, effort et organisation : trois axes distincts

Totaux des deux calculatrices, runs terminés seulement ; tokens = entrée + sortie, cache déjà inclus. Score final identique : 15 groupes / 71 contrôles.

| Organisation | Modèle / effort | Temps mural cumulé (s) | Tokens |
| --- | --- | ---: | ---: |
| V1 | Sol élevé | 1199,432 | 454376 |
| V1 | Astra élevé | 499,653 | 340988 |
| V1 | Astra moyen | 287,132 | 217884 |
| V2 | Sol élevé | 2384,139 | 1475626 |
| V2 | Astra moyen | 1023,177 | 978998 |

[Sol/Astra V1](sol-vs-astra-v1.md) · [Sol V2](sol-v2.md) · [Astra moyen](astra-medium-v1-v2.md) · [Astra élevé V2 et interruptions](astra-v2-retired.md)

Sur V1, Astra élevé consomme **56,5 % de tokens supplémentaires** et prend **74,0 % de temps supplémentaire** par rapport à Astra moyen. Ce n’est pas un effet causal établi : une observation, travail de correction différent. V2 Astra élevé scientifique est interrompu : pas de total complet comparable ; ne pas traiter ses tokens manquants comme zéro.

Ton constat d’épuisement rapide du quota est conservé comme observation utilisateur. Les compteurs de tokens ne donnent pas le débit de facturation du quota Plus ; nous n’avons pas une mesure de quota avant/après par run. Aucune promesse que moyen tiendra, ni conclusion générale qu’élevé est impossible.

Conserver Sol élevé et Astra élevé dans les références. Pour comparer l’organisation, fixer modèle **et** effort ; pour comparer les modèles, fixer organisation **et** effort. Astra moyen contre Sol élevé mélange deux facteurs. Une future V2.2 Sol élevé reste une possibilité à autoriser séparément, pas un lancement ajouté au pilote.

## Reproduire et suite

```bash
python3 -B -m unittest discover -s tests -v
python3 -B scripts/preflight_v2_2_isolation.py --backend bwrap
python3 -B scripts/preflight_v2_2_isolation.py --backend native
```

La dernière commande doit actuellement sortir en échec : c’est une contre-épreuve. Les sondes OS ont nécessité une exécution autorisée hors sandbox imbriquée ; ne pas désactiver les protections du candidat pour les contourner.

**Prochaine étape : résoudre le raccordement entre authentification côté orchestrateur et outils candidats confinés, puis qualifier une sonde modèle seulement après autorisation.** Pas de nouveau paquet nécessaire constaté : bubblewrap 0.12.0 est présent. Les preuves historiques, les défis et leurs tests restent inchangés.

[Protocole](../governance/V2_2_PROTOCOL.md) · [Conclusions](CONCLUSIONS.md) · [README](../README.md)
