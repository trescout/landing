# zaman serileri için yapay zekâ tahminleme

Google Research tarafından geliştirilen Zaman Serisi Temel Modeli (Time Series Foundation Model), zaman serisi tahminleme işlemleri için önceden eğitilmiş bir yapı sunuyor. Model, farklı veri setleri üzerinde genel tahminleme yetenekleri sağlamak amacıyla tasarlanmıştır.

- ★ 22.167
- Python
- GitHub Trending · 2026-06-18

## Ne kazandırır?
- Önceden eğitilmiş temel model ile hızlı tahminleme
- 16k bağlam uzunluğu desteği
- Esnek yapı ile farklı veri setlerine uyum

## Kurulum

**PyPI üzerinden kurulum**

```
pip install timesfm[torch]
# Or with Flax
pip install timesfm[flax]
# And when XReg is needed
pip install timesfm[xreg]
```

**Yerel kurulum**

```
git clone https://github.com/google-research/timesfm.git
cd timesfm
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
TimesFM kütüphanesini kullanarak zaman serisi tahminleme yapmak istiyorum. Google tarafından geliştirilen bu temel modelin 2.5 sürümü ile 200M parametreli yapıyı nasıl yapılandırabilirim? Özellikle modelin derlenmesi (compile) aşamasında max_context ve max_horizon değerlerini nasıl belirlemeliyim ve tahminleme (forecast) fonksiyonuna veri girişlerini hangi formatta sağlamalıyım? Örnek bir kod yapısı ile açıklayabilir misin?

- **Kimin için:** Zaman serisi verileri üzerinde tahminleme yapmak isteyen veri bilimciler ve araştırmacılar için tasarlanmıştır. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/google-research/timesfm)

## İlgili sözlük terimleri
Time Series Foundation Model Foundation Model Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/timesfm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
