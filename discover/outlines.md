# yapay zekâ çıktılarını yapılandırın

Outlines kütüphanesi, büyük dil modellerinden gelen yanıtları önceden tanımlanmış şemalara göre yapılandırılmış çıktılar (structured outputs) halinde sunulmasını sağlıyor. Geliştiriciler, Python tabanlı bu araçla model çıktılarını düzenli ifadeler (regular expressions) veya bağlamsız dil bilgisi (context-free grammars) kurallarıyla kısıtlayarak veri bütünlüğünü koruyor.

- ★ 14.917
- Python
- GitHub Trending · 2026-07-22

## Ne kazandırır?
- Model çıktılarını önceden tanımlanmış şemalara göre kısıtlar
- JSON veya Python veri tipleriyle tam uyum sağlar
- Hatalı çıktıları ayıklama ihtiyacını ortadan kaldırır

## Kurulum

**Kütüphaneyi yükleyin**

```
pip install outlines
```

## Çalıştırma

**Modeli bağlayın**

```
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
AutoTokenizer.from_pretrained(MODEL_NAME)
)
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Outlines kütüphanesini kullanarak bir yapay zekâ modelinden gelen yanıtı belirli bir Pydantic veri yapısına veya Python tipine (örneğin int veya Literal) göre kısıtlamak istiyorum. Modelin çıktısının her zaman istediğim şemaya uygun olmasını sağlamak için model nesnesini tanımladıktan sonra model(istem, çıktı_tipi) fonksiyonunu nasıl kullanabilirim? Lütfen karmaşık nesneler için Pydantic modelini nasıl tanımlayacağımı ve bu yapıyı model çıktısına nasıl uygulayacağımı örnekle açıkla.

- **Kimin için:** Yapay zekâ modellerinden gelen düzensiz metin çıktılarını, yazılım süreçlerinde doğrudan kullanılabilecek yapılandırılmış verilere dönüştürmek isteyen geliştiriciler içindir. 
- **Lisans:** Apache-2.0 

## Bağlantılar
- [GitHub deposu →](https://github.com/dottxt-ai/outlines)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Bu sayfa deponun 2026-07-22 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri
Artificial Intelligence

---
Kaynak: TreScout Keşif · https://trescout.com/discover/outlines/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
