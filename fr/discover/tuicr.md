# Révision du code avec Vim dans le terminal

Développé avec le langage Rust, tuicr est un outil de révision de code basé sur une interface utilisateur de terminal qui prend en charge les raccourcis clavier de Vim. Il permet aux développeurs de gérer leur processus de révision de code directement depuis le terminal.

- ★ 3 221
- Rust
- GitHub Trending · 2026-07-31

## Mises à jour

- **27 septembre 2026:** Étoiles 3,132 → 3,221, dernière version v0.27.0 (23 septembre 2026).
- **16 septembre 2026:** Étoiles 3,009 → 3,132, dernière version v0.26.0 (15 septembre 2026).
- **3 septembre 2026:** Étoiles 2,908 → 3,009, dernière version v0.25.0 (2 septembre 2026).
- **27 août 2026:** Étoiles 2,817 → 2,908, dernière version v0.24.0 (25 août 2026).

## Ce que ça vous apporte

- Révision rapide du code dans le terminal avec les raccourcis Vim
- Publiez des commentaires directement sur GitHub et GitLab
- Prise en charge de la sortie structurée pour les outils d'IA

## Installation

**Installation standard**

```
curl -fsSL tuicr.dev/install.sh | sh
# or
brew install agavra/tap/tuicr
```

**Gestionnaires de paquets alternatifs**

```
# Cargo
cargo install tuicr

# Mise
mise use github:agavra/tuicr

# Nix
nix run github:agavra/tuicr
```

## Exécution

**Examiner les changements locaux**

```
tuicr -w
```

**Examiner un PR spécifique**

```
tuicr pr 125
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Passez en revue cette révision de code et préparez une liste structurée de tous les bogues ou suggestions d'amélioration que vous trouvez, chaque commentaire étant identifié par le chemin du fichier et le numéro de ligne. Lors de la révision, fournissez des suggestions concrètes qui augmenteront la lisibilité et les performances du code, sur la base des données au format markdown que j'ai copiées depuis tuicr.

## Termes liés du glossaire

- [Code Review](https://trescout.com/fr/dictionary/code-review/)
- [User Interface](https://trescout.com/fr/dictionary/user-interface/)
- [Markdown](https://trescout.com/fr/dictionary/markdown/)
- [Terminal](https://trescout.com/fr/dictionary/terminal/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent gérer leurs processus de révision de code avec des raccourcis Vim sans quitter le terminal.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/agavra/tuicr)
- [Lire en turc →](https://trescout.com/discover/tuicr/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-07-31 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/tuicr/
