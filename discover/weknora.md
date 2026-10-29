# Belgeleri yaşayan bilgiye dönüştüren yapay zekâ

Tencent tarafından geliştirilen WeKnora, ham belgeleri sorgulanabilir bir bilgi tabanına (RAG), otonom bir akıl yürütme ajanına ve kendi kendini güncelleyen bir wiki sistemine dönüştüren açık kaynaklı bir platformdur. Go programlama diliyle yazılan bu araç, yapılandırılmamış verileri kurumsal düzeyde erişilebilir bilgi varlıklarına dönüştürmeyi amaçlar.

- ★ 35.846
- Go
- GitHub Trending · 2026-09-18

## Güncelleme

- **29 Ekim 2026:** Yıldız 35.608 → 35.846, son sürüm v0.9.0 (29 Ekim 2026).
- **27 Ekim 2026:** Yıldız 33.893 → 35.608, son sürüm v0.8.3 (14 Ekim 2026).
- **14 Ekim 2026:** Yıldız 33.718 → 33.893, son sürüm v0.8.3 (14 Ekim 2026).
- **13 Ekim 2026:** Yıldız 31.949 → 33.718, son sürüm v0.8.2 (24 Eylül 2026).

## Ne kazandırır?

- Belgeleri sorgulanabilir bir bilgi tabanına dönüştürür
- Karmaşık görevleri otonom şekilde çözen akıl yürütme ajanları sunar
- Belgeleri otomatik güncellenen bir wiki sistemine çevirir

## Kurulum

**Docker ile hızlı kurulum**

```
git clone https://github.com/Tencent/WeKnora.git
cd WeKnora
cp .env.example .env   # Edit .env as needed, see comments in the file
docker compose pull     # Pull the latest images
docker compose up -d    # Start core services
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Sen bir WeKnora asistanısın. Yüklenen belgeleri analiz ederek bunları sorgulanabilir bir bilgi tabanına dönüştür, otonom akıl yürütme ajanlarını kullanarak karmaşık soruları yanıtla ve bilgileri düzenli bir wiki yapısında güncel tut. Kullanıcının belgeler arasındaki bağlantıları kurmasına yardımcı ol, uzun süreli hafıza özelliğini kullanarak önceki etkileşimleri hatırla ve her zaman kurumsal düzeyde güvenli ve erişilebilir yanıtlar üret.

Depo: https://github.com/Tencent/WeKnora. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Kurumsal belgelerini, wiki sayfalarını ve dağınık verilerini akıllı bir bilgi sistemine dönüştürmek isteyen profesyoneller ve ekipler için uygundur.

## Bağlantılar

- [GitHub deposu →](https://github.com/Tencent/WeKnora)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-09-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [RAG](https://trescout.com/dictionary/rag/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/weknora/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
