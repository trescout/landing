# Yerel yapay zekâ motoru TensorFold

ashhart/TensorFold, büyük dil modelleri (LLM) için Metal, CUDA ve Vulkan destekli bir çıkarım motoru (inference engine) sunuyor. Zig diliyle geliştirilen bu araç, Python veya MLX kurulumuna ihtiyaç duymadan Apple Silicon ve NVIDIA grafik işlemcileri üzerinde doğrudan model çalıştırmayı sağlıyor.

- ★ 1.998
- Zig
- GitHub Trending · 2026-11-13

## Güncelleme

- **13 Kasım 2026:** Yıldız 1.996 → 1.998, son sürüm v1.2.7 (11 Kasım 2026).

## Ne kazandırır?

- Apple Silicon ve NVIDIA grafik işlemcileri üzerinde büyük dil modellerini doğrudan çalıştırır.
- Python veya MLX kurulumuna ihtiyaç duymadan ikili dosya üzerinden hizmet verir.
- Yerel web uygulamasıyla modelleri seçmeyi ve sohbet etmeyi sağlar.

## Kurulum

**Mac ile Kurulum**

```
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

## Çalıştırma

**İstek Gönderme**

```
curl -fsS http://127.0.0.1:8080/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Apple Silicon çipine sahip Mac bilgisayarıma TensorFold aracını kurmak ve Qwen3.5-2B modelini indirip sunucuyu başlatmak istiyorum. Bunun için şu komutları sırasıyla çalıştırman gerekiyor:

brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking

Ardından sunucunun çalıştığını doğrulamak için şu komutla istek atabilirsin:

curl -fsS http://127.0.0.1:8080/v1/chat/completions \
-H 'Content-Type: application/json' \
-d '{"model":"local-model","messages":[{"role":"user","content":"Say hello in one sentence."}],"max_tokens":128,"temperature":0}'

Depo: https://github.com/ashhart/TensorFold. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Python kurmadan Apple Silicon veya NVIDIA grafik işlemcileri üzerinde büyük dil modelleri çalıştırmak isteyen geliştiriciler içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/ashhart/TensorFold)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-13 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Temperature](https://trescout.com/dictionary/temperature/)
- [Application](https://trescout.com/dictionary/application/)
- [Inference Engine](https://trescout.com/dictionary/inference-engine/)
- [Apple Silicon](https://trescout.com/dictionary/apple-silicon/)
- [Inference](https://trescout.com/dictionary/inference/)
- [LLM](https://trescout.com/dictionary/llm/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/tensorfold/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
