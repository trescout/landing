# Yapay zekâ ajanları için güvenli ortam

NVIDIA tarafından geliştirilen OpenShell, otonom yapay zekâ ajanları için güvenli ve gizlilik odaklı bir çalışma zamanı (runtime) ortamı sunuyor. Rust diliyle yazılan bu altyapı, ajanların sistem kaynaklarına erişimini izole ederek güvenli bir yürütme alanı oluşturmayı amaçlıyor.

- ★ 18.169
- Rust
- GitHub Trending · 2026-09-29

## Güncelleme

- **23 Ekim 2026:** Yıldız 16.850 → 18.169, son sürüm v0.1.5 (20 Ekim 2026).
- **21 Ekim 2026:** Yıldız 16.170 → 16.850, son sürüm v0.1.5 (20 Ekim 2026).
- **14 Ekim 2026:** Yıldız 15.577 → 16.170, son sürüm v0.1.4 (13 Ekim 2026).
- **9 Ekim 2026:** Yıldız 15.205 → 15.577, son sürüm v0.1.3 (9 Ekim 2026).

## Ne kazandırır?

- Yapay zekâ ajanlarını izole sandbox çevresinde çalıştırır
- Dosya ve ağ erişimini kurallarla sınırlar
- Kimlik bilgilerini gizleyerek güvenliği artırır

## Kurulum

**Aracı Kur ve Demo Ortam Oluştur**

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```

## Çalıştırma

**Yetenekleri Ekle**

```
npx skills add NVIDIA/OpenShell
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenShell aracını kurmak ve test etmek için şu komutları kullanabilirsin: curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh ve ardından openshell sandbox create --name demo komutunu çalıştırarak demo ortamı oluşturabilirsin.

Depo: https://github.com/NVIDIA/OpenShell. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ ajanlarını güvenli ve izole bir ortamda bütün sistem kaynaklarına tam yetki vermeden çalıştırmak isteyen geliştiriciler.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/NVIDIA/OpenShell)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-29 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Sandbox](https://trescout.com/dictionary/sandbox/)
- [Runtime](https://trescout.com/dictionary/runtime/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openshell/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
