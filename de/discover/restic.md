# Sichern Sie Ihre Daten sicher, indem Sie sie verschlüsseln

Restic wurde mit der Go-Sprache entwickelt und bietet ein Open-Source-Backup-Programm, das Daten durch Verschlüsselung schnell und effizient sichert. Dieses Tool, das verschiedene Speichersysteme unterstützt, spart Speicherplatz mit der inkrementellen Backup-Methode.

- ★ 35.302
- GitHub Trending · 2026-06-12

**Hinweis von TreScout:** Es speichert Ihre Backups, indem es sie verschlüsselt, und nimmt keinen Speicherplatz ein, da dieselbe Datei nicht zweimal geschrieben wird. Es verfügt über keine anklickbare Oberfläche, es wird über die Befehlszeile ausgeführt und Sie legen die Aufgabe fest, alte Backups zu bereinigen, da sonst der Speicher mit der Zeit anschwillt. Versuchen Sie, eine Datei am selben Tag wiederherzustellen, an dem Sie sie installiert haben. Andernfalls können Sie nicht erkennen, dass die Sicherung tatsächlich funktioniert hat.

## Aktualisierungen

- **2. August 2026:** Sterne 34,273 → 35,302, neueste Version v0.19.1 (5. Juli 2026).

## Was es bringt

- Bietet hohe Sicherheit durch Verschlüsselung der Daten
- Spart Speicherplatz durch inkrementelles Backup
- Kompatibel mit verschiedenen Cloud- und lokalen Speichersystemen

## Installation

**macOS · Homebrew**

```
brew install restic
```

**Windows · winget**

```
winget install restic.restic
```

## Ausführung

**Backup-Repository erstellen**

```
restic init --repo /path/to/repo
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte meine Daten mit Restic sicher sichern. Wie kann ich einen lokalen Ordner oder ein bestimmtes Verzeichnis in einen verschlüsselten Backup-Speicher exportieren? Können Sie bitte Schritt für Schritt erklären, wie das Backup-Repository erstellt und der erste Backup-Prozess gestartet wird, damit meine Daten verschlüsselt werden?

Repository: https://github.com/restic/restic. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Backup Program](https://trescout.com/de/dictionary/backup-program/)
- [Incremental Backup](https://trescout.com/de/dictionary/incremental-backup/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es eignet sich für alle Nutzer, die ihre Daten schnell und effizient durch Verschlüsselung sichern möchten.
- **Lizenz:** BSD-2-Clause

## Links

- [GitHub-Repository →](https://github.com/restic/restic)
- [Auf Türkisch lesen →](https://trescout.com/discover/restic/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-06-12 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/restic/
