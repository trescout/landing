# Verwandeln Sie Ihren PC in einen lokalen KI-Server

Mit der Open-Source-Lösung Osmantic/ODS können Sie native große Sprachmodellinferenzen, auf der Vektorsuche basierende RAG-Pipelines und autonome Agenten-Workflows einrichten, die auf Ihrer persönlichen Hardware ausgeführt werden.

- ★ 6.854
- Python
- GitHub Trending · 2026-08-31

## Aktualisierungen

- **27. September 2026:** Sterne 5,181 → 6,854, neueste Version v3.0.0 (24. September 2026).

## Was es bringt

- Vollständiger Datenschutz und lokale Ausführung: Sichere KI-Ausführung auf lokaler GPU und CPU, ohne Ihre Daten an externe Cloud-Server zu senden.
- Integriertes RAG (Search Aided Generation): Vektorisieren Sie Ihre persönlichen Notizen, Unternehmensdokumente und Code-Repositories für sofortige semantische Suchen.
- Multimodale Fähigkeiten: Zusammenführung von Textproduktion, Spracherkennung (Whisper), Sprachsynthese und visueller Produktion unter einem Dach.
- OpenAI-kompatible native API: Verweisen Sie Ihre vorhandenen KI-Clients und -Tools mit einer einzigen URL-Änderung auf Ihren lokalen ODS-Server.
- Umfassende Agenten-Orchestrierung: Intelligente Agentenketten, die lokale Tools aufrufen und mehrstufige Aufgaben autonom lösen.

## Installation

**Klonen des Repositorys und Einrichten der Umgebung**

```
git clone https://github.com/Osmantic/ODS.git
cd ODS
pip install -e .
```

## Ausführung

**Starten des lokalen AI-Servers**

```
python -m ods.server --port 8000
# Web paneline http://localhost:8000 adresinden erişin
```

## Technische Architektur und Funktionsweise

- Nativer Inferenzkernel (llama.cpp & vLLM): Modelle in GGUF- und reinen GPU-Formaten schnell laden und ausführen, mit minimalem Speicherbedarf.
- Eingebettete Vektordatenbank: Chunking und Indizierung von Dokumenten mit leichtgewichtigem Vektorspeicher basierend auf ChromaDB und SQLite.
- Aufgabenwarteschlange und Agent-Zustandsmaschine: Asynchrone Handler, die mehrstufige Abfragen und Tool-Aufrufabläufe verarbeiten.

## Native RAG-Workflows und benutzerdefinierte Agent-Pipelines

- Arbeiten mit vertraulichen Unternehmensdokumenten: Fragen Sie Verträge, Finanzberichte und interne Korrespondenz mit der lokalen RAG ab, ohne sie in die Cloud zu extrahieren.
- Assistent für die Analyse und Entwicklung von nativem Code: Stellen Sie die Vervollständigung von nativem KI-Code auf VS Code oder Cursor bereit, indem Sie Ihre benutzerdefinierten Softwareprojekte indizieren.
- Autonome Datenverarbeitungsagenten: Definieren Sie Hintergrundaufgaben, die Konvertierungsberichte im lokalen Dateisystem lesen, zusammenfassen und formatieren.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Können Sie anhand von Code- und Terminalschritten erklären, wie ich die PDF-Dokumente meines Unternehmens in die lokale Vektordatenbank importiere, indem ich den ODS-Server auf meinem PC installiere, und wie ich dann RAG-Fragen und -Antworten auf der Grundlage dieser Dokumente über ein lokales Llama 3-Modell durchführe?

## Häufig gestellte Fragen

- Funktioniert es komplett offline ohne Internetverbindung? Ja. Sobald die erforderlichen Modellgewichte heruntergeladen sind, kann ODS in vollständig Offline-Umgebungen (mit Luftspalt) betrieben werden, ohne dass eine Netzwerkverbindung erforderlich ist.
- Welche Modellformate werden unterstützt? Unterstützt alle offenen Modelle (Llama 3, Mistral, Qwen, DeepSeek) und reine HuggingFace-Gewichte im GGUF-Format.
- Ist ein Webinterface verfügbar? Ja. ODS verfügt über ein integriertes Web-Panel. Sie können Modelle verwalten, Dateien hochladen und Chat-Sitzungen öffnen.
- Funktioniert es nur mit CPU, ohne GPU? Ja. Dank des llama.cpp-Kernels kann es mit AVX2/AVX-512-Befehlssätzen auch auf einer reinen CPU mit hoher Effizienz ausgeführt werden.

## Verwandte Begriffe aus dem Glossar

- [Multimodal](https://trescout.com/de/dictionary/multimodal/)
- [Vector Database](https://trescout.com/de/dictionary/vector-database/)
- [GGUF](https://trescout.com/de/dictionary/gguf/)
- [Whisper](https://trescout.com/de/dictionary/whisper/)
- [CPU](https://trescout.com/de/dictionary/cpu/)
- [RAG](https://trescout.com/de/dictionary/rag/)

- **Für wen es gedacht ist:** Unternehmen, denen der Datenschutz am Herzen liegt, lokale Entwickler künstlicher Intelligenz und Systemadministratoren.
- **Lizenz:** MIT (Özgür açık kaynak lisansı)
- **Framework:** Python & llama.cpp Lokaler AI-Server
- **Plattformen:** Linux, macOS, Windows

## Links

- [GitHub-Repository →](https://github.com/Osmantic/ODS)
- [Auf Türkisch lesen →](https://trescout.com/discover/ods/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-31 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ods/
