# Belgeleri yapay zekâya hazırlayan OCR aracı

PaddlePaddle tarafından geliştirilen PaddleOCR, PDF ve görsel belgeleri büyük dil modelleri (large language models) için yapılandırılmış veriye dönüştüren hafif bir optik karakter tanıma (optical character recognition) aracıdır. 100'den fazla dili destekleyen bu kütüphane, görsel içerikler ile yapay zekâ modelleri arasındaki veri akışını standartlaştırmaktadır.

- ★ 86.787
- GitHub Trending · 2026-06-05

TreScout notu: Taranmış belgedeki ve görseldeki yazıyı düzenlenebilir metne çevirir, tabloları da tanır. Ücretsiz seçenekler arasında en yetkinlerinden, ama kurulumun ağır tarafı altındaki hesaplama kütüphanesidir · ayrı bir çalışma alanında kurun, ekran kartı olmadan da çalışır ama yavaşlar. Türkçe belgelerde iş görür, yine de kendi örneklerinizle deneyin: Sonuç belgenin tarama kalitesine çok bağlı.

## Güncelleme
- 2 Ağustos 2026: Yıldız 80.160 → 86.787, son sürüm v3.7.0 (11 Haziran 2026).

## Ne kazandırır?
- PDF ve görselleri JSON veya Markdown formatına dönüştürür
- 100'den fazla dili tek modelle tanır
- Düşük kaynak kullanımıyla yüksek doğruluk sağlar

## Kurulum

**Python (pip)**

```
pip install paddleocr
```

Kaynak: Resmî kaynak: https://github.com/PaddlePaddle/PaddleOCR

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Elimdeki PDF ve görsel belgeleri, yapay zekâ modellerinin işleyebileceği yapılandırılmış verilere dönüştürmek istiyorum. PaddleOCR'ın sunduğu PP-OCRv6 veya HPD-Parsing gibi modelleri kullanarak, belgelerimdeki metinleri, tabloları ve formülleri en yüksek doğrulukla nasıl Markdown veya JSON formatına çevirebilirim? Bu süreçte yüksek verimlilik ve hız için hangi yapılandırma ayarlarını tercih etmeliyim?

- **Kimin için:** Belgelerini yapay zekâ uygulamalarında kullanmak isteyen geliştiriciler ve veri analistleri için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/PaddlePaddle/PaddleOCR)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Optical Character Recognition Markdown Large Language Models PDF Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/paddleocr/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
