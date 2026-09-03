# Contrôle de source pour les agents d'intelligence artificielle

Atlas est un système de contrôle de source (source control) utilisé pour les agents d'intelligence artificielle dans les processus de développement logiciel. Il permet de suivre et d'interroger les modifications effectuées par plusieurs agents de codage à partir d'un point central.

- ★ 3 058
- Rust
- GitHub Trending · 2026-09-03

## Ce que ça vous apporte
- Suit les modifications effectuées par différents agents de codage à partir d'un point central.
- Grâce à une mémoire partagée entre les agents, il vous permet de reprendre là où vous vous étiez arrêté lors des changements de tâches.
- Associe chaque modification de code à la justification et aux commandes de l'agent qui a effectué cette modification.

## Installation
**Installation des dépendances nécessaires**

```
sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
```

**Compilation de l'application à partir du code source**

```
git clone https://github.com/pacifio/atlas
cd atlas
bun install
bun run dev:app
```


## Si vous ne codez pas
Tu es un assistant de développement logiciel. En utilisant Atlas, enregistre toutes les modifications de code que tu effectues, les décisions que tu prends et les outils que tu utilises avec l'historique de la session. Si tu dois passer d'un agent à un autre, comme Claude Code ou Codex, pendant que tu travailles, lis les plans et les notes d'architecture de la session précédente à partir de la mémoire partagée. Maintiens le contexte en appelant les fichiers, les dossiers ou les sessions passées dans la base de code avec le signe '@' et documente la raison de chaque modification que tu effectues avec les justifications de la session correspondante.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/atlas/
