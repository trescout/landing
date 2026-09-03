# Agent de codage IA pour terminal

DeepSeek-Reasonix est un agent de codage d'IA qui s'exécute sur le terminal et est basé sur les modèles DeepSeek. En se concentrant sur la stabilité du cache de préfixes, cet outil garantit aux développeurs une prise en charge ininterrompue du codage pendant de longues sessions.

- ★ 35 364
- Go
- GitHub Trending · 2026-08-03

## Ce que ça vous apporte
- Fournit une prise en charge ininterrompue à long terme du codage avec les modèles DeepSeek.
- Il offre une gestion de session à faible coût grâce à sa fonction de mise en cache des préfixes.
- Il offre une utilisation flexible via le terminal avec prise en charge des plug-ins configurables.

## Installation
**Installation via NPM ou Homebrew**

```
npm i -g reasonix                  # any OS; pulls the prebuilt native binary
brew install esengine/reasonix/reasonix   # macOS
```

**Compilation à partir du code source**

```
git clone https://github.com/esengine/DeepSeek-Reasonix.git
cd DeepSeek-Reasonix
make build      # -> bin/reasonix(.exe)
make cross      # -> dist/ (darwin|linux|windows × amd64|arm64)
```


## Exécution
**Configuration et initialisation**

```
reasonix setup                      # configure a provider and model
reasonix                            # start an interactive session
reasonix run "implement the TODOs in main.go"
```


## Si vous ne codez pas
Tout en travaillant avec cet agent de codage d'intelligence artificielle exécuté sur le terminal, développer des suggestions de code en tenant compte de la structure actuelle et des objectifs de mon projet. Concentrez-vous sur la production de réponses cohérentes et peu coûteuses au cours de nos longues sessions grâce à la stabilité du cache de préfixes. Lors de l'écriture ou du débogage de code, fournissez des solutions modulaires et propres qui répondent aux besoins du projet.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deepseek-reasonix/
