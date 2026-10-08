# Gérez les arbres de travail Git

Worktrunk est une interface de ligne de commande (CLI) écrite en Rust qui simplifie la gestion des arbres de travail (worktree) Git. Développé spécifiquement pour prendre en charge les flux de travail parallèles des agents d'intelligence artificielle, cet outil accélère le travail sur plusieurs tâches simultanément.

- ★ 8 444
- Rust
- GitHub Trending · 2026-09-13

## Mises à jour

- **28 septembre 2026:** Étoiles 8,424 → 8,444, dernière version v0.80.0 (27 septembre 2026).
- **27 septembre 2026:** Étoiles 7,964 → 8,424, dernière version v0.79.0 (21 septembre 2026).
- **17 septembre 2026:** Étoiles 7,379 → 7,964, dernière version v0.78.0 (16 septembre 2026).
- **13 septembre 2026:** Étoiles 7,376 → 7,379, dernière version v0.77.0 (8 septembre 2026).

## Ce que ça vous apporte

- Crée facilement des espaces de travail pour exécuter plusieurs tâches simultanément
- Accélère les flux de travail locaux avec des hooks automatiques
- Prend en charge le travail parallèle des agents d'intelligence artificielle

## Installation

**Installation avec Homebrew**

```
brew install worktrunk && wt config shell install
```

**Installation avec Cargo**

```
cargo install worktrunk && wt config shell install
```

## Exécution

**Basculer entre les arbres de travail**

```
wt switch feat
```

**Créer et initialiser un nouvel arbre de travail**

```
wt switch -c -x claude feat
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite créer une nouvelle arborescence de travail dans mon projet Git existant en utilisant Worktrunk et démarrer une tâche parallèle dans cet espace. Comment dois-je utiliser les commandes wt pour gérer les arborescences de travail aussi facilement que les branches, et comment puis-je tirer parti des hooks pour automatiser mon flux de travail ?

## Termes liés du glossaire

- [Worktree](https://trescout.com/fr/dictionary/worktree/)
- [CLI](https://trescout.com/fr/dictionary/cli/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Conçu pour les développeurs travaillant simultanément sur plusieurs tâches logicielles ou agents d'intelligence artificielle.

## Liens

- [Dépôt GitHub →](https://github.com/max-sixty/worktrunk)
- [Lire en turc →](https://trescout.com/discover/worktrunk/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-13 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/worktrunk/
