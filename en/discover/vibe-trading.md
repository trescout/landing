# Personal trading with artificial intelligence

Vibe-Trading offers a personal trading agent developed for trading in financial markets. The project allows users to manage automatic trading strategies with its Python-based structure.

- ★ 29,309
- Python
- GitHub Trending · 2026-06-04

## Update
- August 2, 2026: Star 10,343 → 29,309, latest version v0.1.12 (July 22, 2026).

## What you get
- Automated strategy management with personal trading agent.
- Access to market data with multi-brokerage support.
- Security-oriented transaction authorization and audit ledger.

## Installation
**Direct Installation**

```
pip install vibe-trading-ai
```

**Developer Environment Setup**

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


## Running it
**Research with Natural Language**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Strategy Test**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```


## If you don't write code
I want to trade in the financial markets with the Vibe-Trading agent. Please help me analyze current market data, backtest the strategies I have identified, and manage my brokerage connections securely. Explain step by step how I can configure automated trading processes, specifically determining my trading mandates and risk limits.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/vibe-trading/
