# Was ist QA?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

> Quality Assurance

QA (Quality Assurance – Qualitätssicherung) ist eine systematische Qualitätsmanagementdisziplin, die darauf abzielt, Fehler in jeder Phase des Softwareentwicklungslebenszyklus zu verhindern, bevor sie entstehen, Engineering-Standards zu etablieren und die Zuverlässigkeit des Endprodukts zu garantieren.

## Konzeptueller Ursprung: Der Deming-Kreis und der Weg von der Fertigung zur Software

Der Begriff der Qualitätssicherung entstand lange vor der Softwareentwicklung, Mitte des 20. Jahrhunderts in der industriellen Fertigung. Das von W. Edwards Deming und Walter Shewhart begründete Total Quality Management (TQM) und der PDCA-Zyklus (Plan-Do-Check-Act / Planen-Durchführen-Prüfen-Agieren) vertreten die Ansicht, dass Qualität nicht nachträglich geprüft werden kann, sondern direkt in das Produkt eingebaut werden muss. Das Jidoka-Prinzip (sofortiges Anhalten des Fließbands bei der Produktion eines fehlerhaften Produkts) im Toyota-Produktionssystem ist zudem der Vorläufer der heutigen modernen Continuous Integration (CI) und QA-Philosophie.

In der Softwarewelt hat Barry Boehm in seiner berühmten Studie zur „Software Engineering Economics“ nachgewiesen, dass die Kosten für die Behebung eines in der Entwurfsphase erkannten Fehlers 1 Einheit betragen, während die Kosten für die Behebung nach dem Live-Gang (Production) auf das Hundertfache steigen können. QA existiert, um diese enormen Kosten und den Reputationsverlust zu verhindern.

***Analogie:** Debugging (Fehlersuche) ist wie ein Eingriff auf dem Operationstisch, Softwaretests sind wie Laboranalysen. QA hingegen ist das Protokoll für öffentliche Gesundheit und Präventivmedizin: Es zielt darauf ab, das Krankheitsrisiko von vornherein zu eliminieren, indem es Leitfäden für gesunde Ernährung, Impfpläne und Hygieneregeln festlegt.*

## Kritische Unterscheidung: QA vs. QC vs. Testing

Obwohl diese drei Konzepte oft synonym verwendet werden, gibt es klare methodologische Grenzen zwischen ihnen:

**Testing (Testen):** Die Ausführung von Szenarien, um konkrete Fehler (Bugs) in einer bestimmten Softwareversion zu finden (produktorientiert und reaktiv).

**Quality Control (QC – Qualitätskontrolle):** Das Kontrolltor, das vor der Veröffentlichung des Produkts überprüft, ob es den festgelegten technischen Spezifikationen und Abnahmekriterien entspricht (produktorientiert und reaktiv).

**Qualitätssicherung (QA - Quality Assurance):** Die übergeordnete Disziplin, die Entwicklungsmethodologien, die Testinfrastruktur, Architekturstandards und CI/CD-Prozesse entwirft, um Fehler von vornherein zu verhindern (prozessorientiert und proaktiv).

## Modernes QA-Paradigma: Shift-Left und Shift-Right

Im traditionellen Wasserfallmodell schrieben Entwickler den Code und "warfen ihn dann über die Mauer" an die QA-Abteilung zum Testen. In der modernen agilen und DevOps-Welt ist dieser Ansatz zwei komplementären Richtungen gewichen:

**1. Shift-Left (Verlagerung nach links):** Zieht die Qualitätskontrolle an den Anfang der Entwicklung. Bereits beim Schreiben des Codes wenden Entwickler statische Analysen (ESLint, SonarQube), Typüberprüfung (TypeScript), Unit-Tests (Jest, pytest) und TDD (Test-Driven Development) an. Der QA-Ingenieur ist hierbei keine Person, die Tests ausführt, sondern ein Plattform-Architekt, der die Testinfrastruktur und Frameworks aufbaut.

**2. Shift-Right (Verlagerung nach rechts):** Die Aufrechterhaltung der Qualität, nachdem der Code live gegangen ist. Durch synthetisches Monitoring, Canary-Deployments, Fehlerverfolgung (Sentry), Chaos Engineering und Live-Trafficanalysen wird die reale Benutzererfahrung überwacht.

## Testpyramide und Automatisierungsschichten

Eine robuste QA-Architektur basiert auf dem Prinzip der Testpyramide von Mike Cohn:

**Unit-Tests (Birim Testleri):** Bilden die Basis; testen unabhängige Funktionen isoliert, laufen in Millisekunden und haben die geringsten Kosten.

**Integrations- und Vertragstests (Integration & Contract Tests):** Überprüft API-Verträge (z. B. Pact) zwischen Datenbank, Cache und Mikroservices.

**End-to-End-Tests (E2E Tests):** Simuliert die Schritte eines echten Benutzers im Browser mit Tools wie Cypress oder Playwright; der Umfang ist groß, aber die Wartung ist kostspieliger.

**Nicht-funktionale Tests:** Umfasst Last- und Stresstests (k6, Locust), Scans auf Sicherheitslücken (SAST/DAST) und Barrierefreiheitsprüfungen (WCAG / a11y).

## QA im Zeitalter von KI und LLM

Mit der Verbreitung von probabilistischen (nicht-deterministischen) Systemen wie großen Sprachmodellen (LLM) ist die QA-Disziplin in eine neue Phase eingetreten:

**LLM-Evaluierungen (Evals):** Automatisierte Prüfungen (DeepEval, Ragas), die Halluzinationen, Genauigkeit, Toxizität und Relevanz von Modellantworten bewerten.

**Semantische Regressionstests:** Benchmark-Sets, die messen, ob eine Änderung an Prompt-Vorlagen die vorherige Antwortqualität beeinträchtigt.

**KI-gestützte Testerstellung:** Automatische Erkennung von Test-Szenarien und Regressionsunterschieden in der grafischen Benutzeroberfläche mittels KI-Modellen.

## Häufige Fragen

**Was bedeutet QA und wofür steht die Abkürzung?**

Es ist die Abkürzung für Quality Assurance; im Deutschen bedeutet es Qualitätssicherung. Es ist die Ingenieursdisziplin, die sicherstellt, dass Softwareprozesse von Anfang bis Ende fehlerfrei ablaufen.

**Was ist der Unterschied zwischen QA, QC (Qualitätskontrolle) und Testen?**

Testen und QC sind reaktive Schritte, die darauf abzielen, Fehler im vorhandenen Code zu finden. QA hingegen ist der proaktive Prozess, der Entwicklungsprozesse, Standards und Werkzeuge entwirft, damit Fehler gar nicht erst entstehen.

**Was bedeuten die Testansätze Shift-Left und Shift-Right?**

Shift-Left bedeutet, Testprozesse an den Anfang der Entwicklung (den Moment des Codeschreibens) zu ziehen; Shift-Right bezieht sich auf die Echtzeitüberwachung des Systemzustands und des Benutzerverhaltens in der Live-Umgebung.

**Wie wird QA in KI- und LLM-basierten Anwendungen durchgeführt?**

Neben traditionellen Tests werden spezielle Evaluierungs-Frameworks (Evals) verwendet, die Halluzinationsraten, semantische Ähnlichkeit, Prompt-Regression und RAG-Genauigkeitsmetriken messen.

## Verwandte Begriffe

- [Unit Testing](https://trescout.com/de/dictionary/unit-testing/)
- [End-to-End Testing](https://trescout.com/de/dictionary/end-to-end-testing/)
- [Testing Framework](https://trescout.com/de/dictionary/testing-framework/)
- [Production Pipeline](https://trescout.com/de/dictionary/production-pipeline/)
- [Benchmarks](https://trescout.com/de/dictionary/benchmark/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)

## Verwandte Werkzeuge

- [Gstack](https://trescout.com/de/discover/gstack/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/qa/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/qa/
