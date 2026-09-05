# Drahtlose Erfassung mit WiFi-Signalen

RuView ist eine Sensing-Plattform, die WiFi Channel State Information (CSI) verwendet, um Veränderungen in der Umgebung zu untersuchen. Sie kann mit ESP32- oder Forschungs-NIC-Hardware betrieben werden; für eine Bewertung ohne Hardware stehen simulierte Daten zur Verfügung.

- ★ 92.514
- GitHub Trending · 2026-05-30

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
- Bereiten Sie die Umgebung mit dem Docker- oder Quellcode-Weg der offiziellen Anleitungen vor.
- Wenn keine Hardware vorhanden ist, beginnen Sie mit der Bewertung anhand simulierter Daten.
- Führen Sie die in der Bauanleitung beschriebene deterministische Referenzsignalprüfung mit `./verify` aus.
- Wählen Sie den RSSI-only- oder vollständigen CSI-Weg passend zu Ihrer Hardware.

## Sicherer Start

## Erster Prompt
Wie kann ich ein einfaches Szenario zur Bewegungserkennung mit simulierten WiFi-CSI-Daten bewerten?

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Offizielles RuView-GitHub-Repository →
- RuView-Benutzerhandbuch →
- RuView-Bauanleitung →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/ruview/
