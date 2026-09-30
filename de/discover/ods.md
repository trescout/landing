# Verwandeln Sie Ihren PC in einen lokalen KI-Server

Mit der Open-Source-Lösung Osmantic/ODS können Sie native große Sprachmodellinferenzen, auf der Vektorsuche basierende RAG-Pipelines und autonome Agenten-Workflows einrichten, die auf Ihrer persönlichen Hardware ausgeführt werden.

- ★ 6.854
- Python
- GitHub Trending · 2026-08-31

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
Können Sie anhand von Code- und Terminalschritten erklären, wie ich die PDF-Dokumente meines Unternehmens in die lokale Vektordatenbank importiere, indem ich den ODS-Server auf meinem PC installiere, und wie ich dann RAG-Fragen und -Antworten auf der Grundlage dieser Dokumente über ein lokales Llama 3-Modell durchführe?

## Häufig gestellte Fragen
- Funktioniert es komplett offline ohne Internetverbindung? Ja. Sobald die erforderlichen Modellgewichte heruntergeladen sind, kann ODS in vollständig Offline-Umgebungen (mit Luftspalt) betrieben werden, ohne dass eine Netzwerkverbindung erforderlich ist.
- Welche Modellformate werden unterstützt? Unterstützt alle offenen Modelle (Llama 3, Mistral, Qwen, DeepSeek) und reine HuggingFace-Gewichte im GGUF-Format.
- Ist ein Webinterface verfügbar? Ja. ODS verfügt über ein integriertes Web-Panel. Sie können Modelle verwalten, Dateien hochladen und Chat-Sitzungen öffnen.
- Funktioniert es nur mit CPU, ohne GPU? Ja. Dank des llama.cpp-Kernels kann es mit AVX2/AVX-512-Befehlssätzen auch auf einer reinen CPU mit hoher Effizienz ausgeführt werden.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ods/
