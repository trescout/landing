# Sicherheitsaudit für Ihre KI-Infrastruktur

AI-Infra-Guard ist eine End-to-End-KI-Red-Team-Plattform, die Agenten, Fähigkeiten, MCP und KI-Infrastruktur scannt und LLM-Jailbreak-Bewertungen durchführt.

- ★ 6.935
- Python
- GitHub Trending · 2026-08-20

## Aktualisierungen

- **22. Oktober 2026:** Sterne 6,878 → 6,935, neueste Version v4.6.7 (22. Oktober 2026).
- **15. Oktober 2026:** Sterne 6,788 → 6,878, neueste Version v4.6.6 (15. Oktober 2026).
- **8. Oktober 2026:** Sterne 6,650 → 6,788, neueste Version v4.6.5 (8. Oktober 2026).
- **1. Oktober 2026:** Sterne 6,595 → 6,650, neueste Version v4.6.4 (1. Oktober 2026).

## Was es bringt

- Scannt nach Schwachstellen in Systemen der künstlichen Intelligenz.
- Analysiert Agentenfunktionen und Modellsicherheit.
- Bietet Schutz vor Jailbreak-Angriffen.

## Installation

**Schnelle Installation mit Docker**

```
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
# For Docker Compose V2+, replace 'docker-compose' with 'docker compose'
docker-compose -f docker-compose.images.yml up -d
```

**Automatische Installation mit einem Befehl**

```
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/refs/heads/main/docker.sh | bash
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Wie kann ich mithilfe der AI-Infra-Guard-Plattform Schwachstellen in meiner Infrastruktur für künstliche Intelligenz erkennen? Erklären Sie die Schritte, die ich befolgen muss, um die Skill-Scanning- und Jailbreak-Bewertungsprozesse zu starten, insbesondere in agentenbasierten Systemen.

Repository: https://github.com/Tencent/AI-Infra-Guard. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Jailbreak](https://trescout.com/de/dictionary/jailbreak/)
- [MCP](https://trescout.com/de/dictionary/mcp/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Softwareentwickler und Sicherheitsexperten, die Modelle der künstlichen Intelligenz und agentenbasierte Systeme entwickeln und die Infrastruktursicherheit proaktiv überwachen möchten.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/Tencent/AI-Infra-Guard)
- [Auf Türkisch lesen →](https://trescout.com/discover/ai-infra-guard/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-20 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

## Redaktioneller Hinweis

Security note: Use only against AI services, agent/MCP servers, and network targets you own or are explicitly authorized to test. Do not run probes or jailbreak test sets against public targets; protect API keys and results. Keep the WebUI on localhost or behind access control.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ai-infra-guard/
