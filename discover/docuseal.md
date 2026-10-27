# Dijital belgeleri kolayca imzalayın

DocuSeal, dijital belge oluşturma, doldurma ve imzalama süreçleri için açık kaynaklı bir alternatif sunuyor. Ruby diliyle geliştirilen bu platform, elektronik imza (e-signature) süreçlerini kendi altyapısında yönetmek isteyen kullanıcılar için çözüm sağlıyor.

- ★ 18.802
- Ruby
- GitHub Trending · 2026-07-18

## Güncelleme

- **27 Ekim 2026:** Yıldız 18.752 → 18.802, son sürüm 3.3.4 (26 Ekim 2026).
- **19 Ekim 2026:** Yıldız 18.698 → 18.752, son sürüm 3.3.3 (19 Ekim 2026).
- **12 Ekim 2026:** Yıldız 18.654 → 18.698, son sürüm 3.3.2 (12 Ekim 2026).
- **5 Ekim 2026:** Yıldız 18.631 → 18.654, son sürüm 3.3.1 (5 Ekim 2026).

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

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

DocuSeal kullanarak dijital belge imzalama süreçlerimi nasıl optimize edebilirim? PDF formlarını çevrim içi doldurulabilir hale getirme, imza doğrulama ve kullanıcı yönetimi özelliklerini kendi sunucumda yapılandırmak için izlemem gereken adımları açıkla. Ayrıca, Docker üzerinden kurulum yaptıktan sonra SMTP ayarlarıyla otomatik e-posta bildirimlerini nasıl aktif edebileceğim konusunda rehberlik et.

Depo: https://github.com/docusealco/docuseal. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Belge imzalama ve doldurma süreçlerini kendi sunucularında, güvenli ve açık kaynaklı bir çözümle yönetmek isteyen işletmeler ve bireyler içindir.
- **Lisans:** AGPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/docusealco/docuseal)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [E-signature](https://trescout.com/dictionary/e-signature/)
- [PDF](https://trescout.com/dictionary/pdf/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/docuseal/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
