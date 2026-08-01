# Dev yapay zekâ modellerini 4GB VRAM ile çalıştırın

AirLLM, 70 milyar parametreli büyük dil modellerinin (large language models) yalnızca 4 GB video belleğine (VRAM) sahip grafik işlem birimlerinde çalıştırılmasına olanak tanıyor. Bu kütüphane, bellek optimizasyonu tekniklerini kullanarak yüksek kapasiteli modellerin düşük donanım gereksinimleriyle kullanılmasını sağlıyor.

- ★ 19.113
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Ne kazandırır?
- 70B parametreli modelleri 4GB VRAM ile çalıştırma imkanı.
- 405B Llama3.1 modellerini 8GB VRAM üzerinde kullanabilme.
- Blok tabanlı sıkıştırma ile 3 kata kadar hız artışı.

## Kurulum

**Paket kurulumu**

```
pip install airllm
```

## Çalıştırma

**Modeli yükleme ve çalıştırma**

```
from airllm import AutoModel

MAX_LENGTH = 128
# could use hugging face model repo id:
model = AutoModel.from_pretrained("garage-bAInd/Platypus2-70B-instruct")

# or use model's local path...
#model = AutoModel.from_pretrained("/home/ubuntu/.cache/huggingface/hub/models--garage-bAInd--Platypus2-70B-instruct/snapshots/b585e74bcaae02e52665d9ac6d23f4d0dbc81a0f")

input_text = [
'What is the capital of United States?',
#'I like',
]

input_tokens = model.tokenizer(input_text,
return_tensors="pt", 
return_attention_mask=False, 
truncation=True, 
max_length=MAX_LENGTH, 
padding=False)

generation_output = model.generate(
input_tokens['input_ids'].cuda(), 
max_new_tokens=20,
use_cache=True,
return_dict_in_generate=True)

output = model.tokenizer.decode(generation_output.sequences[0])

print(output)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
AirLLM kütüphanesini kullanarak 70B parametreli bir modeli düşük VRAM kapasitesine sahip ekran kartımda çalıştırmak istiyorum. Kurulum için pip install airllm komutunu kullandım. Modelimi yüklemek ve basit bir metin girdisiyle çıktı almak için gerekli olan Python kod yapısını, AutoModel sınıfını kullanarak nasıl oluşturabilirim? İşlem sırasında disk alanımın yeterli olduğundan emin olmam gerektiğini biliyorum, süreci başlatmak için izlemem gereken temel adımları açıklar mısın?

- **Kimin için:** Sınırlı donanım kaynaklarına sahip olup yüksek kapasiteli büyük dil modellerini yerel olarak çalıştırmak isteyen kullanıcılar içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/lyogavin/airllm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: yıldız, sayılar ve metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
VRAM Jupyter Notebooks Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/airllm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
