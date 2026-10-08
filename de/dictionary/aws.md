# Was ist Amazon Web Services?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> Amazon Web Services

AWS (Amazon Web Services) ist eine Cloud-Plattform, auf der Sie IT-Dienste wie Server, Speicher und Datenbanken aus dem Internet mieten.

## Definition und Wortherkunft

Anstatt einen eigenen physischen Server zu bauen, mieten Sie Amazon-Rechenzentren. Wenn der Bedarf steigt, erhöht sich die Kapazität, und wenn der Auftrag abgeschlossen ist, verringert sie sich. Es funktioniert mit dem Zahlungsmodell, das mit der Nutzung steigt. Fast alle modernen Anwendungen verfügen über eine solche Cloud-Infrastruktur im Hintergrund.

***Analogie:** Es ist, als würde man Strom aus dem Netz kaufen, anstatt ein eigenes Kraftwerk zu bauen; Sie zahlen nur für das, was Sie nutzen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Webseite:** Server, die je nach Datenverkehr wachsen.
**Sicherung:** Ein scheinbar endloser Dateitresor.
**Video:** Der Inhalt wird so verbreitet, wie er angezeigt wird.
**Startup:** Gehen Sie nicht auf Sendung, ohne einen Serverraum einzurichten.

## Technische Tiefe und Architektur

Grundleistungen:

**EC2:** Virtueller Server zu vermieten.
**F3:** Objektspeicher, Backup und statischer Dateitresor.
**RDS:** Verwaltete relationale Datenbank.
**Lambda:** Serverlose Funktion, die ausgeführt wird, wenn ein Ereignis auftritt.

Konzepte:

**Region und Zugriffszone:** Physischer Speicherort der Daten und Redundanz.
**Gemeinsame Verantwortung:** Die Sicherheit der Cloud liegt in der Verantwortung von Amazon, die Sicherheit der darin enthaltenen Daten liegt bei Ihnen.
**Kostenloses Kontingent:** Begrenzte kostenlose Nutzung für neue Konten.

So listen Sie laufende Server auf:

```
aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"
```

Es empfiehlt sich, einen Budgetalarm einzurichten, um Rechnungsüberraschungen vorzubeugen, da offene und vergessene Ressourcen weiterhin abgebucht werden.

## Häufig gemischte Dinge

Es wird angenommen, dass es sich lediglich um einen Website-Hosting-Dienst handelt. Es handelt sich jedoch um eine vollständige Infrastrukturplattform, die Datenbank-, künstliche Intelligenz-, Netzwerk- und Sicherheitsschichten mit über 200 Diensten abdeckt.

## Einsatz in verschiedenen Disziplinen

**Stromnetz:** Ausstecken statt Schalttafel einbauen.
**Lager zu vermieten:** Mieten Sie so viele Regale wie nötig.
**Taxi:** Reisen, ohne ein Fahrzeug zu besitzen.

## Häufig gestellte Fragen

**Warum sollte ich AWS verwenden?**

Sie haben sofortigen Zugriff auf die Unternehmensinfrastruktur, ohne Investitionen in Hardware tätigen zu müssen. Bei schwankendem Datenverkehr sparen Skalierung und vorgefertigte Dienste Zeit.

**Kann ich kostenlos starten?**

Ja. Der kostenlose Plan sowie die Kredit- und Laufzeitbedingungen für neue Konten können sich im Laufe der Zeit ändern. Bevor Sie beginnen, sollten Sie die aktuellen Limits auf der AWS Free Kontingent-Seite überprüfen.

**Wo werden meine Daten gespeichert?**

Es wird in der von Ihnen gewählten Region aufbewahrt. Für Vorschriften wie KVKK müssen Sie die Region und Verschlüsselung entsprechend Ihrer Richtlinie auswählen.

**Wie behält man die Rechnung unter Kontrolle?**

Mit Budgetwarnungen, Bereinigung ungenutzter Ressourcen und der richtigen Dimensionierung. In kleinen Teams ist Etikettierungsdisziplin unerlässlich.

## Verwandte Begriffe

- [Cloud Computing](https://trescout.com/de/dictionary/cloud-computing/)
- [IaaS](https://trescout.com/de/dictionary/iaas/)
- [PaaS](https://trescout.com/de/dictionary/paas/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/aws/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/aws/
