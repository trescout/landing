# yapay zekâ modellerini otonom test edin

SIA, yapay zekâ modellerinin ve ajanların belirli kıyaslama görevlerindeki (benchmark tasks) performanslarını otonom şekilde artırmak için geliştirilen bir öz-iyileştiren yapay zekâ (self-improving AI) çerçevesidir. Python tabanlı bu sistem, yapay zekâ sistemlerinin kendi çıktılarını analiz ederek süreçlerini optimize etmesini sağlar.

- ★ 1.478
- Python
- GitHub Trending · 2026-06-12

## Ne kazandırır?
- Yapay zeka modellerinin görev performansını otonom şekilde artırır.
- Meta, hedef ve geri bildirim ajanları arasında döngüsel iyileştirme sağlar.
- Benchmark görevlerinde yüksek doğruluk ve işlem hızı verimliliği sunar.

## Kurulum

**Claude Modelleri ile Kurulum**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[claude]'
export ANTHROPIC_API_KEY="..."
```

**Çoklu Sağlayıcı (OpenHands) ile Kurulum**

```
python3 -m venv .venv && source .venv/bin/activate
pip install 'sia-agent[openhands]'

# Export the key(s) for the provider(s) you'll use:
export ANTHROPIC_API_KEY="..." # for anthropic/* models
export GEMINI_API_KEY="..." # for gemini/* models (or GOOGLE_API_KEY)
export OPENAI_API_KEY="..." # for openai/* models
```

## Çalıştırma

**Öz-İyileştirme Döngüsünü Başlatma**

```
sia run --task gpqa --max_gen 5 --run_id 1
```

**Görselleştirme Paneli**

```
sia web
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
SIA çerçevesini kullanarak bir yapay zeka ajanının performansını artırmak istiyorum. Kurulumu tamamladıktan sonra, mevcut görevlerden birini seçerek (örneğin gpqa) öz-iyileştirme döngüsünü başlatmak için hangi komutu kullanmalıyım ve süreç sonunda oluşan çıktıları (target_agent.py, agent_execution.json, improvement.md) nasıl yorumlamalıyım? Ayrıca, kendi özel görev dizinimi sisteme nasıl dahil edebilirim?

- **Kimin için:** Yapay zeka modellerinin performansını otonom iyileştirme süreçleriyle optimize etmek isteyen geliştiriciler ve araştırmacılar için uygundur. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/hexo-ai/sia)

## İlgili sözlük terimleri
Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/sia/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
