# Açık kaynaklı ziwei doushu astroloji motoru

Renhuai123/ziwei-doushu, Ni Haixia'nın Tianji sistemini temel alan ve Ziwei Doushu astrolojik haritalarını hesaplayan açık kaynaklı bir TypeScript motorudur. Proje, 1950 ile 2026 yılları arasındaki tarihleri kapsayan 13 boyutlu geniş bir astrolojik yorum veri kümesini (v4.0) kullanıma sunuyor.

- ★ 11.459
- TypeScript
- GitHub Trending · 2026-10-24

## Güncelleme

- **31 Ekim 2026:** Yıldız 10.402 → 11.459, son sürüm v4.0-13d (15 Ekim 2026).
- **30 Ekim 2026:** Yıldız 9.213 → 10.402, son sürüm v4.0-13d (15 Ekim 2026).
- **29 Ekim 2026:** Yıldız 8.056 → 9.213, son sürüm v4.0-13d (15 Ekim 2026).
- **26 Ekim 2026:** Yıldız 6.993 → 8.056, son sürüm v4.0-13d (15 Ekim 2026).

## Ne kazandırır?

- Altı yüz yetmiş beş bin命盘 ve on üç boyutlu geniş astrolojik yorum veri kümesi sunar.
- Gerçek zamanlı harita hesaplama ve güneş zamanı düzeltmesi yapar.
- Ni Haixia'nın Tianji sistemini temel alan eksiksiz bir astroloji motoru barındırır.

## Kurulum

**Projeyi klonlayıp hazırlama**

```
git clone https://github.com/Renhuai123/ziwei-doushu.git
cd ziwei-doushu

# 安装依赖
npm install

# 配置环境变量（只看排盘可以跳过；AI 配置仅在你自己实现了 /api/* 接口时才用得上）
cp .env.example .env.local

# 启动开发服务器
npm run dev
```

## Çalıştırma

**Testleri çalıştırma**

```
npm test            # 排盘引擎回归（768 盘 × 紫微铁律、夏令时、立春边界、红鸾天喜、样本时辰一致性、时辰序号边界、日期合法性、同宫双四化）
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Ziwei Doushu projesini bilgisayarıma kurup çalıştırmak istiyorum. Lütfen terminal komutlarını sırasıyla çalıştırarak geliştirme sunucusunu ayağa kaldır.

Depo: https://github.com/Renhuai123/ziwei-doushu. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Çin geleneksel astroloji sistemlerini ve harita hesaplama motorlarını incelemek isteyen geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/Renhuai123/ziwei-doushu)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-24 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [v4.0](https://trescout.com/dictionary/v4-0/)
- [Terminal](https://trescout.com/dictionary/terminal/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ziwei-doushu/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
