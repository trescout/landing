# PostgreSQL üzerinde dayanıklı süreç yönetimi

Microsoft tarafından geliştirilen pg_durable, PostgreSQL üzerinde dayanıklı yürütme (durable execution) süreçlerini yönetmek için tasarlanmış bir kütüphanedir. Rust diliyle yazılan araç, karmaşık iş akışlarını veritabanı içerisinde hata toleranslı ve kalıcı bir şekilde çalıştırmayı sağlar.

- ★ 2.781
- Rust
- GitHub Trending · 2026-06-08

## Güncelleme
- 24 Ağustos 2026: Yıldız 2.716 → 2.781, son sürüm v0.2.6 (24 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 1.580 → 2.716, son sürüm v0.2.5 (30 Temmuz 2026).

## Ne kazandırır?
- İş akışlarını veritabanı içinde hata toleranslı ve kalıcı şekilde yönetir.
- Çökme veya kesinti durumunda işlemleri en son kontrol noktasından devam ettirir.
- Ek altyapı gerektirmeden doğrudan PostgreSQL üzerinde çalışır.

## Kurulum

**Eklentiyi Etkinleştirme**

```
CREATE EXTENSION pg_durable;
```

## Çalıştırma

**İş Akışı Başlatma**

```
SELECT df.start(
'SELECT id FROM documents WHERE processed = false LIMIT 100' |=> 'batch'
~> 'UPDATE documents SET processed = true WHERE id = ANY($batch)'
);
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
PostgreSQL üzerinde pg_durable eklentisini kullanarak bir iş akışı oluşturmak istiyorum. Veritabanı içinde hata toleranslı ve kalıcı bir süreç yönetmek için df.start() fonksiyonunu nasıl yapılandırmalıyım? SQL adımlarını birbirine bağlayan ~> ve |=> operatörlerini kullanarak, verileri işleyen ve hata durumunda kaldığı yerden devam edebilen bir yapıyı nasıl kurabilirim? Lütfen bu süreci SQL komutları ile örneklendirerek açıkla.

- **Kimin için:** Veri işleme süreçlerini, hata toleranslı ve kalıcı bir şekilde doğrudan PostgreSQL üzerinde yönetmek isteyen arka uç geliştiricileri, veritabanı yöneticileri ve veri mühendisleri için uygundur. 

## Bağlantılar
- [GitHub deposu →](https://github.com/microsoft/pg_durable)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-08 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Durable Execution Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pg-durable/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
