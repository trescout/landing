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
Ich möchte das LongCat-Video-Projekt auf meinem System installieren. Bitte leiten Sie mich Schritt für Schritt an, den Quellcode mit den Befehlen 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' und 'cd LongCat-Video' herunterzuladen und anschließend die Download-Befehle mit 'pip install "huggingface_hub[cli]"' auszuführen, um auf die erforderlichen Dateien über die Hugging Face-Modellbibliothek zuzugreifen.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/longcat-video/
