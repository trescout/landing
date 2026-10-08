# Was ist Repository Checkout?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Beim Auschecken des Repositorys wird eine bestimmte Version des Repositorys in Ihren Arbeitsbereich heruntergeladen.

## Definition und Wortherkunft

Sie holen sich die aktuelle Version des Projekts vom Server und bringen sie auf Ihren Schreibtisch. Es ist, als würde man ein Buch aus der Bibliothek ausleihen: Die Quelle bleibt, man arbeitet mit der Kopie. Verlaufs- und Versionsinformationen liegen der Kopie bei.

***Analogie:** Es ist, als würde man sich ein Buch aus der Bibliothek ausleihen, es an den Schreibtisch bringen und beginnen, die Seiten eine nach der anderen zu lesen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Neues Projekt:** Das Repository zum ersten Mal herunterladen.
**Versionsmigration:** Gehen Sie nicht zum alten Tag zurück und untersuchen Sie den Fehler.
**Versuchen Sie es mit Branch:** Eröffnen Sie nicht die Filiale Ihres Freundes vor Ort.

## Technische Tiefe und Architektur

Der Ablauf ist wie folgt:

```
git clone https://github.com/ornek/proje.git
cd proje
git checkout v2.0.0
```

Auszeichnungen:

**Klon:** Zum ersten Mal das gesamte Repository herunterladen.
**Kasse:** Version oder Zweig im heruntergeladenen Repository ändern.
**Wechseln/Wiederherstellen:** Befehle im modernen Git verzweigen und abrufen.
**Spärlich:** Laden Sie nur den erforderlichen Ordner im riesigen Repository herunter.

Regel: Bestehen Sie nicht, während Sie Ihre Arbeit gespeichert haben, sondern übernehmen Sie sie zuerst oder speichern Sie sie.

## Einsatz in verschiedenen Disziplinen

**Bibliothek:** Nehmen Sie das Buch nicht aus dem Regal und bringen Sie es auf den Tisch.
**Archiv:** Entfernen Sie den Ordner aus dem Speicher und untersuchen Sie ihn.
**Foto:** Lassen Sie sich nicht vom Negativen unter Druck setzen.

## Häufig gestellte Fragen

**Lädt es nur Dateien herunter?**

Nein. Verlaufs- und Versionsinformationen sind ebenfalls enthalten, sodass Sie zur alten Version zurückkehren können.

**Was ist der Unterschied zu Clone?**

Beim Klonen handelt es sich um den ersten Download, beim Auschecken um den Durchgang durch das heruntergeladene Repository. Die Reihenfolge geht in diese Richtung.

**Wie kann ich zur alten Version zurückkehren?**

Es wird mit einem Tag oder Commit-Hash übergeben. Wenn ein gespeicherter Job vorhanden ist, wird dieser zuerst gespeichert.

**Was ist Switch?**

Es ist der moderne Befehl zum Verzweigen. Da das Auschecken viel Arbeit macht, hat Git es in zwei Teile aufgeteilt: Wechsel zum Zweig und Wiederherstellung in der Datei.

## Verwandte Begriffe

- [Git Push](https://trescout.com/de/dictionary/git-push/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)
- [Cloning](https://trescout.com/de/dictionary/cloning/)

## Verwandte Werkzeuge

- [Checkout](https://trescout.com/de/discover/checkout/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/repository-checkout/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/repository-checkout/
