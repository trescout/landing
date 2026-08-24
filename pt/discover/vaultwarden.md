# Kendi sunucunuzda parola yönetimi

Não foi possível produzir um resumo para este item hoje. Consulte o link da fonte para obter detalhes.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## O que você ganha
- Resmî Bitwarden istemcileriyle tam uyumlu çalışır
- Düşük kaynak tüketimiyle kendi sunucunuzda barındırılabilir
- İki faktörlü doğrulama ve acil durum erişimi sunar

## Instalação
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


## Se você não programa
Benim için kendi sunucumda parola yönetimi sağlayan Vaultwarden aracını kurmama yardımcı ol. Bu araç, Bitwarden istemcileriyle uyumlu bir sunucu yazılımıdır. Docker kullanarak kurulum yapacağım için gerekli olan imajı çekme ve çalıştırma komutlarını, verilerimin kalıcı olması için bir birim (volume) bağlayarak ve HTTPS gereksinimlerini göz önünde bulundurarak nasıl yapılandıracağımı adım adım açıkla.

## Termos relacionados do glossário

## Links
- Repositório no GitHub →
- Ler em turco →

---
Fonte: TreScout Descobrir · https://trescout.com/pt/discover/vaultwarden/
