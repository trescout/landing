# Framework haute performance pour les agents de codage

Développé avec le langage Rust, jcode offre un cadre pour tester et évaluer les agents d'intelligence artificielle orientés codage. Il fournit une infrastructure standard pour mesurer les performances des agents utilisés dans les processus de développement logiciel.

- ★ 16 378
- Rust
- GitHub Trending · 2026-06-21

## Mise à jour
- 8 août 2026 : Star 16.118 → 16.378, dernière version v0.71.1 (8 août 2026).
- 6 août 2026 : Star 15 647 → 16 118, dernière version v0.68.0 (5 août 2026).
- 4 août 2026 : Star 15 183 → 15 647, dernière version v0.67.1 (3 août 2026).
- 2 août 2026 : Star 7 450 → 15 183, dernière version v0.65.0 (2 août 2026).

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
