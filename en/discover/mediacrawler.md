# Collect social media data automatically

MediaCrawler automatically collects posts and user comments on popular Chinese social media platforms through web scraping. This Python-based tool offers a comprehensive data crawling infrastructure for content analysis and data collection processes.

- ★ 62,789
- Python
- GitHub Trending · 2026-06-26

## What you get
- Pulling posts and comments from popular platforms
- Easy login with browser automation
- Support recording in multiple data formats

## Installation
**Installing dependencies**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Scanner driver installation**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```


## Running it
**Start data extraction**

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


## If you don't write code
I want to pull data from specified social media platform using MediaCrawler tool. Please let me check the settings in the config/base_config.py file and explain step by step how I should configure the uv run main.py command to collect post and comment information by doing keyword search for the xhs platform.

## Related dictionary terms

## Links
- GitHub repository →
- Read in Turkish →

---
Source: TreScout Discover · https://trescout.com/en/discover/mediacrawler/
