# Akademik makaleleri otomatik yazan yapay zekâ aracı

Google Research tarafından geliştirilen PaperOrchestra, ham fikirleri ve deney günlüklerini akademik formatta LaTeX taslaklarına dönüştüren çoklu ajanlı bir çerçeve (multi-agent framework). Yazılım, literatür taraması ve görsel oluşturma süreçlerini otomatikleştirerek araştırma makalesi yazımını destekliyor.

- ★ 4.162
- Python
- GitHub Trending · 2026-11-17

## Güncelleme

- **18 Kasım 2026:** Yıldız 1.732 → 4.162.

## Ne kazandırır?

- Ham fikirleri akademik formata dönüştürür
- Literatür taramasını otomatik yapar
- Gerekli görselleri ve grafikleri oluşturur

## Kurulum

**Gerekli ortamı kurma**

```
conda create -n paper_orchestra python=3.11
    conda activate paper_orchestra
    pip install -r requirements.txt
```

## Çalıştırma

**Betik ile çalıştırma**

```
./paper_writing_cli.sh
```

**Komut satırı ile çalıştırma**

```
python paper_writing_cli.py \
  --raw_materials_dir /path_to_your_raw_materials/ \
  --latex_template_dir /path_to_your_latex_template/ \
  --output_dir /path_to_your_output_folder/ \
  --use_plotting true
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Araştırma fikirlerimi ve deney günlüklerimi akademik makale taslağına dönüştürmek istiyorum. Bunun için öncelikleconda create -n paper_orchestra python=3.11
conda activate paper_orchestra
pip install -r requirements.txt komutunu çalıştırarak gerekli bağımlılıkları kur. Ardından makale yazım sürecini başlatmak için ./paper_writing_cli.sh komutunu kullan.

Depo: https://github.com/google-research/paper-orchestra. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Araştırma makalesi yazım sürecini otomatikleştirerek akademik taslaklar hazırlamak isteyen araştırmacılar içindir.
- **Lisans:** Apache-2.0

## Bağlantılar

- [GitHub deposu →](https://github.com/google-research/paper-orchestra)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-11-17 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Multi-Agent Framework](https://trescout.com/dictionary/multi-agent-framework/)
- [Multi-agent](https://trescout.com/dictionary/multi-agent/)
- [Framework](https://trescout.com/dictionary/framework/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/paper-orchestra/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
