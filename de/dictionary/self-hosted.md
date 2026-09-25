# Self-Hosted Homelabs, Cloud-Repatriierung und eigene Server


**Kategorie:** Dev  

**Zuletzt aktualisiert:** 2026-09-19


Self-Hosted (Selbst-Hosten) bezeichnet den Betrieb, die Konfiguration und die Administration von Softwareanwendungen auf eigener physischer Hardware oder gemieteten Root-Servern anstelle der Nutzung proprietärer SaaS-Dienste.


## Etymologie und Definition
Der Begriff *Self-Hosted* vereint Eigenständigkeit und Serverbetrieb. In der modernen IT verkörpert das Selbst-Hosten die Rückkehr zur digitalen Souveränität: die ungeteilte Kontrolle über eigene Datenströme, Konfigurationen und Datenbanken ohne Abhängigkeit von Großkonzernen.

## 1. Von der SaaS-Müdigkeit zur Cloud-Repatriierung
Was als bequemer Wechsel in die Cloud begann, führte bei vielen Unternehmen zu steigenden Abokosten und unberechenbaren Datenübertragungsgebühren. Vorreiter wie Basecamp prägten den Begriff der **Cloud-Repatriierung**: Berechenbare Dauerlasten werden zurück auf eigene Server geholt, was erhebliche Betriebskosten spart.

## 2. Hardware-Architektur und das Homelab-Ökosystem
Selbst-Hoster greifen auf verschiedene Leistungsklassen zurück :
- **Einplatinencomputer:** Raspberry Pis und moderne Mini-PCs (Intel N100) mit einem Stromverbrauch von unter 15 Watt im Dauerbetrieb.- **Gebrauchte Unternehmens-Server:** Ausgemusterte Rack-Server mit ECC-Speicher und redundanten Festplattenverbünden für anspruchsvolle Virtualisierungen.- **Virtualisierungs-Betriebssysteme:** Proxmox VE oder TrueNAS zur flexiblen Bereitstellung von Linux-Containern (LXC) und virtuellen Maschinen.

## 3. Der moderne Software-Stack für Selbst-Hoster
Dank Container-Technologie ist das Aufsetzen von Diensten so einfach wie nie :
- **Container-Orchestrierung:** Docker und Docker Compose ermöglichen das deklarative Beschreiben ganzer Anwendungslandschaften in einfachen YAML-Dateien.- **Reverse Proxies:** Werkzeuge wie Traefik oder Nginx Proxy Manager verwalten automatisch kostenlose SSL-Zertifikate von Let's Encrypt.- **Sicherer Fernzugriff:** Moderne VPN-Technologien (WireGuard, Tailscale) erlauben den weltweiten Zugriff auf Heimnetz-Dienste, ohne unsichere Router-Ports öffnen zu müssen.

## 4. Populäre Open-Source-Lösungen zum Selbst-Hosten
Für fast jede kommerzielle Cloud-Lösung existiert ein leistungsfähiges Open-Source-Pendant :
- **Dateispeicher und Notizen:** Nextcloud für Office-Aufgaben, Immich als Ersatz für Google Photos und Vaultwarden zur Passwortverwaltung.- **Medienstreaming:** Jellyfin oder Plex zur Wiedergabe persönlicher Film- und Musiksammlungen auf Smart-TVs.- **Gebäudeautomation:** Home Assistant zur lokalen Smart-Home-Steuerung ohne Cloud-Zwang.

## 5. Kritische Pflichten: Die 3-2-1-Backup-Regel
Wer seine eigene Infrastruktur betreibt, trägt die volle Verantwortung für den Ernstfall :
- **Die 3-2-1-Regel:** Mindestens **3** Kopien der Daten auf **2** verschiedenen Speichermedien vorhalten, wovon **1** Kopie an einem externen Ort lagern muss.- **Wiederherstellungstests:** Ein Backup gilt erst dann als vorhanden, wenn die erfolgreiche Wiederherstellung in der Praxis erprobt wurde.

## Im Vergleich
SaaS zu nutzen ist wie das Wohnen zur Miete, wo der Vermieter die Miete anheben oder das Schloss austauschen kann; Self-Hosting ist wie das eigene Haus: Man muss sich selbst um das Dach und die Heizung kümmern, genießt aber absolute Freiheit und Unabhängigkeit.

## Häufig gestellte Fragen

**Was bedeutet der Begriff Self-Hosted?**  
Das Betreiben und Verwalten von Programmen auf eigener Hardware anstelle des Abonnements von kommerziellen Cloud-Diensten.

**Was unterscheidet Local von Self-Hosted?**  
Lokal läuft eine Anwendung direkt auf dem aktuellen PC; Self-Hosted läuft auf einem separaten Server im Dauerbetrieb für das gesamte Netzwerk.

**Wie greift man von unterwegs sicher auf den Heimserver zu?**  
Über moderne Punkt-zu-Punkt-VPNs wie Tailscale oder WireGuard, die verschlüsselte Tunnel aufbauen, ohne Router-Ports zu öffnen.

**Was besagt die 3-2-1-Backup-Regel?**  
Sie fordert 3 Datenkopien auf 2 unterschiedlichen Speichertypen, wobei mindestens 1 Kopie räumlich getrennt gelagert werden muss.

## Verwandte Begriffe
- [Local](/de/dictionary/local/)
- [Offline](/de/dictionary/offline/)
- [Open Source](/de/dictionary/open-source/)
- [Deployment](/de/dictionary/deployment/)

## Verwandte Werkzeuge
- [Immich](/de/discover/immich/)
- [Chatwoot](/de/discover/chatwoot/)
- [Open-Generative-AI](/de/discover/open-generative-ai/)
- [OpenWA](/de/discover/openwa/)
- [Openship](/de/discover/openship/)
- [Instatic](/de/discover/instatic/)
- [TREK](/de/discover/trek/)
- [Celld](/de/discover/celld/)

---
Quelle: TreScout Technik-Glossar · https://trescout.com/de/dictionary/self-hosted/
