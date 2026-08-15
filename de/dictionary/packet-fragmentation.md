# Was ist Packet Fragmentation?

Dabei werden die über das Internet gesendeten Daten entsprechend der Übertragungskapazität des Netzwerks in kleinere Teile aufgeteilt.

## Definition
Beim Senden von Daten im Internet hat jedes Netzwerk eine maximale Größe, die es übertragen kann. Wenn die von Ihnen gesendeten Daten größer sind als diese Größe, zerlegt das System sie in kleine Teile, übermittelt sie an den Zielort und setzt sie dort wieder zusammen.

## So funktioniert es
Während Daten gesendet werden, überprüfen Netzwerkgeräte die Größe des Pakets. Wenn das Limit überschritten wird, wird das Paket fragmentiert und jedes Fragment erhält eine „Sequenznummer“. Das empfangende Gerät prüft diese Nummern und setzt die Teile in der richtigen Reihenfolge zusammen.

## Wo es eingesetzt wird
Dies geschieht ständig im Hintergrund während Internetprotokollen und Netzwerkprozessen.

## Häufig verwechselt mit
Es kann mit Datenverlust verwechselt werden, es handelt sich jedoch um einen kontrollierten Partitionierungsprozess.

## Häufige Fragen
**Was passiert, wenn Teile verloren gehen?**
Das empfangende Gerät erkennt, dass Teile fehlen und fordert den Absender auf, dieses Teil erneut zu senden.


## Verwandte Begriffe
- [Networking Stack](/de/dictionary/networking-stack/)
- [DNS Tunneling](/de/dictionary/dns-tunneling/)

## Verwandte Werkzeuge
- [Zapret Discord Youtube](/de/discover/zapret-discord-youtube/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/packet-fragmentation/
