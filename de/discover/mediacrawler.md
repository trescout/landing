# Sammeln Sie Social-Media-Daten automatisch

MediaCrawler sammelt durch Web Scraping automatisch Beiträge und Benutzerkommentare auf beliebten chinesischen Social-Media-Plattformen. Dieses Python-basierte Tool bietet eine umfassende Daten-Crawling-Infrastruktur für Inhaltsanalyse- und Datenerfassungsprozesse.

- ★ 59.631
- Python
- GitHub Trending · 2026-06-26

## Aktualisieren
- 2. August 2026: Stern 53.062 → 59.631.

## Was es bringt
- Abrufen von Beiträgen und Kommentaren von beliebten Plattformen
- Einfache Anmeldung mit Browser-Automatisierung
- Unterstützt die Aufzeichnung in mehreren Datenformaten

## Installation
**Abhängigkeiten installieren**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Installation des Scannertreibers**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```


## Ausführung
**Starten Sie die Datenextraktion**

```
# 在 config/base_config.py 查看配置项目功能，写的有中文注释

# 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
uv run main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例，执行下面的命令查看
uv run main.py --help
```


## Wenn Sie nicht programmieren
Ich möchte mit dem MediaCrawler-Tool Daten von einer bestimmten Social-Media-Plattform abrufen. Bitte lassen Sie mich die Einstellungen in der Datei config/base_config.py überprüfen und Schritt für Schritt erklären, wie ich den Befehl uv run main.py konfigurieren sollte, um Beitrags- und Kommentarinformationen durch eine Stichwortsuche für die xhs-Plattform zu sammeln.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/mediacrawler/
