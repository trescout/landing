# Umgehen Sie Zensurblockaden mit DNS-Tunneling

MasterDnsVPN ist eine VPN-Lösung (Virtual Private Network) mit geringem Last-Domain-Name-System-Tunneling (DNS-Tunneling), die zur Umgehung von Zensurbarrieren entwickelt wurde. Das in der Go-Sprache geschriebene Tool bietet eine hohe Paketverluststabilität und Resolver-Lastausgleichsfunktionen bei der Datenübertragung.

- ★ 7.154
- Go
- GitHub Trending · 2026-06-11

## Aktualisierungen

- **27. Oktober 2026:** Sterne 6,870 → 7,154, neueste Version v2026.10.26.100415-5f83ee9 (26. Oktober 2026).
- **2. August 2026:** Sterne 5,411 → 6,870, neueste Version v2026.06.13.234407-7de2476 (13. Juni 2026).

## Was es bringt

- Es ermöglicht die Datenübertragung in zensierten Netzwerken über das DNS-Tunneling-Verfahren.
- Es bietet Multipathing und Lastausgleich für geringen Paketverlust und hohe Geschwindigkeit.
- Optimiert für eine stabile Verbindung auch unter eingeschränkten Netzwerkbedingungen.

## Installation

**Automatisches Server-Setup**

```
bash <(curl -Ls https://raw.githubusercontent.com/masterking32/MasterDnsVPN/main/server_linux_install.sh)
```

**Laufen mit Docker**

```
docker run -d \
  --name masterdnsvpn \
  --restart unless-stopped \
  -e DOMAIN=v.example.com \
  -v $(pwd)/data:/data \
  -p 53:53/tcp \
  -p 53:53/udp \
  ghcr.io/masterking32/masterdnsvpn:latest
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit dem Tool MasterDnsVPN eine sichere Verbindung über DNS-Tunneling in einem zensierten Netzwerk herstellen. Wie kann ich die Serverseite mithilfe des gemeinsam genutzten Autoinstallationsskripts konfigurieren und welche grundlegenden Schritte sollte ich befolgen, um die Verbindung auf der Clientseite sicherzustellen? Bitte erläutern Sie die Netzwerkanforderungen, auf die ich während des Installationsvorgangs achten sollte, und die Methode zur Ausführung über Docker.

Repository: https://github.com/masterking32/MasterDnsVPN. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [DNS Tunneling](https://trescout.com/de/dictionary/dns-tunneling/)
- [Resolver Load Balancing](https://trescout.com/de/dictionary/resolver-load-balancing/)
- [DNS](https://trescout.com/de/dictionary/dns/)
- [VPN](https://trescout.com/de/dictionary/vpn/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Forscher und fortgeschrittene Benutzer, die unter eingeschränkten Netzwerkbedingungen einen hochstabilen Internetzugang bereitstellen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/masterking32/MasterDnsVPN)
- [Auf Türkisch lesen →](https://trescout.com/discover/masterdnsvpn/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-11 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/masterdnsvpn/
