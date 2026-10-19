# Sicherheitstests für KI-Modelle

YuJunZhiXue/dsh-purge ist ein JavaScript-Tool, das darauf abzielt, Sicherheitsbeschränkungen (Jailbreak) für verschiedene KI-Modelle mithilfe anpassbarer Prompts zu umgehen. Das Projekt ermöglicht es Benutzern, eigene Befehle für verschiedene Modelle zu definieren und konzentriert sich standardmäßig auf lokale Modelle.

- ★ 7.527
- JavaScript
- GitHub Trending · 2026-10-19

## Aktualisierungen

- **19. Oktober 2026:** Sterne 7,496 → 7,527, neueste Version v1.1.71 (11. Oktober 2026).

## Was es bringt

- Sie können die Sicherheits- und Kontrollregeln der KI-Laufzeitumgebung DeepSeek Harness in einer lokalen Umgebung testen.
- Durch die Definition benutzerdefinierter Prompts für verschiedene Modelle können Sie Modellantworten und Systemfilter direkt untersuchen.
- Sie können System-Patches über die Entwicklerschnittstelle verwalten und jederzeit zum vorherigen Zustand zurückkehren.

## Installation

**Klonen des Repositorys in das Plugin-Verzeichnis**

```
git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge"
```

**Wechseln in das entsprechende Profilverzeichnis und Abhängigkeiten**

```
cd "$DSH_HOME/profiles/web"   # 或 profiles/desktop
pnpm install
```

## Ausführung

**Validierung der Codesyntax**

```
node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Um eine Sicherheitsbewertung in der KI-Laufzeitumgebung DeepSeek Harness durchführen zu können, möchte ich das Plugin dsh-purge installieren und validieren. Führe zunächst den Befehl git clone https://github.com/YuJunZhiXue/dsh-purge.git "$DSH_HOME/plugins/dsh-purge" aus, um das Repository mit der Versionskontrollsoftware Git herunterzuladen. Führe anschließend den Schritt cd "$DSH_HOME/profiles/web" # oder profiles/desktop
pnpm install aus, um die Profilabhängigkeiten mit dem Paketmanager pnpm zu installieren. Führe als letzten Schritt den Befehl node --check lib/index.js
node --check lib/core.js
node --check lib/rewind.js
node --check lib/skills.js
node --check client.js aus, um die Dateien mit der JavaScript-Laufzeitumgebung Node.js zu überprüfen.

Repository: https://github.com/YuJunZhiXue/dsh-purge. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Harness](https://trescout.com/de/dictionary/harness/)
- [Clone](https://trescout.com/de/dictionary/clone/)
- [AI Skills](https://trescout.com/de/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Dies ist für Forscher gedacht, die die Sicherheitsgrenzen und Systemfilter von KI-Modellen in ihrer eigenen lokalen Umgebung überprüfen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/YuJunZhiXue/dsh-purge)
- [Auf Türkisch lesen →](https://trescout.com/discover/dsh-purge/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-19 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/dsh-purge/
