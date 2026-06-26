# Sosyal medya verilerini otomatik toplayın

MediaCrawler, popüler Çin sosyal medya platformlarındaki gönderileri ve kullanıcı yorumlarını otomatik olarak veri madenciliği (web scraping) yöntemiyle topluyor. Python tabanlı bu araç, içerik analizi ve veri toplama süreçleri için geniş kapsamlı bir veri çekme (crawling) altyapısı sunuyor.

- ★ 53.062
- Python
- GitHub Trending · 2026-06-26

## Ne kazandırır?
- Popüler platformlardan gönderi ve yorum çekme
- Tarayıcı otomasyonu ile kolay giriş
- Çoklu veri formatında kayıt desteği

## Kurulum

**Bağımlılıkları yükleme**

```
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

**Tarayıcı sürücüsü kurulumu**

```
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```

## Çalıştırma

**Veri çekmeyi başlatma**

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

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
MediaCrawler aracını kullanarak belirtilen sosyal medya platformundan veri çekmek istiyorum. Lütfen config/base_config.py dosyasındaki ayarları kontrol etmemi sağla ve xhs platformu için anahtar kelime araması yaparak gönderi ve yorum bilgilerini toplamam için gerekli olan uv run main.py komutunu nasıl yapılandırmam gerektiğini adım adım açıkla.

- **Kimin için:** Sosyal medya platformlarından veri toplamak isteyen araştırmacılar ve veri analistleri için uygundur. 

## Bağlantılar
- [GitHub deposu →](https://github.com/NanmiCoder/MediaCrawler)

## İlgili sözlük terimleri
Web Scraping Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/mediacrawler/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
