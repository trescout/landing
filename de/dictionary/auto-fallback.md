# Was ist Auto-fallback?

Wenn in einem System ein Fehler auftritt oder die Hauptmethode fehlschlägt, wechselt das System automatisch zu einer sichereren oder alternativen Methode.

## Definition
Auto-Fallback stellt sicher, dass das System nicht „aufgibt“. Wenn beispielsweise Ihr fortschrittlichstes KI-Modell nicht reagiert, wechselt das System automatisch zu einem schnelleren, aber einfacheren Modell, um den Vorgang abzuschließen. Dies ist eine wichtige Sicherheitsmaßnahme, um sicherzustellen, dass das Benutzererlebnis unterbrechungsfrei bleibt.

## So funktioniert es
In die Software ist eine „Wenn es nicht funktioniert, tun Sie dies“-Regel integriert. Das System überprüft ständig den Status und aktiviert die Backup-Methode, wenn die Hauptmethode einen Fehlercode zurückgibt.

## Wo es eingesetzt wird
Es wird in Diensten der künstlichen Intelligenz, Netzwerkverbindungen und Serververwaltung eingesetzt.

## Häufig verwechselt mit
Es ähnelt der Fehlerbehandlung. Allerdings bezieht sich Auto-Fallback direkt auf eine alternative Lösung.

## Häufige Fragen
**Führt diese Funktion zu einer Verlangsamung?**
Manchmal kann der Übergangsprozess eine Verzögerung von Millisekunden verursachen, aber das ist besser als ein vollständiger Stillstand des Systems.

**Funktioniert es immer?**
Wenn auch die Backup-Methode fehlerhaft ist, wird das System weiterhin ausfallen, daher müssen auch Backups zuverlässig sein.


## Verwandte Begriffe
- [Observability](/de/dictionary/observability/)
- [Runtime](/de/dictionary/runtime/)
- [AI Gateway](/de/dictionary/ai-gateway/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/auto-fallback/
