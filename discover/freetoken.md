# Kişisel bilgisayarda büyük yapay zekâ modelleri

FlashML-org/FreeToken, veri merkezi ölçeğindeki büyük yapay zekâ modellerini kişisel bilgisayarlarda hızlı ve verimli bir şekilde çalıştırmayı sağlayan bir kütüphanedir. Kullanıcıların 290 milyar parametre üzerindeki uzman karışımı (Mixture of Experts, MoE) modellerini standart donanımlar üzerinde etkileşimli hızlarda kullanmasına olanak tanır.

- ★ 16.863
- Python
- GitHub Trending · 2026-11-02

## Güncelleme

- **9 Kasım 2026:** Yıldız 16.721 → 16.863, son sürüm v0.2.2 (9 Kasım 2026).
- **6 Kasım 2026:** Yıldız 15.664 → 16.721, son sürüm v0.2.1 (26 Ekim 2026).
- **2 Kasım 2026:** Yıldız 15.543 → 15.664, son sürüm v0.2.1 (26 Ekim 2026).

## Ne kazandırır?

- Kullanılan donanım kaynaklarını tek bir yapay zekâ altyapısı gibi birleştirir.
- Ekran kartı belleği VRAM ve ana bellek arasında dinamik kaynak yönetimi sunar.
- Büyük uzman karışımı mimarisi MoE modellerini yerel cihazlarda etkileşimli hızlarda çalıştırır.

## Kurulum

**Paket yöneticisi uv ile kurulum**

```
uv pip install "freetoken[accel]"
```

**Kaynak koddan derleyerek kurulum**

```
git clone https://github.com/FlashML-org/FreeToken.git && cd FreeToken
uv venv && source .venv/bin/activate
uv pip install -e ".[accel]"
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Büyük yapay zekâ modellerini yerel bilgisayarda çalıştırmayı sağlayan FreeToken kütüphanesini kurmanız gerekmektedir. Hızlı paket yöneticisi uv ile kurulum yapmak için uv pip install "freetoken[accel]" komutunu kullanabilirsiniz. Doğrudan kaynak koddan derlemek isterseniz git clone https://github.com/FlashML-org/FreeToken.git && cd FreeToken
uv venv && source .venv/bin/activate
uv pip install -e ".[accel]" komut dizisini çalıştırabilirsiniz.

Depo: https://github.com/FlashML-org/FreeToken. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kendi donanımında büyük ölçekli yapay zekâ modellerini yüksek performansla yerel olarak çalıştırmak isteyen kullanıcılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/FlashML-org/FreeToken)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-02 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Mixture of Experts](https://trescout.com/dictionary/mixture-of-experts/)
- [Mixture of Experts - MoE](https://trescout.com/dictionary/mixture-of-experts-moe/)
- [VRAM](https://trescout.com/dictionary/vram/)
- [Clone](https://trescout.com/dictionary/clone/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/freetoken/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
