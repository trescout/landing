# Was ist Worktree?

Eine Struktur, die es Ihnen ermöglicht, gleichzeitig an verschiedenen Versionen eines Projekts zu arbeiten, ohne den ursprünglichen Projektordner zu verändern.

## Definition
Worktree ermöglicht es Ihnen bei der Softwareentwicklung, verschiedene Zweige (Branches) des Projekts in separaten Ordnern zu öffnen, ohne Ihren Hauptarbeitsbereich zu beeinträchtigen. Während Sie beispielsweise an einer Funktion im Hauptprojekt arbeiten, können Sie gleichzeitig in einem anderen Ordner einen alten Fehler beheben. Dies eliminiert den Zeitverlust und die Verwirrung, die durch ständiges Wechseln der Zweige entstehen.

## So funktioniert es
Sie fügen über Versionskontrollsysteme wie Git einen neuen Worktree hinzu. Das System verknüpft eine Kopie des Projekts in einem anderen Verzeichnis für Sie, und Sie arbeiten dort weiter, ohne das Hauptverzeichnis zu berühren.

## Wo es eingesetzt wird
Es wird in komplexen Softwareprojekten verwendet, wenn während langwieriger Funktionsentwicklungen dringende Fehlerbehebungen durchgeführt werden müssen.

## Häufig verwechselt mit
Es ist nicht dasselbe wie das bloße Kopieren von Ordnern; Worktrees sind mit demselben Git-Repository verbunden und arbeiten synchron miteinander.

## Häufige Fragen
**Warum kopieren wir nicht einfach separate Ordner?**
Das Kopieren verschwendet Speicherplatz und erschwert die Verwaltung der Git-Historie; Worktree hingegen ist weitaus effizienter.

**Funktioniert es in jedem Git-Projekt?**
Ja, diese Funktion wird in allen modernen Git-Versionen unterstützt.


## Verwandte Begriffe
- [Source Control](/de/dictionary/source-control/)
- [Git Push](/de/dictionary/git-push/)
- [Repository Checkout](/de/dictionary/repository-checkout/)

## Verwandte Werkzeuge
- [Worktrunk](/de/discover/worktrunk/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/worktree/
