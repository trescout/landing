# Gérez les arbres de travail Git

Worktrunk est une interface de ligne de commande (CLI) écrite en Rust qui simplifie la gestion des arbres de travail (worktree) Git. Développé spécifiquement pour prendre en charge les flux de travail parallèles des agents d'intelligence artificielle, cet outil accélère le travail sur plusieurs tâches simultanément.

- ★ 7 379
- Rust
- GitHub Trending · 2026-09-13

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
Je souhaite créer une nouvelle arborescence de travail dans mon projet Git existant en utilisant Worktrunk et démarrer une tâche parallèle dans cet espace. Comment dois-je utiliser les commandes wt pour gérer les arborescences de travail aussi facilement que les branches, et comment puis-je tirer parti des hooks pour automatiser mon flux de travail ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/worktrunk/
