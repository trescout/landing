# Routeur qui gère le trafic de l'intelligence artificielle

Développé par NVIDIA, Switchyard est un moteur d'inférence d'intelligence artificielle hautes performances écrit en langage Rust. Il offre un environnement d'exécution optimisé pour exécuter efficacement des modèles de langage étendus (LLM) sur différentes infrastructures matérielles.

- ★ 3 227
- Rust
- GitHub Trending · 2026-08-13

## Mises à jour

- **27 septembre 2026:** Étoiles 2,617 → 3,227, dernière version v0.3.0 (22 septembre 2026).
- **31 août 2026:** Étoiles 1,566 → 2,617, dernière version v0.2.0 (10 août 2026).
- **15 août 2026:** Étoiles 923 → 1,566, dernière version v0.2.0 (10 août 2026).

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

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Agissez comme un routeur de trafic IA pour moi. En utilisant Switchyard, je souhaite que vous répartissiez les requêtes de mes agents de codage comme Claude Code ou Codex entre différents modèles, traduisiez automatiquement entre les formats OpenAI et Anthropic API et surveilliez toutes les métriques opérationnelles. Gérez les demandes entrantes avec des algorithmes de routage structurés et effectuez des tests A/B ou un équilibrage de charge entre différents modèles si nécessaire.

## Termes liés du glossaire

- [Inference](https://trescout.com/fr/dictionary/inference/)
- [Runtime](https://trescout.com/fr/dictionary/runtime/)
- [LLM](https://trescout.com/fr/dictionary/llm/)
- [Rust](https://trescout.com/fr/dictionary/rust/)
- [API](https://trescout.com/fr/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il s'adresse aux développeurs qui souhaitent gérer efficacement de grands modèles de langage sur différents fournisseurs de matériel et de services.
- **Licence:** Apache-2.0

## Liens

- [Dépôt GitHub →](https://github.com/NVIDIA-NeMo/Switchyard)
- [Lire en turc →](https://trescout.com/discover/switchyard/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-08-13 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/switchyard/
