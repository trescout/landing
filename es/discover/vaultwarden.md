# Kendi sunucunuzda parola yönetimi

No se pudo producir un resumen de este artículo hoy; consulte el enlace fuente para obtener más detalles.

- ★ 65.982
- Rust
- GitHub Trending · 2026-08-24

## Qué aporta
- Resmî Bitwarden istemcileriyle tam uyumlu çalışır
- Düşük kaynak tüketimiyle kendi sunucunuzda barındırılabilir
- İki faktörlü doğrulama ve acil durum erişimi sunar

## Instalación
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


## Si no programa
Benim için kendi sunucumda parola yönetimi sağlayan Vaultwarden aracını kurmama yardımcı ol. Bu araç, Bitwarden istemcileriyle uyumlu bir sunucu yazılımıdır. Docker kullanarak kurulum yapacağım için gerekli olan imajı çekme ve çalıştırma komutlarını, verilerimin kalıcı olması için bir birim (volume) bağlayarak ve HTTPS gereksinimlerini göz önünde bulundurarak nasıl yapılandıracağımı adım adım açıkla.

## Términos relacionados del glosario

## Enlaces
- Repositorio en GitHub →
- Leer en turco →

---
Fuente: TreScout Descubrir · https://trescout.com/es/discover/vaultwarden/
