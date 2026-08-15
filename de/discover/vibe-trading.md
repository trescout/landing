# Persönlicher Handel mit künstlicher Intelligenz

Vibe-Trading bietet einen persönlichen Handelsagenten, der für den Handel auf Finanzmärkten entwickelt wurde. Das Projekt ermöglicht Benutzern mit seiner Python-basierten Struktur die Verwaltung automatischer Handelsstrategien.

- ★ 30.558
- Python
- GitHub Trending · 2026-06-04

## Was es bringt
- Automatisiertes Strategiemanagement mit persönlichem Handelsagenten.
- Zugriff auf Marktdaten mit Multi-Brokerage-Unterstützung.
- Sicherheitsorientierte Transaktionsautorisierung und Audit-Ledger.

## Installation
**Direkte Installation**

```
pip install vibe-trading-ai
```

**Einrichtung der Entwicklerumgebung**

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


## Ausführung
**Forschung mit natürlicher Sprache**

```
vibe-trading run -p "Backtest a BTC-USDT 20/50 moving-average strategy for 2024, summarize return and drawdown, then export the report"
```

**Strategietest**

```
vibe-trading alpha bench --zoo gtja191 --universe csi300 --period 2018-2025 --top 20
```


## Wenn Sie nicht programmieren
Ich möchte mit dem Vibe-Trading-Agenten auf den Finanzmärkten handeln. Bitte helfen Sie mir, aktuelle Marktdaten zu analysieren, die von mir identifizierten Strategien erneut zu testen und meine Brokerage-Verbindungen sicher zu verwalten. Erklären Sie Schritt für Schritt, wie ich automatisierte Handelsprozesse konfigurieren und dabei konkret meine Handelsmandate und Risikolimits festlegen kann.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vibe-trading/
