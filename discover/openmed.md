# Sağlıkta Açık Kaynak yapay zekâ

OpenMed, sağlık hizmetleri alanında kullanılan açık kaynaklı yapay zekâ (artificial intelligence) modellerini ve veri setlerini bir araya getiren bir platformdur. Tıp odaklı uygulamalar için geliştirilen bu Python tabanlı kütüphane, sağlık verilerinin işlenmesi süreçlerini standartlaştırmayı amaçlar.

- ★ 2.041
- Python
- GitHub Trending · 2026-06-10

## Ne kazandırır?
- Klinik metinlerden yapılandırılmış tıbbi içgörüler çıkarır.
- Kişisel sağlık verilerini cihaz üzerinde anonimleştirir.
- 1.000'den fazla tıbbi yapay zeka modelini çevrimdışı çalıştırır.

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

## İlgili sözlük terimleri
Apple Silicon Open Source Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openmed/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
