# Mémoire du système de fichiers pour les agents d'intelligence artificielle

Développé par Volcengine, OpenViking propose une base de données contextuelle auto-améliorée pour les agents IA. Ce système combine la mémoire des agents, les processus et les capacités de recherche d'informations (RAG) sous un même toit.

- ★ 39 151
- Python
- GitHub Trending · 2026-08-18

## Mises à jour

- **3 octobre 2026:** Étoiles 38,859 → 39,151, dernière version v0.4.23 (2 octobre 2026).
- **28 septembre 2026:** Étoiles 38,733 → 38,859, dernière version v0.4.22 (28 septembre 2026).
- **27 septembre 2026:** Étoiles 37,128 → 38,733, dernière version v0.4.21 (20 septembre 2026).
- **14 septembre 2026:** Étoiles 36,182 → 37,128, dernière version v0.4.20 (14 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Construire une gestion de contexte pour un agent d'intelligence artificielle à l'aide de la base de données OpenViking. Il structure les informations via le protocole viking:// en séparant les informations en couches de résumé L0, d'aperçu L1 et de détail L2. En plaçant la mémoire, les ressources et les capacités de l'agent dans ce système de fichiers virtuel, cela lui permet de parcourir les répertoires pendant l'interrogation et de créer une mémoire à long terme en apprenant des sessions passées.

## Termes liés du glossaire

- [RAG](https://trescout.com/fr/dictionary/rag/)
- [AI Skills](https://trescout.com/fr/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent combiner la gestion de la mémoire, les processus de récupération d'informations et les capacités des agents d'IA en un seul système organisé.
- **Licence:** AGPL-3.0

## Liens

- [Dépôt GitHub →](https://github.com/volcengine/OpenViking)
- [Lire en turc →](https://trescout.com/discover/openviking/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-18 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/openviking/
