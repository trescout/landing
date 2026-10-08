# Collect social media data automatically

MediaCrawler automatically collects posts and user comments on popular Chinese social media platforms through web scraping. This Python-based tool offers a comprehensive data crawling infrastructure for content analysis and data collection processes.

- ★ 65,953
- Python
- GitHub Trending · 2026-06-26

## Updates

- **September 29, 2026:** Stars 62,789 → 65,953.
- **August 18, 2026:** Stars 59,631 → 62,789.
- **August 2, 2026:** Stars 53,062 → 59,631.

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

🤖 Paste this into your AI agent (Claude Code · Codex · Antigravity)

I want to pull data from specified social media platform using MediaCrawler tool. Please let me check the settings in the config/base_config.py file and explain step by step how I should configure the uv run main.py command to collect post and comment information by doing keyword search for the xhs platform.

## Related dictionary terms

- [Web Scraping](https://trescout.com/en/dictionary/web-scraping/)
- [Artificial Intelligence](https://trescout.com/en/dictionary/artificial-intelligence/)

- **Who it is for:** It is suitable for researchers and data analysts who want to collect data from social media platforms.

## Links

- [GitHub repository →](https://github.com/NanmiCoder/MediaCrawler)
- [Read in Turkish →](https://trescout.com/discover/mediacrawler/)

TreScout did not build this tool · we found it in GitHub trends and wrote it up. This page describes the repository as of 2026-06-26: The star count and our text belong to that day, the repository may have changed since. Check the repository link for the current state. This page was **machine-translated** from the Turkish original · the Turkish version prevails.

---
Source: TreScout Discover · https://trescout.com/en/discover/mediacrawler/
