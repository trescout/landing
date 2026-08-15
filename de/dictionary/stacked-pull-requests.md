# Was ist Stacked Pull Requests?

Dabei handelt es sich um eine Methode zur schrittweisen Einführung großer Softwareänderungen in das System in kleinen, überschaubaren Teilen, die miteinander verbunden sind.

## Definition
Bei der Entwicklung von Software reichen Sie nicht eine große Änderung auf einmal ein, sondern unterteilen diese Änderung in logische Teile und reichen sie nacheinander ein. Jedes Stück baut auf dem vorherigen auf. Auf diese Weise können Personen, die Ihren Code überprüfen, kleine und gezielte Schritte schneller genehmigen, anstatt zu versuchen, eine komplexe Struktur auf einmal zu verstehen.

## So funktioniert es
Teilen Sie Ihre Änderungen in logische Blöcke auf. Reichen Sie den ersten Block ein und beginnen Sie mit dem Aufbau des nächsten darauf, bevor er genehmigt wird. Dieser Prozess stellt sicher, dass der Code sauberer bleibt und Fehler früher erkannt werden.

## Wo es eingesetzt wird
Es wird in internen Codeüberprüfungsprozessen des Teams auf Plattformen wie GitHub oder GitLab verwendet, insbesondere bei der Entwicklung großer Funktionen.

## Häufig verwechselt mit
Es kann mit einem einzelnen großen „Pull Request“ verwechselt werden; Diese Methode bietet jedoch einen fragmentierten und sequenziellen Ansatz.

## Häufige Fragen
**Warum schicken wir nicht alles auf einmal?**
Große Änderungen sind anfälliger für Fehler und erschweren die Überprüfung des Codes durch andere.

**Wenn alles miteinander verbunden ist, was passiert, wenn ein Teil kaputt geht?**
Da es sequentiell ist, müssen Sie Ihre Änderungen sorgfältig verwalten, um ein Unterbrechen der Kette zu vermeiden.


## Verwandte Begriffe
- [Code Review](/de/dictionary/code-review/)
- [Git Push](/de/dictionary/git-push/)
- [Checkout](/de/dictionary/checkout/)

## Verwandte Werkzeuge
- [Gh Stack](/de/discover/gh-stack/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/stacked-pull-requests/
