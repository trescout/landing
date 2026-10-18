# Otonom sızma testi için yapay zekâ

Go diliyle geliştirilen Pentagi, karmaşık sızma testlerini (penetration testing) gerçekleştirebilen tam otonom yapay zekâ ajanları (AI agents) sistemi sunuyor. Sistem, güvenlik açıklarını tespit etmek ve sömürmek için otonom iş akışlarını standartlaştırmayı hedefliyor.

- ★ 30.107
- Go
- GitHub Trending · 2026-07-10

## Güncelleme

- **15 Ekim 2026:** Yıldız 28.092 → 30.107, son sürüm v2.2.0 (5 Ekim 2026).
- **13 Ekim 2026:** Yıldız 26.612 → 28.092, son sürüm v2.2.0 (5 Ekim 2026).
- **12 Ekim 2026:** Yıldız 25.256 → 26.612, son sürüm v2.2.0 (5 Ekim 2026).
- **5 Ekim 2026:** Yıldız 24.299 → 25.256, son sürüm v2.2.0 (5 Ekim 2026).

## Ne kazandırır?

- Sandboxed Docker ortamında tam otonom güvenlik testleri
- Nmap ve SQLmap gibi 20'den fazla profesyonel araç desteği
- Grafana ve Prometheus ile detaylı sistem izleme

## Çalıştırma

**Servisi başlatma**

```
curl -O https://raw.githubusercontent.com/vxcontrol/pentagi/master/docker-compose.yml
docker compose up -d
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

PentAGI sistemini kullanarak hedef sistem üzerinde otonom bir sızma testi başlatmak istiyorum. Docker ortamında çalışan bu yapay zekâ ajanının, güvenlik açıklarını tespit etmesi, nmap ve sqlmap gibi araçları kullanarak tarama yapması ve bulguları detaylı bir rapor halinde sunması için gerekli iş akışını nasıl yapılandırabilirim?

Depo: https://github.com/vxcontrol/pentagi. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Sızma testlerini otomatize etmek isteyen güvenlik araştırmacıları ve profesyonelleri için tasarlanmıştır.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/vxcontrol/pentagi)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-10 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Penetration Testing](https://trescout.com/dictionary/penetration-testing/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/pentagi/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
