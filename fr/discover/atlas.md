# Contrôle de source pour les agents d'intelligence artificielle

Atlas est un système de contrôle de source (source control) utilisé pour les agents d'intelligence artificielle dans les processus de développement logiciel. Il permet de suivre et d'interroger les modifications effectuées par plusieurs agents de codage à partir d'un point central.

- ★ 8 872
- Rust
- GitHub Trending · 2026-09-03

## Mises à jour

- **3 octobre 2026:** Étoiles 7,855 → 8,872, dernière version alpha-0.3.4 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 7,448 → 7,855, dernière version alpha-0.3.4 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 4,722 → 7,448, dernière version alpha-0.3.3 (19 septembre 2026).
- **19 septembre 2026:** Étoiles 4,762 → 4,722, dernière version alpha-0.3.3 (19 septembre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Tu es un assistant de développement logiciel. En utilisant Atlas, enregistre toutes les modifications de code que tu effectues, les décisions que tu prends et les outils que tu utilises avec l'historique de la session. Si tu dois passer d'un agent à un autre, comme Claude Code ou Codex, pendant que tu travailles, lis les plans et les notes d'architecture de la session précédente à partir de la mémoire partagée. Maintiens le contexte en appelant les fichiers, les dossiers ou les sessions passées dans la base de code avec le signe '@' et documente la raison de chaque modification que tu effectues avec les justifications de la session correspondante.

## Termes liés du glossaire

- [Source Control](https://trescout.com/fr/dictionary/source-control/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Destiné aux développeurs de logiciels travaillant avec plusieurs agents d'intelligence artificielle et souhaitant suivre les justifications logiques des modifications apportées aux processus de codage.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/pacifio/atlas)
- [Lire en turc →](https://trescout.com/discover/atlas/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/atlas/
