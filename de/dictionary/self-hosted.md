# Was ist Self-hosted?

*Entwicklung · Zuletzt aktualisiert: 19. September 2026*

Self-hosted (Eigenhosting oder lokales Hosting) ist eine Architektur zum Ausführen und Verwalten von Software, Datenbanken oder digitalen Diensten auf einem physischen Server unter Ihrer vollständigen Kontrolle, auf lokaler Hardware (Homelab) oder auf einem virtuellen privaten Server (VPS), ohne von einem Cloud-Unternehmen eines Drittanbieters (SaaS) abhängig zu sein.

## Etymologie und türkische Entsprechung

Der Begriff, der sich aus den englischen Wörtern self (selbst) und host (to host, host) zusammensetzt, heißt im Türkischen self-hosting, Hosting auf dem eigenen Server oder lokales Hosting.

Beim traditionellen SaaS-Modell (Software as a Service) sind die Nutzer lediglich Mieter; Daten und Infrastruktur sind in den Rechenzentren fremder Unternehmen eingeschlossen. Beim Self-Hosted-Ansatz sind Sie hingegen direkt der Systemadministrator und Eigentümer: Die Datenbank, die Speicherfestplatten, die Netzwerkregeln und die Verschlüsselungsschlüssel liegen vollständig in Ihrem physischen oder logischen Eigentum.

## 1. Von der SaaS-Müdigkeit zur Cloud-Repatriierung (Cloud Repatriation)

Der Übergang jeder Software zu einem monatlich wiederkehrenden Abonnementmodell im letzten Jahrzehnt hat bei Einzelpersonen und Unternehmen zu einer erheblichen Abonnement-Müdigkeit geführt:

- Kostenblockade: SaaS-Tools, für die 10–50 US-Dollar pro Monat und Benutzer gezahlt werden, führen mit dem Wachstum des Teams zu unkontrollierten Kosten von Hunderttausenden US-Dollar. Tatsächlich haben globale Technologieführer wie 37signals (Basecamp), die die Cloud verlassen und zu ihrer eigenen Hardware zurückkehren (Cloud Repatriation), die wirtschaftliche Rationalität des selbst gehosteten Ansatzes bewiesen.
- Datensouveränität und Datenschutz: Selbsthosting ist der stärkste Schutz gegen das Risiko, dass Unternehmen die Nutzungsbedingungen einseitig ändern, Daten als Trainingsdaten für Modelle der künstlichen Intelligenz verwenden oder plötzlich Konten schließen. Die Aufbewahrung sensibler Kundendaten innerhalb Ihrer eigenen Grenzen gemäß KVKK- und DSGVO-Standards gewährleistet auch die Einhaltung gesetzlicher Vorschriften.

## 2. Hardware-Architektur und Homelab-Ökosystem

Die Welt des Self-Hosting hat sich heutzutage von teuren Unternehmens-Server-Racks hin zu Wohnzimmern und Heimlaboren (Homelab) verlagert:

- Hardware mit geringem Stromverbrauch: Intel N100-basierte Mini-PCs, Raspberry Pi 5 oder ältere Laptops; Es kann rund um die Uhr ununterbrochen betrieben werden, bei einem Stromverbrauch von nur wenigen hundert Lira pro Jahr.
- Speicher- und Datensicherheit (ZFS & RAID): RAID-Arrays und das ZFS-Dateisystem, in dem mehrere Festplatten gespiegelt werden, machen einen Datenverlust unmöglich, selbst wenn eine Festplatte physisch gebrannt wird. Betriebssysteme wie TrueNAS und unRAID verwandeln diese Hardware in professionelle Speicherpools.
- Cloud-VPS-Alternative: Für diejenigen, die keine Hardware zu Hause hosten möchten, kombinieren günstige virtuelle Server (VPS), die von Anbietern wie Hetzner oder OVH gemietet werden, die Freiheit des Selbsthostings mit der Zuverlässigkeit der Cloud.

## 3. Moderner Self-Hosted Software-Stack

Die Zeiten, in denen man unter Linux PHP und MySQL manuell kompilieren musste, sind vorbei. Die moderne Architektur basiert auf drei Säulen:

- Containerisierung (Docker & Docker Compose): Jeder Dienst (Nextcloud, Vaultwarden, Jellyfin) läuft in einem isolierten Docker-Container mit eigenen Bibliotheken. Dank der Datei docker-compose.yml können Dutzende Dienste mit einem einzigen Befehl gestartet werden.
- Reverse Proxy: Nginx, Traefik oder Caddy; Es verarbeitet eingehende Webanfragen, leitet Domains an den richtigen Container weiter und erneuert kostenlose SSL/TLS-Zertifikate automatisch über Let's Encrypt.
- Sichere Netzwerktunnel (Zero-Trust & Mesh VPN): Das Öffnen externer Ports am Heimmodem lädt zu Cyberangriffen ein. Mit Tailscale, WireGuard oder Cloudflare Tunnels betreiben moderne selbstgehostete Benutzer ihre Systeme sicher in einem internen Netzwerk (Mesh VPN), das von der Außenwelt abgeschottet und nur für ihre autorisierten Geräte geöffnet ist.

## 4. Beliebte Self-Hosted-Lösungen

- Persönliche Cloud und Foto: Nextcloud statt Google Drive, Immich mit künstlicher Intelligenz-Gesichtserkennung statt Google Fotos.
- Passwortverwaltung: Open Source und leichtes Vaultwarden (Bitwarden-kompatibel) anstelle von 1Password.
- Medien-Streaming: Jellyfin und Plex, wo Sie Ihr eigenes Archiv anstelle von Netflix und Spotify verwalten.
- Lokale künstliche Intelligenz: Ollama und Open WebUI laufen auf Ihrer eigenen Grafikkarte anstelle eines ChatGPT-Abonnements.
- Smart Home: Home Assistant, der komplett lokal arbeitet, statt cloudabhängige Hersteller.

## 5. Verantwortlichkeiten: Die 3-2-1-Backup-Regel

Freiheit bringt Verantwortung mit sich. Im Falle eines Hardwarefehlers steht Ihnen kein Cloud-Unternehmen zur Verfügung, das ein Support-Ticket eröffnen könnte. Aus diesem Grund ist die 3-2-1-Backup-Regel obligatorisch:

- Bewahren Sie mindestens 3 Kopien Ihrer Daten auf.
- Speichern Sie diese Kopien auf zwei verschiedenen physischen Medien (z. B. interner Festplatte und externem USB).
- Hosten Sie mindestens eine der Kopien an einem anderen physischen Ort (verschlüsselter Remote-Server oder externer Speicher), um sich vor Feuer und Diebstahl zu schützen.

## Häufig gestellte Fragen

**Was ist Self-Hosting und was bedeutet es auf Deutsch?**

Es handelt sich um einen Begriff englischen Ursprungs, der im Deutschen 'Eigenhosting' oder 'Selbsthosting' bedeutet. Dabei werden Softwareanwendungen auf der eigenen Hardware oder dem eigenen Server des Benutzers anstatt bei Cloud-Anbietern von Drittanbietern betrieben.

**Muss man fortgeschrittene Programmierkenntnisse haben, um Self-Hosting einzurichten?**

Nein, Sie müssen keinen Code schreiben. Grundlegende Kenntnisse der Linux-Befehlszeile und das Verständnis der Docker-Logik sind ausreichend. Zudem bieten moderne Systeme wie CasaOS und Umbrel die Möglichkeit einer Ein-Klick-Installation nach dem App-Store-Prinzip.

**Ist es sicher, Self-Hosting auf einem Heimserver (Homelab) zu betreiben?**

Bei korrekter Konfiguration ist es sicherer als kommerzielle Clouds, da Ihre Daten nicht mit Unternehmen geteilt werden. Es ist jedoch unerlässlich, VPN-Tunnel wie Tailscale zu verwenden, anstatt Ports direkt am Router zu öffnen, und Sicherheitsupdates regelmäßig durchzuführen.

**Warum ist die 3-2-1-Backup-Regel von entscheidender Bedeutung?**

Bei Self-Hosting-Systemen gibt es keinen Kundenservice, der Daten bei Hardwaredefekten wiederherstellen kann. Die Regel von 3 Kopien, 2 verschiedenen Medien und 1 externen Standort verhindert Datenverlust bei Hardwarebränden oder -ausfällen.

## Verwandte Begriffe

- [Local](https://trescout.com/de/dictionary/local/)
- [Offline](https://trescout.com/de/dictionary/offline/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)

## Verwandte Werkzeuge

- [Immich](https://trescout.com/de/discover/immich/)
- [CasaOS](https://trescout.com/de/discover/casaos/)
- [Chatwoot](https://trescout.com/de/discover/chatwoot/)
- [Open-Generative-AI](https://trescout.com/de/discover/open-generative-ai/)
- [OpenWA](https://trescout.com/de/discover/openwa/)
- [Openship](https://trescout.com/de/discover/openship/)
- [Instatic](https://trescout.com/de/discover/instatic/)
- [TREK](https://trescout.com/de/discover/trek/)

Diese Erklärung wurde für TreScout mit KI in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/self-hosted/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/self-hosted/
