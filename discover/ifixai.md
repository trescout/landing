# Yapay zekâ ajanlarini denetleyin

iFixAi, yapay zekâ ajanlarının kendilerine verilen görevleri doğru şekilde yerine getirip getirmediğini denetleyen bağımsız bir denetim aracıdır. Python diliyle geliştirilen bu sistem, insan veya ajanın kendisi tarafından çalıştırılarak süreçlerin doğruluğunu iki dakikadan kısa sürede analiz eder.

- ★ 35.263
- Python
- GitHub Trending · 2026-10-15

## Güncelleme

- **27 Ekim 2026:** Yıldız 33.443 → 35.263, son sürüm v4.3.0 (22 Ekim 2026).
- **23 Ekim 2026:** Yıldız 32.525 → 33.443, son sürüm v4.3.0 (22 Ekim 2026).
- **22 Ekim 2026:** Yıldız 30.965 → 32.525, son sürüm v4.2.1 (21 Ekim 2026).
- **21 Ekim 2026:** Yıldız 29.783 → 30.965, son sürüm v4.2.1 (21 Ekim 2026).

## Ne kazandırır?

- Yapay zekâ ajanlarinizin görevlerini dogru yapip yapmadigini test eder.
- Iki dakikadan kisa sürede ayrintili analiz raporu sunar.
- Sistem açiklarini ve gözden kaçan hatalari önceden yakalar.

## Kurulum

**Paketi yükleyin**

```
pip install "ifixai[openai]"   # or anthropic, gemini, etc.: install the provider extra you'll test
```

**Kurulum sihirbazini açin**

```
ifixai setup                    # arrow-key wizard: pick provider, model, judge, suite → writes ifixai.yaml
```

## Çalıştırma

**Araci çalistirin**

```
ifixai run                      # no flags needed; reports land in ./ifixai-results/
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ ajanimin dogru çalisip çalisgini ve hedeflere ulasip ulasmadigini denetlemek istiyorum. Bu amaçla iFixAi adli araci kullanarak gerekli testleri yap ve sonuçlari raporla.

Depo: https://github.com/ifixai-ai/iFixAi. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ ajanlari gelistiren ve süreçlerin dogrulugunu denetlemek isteyen yazilim gelistiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/ifixai-ai/iFixAi)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-15 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ifixai/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
