# Was ist Cloud Computing?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Cloud Computing ist die Bereitstellung von IT-Ressourcen wie Servern, Speicher, Datenbanken, Netzwerken und Software über das Internet aus entfernten Rechenzentren bei Bedarf (on-demand), anstatt diese auf physischer lokaler Infrastruktur zu betreiben.

## Definition, etymologischer Ursprung und konzeptionelle Entstehung

Cloud Computing ist ein modernes IT-Modell, das es Unternehmen und Ingenieuren ermöglicht, Rechenleistung, Arbeitsspeicher, Speicherplatz und KI-GPU-Cluster innerhalb von Sekunden über das Internet zu mieten, anstatt eigene Serverräume zu bauen und physische Hardware zu kaufen.

Konzeptionell reichen die Wurzeln bis ins Jahr 1961 zurück, zu einer Rede von John McCarthy, einem der Väter der künstlichen Intelligenz, am MIT. McCarthy sagte voraus, dass Rechenleistung in Zukunft wie Strom und Wasser als öffentliche Dienstleistung (Utility) angeboten werden würde. Die Etablierung des Begriffs „Cloud“ in diesem Sektor geht auf die Telekommunikations- und Netzwerktechnik zurück: In den 1990er Jahren zeichneten Systemarchitekten komplexe Telefonzentralen und das Internet-Backbone, deren Details sie abstrahieren wollten, als „Cloud-Symbol“ in ihre Diagramme ein. Mit der Einführung von Amazons Simple Storage Service (S3) und Elastic Compute Cloud (EC2) für Entwickler im Jahr 2006 wurde das auf Investitionsausgaben (CapEx) basierende Modell des Serverkaufs durch das Prinzip der nutzungsabhängigen Bezahlung (OpEx) ersetzt.

***Analogie:** Es ist vergleichbar damit, sich direkt an das nationale Stromnetz anzuschließen, anstatt ein eigenes Wasserkraftwerk oder einen Generator im Garten Ihrer Fabrik oder Ihres Hauses zu installieren. Sobald Sie den Stecker in die Steckdose stecken, fließt Strom; egal wie viel Leistung Ihre Maschine verbraucht, Sie zahlen am Monatsende nur für diesen Verbrauch. Um Defekte am Generator, Kraftstoff oder die Wartung des Transformators müssen Sie sich nicht kümmern.*

## Grundlegende Dienst- und Bereitstellungsmodelle (IaaS, PaaS, SaaS, Serverless)

Die Cloud-Computing-Architektur wird je nach Abstraktionsebene in vier Hauptdienstmodelle unterteilt:

1. IaaS (Infrastructure as a Service · Infrastruktur als Dienstleistung): Dies sind die unterste Ebene von rohen virtuellen Maschinen, Blockspeicher-Festplatten und virtuellen Netzwerktopologien. AWS EC2, Google Compute Engine und Azure VM fallen in diese Kategorie. Die Hardware- und Virtualisierungsschicht wird vom Cloud-Anbieter verwaltet; für die Installation des Betriebssystems, Sicherheits-Patches und den Software-Stack ist der Entwickler verantwortlich.
2. PaaS (Platform as a Service · Plattform als Dienstleistung): Hierbei handelt es sich um Plattformen, die Entwickler von der Konfiguration von Servern, Betriebssystemen und Laufzeitumgebungen entlasten. Vercel, Heroku und AWS Elastic Beanstalk sind hierfür Beispiele. Der Entwickler übermittelt lediglich den Quellcode; Skalierung, SSL-Zertifikate und Lastverteilung werden im Hintergrund automatisch abgewickelt.
3. SaaS (Software as a Service · Software als Dienstleistung): Hierbei handelt es sich um schlüsselfertige Softwarelösungen, auf die der Endnutzer direkt über einen Webbrowser oder eine API zugreift und deren Wartung vollständig vom Anbieter übernommen wird. Google Workspace, Slack, Salesforce und Figma sind die bekanntesten Beispiele für dieses Modell.
4. Serverless (FaaS · Function as a Service): Hierbei handelt es sich um eine ereignisgesteuerte Architektur, die das Konzept des Servers vollständig abstrahiert. Code, der auf AWS Lambda oder Cloudflare Workers geschrieben wurde, wird nur dann ausgeführt, wenn ein auslösender HTTP-Request oder ein Datenbankereignis eingeht, läuft innerhalb von Millisekunden ab und beendet sich anschließend wieder. Bei ausbleibendem Traffic entstehen keine Kosten.

Bereitstellungsmodelle richten sich danach, wo die Daten gehostet werden:

- Public Cloud: Eine Struktur, in der Ressourcen in einer Multi-Tenant-Umgebung in den globalen Rechenzentren großer Anbieter gemeinsam genutzt werden.
- Private Cloud: Eine isolierte Umgebung, die von regulierten Branchen wie dem Finanz-, Verteidigungs- und Gesundheitswesen in ausschließlich ihnen zugewiesenen Rechenzentren betrieben wird.
- Hybrid Cloud: Eine hybride Struktur, bei der sensible Kundendaten auf privaten lokalen Servern (on-premise) gespeichert werden, während die Web-Ebene mit hohem Transaktionsvolumen in der Public Cloud läuft.
- Multi-Cloud: Um eine Abhängigkeit von einem einzigen Anbieter (Vendor Lock-in) zu vermeiden, werden Systeme verteilt sowohl auf AWS als auch auf Google Cloud und Azure konfiguriert.

## Informatik und Systemarchitektur: Hypervisor, Container und CAP

Das technische Wunder, das dem Cloud-Computing zugrunde liegt, ist die softwarebasierte Abstraktion der Hardware (Virtualisierung):

- Hypervisor-Schicht: Die Kernsoftware, die die Prozessor- und RAM-Ressourcen eines einzelnen physischen Servers aufteilt und auf Dutzende unabhängige virtuelle Maschinen (VMs) verteilt. Type-1-Bare-Metal-Hypervisor (KVM, VMware ESXi), die direkt auf der Hardware laufen, bilden das Leistungsrückgrat von Cloud-Anbietern.
- Container und Orchestrierung: Um den Overhead durch das Kopieren von Betriebssystemen bei virtuellen Maschinen zu umgehen, entstanden Docker-Container unter Nutzung der cgroups- (Ressourcenbegrenzung) und namespaces-Funktionen (Prozessisolierung) des Linux-Kernels. Die automatisierte Bereitstellung und Selbstheilung von Tausenden von Containern wird durch Kubernetes-Cluster ermöglicht.
- CAP-Theorem und verteilte Ausfallsicherheit: Globale Cloud-Infrastrukturen arbeiten innerhalb der Grenzen von Eric Brewers CAP-Theorem. Im Falle einer Netzwerkpartition (Network Partition) muss ein System entweder die Datenkonsistenz (Consistency) oder die unterbrechungsfreie Verfügbarkeit (Availability) priorisieren. Cloud-Architekten implementieren Disaster-Recovery-Szenarien durch geografisch redundante (Multi-Region / Availability Zone) Architekturen.
- Modell der geteilten Verantwortung (Shared Responsibility): Die Sicherheit in der Cloud ist zweigeteilt. Der Anbieter ist für die Sicherheit der physischen Rechenzentren, Server, Hypervisor und Netzwerkkabel verantwortlich („Security OF the Cloud“). Der Kunde hingegen ist für Betriebssystem-Updates, Verschlüsselung, IAM-Rollen (Zugriffsverwaltung) und Schwachstellen im Anwendungscode verantwortlich („Security IN the Cloud“).

## Wirtschaftliche, ökologische und geopolitische Dimension

Cloud-Computing ist nicht nur eine technische Revolution, sondern auch ein massiver Umbruch bei der globalen Ressourcenallokation:

- Jevons-Paradoxon: Das Prinzip, das der Ökonom William Stanley Jevons im 19. Jahrhundert für den Kohleverbrauch aufstellte, gilt auch für die Cloud: Wenn der Zugang zu Rechenleistung billiger und einfacher wird, sinkt der Gesamtverbrauch nicht, sondern steigt im Gegenteil exponentiell an. Dass heute KI-Modelle mit Hunderten Milliarden Parametern trainiert werden können, ist das direkte Ergebnis der Skaleneffekte, die das Cloud-Computing bietet.
- Energie- und Wasserverbrauch: Hyperscale-Rechenzentren verbrauchen etwa 1-2 % des weltweiten Stroms, und für die Kühlung riesiger GPU-Cluster werden Millionen Kubikmeter Frischwasser benötigt. Dies hat dazu geführt, dass Rechenzentren zwingend in der Nähe von erneuerbaren Energiequellen und in kühleren Klimazonen errichtet werden müssen.
- Digitale Souveränität und rechtliche Rahmenbedingungen: Wo Daten physisch gespeichert sind, ist eine geopolitische Frage. Während der US CLOUD Act amerikanischen Unternehmen den Zugriff auf Server im Ausland ermöglicht, fördern die Europäische Union mit der DSGVO und der GAIA-X-Initiative sowie die Türkei mit der KVKK-Gesetzgebung den Verbleib kritischer Daten innerhalb der nationalen Grenzen.

## Häufig verwechselt mit

- Cloud-Speicher vs. Cloud-Computing: Google Drive, iCloud oder Dropbox sind reine Speicherdienste; Cloud-Computing hingegen ist ein riesiges Ökosystem, das neben der Speicherung auch dynamische Rechenleistung, KI-Training, Netzwerkmanagement und Datenbank-Orchestrierung umfasst.
- Serverless vs. wirklich serverlos: In einer Serverless-Architektur gibt es natürlich physische Server; der Begriff „serverlos“ bedeutet lediglich, dass sich der Entwickler nicht mehr um die Konfiguration, Aktualisierung oder Überwachung eines Servers kümmern muss, da die Serververwaltung durch den Anbieter unsichtbar gemacht wird.

## Häufige Fragen

**Was bedeutet Cloud Computing und was ist die deutsche Entsprechung?**

Es bedeutet auf Deutsch 'Cloud-Computing'. Es ist ein Modell, bei dem Rechenleistung, Server und Speicherressourcen nicht auf lokalen Computern, sondern über das Internet-Backbone bei Bedarf sofort gemietet werden.

**Was ist der grundlegende Unterschied zwischen den 3 Hauptdienstmodellen des Cloud-Computing (IaaS, PaaS, SaaS)?**

IaaS ist das Mieten von Rohhardware und virtuellen Servern (AWS EC2), PaaS ist eine Umgebung zum direkten Ausführen und Hosten von Code (Vercel), und SaaS ist schlüsselfertige Software, die dem Endbenutzer über das Web bereitgestellt wird (Google Docs).

**Was bedeutet das Modell der geteilten Verantwortung (Shared Responsibility Model)?**

Es ist eine Arbeitsteilung im Bereich Sicherheit, bei der der Cloud-Anbieter für den Schutz der physischen Infrastruktur, des Rechenzentrums und der Hardware verantwortlich ist, während der Benutzer für seine eigene Anwendungssicherheit, Benutzerberechtigungen (IAM) und Datenverschlüsselung verantwortlich ist.

**Wie lässt sich eine Abhängigkeit vom Cloud-Anbieter (Vendor Lock-in) vermeiden?**

Durch die Verwendung von Open-Source-Standards (Docker-Container, Kubernetes), unabhängigen Datenbank-Engines (PostgreSQL) und Infrastructure-as-Code-Tools (Terraform / OpenTofu) wird die Software von anbieterspezifischen proprietären APIs isoliert.

## Verwandte Begriffe

- [SaaS](https://trescout.com/de/dictionary/saas/)
- [PaaS](https://trescout.com/de/dictionary/paas/)
- [IaaS](https://trescout.com/de/dictionary/iaas/)
- [Personal Cloud](https://trescout.com/de/dictionary/personal-cloud/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Network Stack](https://trescout.com/de/dictionary/network-stack/)
- [Memory Management](https://trescout.com/de/dictionary/memory-management/)

## Verwandte Werkzeuge

- [DevOps-Interview-Guide](https://trescout.com/de/discover/devops-interview-guide/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/cloud-computing/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/cloud-computing/
