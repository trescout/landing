# Müzik üretiminde yapay zekâ ile düzenlenebilir kompozisyon

YuE, sembolik planlama ve sıfır örnekli (zero-shot) cover üretimi gibi yeteneklerle donatılmış bir müzik oluşturma sistemidir. Müzik düzenleme süreçlerini otomatize eden bu yapay zekâ modeli, karmaşık kompozisyonları agentik iş akışlarıyla yönetmenize olanak tanır.

- ★ 12.774
- Python
- GitHub Trending · 2026-09-13

## Güncelleme

- **27 Ekim 2026:** Yıldız 11.751 → 12.774, son sürüm yue2-v0.1.6 (9 Eylül 2026).
- **12 Ekim 2026:** Yıldız 10.749 → 11.751, son sürüm yue2-v0.1.6 (9 Eylül 2026).
- **3 Ekim 2026:** Yıldız 9.749 → 10.749, son sürüm yue2-v0.1.6 (9 Eylül 2026).
- **19 Eylül 2026:** Yıldız 8.744 → 9.749, son sürüm yue2-v0.1.6 (9 Eylül 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

YuE2 kullanarak bir şarkı oluşturmak istiyorum. Lütfen bana şarkı sözlerini ve istediğim müzik tarzını temel alan, düzenlenebilir bir melodi ve akor planı hazırla. Ardından bu planı kullanarak vokaller ve enstrüman eşliği içeren tam bir şarkı kaydı üret. Eğer elimde bir notasyon dosyası varsa, bu dosyayı kullanarak düzenleme yapmamı sağla.

Depo: https://github.com/multimodal-art-projection/YuE. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Müzikal kompozisyonlarını yapay zekâ yardımıyla planlamak, notalar üzerinde değişiklik yapmak ve özgün şarkılar üretmek isteyen müzisyenler ve içerik üreticileri için uygundur.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/multimodal-art-projection/YuE)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Zero-shot](https://trescout.com/dictionary/zero-shot/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/yue/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
