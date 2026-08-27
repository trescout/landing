# Açık kaynaklı müşteri destek platformu

Chatwoot, canlı sohbet, e-posta desteği ve çok kanallı müşteri hizmetleri (omni-channel desk) yönetimi sunan açık kaynaklı bir platformdur. Intercom ve Zendesk gibi ticari yazılımlara alternatif olarak geliştirilen bu araç, müşteri etkileşimlerini tek bir merkezden yönetmeyi sağlar.

- ★ 36.253
- GitHub Trending · 2026-06-12

TreScout notu: Müşterilerden gelen mesajları tek ekranda toplar: Site sohbeti, e-posta, WhatsApp. Aynı işi yapan hazır servisler kişi başına aylık ücret alır, bu kendi sunucunuzda çalıştığı için o ücret yoktur, karşılığında sunucu ve bakım sizin işiniz olur. Kurulumu tek parça değildir, yanında birkaç yardımcı program ister ve en ucuz sunucu paketlerinde zorlanır.

## Güncelleme
- 27 Ağustos 2026: Yıldız 36.001 → 36.253, son sürüm v4.17.1 (27 Ağustos 2026).
- 20 Ağustos 2026: Yıldız 35.290 → 36.001, son sürüm v4.17.0 (20 Ağustos 2026).
- 1 Ağustos 2026: Yıldız 30.493 → 35.290, son sürüm v4.16.2 (27 Temmuz 2026).

## Ne kazandırır?
- Tüm müşteri kanallarını tek bir gelen kutusunda birleştirir.
- Yapay zekâ destekli asistan ile rutin soruları otomatik yanıtlar.
- Kendi sunucunuzda barındırarak müşteri verileriniz üzerinde tam kontrol sağlar.

## Kurulum

**Ortam dosyasını indir**

```
wget -O .env https://raw.githubusercontent.com/chatwoot/chatwoot/develop/.env.example
```

**Docker Compose dosyasını indir**

```
wget -O docker-compose.yaml https://raw.githubusercontent.com/chatwoot/chatwoot/develop/docker-compose.production.yaml
```

**Veritabanını hazırla**

```
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
```

## Çalıştırma

**Servisleri başlat**

```
docker compose up -d
```

Kaynak: Resmî kaynak: https://developers.chatwoot.com/self-hosted/deployment/docker

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bir müşteri destek temsilcisi gibi davranarak gelen soruları yanıtla. Chatwoot üzerindeki Captain yapay zekâ asistanı olarak, sık sorulan soruları otomatik olarak çözümle ve karmaşık konuları ilgili ekip arkadaşlarına yönlendir. Müşterilere her zaman nazik, hızlı ve doğru bilgiler vererek destek deneyimini iyileştir.

- **Kimin için:** Müşteri etkileşimlerini tek merkezden yönetmek ve destek süreçlerini otomatize etmek isteyen işletmeler için uygundur. 

## Bağlantılar
- [GitHub deposu →](https://github.com/chatwoot/chatwoot)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Omni-channel Desk Omni-channel Deployment Self-hosted Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/chatwoot/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
