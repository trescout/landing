# Dateisystemspeicher für Agenten der künstlichen Intelligenz

OpenViking wurde von Volcengine entwickelt und bietet eine sich selbst verbessernde Kontextdatenbank für KI-Agenten. Dieses System vereint Agentenspeicher, Information Retrieval (RAG)-Prozesse und -Fähigkeiten unter einem Dach.

- ★ 29.066
- Python
- GitHub Trending · 2026-08-18

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
Erstellen Sie mithilfe der OpenViking-Datenbank ein Kontextmanagement für einen Agenten für künstliche Intelligenz. Es strukturiert die Informationen über das viking://-Protokoll, indem es die Informationen in L0-Zusammenfassungs-, L1-Übersichts- und L2-Detailschichten unterteilt. Indem der Speicher, die Ressourcen und die Fähigkeiten des Agenten in diesem virtuellen Dateisystem platziert werden, kann er während der Abfrage durch Verzeichnisse navigieren und durch Lernen aus vergangenen Sitzungen ein Langzeitgedächtnis erstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openviking/
