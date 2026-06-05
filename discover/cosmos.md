# Cosmos

NVIDIA tarafından geliştirilen Cosmos, robotlar ve otonom araçlar gibi fiziksel sistemler için dünya modelleri (world models), veri setleri ve araçlar sunan açık bir platformdur. Geliştiricilerin fiziksel yapay zekâ (physical AI) uygulamaları oluşturmasını kolaylaştıran bir altyapı sağlar.

- ★ 9.173
- Jupyter Notebook
- GitHub Trending · 2026-06-05

## Ne kazandırır?
- Fiziksel yapay zekâ uygulamaları için dünya modelleri, veri setleri ve araçlar sunar.
- Metin, görsel, ses ve eylem dizilerini birleşik bir mimaride işleyip üretebilir.
- Robotik ve otonom sistemler için tahminleme, planlama ve simülasyon yetenekleri sağlar.

## Kurulum

**vLLM-Omni ile Kurulum**

```
uv pip install --torch-backend=cu130 \
"vllm-omni @ git+https://github.com/vllm-project/vllm-omni.git@main"
```

## Çalıştırma

**Video Üretimi**

```
curl -sS -X POST http://localhost:8000/v1/videos/sync \
--form-string "prompt=A small warehouse robot moves a blue box across a clean floor." \
--form-string 'extra_params={"guardrails":false,"use_resolution_template":false,"use_duration_template":false}' \
-o cosmos3_t2v.mp4
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
NVIDIA Cosmos platformunu kullanarak fiziksel yapay zekâ uygulamaları geliştirmek istiyorum. Cosmos 3 model ailesinin sunduğu yetenekleri, özellikle 'Reasoner' ve 'Generator' yüzeylerinin kullanım farklarını, bu modellerin robotik ve otonom sistemlerdeki görev planlama veya dünya simülasyonu gibi senaryolarda nasıl yapılandırılacağını teknik detaylarıyla açıkla. Ayrıca, kurulum aşamasında 'uv' aracı ve 'vllm-omni' kütüphanesi ile çalışma süreçlerini, CUDA sürücü gereksinimlerini göz önünde bulundurarak adım adım özetle.

- **Kimin için:** Fiziksel yapay zekâ, robotik sistemler ve otonom araçlar üzerine çalışan, dünya modelleri ve çok modlu veri işleme süreçleriyle ilgilenen geliştiriciler içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/NVIDIA/cosmos)

## İlgili sözlük terimleri
Physical AI World Models Jupyter Notebooks Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/cosmos/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
