# Yerel cihazda yapay zekâ modelleri

Bonsai demo projesi, makine öğrenimi (machine learning) modellerinin dağıtım süreçlerini basitleştirmek için tasarlanmış bir araç seti sunuyor. Yazılım, karmaşık model mimarilerini yönetilebilir iş akışlarına dönüştürerek geliştiricilerin uygulama süreçlerini optimize etmesine yardımcı oluyor.

- ★ 1.587
- Shell
- GitHub Trending · 2026-07-17

## Ne kazandırır?
- Düşük bellek kullanımıyla yüksek performanslı modelleri yerel olarak çalıştırır.
- Görsel işleme ve araç çağırma gibi gelişmiş özellikler sunar.
- Farklı donanım mimarileriyle geniş uyumluluk sağlar.

## Kurulum

**macOS ve Linux kurulumu**

```
git clone https://github.com/PrismML-Eng/Bonsai-demo.git
cd Bonsai-demo

# (Optional) Choose a model size: 27B (default), 8B, 4B, or 1.7B
export BONSAI_MODEL=27B

# Set your HuggingFace token (only required for 27B while its repos are private)
export BONSAI_TOKEN="hf_your_token_here"

# One command does everything: installs deps, downloads models + binaries
./setup.sh
```

## Çalıştırma

**Yerel sunucuyu başlatma**

```
./scripts/start_llama_server.sh # http://localhost:8080

# Serve a different model size
BONSAI_MODEL=4B ./scripts/start_llama_server.sh
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Bonsai-demo projesini kullanarak yerel cihazımda yapay zekâ modellerini çalıştırmak istiyorum. Kurulum için gerekli olan git deposunu klonladıktan sonra, HuggingFace token bilgilerimi tanımlayıp ./setup.sh komutuyla bağımlılıkları ve modelleri indirmem gerekiyor. Ardından, ./scripts/start_llama_server.sh komutunu kullanarak yerel sunucuyu ayağa kaldırabilir ve tarayıcım üzerinden 8080 portu ile yapay zekâ ile etkileşime geçebilirim.

- **Kimin için:** Yerel donanımında yüksek verimli yapay zekâ modellerini çalıştırmak isteyen geliştiriciler için uygundur. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/PrismML-Eng/Bonsai-demo)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-17 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Machine Learning Shell Token Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/bonsai-demo/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
