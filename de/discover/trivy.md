# Sicherheits-Scanner für Container und Cloud

Trivy ist ein umfassender, extrem schneller Sicherheits-Scanner zur Erkennung von Schwachstellen (CVEs), Fehlkonfigurationen und geleakten Secrets in Containern, Kubernetes-Clustern und Repositories. Mit nativer Software-Bill-of-Materials-Unterstützung (SBOM) automatisiert er DevSecOps-Prozesse.

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Was es bringt
- Multi-Ziel-Überprüfung: Überprüfen Sie Container-Images (Docker, OCI), lokale Dateisysteme, Git-Repositories und Kubernetes-Cluster mit einem einzigen Tool.
- Kein administrativer Mehraufwand: Benötigt weder externe Datenbankserver noch Hintergrund-Daemons; arbeitet als leichtgewichtige Standalone-Binärdatei.
- Erkennung von Secrets und sensiblen Daten: Identifiziert versehentlich comittete API-Schlüssel, Passwörter und private Zertifikate im Quellcode oder in Image-Layers.
- Infrastructure-as-Code (IaC) Audits: Überprüft Terraform-, Dockerfile- und Kubernetes-YAML-Dateien auf Sicherheitskonfigurationen vor dem Produktivgang.
- SBOM und Lizenz-Compliance: Erzeugt Software-Stücklisten nach CycloneDX- und SPDX-Standards zur Einhaltung gesetzlicher Supply-Chain-Vorgaben.

## Installation

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Grundlegende Befehle

**Container-Image scannen**

```
trivy image image-name:tag
```

**Dateisystem auf Schwachstellen und Secrets prüfen**

```
trivy fs --scanners vuln,secret,misconfig .
```

**SBOM im CycloneDX-Format erzeugen**

```
trivy image --format cyclonedx --output sbom.json image-name:tag
```

## Technische Architektur und Funktionsweise

Entwickelt von Aqua Security und der Open-Source-Community, bietet Trivy modernste Sicherheitsmechanismen für DevSecOps-Pipelines:
- Lokale Trivy DB: Lädt automatisch eine kompakte Schwachstellendatenbank herunter (NVD, GitHub Advisory, Red Hat, Debian), um schnelle Offline-Scans zu ermöglichen.
- Statische Layer-Analyse: Zerlegt OCI-Images direkt auf Dateiebene, ohne Container auszuführen oder Docker-Daemon-Rechte zu erfordern.
- IaC-Engine auf Rego-Basis: Prüft Infrastrukturvorlagen anhand von Open-Policy-Agent-Regeln (OPA), um unsichere Ports oder Root-Privilegien aufzudecken.
- Lückenlose Abhängigkeitsanalyse: Durchleuchtet Lockdateien (package-lock.json, poetry.lock, Cargo.lock) nach transitiven Sicherheitslücken.

## DevSecOps und CI/CD-Pipeline-Integration

Trivy fungiert als automatisiertes Quality Gate, um zu verhindern, dass unsicherer Code in Produktionsumgebungen gelangt:

**Build bei kritischen oder hohen Schwachstellen stoppen**

```
trivy image --exit-code 1 --severity CRITICAL,HIGH image-name:tag
```
- Frühes Feedback (Shift-Left): Entwickler erkennen Schwachstellen in Open-Source-Bibliotheken lokal vor dem Push.
- Automatisierte SARIF-Berichte: Übertragen Sie Ergebnisse direkt in GitHub Code Scanning oder GitLab Security für zentrales Schwachstellenmanagement.
- Cluster-Überwachung (Trivy Operator): Überwacht laufende Kubernetes-Workloads kontinuierlich auf neu entdeckte Zero-Day-Lücken.

## Wenn Sie nicht programmieren
🤖 Wenn Sie nicht programmieren
Ich möchte einen GitHub-Actions-Workflow einrichten, der mein Docker-Image und meinen Quellcode bei jedem Push und PR mit Trivy überprüft. Kannst du eine vollständige .github/workflows/trivy.yml erstellen, die den Build nur bei CRITICAL und HIGH Schwachstellen abbricht (exit-code 1), die Ergebnisse als SARIF an GitHub Security sendet und eine CycloneDX-SBOM-Datei erzeugt?

- **Für wen:** DevOps-Ingenieure, Sicherheitsteams und Entwickler, die Schwachstellen-Audits und SBOM-Erstellung automatisieren wollen.
- **Lizenz:** Apache-2.0 (Freie Open-Source-Lizenz)
- **Entwickler:** Aqua Security und Open-Source-Community
- **Ausgabeformate:** Tabelle, JSON, SARIF, CycloneDX, SPDX, Template

## Häufig gestellte Fragen
- Kann Trivy Images ohne Docker-Daemon scannen? Ja. Trivy kann Images direkt von Registries (Docker Hub, GitHub Container Registry) herunterladen oder lokale Tar-Dateien analysieren, ohne dass Docker läuft.
- Funktioniert Trivy in isolierten Netzen (Air-Gapped)? Ja. Die Trivy-Datenbank kann vorab heruntergeladen und in geschlossene Umgebungen übertragen werden.
- Was ist eine SBOM und warum Trivy dafür nutzen? Eine Software-Stückliste (SBOM) dokumentiert alle enthaltenen Open-Source-Pakete und Lizenzen. Trivy generiert standardisierte CycloneDX- und SPDX-Dateien.
- Wie schnell arbeitet Trivy? Da Abfragen gegen die lokale, vorindizierte Datenbank ohne zwischenzeitliche Netzwerkaufrufe stattfinden, dauert ein Scan meist nur wenige Sekunden.

## Links
- [GitHub →](https://github.com/aquasecurity/trivy)
- [Read in Turkish →](https://trescout.com/discover/trivy/)

## Verwandte Begriffe aus dem Glossar
Container CI-CD Vulnerability Scanning Cloud Native

---
Source: TreScout Discover · https://trescout.com/de/discover/trivy/
