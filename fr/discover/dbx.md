# Client de base de données léger

Développé en Rust, dbx propose un client de base de données léger de 25 Mo prenant en charge plus de 100 types de bases de données. En plus d'une application de bureau, d'une interface en ligne de commande (CLI) et de la prise en charge de Docker, il intègre des fonctionnalités telles qu'un assistant IA et le Model Context Protocol (MCP).

- ★ 25 183
- Rust
- GitHub Trending · 2026-09-29

## Mises à jour

- **8 octobre 2026:** Étoiles 24,988 → 25,183, dernière version v0.6.36 (8 octobre 2026).
- **7 octobre 2026:** Étoiles 24,669 → 24,988, dernière version v0.6.35 (6 octobre 2026).
- **5 octobre 2026:** Étoiles 24,470 → 24,669, dernière version v0.6.34 (4 octobre 2026).
- **4 octobre 2026:** Étoiles 24,157 → 24,470, dernière version v0.6.33 (4 octobre 2026).

## Ce que ça vous apporte

- Prend en charge plus d'une centaine de types de bases de données.
- Fonctionne sur bureau, avec Docker et en ligne de commande.
- Inclut un assistant IA et le Model Context Protocol.

## Installation

**Installation de l'application de bureau**

```
brew install --cask dbx
```

**Installation de l'outil de ligne de commande**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```

## Exécution

**Exécuter avec Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Suivez les étapes nécessaires pour installer et exécuter l'application dbx. Utilisez la commande brew install --cask dbx pour l'application de bureau, et npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json pour l'outil en ligne de commande. Si vous souhaitez l'exécuter avec Docker, exécutez la commande # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
-v dbx-data:/app/data \
t8y2/dbx:latest

## Termes liés du glossaire

- [Database Client](https://trescout.com/fr/dictionary/database-client/)
- [Local](https://trescout.com/fr/dictionary/local/)
- [Database](https://trescout.com/fr/dictionary/database/)
- [MCP](https://trescout.com/fr/dictionary/mcp/)
- [Agent](https://trescout.com/fr/dictionary/agent/)
- [CLI](https://trescout.com/fr/dictionary/cli/)

- **Pour qui:** Destiné aux développeurs qui souhaitent gérer différents types de bases de données avec une interface légère et une assistance par IA.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/t8y2/dbx)
- [Lire en turc →](https://trescout.com/discover/dbx/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-09-29 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/dbx/
