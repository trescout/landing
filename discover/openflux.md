# Ağ trafiği için TCP tünelleme

Go diliyle geliştirilen OpenFlux, ağ yığını (network stack) araştırmaları için tasarlanmış bir TCP tünelleme aracıdır. Eklenebilir taşıma protokolleri (pluggable transports) desteği sayesinde ağ trafiği üzerinde esnek analiz ve yönetim imkânı sunar.

- ★ 1.241
- Go
- GitHub Trending · 2026-09-12

## Güncelleme
- 12 Eylül 2026: Yıldız 1.239 → 1.241, son sürüm 0.0.1 (10 Eylül 2026).

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
export ANDROID_NDK_HOME= 
./build_android.sh
```

## Çalıştırma

**Masaüstü istemciyi başlatma**

```
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenFlux aracını kullanarak bir TCP tüneli oluşturmak istiyorum. Masaüstü bilgisayarımda istemciyi çalıştırmak için gerekli olan derleme adımlarını ve ardından SOCKS5 proxy ayarlarını tarayıcı üzerinde nasıl yapılandıracağımı adım adım açıkla. Ayrıca, bir Linux sunucusu üzerinde çıkış düğümü (exit node) kurarken iptables ile RST paketlerini engellemenin neden gerekli olduğunu ve bu işlemin ağ güvenliğine etkisini teknik detaylarıyla belirt.

- **Kimin için:** Ağ yığını araştırmaları yapan ve TCP trafiğini farklı taşıma protokolleri üzerinden tünellemek isteyen kullanıcılar içindir. 
- **Lisans:** GPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/p1neappleXpress/OpenFlux)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Pluggable Transports Network Stack Proxy Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openflux/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
