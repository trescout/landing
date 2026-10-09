# Agent de codage IA pour terminal

DeepSeek-Reasonix est un agent de codage d'IA qui s'exécute sur le terminal et est basé sur les modèles DeepSeek. En se concentrant sur la stabilité du cache de préfixes, cet outil garantit aux développeurs une prise en charge ininterrompue du codage pendant de longues sessions.

- ★ 35 752
- Go
- GitHub Trending · 2026-08-03

## Mises à jour

- **9 octobre 2026:** Étoiles 35,747 → 35,752, dernière version studio-v2.33.0 (9 octobre 2026).
- **8 octobre 2026:** Étoiles 35,747 → 35,747, dernière version studio-v2.32.0 (8 octobre 2026).
- **8 octobre 2026:** Étoiles 35,744 → 35,747, dernière version studio-v2.31.0 (8 octobre 2026).
- **7 octobre 2026:** Étoiles 35,742 → 35,744, dernière version studio-v2.30.0 (7 octobre 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Tout en travaillant avec cet agent de codage d'intelligence artificielle exécuté sur le terminal, développer des suggestions de code en tenant compte de la structure actuelle et des objectifs de mon projet. Concentrez-vous sur la production de réponses cohérentes et peu coûteuses au cours de nos longues sessions grâce à la stabilité du cache de préfixes. Lors de l'écriture ou du débogage de code, fournissez des solutions modulaires et propres qui répondent aux besoins du projet.

## Termes liés du glossaire

- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels travaillant dans un environnement de terminal qui souhaitent automatiser leurs processus de codage et bénéficier du soutien de l'intelligence artificielle dans leurs projets à long terme.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/esengine/DeepSeek-Reasonix)
- [Lire en turc →](https://trescout.com/discover/deepseek-reasonix/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deepseek-reasonix/
