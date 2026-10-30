# Belgelerinizi yapay zekâ için dönüştürün

MinerU, PDF ve Office gibi karmaşık belge formatlarını büyük dil modelleri (large language models) için uygun olan işaretleme dili (markdown) veya JSON formatına dönüştürüyor. Bu araç, yapılandırılmamış verileri ajan tabanlı iş akışlarında (agentic workflows) kullanılabilir hale getirmeyi amaçlıyor.

- ★ 82.785
- Python
- GitHub Trending · 2026-06-26

## Güncelleme

- **30 Ekim 2026:** Yıldız 81.441 → 82.785, son sürüm mineru-4.1.2-released (29 Ekim 2026).
- **11 Ekim 2026:** Yıldız 81.305 → 81.441, son sürüm mineru-4.0.12-released (11 Ekim 2026).
- **8 Ekim 2026:** Yıldız 80.819 → 81.305, son sürüm mineru-4.0.11-released (8 Ekim 2026).
- **29 Eylül 2026:** Yıldız 80.768 → 80.819, son sürüm mineru-4.0.10-released (29 Eylül 2026).

## Ne kazandırır?

- PDF ve Office dosyalarını işaretleme diline çevirir
- Yapılandırılmamış verileri ajan iş akışlarına hazırlar
- Karmaşık belge formatlarını JSON çıktısına dönüştürür

## Kurulum

**Standart kurulum**

```
pip install --upgrade pip
pip install uv
uv pip install -U "mineru[all]"
```

**Geliştirici kurulumu**

```
git clone https://github.com/opendatalab/MinerU.git
cd MinerU
uv pip install -e .[all]
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Elimdeki karmaşık PDF ve Office belgelerini yapay zekâ ajanımın anlayabileceği bir formata dönüştürmek istiyorum. MinerU aracını kullanarak bu dosyaları işaretleme dili (markdown) veya JSON formatına çevirmem gerekiyor. Bu dönüşüm sürecini nasıl başlatabilirim ve çıktıları ajan tabanlı iş akışlarımda en verimli şekilde nasıl kullanabilirim?

Depo: https://github.com/opendatalab/MinerU. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Belgelerini yapay zekâ modelleri ve ajan tabanlı sistemler için işlenebilir hale getirmek isteyen kullanıcılar içindir.

## Bağlantılar

- [GitHub deposu →](https://github.com/opendatalab/MinerU)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-06-26 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Agentic Workflows](https://trescout.com/dictionary/agentic-workflows/)
- [Workflows](https://trescout.com/dictionary/workflows/)
- [Agentic](https://trescout.com/dictionary/agentic/)
- [Markdown](https://trescout.com/dictionary/markdown/)
- [Large Language Models](https://trescout.com/dictionary/large-language-models/)
- [PDF](https://trescout.com/dictionary/pdf/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/mineru/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
