# Kombinieren Sie 34 kostenlose LLM-Anbieter in einer API

FreeLLMAPI bietet intelligentes Routing und Fehlertoleranz, indem es 34 verschiedene kostenlose Anbieter wichtiger Sprachmodelle in einer einzigen REST-API im OpenAI-Format zusammenfasst.

- ★ 31.427
- TypeScript
- GitHub Trending · 2026-08-28

## Aktualisierungen

- **7. Oktober 2026:** Sterne 30,274 → 31,427, neueste Version v0.13.6 (7. Oktober 2026).
- **3. Oktober 2026:** Sterne 29,808 → 30,274, neueste Version v0.13.4 (3. Oktober 2026).
- **1. Oktober 2026:** Sterne 29,534 → 29,808, neueste Version v0.13.3 (30. September 2026).
- **29. September 2026:** Sterne 29,054 → 29,534, neueste Version v0.13.2 (29. September 2026).

## Was es bringt

- 34 kostenlose Modellanbieter: One-Stop-Zugriff auf Dutzende kostenloser Anbieter, darunter Google Gemini, Groq, Cloudflare Workers AI und HuggingFace.
- OpenAI-REST-API-Kompatibilität: Dank des Endpunkts /v1/chat/completions können Sie mit LangChain, LlamaIndex und vorhandenen KI-Anwendungen arbeiten, ohne den Code zu ändern.
- Intelligentes Routing und Fehlerbehebung: Wechseln Sie automatisch zu einem alternativen Anbieter, wenn ein Anbieter das Tariflimit erreicht oder ausfällt.
- Unterstützung für Streaming (vom Server gesendete Ereignisse): Möglichkeit, Modellausgaben als Echtzeit-Wort-für-Wort-Stream zu empfangen.
- Leicht und einfach bereitzustellen: Architektur, die mit Docker oder Node.js in Sekundenschnelle auf einem lokalen Computer oder Server bereitgestellt werden kann.

## Installation

**Klonen des Repositorys und Installieren von Abhängigkeiten**

```
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
npm install
```

## Ausführung

**Starten des Dienstes und Abfragen des Modells**

```
npm start
# OpenAI uyumlu istek:
curl http://localhost:3000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"Merhaba!"}]}'
```

## Technische Architektur und Funktionsweise

- Provider-Adapterschicht: Erweiterbare Architektur, die verschiedene REST- und WebSocket-APIs in ein gemeinsames JSON-Antwortformat normalisiert.
- Dynamischer Lastenausgleich und Kontingentüberwachung: Überwachen Sie die aktuellen Geschwindigkeitsbegrenzungen jedes Anbieters und leiten Sie Anfragen an das am schnellsten reagierende aktive Modell weiter.
- Integriertes Cache- und Fehlermanagement: Zwischenspeicherung wiederholter Abfragen und automatischer Wiederholungsmechanismus bei Zeitüberschreitungen.

## Modellrouting und Fehlertoleranzmechanismus

- Vergleich mehrerer Modelle: Messen Sie Antwortqualität und Latenz, indem Sie dieselben Benutzereingaben an verschiedene Open-Source-Modelle senden.
- Sparen Sie bei Entwicklung und Prototyping: Bringen Sie KI-gestützte Prototypen und MVP-Projekte schnell zum Laufen, ohne kostenpflichtige API-Schlüssel zu definieren.
- Backup-Strategie (Fallback-Pipeline): Stellen Sie sicher, dass Ihr System ohne Unterbrechung auf sekundäre Modelle umleitet, wenn der primäre Anbieter ausfällt.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Können Sie anhand von Codebeispielen erklären, wie ich das FreeLLMAPI-Tool auf meinem lokalen Server mit Docker ausführe, wie ich das OpenAI Node.js SDK auf diesen lokalen Endpunkt verweise und wie ich die Verwendung eines automatischen Fallback-Modells aktiviert, wenn ein Anbieter ausfällt?

## Häufig gestellte Fragen

- Muss ich einen API-Schlüssel erwerben, um FreeLLMAPI nutzen zu können? Nein. Das System kombiniert 34 KI-Modelle, die kostenlose Stufen anbieten oder kostenlose öffentlich verfügbare Inferenz bereitstellen.
- Welche wichtigen Sprachmodelle werden unterstützt? Offen gewichtete Modelle wie Llama 3, Mistral, Gemma, Claude und beliebte Modelle wie die kostenlose Stufe Google Gemini werden unterstützt.
- Ist es für die Privatsphäre von Unternehmen geeignet? FreeLLMAPI ist Open Source und läuft in Ihrem lokalen Netzwerk, aber die dahinter stehenden kostenlosen Anbieter haben ihre eigenen Nutzungsbedingungen und Datenschutzrichtlinien.
- Ist es mit LangChain oder CrewAI kompatibel? Ja. Da es eine vollständige OpenAI-REST-API-Emulation bietet, kann es direkt mit allen LLM-Frameworks verwendet werden, indem die BaseURL-Adresse auf localhost:3000/v1 gesetzt wird.

## Verwandte Begriffe aus dem Glossar

- [Pipeline](https://trescout.com/de/dictionary/pipeline/)
- [Proxy](https://trescout.com/de/dictionary/proxy/)
- [Localhost](https://trescout.com/de/dictionary/localhost/)
- [SDK](https://trescout.com/de/dictionary/sdk/)
- [LLM](https://trescout.com/de/dictionary/llm/)
- [API](https://trescout.com/de/dictionary/api/)

- **Für wen es gedacht ist:** Entwickler künstlicher Intelligenz, Open-Source-Forscher, Full-Stack-Ingenieure und Prototypenentwickler.
- **Lizenz:** MIT (Özgür açık kaynak lisansı)
- **Framework:** TypeScript / Node.js Reverse Proxy
- **Plattformen:** Docker, Linux, macOS, Windows

## Links

- [GitHub-Repository →](https://github.com/tashfeenahmed/freellmapi)
- [Auf Türkisch lesen →](https://trescout.com/discover/freellmapi/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-28 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/freellmapi/
