# Routeur qui gère le trafic de l'intelligence artificielle

Développé par NVIDIA, Switchyard est un moteur d'inférence d'intelligence artificielle hautes performances écrit en langage Rust. Il offre un environnement d'exécution optimisé pour exécuter efficacement des modèles de langage étendus (LLM) sur différentes infrastructures matérielles.

- ★ 1 566
- Rust
- GitHub Trending · 2026-08-13

## Ce que ça vous apporte
- Acheminer le trafic entre différents modèles d’intelligence artificielle
- Traduction entre les formats OpenAI et Anthropic API
- Suivez les métriques de transactions et les journaux d’erreurs

## Installation
**Installation en tant qu'outil de ligne de commande**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Installation en tant que serveur**

```
cargo install --locked switchyard-server
switchyard-server --help
```


## Exécution
**Vérifier l'état du serveur**

```
curl http://localhost:4000/health
```


## Si vous ne codez pas
Agissez comme un routeur de trafic IA pour moi. En utilisant Switchyard, je souhaite que vous répartissiez les requêtes de mes agents de codage comme Claude Code ou Codex entre différents modèles, traduisiez automatiquement entre les formats OpenAI et Anthropic API et surveilliez toutes les métriques opérationnelles. Gérez les demandes entrantes avec des algorithmes de routage structurés et effectuez des tests A/B ou un équilibrage de charge entre différents modèles si nécessaire.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/switchyard/
