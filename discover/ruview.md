# WiFi Sinyalleriyle Mekansal Zeka Kazanın

RuView , sıradan WiFi sinyallerini kullanarak kamera olmadan gerçek zamanlı mekânsal zekâ, hayati bulgu takibi ve varlık algılama işlemleri gerçekleştirir. Rust ile geliştirilmiş açık kaynak bir projedir.

_Görsel: RuView (proje deposundan)_

- ★ 88.185
- Rust
- MIT
- GitHub Trending · 30 May 2026

## Güncelleme
- 2 Ağustos 2026: Yıldız 68.643 → 88.185, son sürüm v2143 (2 Ağustos 2026).

- **Kimin için:** IoT/algılama/araştırma ile ilgilenenler 
- **Zorluk:** İleri · teknik/donanım 
- **Ne sunar:** WiFi tabanlı algılama ve mekânsal zekâ 
- **Ücret:** Ücretsiz · açık kaynak (MIT) 
- **Lisans:** MIT · ayrıntı aşağıda 

## Ne sunar?
- Kamera kullanmadan varlık ve hareket algılama.
- Hayati bulguların (nefes ve nabız) takibi.
- Gerçek zamanlı mekânsal zekâ.

## Sorumluluk notu
İnsanların varlığını/hareketini algılayan bir teknolojidir. Gizlilik ve rıza açısından dikkatli, yasalara uygun kullanım sizin sorumluluğunuzdadır. 

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Donanım olmadan denemek için terminalde 'docker pull ruvnet/wifi-densepose:latest' çalıştır, ardından 'docker run -p 3000:3000 ruvnet/wifi-densepose:latest' ile başlat ve tarayıcıdan http://localhost:3000 adresini aç; bu, RuView'in WiFi sinyalleriyle hareket/varlık algılama arayüzünü simülasyon veriyle gösterir.

**Docker imajını çek**

```
docker pull ruvnet/wifi-densepose:latest
```

**Docker ile çalıştır (simülasyon, donanım gerekmez)**

```
docker run -p 3000:3000 ruvnet/wifi-densepose:latest
```

**Python paketi (PyPI)**

```
pip install ruview
```

Lisans: MIT · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz. 

## Bağlantılar
- [GitHub deposu →](https://github.com/ruvnet/RuView)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
WiFi Rust Open Source Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ruview/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
