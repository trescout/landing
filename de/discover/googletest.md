# Branchenstandard-Unit-Tests für C++-Projekte

GoogleTest und GoogleMock sind das Open-Source-Testframework des Branchenstandards, mit dem Sie Unit-Tests, Scheinkonnektoren (Mocks) und parametrisierte Tests in modernen C++-Projekten ausführen können.

- ★ 39.588
- C++
- GitHub Trending · 2026-08-27

## Was es bringt
- Reiche Validierungsmakros: Klare Fehlerdiagnose mit ASSERT_* (kritischer Fehler, bricht den Test ab) und EXPECT_* (zeichnet den Fehler auf, setzt den Testfortschritt fort) Makros.
- Erweiterte Mock-Infrastruktur (GoogleMock): Einfaches Simulieren von Schnittstellen mit MOCK_METHOD zur Isolierung von Abhängigkeiten und Definieren von Aufruferwartungen.
- Parametrische Testfähigkeit: Die Fähigkeit, dieselbe Testlogik mit einer einzigen Vorlage automatisch über Dutzende verschiedener Eingaben und Datensätze hinweg zu wiederholen.
- Plattformübergreifend und Threadsicherheit: Thread-sichere Architektur in Linux-, macOS- und Windows-Umgebungen sowie Validierung von Absturzszenarien durch Death Tests.
- CI/CD- und Berichtsintegration: Nahtlose Integration in GitHub Actions-, Jenkins- und GitLab CI-Pipelines mit JUnit-kompatiblen XML- und JSON-Ausgabeformaten.

## Installation
**Hinzufügen zum Projekt mit CMake FetchContent**

```
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.15.2.tar.gz
)
FetchContent_MakeAvailable(googletest)
```


## Ausführung
**Kompilieren des Tests und Ausführen mit CTest**

```
cmake -B build -S .
cmake --build build
ctest --test-dir build --output-on-failure
```


## Technische Architektur und Funktionsweise
- Test-Fixture- und Lebenszyklusverwaltung: Mit Setup- und TearDown-Routinen werden Speicherressourcen vor und nach jedem Test sicher verwaltet.
- Prozessisolation für Death Tests: Fängt unerwartete Programmabstürze oder Assertions mithilfe eines Fork-Mechanismus in isolierten Kindprozessen ab.
- Typ-parametrisierte Testvorlagen: Bietet eine Typ-parameterisierte Testinfrastruktur, um templatisierte Klassen (C++ Templates) mit verschiedenen Datentypen auf einmal zu testen.

## Testzenarien und GoogleMock-Integration
- Abstraktion von Datenbank- und Netzwerkaufrufen: Simulieren Sie mit MOCK_METHOD erwartete API-Antworten und Latenzen, ohne echte Netzwerkverbindungen herzustellen.
- Aufrufe und Parametervalidierung: Überprüfen Sie mit dem EXPECT_CALL-Makro, wie oft, mit welchen Argumenten und in welcher Reihenfolge eine Funktion aufgerufen wird.
- Untersuchung von Fehlschlagsszenarien: Stellen Sie die Robustheit sicher, indem Sie Codeblöcke, die Ausnahmen auslösen (throw), mit EXPECT_THROW-Makros testen.

## Wenn Sie nicht programmieren
Ich möchte in einem modernen C++-Projekt Unit-Tests für eine Datenparser-Klasse unter Verwendung von GoogleTest und GoogleMock schreiben. Können Sie anhand von Codebeispielen erklären, wie ich meine CMakeLists.txt-Datei konfiguriere, eine beispielhafte TEST_F-Test-Fixture erstelle und ein Mock-Objekt mit MOCK_METHOD generiere sowie Aufruferwartungen validiere?

## Häufig gestellte Fragen
- Was ist der modernste Weg, GoogleTest in ein Projekt einzubinden? Bei modernen CMake-Projekten ist der FetchContent-Mechanismus der am meisten empfohlene Ansatz. Er lädt den Quellcode ohne die Notwendigkeit eines externen Paketmanagers herunter und bindet ihn in den Ziel-Kompilierungsprozess ein.
- Was ist der Hauptunterschied zwischen EXPECT_* und ASSERT_*? EXPECT_* Makrosive protokollieren den Fehler bei Fehlschlägen, erlauben aber der restlichen Funktion weiterzulaufen. ASSERT_* hingegen bricht die aktuelle Testfunktion im Fehlerfall sofort ab.
- Ist GoogleMock eine separate Bibliothek? GoogleMock war ursprünglich ein eigenständiges Projekt, ist aber bereits seit längerer Zeit unter dem Dach des GoogleTest-Repositorys zusammengefasst; beide werden gemeinsam installiert und verwendet.
- Bietet es Thread-Sicherheit? Ja. GoogleTest läuft auf Systemen, die pthreads unterstützen, sowie unter Windows thread-safe und synchronisiert gleichzeitige Benachrichtigungen von mehreren Threads korrekt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/googletest/
