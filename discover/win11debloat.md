# Windows Sistemini Gereksizlerden Arındırın

Win11Debloat, Windows 10 ve 11 işletim sistemlerinde önceden yüklenmiş uygulamaları kaldırmayı ve telemetri verilerini devre dışı bırakmayı sağlayan bir PowerShell betiğidir. Kullanıcıların sistemlerini özelleştirmelerine ve gereksiz bileşenlerden arındırarak sistem hafifletme (debloat) işlemi yapmalarına olanak tanır.

- ★ 54.506
- GitHub Trending · 2026-06-16

TreScout notu: Windows'la birlikte gelen istemediğiniz uygulamaları kaldırır, arka planda veri toplayan ayarları kapatır. Çalıştırmadan önce ne yaptığını okuyun: Kaldırılan bazı parçaları geri getirmek kolay değildir. Kişisel bilgisayarda pratik, şirket cihazında ya da başkasıyla paylaştığınız bilgisayarda kullanmayın.

## Güncelleme
- 2 Ağustos 2026: Yıldız 48.210 → 54.506, son sürüm 2026.07.11 (11 Temmuz 2026).

## Ne kazandırır?
- Önceden yüklenmiş gereksiz uygulamaları hızla kaldırır.
- Telemetri ve izleme verilerini devre dışı bırakır.
- Yapay zekâ destekli özellikleri ve reklamları kapatır.

## Kurulum

**PowerShell ile doğrudan çalıştırma (Windows)**

```
& ([scriptblock]::Create((irm "https://debloat.raphi.re/")))
```

## Çalıştırma

**Sessiz modda çalıştır**

```
& ([scriptblock]::Create((irm "https://debloat.raphi.re/"))) -Silent
```

Kaynak: Resmî Win11Debloat README (Raphire/Win11Debloat)

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Windows 11 işletim sistemimdeki gereksiz uygulamaları kaldırmak, telemetri verilerini kapatmak ve yapay zekâ destekli Copilot gibi özellikleri devre dışı bırakmak istiyorum. Win11Debloat aracını kullanarak sistemimi nasıl daha hafif ve gizlilik odaklı hale getirebilirim? Lütfen bu aracı kullanırken sistem kararlılığını korumak için dikkat etmem gerekenleri ve güvenli bir şekilde nasıl özelleştirme yapabileceğimi adım adım açıkla.

- **Kimin için:** Windows 10 veya 11 işletim sistemini kullanan, sistemini gereksiz bileşenlerden arındırmak ve gizlilik ayarlarını kontrol etmek isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/Raphire/Win11Debloat)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-16 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/win11debloat/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
