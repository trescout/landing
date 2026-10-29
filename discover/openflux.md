# Ağ trafiği için TCP tünelleme

Go diliyle geliştirilen OpenFlux, ağ yığını (network stack) araştırmaları için tasarlanmış bir TCP tünelleme aracıdır. Eklenebilir taşıma protokolleri (pluggable transports) desteği sayesinde ağ trafiği üzerinde esnek analiz ve yönetim imkânı sunar.

- ★ 2.299
- Go
- GitHub Trending · 2026-09-12

## Güncelleme

- **29 Ekim 2026:** Yıldız 2.184 → 2.299, son sürüm v0.17.1 (28 Ekim 2026).
- **16 Ekim 2026:** Yıldız 2.120 → 2.184, son sürüm v0.13.0 (16 Ekim 2026).
- **14 Ekim 2026:** Yıldız 2.107 → 2.120, son sürüm v0.7.3 (14 Ekim 2026).
- **13 Ekim 2026:** Yıldız 2.092 → 2.107, son sürüm v0.7.2 (13 Ekim 2026).

## Ne kazandırır?

- Eklenebilir taşıma protokolleri ile esnek ağ yönetimi
- SOCKS5 proxy desteği ile yerel ağ trafiği yönlendirme
- Yandex Docs ve WebRTC üzerinden veri iletimi

## Kurulum

**Masaüstü istemci ve çıkış düğümü derleme**

```
go mod tidy
go build -o universal-bypass-tool .
```

**Android istemci derleme**

```
export ANDROID_NDK_HOME=<your Android NDK path>
./build_android.sh
```

## Çalıştırma

**Masaüstü istemciyi başlatma**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenFlux aracını kullanarak bir TCP tüneli oluşturmak istiyorum. Masaüstü bilgisayarımda istemciyi çalıştırmak için gerekli olan derleme adımlarını ve ardından SOCKS5 proxy ayarlarını tarayıcı üzerinde nasıl yapılandıracağımı adım adım açıkla. Ayrıca, bir Linux sunucusu üzerinde çıkış düğümü (exit node) kurarken iptables ile RST paketlerini engellemenin neden gerekli olduğunu ve bu işlemin ağ güvenliğine etkisini teknik detaylarıyla belirt.

Depo: https://github.com/p1neappleXpress/OpenFlux. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Ağ yığını araştırmaları yapan ve TCP trafiğini farklı taşıma protokolleri üzerinden tünellemek isteyen kullanıcılar içindir.
- **Lisans:** GPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/p1neappleXpress/OpenFlux)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Pluggable Transports](https://trescout.com/dictionary/pluggable-transports/)
- [Network Stack](https://trescout.com/dictionary/network-stack/)
- [Proxy](https://trescout.com/dictionary/proxy/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openflux/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
