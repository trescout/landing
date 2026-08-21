# Yapay zekâ ajanları için dosya sistemli hafıza

Volcengine tarafından geliştirilen OpenViking, yapay zekâ ajanları için kendi kendini geliştiren bir bağlam veritabanı sunuyor. Bu sistem, ajan hafızasını, bilgi getirme (RAG) süreçlerini ve yetenekleri (skills) tek bir çatı altında birleştiriyor.

- ★ 31.462
- Python
- GitHub Trending · 2026-08-18

## Güncelleme
- 21 Ağustos 2026: Yıldız 30.721 → 31.462, son sürüm v0.4.16 (21 Ağustos 2026).
- 20 Ağustos 2026: Yıldız 29.066 → 30.721, son sürüm v0.4.15 (18 Ağustos 2026).
- 18 Ağustos 2026: Yıldız 29.050 → 29.066, son sürüm v0.4.15 (18 Ağustos 2026).

## Ne kazandırır?
- Bilgileri dosya sistemi gibi hiyerarşik düzenler.
- Katmanlı yükleme ile yapay zekâ maliyetini düşürür.
- Ajan geçmişini izlenebilir ve hata ayıklanabilir kılar.

## Kurulum

**Sunucu kurulumu ve başlatma**

```
pip install openviking --upgrade
openviking-server init # interactive wizard: providers, models, ov.conf
openviking-server doctor # validate setup
openviking-server # start (background: nohup openviking-server > openviking.log 2>&1 &)
```

## Çalıştırma

**Bot desteğiyle sohbet başlatma**

```
pip install "openviking[bot]"
openviking-server --with-bot
ov chat # in another terminal
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
OpenViking veritabanını kullanarak bir yapay zekâ ajanı için bağlam yönetimi kurgula. Bilgileri L0 özet, L1 genel bakış ve L2 detay katmanlarına ayırarak viking:// protokolü üzerinden yapılandır. Ajanın hafızasını, kaynaklarını ve yeteneklerini bu sanal dosya sistemine yerleştirerek, sorgulama sırasında dizinler arasında gezinebilmesini ve geçmiş oturumlarından öğrenerek uzun vadeli hafıza oluşturmasını sağla.

- **Kimin için:** Yapay zekâ ajanlarının hafıza yönetimi, bilgi getirme süreçleri ve yeteneklerini tek bir düzenli sistemde birleştirmek isteyen geliştiriciler içindir. 
- **Lisans:** AGPL-3.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/volcengine/OpenViking)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-18 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
RAG AI Skills Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/openviking/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
