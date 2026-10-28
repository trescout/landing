# Agent de codage IA pour terminal

DeepSeek-Reasonix est un agent de codage d'IA qui s'exécute sur le terminal et est basé sur les modèles DeepSeek. En se concentrant sur la stabilité du cache de préfixes, cet outil garantit aux développeurs une prise en charge ininterrompue du codage pendant de longues sessions.

- ★ 35 979
- Go
- GitHub Trending · 2026-08-03

## Mises à jour

- **28 octobre 2026:** Étoiles 35,978 → 35,979, dernière version studio-v2.54.0 (28 octobre 2026).
- **27 octobre 2026:** Étoiles 35,965 → 35,978, dernière version studio-v2.53.1 (27 octobre 2026).
- **26 octobre 2026:** Étoiles 35,956 → 35,965, dernière version studio-v2.52.0 (26 octobre 2026).
- **25 octobre 2026:** Étoiles 35,946 → 35,956, dernière version studio-v2.51.0 (24 octobre 2026).

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

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Tout en travaillant avec cet agent de codage d'intelligence artificielle exécuté sur le terminal, développer des suggestions de code en tenant compte de la structure actuelle et des objectifs de mon projet. Concentrez-vous sur la production de réponses cohérentes et peu coûteuses au cours de nos longues sessions grâce à la stabilité du cache de préfixes. Lors de l'écriture ou du débogage de code, fournissez des solutions modulaires et propres qui répondent aux besoins du projet.

Dépôt : https://github.com/esengine/DeepSeek-Reasonix. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs de logiciels travaillant dans un environnement de terminal qui souhaitent automatiser leurs processus de codage et bénéficier du soutien de l'intelligence artificielle dans leurs projets à long terme.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/esengine/DeepSeek-Reasonix)
- [Lire en turc →](https://trescout.com/discover/deepseek-reasonix/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-03 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/deepseek-reasonix/
