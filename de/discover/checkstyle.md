# Unternehmensstil und Qualitätsprüfung in Java-Code

Checkstyle ist ein führendes Tool zur statischen Analyse in Java-Projekten, das die Einhaltung des Google Java Style und der Sun-Coding-Conventions automatisch überprüft und in CI/CD-Pipelines integriert werden kann.

- ★ 9.577
- Java
- GitHub Trending · 2026-08-31

## Was es bringt
- Einhaltung von Unternehmensstandards: Null Formatierungsdiskussionen im gesamten Team dank Google Java Style- und Sun Code Conventions-Vorlagen.
- Analyse des abstrakten Syntaxbaums (AST): Nicht nur Textsuche, sondern die Fähigkeit, die semantische Grammatikstruktur von Java-Code tiefgehend zu überprüfen.
- Umfangreiche integrierte Regelbibliothek: Namenskonventionen, Abstandsformatierung, Verschachtelungstiefe, Javadoc-Mängel und Komplexitätsmetriken.
- Build-Tool-Ökosystem: Automatisches Qualitätsgate im Build-Schritt mit Maven- (maven-checkstyle-plugin) und Gradle-Plugins.
- Anpassbare XML-Konfiguration: Flexibles Anpassen von Regeln an Teamanforderungen, Ausschluss (Suppression) und Verwaltung von Warn-/Fehlerstufen.

## Installation
**Unabhängige CLI-Jar-Datei herunterladen**

```
curl -sSL -O https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.18.0/checkstyle-10.18.0-all.jar
```


## Ausführung
**Mit Google Java Style-Regeln analysieren**

```
java -jar checkstyle-10.18.0-all.jar -c /google_checks.xml src/
# veya Maven ile:
./mvnw checkstyle:check
```


## Technische Architektur und Funktionsweise
- Java-Parser- und ANTLR-Infrastruktur: Unterteilt jede Klasse, Methode und jeden Ausdruck mithilfe eines ANTLR-basierten Grammatikanalysators in Baumknoten.
- Event-Driven Visitor-Muster: Jeder Regel-Controller abonniert ausschließlich die AST-Knoten, die ihn interessieren, und sorgt so für ein performantes Scanning.
- SuppressionFilter und Kommentar-Verstoßausnahmen: Die Möglichkeit, bestimmte Zeilen und Klassen mithilfe von CHECKSTYLE:OFF-Tags oder XML-Filtern von der Prüfung auszunehmen.

## Regelsätze und CI/CD-Integration
- Das Pull-Request-Tor mit GitHub Actions: Verhindern Sie, dass nicht-standardkonforme Codes in den Hauptbranch gelangen, indem Sie bei jedem Öffnen eines PRs eine Checkstyle-Prüfung ausführen.
- IDE-Integration (IntelliJ & Eclipse): Beschleunigen Sie den Feedback-Zyklus, indem Entwickler beim Schreiben von Code Echtzeit-Stilwarnungen erhalten.
- Generierung von HTML- und XML-Berichten: Archivieren Sie technische Schulden und Stilverstöße in der Codebasis, indem Sie sie in Form von Grafiken und Tabellen berichten.

## Wenn Sie nicht programmieren
Können Sie anhand von pom.xml- und checkstyle.xml-Beispielen erklären, wie ich das Checkstyle-Plugin mit Maven in einem bestehenden Spring Boot-Projekt konfiguriere, die Google Java Style-Regeln als Basis nutze und das Zeilenlängenlimit gemäß unseren Teamstandards auf 120 Zeichen aktualisiere?

## Häufig gestellte Fragen
- Korrigiert Checkstyle meinen Code automatisch? Nein. Checkstyle ist ein Analysewerkzeug (Linter), das Zeilen erkennt, die nicht den Regeln entsprechen. Es wird zusammen mit Werkzeugen wie Spotless oder google-java-format für die automatische Neugestaltung des Codes verwendet.
- Was ist der Unterschied zwischen Google Java Style und den Sun-Standards? Die Sun-Standards basieren auf den originalen Java-Regeln aus dem Jahr 1999 (4 Leerzeichen Einrückung, 80 Zeichen pro Zeile). Der Google Java Style hingegen spiegelt mit 2 Leerzeichen Einrückung und einem Limit von 100 Zeichen die moderne Industriepraxis wider.
- Kann Checkstyle den Build stoppen? Ja. Über Parameter wie failOnViolation oder maxAllowedViolations in Maven oder Gradle kann verhindert werden, dass Code mit Stilfehlern kompiliert wird.
- Wie ist die Leistung bei großen Projekten? Da Checkstyle auf dem abstrakten Syntaxbaum (AST) arbeitet, kann es selbst Projekte mit Hunderttausenden von Zeilen in Sekundenschnelle analysieren.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/checkstyle/
