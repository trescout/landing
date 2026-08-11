# Yerel donanımda DeepSeek çalıştırma motoru

Redis'in yaratıcısı Salvatore Sanfilippo tarafından geliştirilen ds4, DeepSeek modellerini yerel donanımlar üzerinde çalıştırmayı sağlayan bir çıkarım motoru (inference engine). C diliyle yazılan bu araç, Metal, CUDA ve ROCm desteği sayesinde farklı grafik işlemcilerinde yüksek performanslı model çalıştırma imkânı sunuyor.

- ★ 21.134
- C
- GitHub Trending · 2026-08-03

## Güncelleme
- 11 Ağustos 2026: Yıldız 20.117 → 21.134.

## Ne kazandırır?
- Tüketici sınıfı donanımlarda yüksek performanslı yapay zekâ modelleri çalıştırır
- SSD üzerinden veri akışı sağlayarak kısıtlı bellek kapasitesinde bile model kullanımı sunar
- Çoklu grafik işlemci desteğiyle kurumsal seviyede LLM sunucusu oluşturmaya olanak tanır

## Kurulum

**Donanımınıza uygun derleme**

```
make # macOS Metal
make cuda-spark # Linux CUDA, DGX Spark / GB10
make cuda-generic # Linux CUDA, other local CUDA GPUs
make strix-halo # Linux ROCm, AMD Strix Halo
make cpu # CPU-only diagnostics build
```

**Modeli indirme**

```
./download_model.sh q2-imatrix # 96/128 GB RAM machines, imatrix-tuned q2
./download_model.sh q2-q4-imatrix # 96/128 GB RAM machines, q2 with last 6 layers q4
./download_model.sh q4-imatrix # >= 256 GB RAM machines, imatrix-tuned q4
./download_model.sh pro-q2-imatrix # 512 GB RAM machines, PRO q2 imatrix quant
```

## Çalıştırma

**Modeli başlatma**

```
./download_model.sh q2-imatrix

./ds4 \
-m ./ds4flash.gguf \
--ssd-streaming \
--ssd-streaming-cache-experts 32GB \
--ctx 32768 \
--nothink
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Benim sistemimdeki donanım özelliklerine göre en uygun DeepSeek veya GLM modelini seçmemde yardımcı ol. Hangi indirme komutunu kullanmalıyım ve SSD üzerinden veri akışı (streaming) özelliğini aktif ederek bellek darboğazını nasıl aşabilirim? Ayrıca, kurduğum bu yapay zekâ sistemini yerel bir sunucu olarak kullanabilmem için gerekli temel yapılandırma ayarlarını açıkla.

- **Kimin için:** Yüksek performanslı yapay zekâ modellerini kendi yerel donanımı üzerinde çalıştırmak isteyen yazılımcılar ve sistem yöneticileri içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/antirez/ds4)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-03 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Inference Engine Inference LLM Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ds4/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
