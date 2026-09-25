# Was ist QA (Qualitätssicherung)?

**Kategorie:** Entwicklung
**Letzte Aktualisierung:** 2026-09-19

QA (Quality Assurance - Qualitätssicherung) ist eine systematische Software-Engineering-Disziplin, die darauf abzielt, Fehler in allen Phasen des Entwicklungslebenszyklus (SDLC) im Vorfeld zu verhindern, Entwicklungsstandards zu etablieren und die Zuverlässigkeit des Endprodukts sicherzustellen.

## Konzeptionelle Herkunft: Vom Deming-Kreis zur Softwareentwicklung
Das Konzept der Qualitätssicherung entstand Mitte des 20. Jahrhunderts in der industriellen Fertigung. Das von W. Edwards Deming und Walter Shewhart geprägte Total Quality Management (TQM) und der PDCA-Zyklus (Plan-Do-Check-Act) besagten, dass Qualität nicht erst nachträglich hineingeprüft werden kann, sondern integraler Bestandteil des Fertigungsprozesses sein muss. Das Jidoka-Prinzip des Toyota-Produktionssystems (sofortiges Anhalten des Bandes bei Fehlern) bildet das Fundament moderner Continuous-Integration-Pipelines (CI).In der Softwarebranche bewies Barry Boehm, dass die Behebung eines in der Entwurfsphase erkannten Fehlers 1 Kosteneinheit erfordert, während die Korrektur desselben Fehlers im Livebetrieb bis zu 100-mal teurer wird. QA existiert, um diese massiven Schäden systematisch abzuwenden.

## Wesentliche Unterscheidung: QA vs. QC vs. Testing
Obwohl diese Begriffe in der Praxis oft vermischt werden, trennen sie klare methodische Grenzen:Testing (Prüfen): Die gezielte Ausführung von Testfällen, um konkrete Fehler in einem Build aufzudecken (produktbezogen und reaktiv).Qualitätskontrolle (QC - Quality Control): Die Prüfschranke, die verifiziert, ob ein fertiges Release den Spezifikationen und Akzeptanzkriterien entspricht (produktbezogen und reaktiv).Qualitätssicherung (QA - Quality Assurance): Die übergeordnete Disziplin, die Entwicklungsmethoden, Testinfrastrukturen, Kodierrichtlinien und CI/CD-Pipelines so auslegt, dass Fehler gar nicht erst entstehen (prozessbezogen und proaktiv).

## Moderne QA-Paradigmen: Shift-Left und Shift-Right
Im alten Wasserfallmodell schrieben Entwickler den Code und warfen ihn den Testern 'über den Zaun'. Agile und DevOps-Teams setzen stattdessen auf zwei synchronisierte Stoßrichtungen:1. Shift-Left (Frühzeitige Qualität): Qualitätssicherung wandert an den Beginn des Codeschreibens. Entwickler nutzen statische Analyse (SonarQube), strikte Typisierung, Unit-Tests und TDD. QA-Ingenieure agieren hierbei als Plattform-Architekten, die Test-Frameworks und Pipelines bereitstellen.2. Shift-Right (Qualität im Livebetrieb): Absicherung im Produktivbetrieb. Synthetisches Monitoring, Canary-Deployments, Fehler-Telemetrie (Sentry) und Chaos Engineering überwachen die Stabilität unter echter Nutzerlast.

## Die Testpyramide und Automatisierungsschichten
Eine stabile QA-Architektur spiegelt Mike Cohns Testpyramide wider:Unit-Tests: Das solide Fundament; blitzschnell, isoliert und mit minimalem Pflegeaufwand.Integrations- und Vertragstests: Sichern Schnittstellen zwischen Datenbanken, Caches und Microservices über API-Verträge (z. B. Pact) ab.End-to-End-Tests (E2E): Steuern Headless-Browser via Playwright oder Cypress und simulieren echte Nutzerabläufe; bieten maximale Abdeckung bei höherem Wartungsaufwand.Nicht-funktionale Tests: Last- und Stresstests (k6, Locust), automatisierte Sicherheitsscans (SAST/DAST) und Barrierefreiheitsprüfungen (WCAG).

## Analogie
Debugging ist wie eine Notoperation im Krankenhaus und Softwaretesten wie eine Laboranalyse. QA entspricht der präventiven Medizin und Gesundheitspolitik: Sie setzt Hygienestandards, Ernährungsregeln und Impfpläne durch, damit Erkrankungen gar nicht erst ausbrechen.

## QA im Zeitalter von Künstlicher Intelligenz und LLMs
Mit dem Aufkommen probabilistischer Sprachmodelle (LLMs) erweitert sich QA um neue Prüfverfahren:LLM-Evaluierungen (Evals): Automatisierte Frameworks (DeepEval, Ragas) zur Bewertung von Halluzinationsraten, Faktentreue und semantischer Relevanz.Semantische Regressionstests: Benchmark-Suiten, die sicherstellen, dass Anpassungen an Prompts die Antwortqualität früherer Versionen nicht verschlechtern.KI-gestützte Testgenerierung: Autonome Synthese komplexer Testdaten und visuelle Oberflächenprüfung mittels Computer Vision.

## Häufig gestellte Fragen

### Wofür steht die Abkürzung QA in der Softwareentwicklung?
QA steht für Quality Assurance (Qualitätssicherung). Es ist die Ingenieursdisziplin, die Prozesse, Standards und Werkzeuge gestaltet, um fehlerfreie Softwareprodukte zu gewährleisten.

### Wie unterscheidet sich QA vom Softwaretesten?
Testing ist das reaktive Aufspüren von Bugs in existierendem Code. QA ist der proaktive Prozess, der die Entwicklungsumgebung so auslegt, dass Fehler von vornherein vermieden werden.

### Was bedeuten Shift-Left und Shift-Right?
Shift-Left verlagert Qualitätsprüfungen ganz an den Anfang der Entwicklung (Unit-Tests, Linter). Shift-Right überwacht Systemstabilität und Nutzerverhalten kontinuierlich im Livebetrieb.

### Wie läuft QA bei KI- und LLM-Anwendungen ab?
Ergänzend zu klassischen Tests werden Evaluation-Frameworks (Evals) eingesetzt, die Halluzinationsraten, semantische Ähnlichkeit und Retrieval-Genauigkeit (RAG) quantifizieren.

## Verwandte Begriffe
- [Unit Testing](/de/dictionary/unit-testing/)
- [End-to-End Testing](/de/dictionary/end-to-end-testing/)
- [Testing Framework](/de/dictionary/testing-framework/)
- [Production Pipeline](/de/dictionary/production-pipeline/)
- [Benchmarks](/de/dictionary/benchmark/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Tools
- [Gstack](/de/discover/gstack/)

---
Source: TreScout Tech Dictionary · https://trescout.com/de/dictionary/qa/
