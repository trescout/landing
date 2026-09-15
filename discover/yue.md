# Müzik üretiminde yapay zekâ ile düzenlenebilir kompozisyon

YuE, sembolik planlama ve sıfır örnekli (zero-shot) cover üretimi gibi yeteneklerle donatılmış bir müzik oluşturma sistemidir. Müzik düzenleme süreçlerini otomatize eden bu yapay zekâ modeli, karmaşık kompozisyonları agentik iş akışlarıyla yönetmenize olanak tanır.

- ★ 8.744
- Python
- GitHub Trending · 2026-09-13

## Güncelleme
- 15 Eylül 2026: Yıldız 7.463 → 8.744, son sürüm yue2-v0.1.6 (9 Eylül 2026).
- 13 Eylül 2026: Yıldız 7.459 → 7.463, son sürüm yue2-v0.1.6 (9 Eylül 2026).

## Ne kazandırır?
- Söz ve stil girdisiyle melodi ve akor planı oluşturma
- Müzik notalarını ses dosyasına dönüştürmeden önce düzenleyebilme
- Mevcut şarkıları farklı tarzlarda yeniden yorumlama ve düzenleme

## Kurulum

**Projeyi indirme ve kurulum**

```
git clone https://github.com/multimodal-art-projection/YuE.git
cd YuE
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install .
python examples/generate.py --output outputs/first-song
```

## Çalıştırma

**Düzenlenmiş notalarla şarkı oluşturma**

```
python examples/generate.py --request examples/song.json \
--abc-file edited.abc --cot full --output outputs/edited
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
YuE2 kullanarak bir şarkı oluşturmak istiyorum. Lütfen bana şarkı sözlerini ve istediğim müzik tarzını temel alan, düzenlenebilir bir melodi ve akor planı hazırla. Ardından bu planı kullanarak vokaller ve enstrüman eşliği içeren tam bir şarkı kaydı üret. Eğer elimde bir notasyon dosyası varsa, bu dosyayı kullanarak düzenleme yapmamı sağla.

- **Kimin için:** Müzikal kompozisyonlarını yapay zekâ yardımıyla planlamak, notalar üzerinde değişiklik yapmak ve özgün şarkılar üretmek isteyen müzisyenler ve içerik üreticileri için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/multimodal-art-projection/YuE)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Zero-shot Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/yue/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
