# Sağlıkta açık kaynak yapay zekâ

OpenMed, sağlık hizmetleri alanında kullanılan açık kaynaklı yapay zekâ (artificial intelligence) modellerini ve veri setlerini bir araya getiren bir platformdur. Tıp odaklı uygulamalar için geliştirilen bu Python tabanlı kütüphane, sağlık verilerinin işlenmesi süreçlerini standartlaştırmayı amaçlar.

- ★ 5.715
- Python
- GitHub Trending · 2026-06-10

## Güncelleme

- **27 Ekim 2026:** Yıldız 5.457 → 5.715, son sürüm v3.1.0 (26 Ekim 2026).
- **8 Ekim 2026:** Yıldız 5.329 → 5.457, son sürüm v3.0.0 (7 Ekim 2026).
- **16 Eylül 2026:** Yıldız 5.217 → 5.329, son sürüm v2.5.0 (15 Eylül 2026).
- **5 Eylül 2026:** Yıldız 5.076 → 5.217, son sürüm v2.3.0 (4 Eylül 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenMed kütüphanesini kullanarak tıbbi metin analizi yapmak istiyorum. Cihazımda Python yüklü. Öncelikle pip install "openmed[hf]" komutuyla kurulumu tamamladım. Şimdi elimdeki klinik notları analiz etmek ve içerisindeki tıbbi terimleri veya kişisel verileri (PII) tespit etmek için Python kodumda hangi fonksiyonları çağırmalıyım? Lütfen bana model seçimi ve çıktıları yazdırma konusunda basit bir örnek kod bloğu oluştur.

Depo: https://github.com/maziyarpanahi/openmed. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Tıbbi verilerini bulut servislerine göndermeden, kendi donanımı üzerinde gizlilik odaklı analiz yapmak isteyen sağlık profesyonelleri ve yazılımcılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/maziyarpanahi/openmed)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-10 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Apple Silicon](https://trescout.com/dictionary/apple-silicon/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openmed/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
