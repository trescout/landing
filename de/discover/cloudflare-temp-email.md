# Kostenlose temporäre E-Mail auf Cloudflare

Cloudflare Temp Email ist eine Open-Source-Plattform, mit der Sie einen völlig kostenlosen, serverlosen Wegwerf-E-Mail-Dienst (Disposable Email) unter Ihrer eigenen Domain einrichten können, der die Infrastruktur von Cloudflare Workers, Pages und D1/KV-Datenbanken nutzt. Er schützt Ihre Privatsphäre durch Posteingangsverwaltung, Speicherung von Anhängen, Telegram-Bot-Integration und automatische Bereinigungsmechanismen.

- ★ 11.982
- TypeScript
- GitHub Trending · 2026-07-23

## Aktualisierungen

- **19. Oktober 2026:** Sterne 11,734 → 11,982, neueste Version v1.13.0 (18. Oktober 2026).
- **13. September 2026:** Sterne 11,391 → 11,734, neueste Version v1.12.0 (13. September 2026).
- **23. August 2026:** Sterne 11,332 → 11,391, neueste Version v1.11.1 (22. August 2026).
- **19. August 2026:** Sterne 11,156 → 11,332, neueste Version v1.11.0 (19. August 2026).

## Was es bringt

- Keine Server- und Betriebskosten: Läuft auf dem großzügigen kostenlosen Tarif von Cloudflare (100.000 Workers-Anfragen pro Tag, kostenloses Email Routing und Pages-Hosting), ohne dass ein externer Server gemietet werden muss.
- Eigene Domain und nicht blockierbare Adressen: Im Gegensatz zu allgemeinen Wegwerf-E-Mail-Diensten generiert dieser Service Einwegadressen mit Ihrer eigenen Domain, die nicht auf den Blacklists von Websites landen.
- Schnelle E-Mail-Analyse mit Rust und WASM: Verarbeitet komplexe eingehende E-Mails mit MIME-, Multipart- und HTML-Inhalten dank eines in Rust kompilierten WebAssembly-Moduls in Millisekunden.
- Telegram-Bot und Push-Benachrichtigungen: Erhalten Sie bei Eingang einer neuen E-Mail direkt über Telegram eine Benachrichtigung, lesen Sie den Nachrichteninhalt oder erstellen Sie per Bot-Befehl sofort eine neue Adresse.
- Automatische Reinigung und sicherer Zugriff: Bereinigt automatisch alte Nachrichten und Anhänge nach einer bestimmten Zeitspanne; Verhindert unbefugten Zugriff mit Administratorkennwort.

## Erste Schritte und Installationsoptionen

Um das Projekt bereitzustellen, benötigen Sie lediglich ein Cloudflare-Konto und eine Domain, die über Cloudflare DNS verwaltet wird. Sie können das Projekt entweder über die grafische Benutzeroberfläche von Cloudflare Pages mit einem Klick mit Ihrem GitHub-Repository verbinden oder die D1-Datenbank und Worker-Funktionen direkt von Ihrer lokalen Umgebung aus über das Wrangler CLI veröffentlichen.

- [Resmî kurulum rehberi →](https://temp-mail-docs.awsl.uk)
- [Canlı demo arayüzü →](https://mail.awsl.uk)

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das Open-Source-Projekt dreamhunter2333/cloudflare_temp_email, das auf Cloudflare läuft, mit meiner eigenen Domain einrichten. Ich habe ein Cloudflare-Konto und eine Domain, die mit Cloudflare DNS verbunden ist. Können Sie mir Schritt für Schritt erklären, wie ich das E-Mail-Routing, die D1-Datenbank und die Cloudflare Pages-Schnittstelle über das Cloudflare-Dashboard von Grund auf neu einrichte? Welche Konfigurationsschritte muss ich außerdem befolgen, um eingehende E-Mails an meinen Telegram-Bot weiterzuleiten?

Repository: https://github.com/dreamhunter2333/cloudflare_temp_email. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Häufig gestellte Fragen

- Ist der kostenlose Plan von Cloudflare für den persönlichen Gebrauch ausreichend? Ja. Der kostenlose Tarif von Cloudflare bietet täglich 100.000 Worker-Anfragen, kostenloses E-Mail-Routing und ein Kontingent für die D1-Datenbank. Bei persönlicher Nutzung und in kleinen Teams ist es nahezu unmöglich, diese Grenzen zu überschreiten; das System arbeitet komplett ohne Kosten.
- Ist für die Nutzung des Dienstes eine eigene Domain (Custom Domain) erforderlich? Ja. Um E-Mails empfangen zu können, müssen Sie über eine Domain (oder Subdomain, z. B. mail.ihredomain.de) verfügen, die über Cloudflare DNS verwaltet wird. Auf diese Weise können Sie problemlos Websites umgehen, die allgemeine temporäre E-Mail-Dienste blockieren.
- Werden eingehende E-Mails dauerhaft gespeichert? Nein, dies ist ein temporärer E-Mail-Dienst. Als Systemadministrator können Sie über das Panel die Speicherdauer der E-Mails festlegen (z. B. 1 Stunde, 24 Stunden oder 7 Tage); abgelaufene Datensätze werden automatisch aus dem D1- und R2-Speicher gelöscht.
- Kann über den Dienst eine E-Mail-Antwort nach außen gesendet werden? Ja. Obwohl Cloudflare Email Routing nur den E-Mail-Empfang unterstützt, ermöglicht das Projekt durch die Anbindung einer API von Resend, Brevo oder eines eigenen SMTP-Servers auch das Senden und Beantworten von E-Mails über das Web-Panel.

## Verwandte Begriffe aus dem Glossar

- [CLI](https://trescout.com/de/dictionary/cli/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Open Source](https://trescout.com/de/dictionary/open-source/)
- [API](https://trescout.com/de/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Für Entwickler, Testteams und datenschutzorientierte Benutzer, die einen kostenlosen, sicheren und uneingeschränkten temporären E-Mail-Dienst unter ihrer eigenen Domain hosten möchten.
- **Lizenz:** MIT (Freie Open-Source-Lizenz)
- **Infrastruktur:** Cloudflare Workers, Pages, D1 (SQLite) und Email Routing
- **Sprachen und Tools:** TypeScript, Rust (WASM), Vue 3, Wrangler

## Links

- [GitHub-Repository →](https://github.com/dreamhunter2333/cloudflare_temp_email)
- [Auf Türkisch lesen →](https://trescout.com/discover/cloudflare-temp-email/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-23 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cloudflare-temp-email/
