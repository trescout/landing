# Whichllm

Whichllm, donanımınız üzerinde en yüksek performansı gösteren yerel büyük dil modellerini (large language models) belirlemenizi sağlayan bir araçtır. Parametre sayısından ziyade güncel kıyaslama testlerine (benchmarks) odaklanan bu Python tabanlı yazılım, tek komutla en uygun modeli seçmenize olanak tanır.

- ★ 3.679
- Python
- GitHub Trending · 2026-06-09

## Ne kazandırır?
- Donanımınıza en uygun yerel dil modelini güncel kıyaslama verileriyle belirler.
- GPU ve sistem özelliklerini otomatik algılayarak performans tahmini yapar.
- Tek komutla model indirme, sohbet başlatma ve Python kod örneği oluşturma imkanı sunar.

## Kurulum

**Araç kurulumu**

```
uv tool install whichllm
uv tool upgrade whichllm # update an existing install
```

**Alternatif kurulum yöntemleri**

```
brew install andyyyy64/whichllm/whichllm
pip install whichllm
```

## Çalıştırma

**Donanımınıza en uygun modelleri listelem**

```
whichllm
```

**Belirli bir model ile sohbet başlatma**

```
whichllm run "qwen 2.5 1.5b gguf"
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Whichllm aracını kullanarak donanım özelliklerime en uygun yerel büyük dil modellerini listelemek ve bu modellerin performans tahminlerini görmek istiyorum. Sistemimdeki GPU veya CPU kapasitesine göre en yüksek benchmark puanına sahip modelleri nasıl filtreleyebilirim, ayrıca belirli bir model için gerekli olan donanım planlamasını nasıl yapabilirim?

- **Kimin için:** Kendi donanımı üzerinde en verimli şekilde çalışacak yerel yapay zeka modellerini arayan ve teknik karmaşadan uzak durmak isteyen kullanıcılar içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/Andyyyy64/whichllm)

## İlgili sözlük terimleri
Benchmarks Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/whichllm/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
