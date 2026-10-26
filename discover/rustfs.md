# Yüksek performanslı nesne depolama sistemi

RustFS, S3 uyumlu yüksek performanslı bir nesne depolama sistemi (object storage system) olarak geliştirildi. MinIO ve Ceph gibi diğer S3 uyumlu platformlarla birlikte çalışabilme ve veri taşıma desteği sunuyor.

- ★ 35.371
- Rust
- GitHub Trending · 2026-09-19

## Güncelleme

- **26 Ekim 2026:** Yıldız 35.063 → 35.371, son sürüm 1.0.4 (25 Ekim 2026).
- **18 Ekim 2026:** Yıldız 35.038 → 35.063, son sürüm 1.0.3 (17 Ekim 2026).
- **17 Ekim 2026:** Yıldız 34.330 → 35.038, son sürüm 1.0.2 (16 Ekim 2026).
- **3 Ekim 2026:** Yıldız 33.264 → 34.330, son sürüm 1.0.1 (3 Ekim 2026).

## Ne kazandırır?

- Rust dili ile yüksek hız ve bellek güvenliği sağlar
- S3 uyumlu yapısıyla mevcut araçlarla sorunsuz çalışır
- Apache 2.0 lisansı ile kısıtlamasız ticari kullanım sunar

## Kurulum

**Kurulum betiği ile başlatma**

```
curl -O https://rustfs.com/install_rustfs.sh && bash install_rustfs.sh
```

**Docker ile en güncel sürümü çalıştırma**

```
docker run -d -p 9000:9000 -p 9001:9001 -v $(pwd)/data:/data -v $(pwd)/logs:/logs rustfs/rustfs:latest
```

## Çalıştırma

**Docker Compose kullanarak sistemi başlat**

```
docker compose -f docker-compose-simple.yml up -d
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

RustFS kullanarak yüksek performanslı bir nesne depolama ortamı kurmak istiyorum. Sistemin S3 uyumluluğundan faydalanarak verilerimi nasıl yönetebilirim ve dağıtık mimari üzerinde ölçeklendirme yaparken nelere dikkat etmeliyim? Apache 2.0 lisanslı bu sistemin kurulumu ve temel yapılandırma ayarları hakkında bana adım adım rehberlik et.

Depo: https://github.com/rustfs/rustfs. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Büyük veri iş yükleri, yapay zekâ projeleri ve veri gölleri için hızlı, güvenli ve S3 uyumlu bir depolama çözümü arayan sistem yöneticileri ve geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/rustfs/rustfs)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-19 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Object Storage System](https://trescout.com/dictionary/object-storage-system/)
- [Rust](https://trescout.com/dictionary/rust/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/rustfs/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
