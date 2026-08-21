# Sağlıkta Açık Kaynak yapay zekâ

OpenMed, sağlık hizmetleri alanında kullanılan açık kaynaklı yapay zekâ (artificial intelligence) modellerini ve veri setlerini bir araya getiren bir platformdur. Tıp odaklı uygulamalar için geliştirilen bu Python tabanlı kütüphane, sağlık verilerinin işlenmesi süreçlerini standartlaştırmayı amaçlar.

- ★ 5.076
- Python
- GitHub Trending · 2026-06-10

## Güncelleme
- 21 Ağustos 2026: Yıldız 5.015 → 5.076, son sürüm v2.2.0 (21 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 4.793 → 5.015, son sürüm v2.1.0 (12 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 2.041 → 4.793, son sürüm v2.0.0 (28 Temmuz 2026).

## Ne kazandırır?
- Klinik metinlerden yapılandırılmış tıbbi içgörüler çıkarır.
- Kişisel sağlık verilerini cihaz üzerinde anonimleştirir.
- 1.000'den fazla tıbbi yapay zekâ modelini çevrimdışı çalıştırır.

## Kurulum

**Temel Kurulum**

```
pip install "openmed[hf]"
```

**Apple Silicon (MLX) Desteği**

```
pip install "openmed[mlx]"
```

## Çalıştırma

**Python ile Basit Analiz**

```
python -c "from openmed import extract_pii; print([(e.label, e.text) for e in extract_pii('Dr. Pedro Almeida, CPF: 123.456.789-09, email: pedro@hospital.pt', lang='pt').entities])"
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenMed kütüphanesini kullanarak tıbbi metin analizi yapmak istiyorum. Cihazımda Python yüklü. Öncelikle pip install "openmed[hf]" komutuyla kurulumu tamamladım. Şimdi elimdeki klinik notları analiz etmek ve içerisindeki tıbbi terimleri veya kişisel verileri (PII) tespit etmek için Python kodumda hangi fonksiyonları çağırmalıyım? Lütfen bana model seçimi ve çıktıları yazdırma konusunda basit bir örnek kod bloğu oluştur.

- **Kimin için:** Tıbbi verilerini bulut servislerine göndermeden, kendi donanımı üzerinde gizlilik odaklı analiz yapmak isteyen sağlık profesyonelleri ve yazılımcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/maziyarpanahi/openmed)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-10 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Apple Silicon Open Source Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openmed/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
