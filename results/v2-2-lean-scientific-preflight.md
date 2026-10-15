# Préflight scientifique — binôme allégé

[Français](v2-2-lean-scientific-preflight.md) · [English (UK)](v2-2-lean-scientific-preflight.en.md) · [Español](v2-2-lean-scientific-preflight.es.md) · [Português](v2-2-lean-scientific-preflight.pt.md)

Préparation uniquement : aucun candidat lancé, aucun appel modèle. Les résultats simples restent intacts.

## Constat et proposition

Le contrat intégral occupe une enveloppe initiale de 5 023 caractères. Les profils ci-dessous emploient uniquement du texte synthétique, jamais une ancienne solution. Ils incluent un README de 1 000 caractères, un rapport MAIN de 150 mots, une revue de 300 mots et 1 000 caractères de sortie de contrôle. Ce ne sont ni des estimations de taille du futur code, ni des tokens.

| Code synthétique | Revue | Transmission finale | 12 000 | 24 000 proposés |
| ---: | ---: | ---: | :---: | :---: |
| 4 000 | 12 527 | 16 791 | ✗ | ✓ |
| 8 000 | 17 073 | 21 337 | ✗ | ✓ |
| 16 000 | 26 165 | 30 429 | ✗ | ✗ |

Aucun profil ne passe à 12 000 ; même sans code, ces transmissions fictives dépassent ce seuil. À 24 000, la frontière de cette fixture est 10 342 caractères de code. Les échappements JSON comptent ; le mandat et le contexte client sont exclus. Une sortie de revue plus longue peut dépasser le seuil. Aucun contenu ne sera tronqué silencieusement.

## Protocole proposé

Astra moyen, un développeur et un relecteur, trois sessions distinctes, aucune relance. Arrêt intersession à 150 000 tokens observés entrée + sortie, dépassement possible pendant une session. Pas de cible < 100 000 promise pour la scientifique. Score attendu à mesurer : 9 groupes / 57 contrôles, pas un résultat acquis.

OBS-001 est traité dans de nouveaux mandats : les contrôles locaux sont explicitement autorisés sans référence à un manifeste absent des entrées. Nouvelle campagne proposée astra-medium-lean-002 ; comparaison historique exploratoire, pas attribution causale à l'organisation. Une comparaison homogène nécessitera des témoins autorisés séparément.

## Suite et limites

Le moteur figé 001 reste limité à la calculatrice simple : aucune adaptation réelle livrée dans cette préparation. Après accord sur 24 000 : adapter dans une nouvelle version le défi, les livrables, la suite copiée et la commande scientifique ; vérifier sans modèle les trois phases, les frontières de fichiers et les arrêts, puis geler. Lancement réel soumis à accord explicite. Aucun changement de gouvernance générale.

## Artefacts

- [JSON](v2-2-lean-scientific-size.json) · [Script](../scripts/preflight_lean_scientific.py) · [Tests](../tests/test_lean_scientific_preflight.py).
- [Draft](../governance/v2-2-lean-scientific-draft.json).
- [MAIN initial](../prompts/v2-2-lean-scientific-initial-draft.md) · [REV-01](../prompts/v2-2-lean-scientific-review-draft.md) · [MAIN final](../prompts/v2-2-lean-scientific-final-draft.md).
- [OBS-001](v2-2-lean-001.md).

```bash
python3 -B scripts/preflight_lean_scientific.py
python3 -B -m unittest discover -s tests -q
```
