# Sichere Umgebung für KI-Agenten

Das von NVIDIA entwickelte OpenShell bietet eine sichere und datenschutzorientierte Laufzeitumgebung (Runtime) für autonome KI-Agenten. Diese in der Programmiersprache Rust geschriebene Infrastruktur zielt darauf ab, den Zugriff von Agenten auf Systemressourcen zu isolieren und einen sicheren Ausführungsbereich zu schaffen.

- ★ 16.170
- Rust
- GitHub Trending · 2026-09-29

## Aktualisierungen

- **14. Oktober 2026:** Sterne 15,577 → 16,170, neueste Version v0.1.4 (13. Oktober 2026).
- **9. Oktober 2026:** Sterne 15,205 → 15,577, neueste Version v0.1.3 (9. Oktober 2026).
- **7. Oktober 2026:** Sterne 14,197 → 15,205, neueste Version v0.1.2 (28. September 2026).
- **2. Oktober 2026:** Sterne 12,978 → 14,197, neueste Version v0.1.2 (28. September 2026).

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

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Um das OpenShell-Tool zu installieren und zu testen, kannst du folgende Befehle verwenden: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh und anschließend den Befehl openshell sandbox create --name demo ausführen, um eine Demoumgebung zu erstellen.

Repository: https://github.com/NVIDIA/OpenShell. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Sandbox](https://trescout.com/de/dictionary/sandbox/)
- [Runtime](https://trescout.com/de/dictionary/runtime/)
- [Rust](https://trescout.com/de/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Entwickler, die KI-Agenten in einer sicheren und isolierten Umgebung ausführen möchten, ohne ihnen vollen Zugriff auf alle Systemressourcen zu gewähren.
- **Lizenz:** Apache-2.0

## Links

- [GitHub-Repository →](https://github.com/NVIDIA/OpenShell)
- [Auf Türkisch lesen →](https://trescout.com/discover/openshell/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-29 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/openshell/
