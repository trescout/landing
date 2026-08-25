# Doğal ve Akıcı Sesler Üretin

MOSS-TTS (MOSI.AI ve OpenMOSS); yüksek sadakatli konuşma ve ses üretimi sağlayan açık kaynak bir model ailesidir. Uzun metinli konuşma sentezi, çoklu konuşmacı desteği ve gerçek zamanlı akış gibi senaryolar için çözümler sunar.

_Görsel: MOSS-TTS (proje deposundan)_

- ★ 3.939
- Python
- Apache-2.0
- GitHub Trending · 29 May 2026

## Güncelleme
- 2 Ağustos 2026: Yıldız 2.440 → 3.939.

- **Kimin için:** TTS/ses üretimi yapan geliştiriciler, araştırmacılar 
- **Zorluk:** İleri · ML/model bilgisi 
- **Ne sunar:** Açık kaynak TTS model ailesi 
- **Özellik:** Uzun metin, çoklu konuşmacı, gerçek zamanlı akış 
- **Ücret:** Ücretsiz · açık kaynak (Apache-2.0) 

## Ne sunar?
- Yüksek doğrulukta konuşma ve ses sentezi sağlar.
- Çoklu konuşmacı desteği sunar.
- Gerçek zamanlı ses akışı (streaming) destekler.
- Açık kaynaklı model ailesine dayanır.

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
MOSS-TTS ses üretim modelini kur: 'git clone https://github.com/OpenMOSS/MOSS-TTS.git' ile depoyu indir, içine girip bağımlılıkları kur, sonra 'python clis/moss_tts_app.py' ile Gradio arayüzünü açıp metinden konuşma üret.

**Conda ortamı oluştur**

```
conda create -n moss-tts python=3.12 -y
conda activate moss-tts
```

**Depoyu klonla ve kur**

```
git clone https://github.com/OpenMOSS/MOSS-TTS.git
cd MOSS-TTS
pip install --extra-index-url https://download.pytorch.org/whl/cu128 -e ".[torch-runtime]"
```

**Gradio demosunu çalıştır**

```
python clis/moss_tts_app.py
```

Lisans: Apache-2.0 · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz (patent koruması da içerir). Model çıktısı için ilgili model kartını da inceleyin.

## Bağlantılar
- [GitHub deposu →](https://github.com/OpenMOSS/MOSS-TTS)
- [MOSI.AI →](https://mosi.cn)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Text-to-Speech Clone Open Source Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/moss-tts/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
