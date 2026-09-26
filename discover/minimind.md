# Sıfırdan iki saatte eğitilen 64M parametreli dil modeli

MiniMind, büyük dil modellerinin (LLM) çalışma prensiplerini anlamak isteyen geliştiriciler için tokenizasyon, ön eğitim, gözetimli ince ayar (SFT), LoRA ve DPO aşamalarını yalın PyTorch kodlarıyla sunar.

- ★ 55.708
- Python
- GitHub Trending · 2026-08-31

## Güncelleme
- 31 Ağustos 2026: Yıldız 55.708, MoE (Mixture of Experts) mimarisi ve DPO pekiştirmeli hizalama desteği.

## Ne kazandırır?
- Tüketici donanımında 2 saatte eğitim: Tek bir NVIDIA RTX 3090/4090 ekran kartında yaklaşık 2 saatte sıfırdan eğitilebilen kompakt mimari.
- Tam LLM eğitim yaşam döngüsü: BPE tokenizasyon, pretraining, gözetimli ince ayar (SFT), LoRA adaptasyonu ve DPO hizalama boru hattı.
- Minimalist ve okunabilir kod tabanı: Karmaşık üçüncü taraf soyutlamaları olmadan saf PyTorch ile yazılmış şeffaf Transformer blokları.
- MoE (Uzman Karışımı) desteği: Dense modellerin yanı sıra 8x MoE mimarisini sıfırdan deneme ve çalıştırma olanağı.
- Mükemmel eğitim ve pedagoji kaynağı: Büyük dil modellerinin iç işleyişini deneysel olarak kavramak isteyen araştırmacılar için ideal kılavuz.

## Kurulum

**Depoyu klonlama ve bağımlılıkları yükleme**

```
git clone https://github.com/jingyaogong/minimind.git
cd minimind
pip install -r requirements.txt
```

## Çalıştırma

**Ön eğitim başlatma ve model çıktısını test etme**

```
python 1-pretrain.py
# Eğitilen modelle test çıkarımı:
python 5-eval.py
```

## Teknik mimari ve çalışma prensibi

MiniMind, LLaMA ve Mistral benzeri modern oto-regresif Decoder-Only Transformer mimarisini temel alır:
- RoPE ve SwiGLU Aktivasyonları: Dönel konumsal gömmeler (Rotary Position Embeddings) ve SwiGLU aktivasyon fonksiyonları ile modern mimari standartları.
- RMSNorm ile Kararlı Gradyan Akışı: Geleneksel LayerNorm yerine daha hızlı ve kararlı olan RMSNorm katman normalizasyonu kullanımı.
- Flash Attention Entegrasyonu: Büyük dikkat matrislerini GPU belleğinde hızlıca hesaplamak için Flash Attention v2 optimizasyonu.

## Eğitim aşamaları: Ön eğitim, SFT ve DPO

MiniMind'ın modüler yapısı, bir dil modelinin ham metinden diyaloğa dönüşümünü adım adım görselleştirir:
- Aşama 1 - Ön Eğitim (1-pretrain.py): Ham metinler üzerinde bir sonraki tokeni tahmin etme mantığıyla dilbilgisi ve genel dünya bilgisini öğrenir.
- Aşama 2 - Gözetimli İnce Ayar (2-sft.py): Soru-cevap ve talimat veri kümeleri ile modeli kullanıcı komutlarına itaat eden bir asistana dönüştürür.
- Aşama 3 - DPO Hizalama (4-dpo.py): İyi ve kötü yanıt çiftleri üzerinden modeli kullanıcı tercihlerine göre doğrudan optimize eder.

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
MiniMind deposunu kullanarak PyTorch ile sıfırdan 64M parametreli bir dil modeli eğitmek istiyorum. Kendi Türkçe metin veri kümeme göre tokenizer'ı nasıl hazırlayacağımı, 1-pretrain.py betiğini nasıl çalıştıracağımı ve ardından LoRA ile nasıl ince ayar yapacağımı adım adım açıklar mısın?

- **Kimin için:** Yapay zekâ araştırmacıları, makine öğrenimi mühendisleri, veri bilimciler ve öğrenciler. 
- **Lisans:** Apache-2.0 (Açık kaynak lisansı) 
- **Çatı:** PyTorch Tabanlı Minimalist LLM Çatısı 
- **Platformlar:** Linux, macOS (Apple Silicon MPS), Windows 

## Sıkça sorulan sorular
- MiniMind'ı eğitmek için ne kadar VRAM gerekir? 64M parametreli model, batch size ayarına bağlı olarak 6GB ile 12GB VRAM aralığında rahatça eğitilebilir; RTX 3060 veya RTX 4060 bile yeterlidir.
- Apple Silicon (Mac M serisi) üzerinde çalışır mı? Evet. PyTorch MPS (Metal Performance Shaders) hızlandırması ile Mac bilgisayarlarda da eğitim ve çıkarım yapılabilir.
- Modelin çıktıları günlük konuşma için yeterli mi? 64M küçük bir modeldir; karmaşık mantıksal akıl yürütme yerine dil yapısını, temel soruları yanıtlama ve metin tamamlama yeteneklerini sergilemek için optimize edilmiştir.
- Hangi veri kümeleri hazır olarak geliyor? Depo, Çince ve İngilizce ön eğitim ve SFT için filtrelenmiş açık veri kümelerini otomatik indirme komutları sunar.

## Bağlantılar
- [GitHub deposu →](https://github.com/jingyaogong/minimind)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-08-31 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Yapay Zekâ LLM Açık Kaynak Makine Öğrenimi CLI

---
Kaynak: TreScout Keşif · https://trescout.com/discover/minimind/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
