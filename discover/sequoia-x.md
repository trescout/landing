# Çin borsası için otomatik hisse seçimi

Sequoia-X, Çin borsa verilerini kullanarak teknik analiz formüllerine göre otomatik hisse senedi seçimi yapan bir Python tabanlı yazılım. Gün sonu piyasa kapanışından sonra tarama işlemlerini gerçekleştirerek sonuçları kurumsal mesajlaşma uygulaması olan Feishu üzerinden iletiyor.

- ★ 6.376
- Python
- GitHub Trending · 2026-09-03

## Ne kazandırır?
- Hisse senedi verilerini yerel veritabanında saklar
- Birden fazla teknik analiz stratejisini otomatik uygular
- Gün sonu sonuçlarını mesajlaşma uygulaması Feishu üzerinden iletir

## Kurulum

**Gerekli kütüphaneleri yükleme**

```
pip install .
```

## Çalıştırma

**Geçmiş verileri ilk kez yükleme**

```
python main.py --backfill
```

**Günlük taramayı başlatma**

```
python main.py
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Sequoia-X aracını kullanarak Çin borsasındaki hisse senetlerini teknik analiz yöntemleriyle taramak istiyorum. Python ortamımda gerekli kurulumları yaptıktan sonra, önce geçmiş verileri yüklemek için backfill modunu, ardından günlük piyasa kapanışından sonra otomatik tarama ve bildirim almak için günlük çalışma modunu kullanacağım. Bu süreçte verilerin yerel SQLite veritabanında saklanmasını ve sonuçların Feishu üzerinden gönderilmesini sağlamak istiyorum.

- **Kimin için:** Çin borsasında işlem yapan ve teknik analiz stratejilerini otomatize etmek isteyen yatırımcılar içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/sngyai/Sequoia-X)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-09-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/sequoia-x/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
