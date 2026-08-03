# Grok servisleri için merkezi yönetim

Grok Build, Grok Web ve Grok Console platformları için geliştirilen bu ağ geçidi (API gateway), çoklu hesap yönetimini tek bir merkezde topluyor. Go diliyle yazılan araç, kullanıcıların farklı Grok servislerine erişimini standartlaştırarak yönetilebilir bir arayüz sunuyor.

- ★ 6.945
- Go
- GitHub Trending · 2026-07-15

## Güncelleme
- 2 Ağustos 2026: Yıldız 5.927 → 6.945, son sürüm v3.0.11 (29 Temmuz 2026).

## Ne kazandırır?
- Grok Build, Web ve Console hesaplarını tek panelde birleştirir
- OpenAI ve Anthropic uyumlu standart API arayüzü sunar
- Gelişmiş hesap yönetimi, model yönlendirme ve hata yönetimi sağlar

## Kurulum

**Docker ile hızlı kurulum**

```
git clone https://github.com/chenyme/grok2api.git
cd grok2api
cp config.example.yaml config.yaml
```

**Servisi başlatma**

```
docker compose pull
docker compose up -d
```

## Çalıştırma

**Servis yönetimi**

```
docker compose logs -f grok2api
docker compose restart grok2api
docker compose down
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Grok2API kurulumunu tamamladım ve yönetici paneline giriş yaptım. Şimdi Grok Build, Web veya Console hesaplarımı sisteme nasıl tanımlayabilirim, model eşleştirmelerini nasıl yaparım ve dışarıdan kullanmak için API anahtarını hangi adımları izleyerek oluşturabilirim? Lütfen bu süreci adım adım açıkla.

- **Kimin için:** Birden fazla Grok hesabını yönetmek isteyen ve bu servisleri kendi uygulamalarında standart bir API üzerinden kullanmayı hedefleyen geliştiriciler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/chenyme/grok2api)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-15 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
API Gateway Gateway API Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/grok2api/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
