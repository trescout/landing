# Schnelle Logging-Bibliothek für C++-Projekte

spdlog ist eine ultraschnelle, als reine Header-Datei (header-only) oder vorkompilierte Bibliothek nutzbare C++-Logging-Bibliothek. Auf Basis moderner C++-Standards bietet sie verzögerungsfreie und thread-sichere Protokollierung mit minimalem Overhead.

- ★ 29.437
- C++
- GitHub Trending · 2026-08-05

## Aktualisierungen
- 6. August 2026: Sterne 29.402 → 29.437, neueste Version v1.17.0 (4. Januar 2026).

## Was es bringt
- Millionen Zeilen Durchsatz pro Sekunde: Zero-Allocation-Design und Compile-Time-Optimierungen sorgen für Mikrosekunden-Latenz im Hauptthread.
- Asynchroner, sperrenfreier Ringpuffer: Lagert Festplatten- und Netzwerk-I/O in einen Hintergrund-Thread-Pool aus, um Blockaden zu verhindern.
- Vielseitige Senken (Sinks): Gleichzeitiges Schreiben auf die farbige Konsole, in rotierende Dateien, tägliche Archive und Syslog.
- Integrierte {fmt}-Formatierungsstärke: Nutzt die {fmt}-Bibliothek (C++20-Standard) für typsichere, schnelle und elegante Formatierung.
- Header-only oder vorkompiliert: Einfach per Ordnerkopie einbinden oder statisch verknüpfen, um Compile-Zeiten zu reduzieren.

## Installation

**macOS (Homebrew)**

```
brew install spdlog
```

**vcpkg Paketmanager**

```
vcpkg install spdlog
```

**CMake FetchContent Integration**

```
include(FetchContent)
FetchContent_Declare(
  spdlog
  GIT_REPOSITORY https://github.com/gabime/spdlog.git
  GIT_TAG v1.17.0
)
FetchContent_MakeAvailable(spdlog)
target_link_libraries(mein_projekt PRIVATE spdlog::spdlog)
```

Source: Homebrew-Formel

## Erste Schritte und grundlegende Nutzung

Der Einstieg in spdlog ist unkompliziert. Nach Einbindung des Headers können Sie direkt globale Logging-Funktionen aufrufen oder eigene Logger instanziieren:

**C++ Anwendungsbeispiel**

```
#include "spdlog/spdlog.h"
#include "spdlog/sinks/rotating_file_sink.h"

int main() {
    // Standard-Konsolen-Logging
    spdlog::info("spdlog erfolgreich initialisiert.");
    spdlog::warn("Warnung: Speicherauslastung steigt an!");
    spdlog::error("Fehlercode: {:d}, Nachricht: {}", 404, "Seite nicht gefunden");

    // Rotierender Datei-Logger (max. 5MB, 3 Dateien)
    auto file_logger = spdlog::rotating_logger_mt("file_logger", "logs/app.txt", 1024 * 1024 * 5, 3);
    file_logger->info("Diese Nachricht ist thread-sicher und wird automatisch archiviert.");

    return 0;
}
```

## Technische Architektur und Funktionsweise

Die herausragende Geschwindigkeit von spdlog basiert auf einer modularen Architektur ohne Overhead:
- Trennung von Logger und Sink: Der Logger filtert nach Schweregrad und leitet formatierte Datensätze an verbundene Sinks weiter.
- Thread-Sicherheit (_mt vs _st): Alle Sinks existieren als Mutex-synchronisierte Versionen (_mt) sowie als lock-free Single-Thread-Varianten (_st).
- Asynchroner Ringpuffer: Ein via spdlog::init_thread_pool erstellter Puffer wird von Worker-Threads abgearbeitet, ohne den Hauptcode zu blockieren.
- Intelligenter Flush: Daten werden performant im Betriebssystem-Puffer gehalten und bei kritischen Fehlern sofort auf die Festplatte geschrieben.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte spdlog in einem modernen C++-Projekt mit CMake asynchron einrichten. Kannst du mir eine Initialisierungsfunktion und eine CMakeLists.txt erstellen, die farbige Konsolenausgabe, eine rotierende 10MB-Datei und sofortiges Flashen bei Fehlern konfiguriert?

- **Für wen:** C++-Entwickler, Spiele-Engine-Programmierer und Embedded-System-Architekten, die minimale Latenz benötigen.
- **Lizenz:** MIT (Freie Open-Source-Lizenz)
- **Integration:** Header-only oder vorkompilierte Bibliothek
- **Standards:** C++11, C++14, C++17, C++20

## Häufig gestellte Fragen
- Warum spdlog statt printf oder std::cout verwenden? spdlog ist um ein Vielfaches schneller, thread-sicher, bietet standardisierte Log-Level und blockiert die Anwendung nicht bei I/O-Vorgängen.
- Können eigene Klassen geloggt werden? Ja, durch Überladen von operator<< oder Spezialisieren von fmt::formatter für eigene Datentypen.
- Eignet sich spdlog für Gaming und High-Frequency Trading? Ja, mit asynchronen Puffern erfolgt das Absetzen von Log-Nachrichten in Nanosekunden, ohne die Render-Schleife zu stören.
- Wird strukturierte JSON-Ausgabe unterstützt? Ja, über benutzerdefinierte Muster können Sie JSON-Streams erzeugen, die direkt von Grafana Loki oder Datadog eingelesen werden.

## Links
- [GitHub →](https://github.com/gabime/spdlog)
- [Read in Turkish →](https://trescout.com/discover/spdlog/)

## Verwandte Begriffe aus dem Glossar
Logging Logs Runtime Memory Management

---
Source: TreScout Discover · https://trescout.com/de/discover/spdlog/
