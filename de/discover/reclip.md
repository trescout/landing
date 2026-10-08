# Laden Sie Internetvideos auf Ihrem eigenen Server herunter

Reclip, entwickelt von Averygan, ist ein leichtgewichtiges und selbst gehostetes Tool zum Herunterladen von Videos von fast allen Internetseiten. Es ermöglicht Ihnen, Mediendateien über eine einfache Weboberfläche auf Ihrem lokalen Gerät zu speichern.

- ★ 10.476
- HTML
- GitHub Trending · 2026-09-02

## Aktualisierungen

- **30. September 2026:** Sterne 9,067 → 10,476.
- **11. September 2026:** Sterne 7,951 → 9,067.

## Was es bringt

- Lädt Video- und Audiodateien von über 1000 Websites wie YouTube und Instagram herunter.
- Speichert heruntergeladene Dateien im MP4-Video- oder MP3-Audioformat.
- Bietet eine einfache und schnelle Benutzeroberfläche, die über einen Webbrowser funktioniert.

## Installation

**Standardinstallation**

```
brew install yt-dlp ffmpeg    # or apt install ffmpeg && pip install yt-dlp
git clone https://github.com/averygan/reclip.git
cd reclip
./reclip.sh
```

**Installation mit Docker**

```
docker build -t reclip . && docker run -p 8899:8899 reclip
```

## Ausführung

**Zugriff auf die Schnittstelle**

```
http://localhost:8899
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das Reclip-Tool verwenden, um Videolinks aus dem Internet im MP4- oder MP3-Format auf mein lokales Gerät herunterzuladen. Um den Download-Vorgang zu starten, muss ich die Links in das Eingabefeld einfügen, das Format auswählen, auf die Schaltfläche „Fetch“ klicken, um die Videoinformationen zu laden, und dann die Schaltfläche „Download“ verwenden. Während dieses Vorgangs kann ich Massen-Downloads durchführen und die Videoauflösung nach meinen Wünschen anpassen.

## Verwandte Begriffe aus dem Glossar

- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Geeignet für Benutzer, die Medieninhalte aus dem Internet auf ihrem eigenen lokalen Speicher sichern möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/averygan/reclip)
- [Auf Türkisch lesen →](https://trescout.com/discover/reclip/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-09-02 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/reclip/
