# Was ist Load Balancer?

*Entwicklung · Zuletzt aktualisiert: 20. November 2026*

Es handelt sich um einen Verkehrsrouter, der den eingehenden Netzwerkverkehr auf mehrere Server verteilt, um Systemabstürze zu verhindern und die Leistung zu steigern.

## Definition

Ein Load Balancer verteilt Benutzeranfragen, die an eine Website oder einen digitalen Dienst gerichtet sind, gleichmäßig auf einen Pool von Backend-Servern. Er verhindert, dass ein einzelner Server unter Überlastung zusammenbricht, und leitet den Datenverkehr bei Hardwareausfällen sofort auf funktionierende Server um. Auf diese Weise stellen Sie sicher, dass Ihr System unterbrechungsfrei, schnell und zuverlässig arbeitet.

***Analogie:** Es ähnelt einem Warteschlangensystem in einer stark frequentierten Bankfiliale, das Kunden nacheinander an freie Schalter leitet, um Staus vor einem einzelnen Schalter zu vermeiden.*

## So funktioniert es

Die Netzwerkanfrage des Benutzers geht nicht direkt an den Server, sondern trifft zuerst auf den Load Balancer. Das System leitet die Anfrage unter Verwendung von Algorithmen wie Round Robin, der geringsten Anzahl an Verbindungen oder der Server-Antwortzeit an den am besten geeigneten Server weiter. Gleichzeitig überwacht es den Gesundheitszustand der Server und entfernt ausgefallene Server automatisch aus dem Datenverkehrsfluss.

## Wo es eingesetzt wird

Es wird auf E-Commerce-Plattformen, die Millionen von Benutzern bedienen, in Microservice-basierten Cloud-Architekturen und in Finanzsystemen eingesetzt, die keine Ausfallzeiten tolerieren.

## Häufig verwechselt mit

Es kann mit einem API Gateway verwechselt werden. Während sich ein API Gateway auf Funktionen wie Authentifizierung, Anfragetransformation und API-Management konzentriert, zielt ein Load Balancer primär auf die effiziente Verteilung des Datenverkehrs zwischen Servern ab.

## Fragen und Antworten

**Ist die Verwendung eines Load Balancers zwingend erforderlich?**

Für einfache Websites mit geringem Datenverkehr ist er nicht zwingend erforderlich, aber sobald Ihre Anwendung wächst und ein einzelner Server nicht mehr ausreicht, wird er unverzichtbar, um Ausfälle zu vermeiden.

**Was ist der Unterschied zwischen einem softwarebasierten und einem hardwarebasierten Load Balancer?**

Hardwaremodelle sind spezielle physische Geräte, die in Rechenzentren installiert werden. Softwaremodelle wie NGINX oder HAProxy hingegen sind flexible Programme, die in Cloud-Umgebungen und auf Standardservern laufen.

## Verwandte Begriffe

- [API Gateway](https://trescout.com/de/dictionary/api-gateway/)
- [Reverse Proxy](https://trescout.com/de/dictionary/reverse-proxy/)
- [Microservices](https://trescout.com/de/dictionary/microservices/)
- [Cloud Computing](https://trescout.com/de/dictionary/cloud-computing/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/load-balancer/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/load-balancer/
