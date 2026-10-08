# Was ist Service Mesh?

*Glossar · Dev · Zuletzt aktualisiert: 22. September 2026*

Ein Service Mesh ist die unsichtbare Infrastrukturschicht, die den Datenverkehr von Microservices verwaltet.

## Definition und Wortherkunft

In Systemen mit Hunderten von Komponenten ist es schwierig, dass sich die Teile gegenseitig finden und sicher miteinander kommunizieren. Das Service Mesh steuert die Kommunikation, regelt den Datenverkehr und sorgt für Sicherheit. Es wendet Netzwerkrichtlinien an, ohne den Code zu berühren.

***Analogie:** Es ist wie der Turm, der den Flugverkehr an einem großen Flughafen steuert; er sorgt dafür, dass sich die Dienste sicher bewegen, ohne miteinander zu kollidieren.*

## Wie kann man es kennen und im täglichen Leben anwenden?

**Cloud:** Große Anwendungen mit Microservices.
**Bank:** Service-Traffic mit strenger Sicherheit.
**E-Commerce:** Bestellpipeline unter Kampagnenlast.

## Technische Tiefe und Architektur

Teile:

**Sidecar:** Der kleine Proxy neben jedem Service, über den der Datenverkehr fließt.
**Control Plane:** Das Gehirn, das die Regeln verteilt.
**Data Plane:** Die Proxies, die die Arbeit erledigen.
**mTLS:** Verschlüsselte Identität zwischen Diensten.
**Resilienz:** Wiederholungsversuch und Leistungsschalter (Circuit Breaker).

Wiederholungsregel:

```
retries:
  attempts: 3
  perTryTimeout: 2s
```

Istio und Linkerd sind bekannte Implementierungen. Bei kleinen Systemen übersteigen die Kosten den Nutzen.

## Einsatz in verschiedenen Disziplinen

**Flughafen:** Der Turm, der Kollisionen von Flugzeugen verhindert.
**Verkehr:** Ein Signalnetzwerk, das den Fluss regelt.
**Post:** Das Verteilerzentrum, das die Sendung trennt.

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

- [Cloud Native](https://trescout.com/de/dictionary/cloud-native/)
- [API](https://trescout.com/de/dictionary/api/)
- [Proxy](https://trescout.com/de/dictionary/proxy/)

## Verwandte Werkzeuge

- [Meshery](https://trescout.com/de/discover/meshery/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/service-mesh/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/service-mesh/
