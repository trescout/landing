# Client de base de données léger

Développé en Rust, dbx propose un client de base de données léger de 25 Mo prenant en charge plus de 100 types de bases de données. En plus d'une application de bureau, d'une interface en ligne de commande (CLI) et de la prise en charge de Docker, il intègre des fonctionnalités telles qu'un assistant IA et le Model Context Protocol (MCP).

- ★ 24 157
- Rust
- GitHub Trending · 2026-09-29

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

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/dbx/
