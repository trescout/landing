# Was ist QA?

> Quality Assurance

QA (Quality Assurance – Qualitätssicherung) ist eine systematische Qualitätsmanagementdisziplin, die darauf abzielt, Fehler in jeder Phase des Softwareentwicklungslebenszyklus zu verhindern, bevor sie entstehen, Engineering-Standards zu etablieren und die Zuverlässigkeit des Endprodukts zu garantieren.

## Konzeptueller Ursprung: Der Deming-Kreis und der Weg von der Fertigung zur Software
Der Begriff der Qualitätssicherung entstand lange vor der Softwareentwicklung, Mitte des 20. Jahrhunderts in der industriellen Fertigung. Das von W. Edwards Deming und Walter Shewhart begründete Total Quality Management (TQM) und der PDCA-Zyklus (Plan-Do-Check-Act / Planen-Durchführen-Prüfen-Agieren) vertreten die Ansicht, dass Qualität nicht nachträglich geprüft werden kann, sondern direkt in das Produkt eingebaut werden muss. Das Jidoka-Prinzip (sofortiges Anhalten des Fließbands bei der Produktion eines fehlerhaften Produkts) im Toyota-Produktionssystem ist zudem der Vorläufer der heutigen modernen Continuous Integration (CI) und QA-Philosophie.

## Kritische Unterscheidung: QA vs. QC vs. Testing
Obwohl diese drei Konzepte oft synonym verwendet werden, gibt es klare methodologische Grenzen zwischen ihnen:

## Modernes QA-Paradigma: Shift-Left und Shift-Right
Im traditionellen Wasserfallmodell schrieben Entwickler den Code und "warfen ihn dann über die Mauer" an die QA-Abteilung zum Testen. In der modernen agilen und DevOps-Welt ist dieser Ansatz zwei komplementären Richtungen gewichen:

## Testpyramide und Automatisierungsschichten
Eine robuste QA-Architektur basiert auf dem Prinzip der Testpyramide von Mike Cohn:

## QA im Zeitalter von KI und LLM
Mit der Verbreitung von probabilistischen (nicht-deterministischen) Systemen wie großen Sprachmodellen (LLM) ist die QA-Disziplin in eine neue Phase eingetreten:

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
- [Unit Testing](/de/dictionary/unit-testing/)
- [End-to-End Testing](/de/dictionary/end-to-end-testing/)
- [Testing Framework](/de/dictionary/testing-framework/)
- [Production Pipeline](/de/dictionary/production-pipeline/)
- [Benchmarks](/de/dictionary/benchmark/)
- [Runtime](/de/dictionary/runtime/)

## Verwandte Werkzeuge
- [Gstack](/de/discover/gstack/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/qa/
