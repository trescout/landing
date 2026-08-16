# Açık kaynaklı istihbarat toplama aracı

SpiderFoot, tehdit istihbaratı ve saldırı yüzeyi haritalama süreçleri için açık kaynaklı istihbarat (OSINT) toplama işlemlerini otomatize eden bir Python aracıdır. Çeşitli veri kaynaklarını entegre ederek dijital varlıklar üzerindeki güvenlik açıklarını tespit etmeyi sağlar.

- ★ 21.076
- Python
- GitHub Trending · 2026-06-22

## Güncelleme
- 15 Ağustos 2026: Yıldız 20.026 → 21.076, son sürüm v4.0 (7 Nisan 2022).
- 2 Ağustos 2026: Yıldız 18.921 → 20.026, son sürüm v4.0 (7 Nisan 2022).

## Ne kazandırır?
- 200'den fazla modül ile otomatik veri toplama
- Web tabanlı arayüz veya komut satırı desteği
- Dijital varlıklar için kapsamlı saldırı yüzeyi haritalama

## Kurulum

**Kararlı sürüm kurulumu**

```
wget https://github.com/smicallef/spiderfoot/archive/v4.0.tar.gz
tar zxvf v4.0.tar.gz
cd spiderfoot-4.0
pip3 install -r requirements.txt
python3 ./sf.py -l 127.0.0.1:5001
```

**Geliştirme sürümü kurulumu**

```
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot
pip3 install -r requirements.txt
python3 ./sf.py -l 127.0.0.1:5001
```

## Çalıştırma

**Arayüzü başlatma**

```
python3 ./sf.py -l 127.0.0.1:5001
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
SpiderFoot aracını kullanarak bir hedef üzerinde OSINT taraması başlatmak istiyorum. Hedefim bir alan adı/IP adresi. Bu aracı kullanarak dijital varlıklarımın internet üzerinde ne kadar görünür olduğunu ve hangi güvenlik açıklarına sahip olabileceğini analiz etmek için hangi adımları izlemeliyim? Lütfen 200'den fazla modülün nasıl çalıştığını ve sonuçları nasıl yorumlamam gerektiğini açıkla.

- **Kimin için:** Siber güvenlik uzmanları, sızma testi yapanlar ve kurumlarının internet üzerindeki ayak izini merak eden savunma odaklı kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/smicallef/spiderfoot)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
OSINT Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/spiderfoot/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
