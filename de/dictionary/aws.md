# Was ist AWS?

> Amazon Web Services

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-22

AWS (Amazon Web Services) ist die führende Cloud-Computing-Plattform von Amazon, die Rechenleistung, Datenbanken, Speicherplatz und skalierbare IT-Infrastruktur bedarfsgerecht über das Internet bereitstellt.

## Definition und Wortherkunft
Anstatt kapitalintensive eigene Rechenzentren aufzubauen, mieten Unternehmen flexible Serverkapazitäten in den weltweiten Rechenzentren von Amazon. Die Leistung wächst bei Besucheranstürmen dynamisch mit und schrumpft bei geringer Last, abgerechnet nach tatsächlichem Verbrauch.

## Alltägliche Anwendung und Praxis
- **Webplattformen:** Automatisch skalierende Servercluster bei unvorhersehbaren Zugriffswellen.
- **Archivierung & Backups:** Hochverfügbarer Objektspeicher für geschäftskritische Unternehmensdaten.
- **Medien-Streaming:** Edge-Netzwerke für latenzfreie weltweite Auslieferung von Videoinhalten.
- **Startups:** Sofortiger Start marktfähiger Cloud-Architekturen ohne Investitionskosten in Serverräume.

## Technische Tiefe und Architektur
Zentrale Basisinfrastruktur-Dienste:- **EC2:** Virtuelle Serverinstanzen mit flexiblen CPU- und Arbeitsspeicherkonfigurationen.
- **S3:** Zuverlässiger Objektspeicher mit höchster Ausfallsicherheit für Dokumente und Medien.
- **RDS:** Vollständig verwaltete relationale Datenbanken wie PostgreSQL und MySQL.
- **Lambda:** Ereignisgesteuerte serverlose Codeausführung ohne manuelle Serveradministration.

Das System basiert auf weltweiten Regionen und redundanten Verfügbarkeitszonen (Availability Zones). Nach dem Modell der geteilten Verantwortung sichert Amazon die Hardware ab, während Kunden ihre Anwendungsdaten und Zugriffsschlüssel verwalten.<div class="disc-cmd"><div class="disc-cmd-head"><span>Aktive EC2-Instanzen mit der AWS CLI abfragen</span></div><pre><code>aws ec2 describe-instances --query "Reservations[].Instances[].State.Name"</code></pre></div>

## Häufig verwechselt mit
Wird häufig mit gewöhnlichem Webhosting verwechselt. Ein Standard-Webhoster stellt lediglich Dateispeicher für Webseiten bereit; AWS ist ein Technologiebaukasten aus über 200 professionellen Rechen-, Netzwerk- und KI-Diensten.

## Interdisziplinäre Perspektiven
- **Stromnetz:** Strom aus der Steckdose beziehen, anstatt ein eigenes Kraftwerk zu betreiben.
- **Mietlager:** Je nach Warenbestand flexibel Lagerboxen anmieten und kündigen.
- **Carsharing:** Mobilität nach Kilometern abrechnen, ohne eigene Fahrzeugflotten zu erwerben.

## Als Analogie
Es gleicht dem Strombezug aus dem öffentlichen Netz: Sie stecken den Stecker in die Wand und zahlen exakt für die Kilowattstunden, die Sie tatsächlich verbraucht haben.

## Häufige Fragen

**Warum migrieren Entwickler zu AWS?**  
Um teure Hardwareinvestitionen zu vermeiden, weltweit innerhalb von Minuten zu skalieren und Wartungsarbeiten auszulagern.

**Gibt es ein kostenloses Kontingent?**  
Ja. Das AWS Free Tier bietet neuen Nutzern begrenzte monatliche Freikontingente für EC2, S3 und Lambda zum Kennenlernen der Plattform.

**Wo werden meine Kundendaten physisch gespeichert?**  
Ausschließlich in der bei der Einrichtung explizit gewählten Rechenzentrumsregion (z. B. Frankfurt für DSGVO-Konformität).

**Wie lassen sich Rechnungsüberraschungen vermeiden?**  
Durch das Einrichten von Kostenwarnungen in AWS Budgets und das konsequente Löschen ungenutzter Speicherressourcen.

## Verwandte Begriffe
- [Cloud Computing](/de/dictionary/cloud-computing/)
- [IaaS](/de/dictionary/iaas/)
- [PaaS](/de/dictionary/paas/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/aws/
