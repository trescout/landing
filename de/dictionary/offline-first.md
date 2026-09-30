# Was ist Offline-first?

Es handelt sich um einen Software-Design-Ansatz, der alle Grundfunktionen der Anwendung ohne Unterbrechung weiterführt, auch wenn die Internetverbindung unterbrochen wird.

## Definition
Bei diesem Ansatz speichert die Anwendung zunächst Daten auf dem eigenen Gerät des Benutzers und führt Vorgänge lokal aus. Sobald eine Internetverbindung besteht, werden die Daten auf dem Gerät im Hintergrund stillschweigend mit dem Cloud-Server synchronisiert. Als TreScout empfehlen wir diese Architektur, um das Benutzererlebnis auf höchstem Niveau zu halten und nicht durch Verbindungsunterbrechungen beeinträchtigt zu werden.

## So funktioniert es
Wenn die Anwendung geöffnet wird, liest sie die Daten aus der lokalen Datenbank auf dem Gerät, anstatt sie von einem Remote-Server abzurufen. Alle neuen Datensätze und vom Benutzer vorgenommenen Änderungen werden zunächst in diese lokale Datenbank geschrieben. Ein spezieller Synchronisationsmechanismus, der im Hintergrund läuft, überprüft ständig die Internetverbindung und synchronisiert die Daten bilateral mit dem Server.

## Wo es eingesetzt wird
Es wird häufig in Notizanwendungen beim Fahren in der U-Bahn, in Auftragsverfolgungssystemen, in denen Außendienstmitarbeiter Daten an Orten ohne Internetverbindung eingeben, und in Kartenanwendungen verwendet.

## Häufig verwechselt mit
Es wird mit dem Offline-Betriebsmodus verwechselt: Während der Offline-Modus nur darauf abzielt, Fehler zu verhindern, wenn kein Internet vorhanden ist, basiert der Offline-First-Ansatz das Hauptarbeitsprinzip der Anwendung vollständig auf lokalen Daten.

## Häufige Fragen
**Was passiert, wenn offline vorgenommene Änderungen online mit den Daten anderer Benutzer in Konflikt geraten?**
Konfliktlösungsalgorithmen in der Software kommen ins Spiel und führen die Daten sicher zusammen, wobei die letzte vorgenommene Änderung erhalten bleibt oder der Benutzer aufgefordert wird, sie anzuzeigen.

**Nehmen Offline-First-Anwendungen viel Platz auf dem Gerät ein?**
Nein, da auf dem Gerät nur textbasierte Daten und kleine Dateien gespeichert werden, die der Nutzer aktiv nutzt, wird der Speicherplatz nicht unnötig belegt.


## Verwandte Begriffe
- [Local-first](/de/dictionary/local-first/)
- [Offline](/de/dictionary/offline/)
- [Database](/de/dictionary/database/)
- [State Management](/de/dictionary/state-management/)

## Verwandte Werkzeuge
- [LAP](/de/discover/lap/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/offline-first/
