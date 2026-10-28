# Yapay zekâ altyapınız için güvenlik denetimi

AI-Infra-Guard, ajanları, becerileri, MCP'yi ve yapay zekâ altyapısını tarayan, ayrıca LLM jailbreak değerlendirmeleri yapan uçtan uca bir yapay zekâ kırmızı ekip platformudur.

- ★ 6.935
- Python
- GitHub Trending · 2026-08-20

## Güncelleme

- **22 Ekim 2026:** Yıldız 6.878 → 6.935, son sürüm v4.6.7 (22 Ekim 2026).
- **15 Ekim 2026:** Yıldız 6.788 → 6.878, son sürüm v4.6.6 (15 Ekim 2026).
- **8 Ekim 2026:** Yıldız 6.650 → 6.788, son sürüm v4.6.5 (8 Ekim 2026).
- **1 Ekim 2026:** Yıldız 6.595 → 6.650, son sürüm v4.6.4 (1 Ekim 2026).

## Ne kazandırır?

- Yapay zekâ sistemlerindeki güvenlik açıklarını tarar.
- Ajan yeteneklerini ve model güvenliğini analiz eder.
- Jailbreak saldırılarına karşı koruma sağlar.

## Kurulum

**Docker ile hızlı kurulum**

```
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
# For Docker Compose V2+, replace 'docker-compose' with 'docker compose'
docker-compose -f docker-compose.images.yml up -d
```

**Tek komutla otomatik kurulum**

```
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/refs/heads/main/docker.sh | bash
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

AI-Infra-Guard platformunu kullanarak yapay zekâ altyapımdaki güvenlik açıklarını nasıl tespit edebilirim? Özellikle ajan tabanlı sistemlerdeki yetenek taraması ve jailbreak değerlendirmesi süreçlerini başlatmak için izlemem gereken adımları açıkla.

Depo: https://github.com/Tencent/AI-Infra-Guard. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ modelleri ve ajan tabanlı sistemler geliştiren, altyapı güvenliğini proaktif şekilde denetlemek isteyen yazılım geliştiriciler ve güvenlik uzmanları içindir.
- **Lisans:** Apache-2.0

## Editoryal not

Güvenlik notu: Bu araç yalnızca sahip olunan veya açıkça yetkilendirilen AI servisleri, agent/MCP sunucuları ve ağ hedeflerinde kullanılmalıdır. Ağ probe’larını ve jailbreak test setlerini kamu hedeflerine karşı çalıştırmayın; API anahtarlarını ve sonuçları koruyun. WebUI’yi localhost veya erişim kontrollü ağla sınırlayın.

## Bağlantılar
- [GitHub deposu →](https://github.com/Tencent/AI-Infra-Guard)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-08-20 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Jailbreak](https://trescout.com/dictionary/jailbreak/)
- [MCP](https://trescout.com/dictionary/mcp/)
- [LLM](https://trescout.com/dictionary/llm/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ai-infra-guard/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
