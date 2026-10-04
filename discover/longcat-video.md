# Uzun videoları tutarlı şekilde oluşturun

Meituan tarafından geliştirilen LongCat-Video, uzun videoları tutarlı bir şekilde oluşturmak için kullanılan bir video üretim çerçevesi (framework). Bu araç, görüntü tutarlılığını koruyarak daha uzun süreli ve yüksek kaliteli video içerikleri üretmeyi sağlıyor.

- ★ 8.892
- Python
- GitHub Trending · 2026-10-04

## Ne kazandırır?
- Metinden, görselden veya mevcut videolardan uzun süreli yeni içerikler üretebilirsiniz.
- Dakikalar süren videolarda renk kayması ve kalite düşüşü olmadan çıktı alabilirsiniz.
- Ses dosyalarını kullanarak sesle uyumlu karakter animasyonları oluşturabilirsiniz.

## Kurulum

**Kod deposunu bilgisayara indirme**

```
git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video
cd LongCat-Video
```

**Model ağırlıklarını indirme**

```
pip install "huggingface_hub[cli]"
huggingface-cli download meituan-longcat/LongCat-Video --local-dir ./weights/LongCat-Video
huggingface-cli download meituan-longcat/LongCat-Video-Avatar --local-dir ./weights/LongCat-Video-Avatar
huggingface-cli download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ./weights/LongCat-Video-Avatar-1.5
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
LongCat-Video projesini sistemime kurmak istiyorum. Lütfen 'git clone --single-branch --branch main https://github.com/meituan-longcat/LongCat-Video' ve 'cd LongCat-Video' komutlarıyla kaynak kodları indirmem, ardından model kütüphanesi Hugging Face üzerinden gerekli dosyalara ulaşmak için 'pip install "huggingface_hub[cli]"' ile indirme komutlarını adım adım çalıştırmam konusunda bana rehberlik edin.

- **Kimin için:** Yapay zekâ yardımıyla metin, görsel veya ses girdilerinden yüksek kaliteli ve uzun süreli videolar üretmek isteyen geliştiriciler ve içerik üreticileri içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/meituan-longcat/LongCat-Video)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-10-04 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Clone Framework Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/longcat-video/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
