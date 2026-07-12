# Rust ile yeniden yazılan PostgreSQL

PostgreSQL veritabanı yönetim sisteminin Rust programlama dili ile yeniden yazıldığı pgrust projesi, tüm regresyon testlerini başarıyla tamamlıyor. Bu çalışma, bellek güvenliği (memory safety) odaklı bir dille veritabanı mimarisini modernize etmeyi amaçlıyor.

- ★ 2.171
- Rust
- GitHub Trending · 2026-07-12

## Ne kazandırır?
- Postgres 18.3 ile disk uyumluluğu
- 46 binden fazla regresyon test başarısı
- Bellek güvenliği odaklı modern mimari

## Kurulum

**Docker ile hızlı deneme**

```
docker run -d --name pgrust -e POSTGRES_PASSWORD=secret malisper/pgrust:v0.1 && until docker exec -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres -c '\q' >/dev/null 2>&1; do sleep 1; done && docker exec -it -e PGPASSWORD=secret pgrust psql -h 127.0.0.1 -U postgres; docker rm -f pgrust
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Pgrust projesinin temel amacı nedir, mevcut PostgreSQL ile disk uyumluluğu nasıl sağlanıyor ve projenin geliştirilmesinde yapay zekâ destekli programlamadan nasıl yararlanılıyor? Pgrust'un şu anki sürümünün Postgres 18.3 ile uyumluluk durumu ve regresyon testlerindeki başarısı hakkında bilgi ver.

- **Kimin için:** PostgreSQL mimarisini Rust dili ile modernize etmek isteyen geliştiriciler ve veritabanı araştırmacıları için uygundur. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/malisper/pgrust)

## İlgili sözlük terimleri
Memory Rust Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pgrust/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
