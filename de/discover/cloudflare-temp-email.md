# Kostenlose temporäre E-Mail auf Cloudflare

Cloudflare Temp Email ist eine Open-Source-Plattform zur Erstellung eines völlig kostenlosen, serverlosen Wegwerf-E-Mail-Dienstes (Disposable Email) mit eigener Domain über Cloudflare Workers, Pages und D1/KV. Es schützt die Privatsphäre durch Posteingangsverwaltung, Anhangunterstützung, Telegram-Bot-Integration und automatische Datenbereinigung.

- ★ 11.734
- TypeScript
- GitHub Trending · 2026-07-23

## Aktualisierungen
- 13. September 2026: Sterne 11.391 → 11.734, neueste Version v1.12.0 (13. September 2026).
- 23. August 2026: Sterne 11.332 → 11.391, neueste Version v1.11.1 (22. August 2026).
- 19. August 2026: Sterne 11.156 → 11.332, neueste Version v1.11.0 (19. August 2026).
- 2. August 2026: Sterne 10.884 → 11.156, neueste Version v1.10.0 (31. Juli 2026).

## Was es bringt
- Null Server- und Betriebskosten: Läuft auf dem großzügigen kostenlosen Kontingent von Cloudflare (100.000 Workers-Anfragen/Tag, kostenloses Email Routing und Pages) ohne dedizierte Servermiete.
- Eigene Domain und unblockierbare Adressen: Erzeugt Wegwerfadressen unter Ihrer eigenen Domain und umgeht Sperrlisten gängiger öffentlicher Temp-Mail-Anbieter.
- Schnelles E-Mail-Parsing mit Rust und WASM: Verarbeitet komplexe MIME-, Multipart- und HTML-E-Mails in Millisekunden dank eines in Rust kompilierten WebAssembly-Moduls.
- Telegram-Bot und Sofortbenachrichtigungen: Erhalten Sie Benachrichtigungen über eingehende E-Mails direkt in Telegram, lesen Sie Nachrichten oder generieren Sie Adressen per Befehl.
- Automatische Bereinigung und sichere Verwaltung: Löscht abgelaufene E-Mails und Anhänge nach einer definierten Frist automatisch und schützt den Administratorzugriff per Passwort.

## Erste Schritte und Bereitstellungsoptionen

Für die Bereitstellung sind lediglich ein Cloudflare-Konto und eine über Cloudflare DNS verwaltete Domain erforderlich. Sie können das GitHub-Repository mit einem Klick über Cloudflare Pages anbinden oder die D1-Datenbank und Worker lokal über die Wrangler CLI bereitstellen.
- [Offizielle Installationsanleitung →](https://temp-mail-docs.awsl.uk)
- [Live-Demo-Oberfläche →](https://mail.awsl.uk)

## Technische Architektur und Funktionsweise

Cloudflare Temp Email eliminiert den Wartungsaufwand herkömmlicher Mailserver (Postfix, Dovecot) durch ein modernes serverloses Design:
- Cloudflare Email Routing: Eingehender MX-Datenverkehr wird von der Cloudflare-Infrastruktur entgegengenommen und über eine Catch-all-Regel an den empfangenden Worker weitergeleitet.
- Edge Worker & Rust WASM-Parser: Der E-Mail-Datenstrom wird an das optimierte Rust-WASM-Modul übergeben, um Header, Textinhalt, HTML und Anhänge verzögerungsfrei zu trennen.
- Speicherung mit Cloudflare D1 & R2: E-Mail-Texte und Metadaten werden in der Edge-SQLite-Datenbank Cloudflare D1 gespeichert; Anhänge können optional nach Cloudflare R2 ausgelagert werden.
- Moderne Single-Page-App (SPA): Die Benutzeroberfläche wird über das globale Edge-CDN von Cloudflare Pages mit minimaler Latenz an Besucher ausgeliefert.
- REST-API & externe Schnittstellen: Programmierbare Endpunkte ermöglichen automatisierten Tests oder CI/CD-Pipelines die Adressgenerierung und das Auslesen von Verifizierungscodes.

## Installation und Bereitstellungsbeispiel

```bash
# 1. Repository klonen und Abhaengigkeiten installieren
git clone https://github.com/dreamhunter2333/cloudflare_temp_email.git
cd cloudflare_temp_email
pnpm install

# 2. Cloudflare D1-Datenbank anlegen
npx wrangler d1 create temp_email_db

# 3. Datenbankschema ausfuehren und deployen
npx wrangler d1 execute temp_email_db --file=./db/schema.sql
pnpm run deploy
```

## Wenn Sie nicht programmieren
🤖 Fügen Sie dies in Ihren KI-Agenten ein (Claude Code · Codex · Antigravity) 
Ich möchte das Open-Source-Projekt dreamhunter2333/cloudflare_temp_email für temporäre E-Mails mit meiner eigenen Domain auf Cloudflare einrichten. Ich besitze ein Cloudflare-Konto und eine Domain auf Cloudflare DNS. Kannst du mir Schritt für Schritt erklären, wie ich die Email Routing Catch-all-Regeln konfiguriere, die D1-Datenbank erstelle und das Frontend auf Cloudflare Pages veröffentliche? Welche Umgebungsvariablen muss ich hinterlegen, um Benachrichtigungen über einen Telegram-Bot zu erhalten?

- **Für wen:** Entwickler, QS-Ingenieure und datenschutzbewusste Anwender, die einen kostenlosen, unblockierbaren Wegwerf-E-Mail-Dienst unter eigener Domain betreiben möchten. 
- **Lizenz:** MIT (Freie Open-Source-Lizenz) 
- **Infrastruktur:** Cloudflare Workers, Pages, D1 (SQLite) und Email Routing 
- **Sprachen & Tools:** TypeScript, Rust (WASM), Vue 3, Wrangler 

## Häufig gestellte Fragen
- Reicht der kostenlose Cloudflare-Tarif für den persönlichen Gebrauch? Ja. Der kostenlose Tarif umfasst täglich 100.000 Worker-Anfragen sowie freie Kontingente für Email Routing und D1. Für Einzelpersonen und kleine Teams ist ein Überschreiten dieser Grenzen so gut wie ausgeschlossen; der Betrieb bleibt kostenfrei.
- Ist eine eigene Domain zwingend erforderlich? Ja. Um E-Mails empfangen zu können, benötigen Sie eine auf Cloudflare DNS verwaltete Domain oder Subdomain. Dadurch wird zudem verhindert, dass Ihre Adressen von Webdiensten geblockt werden.
- Werden eingehende E-Mails dauerhaft gespeichert? Nein, dies ist ein temporärer Dienst. Administratoren können Aufbewahrungsfristen (z. B. 1 Stunde, 24 Stunden oder 7 Tage) definieren; abgelaufene Nachrichten werden automatisch aus dem Speicher entfernt.
- Unterstützt der Dienst das Versenden von Antworten? Ja. Obwohl Cloudflare Email Routing nur den Empfang übernimmt, unterstützt das Projekt über Schnittstellen zu Resend, Brevo oder externen SMTP-Servern auch das Beantworten und Versenden von E-Mails.

## Links
- [GitHub-Repository →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Auf Türkisch lesen →](https://trescout.com/discover/cloudflare-temp-email/)

TreScout hat dieses Tool nicht selbst entwickelt · wir haben es in den GitHub-Trends entdeckt und auf Deutsch zusammengefasst. Diese Seite beschreibt den Stand des Repositorys vom 2026-07-23.

## Verwandte Begriffe aus dem Glossar
Self-Hosted Cloud Computing Digital Privacy Open Source API Rust

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cloudflare-temp-email/
