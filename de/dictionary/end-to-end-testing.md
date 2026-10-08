# Was ist End-to-End Testing?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> E2E Testing

End-to-End-Testing (kurz E2E-Test) ist das Testen der Anwendung von Anfang bis Ende wie ein echter Benutzer.

## Definition und Wortherkunft

End-to-End bedeutet von Anfang bis Ende. Es wird das Ganze statt nur Teilstücke getestet: Man loggt sich ein, drückt den Knopf, die Daten werden gesendet, das Ergebnis kommt zurück. Es ist das Kompatibiltätstor vor dem Go-Live.

***Analogie:** Das ist so, als würde man versuchen, den Schlüssel zu drehen und loszufahren, statt den Motor zu starten.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Veröffentlichung:** Runde vor dem Release.
**Store:** Kaufprozess.
**Formular:** Registrierungsablauf.

## Technische Tiefe und Architektur

Layout:

**Kritischer Pfad:** Der zuerst Geld einbringende Strom.
**Automatisierung:** Ein Tool, das den Browser steuert.
**Daten:** Testkonto und Zurücksetzen.

Beispiel:

```
test("giriş", async () => {
  await sayfa.goto("/giris");
  await bekle("#panel");
});
```

Grund für Langsamkeit: Ein echter Browser öffnet sich. Der kritische Pfad wird gewählt, nicht alles wird getestet.

## Häufig gemischte Dinge

Wird oft für einen Unit-Test gehalten. Er schaut sich jenes Teil an, dieser schaut sich das Ganze an. Das eine ist ein Schraubentest, das andere ein Fahrtest.

## Einsatz in verschiedenen Disziplinen

**Auto:** Losfahren mit dem Schlüssel.
**Probe:** Gesamtwiederholung.
**Finale:** Sendeprobe.

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

- [Unit Testing](https://trescout.com/de/dictionary/unit-testing/)
- [Testing Framework](https://trescout.com/de/dictionary/testing-framework/)
- [Web Interface](https://trescout.com/de/dictionary/web-interface/)

## Verwandte Werkzeuge

- [Cypress](https://trescout.com/de/discover/cypress/)
- [E2e](https://trescout.com/de/discover/e2e/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/end-to-end-testing/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/end-to-end-testing/
