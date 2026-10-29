# TCP-Tunneling für Netzwerkverkehr

OpenFlux, entwickelt in der Sprache Go, ist ein TCP-Tunneling-Tool, das für die Erforschung des Netzwerk-Stacks konzipiert wurde. Dank der Unterstützung für steckbare Transportprotokolle (pluggable transports) bietet es flexible Möglichkeiten zur Analyse und Verwaltung des Netzwerkverkehrs.

- ★ 2.299
- Go
- GitHub Trending · 2026-09-12

## Aktualisierungen

- **29. Oktober 2026:** Sterne 2,184 → 2,299, neueste Version v0.17.1 (28. Oktober 2026).
- **16. Oktober 2026:** Sterne 2,120 → 2,184, neueste Version v0.13.0 (16. Oktober 2026).
- **14. Oktober 2026:** Sterne 2,107 → 2,120, neueste Version v0.7.3 (14. Oktober 2026).
- **13. Oktober 2026:** Sterne 2,092 → 2,107, neueste Version v0.7.2 (13. Oktober 2026).

## Was es bringt

- Flexibles Netzwerkmanagement mit steckbaren Transportprotokollen
- Lokale Netzwerkverkehrssteuerung mit SOCKS5-Proxy-Unterstützung
- Datenübertragung über Yandex Docs und WebRTC

## Installation

**Kompilierung von Desktop-Client und Exit-Node**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Kompilierung des Android-Clients**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```

## Ausführung

**Starten des Desktop-Clients**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte mit dem OpenFlux-Tool einen TCP-Tunnel erstellen. Erkläre Schritt für Schritt die notwendigen Kompilierungsschritte, um den Client auf meinem Desktop-Computer auszuführen, und wie ich anschließend die SOCKS5-Proxy-Einstellungen im Browser konfiguriere. Erläutere zudem technisch, warum es beim Einrichten eines Exit-Nodes auf einem Linux-Server notwendig ist, RST-Pakete mit iptables zu blockieren, und welche Auswirkungen dieser Vorgang auf die Netzwerksicherheit hat.

Repository: https://github.com/p1neappleXpress/OpenFlux. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Pluggable Transports](https://trescout.com/de/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/de/dictionary/network-stack/)
- [Proxy](https://trescout.com/de/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Dies ist für Benutzer gedacht, die Netzwerk-Stack-Forschung betreiben und TCP-Verkehr über verschiedene Transportprotokolle tunneln möchten.
- **Lizenz:** GPL-3.0

## Links

- [GitHub-Repository →](https://github.com/p1neappleXpress/OpenFlux)
- [Auf Türkisch lesen →](https://trescout.com/discover/openflux/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openflux/
