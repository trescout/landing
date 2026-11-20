# Verwaltbare Workflows für Ihre Coding-Agenten

LoopForge, entwickelt von Tencent, ist ein selbst gehostetes Workflow-Tool zur Verwaltung der Bereitstellungsprozesse von Coding-Agenten. Es unterstützt lokale Coding-Assistentenprozesse, indem es Software wie CodeBuddy, Codex und Claude Code mit Skripten und menschlichen Genehmigungsmechanismen orchestriert.

- ★ 5.104
- Go
- GitHub Trending · 2026-11-15

## Aktualisierungen

- **20. November 2026:** Sterne 3,785 → 5,104, neueste Version v0.4.0 (17. November 2026).
- **18. November 2026:** Sterne 2,090 → 3,785, neueste Version v0.4.0 (17. November 2026).
- **16. November 2026:** Sterne 986 → 2,090, neueste Version v0.3.8 (12. November 2026).
- **15. November 2026:** Sterne 983 → 986, neueste Version v0.3.8 (12. November 2026).

## Was es bringt

- Führt KI-Coding-Tools sicher in Sandbox-Umgebungen aus.
- Ermöglicht reproduzierbare Bereitstellungen durch Standardprozesse und menschliche Freigabeschritte.
- Weist Rollen Aufgaben über eine Chat-Oberfläche zu oder führt schrittweise Workflows aus.

## Installation

**Repository klonen und System starten**

```
git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh
```

**Mit alternativer Image-Quelle starten**

```
MIRROR=ghcr.nju.edu.cn ./start.sh
```

## Ausführung

**Coding-Assistenten im Projekt einrichten**

```
# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Um die Bereitstellungsprozesse von Coding-Agenten auf meinem eigenen Server zu verwalten, möchte ich das LoopForge-System einrichten. Klonen Sie zunächst das Repository und starten Sie das System, indem Sie die Befehlssequenz `git clone https://github.com/Tencent/LoopForge.git
cd LoopForge
./start.sh` ausführen. Sollte es während des Downloads zu Hängern kommen, verwenden Sie den Befehl `MIRROR=ghcr.nju.edu.cn ./start.sh`, um die Images von einem alternativen Server abzurufen und die Einrichtung abzuschließen. Führen Sie den Befehl `# Run inside your target project, e.g. for Claude Code
npx -y loopforge-cli@latest install claude` in Ihrem Zielprojekt aus, um den Coding-Assistenten zu installieren.

Repository: https://github.com/Tencent/LoopForge. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Self-hosted](https://trescout.com/de/dictionary/self-hosted/)
- [Clone](https://trescout.com/de/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Teams, die KI-gestützte Codierungs-Agenten in ihrer eigenen Infrastruktur mit menschlicher Freigabe und Standard-Arbeitsabläufen verwalten möchten.

## Links

- [GitHub-Repository →](https://github.com/Tencent/LoopForge)
- [Auf Türkisch lesen →](https://trescout.com/discover/loopforge/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-11-15 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/loopforge/
