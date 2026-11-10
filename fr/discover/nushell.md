# Interface de ligne de commande proposant des objets structurés

Développé en Rust, nushell propose une nouvelle interface de ligne de commande (shell) qui traite les données sous forme d'objets structurés. Ayant atteint le niveau de produit minimum viable (minimum-viable-product), ce projet est choisi pour un usage quotidien malgré une certaine instabilité potentielle sur certaines commandes.

- ★ 41 079
- Rust
- GitHub Trending · 2026-11-07

## Mises à jour

- **10 novembre 2026:** Étoiles 41,012 → 41,079, dernière version 0.117.0 (10 novembre 2026).
- **7 novembre 2026:** Étoiles 41,011 → 41,012, dernière version 0.116.1 (4 octobre 2026).

## Ce que ça vous apporte

- Traite les données comme des objets structurés.
- Permet un flux de pipeline entre les commandes.
- Charge le contenu des fichiers sous forme de données structurées.

## Installation

**Installation**

```
# Linux and macOS
brew install nushell
# Windows
winget install nushell
```

## Exécution

**Lister les dossiers**

```
ls | where type == "dir" | table
# => ╭────┬──────────┬──────┬─────────┬───────────────╮
# => │ #  │   name   │ type │  size   │   modified    │
# => ├────┼──────────┼──────┼─────────┼───────────────┤
# => │  0 │ .cargo   │ dir  │     0 B │ 9 minutes ago │
# => │  1 │ assets   │ dir  │     0 B │ 2 weeks ago   │
# => │  2 │ crates   │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  3 │ docker   │ dir  │     0 B │ 2 weeks ago   │
# => │  4 │ docs     │ dir  │     0 B │ 2 weeks ago   │
# => │  5 │ images   │ dir  │     0 B │ 2 weeks ago   │
# => │  6 │ pkg_mgrs │ dir  │     0 B │ 2 weeks ago   │
# => │  7 │ samples  │ dir  │     0 B │ 2 weeks ago   │
# => │  8 │ src      │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │  9 │ target   │ dir  │     0 B │ a day ago     │
# => │ 10 │ tests    │ dir  │ 4.0 KiB │ 2 weeks ago   │
# => │ 11 │ wix      │ dir  │     0 B │ 2 weeks ago   │
# => ╰────┴──────────┴──────┴─────────┴───────────────╯
```

## Si vous ne codez pas

Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite installer et utiliser la nouvelle interface de ligne de commande appelée Nushell. Une fois l'installation terminée, aide-moi à exécuter la commande ls | where type == "dir" | table.

Dépôt : https://github.com/nushell/nushell. Base-toi sur les instructions officielles du fichier README de ce dépôt pour l'installation et l'exécution.

Avant de commencer, vérifie quel système d'exploitation nous utilisons et si les outils nécessaires (ex: Python, Node.js, Git, Docker) sont installés. Installe ceux qui manquent étape par étape selon ce système.

Crée un nouveau dossier vide pour travailler. Ne touche pas aux fichiers en dehors de ce dossier et ne supprime rien. Avant chaque commande, décris ce que tu vas faire en une phrase.

Dis-moi ce que je devrais voir à l'écran à la fin de chaque étape. Si une erreur survient, je te copierai le message d'erreur tel quel et nous la corrigerons ensemble.

## Termes liés du glossaire

- [Shell](https://trescout.com/fr/dictionary/shell/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux développeurs qui souhaitent gérer des données sous forme d'objets structurés en ligne de commande.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/nushell/nushell)
- [Lire en turc →](https://trescout.com/discover/nushell/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-11-07 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Le texte de présentation a été préparé avec l’IA à partir de la propre documentation du dépôt et cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/nushell/
