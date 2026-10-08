# Personal trading with artificial intelligence

Vibe-Trading offers a personal trading agent developed for trading in financial markets. The project allows users to manage automatic trading strategies with its Python-based structure.

- ★ 34,287
- Python
- GitHub Trending · 2026-06-04

## Updates

- **September 29, 2026:** Stars 33,083 → 34,287, latest release v0.1.16 (September 29, 2026).
- **September 9, 2026:** Stars 32,899 → 33,083, latest release v0.1.15 (September 9, 2026).
- **September 7, 2026:** Stars 31,295 → 32,899, latest release v0.1.14 (August 20, 2026).
- **August 20, 2026:** Stars 30,558 → 31,295, latest release v0.1.14 (August 20, 2026).

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to trade in the financial markets with the Vibe-Trading agent. Please help me analyze current market data, backtest the strategies I have identified, and manage my brokerage connections securely. Explain step by step how I can configure automated trading processes, specifically determining my trading mandates and risk limits.

## Related dictionary terms

- [Trading Agent](https://trescout.com/en/dictionary/trading-agent/)
- [Agent](https://trescout.com/en/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is designed for users who want to develop and manage automatic trading strategies in financial markets.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/HKUDS/Vibe-Trading)
- [Read in Turkish →](https://trescout.com/discover/vibe-trading/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-04: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/vibe-trading/
