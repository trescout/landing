# Was ist IaaS?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

> Infrastructure as a Service

IaaS (Infrastructure as a Service, Infrastruktur als Dienstleistung) ist die Anmietung von Hardware.

## Definition und Wortherkunft

Wenn die Leistung nicht ausreicht, werden Teile aus einem riesigen Rechenzentrum gemietet. Das Betriebssystem und die Software liegen bei Ihnen, die Verantwortung für die Hardware beim Anbieter. Der Vergleich mit einem unbebauten Grundstück ist treffend: Die Infrastruktur ist bereit, das Gebäude gehört Ihnen.

***Analogie:** Ähnlich wie die Miete eines unbebauten Grundstücks; die Infrastruktur ist bereit, das Gebäude gehört Ihnen.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Website:** Maschine je nach Datenverkehr.
**Backup:** Remote-Festplatte.
**Test:** Temporäre Umgebung.

## Technische Tiefe und Architektur

Schichten:

**Virtuelle Maschine:** Prozessor- und Speichersegment.
**Speicher:** Block- und Objektspeicher.
**Netzwerk:** Virtuelles Netzwerk und Adresse.

Maschine als Code:

```
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t3.micro"
}
```

Kostenregel: Wer die Maschine vergisst auszuschalten, zahlt. Disziplin bei Tags und Alarmen ist unerlässlich.

## Häufig gemischte Dinge

Wird oft für PaaS gehalten. IaaS stellt Hardware bereit, PaaS bietet eine fertige Umgebung. Das eine ist ein Grundstück, das andere eine möblierte Wohnung.

## Einsatz in verschiedenen Disziplinen

**Grundstück:** Erschlossenes unbebautes Land.
**Lager:** Lagerhalle mit fertigen Regalen.
**Feld:** Miete von gepflügtem Boden.

## Häufig gestellte Fragen

**Ist IaaS sicher?**

Die Infrastruktur ist sicher, für die interne Sicherheit sind Sie verantwortlich. Disziplin bei Patches und Zugriffen ist unerlässlich.

**Was ist der Unterschied bei PaaS?**

IaaS bietet Hardware, PaaS bietet eine Umgebung. Wenn Sie die Kontrolle behalten wollen, wählen Sie das Erste; wenn Geschwindigkeit gefragt ist, das Zweite.

**Wie lassen sich die Kosten kontrollieren?**

Nicht genutzte Ressourcen abschalten, die richtige Größe wählen und Alarme einrichten.

**Wann sollte man es wählen?**

Wenn volle Kontrolle und eine individuelle Einrichtung erforderlich sind. Bei Standardaufgaben ist PaaS ausreichend.

## Verwandte Begriffe

- [SaaS](https://trescout.com/de/dictionary/saas/)
- [PaaS](https://trescout.com/de/dictionary/paas/)
- [Virtual Machines](https://trescout.com/de/dictionary/virtual-machines/)

## Verwandte Werkzeuge

- [Free for Dev](https://trescout.com/de/discover/free-for-dev/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/iaas/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/iaas/
