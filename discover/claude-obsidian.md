# Claude Code İçin Yerel Bilgi Sistemi

Claude Code ve uyumlu Agent Skills sunucuları için yerel öncelikli bir bilgi sistemidir. Kaynak materyallerini kaynak gösteren, bağlantılı Obsidian sayfalarına dönüştürür.

- ★ 13.706
- Python
- GitHub Trending · 2026-08-25

## Kurulum

**Claude Code marketplace’ini ekle**

```
claude plugin marketplace add AgriciDaniel/claude-obsidian
```

**Claude-obsidian eklentisini kur**

```
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

**Ayrı vault planını oluştur**

```
python3 scripts/claude-obsidian.py init --generated-at --operation-id init-reviewed
```

## Çalıştırma

**Eklenti kurulumunu doğrula**

```
claude plugin list
```

**Wiki akışını başlat**

```
/claude-obsidian:wiki
```

Kaynak: Resmî README ve dokümantasyon kaynakları: https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md, https://github.com/AgriciDaniel/claude-obsidian

## Güncelleme
- 27 Ağustos 2026: Yıldız 12.404 → 13.706, son sürüm v2.1.1 (25 Ağustos 2026).

## Bu araç ne yapar?

Kaynak ve iddia defterleri, bağlantılı sayfalar ve bilgi haritalarıyla araştırma içeriğini düzenler. Paralel aracılar taslaklar üretir, bir orkestratör ise geri alınabilir bir işlemle onaylanan değişiklikleri uygular.

## Kimin için?

Claude Code ile yerel, kaynak gösteren bir Obsidian bilgi tabanı oluşturmak isteyenler.

## Ne beklememeli?

Otomatik transkript kaydı, bulut senkronizasyonu, doğruluk garantisi veya yedekleme ve kaynak kontrolü yerine kullanım.

## Öne çıkanlar
- Yerel varsayılan çalışma ve açık ağ çıkışı yaklaşımı
- Kaynak ve iddia defterleriyle kaynak gösteren, bağlantılı sayfalar
- Onaylanmış değişiklikleri geri alınabilir işlemlerle uygulama

## İlk kullanım akışı
- Depoyu klonlayın ve Python 3.11 veya üzeri bir ortam hazırlayın
- Ayrı bir vault için başlangıç planını oluşturun ve JSON planını inceleyin
- approved_plan_sha256 değerini kontrol edip tam işlemi onaylayın
- Vault'u Obsidian'da açın ve yerel eklentiyle Claude Code'u çalıştırın
- Wiki akışını başlatıp kaynak ekleme, sorgulama ve açıkça kaydetme adımlarını kullanın

## Güvenli başlangıç

Sistem bir doğruluk kaynağı değildir. Veriler için ayrıca yedekleme ve kaynak kontrolü kullanın; ağ çıkışı ve uygulanan planı gözden geçirin.

## İlk görev istemi
İlk adım için hazır istem 
Kaynakları kaynak ve iddia defterleriyle ilişkilendirerek yerel bir Obsidian wiki akışı başlat.

## Bağlantılar
- [GitHub deposu →](https://github.com/AgriciDaniel/claude-obsidian)
- [Kurulum rehberi →](https://github.com/AgriciDaniel/claude-obsidian/blob/main/docs/install-guide.md)
- [Resmî README →](https://github.com/AgriciDaniel/claude-obsidian)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-25 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Agent Skills AI Skills Agent

---
Kaynak: TreScout Keşif · https://trescout.com/discover/claude-obsidian/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
