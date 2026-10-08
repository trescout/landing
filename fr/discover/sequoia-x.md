# Sélection automatique d'actions pour la bourse chinoise

Sequoia-X est un logiciel basé sur Python qui effectue une sélection automatique d'actions selon des formules d'analyse technique en utilisant les données de la bourse chinoise. Il effectue des opérations de scan après la fermeture du marché en fin de journée et transmet les résultats via Feishu, une application de messagerie d'entreprise.

- ★ 7 594
- Python
- GitHub Trending · 2026-09-03

## Mises à jour

- **27 septembre 2026:** Étoiles 6,376 → 7,594.

## Ce que ça vous apporte

- Stocke les données boursières dans une base de données locale
- Applique automatiquement plusieurs stratégies d'analyse technique
- Transmet les résultats de fin de journée via l'application de messagerie Feishu

## Installation

**Installation des bibliothèques requises**

```
pip install .
```

## Exécution

**Chargement initial des données historiques**

```
python main.py --backfill
```

**Lancement du scan quotidien**

```
python main.py
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite utiliser l'outil Sequoia-X pour scanner les actions de la bourse chinoise avec des méthodes d'analyse technique. Après avoir effectué les installations nécessaires dans mon environnement Python, j'utiliserai d'abord le mode backfill pour charger les données historiques, puis le mode de fonctionnement quotidien pour obtenir un scan automatique et des notifications après la fermeture du marché. Dans ce processus, je souhaite que les données soient stockées dans une base de données SQLite locale et que les résultats soient envoyés via Feishu.

## Termes liés du glossaire

- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux investisseurs opérant sur la bourse chinoise et souhaitant automatiser leurs stratégies d'analyse technique.

## Liens

- [Dépôt GitHub →](https://github.com/sngyai/Sequoia-X)
- [Lire en turc →](https://trescout.com/discover/sequoia-x/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/sequoia-x/
