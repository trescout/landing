# Düşük bellekte yapay zekâ eğitimi

Soup, büyük dil modellerine (large language models) tek bir YAML dosyası üzerinden ince ayar (fine-tuning) yapılmasına olanak tanıyan bir Python kütüphanesi. Katman akış (layer streaming) yöntemiyle 8 milyar parametreli modelleri 4 GB belleğe sahip dizüstü bilgisayar grafik işlemcilerinde eğitebiliyor.

- ★ 2.222
- Python
- GitHub Trending · 2026-08-16

## Güncelleme
- 18 Ağustos 2026: Yıldız 1.739 → 2.222, son sürüm v0.73.3 (18 Ağustos 2026).
- 16 Ağustos 2026: Yıldız 1.729 → 1.739, son sürüm v0.73.2 (15 Ağustos 2026).

## Ne kazandırır?
- 4 GB grafik belleğine sahip dizüstü bilgisayarlarda 8 milyar parametreli modelleri eğitebilirsiniz.
- Katman akış yöntemiyle donanım kısıtlamalarını aşarak karmaşık kurulumlarla uğraşmazsınız.
- Tek bir yapılandırma dosyası üzerinden tüm eğitim sürecini yönetebilirsiniz.

## Kurulum

**Temel kurulum**

```
pip install "soup-cli[train]"
```

**Tüm özelliklerle kurulum**

```
pip install "soup-cli[all]"
```

## Çalıştırma

**Eğitimi başlatma**

```
soup init --template chat
soup train
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Soup kütüphanesini kullanarak 8 milyar parametreli bir yapay zekâ modelini 4 GB grafik belleğine sahip bilgisayarımda eğitmek istiyorum. Katman akış özelliğini aktif eden ve 4-bit nicemleme kullanan bir YAML yapılandırma dosyası oluşturmama yardımcı ol. Eğitim sürecini başlatmak için gerekli olan soup.yaml dosyasının içeriğini hazırla ve ardından bu dosyayı kullanarak eğitimi nasıl başlatacağımı adım adım açıkla.

- **Kimin için:** Yüksek donanım maliyetleri olmadan kendi yerel bilgisayarında büyük dil modellerine ince ayar yapmak isteyen geliştiriciler içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/MakazhanAlpamys/Soup)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Layer Streaming Fine-tuning Large Language Models Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/soup/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
