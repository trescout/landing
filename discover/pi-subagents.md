# Yapay zekâ ile asenkron görev yönetimi

**pi-subagents**, Pi platformu üzerinde **asenkron alt-ajan delegasyonu** süreçlerini yönetmek için geliştirilmiş bir TypeScript kütüphanesidir. Karmaşık iş yüklerini alt-ajanlara dağıtmayı kolaylaştırır.

- ★ 3.966
- TypeScript
- Lisans: yok
- GitHub Trending · 1 Haziran 2026

## Güncelleme

- **20 Ekim 2026:** Yıldız 3.948 → 3.966, son sürüm v0.79.2 (20 Ekim 2026).
- **18 Ekim 2026:** Yıldız 3.942 → 3.948, son sürüm v0.79.1 (18 Ekim 2026).
- **17 Ekim 2026:** Yıldız 3.919 → 3.942, son sürüm v0.79.0 (17 Ekim 2026).
- **13 Ekim 2026:** Yıldız 3.893 → 3.919, son sürüm v0.78.0 (13 Ekim 2026).

- **Kimin için:** Pi platformunda ajan geliştirenler
- **Zorluk:** İleri · geliştirici kütüphanesi
- **Ne sunar:** Asenkron alt-ajan delegasyonu
- **Ücret:** Açık kaynak (lisans notuna bakın)
- **Lisans:** Belirtilmemiş · ayrıntı aşağıda

## Ne kazandırır?

- İş yükünü alt ajanlara dağıtır.
- Asenkron ve paralel yürütme sağlar.
- Pi platformu ile tam entegre çalışır.

## Nasıl kurulur, nasıl kullanılır?

Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

'pi install npm:pi-subagents' komutuyla bu paketi kur, sonra '/run reviewer' ile bir kod incelemesi yaptır ya da '/parallel' ile birden çok uzman alt-ajanı (örn. inceleyici, planlayıcı) aynı anda çalıştırarak işi onlara dağıt.

Depo: https://github.com/nicobailon/pi-subagents. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

**Pi ile kur**

```
pi install npm:pi-subagents
```

**Bir alt-ajanı çalıştır**

```
/run <ajan> [görev]
```

**Ajanları paralel çalıştır**

```
/parallel ajan1 "görev1" -> ajan2 "görev2"
```

**Lisans:** ⚠️ Repo'da bir lisans belirtilmemiş; varsayılan olarak 'tüm hakları saklı'. Denemek için bakabilirsiniz, ancak yeniden kullanım için yazarın açık izni gerekir.

## Bağlantılar

- [GitHub deposu →](https://github.com/nicobailon/pi-subagents)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pi-subagents/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
