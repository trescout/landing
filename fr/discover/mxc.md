# Isolation du système en couches basée sur des politiques avec Rust

Développé par Microsoft, MXC est une solution d'isolation et de confinement en couches basée sur des politiques et écrite en langage Rust. Il est conçu pour limiter en toute sécurité les ressources système et augmenter la sécurité des applications.

- ★ 641
- Rust
- GitHub Trending · 2026-06-07

## Ce que ça vous apporte
- Exécute du code non fiable en toute sécurité dans des environnements isolés.
- Contrôle l’accès aux fichiers, au réseau et aux interfaces avec des politiques basées sur JSON.
- Il propose plusieurs backends d'isolation sur Windows, Linux et macOS.

## Installation
**Compilation sous Linux**

```
./build.sh
```

**Construire sur macOS**

```
./build-mac.sh
```


## Exécution
**Exécuter avec un binaire natif**

```
wxc-exec.exe config.json
```


## Si vous ne codez pas
Je souhaite exécuter un extrait de code non fiable dans un conteneur isolé à l'aide de l'outil MXC développé par Microsoft. Selon la documentation du référentiel GitHub du projet, je dois préparer un fichier de configuration basé sur JSON et utiliser le binaire approprié à ma plateforme. Pouvez-vous créer un exemple de fichier de configuration JSON pour moi qui me permettra d'exécuter un script Python avec un système de fichiers et un accès réseau restreints, et expliquer étape par étape comment exécuter cette configuration avec wxc-exec.exe ?

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/mxc/
