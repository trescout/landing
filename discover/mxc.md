# Rust ile politika tabanlı katmanlı sistem yalıtımı

Microsoft tarafından geliştirilen MXC, Rust diliyle yazılmış politika tabanlı, katmanlı bir yalıtım ve kapsayıcılık (isolation and containment) çözümüdür. Sistem kaynaklarını güvenli bir şekilde sınırlandırmak ve uygulama güvenliğini artırmak amacıyla tasarlanmıştır.

- ★ 2.882
- Rust
- GitHub Trending · 2026-06-07

## Güncelleme

- **17 Ekim 2026:** Yıldız 2.506 → 2.882, son sürüm v1.0.1 (17 Ekim 2026).
- **10 Ekim 2026:** Yıldız 1.398 → 2.506, son sürüm v1.0.0 (7 Ekim 2026).
- **7 Ekim 2026:** Yıldız 641 → 1.398, son sürüm v1.0.0 (7 Ekim 2026).

## Ne kazandırır?

- Güvenilmeyen kodları yalıtılmış ortamlarda güvenle çalıştırır.
- JSON tabanlı politikalarla dosya, ağ ve arayüz erişimini denetler.
- Windows, Linux ve macOS üzerinde çoklu yalıtım arka uçları sunar.

## Kurulum

**Linux üzerinde derleme**

```
./build.sh
```

**macOS üzerinde derleme**

```
./build-mac.sh
```

## Çalıştırma

**Yerel ikili dosya ile çalıştırma**

```
wxc-exec.exe config.json
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Microsoft tarafından geliştirilen MXC aracını kullanarak güvenilmeyen bir kod parçacığını yalıtılmış bir kapsayıcıda çalıştırmak istiyorum. Projenin GitHub deposundaki dokümantasyona göre, JSON tabanlı bir yapılandırma dosyası hazırlamam ve platformuma uygun ikili dosyayı kullanmam gerekiyor. Bana, bir Python betiğini kısıtlı dosya sistemi ve ağ erişimiyle çalıştırmamı sağlayacak örnek bir JSON yapılandırma dosyası oluşturur musun ve bu yapılandırmayı wxc-exec.exe ile nasıl çalıştıracağımı adım adım açıklar mısın?

Depo: https://github.com/microsoft/mxc. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Güvenilmeyen kodları, eklentileri veya araçları sistem kaynaklarını koruyarak izole bir ortamda çalıştırmak isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/microsoft/mxc)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-07 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/mxc/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
