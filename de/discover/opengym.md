# Fitness-Tracking-Software, die auf Ihrem eigenen Server läuft

OpenGym ist ein Open-Source-Studioverwaltungstool zum Planen von Trainingsroutinen und Verfolgen von Eigengewichtsübungen. Die Software ermöglicht es Benutzern, ihre Daten auf eigenen Servern zu hosten, und unterstützt den Datenimport von beliebten Fitness-Apps (Strong, Hevy).

- ★ 13.304
- JavaScript
- GitHub Trending · 2026-10-05

## Aktualisierungen

- **18. Oktober 2026:** Sterne 12,021 → 13,304, neueste Version v1.4.1 (10. Oktober 2026).
- **15. Oktober 2026:** Sterne 10,912 → 12,021, neueste Version v1.4.1 (10. Oktober 2026).
- **13. Oktober 2026:** Sterne 9,501 → 10,912, neueste Version v1.4.1 (10. Oktober 2026).
- **11. Oktober 2026:** Sterne 8,392 → 9,501, neueste Version v1.4.1 (10. Oktober 2026).

## Was es bringt

- Sie können Ihre Trainingsdaten an einem sicheren Ort speichern, den Sie selbst kontrollieren, anstatt auf Servern von Drittanbietern.
- Sie können Ihre vergangenen Trainingsdaten ganz einfach aus beliebten Fitness-Apps wie Strong und Hevy importieren.
- Selbst ohne Internetverbindung können Sie Ihre Trainingseinheiten von Ihrem Telefon oder Computer aus planen und verfolgen.

## Installation

**Mit der Docker-Container-Verwaltungsplattform k**

```
git clone https://github.com/DuarteSantos8/openGym
cd openGym
cp .env.example .env
docker compose pull      # prebuilt images, amd64 + arm64 (skip this to build from source)
docker compose up -d
```

## Wenn Sie nicht programmieren

Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte die Fitness-Tracking-Software openGym auf der Docker-Container-Verwaltungsplattform installieren. Könnten Sie mir Schritt für Schritt die Installationsschritte erklären, die mit dem Befehl 'git clone https://github.com/DuarteSantos8/openGym' beginnen, wie die Umgebungsvariablendatei '.env' konfiguriert wird und wie ich nach Abschluss der Installation über den Browser auf die Anwendung zugreifen kann?

Repository: https://github.com/DuarteSantos8/openGym. Richte dich bei der Installation und Ausführung nach den offiziellen Anweisungen in der README-Datei dieses Repositorys.

Prüfe vor dem Start, unter welchem Betriebssystem wir arbeiten und ob die notwendigen Tools (z. B. Python, Node.js, Git, Docker) installiert sind. Installiere fehlende Tools schrittweise entsprechend diesem System.

Erstelle einen neuen, leeren Ordner für die Arbeit. Rühre keine Dateien außerhalb dieses Ordners an und lösche nichts. Sag mir vor jedem Befehl in einem Satz, was du tun wirst.

Falls ein API-Schlüssel erforderlich ist, fordere mich nicht auf, ihn in den Chat zu schreiben. Zeig mir, wie ich ihn zur .env-Datei hinzufüge und stelle sicher, dass diese Datei nicht an Git übertragen wird.

Sag mir, was ich am Ende jedes Schrittes auf dem Bildschirm sehen sollte. Wenn ein Fehler auftritt, füge ich die Fehlermeldung exakt so ein, wie sie ist, und wir beheben sie gemeinsam.

## Verwandte Begriffe aus dem Glossar

- [Clone](https://trescout.com/de/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es ist für Fitnessbegeisterte gedacht, die Wert auf den Datenschutz ihrer Trainingsdaten legen und ihre Studio-Routinen kostenlos auf ihrem eigenen Server verfolgen möchten.
- **Lizenz:** AGPL-3.0

## Links

- [GitHub-Repository →](https://github.com/DuarteSantos8/openGym)
- [Auf Türkisch lesen →](https://trescout.com/discover/opengym/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-05 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Der Präsentationstext wurde mit KI aus der eigenen Dokumentation des Repositories erstellt und diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/opengym/
