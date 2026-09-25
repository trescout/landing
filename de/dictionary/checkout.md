# Was bedeutet Checkout? E-Commerce vs. Git

> Englisch: Checkout · Wortherkunft: englisch check (prüfen) + out (hinaus/Abschluss)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-19

Checkout ist ein Begriff mit zwei zentralen technischen Bedeutungen: der finale Bezahl- und Bestellvorgang im Online-Handel oder die Git-Operation zum Wechseln von Entwicklungszweigen und Wiederherstellen von Dateien.

## Als Analogie
Im Supermarkt ist der Checkout das Kassenband, an dem Sie bezahlen und den Beleg erhalten; in einer Leihbibliothek ist es die Verbuchung am Schalter, um ein Buch von der Ausleihe mit nach Hause zu nehmen.

## 1. Checkout-Architektur im E-Commerce und SaaS
Im Online-Handel beschreibt der Checkout den umsatzkritischen Übergang vom Warenkorb zur verbindlichen Bestellung. Systemisch steuert dieser Schritt Warenbestandsreservierungen, Adressvalidierungen und die Anbindung von Zahlungsdienstleistern über tokenisierte Schnittstellen (z. B. Stripe Elements), sodass sensible Kartendaten den Händlerserver nie berühren.

## 2. Checkout im Versionskontrollsystem Git
Für Programmierer ist <code>git checkout</code> die klassische Anweisung, um den HEAD-Zeiger auf einen anderen Entwicklungszweig (Branch) oder Commit zu richten und das Arbeitsverzeichnis entsprechend anzupassen. Seit Git 2.23 wurde dieser überladene Befehl in <code>git switch</code> (Zweigwechsel) und <code>git restore</code> (Dateien zurücksetzen) präzisiert.

## Vergleich: E-Commerce gegen Git Checkout
Gegenüberstellung der beiden Domänen:
- **E-Commerce-Checkout:** Finanztransaktion mit Bestandsreservierung, Steuerberechnung und Webhook-Bestätigungen.- **Git Checkout:** Lokale Dateisystem-Operation zur Aktualisierung des HEAD-Zeigers und Wiederherstellung von Dateiversionen.- **Fehlerfolgen:** Im E-Commerce führt ein Ausfall zu Warenkorbabbrüchen; in Git führt Fehlbedienung zu einem abgetrennten Zustand (detached HEAD).

## Häufige Fragen

**Warum wurde 'git checkout' durch 'switch' und 'restore' ergänzt?**  
Weil der alte checkout-Befehl zu viele Aufgaben vereinte: Zweige wechseln und lokale Dateien überschreiben. Die Aufteilung verhindert Datenverlust.

**Wie verringert man Kaufabbrüche beim E-Commerce-Checkout?**  
Durch One-Click-Zahlungsarten wie Apple Pay oder Google Pay sowie Gast-Bestellungen ohne verpflichtende Kontoerstellung.

**Was bedeutet ein 'detached HEAD' in Git?**  
Es bedeutet, dass man direkt auf einem einzelnen Commit statt auf einem Zweig arbeitet; neue Commits werden keinem Branch zugeordnet.

**Welchen Zweck erfüllt ein Idempotenz-Schlüssel bei Online-Zahlungen?**  
Er stellt sicher, dass wiederholte Netzwerkanfragen die Kreditkarte des Kunden bei Verbindungsabbrüchen nicht versehentlich doppelt belasten.

## Verwandte Begriffe
- [API](/de/dictionary/api/)
- [SaaS](/de/dictionary/saas/)
- [Git Push](/de/dictionary/git-push/)

## Verwandte Tools
- [Checkout](/de/discover/checkout/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/checkout/
