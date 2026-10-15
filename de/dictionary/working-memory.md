# Was ist Working Memory?

*Künstliche Intelligenz · Zuletzt aktualisiert: 22. September 2026*

Arbeitsspeicher (im Englischen Working Memory) ist die temporäre Information, die das Modell für die aktuelle Aufgabe bereithält.

## Definition und Wortherkunft

Sobald die Aufgabe beendet ist oder sich der Kontext ändert, wird der Inhalt gelöscht. Das Kontextfenster ist der Behälter für die aktiven Informationen im Arbeitsspeicher. Der Chatverlauf und Zwischenergebnisse werden hier gespeichert.

***Analogie:** Es ist wie flüchtige Notizen am Rand beim Lösen von Mathematikaufgaben; sobald das Problem gelöst ist, verlieren sie ihre Bedeutung.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Chat:** Erinnerung an vorherige Nachrichten.
**Schlussfolgerung:** Speicherung von Zwischenschritten.
**Fahrzeug:** Zwischenspeicherung von Aufrufergebnissen.

## Technische Tiefe und Architektur

Budgetberechnung:

```
bağlam: 128K token
geçmiş: 100K → kalan 28K
```

Bei einem Überlauf verabschiedet sich das Modell von alten Daten: Es werden Kürzungen, Zusammenfassungen oder Verschiebungen angewendet. RAG-Unterschied: RAG ruft Informationen von außen ab, der Arbeitsspeicher hält die aktuellen Informationen. Beide arbeiten zusammen.

## Häufig gemischte Dinge

Wird oft für das Langzeitgedächtnis gehalten. Das ist das dauerhafte Profil, dies ist die temporäre Werkbank. Wenn die Sitzung endet, wird dieser Bereich geleert.

## Einsatz in verschiedenen Disziplinen

**Randnotiz:** Die Kritzelei, die weggeworfen wird, wenn das Problem gelöst ist.
**Stand:** Das Werkzeug, das nach getaner Arbeit weggeräumt wird.
**RAM:** Der Bereich, der gelöscht wird, wenn der Strom unterbrochen wird.

## Häufig gestellte Fragen

**Was passiert, wenn es voll ist?**

Alte Informationen werden vergessen, der Kontext verschiebt sich. Es wird durch Zusammenfassen und Beschneiden verwaltet.

**Wie wird es vergrößert?**

Es wird ein Modell mit einem größeren Fenster gewählt oder externe Informationen werden mittels RAG hinzugefügt.

**Was ist der Unterschied bei RAG?**

RAG holt Informationen von außen, der Speicher hält den aktuellen Moment fest. Beide ergänzen sich.

**Vergisst es?**

Ja. Es ist ein temporärer Bereich, Dauerhaftigkeit wird nicht erwartet. Dauerhafte Informationen werden extern geschrieben.

## Verwandte Begriffe

- [Memory](https://trescout.com/de/dictionary/memory/)
- [Context Window](https://trescout.com/de/dictionary/context-window/)
- [Long-term Memory](https://trescout.com/de/dictionary/long-term-memory/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/working-memory/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/working-memory/
