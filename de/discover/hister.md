# Privater Suchmotor für persönliche Seiten und Dateien

Indiziert lokal besuchte Webseiten und gespeicherte Dateien und bietet Volltextsuche sowie erweiterte Abfragefilter. Optionales semantisches Suchen sendet Dokumenttext an die gewählte Embeddings-Endpoint.

- ★ 5.740
- Go
- GitHub Trending · 2026-08-25

## Aktualisierungen

- **27. September 2026:** Sterne 4,602 → 5,740, neueste Version v0.20.0 (24. September 2026).
- **18. September 2026:** Sterne 3,574 → 4,602, neueste Version v0.19.0 (3. September 2026).
- **4. September 2026:** Sterne 3,100 → 3,574, neueste Version v0.19.0 (3. September 2026).
- **27. August 2026:** Sterne 2,620 → 3,100, neueste Version v0.18.0 (23. August 2026).

## Installation

**Binary ausführbar machen**

```
chmod +x hister
```

## Ausführung

**Hister-Server starten**

```
./hister listen
```

**Auf die lokale Benutzeroberfläche zugreifen**

```
http://127.0.0.1:4433
```

## Was macht dieses Werkzeug?

Hister kann lokal oder auf von Ihnen kontrollierter Infrastruktur betrieben werden; ein Cloud-Service oder Telemetrie sind nicht zwingend erforderlich. Mit Chrome- und Firefox-Erweiterungen indiziert es Seiten, bietet Website-Crawling und das Importieren des Browserverlaufs. Wenn semantische Suche aktiviert ist, wird Dokumenttext an die ausgewählte Embeddings-Schnittstelle gesendet.

## Für wen ist es?

Nutzer, die Webseiten und persönliche Dateien in einer von ihnen kontrollierten Suchinfrastruktur durchsuchen möchten.

## Was Sie nicht erwarten sollten

Szenarien, die zwingend Cloud-Dienste oder Telemetrie erfordern, oder Browserverläufe/Indexing-Flows, bei denen das Senden von Inhalten an einen konfigurierten Hister-Server nicht erlaubt ist.

## Höhepunkte

- Betrieb lokal oder auf kontrollierter Infrastruktur ohne Telemetrie und verpflichtende Cloud-Dienste
- Volltextsuche mit Feldfiltern, Phrasen, Wildcards, Negation und Priorisierungen
- Web-, Terminal-, TUI-, CLI- und MCP-Clients sowie optionale semantische Suche

## Ablauf für die erste Nutzung

1. Die passende Binärdatei für Ihre Plattform herunterladen und unter Linux/macOS ausführbar machen
2. Den Hister-Server im lokalen Listen-Modus starten
3. Die lokale Weboberfläche öffnen
4. Die Chrome- oder Firefox-Erweiterung installieren und die zu indexierenden Seiten auswählen

## Sicherer Start

Die Browser-Erweiterung sendet Seiteninhalte (abgesehen von Favicon-Downloads) an den konfigurierten Hister-Server. Optionale semantische Suche übermittelt Dokumenttext an die gewählte Embeddings-Endpoint.

## Erster Prompt

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Öffne die lokale Oberfläche, indiziere mit der Browser-Erweiterung ausgewählte Seiten und verifiziere Suchen mit Abfragefiltern.

## Verwandte Begriffe aus dem Glossar

- [TUI](https://trescout.com/de/dictionary/tui/)
- [Binary](https://trescout.com/de/dictionary/binary/)
- [MCP](https://trescout.com/de/dictionary/mcp/)
- [Terminal](https://trescout.com/de/dictionary/terminal/)
- [CLI](https://trescout.com/de/dictionary/cli/)

## Links

- [GitHub-Repository →](https://github.com/asciimoo/hister)
- [Schnellstart →](https://hister.org/docs/quickstart)
- [README zu Datenschutz und Nutzung →](https://github.com/asciimoo/hister)
- [Nutzungsablauf →](https://hister.org/posts/how-i-use-hister)
- [Auf Türkisch lesen →](https://trescout.com/discover/hister/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-25 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/hister/
