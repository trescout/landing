# Windows sisteminizi gereksizlerden arındırın

Win11Debloat, Windows 10 ve 11 işletim sistemlerinde önceden yüklenmiş uygulamaları kaldırmayı ve telemetri verilerini devre dışı bırakmayı sağlayan bir PowerShell betiğidir. Kullanıcıların sistemlerini özelleştirmelerine ve gereksiz bileşenlerden arındırarak sistem hafifletme (debloat) işlemi yapmalarına olanak tanır.

- ★ 48.210
- GitHub Trending · 2026-06-16

TreScout notu: Betiği uzaktan indirip çalıştırdığınız için ne yaptığını önce okumanız gerekir, kaldırılan bazı bileşenleri geri getirmek kolay değildir. Kişisel makinede önyüklü uygulamalardan ve telemetriden kurtulmak için pratik. Kurum cihazında ya da başkalarıyla paylaştığınız bilgisayarda kullanmayın.

## Ne kazandırır?
- Önceden yüklenmiş uygulamaları hızla kaldırın
- Telemetri ve takip verilerini devre dışı bırakın
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
Windows 11 veya 10 işletim sistemimde gereksiz uygulamaları kaldırmak, telemetri verilerini kapatmak ve sistemimi hafifletmek istiyorum. Win11Debloat aracını kullanarak sistem performansımı nasıl optimize edebilirim ve hangi ayarların gizlilik açısından kapatılması daha güvenlidir?

- **Kimin için:** Windows işletim sistemini gereksiz bileşenlerden arındırarak daha hafif ve kişiselleştirilmiş bir deneyim isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/Raphire/Win11Debloat)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-16 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/win11debloat/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
