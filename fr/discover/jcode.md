# Framework haute performance pour les agents de codage

Développé avec le langage Rust, jcode offre un cadre pour tester et évaluer les agents d'intelligence artificielle orientés codage. Il fournit une infrastructure standard pour mesurer les performances des agents utilisés dans les processus de développement logiciel.

- ★ 17 227
- Rust
- GitHub Trending · 2026-06-21

## Mise à jour
- 12 août 2026 : Star 16 663 → 17 227, dernière version v0.75.3 (11 août 2026).
- 10 août 2026 : Star 16.653 → 16.663, dernière version v0.75.0 (10 août 2026).
- 10 août 2026 : Star 16.505 → 16.653, dernière version v0.74.0 (10 août 2026).
- 9 août 2026 : Star 16 378 → 16 505, dernière version v0.72.0 (8 août 2026).

## Ce que ça vous apporte
- Haute efficacité des ressources dans les flux de travail multisessions
- Faible utilisation de la mémoire et temps de démarrage rapide
- Infrastructure de test pour les agents d'intelligence artificielle axés sur le codage

## Installation
**Installation MacOS et Linux**

```
curl -fsSL https://raw.githubusercontent.com/1jehuang/jcode/master/scripts/install.sh | bash
```

**Installation avec Homebrew**

```
brew tap 1jehuang/jcode
brew install jcode
```


## Exécution
**Première course avec Ollama**

```
ollama pull llama3.2
jcode login --provider ollama
jcode --provider ollama --model llama3.2 run 'hello'
```


## Si vous ne codez pas
Je souhaite tester les performances et la capacité de gestion multi-sessions de mon agent IA axé sur le codage. Permettez-moi d'optimiser l'utilisation des ressources de mon agent et de mettre en place un environnement de test standard à l'aide du framework jcode.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/jcode/
