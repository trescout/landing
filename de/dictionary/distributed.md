# Was ist Distributed?

*Entwicklung · Zuletzt aktualisiert: 19. September 2026*

Verteilt ist in der Computerwelt die gemeinsame Nutzung von Hardware, Daten und Berechnungsprozessen auf viele unabhängige Server (Knoten), die über das Netzwerk miteinander verbunden sind, anstelle einer einzigen zentralen Maschine, und dieses System dient dem Endbenutzer so, als wäre es ein einziger vollständiger Computer.

## Etymologie und die Natur verteilter Systeme

Das Wort „Distributed“ bedeutet auf Türkisch verteilt. Leslie Lamport, einer der Pioniere der Informatik, definierte verteilte Systeme mit dem folgenden Aphorismus, der in die Geschichte einging: „Ein verteiltes System ist ein System, in dem der Absturz eines Computers, von dem Sie nicht einmal wissen, dass er existiert, Ihren eigenen Computer unbrauchbar machen kann.“

In zentralisierten (monolithischen) Architekturen erfolgen alle Vorgänge auf einem einzigen Hauptspeicher und Prozessor. In verteilten Systemen dienen Hunderte von Knoten, die physisch über Rechenzentren auf verschiedenen Kontinenten der Welt verteilt sind, einem gemeinsamen Zweck, indem sie über unzuverlässige Netzwerkkabel kommunizieren.

## 8 Irrtümer des verteilten Rechnens

In den 1990er Jahren listeten die Sun Microsystems-Ingenieure L. Peter Deutsch und James Gosling die „8 tödlichen Fehler“ auf, die Softwareentwickler bei der Entwicklung verteilter Systeme machten. Alle Verteidigungslinien moderner Cloud- und Microservice-Architekturen basieren auf diesen Missverständnissen:

1. Das Netzwerk ist zuverlässig: In der Realität gehen Pakete verloren, Glasfaserleitungen brechen ab, Router stürzen ab.
2. Die Latenz ist Null: Blitzgeschwindigkeit und Latenz beim Netzwerkwechsel zwischen zwei Maschinen sind immer vorhanden.
3. Die Bandbreite ist unendlich: Mit steigendem Datenvolumen verstopfen die Netzwerkleitungen.
4. Das Netzwerk ist sicher: Die gesamte verteilte Kommunikation erfolgt über offene Leitungen und erfordert kryptografischen Schutz.
5. Die Topologie ändert sich nicht: Server werden ständig ein- und ausgeschaltet, IP-Adressen ändern sich.
6. Es gibt nur einen Systemadministrator: Mehrere Teams und Cloud-Anbieter sind beteiligt.
7. Transportkosten sind Null: Serialisierungs- und CPU-Verpackungskosten können nicht ignoriert werden.
8. Das Netzwerk ist homogen: Linux, Windows, ARM, x86 und verschiedene Protokolle arbeiten im System zusammen.

## CAP-Theorem und PACELC-Modell

Das von Eric Brewer vorgeschlagene CAP-Theorem zeigt die grundlegenden Grenzen der verteilten Datenverwaltung auf. Wenn eine Netzwerkpartition (P) auftritt, muss das System eine von zwei Optionen wählen:

- CP (Konsistenz + Partitionstoleranz): Das System wählt Konsistenz. Knoten, deren Daten veraltet sind, verweigern die Antwort; Die Zugänglichkeit wird geopfert (z. B. Finanz- und Bankgeschäfte).
- AP (Verfügbarkeit + Partitionstoleranz): Das System wählt die Verfügbarkeit aus. Knoten antworten weiterhin, aber einige Benutzer sehen möglicherweise veraltete Daten von vor ein paar Sekunden (z. B. Social-Media-Feeds).

In modernen Systemen wird das PACELC-Modell von Daniel Abadi verwendet: Wenn das Netzwerk geteilt ist (P) Verfügbarkeit oder Konsistenz; Wird bei normalem Betrieb des Systems auf Else (E) Latency (geringe Latenz) oder Consistency (sofortige Konsistenz) abgezielt?

## Konsensprotokolle: Raft und Paxos

Konsensalgorithmen wurden entwickelt, damit unabhängige Server, die einander nicht vertrauen und jederzeit ausfallen können, sich auf eine einzige Wahrheit einigen können:

- Paxos: Konsensalgorithmus, entwickelt von Leslie Lamport, mathematisch bewährt, aber äußerst komplex in der Praxis umzusetzen.
- Raft: Ein von Diego Ongaro und John Ousterhout entwickeltes Mensch-Intelligenz-Konsensprotokoll, um die Komplexität von Paxos zu lösen. Leader Election basiert auf Log Replication und Safety State Machines (es funktioniert im Herzen riesiger Systeme wie Etcd, Kubernetes, Consul).
- Byzantinische Fehlertoleranz (BFT): Sie ist die Grundlage von Blockchain-Protokollen, die einen Konsens auch in Umgebungen gewährleisten, in denen einige Knoten absichtlich fehlerhafte oder bösartige Informationen verbreiten.

## Das Zeitproblem in verteilten Systemen und Lösungen

Auf einem zentralen Computer zeigt die Hardware-Uhr eine einzige Wahrheit an. In verteilten Systemen hingegen weisen Serveruhren physikalische Abweichungen (Clock Drift) auf, und das NTP (Network Time Protocol) reicht für eine millisekundengenaue Präzision nicht aus:

- Lamport Logical Times (Lamport Timestamps): Definiert die „Reihenfolge der Ereignisse“ anstelle der physischen Zeit.
- Vector Clocks: Erkennt Datenkonflikte, indem ermittelt wird, welche Daten die Ursache oder Wirkung der anderen sind.
- Google TrueTime: Kombination aus Atomuhren und GPS-Antennen, die in der verteilten Google Spanner-Datenbank verwendet werden. Es ermöglicht ACID-Transaktionen auf globaler Ebene, indem es die Unsicherheitsspanne auf wenige Millisekunden reduziert.

## Verteilte Daten- und Transaktionsverwaltung: Saga-Muster

Datenbanktransaktionen (ACID-Transaktionen) in monolithischen Systemen werden durch den Saga-Pattern-Ansatz in Microservices ersetzt. Anstatt lang laufende verteilte Schritte mit zweiphasigen Sperren zu sperren (2PC – Two Phase Commit); Es werden ereignisgesteuerte Architekturen verwendet, bei denen jeder Dienst seine lokale Aktion ausführt und im Fehlerfall rückwärts kompensierende Transaktionen ausgelöst werden.

## Fragen und Antworten

**Was bedeutet distributed (türkische Bedeutung)?**

Bedeutet in der IT-Terminologie 'verteilt'. Es bezeichnet die Aufteilung von Rechenleistung, Speicherplatz oder Datenbanken auf zahlreiche unabhängige Maschinen, die über ein Netzwerk kommunizieren, anstatt sie auf einem einzigen Server zu belassen.

**Was bedeutet das CAP-Theorem in der Praxis?**

Es besagt, dass bei einer Unterbrechung oder Verzögerung der Netzwerkverbindung (Partitionierung) das System entweder die aktuellsten Daten garantieren und einige Anfragen zurückstellen muss (Konsistenz) oder um den Preis veralteter Daten sofort auf jede Anfrage antworten muss (Verfügbarkeit).

**Warum wird der Raft-Konsensalgorithmus in verteilten Systemen eingesetzt?**

Er wird verwendet, um sicherzustellen, dass selbst dann, wenn einige der Server im Netzwerk abstürzen, die verbleibende Mehrheit der Knoten (Quorum) einen neuen Anführer unter sich wählen und die Datenbankprotokolle verlustfrei im gesamten Cluster synchronisiert werden können.

**Warum wird das Saga-Muster dem Two-Phase Commit (2PC) vorgezogen?**

2PC (Two-Phase Commit) sperrt Datenbankressourcen auf verteilten Knoten und blockiert das gesamte System, wenn eine Maschine nicht antwortet. Das Saga-Muster hingegen nutzt asynchrone Ereignisse und Kompensationsschritte, um die hohe Verfügbarkeit des Systems aufrechtzuerhalten.

## Verwandte Begriffe

- [Cloud Computing](https://trescout.com/de/dictionary/cloud-computing/)
- [Network Stack](https://trescout.com/de/dictionary/network-stack/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)

## Verwandte Werkzeuge

- [Elasticsearch](https://trescout.com/de/discover/elasticsearch/)
- [Cassandra](https://trescout.com/de/discover/cassandra/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/distributed/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/distributed/
