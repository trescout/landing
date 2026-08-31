# Yapay zekâ trafiğini yöneten yönlendirici

NVIDIA tarafından geliştirilen Switchyard, Rust diliyle yazılmış yüksek performanslı bir yapay zekâ çıkarım (inference) motoru. Büyük dil modellerini (LLM) farklı donanım altyapılarında verimli şekilde çalıştırmak için optimize edilmiş bir çalışma zamanı (runtime) ortamı sunuyor.

- ★ 2.617
- Rust
- GitHub Trending · 2026-08-13

## Güncelleme
- 31 Ağustos 2026: Yıldız 1.566 → 2.617, son sürüm v0.2.0 (10 Ağustos 2026).
- 15 Ağustos 2026: Yıldız 923 → 1.566, son sürüm v0.2.0 (10 Ağustos 2026).

## Ne kazandırır?
- Farklı yapay zekâ modelleri arasında trafik yönlendirme
- OpenAI ve Anthropic API formatları arası çeviri
- İşlem metriklerini ve hata kayıtlarını takip etme

## Kurulum

**Komut satırı aracı olarak kurulum**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv tool install --python 3.10 "nemo-switchyard[cli]"
```

**Sunucu olarak kurulum**

```
cargo install --locked switchyard-server
switchyard-server --help
```

## Çalıştırma

**Sunucu durumunu kontrol etme**

```
curl http://localhost:4000/health
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Benim için bir yapay zekâ trafik yönlendiricisi olarak hareket et. Switchyard kullanarak Claude Code veya Codex gibi kodlama ajanlarımın isteklerini farklı modeller arasında dağıtmanı, OpenAI ve Anthropic API formatları arasında otomatik çeviri yapmanı ve tüm operasyonel metrikleri izlemeni istiyorum. Gelen istekleri yapılandırılmış yönlendirme algoritmalarıyla yönet ve gerektiğinde farklı modeller arasında A/B testi veya yük dengeleme yap.

- **Kimin için:** Büyük dil modellerini farklı donanım ve servis sağlayıcılar üzerinden verimli şekilde yönetmek isteyen geliştiriciler içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/NVIDIA-NeMo/Switchyard)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Inference Runtime LLM API Rust Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/switchyard/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
