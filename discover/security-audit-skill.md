# Yapay zekâ ile otomatik güvenlik denetimi

Cloudflare tarafından geliştirilen security-audit-skill, kodlama ajanlarının çok aşamalı güvenlik denetimleri yapmasını sağlayan bir yetenek paketi (skill). Makine tarafından okunabilir ve bağımsız olarak doğrulanmış bulgular üreterek yazılım geliştirme süreçlerinde güvenlik standartlarını otomatize ediyor.

- ★ 37.788
- JavaScript
- GitHub Trending · 2026-09-18

## Güncelleme

- **22 Ekim 2026:** Yıldız 34.917 → 37.788.
- **21 Ekim 2026:** Yıldız 32.941 → 34.917.
- **20 Ekim 2026:** Yıldız 31.356 → 32.941.
- **19 Ekim 2026:** Yıldız 29.705 → 31.356.

## Ne kazandırır?

- Kod tabanında çok aşamalı güvenlik taraması yapar
- Bulguları bağımsız doğrulama ile onaylar
- Standartlaştırılmış güvenlik raporları oluşturur

## Kurulum

**Yerel kurulum**

```
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit
```

**Genel kurulum**

```
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit \
  --global
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bu kod tabanı için kapsamlı bir güvenlik denetimi başlat. Mimariyi haritalandırarak giriş noktalarını belirle, ardından güvenlik açıklarını tespit etmek için çok aşamalı bir tarama gerçekleştir. Bulduğun her bir güvenlik açığı adayını bağımsız bir doğrulama sürecinden geçirerek doğrulanmış, doğrulanması gereken veya reddedilmiş olarak sınıflandır. Sonuçları yapılandırılmış bir formatta raporla ve tüm bulguları projenin güvenlik standartlarına göre belgele.

Depo: https://github.com/cloudflare/security-audit-skill. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kodlama ajanı kullanan ve yazılım geliştirme süreçlerine otomatik güvenlik denetimlerini entegre etmek isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/cloudflare/security-audit-skill)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Skill](https://trescout.com/dictionary/skill/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/security-audit-skill/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
