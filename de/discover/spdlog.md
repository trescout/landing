# Schnelle Protokollierung für C++-Projekte

spdlog ist eine ultraschnelle Protokollierungsbibliothek, die für die Programmiersprache C++ entwickelt wurde und nur als Header oder als kompilierte Bibliothek verwendet werden kann. Es bietet verzögerungsfreies und leistungsstarkes Ausgabemanagement in Softwareprojekten unter Verwendung moderner C++-Standards.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Aktualisierungen

- **6. August 2026:** Sterne 29,402 → 29,437, neueste Version v1.17.0 (4. Januar 2026).

## Was es bringt

- Protokollierungsleistung in Millionen von Zeilen pro Sekunde: Erzeugt Latenz im Mikrosekundenbereich im Hauptanwendungsthread mit einem Ansatz ohne Speicherzuweisung und Optimierungen zur Kompilierungszeit.
- Asynchrone und sperrenfreie Ringwarteschlange: Isoliert Datei- oder Netzwerk-E/A-Engpässe vollständig von der aufrufenden Pipeline, indem Protokollschreibvorgänge in den Hintergrundpool verlagert werden.
- Reichhaltige Zielvielfalt: Bunte Konsolenausgabe, nach Größe rotierende Dateien, Archive mit Tagesdaten, gleichzeitiges Schreiben in Syslog- und Android-Logcat-Ziele.
- Integrierte FMT-Formatierungsleistung: Bietet sichere, schnelle und flexible Textformatierung im Python-Stil mithilfe der {fmt}-Bibliothek, die die Grundlage des C++20-Formatierungsstandards bildet.
- Flexibilität der reinen Header- oder kompilierten Verwendung: Sie können es in Ihr Projekt einbinden, indem Sie ein einzelnes Verzeichnis kopieren oder es als statische Bibliothek verknüpfen, um die Kompilierungszeiten zu verkürzen.

## Installation

**macOS (Homebrew)**

```
brew install spdlog
```

## Erste Schritte und grundlegende Verwendung

Der Einstieg in die spdlog-Bibliothek ist äußerst mühelos. Sobald Sie die Header-Datei in Ihr Projekt eingebunden haben, können Sie globale Protokollierungsfunktionen direkt aufrufen oder benutzerdefinierte Logger-Objekte erstellen:

## Technische Architektur und Funktionsweise

- Unterscheidung zwischen Logger und Sink: Das Logger-Objekt filtert das eingehende Protokoll (Trace, Debug, Info, Warnung, Fehler, kritisch). Akzeptierte Nachrichten werden an ein oder mehrere Sink-Objekte übertragen. Beispielsweise kann ein einzelner Logger im JSON-Format in die Datei schreiben und gleichzeitig Farbe an die Konsole drucken.
- Thread-sicher (_mt vs. _st): spdlog stellt alle Senkenklassen in zwei Formen bereit: Multi-Thread-sichere Mutex-Sperrversion (_mt) und Single-Thread-spezifische sperrenfreie Version (_st). Im Single-Threaded-Modus betragen die Mutex-Kosten vollständig Null.
- Asynchrone Ringwarteschlange (Ringpuffer): Der mit spdlog::init_thread_pool zugewiesene Speicherblock wird vom im Hintergrund ausgeführten Thread verbraucht. Die Hauptanwendung belässt das Protokoll in der Warteschlange und setzt ihren Weg sofort fort.
- Intelligentes Puffer-Flushing (Flush): Daten werden aus Leistungsgründen im Betriebssystempuffer gespeichert; Allerdings kann der spdlog::flush_on(spdlog::level::err)-Mechanismus ausgelöst werden, um Datenverlust in kritischen Fehlermomenten zu verhindern.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die spdlog-Bibliothek mit asynchroner Architektur mithilfe von CMake in einem modernen C++-Projekt konfigurieren. Können Sie die Datei CMakeLists.txt mit einer Beispiel-C++-Initialisierungsfunktion vorbereiten, die die Datei rotiert, wenn das Protokoll eine Größe von 10 MB erreicht, außerdem eine Farbausgabe an die Konsole liefert und sie bei Fehlerstufe sofort auf die Festplatte schreibt?

## Häufig gestellte Fragen

- Sollte spdlog nur im Header verwendet oder kompiliert werden? In kleinen und mittelgroßen Projekten bietet die Verwendung von Nur-Headern durch Hinzufügen nur des Include-Verzeichnisses große Praktikabilität. In großen C++-Projekten, die aus Hunderten von Quelldateien bestehen, wird jedoch empfohlen, die Bibliothek mit dem Flag SPDLOG_COMPILED zu kompilieren und zu verknüpfen, um die Kompilierungszeit zu optimieren.
- Beeinflusst die Protokollierung die Ausführungsgeschwindigkeit der Hauptanwendung? Spdlog läuft selbst im synchronen Modus auf Mikrosekundenebene und reduziert die E/A-Last im Hauptthread auf nahezu Null, wenn eine asynchrone Logger-Architektur verwendet wird. Die Nachricht wird in die Warteschlange kopiert und das Schreiben auf die Festplatte erfolgt im Hintergrund.
- Wie funktioniert der rotierende Feilenmechanismus? Wenn die angegebene maximale Dateigröße (z. B. 10 MB) erreicht ist, wird die aktive Datei archiviert (application.1.txt, application.2.txt) und eine neue Datei von Grund auf geöffnet. Wenn die angegebene maximale Anzahl von Dateien überschritten wird, wird die älteste Protokolldatei automatisch gelöscht.
- Wird es einen Konflikt mit der externen FMT-Bibliothek geben? Nein. spdlog verwendet standardmäßig die intern gepackte Version von fmt. Wenn Sie möchten, können Sie die vorhandene unabhängige FMT-Bibliothek direkt in Ihr System mit spdlog integrieren, indem Sie das Makro SPDLOG_FMT_EXTERNAL definieren.

## Verwandte Begriffe aus dem Glossar

- [Logging](https://trescout.com/de/dictionary/logging/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für C++-Entwickler, Game-Engine- und Embedded-System-Architekten, die das Debuggen, Überwachen und Überprüfen von Softwareprojekten ohne Latenz beschleunigen möchten.
- **Lizenz:** MIT Lisansı (Ticari ve açık kaynak projelerde tamamen serbest)
- **Standard:** Kompatibel mit C++11, C++14, C++17, C++20 und C++23
- **Bibliothekstyp:** Nur-Header- oder kompilierte statische/dynamische Verknüpfung

## Links

- [GitHub-Repository →](https://github.com/gabime/spdlog)
- [Auf Türkisch lesen →](https://trescout.com/discover/spdlog/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-08-05 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/spdlog/
