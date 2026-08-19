# Computersteuerung für Agenten der künstlichen Intelligenz

CUA bietet eine Open-Source-Infrastruktur für computerfähige Agenten der künstlichen Intelligenz. Es vereint Sandbox, Software Development Kit (SDK) und Benchmark-Tools unter einem Dach, um Agenten zu schulen und zu evaluieren, die Desktop-Betriebssysteme steuern können.

- ★ 21.592
- HTML
- GitHub Trending · 2026-06-16

## Was es bringt
- Steuern Sie Desktop-Apps im Hintergrund
- Isolierte Sandboxen für verschiedene Betriebssysteme
- Benchmarking-Tools zur Messung der Agentenleistung

## Installation
**Treiberinstallation (macOS/Linux)**

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"
```

**Sandbox SDK-Installation**

```
pip install cua
```


## Ausführung
**Start der virtuellen macOS-Maschine**

```
# Install Lume
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"

# Pull & start a macOS VM
lume run macos-sequoia-vanilla:latest
```


## Wenn Sie nicht programmieren
Ich möchte einen Computernutzungsagenten entwickeln, der die CUA-Infrastruktur nutzt. Helfen Sie mir, die grundlegende Python-Struktur einzurichten, die es meinem Agenten ermöglicht, im Hintergrund mit Desktop-Anwendungen zu interagieren, Mausklicks auszuführen und Tastatureingaben zu senden. Erstellen Sie mit dem CUA Sandbox SDK eine Beispielcodeskizze, die Befehle ausführt und Screenshots in einer Linux-Umgebung erstellt.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cua/
