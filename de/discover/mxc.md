# Richtlinienbasierte mehrschichtige Systemisolierung mit Rust

MXC wurde von Microsoft entwickelt und ist eine richtlinienbasierte, mehrschichtige Isolations- und Eindämmungslösung, die in der Rust-Sprache geschrieben ist. Es wurde entwickelt, um Systemressourcen sicher zu begrenzen und die Anwendungssicherheit zu erhöhen.

- ★ 641
- Rust
- GitHub Trending · 2026-06-07

## Was es bringt
- Führt nicht vertrauenswürdigen Code sicher in isolierten Umgebungen aus.
- Steuert den Datei-, Netzwerk- und Schnittstellenzugriff mit JSON-basierten Richtlinien.
- Es bietet mehrere Isolations-Backends für Windows, Linux und macOS.

## Installation
**Kompilieren unter Linux**

```
./build.sh
```

**Bauen Sie auf macOS auf**

```
./build-mac.sh
```


## Ausführung
**Läuft mit nativer Binärdatei**

```
wxc-exec.exe config.json
```


## Wenn Sie nicht programmieren
Ich möchte mit dem von Microsoft entwickelten MXC-Tool einen nicht vertrauenswürdigen Codeausschnitt in einem isolierten Container ausführen. Gemäß der Dokumentation im GitHub-Repository des Projekts muss ich eine JSON-basierte Konfigurationsdatei vorbereiten und die für meine Plattform geeignete Binärdatei verwenden. Können Sie für mich eine Beispiel-JSON-Konfigurationsdatei erstellen, die es mir ermöglicht, ein Python-Skript mit eingeschränktem Dateisystem- und Netzwerkzugriff auszuführen, und mir Schritt für Schritt erklären, wie diese Konfiguration mit wxc-exec.exe ausgeführt wird?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/mxc/
