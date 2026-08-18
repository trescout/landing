# Was ist Caching?

Häufig verwendete Daten werden für den schnellen Zugriff vorübergehend im Speicher gespeichert.

## Definition
Caching ist eine Beschleunigungsmethode, mit der verhindert werden soll, dass ein System wiederholt dieselben Daten berechnet oder von einer entfernten Quelle abruft. Die Daten werden in einen schnell zugänglichen Bereich (Cache) kopiert und von dort bei Bedarf bereitgestellt. Dadurch wird die Gesamtreaktionszeit des Systems erheblich verkürzt.

## So funktioniert es
Wenn das System Daten anfordert, prüft es zunächst den Cache. Wenn die Daten vorhanden sind, werden sie sofort abgerufen, andernfalls werden sie von der Hauptquelle abgerufen und eine Kopie im Cache belassen.

## Wo es eingesetzt wird
Es wird häufig zur Verbesserung der Leistung in Webbrowsern, Anwendungen und großen Rechenzentren eingesetzt.

## Häufig verwechselt mit
Es kann mit einer Datenbank verwechselt werden, aber der Cache ist temporär und schnell, während die Datenbank permanent und größer ist.

## Häufige Fragen
**Was passiert, wenn der Cache voll wird?**
Alte oder selten genutzte Daten werden gelöscht und durch neue Daten ersetzt.


## Verwandte Begriffe
- [KV Cache](/de/dictionary/kv-cache/)
- [Prefix Cache](/de/dictionary/prefix-cache/)
- [Database](/de/dictionary/database/)

## Verwandte Werkzeuge
- [Guava](/de/discover/guava/)
- [Omlx](/de/discover/omlx/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/caching/
