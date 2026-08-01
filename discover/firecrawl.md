# Web verilerini yapay zekâya hazırlayın

Firecrawl, web sitelerindeki verileri büyük ölçekte taramak, ayıklamak ve yapay zekâ modellerinin işleyebileceği temiz metin formatına dönüştürmek için bir arayüz (API) sunuyor. Bu araç, web içeriğiyle etkileşimi otomatize ederek veri toplama süreçlerini kolaylaştırıyor.

- ★ 137.683
- TypeScript
- GitHub Trending · 2026-06-23

## Ne kazandırır?
- Web sitelerini temiz metin formatına dönüştürür
- Yapay zekâ ajanları için veri toplar
- Karmaşık web sayfalarıyla etkileşime girer

## Kurulum

**Ajan kurulumu**

```
npx -y firecrawl-cli@latest init --all --browser
```

## Çalıştırma

**Web sitesini tarama**

```
curl -X POST 'https://api.firecrawl.dev/v2/scrape' \
-H 'Authorization: Bearer fc-YOUR_API_KEY' \
-H 'Content-Type: application/json' \
-d '{
"url": "firecrawl.dev"
}'
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Firecrawl kullanarak belirttiğim web sitesindeki verileri tara ve yapay zekâ modellerinin kolayca işleyebileceği temiz bir Markdown formatına dönüştür. Sayfa içeriğini çekerken karmaşık yapıları temizle ve yalnızca anlamlı metinleri, yapılandırılmış verileri veya gerekli görsel bilgilerini ayıkla.

- **Kimin için:** Web sitelerinden veri toplayıp bu verileri yapay zekâ uygulamalarında kullanmak isteyen geliştiriciler ve veri analistleri içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/firecrawl/firecrawl)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-23 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Markdown API Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/firecrawl/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
