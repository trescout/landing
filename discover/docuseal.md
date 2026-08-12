# Dijital belgeleri kolayca imzalayın

DocuSeal, dijital belge oluşturma, doldurma ve imzalama süreçleri için açık kaynaklı bir alternatif sunuyor. Ruby diliyle geliştirilen bu platform, elektronik imza (e-signature) süreçlerini kendi altyapısında yönetmek isteyen kullanıcılar için çözüm sağlıyor.

- ★ 18.245
- Ruby
- GitHub Trending · 2026-07-18

## Güncelleme
- 12 Ağustos 2026: Yıldız 18.183 → 18.245, son sürüm 3.2.0 (11 Ağustos 2026).
- 4 Ağustos 2026: Yıldız 18.176 → 18.183, son sürüm 3.1.7 (3 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 17.916 → 18.176, son sürüm 3.1.6 (27 Temmuz 2026).

## Ne kazandırır?
- PDF formlarını çevrim içi oluşturma ve imzalama
- Mobil uyumlu kullanıcı arayüzü
- Kendi altyapınızda güvenli veri yönetimi

## Kurulum

**Docker ile hızlı kurulum**

```
docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal
```

**Docker Compose yapılandırması**

```
curl https://raw.githubusercontent.com/docusealco/docuseal/master/docker-compose.yml > docker-compose.yml
```

## Çalıştırma

**Uygulamayı başlatma**

```
sudo HOST=your-domain-name.com docker compose up
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
DocuSeal kullanarak dijital belge imzalama süreçlerimi nasıl optimize edebilirim? PDF formlarını çevrim içi doldurulabilir hale getirme, imza doğrulama ve kullanıcı yönetimi özelliklerini kendi sunucumda yapılandırmak için izlemem gereken adımları açıkla. Ayrıca, Docker üzerinden kurulum yaptıktan sonra SMTP ayarlarıyla otomatik e-posta bildirimlerini nasıl aktif edebileceğim konusunda rehberlik et.

- **Kimin için:** Belge imzalama ve doldurma süreçlerini kendi sunucularında, güvenli ve açık kaynaklı bir çözümle yönetmek isteyen işletmeler ve bireyler içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/docusealco/docuseal)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
E-signature PDF Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/docuseal/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
