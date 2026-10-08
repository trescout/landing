# Was ist Virtual Machines?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Eine Virtual Machine (auf Deutsch: virtuelle Maschine) ist ein unabhängiger Computer, der sich die Hardware teilt.

## Definition und Wortherkunft

Virtual bedeutet virtuell. Mehrere Betriebssysteme laufen auf einer einzigen Maschine. Jedes läuft isoliert mit eigenen Ressourcen und beschädigt das Hauptsystem nicht.

***Analogie:** Ähnlich wie das Vermieten von Zimmern mit separaten Türen in einem einzigen Haus.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Moderator:** Mandantenfähiges Hosting (Multi-Tenant).
**Test:** Ausprobieren verschiedener Systeme.
**Entwicklung:** Saubere Testumgebung.

## Technische Tiefe und Architektur

Schichten:

**Hypervisor:** Die Software, die die Hardware aufteilt.
**Gast:** Das oben laufende System.
**Snapshot:** Schnappschuss, Rückfahrkarte.

Schnelle Maschine:

```
multipass launch --name test --cpus 2 --memory 4G
```

Container-Unterschied: Maschine transportiert System, Container transportiert Anwendung. Die Isolierung ist bei der Maschine stärker.

## Häufig gemischte Dinge

Wird für einen Container gehalten. Maschine ist ein vollständiges System, Container ist ein geteilter Kernel. Das eine ist eine Wohnung, das andere eine Wohngemeinschaft.

## Einsatz in verschiedenen Disziplinen

**Zimmer:** Abteile mit unabhängigen Türen.
**Wohnung:** Gemeinsames Gebäude, privater Bereich.
**Container:** Transport mit Fächern.

## Häufig gestellte Fragen

**Verlangsamt es?**

Es gibt einen Overhead. Bei richtiger Dimensionierung fällt er nicht auf.

**Können Viren übertragen werden?**

Im Allgemeinen nein. Die Isolierung ist stark, der freigegebene Ordner wird überwacht.

**Wie viele Ressourcen werden zugewiesen?**

Wird je nach Aufgabe festgelegt. Wird durch Monitoring schrittweise angepasst.

**Was ist der Unterschied zum Container?**

Die virtuelle Maschine transportiert das System, der Container die Anwendung. Isolierung und Geschwindigkeit werden gegeneinander abgewogen.

## Verwandte Begriffe

- [Containers](https://trescout.com/de/dictionary/containers/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Self-hosting](https://trescout.com/de/dictionary/self-hosting/)

## Verwandte Werkzeuge

- [Container](https://trescout.com/de/discover/container/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/virtual-machines/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/virtual-machines/
