# Personal trading with artificial intelligence

Vibe-Trading offers a personal trading agent developed for trading in financial markets. The project allows users to manage automatic trading strategies with its Python-based structure.

- ★ 36,114
- Python
- GitHub Trending · 2026-06-04

## Updates

- **October 21, 2026:** Stars 36,012 → 36,114, latest release v0.1.17 (October 21, 2026).
- **October 20, 2026:** Stars 34,287 → 36,012, latest release v0.1.16 (September 29, 2026).
- **September 29, 2026:** Stars 33,083 → 34,287, latest release v0.1.16 (September 29, 2026).
- **September 9, 2026:** Stars 32,899 → 33,083, latest release v0.1.15 (September 9, 2026).

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

Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to trade in the financial markets with the Vibe-Trading agent. Please help me analyze current market data, backtest the strategies I have identified, and manage my brokerage connections securely. Explain step by step how I can configure automated trading processes, specifically determining my trading mandates and risk limits.

Repository: https://github.com/HKUDS/Vibe-Trading. Follow the official instructions in the README of this repository for setup and execution.

Before starting, check which OS we are on and if the necessary tools (e.g., Python, Node.js, Git, Docker) are installed. Install any missing ones step-by-step according to this system.

Create a new, empty folder to work in. Do not touch any files outside this folder and do not delete anything. Tell me what you are going to do in one sentence before running each command.

Tell me what I should see on the screen at the end of each step. If an error occurs, I will paste the error message to you exactly as it is, and we will fix it together.

## Related dictionary terms

- [Trading Agent](https://trescout.com/en/dictionary/trading-agent/)
- [Agent](https://trescout.com/en/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is designed for users who want to develop and manage automatic trading strategies in financial markets.
- **License:** MIT

## Links

- [GitHub repository →](https://github.com/HKUDS/Vibe-Trading)
- [Read in Turkish →](https://trescout.com/discover/vibe-trading/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-04: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. The introductory text was prepared with AI from the repository's own documentation, and this page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/vibe-trading/
