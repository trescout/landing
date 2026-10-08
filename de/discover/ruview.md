# Drahtlose Erfassung mit WiFi-Signalen

RuView ist eine Sensing-Plattform, die WiFi Channel State Information (CSI) verwendet, um Veränderungen in der Umgebung zu untersuchen. Sie kann mit ESP32- oder Forschungs-NIC-Hardware betrieben werden; für eine Bewertung ohne Hardware stehen simulierte Daten zur Verfügung.

- ★ 96.773
- GitHub Trending · 2026-05-30

## Aktualisierungen

- **7. Oktober 2026:** Sterne 96,651 → 96,773, neueste Version v3067 (6. Oktober 2026).
- **6. Oktober 2026:** Sterne 96,464 → 96,651, neueste Version v3060 (5. Oktober 2026).
- **5. Oktober 2026:** Sterne 95,926 → 96,464, neueste Version v3037 (4. Oktober 2026).
- **2. Oktober 2026:** Sterne 95,751 → 95,926, neueste Version v2975 (2. Oktober 2026).

## Installation

**Docker-Image abrufen**

```
docker pull ruvnet/wifi-densepose:latest
```

**Quellcode klonen**

```
git clone https://github.com/ruvnet/RuView.git
```

## Ausführung

**Demo-Server ohne Hardware**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Deterministische Prüfung**

```
./verify
```

## Was macht dieses Werkzeug?

RuView ist eine MIT-lizenzierte Plattform für Sensing-Experimente mit WiFi Channel State Information. Sie kann mit Docker oder aus dem Quellcode installiert und ohne Hardware mit simulierten Daten bewertet werden. Die Fähigkeiten hängen vom Hardwaremodus ab: RSSI-only-Sensing auf einem Laptop dient der groben Erkennung von Anwesenheit und Bewegung, während erweitertes Sensing vollständige CSI-Hardware erfordert.

## Für wen ist es?

Forscher und Entwickler, die Anwesenheit, Bewegung oder Umgebungsveränderungen anhand von WiFi-Signalen untersuchen möchten.

## Was Sie nicht erwarten sollten

Medizinische Überwachung oder Erwartungen an Pose-Schätzung mit einem gewöhnlichen Laptop im RSSI-only-Modus.

## Höhepunkte

- Bietet CSI-basierte Sensing-Wege mit ESP32- und Forschungs-NIC-Hardware.
- Kann ohne Hardware mit simulierten Daten bewertet werden.
- Dokumentiert eine deterministische Referenzsignalprüfung mit `./verify`.
- Trennt die Fähigkeiten des RSSI-only-Laptopmodus von denen vollständiger CSI-Hardware.

## Ablauf für die erste Nutzung

1. Bereiten Sie die Umgebung mit dem Docker- oder Quellcode-Weg der offiziellen Anleitungen vor.
2. Wenn keine Hardware vorhanden ist, beginnen Sie mit der Bewertung anhand simulierter Daten.
3. Führen Sie die in der Bauanleitung beschriebene deterministische Referenzsignalprüfung mit `./verify` aus.
4. Wählen Sie den RSSI-only- oder vollständigen CSI-Weg passend zu Ihrer Hardware.

## Sicherer Start

Der RSSI-only-Modus auf einem Laptop ist für die grobe Erkennung von Anwesenheit und Bewegung gedacht und unterstützt keine Pose. Pose und einige Benchmark-Funktionen sind als experimentell, als erste Version oder mit Einschränkungen dokumentiert; bewerten Sie Ergebnisse passend zum verwendeten Hardwaremodus.

## Erster Prompt

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Wie kann ich ein einfaches Szenario zur Bewegungserkennung mit simulierten WiFi-CSI-Daten bewerten?

## Verwandte Begriffe aus dem Glossar

- [WiFi](https://trescout.com/de/dictionary/wifi/)
- [Benchmark](https://trescout.com/de/dictionary/benchmark/)

## Links

- [GitHub-Repository →](https://github.com/ruvnet/RuView)
- [Offizielles RuView-GitHub-Repository →](https://github.com/ruvnet/RuView)
- [RuView-Benutzerhandbuch →](https://github.com/ruvnet/RuView/blob/main/docs/user-guide.md)
- [RuView-Bauanleitung →](https://github.com/ruvnet/RuView/blob/main/docs/build-guide.md)
- [Auf Türkisch lesen →](https://trescout.com/discover/ruview/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-05-30 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ruview/
