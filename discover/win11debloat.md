# Windows sisteminizi gereksizlerden arındırın

Win11Debloat, Windows 10 ve 11 işletim sistemlerinde önceden yüklenmiş uygulamaları kaldırmayı ve telemetri verilerini devre dışı bırakmayı sağlayan bir PowerShell betiğidir. Kullanıcıların sistemlerini özelleştirmelerine ve gereksiz bileşenlerden arındırarak sistem hafifletme (debloat) işlemi yapmalarına olanak tanır.

- ★ 48.210
- GitHub Trending · 2026-06-16

TreScout notu: Betiği uzaktan indirip çalıştırdığınız için ne yaptığını önce okumanız gerekir, kaldırılan bazı bileşenleri geri getirmek kolay değildir. Kişisel makinede önyüklü uygulamalardan ve telemetriden kurtulmak için pratik. Kurum cihazında ya da başkalarıyla paylaştığınız bilgisayarda kullanmayın.

## Ne kazandırır?
- Önceden yüklü uygulamaları hızla kaldırın
- Telemetri ve izleme verilerini devre dışı bırakın
- Sistem arayüzünü ve ayarlarını özelleştirin

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
Windows 11 veya 10 işletim sistemimde gereksiz ön yüklü uygulamaları kaldırmak, telemetri verilerini kapatmak ve sistemimi hafifletmek istiyorum. Win11Debloat aracını kullanarak sistem performansımı nasıl optimize edebilirim ve hangi ayarlar gizlilik için en uygunudur?

- **Kimin için:** Windows sistemindeki gereksiz uygulamalardan kurtulmak ve gizlilik ayarlarını kontrol altına almak isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/Raphire/Win11Debloat)

## İlgili sözlük terimleri
Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/win11debloat/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
