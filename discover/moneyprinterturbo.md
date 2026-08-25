# Tek tuşla yapay zekâ videoları üretin

MoneyPrinterTurbo , verdiğiniz bir konu veya anahtar kelimeden büyük dil modellerini kullanarak otomatik kısa videolar üretir. Metin, altyazı, arka plan müziği ve görselleri birleştirir. (İsim pazarlama amaçlıdır, bir 'para basma' makinesi değil, içerik üretim aracıdır.)

_Görsel: MoneyPrinterTurbo (proje deposundan)_

- ★ 114.747
- Python
- MIT
- GitHub Trending · 28 May 2026

## Güncelleme
- 23 Ağustos 2026: Yıldız 108.989 → 114.747, son sürüm v1.3.5 (22 Ağustos 2026).
- 19 Ağustos 2026: Yıldız 102.680 → 108.989, son sürüm v1.3.4 (12 Ağustos 2026).
- 12 Ağustos 2026: Yıldız 101.070 → 102.680, son sürüm v1.3.4 (12 Ağustos 2026).
- 2 Ağustos 2026: Yıldız 62.104 → 101.070, son sürüm v1.3.3 (24 Temmuz 2026).

- **Kimin için:** Kısa video / içerik üretenler 
- **Zorluk:** Orta · kurulum + AI API anahtarı gerekir 
- **Ne sunar:** Konudan otomatik kısa video 
- **Ön koşul:** Bir LLM API anahtarı (OpenAI/Claude/Gemini…) 
- **Ücret:** Ücretsiz · açık kaynak (MIT) · API maliyeti ayrı 

## Ne kazandırır?
- Metin, altyazı, müzik ve görsel kullanarak otomatik kurgu oluşturur.
- Web arayüzü sayesinde kullanımı kolaydır.
- Toplu ve çoklu video üretimine olanak tanır.

## Dürüst not

Çalışması için bir AI model API anahtarı + kurulum gerekir; API kullanımı ücretli olabilir. Üretilen videoların telif ve platform kurallarına uygunluğu kullanıcının sorumluluğundadır.

## Nasıl kurulur, nasıl kullanılır?
🤖 Kod bilmiyorsanız · yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
MoneyPrinterTurbo'yu kur ve çalıştır: 'git clone https://github.com/harry0703/MoneyPrinterTurbo.git' ile depoyu indir, dizine girip 'docker-compose up' komutuyla başlat, sonra tarayıcıdan http://127.0.0.1:8501 adresindeki web arayüzünü aç.

**Depoyu klonla**

```
git clone https://github.com/harry0703/MoneyPrinterTurbo.git
```

**Docker ile başlat**

```
cd MoneyPrinterTurbo
docker-compose up
```

**Web arayüzünü çalıştır (uv ile)**

```
uv run streamlit run ./webui/Main.py --browser.gatherUsageStats=False
```

Lisans: MIT · özgürce kullanabilir, değiştirebilir, ticari kullanabilirsiniz.

## Bağlantılar
- [GitHub deposu →](https://github.com/harry0703/MoneyPrinterTurbo)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun keşif tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Clone LLM API Open Source Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/moneyprinterturbo/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
