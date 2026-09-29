# Kostenlose temporäre E-Mail auf Cloudflare

Cloudflare Temp Email ist eine Open-Source-Plattform, mit der Sie einen völlig kostenlosen, serverlosen Wegwerf-E-Mail-Dienst (Disposable Email) unter Ihrer eigenen Domain einrichten können, der die Infrastruktur von Cloudflare Workers, Pages und D1/KV-Datenbanken nutzt. Er schützt Ihre Privatsphäre durch Posteingangsverwaltung, Speicherung von Anhängen, Telegram-Bot-Integration und automatische Bereinigungsmechanismen.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Was es bringt
- Keine Server- und Betriebskosten: Läuft auf dem großzügigen kostenlosen Tarif von Cloudflare (100.000 Workers-Anfragen pro Tag, kostenloses Email Routing und Pages-Hosting), ohne dass ein externer Server gemietet werden muss.
- Eigene Domain und nicht blockierbare Adressen: Im Gegensatz zu allgemeinen Wegwerf-E-Mail-Diensten generiert dieser Service Einwegadressen mit Ihrer eigenen Domain, die nicht auf den Blacklists von Websites landen.
- Schnelle E-Mail-Analyse mit Rust und WASM: Verarbeitet komplexe eingehende E-Mails mit MIME-, Multipart- und HTML-Inhalten dank eines in Rust kompilierten WebAssembly-Moduls in Millisekunden.
- Telegram-Bot und Push-Benachrichtigungen: Erhalten Sie bei Eingang einer neuen E-Mail direkt über Telegram eine Benachrichtigung, lesen Sie den Nachrichteninhalt oder erstellen Sie per Bot-Befehl sofort eine neue Adresse.
- Automatische Reinigung und sicherer Zugriff: Bereinigt automatisch alte Nachrichten und Anhänge nach einer bestimmten Zeitspanne; Verhindert unbefugten Zugriff mit Administratorkennwort.

## Erste Schritte und Installationsoptionen
- Offizieller Installationsleitfaden →
- Live-Demo-Oberfläche →

## Technische Architektur und Funktionsweise
- Cloudflare Email Routing-Integration: Der gesamte MX-Datenverkehr für Ihre Domain wird über die Cloudflare-Infrastruktur empfangen und mittels einer Catch-all-Regel direkt an die Catch-all-Worker-Funktion weitergeleitet.
- Edge Worker und Rust WASM-Parser: Der eingehende E-Mail-Datenstrom (Raw Stream) wird an eine optimierte, innerhalb des Workers laufende Rust WASM-Engine übergeben, um Header, Body, HTML und Anhänge schnell zu parsen.
- Cloudflare D1 und R2-Speicher: E-Mail-Texte und Metadaten werden in der Edge-SQLite-Datenbank Cloudflare D1 gespeichert. Dateianhänge werden optional in den Cloudflare R2-Objektspeicher geschrieben.
- Moderne Single-Page-Application (SPA): Die benutzerfreundliche Weboberfläche wird über das globale CDN-Netzwerk von Cloudflare mit null Latenz bereitgestellt.
- REST-API und externe Integrationen: Bietet die Möglichkeit, über REST-API-Endpunkte neue E-Mail-Adressen abzuleiten und Posteingänge für automatisierte Tests oder Drittanbietersoftware abzufragen.

## Installation und Beispielbereitstellung
**Bereitstellungsschritte mit Wrangler CLI**

```
# 1. Depoyu klonlayin ve bagimliliklari kurun
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1 veritabanini olusturun
npx wrangler d1 create temp_email_db

# 3. Veritabani semasini calistirin ve yayinlayin
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```


## Wenn Sie nicht programmieren
Ich möchte das Open-Source-Projekt dreamhunter2333/cloudflare_temp_email, das auf Cloudflare läuft, mit meiner eigenen Domain einrichten. Ich habe ein Cloudflare-Konto und eine Domain, die mit Cloudflare DNS verbunden ist. Können Sie mir Schritt für Schritt erklären, wie ich das E-Mail-Routing, die D1-Datenbank und die Cloudflare Pages-Schnittstelle über das Cloudflare-Dashboard von Grund auf neu einrichte? Welche Konfigurationsschritte muss ich außerdem befolgen, um eingehende E-Mails an meinen Telegram-Bot weiterzuleiten?

## Häufig gestellte Fragen
- Ist der kostenlose Plan von Cloudflare für den persönlichen Gebrauch ausreichend? Ja. Der kostenlose Tarif von Cloudflare bietet täglich 100.000 Worker-Anfragen, kostenloses E-Mail-Routing und ein Kontingent für die D1-Datenbank. Bei persönlicher Nutzung und in kleinen Teams ist es nahezu unmöglich, diese Grenzen zu überschreiten; das System arbeitet komplett ohne Kosten.
- Ist für die Nutzung des Dienstes eine eigene Domain (Custom Domain) erforderlich? Ja. Um E-Mails empfangen zu können, müssen Sie über eine Domain (oder Subdomain, z. B. mail.ihredomain.de) verfügen, die über Cloudflare DNS verwaltet wird. Auf diese Weise können Sie problemlos Websites umgehen, die allgemeine temporäre E-Mail-Dienste blockieren.
- Werden eingehende E-Mails dauerhaft gespeichert? Nein, dies ist ein temporärer E-Mail-Dienst. Als Systemadministrator können Sie über das Panel die Speicherdauer der E-Mails festlegen (z. B. 1 Stunde, 24 Stunden oder 7 Tage); abgelaufene Datensätze werden automatisch aus dem D1- und R2-Speicher gelöscht.
- Kann über den Dienst eine E-Mail-Antwort nach außen gesendet werden? Ja. Obwohl Cloudflare Email Routing nur den E-Mail-Empfang unterstützt, ermöglicht das Projekt durch die Anbindung einer API von Resend, Brevo oder eines eigenen SMTP-Servers auch das Senden und Beantworten von E-Mails über das Web-Panel.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cloudflare-temp-email/
