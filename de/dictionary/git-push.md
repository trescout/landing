# Was ist Git Push?

> Englisch: Git Push · Wortherkunft: britischer Slang git + lateinisch pulsare (stoßen/antreiben)

**Kategorie:** Dev  
**Letzte Aktualisierung:** 2026-09-19

Git Push ist der fundamentale Versionskontrollbefehl, der lokal erstellte Commits, Quellcode-Änderungen und Versionshistorien an ein entferntes Git-Repository überträgt und Entwicklungszweige synchronisiert.

## Als Analogie
Es ist wie das Schreiben neuer Kapitel eines Buches auf dem eigenen Laptop, die nach Fertigstellung per Upload an die Verlagsredaktion übermittelt werden, damit alle Lektoren auf demselben Stand arbeiten.

## 1. Definition und das 4-Ebenen-Datenmodell von Git
Git ist ein verteiltes Versionskontrollsystem (DVCS) mit vier Speicherbereichen: dem Arbeitsverzeichnis (Working Tree), der Staging Area (Index), dem lokalen Repository (.git-Ordner) und dem entfernten Repository (GitHub, GitLab). Während <code>git commit</code> Änderungen lokal auf der Festplatte speichert, überträgt erst <code>git push</code> diese Daten über das Netzwerk an den zentralen Server des Teams.

## 2. Die wichtigsten Befehle im Überblick
Gängige Anweisungen im Programmieralltag:
- **Erstes Veröffentlichen eines Zweigs:** <code>git push -u origin mein-branch</code> (verknüpft den lokalen Zweig mit dem Remote-Server).- **Standard-Push:** <code>git push</code> (aktualisiert den verfolgten Upstream-Zweig).- **Tags übertragen:** <code>git push origin --tags</code> (veröffentlicht Release-Markierungen).- **Entfernten Zweig löschen:** <code>git push origin --delete alter-branch</code>.- **Sicheres Überschreiben:** <code>git push --force-with-lease</code> (überschreibt Remote-Historien nur dann, wenn zwischenzeitlich kein Kollege Änderungen hochgeladen hat).

## 3. Typische Fehler und deren Behebung
Lösungen für häufige Push-Fehlermeldungen:
- **fatal: [rejected - non-fast-forward]:** Auf dem Server liegen Commits, die lokal fehlen. Lösung: <code>git pull --rebase origin main</code> ausführen, Konflikte lösen und erneut pushen.- **fatal: The current branch has no upstream branch:** Den Parameter <code>-u</code> verwenden, um den Remote-Zweig festzulegen.- **Abweisung großer Dateien:** Git blockiert Dateien über 100 MB; für große Binärdateien ist Git LFS (Large File Storage) einzusetzen.

## Häufige Fragen

**Worin liegt der Unterschied zwischen 'git commit' und 'git push'?**  
Git commit sichert den Bearbeitungsstand lokal auf dem Rechner; git push lädt diese Schnappschüsse auf den gemeinsamen Server wie GitHub hoch.

**Warum ist '--force-with-lease' sicherer als '--force'?**  
Weil --force den Remote-Server blind überschreibt; --force-with-lease bricht ab, wenn ein Teammitglied in der Zwischenzeit neue Commits hochgeladen hat.

**Welche Aufgabe haben Pre-Push-Hooks?**  
Sie führen vor der Übertragung automatisierte Tests und Linter auf dem Entwicklungsrechner aus und verhindern den Push bei Fehlern.

**Kann man mit einem Befehl zu zwei verschiedenen Servern pushen?**  
Ja, indem man in der Datei .git/config unter demselben Remote-Namen mehrere Push-URLs hinterlegt.

## Verwandte Begriffe
- [CLI](/de/dictionary/cli/)
- [Code Snippets](/de/dictionary/code-snippets/)
- [Checkout](/de/dictionary/checkout/)

## Verwandte Tools
- [No Mistakes](/de/discover/no-mistakes/)

---
Quelle: TreScout Tech-Glossar · https://trescout.com/de/dictionary/git-push/
