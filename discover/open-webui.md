# Yapay zekâ modelleriniz için tek arayüz

open-webui, Ollama ve OpenAI API gibi yapay zekâ modelleriyle etkileşime geçmeyi sağlayan kullanıcı dostu bir arayüzdür. Yerel veya bulut tabanlı dil modellerini yönetmek için geliştirilmiş web tabanlı bir arayüz (interface) sunar.

- ★ 155.750
- Python
- GitHub Trending · 2026-10-12

## Güncelleme

- **15 Ekim 2026:** Yıldız 154.432 → 155.750, son sürüm v0.12.2 (14 Ekim 2026).
- **12 Ekim 2026:** Yıldız 154.419 → 154.432, son sürüm v0.12.0 (10 Ekim 2026).

## Ne kazandırır?

- Yerel ve bulut tabanlı tüm yapay zekâ modellerini tek bir web ekranında yönetebilirsiniz.
- Kendi belgelerinizi sisteme yükleyerek metinleriniz üzerinden soru-cevap yapabilir ve internette arama yaptırabilirsiniz.
- Görsel üretimi, sesli arama, takvim yönetimi ve not alma araçlarını sohbet alanından ayrılmadan kullanabilirsiniz.

## Kurulum

**Python paket yöneticisi pip ile kurulum**

```
pip install open-webui
```

## Çalıştırma

**Yazılım kutulama aracı Docker ile başlat**

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bilgisayarımda yerel veya bulut tabanlı yapay zekâ modellerini çalıştırmak için Open WebUI kurmak istiyorum. Yazılım paketleme aracı Docker üzerinden `docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main` komutunu kullanarak ya da Python tarafında `pip install open-webui` komutu ile kurulumu nasıl tamamlayacağımı, arayüze tarayıcıdan nasıl erişeceğimi adım adım ve teknik terimleri basitleştirerek anlat.

- **Kimin için:** Farklı yapay zekâ modellerini kendi bilgisayarında veya sunucusunda tek bir modern arayüzden yönetmek isteyen herkes içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/open-webui/open-webui)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Backend](https://trescout.com/dictionary/backend/)
- [Interface](https://trescout.com/dictionary/interface/)
- [API](https://trescout.com/dictionary/api/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/open-webui/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
