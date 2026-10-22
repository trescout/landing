# Claude Code için yapay zekâ destekli kod inceleme

OpenAI tarafından geliştirilen Codex eklentisi, Claude Code üzerinde kod inceleme süreçlerini otomatize etmek ve görev delegasyonu sağlamak için kullanılıyor. Bu araç, yazılım geliştirme iş akışlarında farklı yapay zekâ modellerinin (large language models) entegre çalışmasına olanak tanıyor.

- ★ 34.241
- JavaScript
- GitHub Trending · 2026-07-03

## Güncelleme

- **15 Ekim 2026:** Yıldız 32.597 → 34.241, son sürüm v1.0.6 (8 Temmuz 2026).
- **31 Ağustos 2026:** Yıldız 30.950 → 32.597, son sürüm v1.0.6 (8 Temmuz 2026).
- **2 Ağustos 2026:** Yıldız 22.800 → 30.950, son sürüm v1.0.6 (8 Temmuz 2026).

## Ne kazandırır?

- Kod inceleme süreçlerini otomatize eder
- Görevleri Codex modeline delege eder
- Arka planda uzun süreli işleri yönetir

## Kurulum

**Codex paketini yükleyin**

```
npm install -g @openai/codex
```

## Çalıştırma

**İlk incelemeyi başlatın**

```
/codex:review
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Claude Code içerisinde Codex eklentisini kullanarak mevcut kodum üzerinde bir inceleme başlat ve bulguları raporla. Eğer karmaşık bir görev varsa, bunu /codex:rescue komutu ile Codex'e devret ve arka planda çalıştırarak ilerlemeyi /codex:status ile takip etmemi sağla.

Depo: https://github.com/openai/codex-plugin-cc. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Claude Code iş akışına Codex'in kod inceleme ve görev yönetimi yeteneklerini entegre etmek isteyen yazılım geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/openai/codex-plugin-cc)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Large Language Models](https://trescout.com/dictionary/large-language-models/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/codex-plugin-cc/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
