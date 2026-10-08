# Trading personnel avec intelligence artificielle

Vibe-Trading propose un agent de trading personnel développé pour le trading sur les marchés financiers. Le projet permet aux utilisateurs de gérer des stratégies de trading automatique grâce à sa structure basée sur Python.

- ★ 34 287
- Python
- GitHub Trending · 2026-06-04

## Mises à jour

- **29 septembre 2026:** Étoiles 33,083 → 34,287, dernière version v0.1.16 (29 septembre 2026).
- **9 septembre 2026:** Étoiles 32,899 → 33,083, dernière version v0.1.15 (9 septembre 2026).
- **7 septembre 2026:** Étoiles 31,295 → 32,899, dernière version v0.1.14 (20 août 2026).
- **20 août 2026:** Étoiles 30,558 → 31,295, dernière version v0.1.14 (20 août 2026).

## Ce que ça vous apporte

- Gestion de stratégie automatisée avec agent commercial personnel.
- Accès aux données de marché avec support multi-courtage.
- Autorisation de transaction et registre d'audit axés sur la sécurité.

## Installation

**Installation directe**

```
pip install vibe-trading-ai
```

**Configuration de l'environnement du développeur**

```
git clone https://github.com/HKUDS/Vibe-Trading.git
cd Vibe-Trading
python -m venv .venv

# Activate
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\Activate.ps1       # Windows PowerShell

pip install -e .
cp agent/.env.example agent/.env   # Edit — set your LLM provider API key
vibe-trading                       # Launch interactive TUI
```

## Exécution

**Recherche avec le langage naturel**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Test de stratégie**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite négocier sur les marchés financiers avec l'agent Vibe-Trading. S'il vous plaît, aidez-moi à analyser les données actuelles du marché, à tester les stratégies que j'ai identifiées et à gérer mes connexions de courtage en toute sécurité. Expliquez étape par étape comment configurer des processus de trading automatisés, en déterminant spécifiquement mes mandats de trading et mes limites de risque.

## Termes liés du glossaire

- [Trading Agent](https://trescout.com/fr/dictionary/trading-agent/)
- [Agent](https://trescout.com/fr/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il est conçu pour les utilisateurs qui souhaitent développer et gérer des stratégies de trading automatique sur les marchés financiers.
- **Licence:** MIT

## Liens

- [Dépôt GitHub →](https://github.com/HKUDS/Vibe-Trading)
- [Lire en turc →](https://trescout.com/discover/vibe-trading/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-04 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vibe-trading/
