# Mémoire du système de fichiers pour les agents d'intelligence artificielle

Développé par Volcengine, OpenViking propose une base de données contextuelle auto-améliorée pour les agents IA. Ce système combine la mémoire des agents, les processus et les capacités de recherche d'informations (RAG) sous un même toit.

- ★ 33 757
- Python
- GitHub Trending · 2026-08-18

## Ce que ça vous apporte
- Organise les informations de manière hiérarchique comme un système de fichiers.
- Il réduit le coût de l’intelligence artificielle grâce au chargement en couches.
- Rend l'historique de l'agent traçable et déboguable.

## Installation
**Installation et démarrage du serveur**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```


## Exécution
**Démarrez une discussion avec le support du bot**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```


## Si vous ne codez pas
Construire une gestion de contexte pour un agent d'intelligence artificielle à l'aide de la base de données OpenViking. Il structure les informations via le protocole viking:// en séparant les informations en couches de résumé L0, d'aperçu L1 et de détail L2. En plaçant la mémoire, les ressources et les capacités de l'agent dans ce système de fichiers virtuel, cela lui permet de parcourir les répertoires pendant l'interrogation et de créer une mémoire à long terme en apprenant des sessions passées.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openviking/
