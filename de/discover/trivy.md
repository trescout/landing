# Container- und Cloud-Sicherheitsscanner

Trivy ist ein umfassendes Sicherheitsscan-Tool, das Schwachstellen, Fehlkonfigurationen und Geheimnisse in Containern, Kubernetes-Clustern, Code-Repositorys und Cloud-Infrastrukturen in Sekundenschnelle erkennt. Es automatisiert DevSecOps-Prozesse durchgängig mit Software-Bill-of-Materials-Unterstützung (SBOM).

- ★ 35.511
- Go
- GitHub Trending · 2026-06-04

## Was es bringt

- Mehrschichtiges Zielscannen: Inspiziert Container-Images (Docker, OCI), lokale Dateisysteme, Remote-Git-Repositorys, Festplatten virtueller Maschinen und Live-Kubernetes-Cluster mit einem einzigen Tool.
- Kein zusätzlicher Infrastrukturaufwand: Kein externer Datenbankserver oder ständig laufende Agenten erforderlich; Es liefert Analysen in Sekundenschnelle als einzelne ausführbare Binärdatei.
- Erfassen sensibler Daten und Geheimnisse: Mit seiner heuristischen Engine erkennt es API-Schlüssel, Passwörter und private Zertifikate, die versehentlich in den Quellcode oder Bildebenen eingebettet sind.
- Audit der Infrastruktur als Code (IaC): Erkennt Sicherheitsfehlkonfigurationen in Terraform-, Dockerfile-, Kubernetes YAML- und CloudFormation-Dateien, bevor sie in die Produktion gehen.
- Einhaltung von SBOM und Open-Source-Lizenzen: Entspricht der Sicherheit der Software-Lieferkette den gesetzlichen Vorschriften, indem Software-Stücklisten in den CycloneDX- und SPDX-Standards erstellt werden.

## Installation

**macOS (Homebrew)**

```
brew install trivy
```

**Windows (winget)**

```
winget install AquaSecurity.Trivy
```

## Ausführung

**Container-Image scannen**

```
trivy image imaj-adi:etiket
```

## Technische Architektur und Funktionsweise

- Trivy DB und lokaler Cache: NVD lädt automatisch einen kompakten Datenbank-Cache herunter, der GitHub Advisory Database, Red Hat, Debian, Ubuntu und Alpine-Sicherheitsbulletins enthält. Da Scans über diesen lokalen Cache durchgeführt werden, läuft er auch in Umgebungen mit Netzwerkeinschränkungen blitzschnell.
- Statische Layer-Analyse: Analysiert OCI-Layer direkt, ohne Container-Images auszuführen oder einen Docker-Daemon zu benötigen. Dieser Ansatz beeinträchtigt die Systemsicherheit während des Scanvorgangs nicht.
- IaC-Engine und Rego-Richtlinien: Steuert Infrastrukturvorlagen mit Open Policy Agent (OPA)-konformen Regeln. Unsichere offene Ports oder Dienste, die mit Root-Rechten ausgeführt werden, werden sofort gemeldet.
- SBOM-Standardisierung: Der Paketmanager scannt die Sperrdateien (package-lock.json, poet.lock, Cargo.lock usw.) und erstellt eine vollständige Abhängigkeitskarte Ihrer Anwendung.

## DevSecOps- und CI/CD-Pipeline-Integration

- Feedback zu einem frühen Zeitpunkt: Entwickler erkennen Schwachstellen in Open-Source-Bibliotheken sofort, indem sie Trivy in ihrer lokalen Umgebung ausführen, bevor sie ihren Code in das Remote-Repository übertragen.
- Automatische SARIF-Berichterstellung: Die erzeugten SARIF-Ausgaben werden an GitHub Code Scanning oder GitLab Security-Dashboards übertragen, sodass Teams eine zentrale Schwachstellenverfolgung durchführen können.
- Live-Cluster-Überwachung (Trivy Operator): Es überwacht ständig die in der Kubernetes-Umgebung ausgeführten Arbeitslasten und meldet neu entdeckte Zero-Day-Schwachstellen (0-Day) sofort.

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte einen Sicherheitsworkflow auf GitHub Actions einrichten, der mein Docker-Image und meine Quellcodes mit Trivy bei jeder Code-Push- und Pull-Anfrage (PR) scannt. Können Sie eine vollständige .github/workflows/trivy.yml-Datei erstellen, die den Build nur bei Schwachstellen KRITISCH und HOHER Stufe stoppt (Exit-Code 1), die Ergebnisse im SARIF-Format in das GitHub-Sicherheitsdashboard hochlädt und eine SBOM-Datei im CycloneDX-Format erstellt?

## Häufig gestellte Fragen

- Kann Trivy Docker Container-Images ohne Daemon scannen? Ja. Trivy kann Bilder direkt von Remote-Image-Repositorys (Docker Hub, GitHub Container Registry, AWS ECR usw.) oder lokalen TAR-Archiven herunterladen und scannen, ohne dass ein Docker-Client oder -Daemon erforderlich ist.
- Funktioniert es in Air-Gap-Umgebungen ohne Internetverbindung? Ja. Die Trivy-Datenbank (trivy-db) kann vorab heruntergeladen und in eine geschlossene Netzwerkumgebung verschoben werden. Trivy kann den lokalen Datenbankcache durchsuchen, ohne online zu gehen.
- Was ist SBOM und warum wird Trivy in diesem Bereich bevorzugt? SBOM (Software Bill of Materials) ist eine digitale Inhaltsliste, die alle in Ihrer Software enthaltenen Open-Source-Bibliotheken, Versionen und Lizenzen dokumentiert. Trivy ist eines der wenigen Standardtools, das SBOM sowohl auf Bildebene als auch auf Quellcodeebene erstellen kann.
- Wie kann man Fehlalarme oder akzeptierte Risiken ausschließen? Sie können die CVE-Codes, die Sie ignorieren möchten, Zeile für Zeile auflisten, indem Sie eine .trivyignore-Datei zum Projektstammverzeichnis hinzufügen. Auf diese Weise werden unnötige Kompilierungsunterbrechungen in CI/CD-Pipelines verhindert.

## Verwandte Begriffe aus dem Glossar

- [Secrets](https://trescout.com/de/dictionary/secrets/)
- [SBOM](https://trescout.com/de/dictionary/sbom/)
- [Root](https://trescout.com/de/dictionary/root/)
- [Workflows](https://trescout.com/de/dictionary/workflows/)
- [Database](https://trescout.com/de/dictionary/database/)
- [Binary](https://trescout.com/de/dictionary/binary/)

- **Für wen es gedacht ist:** Für Ingenieure, die Sicherheitsüberprüfungen, geheime Schlüsselprüfungen und SBOM-Generierung in ihren Softwareentwicklungs- und Bereitstellungsprozessen automatisieren möchten.
- **Lizenz:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı)
- **Entwickler:** Aqua Security und Open Source Community
- **Ausgabeformate:** Tabelle, JSON, SARIF, CycloneDX, SPDX, Vorlage

## Links

- [GitHub-Repository →](https://github.com/aquasecurity/trivy)
- [Auf Türkisch lesen →](https://trescout.com/discover/trivy/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-04 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/trivy/
