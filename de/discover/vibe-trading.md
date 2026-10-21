# Persönlicher Handel mit künstlicher Intelligenz

Vibe-Trading bietet einen persönlichen Handelsagenten, der für den Handel auf Finanzmärkten entwickelt wurde. Das Projekt ermöglicht Benutzern mit seiner Python-basierten Struktur die Verwaltung automatischer Handelsstrategien.

- ★ 36.114
- Python
- GitHub Trending · 2026-06-04

## Aktualisierungen

- **21. Oktober 2026:** Sterne 36,012 → 36,114, neueste Version v0.1.17 (21. Oktober 2026).
- **20. Oktober 2026:** Sterne 34,287 → 36,012, neueste Version v0.1.16 (29. September 2026).
- **29. September 2026:** Sterne 33,083 → 34,287, neueste Version v0.1.16 (29. September 2026).
- **9. September 2026:** Sterne 32,899 → 33,083, neueste Version v0.1.15 (9. September 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit dem Vibe-Trading-Agenten auf den Finanzmärkten handeln. Bitte helfen Sie mir, aktuelle Marktdaten zu analysieren, die von mir identifizierten Strategien erneut zu testen und meine Brokerage-Verbindungen sicher zu verwalten. Erklären Sie Schritt für Schritt, wie ich automatisierte Handelsprozesse konfigurieren und dabei konkret meine Handelsmandate und Risikolimits festlegen kann.

Repository: https://github.com/HKUDS/Vibe-Trading. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Trading Agent](https://trescout.com/de/dictionary/trading-agent/)
- [Agent](https://trescout.com/de/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Benutzer, die automatische Handelsstrategien auf den Finanzmärkten entwickeln und verwalten möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/HKUDS/Vibe-Trading)
- [Auf Türkisch lesen →](https://trescout.com/discover/vibe-trading/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-04 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vibe-trading/
