# Yerel sistemde yapay zekâ ile video üretimi

Lightricks tarafından geliştirilen LTX-2, ses ve video üreten yapay zekâ modelleri için Python çıkarım (inference) ve düşük dereceli uyarlama (low-rank adaptation, LoRA) eğitim paketi sunuyor. Bu araç seti, kullanıcıların LTX-2 modellerini kendi verileriyle eğitmesine ve model çıktılarını yerel sistemlerde çalıştırmasına olanak tanıyor.

- ★ 8.587
- GitHub Trending · 2026-06-19

## Güncelleme
- 12 Ağustos 2026: Yıldız 8.554 → 8.587, son sürüm v1.2.0 (11 Ağustos 2026).
- 10 Ağustos 2026: Yıldız 7.550 → 8.554.

## Ne kazandırır?
- Ses ve video senkronizasyonu sağlar
- Kendi verilerinizle LoRA eğitimi yapabilirsiniz
- Yerel sistemde yüksek kaliteli video üretimi

## Kurulum

**GitHub'dan depoyu klonla ve dizine gir**

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
```

**Model ağırlıklarını indirin (Hugging Face CLI)**

```
hf download Lightricks/LTX-2.3 ltx-2.3-22b-distilled-1.1.safetensors --local-dir models/ltx-2.3
```

## Çalıştırma

**uv ile çıkarım (inference) boru hattını çalıştır**

```
uv run python -m ltx_pipelines.distilled --distilled-checkpoint-path models/ltx-2.3/ltx-2.3-22b-distilled-1.1.safetensors
```

Kaynak: Resmî LTX-2 README (Lightricks/LTX-2)

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Lütfen LTX-2 modelini kullanarak, istediğim sahneyi detaylı bir şekilde betimleyen ve ses ile video senkronizasyonunu içeren bir video oluştur. Sahne detaylarını, karakterin görünümünü, kamera açısını ve konuşma metnini belirterek modelin çıktı üretmesini sağla.

- **Kimin için:** Kendi yerel sisteminde sesli ve görüntülü yapay zekâ videoları oluşturmak veya modelleri eğitmek isteyen kullanıcılar içindir. 

## Bağlantılar
- [GitHub deposu →](https://github.com/Lightricks/LTX-2)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-19 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
LoRA Inference CLI Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ltx-2/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
