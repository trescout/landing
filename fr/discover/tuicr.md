# Révision du code avec Vim dans le terminal

Développé avec le langage Rust, tuicr est un outil de révision de code basé sur une interface utilisateur de terminal qui prend en charge les raccourcis clavier de Vim. Il permet aux développeurs de gérer leur processus de révision de code directement depuis le terminal.

- ★ 2 908
- Rust
- GitHub Trending · 2026-07-31

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
Passez en revue cette révision de code et préparez une liste structurée de tous les bogues ou suggestions d'amélioration que vous trouvez, chaque commentaire étant identifié par le chemin du fichier et le numéro de ligne. Lors de la révision, fournissez des suggestions concrètes qui augmenteront la lisibilité et les performances du code, sur la base des données au format markdown que j'ai copiées depuis tuicr.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/tuicr/
