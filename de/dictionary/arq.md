# Was ist ARQ?

*Glossar · Dev · Zuletzt aktualisiert: 12. Juni 2026*

> Automatic Repeat Request

Dabei handelt es sich um einen Fehlerkontrollmechanismus, der sicherstellt, dass Informationen automatisch erneut gesendet werden, wenn bei der Datenübertragung ein Fehler auftritt.

## Definition

Beim Senden von Daten über das Internet können Pakete manchmal verloren gehen oder beschädigt werden. ARQ prüft, ob die empfangende Partei die Daten erhalten hat, und wenn es einen Fehler erkennt, teilt es dem Absender mit: „Ich habe diese Daten nicht erhalten, senden Sie sie erneut.“ Dadurch wird sichergestellt, dass die Daten vollständig und fehlerfrei empfangen werden.

***Analogie:** Während des Telefonierens sagt der andere Teilnehmer: „Ich habe es nicht verstanden, können Sie es noch einmal sagen?“ Es ist, als würde man diesen Satz sagen und wiederholen.*

## So funktioniert es

Der Absender sendet das Datenpaket und wartet auf eine Bestätigung. Erfolgt innerhalb einer bestimmten Frist keine Bestätigung, gilt das Paket als beschädigt oder verloren und wird erneut versendet.

## Wo es eingesetzt wird

Es wird in den Grundprotokollen und Netzwerkprotokollen des Internets verwendet, beispielsweise im TCP-Protokoll.

## Häufige Fragen

**Warum ist es so wichtig?**

Internetverbindungen sind nicht immer perfekt; ARQ gewährleistet die Zuverlässigkeit der Daten.

**Wird es zu Verzögerungen kommen?**

Ja, das erneute Versenden fehlerhafter Pakete kann den Prozess etwas verlangsamen.

## Verwandte Begriffe

- [API](https://trescout.com/de/dictionary/api/)
- [DNS Tunneling](https://trescout.com/de/dictionary/dns-tunneling/)
- [Computer Science](https://trescout.com/de/dictionary/computer-science/)

Diese Erklärung wurde für TreScout in einfacher Sprache verfasst und **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung. Wenn etwas falsch oder unvollständig wirkt, schreiben Sie an [hello@trescout.com](mailto:hello@trescout.com). [Auf Türkisch lesen →](https://trescout.com/dictionary/arq/)

---
Quelle: TreScout Glossar · https://trescout.com/de/dictionary/arq/
