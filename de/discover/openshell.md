# Sichere Umgebung für KI-Agenten

Das von NVIDIA entwickelte OpenShell bietet eine sichere und datenschutzorientierte Laufzeitumgebung (Runtime) für autonome KI-Agenten. Diese in der Programmiersprache Rust geschriebene Infrastruktur zielt darauf ab, den Zugriff von Agenten auf Systemressourcen zu isolieren und einen sicheren Ausführungsbereich zu schaffen.

- ★ 11.092
- Rust
- GitHub Trending · 2026-09-29

## Was es bringt
- Führt KI-Agenten in einer isolierten Sandbox-Umgebung aus
- Schränkt den Datei- und Netzwerkzugriff durch Regeln ein
- Erhöht die Sicherheit durch das Verbergen von Anmeldeinformationen

## Installation
**Tool installieren und Demo-Umgebung erstellen**

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```


## Ausführung
**Funktionen hinzufügen**

```
npx skills add NVIDIA/OpenShell
```


## Wenn Sie nicht programmieren
Um das OpenShell-Tool zu installieren und zu testen, kannst du folgende Befehle verwenden: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh und anschließend den Befehl openshell sandbox create --name demo ausführen, um eine Demoumgebung zu erstellen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openshell/
