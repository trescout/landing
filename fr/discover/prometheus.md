# Outil de surveillance de systèmes et de services Prometheus

Prometheus est un outil de surveillance qui assure des opérations de surveillance de systèmes et de services ainsi que la gestion d'une base de données de séries temporelles (time series database). Collectant des métriques à partir de cibles à des intervalles définis, le système évalue des règles, affiche les résultats et peut générer des alertes selon des conditions définies.

- ★ 67 226
- Go
- GitHub Trending · 2026-11-07

## Mises à jour

- **7 novembre 2026:** Étoiles 67,225 → 67,226, dernière version v3.16.0 (5 novembre 2026).

## Ce que ça vous apporte

- collecte des métriques à partir des cibles à des intervalles définis
- affiche les résultats en évaluant les règles
- peut générer des alertes dans les conditions définies

## Installation

**exécution avec Docker**

```
docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus
```

## Exécution

**compilation à partir de la source et exécution**

```
make build
./prometheus --config.file=your_config.yml
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite démarrer l'application Prometheus, un outil de surveillance de systèmes et de services, en utilisant Docker. À cette fin, exécutez la commande docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus.

Dépôt : https://github.com/prometheus/prometheus. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Time Series Database](https://trescout.com/fr/dictionary/time-series-database/)
- [Database](https://trescout.com/fr/dictionary/database/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** développeurs et administrateurs système souhaitant suivre l'état du système et de ses services
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/prometheus/prometheus)
- [Lire en turc →](https://trescout.com/discover/prometheus/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-07 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/prometheus/
