# Trading personnel avec intelligence artificielle

Vibe-Trading propose un agent de trading personnel développé pour le trading sur les marchés financiers. Le projet permet aux utilisateurs de gérer des stratégies de trading automatique grâce à sa structure basée sur Python.

- ★ 29 309
- Python
- GitHub Trending · 2026-06-04

## Mise à jour
- 2 août 2026 : Star 10 343 → 29 309, dernière version v0.1.12 (22 juillet 2026).

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
Je souhaite négocier sur les marchés financiers avec l'agent Vibe-Trading. S'il vous plaît, aidez-moi à analyser les données actuelles du marché, à tester les stratégies que j'ai identifiées et à gérer mes connexions de courtage en toute sécurité. Expliquez étape par étape comment configurer des processus de trading automatisés, en déterminant spécifiquement mes mandats de trading et mes limites de risque.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vibe-trading/
