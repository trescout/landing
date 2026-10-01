# Was ist Service Mesh?

Ein Service Mesh ist die unsichtbare Infrastrukturschicht, die den Datenverkehr von Microservices verwaltet.

## Definition und Wortherkunft
In Systemen mit Hunderten von Komponenten ist es schwierig, dass sich die Teile gegenseitig finden und sicher miteinander kommunizieren. Das Service Mesh steuert die Kommunikation, regelt den Datenverkehr und sorgt für Sicherheit. Es wendet Netzwerkrichtlinien an, ohne den Code zu berühren.

## Wie kann man es kennen und im täglichen Leben anwenden?
Cloud: Große Anwendungen mit Microservices.Bank: Service-Traffic mit strenger Sicherheit.E-Commerce: Bestellpipeline unter Kampagnenlast.

## Technische Tiefe und Architektur
Teile:

## Einsatz in verschiedenen Disziplinen
Flughafen: Der Turm, der Kollisionen von Flugzeugen verhindert.Verkehr: Ein Signalnetzwerk, das den Fluss regelt.Post: Das Verteilerzentrum, das die Sendung trennt.

## Häufig gestellte Fragen
**Ist es für jedes Projekt notwendig?**
Nein. Bei Systemen mit wenigen Diensten bringt es zusätzlichen Aufwand. Es ergibt erst Sinn, wenn die Komplexität zunimmt.

**Wie hoch sind die Kosten?**
Es fügt Speicher und Latenz pro Proxy hinzu. Dies ist der Preis, der für den Gewinn an Beobachtbarkeit gezahlt wird.

**Ist Kubernetes zwingend erforderlich?**
Nein, aber sie werden meistens zusammen verwendet. Es gibt auch Versionen, die auf virtuellen Maschinen laufen.

**Ersetzt es ein API-Gateway?**
Nein. Das Gateway ist das Eingangstor, das Mesh ist der interne Datenverkehr. Die beiden arbeiten zusammen.


## Verwandte Begriffe
- [Cloud Native](/de/dictionary/cloud-native/)
- [API](/de/dictionary/api/)
- [Proxy](/de/dictionary/proxy/)

## Verwandte Werkzeuge
- [Meshery](/de/discover/meshery/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/service-mesh/
