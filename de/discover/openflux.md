# TCP-Tunneling für Netzwerkverkehr

OpenFlux, entwickelt in der Sprache Go, ist ein TCP-Tunneling-Tool, das für die Erforschung des Netzwerk-Stacks konzipiert wurde. Dank der Unterstützung für steckbare Transportprotokolle (pluggable transports) bietet es flexible Möglichkeiten zur Analyse und Verwaltung des Netzwerkverkehrs.

- ★ 1.241
- Go
- GitHub Trending · 2026-09-12

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
Ich möchte mit dem OpenFlux-Tool einen TCP-Tunnel erstellen. Erkläre Schritt für Schritt die notwendigen Kompilierungsschritte, um den Client auf meinem Desktop-Computer auszuführen, und wie ich anschließend die SOCKS5-Proxy-Einstellungen im Browser konfiguriere. Erläutere zudem technisch, warum es beim Einrichten eines Exit-Nodes auf einem Linux-Server notwendig ist, RST-Pakete mit iptables zu blockieren, und welche Auswirkungen dieser Vorgang auf die Netzwerksicherheit hat.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openflux/
