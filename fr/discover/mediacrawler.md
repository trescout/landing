# Collectez automatiquement les données des réseaux sociaux

MediaCrawler collecte automatiquement les publications et les commentaires des utilisateurs sur les plateformes de médias sociaux chinoises populaires grâce au web scraping. Cet outil basé sur Python offre une infrastructure complète d'exploration de données pour les processus d'analyse de contenu et de collecte de données.

- ★ 65 953
- Python
- GitHub Trending · 2026-06-26

## Mises à jour

- **29 septembre 2026:** Étoiles 62,789 → 65,953.
- **18 août 2026:** Étoiles 59,631 → 62,789.
- **2 août 2026:** Étoiles 53,062 → 59,631.

## Ce que ça vous apporte

- Extraire des publications et des commentaires de plateformes populaires
- Connexion facile avec l'automatisation du navigateur
- Prise en charge de l'enregistrement dans plusieurs formats de données

## Installation

**Installation des dépendances**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Installation du pilote du scanner**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```

## Exécution

**Démarrer l'extraction des données**

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

## Si vous ne codez pas

🤖 Collez ceci dans votre agent (Claude Code · Codex · Antigravity)

Je souhaite extraire des données d'une plate-forme de médias sociaux spécifiée à l'aide de l'outil MediaCrawler. Veuillez me permettre de vérifier les paramètres dans le fichier config/base_config.py et d'expliquer étape par étape comment configurer la commande uv run main.py pour collecter des informations sur les publications et les commentaires en effectuant une recherche par mot clé pour la plate-forme xhs.

## Termes liés du glossaire

- [Web Scraping](https://trescout.com/fr/dictionary/web-scraping/)
- [Artificial Intelligence](https://trescout.com/fr/dictionary/artificial-intelligence/)

- **Pour qui:** Il convient aux chercheurs et aux analystes de données qui souhaitent collecter des données sur les plateformes de médias sociaux.

## Liens

- [Dépôt GitHub →](https://github.com/NanmiCoder/MediaCrawler)
- [Lire en turc →](https://trescout.com/discover/mediacrawler/)

TreScout n'a pas développé cet outil · nous l'avons repéré dans les tendances GitHub et présenté. Cette page décrit le dépôt tel qu'il était le 2026-06-26 : Le nombre d'étoiles et notre texte datent de ce jour, le dépôt a pu changer depuis. Consultez le lien du dépôt pour l'état actuel. Cette page a été **traduite automatiquement** depuis l’original turc · la version turque fait foi.

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/mediacrawler/
