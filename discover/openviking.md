# Yapay zekâ ajanları için dosya sistemli hafıza

Volcengine tarafından geliştirilen OpenViking, yapay zekâ ajanları için kendi kendini geliştiren bir bağlam veritabanı sunuyor. Bu sistem, ajan hafızasını, bilgi getirme (RAG) süreçlerini ve yetenekleri (skills) tek bir çatı altında birleştiriyor.

- ★ 40.425
- Python
- GitHub Trending · 2026-08-18

## Güncelleme

- **20 Ekim 2026:** Yıldız 40.333 → 40.425, son sürüm v0.5.1.1 (20 Ekim 2026).
- **19 Ekim 2026:** Yıldız 39.519 → 40.333, son sürüm v0.5.1 (19 Ekim 2026).
- **9 Ekim 2026:** Yıldız 39.151 → 39.519, son sürüm v0.5.0 (9 Ekim 2026).
- **3 Ekim 2026:** Yıldız 38.859 → 39.151, son sürüm v0.4.23 (2 Ekim 2026).

## Ne kazandırır?

- Bilgileri dosya sistemi gibi hiyerarşik düzenler.
- Katmanlı yükleme ile yapay zekâ maliyetini düşürür.
- Ajan geçmişini izlenebilir ve hata ayıklanabilir kılar.

## Kurulum

**Sunucu kurulumu ve başlatma**

```
pip install openviking --upgrade
openviking-server init      # interactive wizard: providers, models, ov.conf
openviking-server doctor    # validate setup
openviking-server           # start (background: nohup openviking-server > openviking.log 2>&1 &)
```

## Çalıştırma

**Bot desteğiyle sohbet başlatma**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat   # in another terminal
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

OpenViking veritabanını kullanarak bir yapay zekâ ajanı için bağlam yönetimi kurgula. Bilgileri L0 özet, L1 genel bakış ve L2 detay katmanlarına ayırarak viking:// protokolü üzerinden yapılandır. Ajanın hafızasını, kaynaklarını ve yeteneklerini bu sanal dosya sistemine yerleştirerek, sorgulama sırasında dizinler arasında gezinebilmesini ve geçmiş oturumlarından öğrenerek uzun vadeli hafıza oluşturmasını sağla.

Depo: https://github.com/volcengine/OpenViking. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ ajanlarının hafıza yönetimi, bilgi getirme süreçleri ve yeteneklerini tek bir düzenli sistemde birleştirmek isteyen geliştiriciler içindir.
- **Lisans:** AGPL-3.0

## Bağlantılar

- [GitHub deposu →](https://github.com/volcengine/OpenViking)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [RAG](https://trescout.com/dictionary/rag/)
- [AI Skills](https://trescout.com/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openviking/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
