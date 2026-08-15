# Was ist Durable Objects?

Dabei handelt es sich um kleine Softwareeinheiten, die kontinuierlich im Internet laufen und Daten speichern können, ohne ihren Zustand zu verlieren.

## Definition
Normalerweise sind Programme im Internet temporär, aber diese Strukturen funktionieren ohne Unterbrechung, indem sie die Daten in sich behalten. Sie vergessen die Daten auch dann nicht, wenn eine Benutzerinteraktion endet. Ideal zur Aufrechterhaltung der Konsistenz in verteilten Systemen.

## So funktioniert es
Sie leben mit einer bestimmten Identität auf dem Server und verarbeiten jede eingehende Anfrage mit dem aktuellen Status in ihrem Speicher.

## Wo es eingesetzt wird
Es wird in Echtzeitspielen, Chat-Anwendungen und Webdiensten verwendet, deren Status beibehalten werden muss.

## Häufig verwechselt mit
Nicht zu verwechseln mit temporären Serverfunktionen (serverlos); weil sie jedes Mal bei Null anfangen.

## Häufige Fragen
**Wo werden die Daten gespeichert?**
Die Speicherung erfolgt innerhalb des Volumes selbst, also direkt als Teil der Betriebsumgebung.


## Verwandte Begriffe
- [Runtime](/de/dictionary/runtime/)
- [State Management](/de/dictionary/state-management/)
- [Distributed](/de/dictionary/distributed/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/durable-objects/
