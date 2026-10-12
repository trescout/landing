# İşlemcide verimli yapay zekâ çıkarımı

Microsoft tarafından geliştirilen BitNet, 1-bit büyük dil modelleri (LLMs) için resmi bir çıkarım çerçevesi (inference framework) sunuyor. C++ diliyle yazılan bu araç, düşük bit hassasiyetli modellerin çalıştırılmasını optimize etmeyi hedefliyor.

- ★ 40.731
- C++
- GitHub Trending · 2026-10-12

## Ne kazandırır?

- Standart bilgisayar işlemcilerinde yapay zekâ modellerini yüksek hız ve düşük enerji tüketimiyle çalıştırır.
- Sıkıştırılmış 1-bit dil modellerini kalite kaybı yaşamadan yerel cihazınızda kullanmanızı sağlar.
- Diyalog modu desteği sayesinde indirilen modellerle doğrudan sohbet etme imkânı sunar.

## Kurulum

**Kaynak kodları indirin**

```
git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet
```

**Ortamı hazırlayın ve bağımlılıkları yükl**

```
# (Recommended) Create a new conda environment
conda create -n bitnet-cpp python=3.10
conda activate bitnet-cpp

pip install -r requirements.txt
```

## Çalıştırma

**Modeli indirin ve ortamı yapılandırın**

```
# Manually download the model and run with local path
huggingface-cli download microsoft/BitNet-b1.58-2B-4T-gguf --local-dir models/BitNet-b1.58-2B-4T
python setup_env.py -md models/BitNet-b1.58-2B-4T -q i2_s
```

**Modeli sohbet modunda çalıştırın**

```
# Run inference with the quantized model
python run_inference.py -m models/BitNet-b1.58-2B-4T/ggml-model-i2_s.gguf -p "You are a helpful assistant" -cnv
```

## Kod bilmiyorsanız

🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Bilgisayarımda BitNet altyapısını kullanarak 1-bit yapay zekâ modelini çalıştırmak istiyorum. Öncelikle 'git clone --recursive https://github.com/microsoft/BitNet.git' komutuyla projeyi klonlayıp klasörüne girme, paket yöneticisi Conda ile Python 3.10 ortamı açıp gereksinimleri kurma adımlarında bana rehberlik et. Ardından açık kaynak model platformu Hugging Face üzerinden microsoft/BitNet-b1.58-2B-4T-gguf modelini indirip 'setup_env.py' ile hazırlama ve son olarak 'run_inference.py' betiğiyle sohbet modunu başlatma adımlarını kodlama bilmeyen birinin anlayacağı sadelikte, adım adım açıkla.

- **Kimin için:** Güçlü ekran kartlarına ihtiyaç duymadan, kendi bilgisayar işlemcisinde hızlı ve hafif dil modelleri çalıştırmak isteyen kullanıcılar içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/microsoft/BitNet)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-12 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Inference Framework](https://trescout.com/dictionary/inference-framework/)
- [Inference](https://trescout.com/dictionary/inference/)
- [Clone](https://trescout.com/dictionary/clone/)
- [Framework](https://trescout.com/dictionary/framework/)
- [Open Source](https://trescout.com/dictionary/open-source/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/bitnet/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
