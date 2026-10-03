# Was ist Git Push?

Git Push ist der grundlegende Git-Befehl, der committete Codeblöcke, die Commit-Historie und Objekte aus Ihrer lokalen Entwicklungsumgebung auf einen Remote-Git-Server überträgt und den Remote-Branch aktualisiert.

## 1. Definition und das 4-Schichten-Datenmodell von Git
Git ist ein verteiltes Versionskontrollsystem (DVCS). In dieser Architektur durchlaufen Codeänderungen 4 verschiedene Arbeitsbereiche, bevor sie einen Remote-Server erreichen:

## 2. Die am häufigsten verwendeten Befehlsvorlagen (Cheatsheet)
Das Flag -u oder --set-upstream verknüpft Ihren lokalen Branch dauerhaft mit dem Remote-Branch. Nach dieser Zuordnung reicht es aus, wenn Sie sich auf demselben Branch befinden, einfach nur git push oder git pull einzugeben.

## 3. Die am häufigsten auftretenden Git-Push-Fehler und Lösungen

## Häufige Fragen
**Was bedeutet Git Push und wozu dient es?**
Git Push ist der grundlegende Befehl, der die auf Ihrem lokalen Computer abgeschlossenen Commits auf Remote-Server wie GitHub, GitLab oder Bitbucket hochlädt und so die Remote-Repositories mit dem lokalen Status synchronisiert.

**Was bedeutet das -u im Befehl git push -u origin main?**
Das Flag -u (--set-upstream) stellt eine Tracking-Verbindung zwischen dem lokalen Branch und dem Remote-Branch her. Dadurch können Sie bei zukünftigen Vorgängen einfach nur git push schreiben, ohne das Ziel angeben zu müssen.

**Warum sollte man anstelle von git push -f lieber --force-with-lease verwenden?**
git push -f löscht Änderungen, die andere im Remote-Repository vorgenommen haben, dauerhaft, ohne sie zu prüfen. --force-with-lease hingegen schützt den Code Ihrer Teamkollegen, indem es das Überschreiben nur dann zulässt, wenn sich der Branch noch in dem Zustand befindet, in dem Sie ihn zuletzt abgerufen haben.

**Wie lässt sich der Fehler „non-fast-forward“ beheben?**
Dieser Fehler tritt auf, weil neue Commits im Remote-Repository noch nicht in Ihrem lokalen Repository vorhanden sind. Zur Lösung sollten die Commits durch Ausführen von git pull --rebase origin <branch> aktualisiert und anschließend erneut git push ausgeführt werden.


## Verwandte Begriffe
- [CLI](/de/dictionary/cli/)
- [Deployment](/de/dictionary/deployment/)
- [Production Pipeline](/de/dictionary/production-pipeline/)
- [Patch](/de/dictionary/patch/)
- [Tech Stack](/de/dictionary/tech-stack/)

## Verwandte Werkzeuge
- [No Mistakes](/de/discover/no-mistakes/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/git-push/
