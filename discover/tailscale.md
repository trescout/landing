# Cihazlar arası güvenli ağ bağlantısı

Tailscale, WireGuard protokolünü iki faktörlü kimlik doğrulama (two-factor authentication) ile birleştirerek güvenli ağ bağlantıları kurmayı kolaylaştırıyor. Go diliyle geliştirilen bu araç, karmaşık ağ yapılandırmalarına ihtiyaç duymadan cihazlar arası şifreli iletişim sağlıyor.

- ★ 38.204
- Go
- GitHub Trending · 2026-07-11

## Güncelleme

- **28 Ekim 2026:** Yıldız 37.855 → 38.204, son sürüm v1.104.4 (28 Ekim 2026).
- **21 Ekim 2026:** Yıldız 37.270 → 37.855, son sürüm v1.104.2 (21 Ekim 2026).
- **8 Ekim 2026:** Yıldız 37.012 → 37.270, son sürüm v1.104.1 (7 Ekim 2026).
- **29 Eylül 2026:** Yıldız 36.353 → 37.012, son sürüm v1.102.5 (29 Eylül 2026).

## Ne kazandırır?

- WireGuard protokolü ile şifreli iletişim
- İki faktörlü kimlik doğrulama desteği
- Karmaşık ağ yapılandırması gerektirmeyen kurulum

## Kurulum

**Go ile kurulum**

```
go install tailscale.com/cmd/tailscale{,d}
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Tailscale kullanarak farklı cihazlarım arasında nasıl güvenli bir ağ kurabilirim ve bu süreçte WireGuard protokolünün sağladığı şifreleme avantajlarından nasıl yararlanabilirim? İki faktörlü kimlik doğrulamanın ağ güvenliğime katkılarını ve cihazlarımı birbirine bağlamak için izlemem gereken temel adımları açıklar mısın?

Depo: https://github.com/tailscale/tailscale. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Cihazları arasında karmaşık ağ ayarlarıyla uğraşmadan güvenli ve şifreli bir bağlantı kurmak isteyen herkes için uygundur.
- **Lisans:** BSD-3-Clause

## Bağlantılar

- [GitHub deposu →](https://github.com/tailscale/tailscale)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-11 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tailscale/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
