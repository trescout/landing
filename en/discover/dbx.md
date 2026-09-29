# Lightweight database client

Developed in Rust, dbx offers a lightweight database client of 25 MB that supports over 100 database types. Along with a desktop application, command-line interface (CLI), and Docker support, it includes features such as a built-in AI assistant and Model Context Protocol (MCP).

- ★ 21,621
- Rust
- GitHub Trending · 2026-09-29

## What you get
- Supports over a hundred database types.
- Works with desktop, Docker, and command line.
- Includes an AI assistant and Model Context Protocol.

## Installation
**Desktop Application Installation**

```
brew install --cask dbx
```

**Command Line Tool Installation**

```
npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json
```


## Running it
**Running with Docker**

```
# The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest
```


## If you don't write code
Follow the necessary steps to install and run the dbx application. For the desktop app, use the brew install --cask dbx command, and for the command line interface, use the npm install -g @dbx-app/cli
# or via Homebrew
brew tap t8y2/tap && brew install dbx-cli
dbx agent setup
dbx connections list --json
dbx query local "select 1" --json commands. If you want to run it with Docker, run the # The default keeps the key in the persistent /app/data volume.
docker run -d --pull=always --name dbx -p 4224:4224 \
  -v dbx-data:/app/data \
  t8y2/dbx:latest command.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/dbx/
