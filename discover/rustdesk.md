# Açık kaynaklı uzak masaüstü kontrolü

Rust ile geliştirilen RustDesk, kendi sunucunuzda barındırabileceğiniz açık kaynaklı bir uzak masaüstü uygulamasıdır. Uzaktan erişim ve kontrol imkânı sunan bu yazılım, TeamViewer gibi ücretli servislere alternatif bir çözüm oluşturur.

- ★ 120.685
- Rust
- GitHub Trending · 2026-08-15

## Ne kazandırır?
- Kendi sunucunuzda barındırma imkânı
- Veri üzerinde tam kontrol
- Ek yapılandırma gerektirmeyen hazır çözüm

## Kurulum

**VCPKG kurulumu**

```
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
RustDesk kullanarak uzak masaüstü bağlantısı kurmak istiyorum. Veri güvenliğimi sağlamak adına kendi sunucumu nasıl yapılandırabilirim ve bağlantı sırasında dikkat etmem gereken temel güvenlik ayarları nelerdir?

- **Kimin için:** Uzaktan erişim ve kontrol ihtiyaçlarını, verilerini üçüncü taraf servisler yerine kendi sunucularında tutarak karşılamak isteyen kullanıcılar için uygundur. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/rustdesk/rustdesk)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-15 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rustdesk/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
