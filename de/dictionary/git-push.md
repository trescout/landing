# Was ist Git Push?

*Glossar · Dev · Zuletzt aktualisiert: 19. September 2026*

Git Push ist der grundlegende Git-Befehl, der committete Codeblöcke, die Commit-Historie und Objekte aus Ihrer lokalen Entwicklungsumgebung auf einen Remote-Git-Server überträgt und den Remote-Branch aktualisiert.

## 1. Definition und das 4-Schichten-Datenmodell von Git

Git ist ein verteiltes Versionskontrollsystem (DVCS). In dieser Architektur durchlaufen Codeänderungen 4 verschiedene Arbeitsbereiche, bevor sie einen Remote-Server erreichen:

```
[Çalışma Dizini] ──git add──> [Staging / Index] ──git commit──> [Yerel Depo] ──git push──> [Uzak Depo]
(Working Directory)            (Hazırlık Alanı)                 (.git veritabanı)            (GitHub/GitLab)
```

1. Working Directory (Arbeitsverzeichnis): Der Live-Code-Bereich, in dem Sie Ihre Dateien bearbeiten.
2. Staging Area / Index (Bereitstellungsbereich): Änderungen, die Sie mit git add für den nächsten Commit ausgewählt haben.
3. Lokales Repository: Kontrollpunkte, die mit git commit dauerhaft im .git-Verzeichnis auf Ihrer eigenen Festplatte versiegelt werden.
4. Remote Repository (Remote-Repository): Der zentrale Server, auf dem Sie mit git push Ihre Änderungen hochladen, damit Teammitglieder sie sehen können und CI/CD-Pipelines ausgelöst werden.

Beim Ausführen von git push werden nicht nur Textunterschiede übertragen; stattdessen werden die Commit-, Tree- und Blob-Objekte aus der Objekt-Datenbank von Git in einer komprimierten Packfile an den Remote-Server gesendet und die dortige Branch-Referenz wird aktualisiert.

***Analogie:** Es ist so, als würden Sie die Kapitel eines Buches, das Sie auf Ihrem Computer geschrieben haben, in Ihrem lokalen Entwurfsordner speichern und dann dem gemeinsamen Druckzentrum der Druckerei per Kurier mitteilen: „Laden Sie diese Kapitel in das offizielle Archiv hoch und stellen Sie sie in die Druckwarteschlange“.*

## 2. Die am häufigsten verwendeten Befehlsvorlagen (Cheatsheet)

```
git push -u origin feature/auth
```

Das Flag -u oder --set-upstream verknüpft Ihren lokalen Branch dauerhaft mit dem Remote-Branch. Nach dieser Zuordnung reicht es aus, wenn Sie sich auf demselben Branch befinden, einfach nur git push oder git pull einzugeben.

```
git push --force-with-lease
```

Wenn ein Standard-Push nach git commit --amend oder git rebase abgelehnt wird, kann die Verwendung von git push -f die Commits Ihrer Teamkollegen auf dem Server löschen. --force-with-lease ist eine Sicherheitsfunktion, die das Überschreiben nur dann zulässt, wenn nach Ihnen niemand anderes Commits auf diesen Branch gepusht hat.

```
git push origin --delete eski-ozellik-dali
git push origin --tags
```

## 3. Die am häufigsten auftretenden Git-Push-Fehler und Lösungen

- fatal: [rejected - non-fast-forward]: Der Remote-Branch enthält Commits, die lokal noch nicht vorhanden sind. Zur Lösung sollte git pull --rebase origin \<branch> und anschließend git push ausgeführt werden.
- fatal: Der aktuelle Branch hat keinen Upstream-Branch: Für den Branch wurde kein Remote-Gegenstück definiert. Lösung: git push -u origin HEAD.
- remote rejected: pre-receive hook declined: Blockiert durch eine Regel für geschützte Branches oder fehlende Berechtigungen; statt eines direkten Push muss ein Pull Request (PR) erstellt werden.

## Häufige Fragen

**Was bedeutet Git Push und wozu dient es?**

Git Push ist der grundlegende Befehl, der die auf Ihrem lokalen Computer abgeschlossenen Commits auf Remote-Server wie GitHub, GitLab oder Bitbucket hochlädt und so die Remote-Repositories mit dem lokalen Status synchronisiert.

**Was bedeutet das -u im Befehl git push -u origin main?**

Das Flag -u (--set-upstream) stellt eine Tracking-Verbindung zwischen dem lokalen Branch und dem Remote-Branch her. Dadurch können Sie bei zukünftigen Vorgängen einfach nur git push schreiben, ohne das Ziel angeben zu müssen.

**Warum sollte man anstelle von git push -f lieber --force-with-lease verwenden?**

git push -f löscht Änderungen, die andere im Remote-Repository vorgenommen haben, dauerhaft, ohne sie zu prüfen. --force-with-lease hingegen schützt den Code Ihrer Teamkollegen, indem es das Überschreiben nur dann zulässt, wenn sich der Branch noch in dem Zustand befindet, in dem Sie ihn zuletzt abgerufen haben.

**Wie lässt sich der Fehler „non-fast-forward“ beheben?**

Dieser Fehler tritt auf, weil neue Commits im Remote-Repository noch nicht in Ihrem lokalen Repository vorhanden sind. Zur Lösung sollten die Commits durch Ausführen von git pull --rebase origin \<branch> aktualisiert und anschließend erneut git push ausgeführt werden.

## Verwandte Begriffe

- [CLI](https://trescout.com/de/dictionary/cli/)
- [Deployment](https://trescout.com/de/dictionary/deployment/)
- [Production Pipeline](https://trescout.com/de/dictionary/production-pipeline/)
- [Patch](https://trescout.com/de/dictionary/patch/)
- [Tech Stack](https://trescout.com/de/dictionary/tech-stack/)

## Verwandte Werkzeuge

- [No Mistakes](https://trescout.com/de/discover/no-mistakes/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/git-push/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/git-push/
