# Was ist End-to-End Testing?

> E2E Testing

End-to-End-Testing (kurz E2E-Test) ist das Testen der Anwendung von Anfang bis Ende wie ein echter Benutzer.

## Definition und Wortherkunft
End-to-End bedeutet von Anfang bis Ende. Es wird das Ganze statt nur Teilstücke getestet: Man loggt sich ein, drückt den Knopf, die Daten werden gesendet, das Ergebnis kommt zurück. Es ist das Kompatibiltätstor vor dem Go-Live.

## Wie kann man es kennen und im täglichen Leben anwenden?
Veröffentlichung: Runde vor dem Release.Store: Kaufprozess.Formular: Registrierungsablauf.

## Technische Tiefe und Architektur
Layout:

## Häufig gemischte Dinge
Wird oft für einen Unit-Test gehalten. Er schaut sich jenes Teil an, dieser schaut sich das Ganze an. Das eine ist ein Schraubentest, das andere ein Fahrtest.

## Einsatz in verschiedenen Disziplinen
Auto: Losfahren mit dem Schlüssel.Probe: Gesamtwiederholung.Finale: Sendeprobe.

## Häufig gestellte Fragen
**Warum wird nur das nicht gemacht?**
Es ist langsam, der Ort des Fehlers ist unklar. Wird zusammen mit der Einheit verwendet.

**Wie oft läuft es?**
Vor der Sendung und in der Nacht. Bei jedem Commit läuft eine kritische Untermenge.

**Wer schreibt es?**
Entwickler und Tester schreiben es gemeinsam. Es hat einen klaren Verantwortlichen.

**Ist es anfällig (fragil)?**
Es geht kaputt, wenn sich die Benutzeroberfläche ändert. Es wird selektiv und robust geschrieben.


## Verwandte Begriffe
- [Unit Testing](/de/dictionary/unit-testing/)
- [Testing Framework](/de/dictionary/testing-framework/)
- [Web Interface](/de/dictionary/web-interface/)

## Verwandte Werkzeuge
- [Cypress](/de/discover/cypress/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/end-to-end-testing/
