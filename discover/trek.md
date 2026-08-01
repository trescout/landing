# Kendi sunucunuzda kişisel yapay zekâ seyahat planlayıcısı

TREK, gerçek zamanlı iş birliği, etkileşimli haritalar ve bütçe yönetimi gibi özellikler sunan, kendi kendine barındırılan (self-hosted) bir seyahat planlama uygulamasıdır. Aşamalı web uygulaması (PWA) desteği ve tek oturum açma (SSO) entegrasyonu ile kullanıcıların seyahat süreçlerini dijital ortamda organize etmelerine olanak tanır.

- ★ 7.040
- TypeScript
- GitHub Trending · 2026-06-26

## Ne kazandırır?
- Sürükle bırak yöntemiyle etkileşimli seyahat planlama
- Bütçe yönetimi ve masraf paylaşımı
- Yapay zekâ destekli otomatik rota ve liste oluşturma

## Kurulum

**Docker ile hızlı kurulum**

```
ENCRYPTION_KEY=$(openssl rand -hex 32) docker run -d -p 3000:3000 \
-e ENCRYPTION_KEY=$ENCRYPTION_KEY \
-v ./data:/app/data -v ./uploads:/app/uploads mauriceboe/trek
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sen benim kişisel seyahat asistanımsın. TREK uygulamam üzerinden bir sonraki seyahatim için 3 günlük bir plan oluşturmanı, bütçemi optimize etmeni ve ihtiyaç listemi hazırlamanı istiyorum. Lütfen gidilecek yerlerin konumlarını, tahmini harcamaları ve günlük aktiviteleri içeren kapsamlı bir program hazırla.

- **Kimin için:** Seyahatlerini dijital ortamda organize etmek, masraflarını takip etmek ve kendi sunucusunda veri gizliliğine önem vererek yapay zekâ desteği almak isteyen gezginler içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/mauriceboe/TREK)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-26 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
PWA SSO Self-hosted Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/trek/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
