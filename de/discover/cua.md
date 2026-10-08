# Computersteuerung für Agenten der künstlichen Intelligenz

CUA bietet eine Open-Source-Infrastruktur für computerfähige Agenten der künstlichen Intelligenz. Es vereint Sandbox, Software Development Kit (SDK) und Benchmark-Tools unter einem Dach, um Agenten zu schulen und zu evaluieren, die Desktop-Betriebssysteme steuern können.

- ★ 28.129
- HTML
- GitHub Trending · 2026-06-16

## Aktualisierungen

- **5. Oktober 2026:** Sterne 28,101 → 28,129, neueste Version cua-sdk-v0.4.1 (5. Oktober 2026).
- **5. Oktober 2026:** Sterne 27,988 → 28,101, neueste Version cua-spaces-v0.7.2 (5. Oktober 2026).
- **4. Oktober 2026:** Sterne 27,887 → 27,988, neueste Version cua-sdk-v0.3.1 (4. Oktober 2026).
- **3. Oktober 2026:** Sterne 27,875 → 27,887, neueste Version cua-spacesd-v0.4.1 (3. Oktober 2026).

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

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte einen Computernutzungsagenten entwickeln, der die CUA-Infrastruktur nutzt. Helfen Sie mir, die grundlegende Python-Struktur einzurichten, die es meinem Agenten ermöglicht, im Hintergrund mit Desktop-Anwendungen zu interagieren, Mausklicks auszuführen und Tastatureingaben zu senden. Erstellen Sie mit dem CUA Sandbox SDK eine Beispielcodeskizze, die Befehle ausführt und Screenshots in einer Linux-Umgebung erstellt.

## Verwandte Begriffe aus dem Glossar

- [Benchmark](https://trescout.com/de/dictionary/benchmark/)
- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [SDK](https://trescout.com/de/dictionary/sdk/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für Softwareentwickler und Forscher, die Agenten der künstlichen Intelligenz entwickeln, die autonome Aufgaben am Computer ausführen.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/trycua/cua)
- [Auf Türkisch lesen →](https://trescout.com/discover/cua/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-16 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/cua/
