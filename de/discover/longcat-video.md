# Lange Videos konsistent erstellen

LongCat-Video, entwickelt von Meituan, ist ein Video-Generierungs-Framework zur konsistenten Erstellung langer Videos. Dieses Tool ermöglicht die Produktion von längeren und qualitativ hochwertigen Videoinhalten unter Beibehaltung der Bildkonsistenz.

- ★ 8.892
- Python
- GitHub Trending · 2026-10-04

## Was es bringt

- Sie können neue, langformatige Inhalte aus Texten, Bildern oder bestehenden Videos erstellen.
- Sie können Videos von mehreren Minuten Länge ohne Farbverschiebung und Qualitätsverlust ausgeben.
- Sie können Audiodateien verwenden, um mit dem Ton harmonierende Charakteranimationen zu erstellen.

## Installation

**Herunterladen des Code-Repositorys auf den Computer**

```
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

**Herunterladen der Modellgewichte**

```
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5
```

## Wenn Sie nicht programmieren

🤖 Fügen Sie dies in Ihren Agenten ein (Claude Code · Codex · Antigravity)

Ich möchte das LongCat-Video-Projekt auf meinem System installieren. Bitte leiten Sie mich Schritt für Schritt an, den Quellcode mit den Befehlen 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' und 'cd LongCat-Video' herunterzuladen und anschließend die Download-Befehle mit 'pip install "huggingface_hub[cli]"' auszuführen, um auf die erforderlichen Dateien über die Hugging Face-Modellbibliothek zuzugreifen.

## Verwandte Begriffe aus dem Glossar

- [Clone](https://trescout.com/de/dictionary/clone/)
- [Framework](https://trescout.com/de/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/de/dictionary/artificial-intelligence/)

- **Für wen es gedacht ist:** Es richtet sich an Entwickler und Content-Ersteller, die mithilfe von künstlicher Intelligenz hochwertige und langformatige Videos aus Text-, Bild- oder Audioeingaben erstellen möchten.
- **Lizenz:** MIT

## Links

- [GitHub-Repository →](https://github.com/meituan-longcat/LongCat-Video)
- [Auf Türkisch lesen →](https://trescout.com/discover/longcat-video/)

TreScout hat dieses Werkzeug nicht entwickelt · wir haben es in den GitHub-Trends gefunden und stellen es vor. Diese Seite beschreibt das Repository so, wie es am 2026-10-04 war: Die Anzahl der Sterne und unser Text stammen von diesem Tag, das Repository kann sich seitdem geändert haben. Den aktuellen Stand finden Sie über den Link zum Repository. Diese Seite wurde **maschinell übersetzt** aus dem türkischen Original · maßgeblich ist die türkische Fassung.

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/longcat-video/
