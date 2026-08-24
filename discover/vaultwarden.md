# Kendi sunucunuzda parola yönetimi

Bu öğenin özeti bugün üretilemedi · detaylar için kaynak bağlantısını inceleyebilirsiniz.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## Güncelleme
- 24 Ağustos 2026: Yıldız 65.983 → 65.982, son sürüm 1.37.2 (22 Ağustos 2026).

## Ne kazandırır?
- Resmî Bitwarden istemcileriyle tam uyumlu çalışır
- Düşük kaynak tüketimiyle kendi sunucunuzda barındırılabilir
- İki faktörlü doğrulama ve acil durum erişimi sunar

## Kurulum

**Kapsayıcıyı indirme ve çalıştırma**

```
docker pull vaultwarden/server:latest
docker run --detach --name vaultwarden \
--env DOMAIN="https://vw.domain.tld" \
--volume /vw-data/:/data/ \
--restart unless-stopped \
--publish 127.0.0.1:8000:80 \
vaultwarden/server:latest
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Benim için kendi sunucumda parola yönetimi sağlayan Vaultwarden aracını kurmama yardımcı ol. Bu araç, Bitwarden istemcileriyle uyumlu bir sunucu yazılımıdır. Docker kullanarak kurulum yapacağım için gerekli olan imajı çekme ve çalıştırma komutlarını, verilerimin kalıcı olması için bir birim (volume) bağlayarak ve HTTPS gereksinimlerini göz önünde bulundurarak nasıl yapılandıracağımı adım adım açıkla.

- **Kimin için:** Kendi şifrelerini ve hassas verilerini üçüncü taraf bulut hizmetlerine güvenmek yerine, kendi sunucusunda barındırmak isteyen kullanıcılar içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/dani-garcia/vaultwarden)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-24 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/vaultwarden/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
