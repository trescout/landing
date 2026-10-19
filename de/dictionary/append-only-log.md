# Was ist Append-only log?

*Daten und Infrastruktur · Zuletzt aktualisiert: 20. September 2026*

Das Nur-Anhängen-Protokoll ist eine unveränderliche Datenstrukturarchitektur, in der Daten niemals vor Ort geändert oder gelöscht werden. Jede neue Transaktion wird in chronologischer Reihenfolge an das Ende der Datei angehängt.

## Etymologie und das Invarianzparadigma

Das Append-Only-Log-Konzept wurde als radikale Alternative zum „Update-in-Place“-Paradigma traditioneller Datenbanken entwickelt. In klassischen Datenbanken werden bei der Aktualisierung eines Kontostands oder Profils die alten Daten auf der Festplatte gelöscht und mit dem neuen Wert überschrieben. Dieser Ansatz führt zu ernsthaften Zuverlässigkeitsproblemen aufgrund unvollständiger Schreibvorgänge, die Daten im Falle eines Systemabsturzes, Deadlock-Engpässen und zufälligem Festplattenzugriff (zufällige E/A) beschädigen.

In der Nur-Anhänge-Protokollarchitektur ist der Verlauf heilig und kann nicht manipuliert werden. Anstatt den Kontostand direkt zu ändern, wird jede Ein- und Auszahlungstransaktion als neuer Datensatz am Ende des Journals hinzugefügt. Der aktuelle Zustand des Systems ist ein natürliches Ergebnis der Faltung/Reduzierung all dieser Ereignisse, die von der Vergangenheit zur Gegenwart in chronologischer Reihenfolge hinzugefügt wurden. Dieses Prinzip bildet das Rückgrat moderner verteilter Systeme, leistungsstarker Speicher-Engines und Blockchain-Netzwerke.

***Analogie:** Stellen Sie sich das offizielle Journal vor, das von einem Buchhalter geführt wird. Wenn der Buchhalter in einer Zeile einen Fehler macht, kann er die vorherigen Seiten nicht öffnen und die alte Nummer nicht mit der Korrekturflüssigkeit löschen. Stattdessen wird der letzten Leerzeile des Hauptbuchs eine neue Umkehrbuchungszeile hinzugefügt, wodurch der Fehler korrigiert wird. Das Hauptbuch wächst nur vorwärts, die Vergangenheit wird nie verändert; Wann und wie sich Geld bewegt, kann im Nachhinein überprüft werden. Das Nur-Anhängen-Protokoll ist genau dieses digitale Hauptbuch. Es zeichnet Daten als lebendige Geschichte auf, nicht als Momentaufnahme.*

## Technische Tiefe und Systemarchitektur

Auf technischer Ebene basiert die Append-Only-Logging-Architektur auf drei Hauptpfeilern in Bezug auf Hardwareoptimierungen und Datenkonsistenz:

- Sequentielle Festplattenzugriffe (Sequentielle I/O) und WAL: Magnetplatten (HDD) und sogar moderne Solid-State-Laufwerke (SSD/NVMe) arbeiten beim Schreiben in aufeinanderfolgende Blöcke mit einer um Größenordnungen höheren Effizienz als beim Schreiben an zufällige Adressen. Aus diesem Grund verwenden Datenbanken wie PostgreSQL, MySQL und SQLite Write-Ahead Logging (WAL). Wenn eine Transaktion stattfindet, wird eine Nur-Anhänge-Protokollzeile sequentiell auf die Festplatte geschrieben und fsynced. Selbst wenn die Stromversorgung des Servers plötzlich unterbrochen wird, wird auf diese Weise das Protokoll beim Neustart von Anfang an gelesen und die Datenbank wird innerhalb von Sekunden in ihren vollständig konsistenten Zustand zurückversetzt.
- LSM-Tree und Komprimierung: Hoch schreibintensive NoSQL-Engines wie RocksDB, Apache Cassandra und Bigtable verwenden die Log-Structured Merge-Tree (LSM-Tree)-Architektur. Alle eingehenden Daten werden zunächst an eine sequentielle Struktur im Speicher (MemTable) und ein gleichzeitiges Nur-Anhänge-Protokoll angehängt. Wenn die MemTable voll ist, wird sie als unveränderliche SSTable-Dateien auf der Festplatte gespeichert. Alte oder ungültige Daten, die sich im Laufe der Zeit ansammeln, werden durch im Hintergrund ausgeführte Komprimierungsprozesse bereinigt.
- Event Sourcing und Distributed Streaming (Kafka): In Microservice-Architekturen funktionieren verteilte Messaging-Plattformen wie Apache Kafka und Redpanda wie ein riesiges verteiltes Nur-Append-Protokoll. Anstatt Anwendungszustände in der Datenbank zu speichern, werden generierte Ereignisse in unveränderliche Dateien geschrieben. Verschiedene Dienste nutzen dieses Protokoll in ihrem eigenen Tempo und erstellen so ihren eigenen lokalen Status.
- Kryptografische Unveränderlichkeit und Blockchain: Distributed-Ledger-Technologien (DLT) wie Bitcoin und Ethereum sind verteilte Nur-Anhänge-Protokolle, bei denen jeder Block den kryptografischen Hash des vorherigen Blocks enthält. Kein Knoten im Netzwerk kann vergangene Blöcke ändern; Am Ende des Ledgers können nur neue Blöcke hinzugefügt werden, die den Konsensregeln entsprechen.

## Soziologische Dimension: Digitales Gedächtnis und Prüfpfad

Das Append-Only-Protokoll ist mehr als nur ein Softwaremuster und verkörpert eine Philosophie der digitalen Verantwortlichkeit und Transparenz. In der Unternehmenswelt und der öffentlichen Verwaltung ist die mit unverwüstlicher Genauigkeit zu beantwortende Frage „Wer hat was wann geändert“ das wichtigste Sicherheitsventil, das Vertrauenskrisen vorbeugt.

In herkömmlichen Systemen macht die Fähigkeit des Datenbankadministrators, den Verlauf mit einem einzigen SQL-Befehl zu löschen und neu zu schreiben, den Unternehmensspeicher anfällig. Nur-Append-Systeme hingegen stellen sicher, dass die Vergangenheit nicht umgeschrieben werden kann, und schaffen so einen mathematischen Immunitätsschutz gegen menschliches Versagen, interne Bedrohungen und Autoritätsmissbrauch.

## Häufige Fehler und Missverständnisse

- Keine Vorhersage des Festplattenverbrauchs: Wenn keine geeigneten Datenaufbewahrungs- und Komprimierungsstrategien etabliert werden und vergessen wird, dass die Protokolle nur wachsen, wird der Festplattenspeicher schnell verbraucht.
- Vernachlässigung der Leseleistung: Das Durchsuchen von Millionen von Protokollzeilen (Wiedergabe) zur Berechnung des endgültigen Status beeinträchtigt die Lesezeit; Es sollten regelmäßig Status-Snapshots erstellt werden.
- DSGVO ignoriert das Recht auf Vergessenwerden: Wenn Gesetze zum Schutz personenbezogener Daten das Recht auf Löschung verlangen, erzwingt das Löschen von Daten aus unveränderlichen Protokollen die Architektur; Dieses Problem soll durch das Krypto-Shredding-Verfahren gelöst werden, bei dem die Daten durch das Löschen des Verschlüsselungsschlüssels bedeutungslos gemacht werden.

## Häufig gestellte Fragen

**Warum ist die Nur-Anhang-Protokollarchitektur schneller als das Update-in-Place-Modell?**

Das sequenzielle Schreiben von Daten bis zum Ende der Datei (sequentielles Schreiben), anstatt nach zufälligen Blöcken auf der Festplatte zu suchen, sorgt für sehr hohe Schreibgeschwindigkeiten, indem die Bewegung des Festplattenkopfs und die E/A-Latenz minimiert werden.

**Wie verwalte ich den Speicherplatz, wenn das Nur-Anhängen-Protokoll für immer wächst?**

Systeme erstellen in regelmäßigen Abständen eine Momentaufnahme der aktuellen Situation und löschen oder archivieren alte Protokolle sicher, indem sie Komprimierungs- oder Segmentbereinigungsprozesse im Hintergrund ausführen.

**Wie verwende ich die Append-Only-Anmeldung in verteilten Systemen und Apache Kafka?**

Kafka-Themen sind partitionierte Nur-Anhänge-Protokolle, in denen Nachrichten in chronologischer Reihenfolge hinzugefügt werden. Mehrere Verbraucher lesen das Protokoll verlustfrei und mit hoher Geschwindigkeit mit unabhängigen Offsetwerten.

**Wie gilt das DSGVO-Recht auf Vergessenwerden für Nur-Anhänge-Protokollierungssysteme?**

Benutzerdaten in der unveränderlichen Datei werden mit einem privaten Schlüssel verschlüsselt; Wenn der Benutzer das Löschen anfordert, wird nur der Verschlüsselungsschlüssel dieses Benutzers zerstört (Krypto-Schreddern), wodurch die Daten unlesbar werden, ohne dass das Protokoll beschädigt wird.

## Verwandte Begriffe

- [Distributed](https://trescout.com/de/dictionary/distributed/)
- [Serialization](https://trescout.com/de/dictionary/serialization/)
- [Local](https://trescout.com/de/dictionary/local/)
- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Memory Management](https://trescout.com/de/dictionary/memory-management/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/append-only-log/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/append-only-log/
