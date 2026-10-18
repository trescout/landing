# Sichere und einfache Dateiübertragung

Croc ist ein Tool, das mittels Ende-zu-Ende-Verschlüsselung eine sichere Datei- und Datenübertragung zwischen zwei Computern ermöglicht. Diese mit der Programmiersprache Go entwickelte Software nutzt einen temporären Relay-Mechanismus, um den Übertragungsprozess zu erleichtern.

- ★ 40.451
- Go
- GitHub Trending · 2026-07-22

## Aktualisierungen

- **27. September 2026:** Sterne 40,324 → 40,451, neueste Version v11.5.4 (26. September 2026).
- **14. September 2026:** Sterne 40,287 → 40,324, neueste Version v11.5.3 (13. September 2026).
- **10. September 2026:** Sterne 40,279 → 40,287, neueste Version v11.5.2 (9. September 2026).
- **9. September 2026:** Sterne 40,262 → 40,279, neueste Version v11.5.1 (8. September 2026).

## Was es bringt

- Ende-zu-Ende verschlüsselte Datenübertragung
- Kompatibilität zwischen verschiedenen Betriebssystemen
- Unterbrochene Übertragungen dort fortsetzen, wo sie aufgehört haben

## Installation

**Allgemeine Installation**

```
curl https://getcroc.schollz.com | bash
```

**Installation auf macOS**

```
brew install croc
```

## Ausführung

**Datei senden**

```
croc send [file(s)-or-folder]
```

**Dateien empfangen**

```
croc code-phrase
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte Dateien mit dem Croc-Tool sicher zwischen zwei Computern übertragen. Wie kann ich den mir gegebenen Codeausdruck abgleichen, wenn ich den Befehl „croc send [Dateiname]“ auf der Senderseite mit dem Befehl „croc [Codeausdruck]“ auf der Empfängerseite ausführe und die Übertragung starte? Gibt es eine besondere Einstellung, auf die ich achten sollte, um sicherzustellen, dass bei der Übertragung eine Ende-zu-Ende-Verschlüsselung erfolgt und der Vorgang sicher ist?

Repository: https://github.com/schollz/croc. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [End-to-End Encryption](https://trescout.com/de/dictionary/end-to-end-encryption/)
- [Relay](https://trescout.com/de/dictionary/relay/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für alle, die verschlüsselte und schnelle Dateien zwischen zwei Geräten teilen möchten, ohne dass ein Zwischenserver erforderlich ist.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/schollz/croc)
- [Auf Türkisch lesen →](https://trescout.com/discover/croc/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-07-22 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/croc/
