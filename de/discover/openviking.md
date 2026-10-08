# Dateisystemspeicher für Agenten der künstlichen Intelligenz

OpenViking wurde von Volcengine entwickelt und bietet eine sich selbst verbessernde Kontextdatenbank für KI-Agenten. Dieses System vereint Agentenspeicher, Information Retrieval (RAG)-Prozesse und -Fähigkeiten unter einem Dach.

- ★ 39.151
- Python
- GitHub Trending · 2026-08-18

## Aktualisierungen

- **3. Oktober 2026:** Sterne 38,859 → 39,151, neueste Version v0.4.23 (2. Oktober 2026).
- **28. September 2026:** Sterne 38,733 → 38,859, neueste Version v0.4.22 (28. September 2026).
- **27. September 2026:** Sterne 37,128 → 38,733, neueste Version v0.4.21 (20. September 2026).
- **14. September 2026:** Sterne 36,182 → 37,128, neueste Version v0.4.20 (14. September 2026).

## Was es bringt

- Organisiert Informationen hierarchisch wie ein Dateisystem.
- Es reduziert die Kosten für künstliche Intelligenz durch mehrschichtiges Laden.
- Macht den Agentenverlauf nachvollziehbar und debuggbar.

## Installation

**Serverinstallation und -start**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```

## Ausführung

**Starten Sie einen Chat mit dem Bot-Support**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Erstellen Sie mithilfe der OpenViking-Datenbank ein Kontextmanagement für einen Agenten für künstliche Intelligenz. Es strukturiert die Informationen über das viking://-Protokoll, indem es die Informationen in L0-Zusammenfassungs-, L1-Übersichts- und L2-Detailschichten unterteilt. Indem der Speicher, die Ressourcen und die Fähigkeiten des Agenten in diesem virtuellen Dateisystem platziert werden, kann er während der Abfrage durch Verzeichnisse navigieren und durch Lernen aus vergangenen Sitzungen ein Langzeitgedächtnis erstellen.

## Verwandte Begriffe aus dem Glossar

- [RAG](https://trescout.com/de/dictionary/rag/)
- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler, die die Speicherverwaltung, Informationsabrufprozesse und Fähigkeiten von KI-Agenten in einem organisierten System kombinieren möchten.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/volcengine/OpenViking)
- [Auf Türkisch lesen →](https://trescout.com/discover/openviking/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-18 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openviking/
