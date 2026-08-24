# Kendi sunucunuzda parola yönetimi

Un résumé pour cet article n'a pas pu être produit aujourd'hui · voir le lien source pour plus de détails.

- ★ 65 982
- Rust
- GitHub Trending · 2026-08-24

## Ce que ça vous apporte
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


## Si vous ne codez pas
Benim için kendi sunucumda parola yönetimi sağlayan Vaultwarden aracını kurmama yardımcı ol. Bu araç, Bitwarden istemcileriyle uyumlu bir sunucu yazılımıdır. Docker kullanarak kurulum yapacağım için gerekli olan imajı çekme ve çalıştırma komutlarını, verilerimin kalıcı olması için bir birim (volume) bağlayarak ve HTTPS gereksinimlerini göz önünde bulundurarak nasıl yapılandıracağımı adım adım açıkla.

## Termes liés du glossaire

## Liens
- Dépôt GitHub →
- Lire en turc →

---
Source : TreScout Découvrir · https://trescout.com/fr/discover/vaultwarden/
