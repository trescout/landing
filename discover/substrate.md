# Yapay zekâ ajanları için ölçeklenebilir altyapı

Agent Substrate, yapay zekâ ajanları için ölçeklenebilir altyapı sağlayan temel sistemdir.

- ★ 5.748
- Go
- GitHub Trending · 2026-08-20

## Güncelleme

- **23 Ekim 2026:** Yıldız 5.191 → 5.748, son sürüm v0.6.0 (22 Ekim 2026).
- **15 Ekim 2026:** Yıldız 4.569 → 5.191, son sürüm v0.5.0 (14 Ekim 2026).
- **8 Ekim 2026:** Yıldız 4.033 → 4.569, son sürüm v0.4.0 (8 Ekim 2026).
- **1 Ekim 2026:** Yıldız 3.839 → 4.033, son sürüm v0.3.0 (30 Eylül 2026).

## Ne kazandırır?

- Ajanları düşük gecikmeyle saniyeler içinde başlatır
- Bellek ve dosya sistemi durumunu koruyarak süreklilik sağlar
- Sınırlı kaynakla çok sayıda ajanı aynı anda çalıştırır

## Çalıştırma

**Örnek sayaca istek gönderme**

```
curl -X POST -H "Host: my-counter-1.demo.actors.resources.substrate.ate.dev" -i http://localhost:8000/
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ ajanlarını ölçekli bir şekilde çalıştırmak için Substrate altyapısını kullanıyorum. Kubernetes (konteyner yönetim sistemi) üzerinde çalışan bu sistemde, aktörlerin yaşam döngüsünü yönetmek, kaynakları verimli kullanmak ve yüksek yoğunluklu ajan dağıtımları gerçekleştirmek istiyorum. Substrate'in sunduğu performanslı çalışma ortamını kullanarak ajanlarımın durumunu korumak ve hızlı bir şekilde aktif hale getirmek için gerekli yapılandırmayı nasıl optimize edebilirim?

Depo: https://github.com/agent-substrate/substrate. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Büyük ölçekli yapay zekâ ajanlarını Kubernetes üzerinde yönetmek ve çalıştırmak isteyen geliştiriciler için uygundur.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/agent-substrate/substrate)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Agent](https://trescout.com/dictionary/agent/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/substrate/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
