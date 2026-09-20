# Dev yapay zekâ modellerini 4GB VRAM ile çalıştırın

AirLLM, 70 milyar ve 405 milyar parametreli dev büyük dil modellerini (LLM) kurumsal sunuculara veya pahalı GPU kümelerine ihtiyaç duymadan, yalnızca 4 GB video belleğine (VRAM) sahip standart tüketici sınıfı ekran kartlarında çalıştıran çığır açıcı bir açık kaynak kütüphanedir.

- ★ 33.755
- Jupyter Notebook
- GitHub Trending · 2026-06-04

## Güncelleme
- 6 Eylül 2026: Yıldız 33.307 → 33.755, son sürüm v4.0.0 (5 Eylül 2026).
- 31 Ağustos 2026: Yıldız 31.598 → 33.307, son sürüm v3.3.0 (28 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 30.796 → 31.598, son sürüm v3.2.0 (18 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 29.265 → 30.796, son sürüm v3.1.0 (29 Temmuz 2026).

## Ne kazandırır?
- 70B modelleri 4GB VRAM ile yürütme: Llama 3 70B, Qwen veya DeepSeek gibi yüksek parametreli modelleri giriş seviyesi GTX 1650 veya RTX 3050 ekran kartlarında dahi açabilme gücü.
- 405B Llama 3.1 desteği: Veri merkezlerinde yüz binlerce dolarlık GPU kümesi gerektiren 405 milyar parametreli modelleri 8GB VRAM'li kişisel bilgisayarlarda çalıştırabilme.
- Katman bazlı bellek döngüsü (Layer-wise Execution): Modelin tamamını VRAM'e sığdırmak yerine, katmanları diskten sırayla belleğe alıp işleyerek VRAM darboğazını aşar.
- Blok tabanlı sıkıştırma ile 3 kata kadar hız: NVMe SSD üzerindeki model ağırlıklarını optimize edilmiş bloklar halinde okuyarak diskten GPU'ya veri aktarımını hızlandırır.
- Kuantizasyon kalitesi kaybı olmadan tam hassasiyet: Ağırlıkları 4-bit'e sıkıştırma zorunluluğu olmadan, istenirse orijinal 16-bit (bfloat16) hassasiyetinde bile akıl yürütme imkanı sağlar.

## Kurulum

**pip ile (PyPI)**

```
pip install airllm
```

Kaynak: Resmî kaynak: https://github.com/lyogavin/airllm

## Teknik mimari ve çalışma prensibi

Geleneksel LLM çıkarım motorları (vLLM, Ollama veya HuggingFace) modelin tüm ağırlıklarının aynı anda GPU video belleğinde (VRAM) bulunmasını şart koşar. 70 milyar parametreli bir model 16-bit hassasiyette yaklaşık 140 GB, 4-bit kuantize edilmiş halde ise en az 35-40 GB VRAM gerektirir. AirLLM bu temel paradigmayı kökten değiştirir:
- Transformer katmanlarının ardışık doğası: Bir Transformer ağı 80 bağımsız katmandan oluşur. Her katman bir önceki katmanın tensör çıktısını girdi olarak alır. Modelin tamamının bellekte durması teorik olarak zorunlu değildir.
- Katman katman akış (Sequential Offloading): AirLLM yalnızca o an hesaplanan tek bir katmanı VRAM'e taşır (yaklaşık 1.5 GB). İlgili katmanın ileri besleme (forward pass) hesabı bittiğinde bellek boşaltılır ve diskten sıradaki katman çekilir.
- Hız ve bellek takası (Trade-off): Bu mimari saniyede onlarca token üreten etkileşimli sohbetler için değil; toplu veri analizi, derin akıl yürütme, çeviri, sentetik veri üretimi ve model değerlendirme (evals) süreçleri için eşsiz bir tasarruf aracıdır.
- Hafıza eşlemeli dosya okuma (mmap): PyTorch tensörlerini diske doğrudan mmap yöntemiyle bağlayarak sistem RAM'ini gereksiz yere şişirmeden doğrudan NVMe SSD bant genişliğini kullanır.

## Örnek Python kullanımı

AirLLM, HuggingFace AutoModel API'sine çok benzer, son derece sade bir Python sözdizimine sahiptir:

**Python ile 70B Model Çalıştırma**

```
from airllm import AutoModel

# 70B modeli yalnizca 4GB VRAM ile baslatin
model = AutoModel.from_pretrained("meta-llama/Meta-Llama-3-70B-Instruct")

input_text = ["Turkiye'nin yapay zeka alanindaki potansiyelini ozetle."]
input_tokens = model.tokenizer(input_text, return_tensors="pt", padding=True)

# Cikti uretimi (katmanlar sirayla yurutulur)
generation_output = model.generate(
input_tokens['input_ids'].cuda(),
max_new_tokens=100,
use_cache=True,
return_dict_in_generate=True
)

output = model.tokenizer.decode(generation_output.sequences[0])
print(output)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
AirLLM kütüphanesini kullanarak 70 milyar parametreli bir modeli (örneğin meta-llama/Llama-3-70B-Instruct) 4GB VRAM kapasitesine sahip yerel ekran kartımda çalıştırmak istiyorum. Kurulum için pip install airllm komutunu kullandım. Modelimi yüklemek, metin girdisiyle çıktı almak ve bellek taşmasını önlemek için gerekli olan Python kodunu açıklar mısın? Süreçte disk alanımın yeterli olduğundan emin olmam gerektiğini biliyorum, izlemem gereken adımları detaylandırır mısın?

- **Kimin için:** Sınırlı donanım kaynaklarına sahip olup yüksek kapasiteli 70B ve 405B modellerini yerel olarak test etmek, veri madenciliği ve değerlendirme yapmak isteyen araştırmacılar içindir. 
- **Lisans:** Apache-2.0 (Geniş özgürlük sunan açık kaynak lisansı) 
- **Gereksinim:** Minimum 4 GB VRAM GPU ve yüksek hızlı NVMe SSD disk alanı 
- **Ekosistem:** Python, PyTorch ve HuggingFace Transformers 

## Sıkça sorulan sorular
- AirLLM ile model çalıştırmak ne kadar hızlıdır? AirLLM katmanları sürekli disk ile GPU arasında taşıdığı için token üretim hızı doğrudan NVMe SSD diskinizin okuma hızına bağlıdır. Tipik bir Gen4 SSD üzerinde 70B model saniyede 1-3 token hızında çalışır. Bu hız etkileşimli sohbet için yavaş olsa da, sıfır donanım maliyetiyle dev modelleri yerel olarak koşturmak için benzersizdir.
- AirLLM için ne kadar boş disk alanı gereklidir? 70B parametreli bir model 16-bit float formatında yaklaşık 140 GB disk alanı gerektirir. 4-bit kuantize edilmiş sürümlerde bu alan 35-40 GB seviyesine düşer. 405B modeli için ise en az 800 GB boş NVMe disk alanı ayrılmalıdır.
- Kuantizasyon yapmadan orijinal model ağırlıklarını kullanabilir miyim? Evet. AirLLM'in en büyük avantajlarından biri kuantizasyon mecburiyetini ortadan kaldırmasıdır. VRAM kısıtlaması katman bazında çözüldüğü için orijinal 16-bit ağırlıkları hiçbir akıl yürütme veya doğruluk kaybı yaşamadan çalıştırabilirsiniz.
- AirLLM Apple Silicon Mac veya sadece CPU üzerinde çalışır mı? AirLLM temel olarak CUDA (NVIDIA GPU) hızlandırması için optimize edilmiştir. Ancak deneysel olarak CPU yürütmesini ve MPS (Apple Silicon Metal) katmanlarını da desteklemektedir. En yüksek verim hızlı bir NVMe SSD ve NVIDIA ekran kartı ile elde edilir.

## Bağlantılar
- [GitHub deposu →](https://github.com/lyogavin/airllm)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-06-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
VRAM LLM Large Language Models Transformer Open Source

---
Kaynak: TreScout Keşif · https://trescout.com/discover/airllm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
