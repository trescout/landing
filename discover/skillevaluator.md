# Yapay zekâ ajan yeteneklerini değerlendirme aracı

NVIDIA tarafından geliştirilen SkillEvaluator, yapay zekâ ajanlarının yeteneklerini kalite kontrolü, anlamsal çakışma tespiti ve sentetik veri üretimi gibi yöntemlerle değerlendiren çok katmanlı bir çerçeve (framework). Bu araç, ajanların davranışları üzerindeki etkileri ölçmek amacıyla canlı değerlendirme süreçleri sunuyor.

- ★ 3.655
- Python
- GitHub Trending · 2026-11-16

## Güncelleme

- **18 Kasım 2026:** Yıldız 2.913 → 3.655, son sürüm v1.0.1 (18 Kasım 2026).
- **17 Kasım 2026:** Yıldız 1.912 → 2.913, son sürüm v0.9.0 (13 Kasım 2026).
- **16 Kasım 2026:** Yıldız 1.897 → 1.912, son sürüm v0.9.0 (13 Kasım 2026).

## Ne kazandırır?

- Yapay zekâ ajan yeteneklerinin kalitesini kontrol eder
- Ajan becerilerinin görev sonuçlarına etkisini ölçer
- Katmanlı çerçeve ile ayrıntılı raporlar sunar

## Kurulum

**Paketi yükleme**

```
pip install skillevaluator
```

## Çalıştırma

**Kalite kontrolü yapma**

```
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ ajanı yeteneklerini değerlendirmek istiyorum. Bu amaçla terminal üzerinden pip install skillevaluator komutunu çalıştırarak kurulumu tamamla ve ardından örnek kalite kontrol testi için uv run --python 3.13 skillevaluator quality-check \
src/skillevaluator/tier3/reference_skills/text-analyzer \
-r cli -r json -o reports/first-quality komutunu çalıştır.

Depo: https://github.com/NVIDIA/SkillEvaluator. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ ajanları geliştiren ve bu ajanların beceri performansını test etmek isteyen geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/NVIDIA/SkillEvaluator)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Framework](https://trescout.com/dictionary/framework/)
- [Terminal](https://trescout.com/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/skillevaluator/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
