# Kendi sunucunuzda parola yönetimi

Eine Zusammenfassung für diesen Artikel konnte heute nicht erstellt werden. Einzelheiten finden Sie im Quelllink.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## Was es bringt
- Resmî Bitwarden istemcileriyle tam uyumlu çalışır
- Düşük kaynak tüketimiyle kendi sunucunuzda barındırılabilir
- İki faktörlü doğrulama ve acil durum erişimi sunar

## Installation
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


## Wenn Sie nicht programmieren
Benim için kendi sunucumda parola yönetimi sağlayan Vaultwarden aracını kurmama yardımcı ol. Bu araç, Bitwarden istemcileriyle uyumlu bir sunucu yazılımıdır. Docker kullanarak kurulum yapacağım için gerekli olan imajı çekme ve çalıştırma komutlarını, verilerimin kalıcı olması için bir birim (volume) bağlayarak ve HTTPS gereksinimlerini göz önünde bulundurarak nasıl yapılandıracağımı adım adım açıkla.

## Verwandte Begriffe aus dem Glossar

## Links
- GitHub-Repository →
- Auf Türkisch lesen →

---
Quelle: TreScout Entdecken · https://trescout.com/de/discover/vaultwarden/
