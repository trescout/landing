# Kendi sunucunuzda yapay zekâ destekli seyahat planlayıcı

TREK, gerçek zamanlı iş birliği, etkileşimli haritalar ve bütçe yönetimi gibi özellikler sunan, kendi kendine barındırılan (self-hosted) bir seyahat planlama uygulamasıdır. Aşamalı web uygulaması (PWA) desteği ve tek oturum açma (SSO) entegrasyonu ile kullanıcıların seyahat süreçlerini dijital ortamda organize etmelerine olanak tanır.

- ★ 7.040
- GitHub Trending · 2026-06-26

## Ne kazandırır?
- Sürükle bırak yöntemiyle günlük seyahat rotaları ve planları oluşturma
- Grup harcamalarını takip etme ve kişi başı bölüştürme
- Yapay zekâ entegrasyonu ile otomatik seyahat ve bütçe yönetimi

## Kurulum

**Docker ile hızlı kurulum**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
-e ENCRYPTION_KEY=$ENCRYPTION_KEY \
-v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sen bir seyahat asistanısın. TREK üzerindeki MCP (Model Context Protocol) araçlarını kullanarak benim için 3 günlük bir Paris seyahat planı hazırla, bütçemi günlük harcama limitlerine göre ayarla ve yanıma almam gerekenler için bir paketleme listesi oluştur.

- **Kimin için:** Seyahatlerini dijital ortamda organize etmek, harcamalarını takip etmek ve kendi verisi üzerinde tam kontrol sahibi olmak isteyen gezginler içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/mauriceboe/TREK)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-26 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
PWA SSO Self-hosted Model Context Protocol Model Context Protocol MCP

---
Kaynak: TreScout Keşif · https://trescout.com/discover/trek/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
