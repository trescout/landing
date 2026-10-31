# Yapay zekâ kodlama ajanlarına uzmanlık kazandırın

Claude Code ve çeşitli kodlama ajanları için geliştirilen bu kütüphane, mühendislikten pazarlamaya kadar farklı alanlarda 330'dan fazla yetenek paketi (skills) ve 70'in üzerinde özel komut sunuyor. Python tabanlı bu araç seti, yapay zekâ tabanlı iş akışlarını standartlaştırmak ve üretkenliği artırmak amacıyla özelleştirilebilir betikler sağlıyor.

- ★ 29.039
- Python
- GitHub Trending · 2026-07-05

## Güncelleme

- **31 Ekim 2026:** Yıldız 29.039 → 29.039, son sürüm v2.14.5 (31 Ekim 2026).
- **31 Ekim 2026:** Yıldız 28.939 → 29.039, son sürüm v2.14.4 (30 Ekim 2026).
- **29 Ekim 2026:** Yıldız 28.795 → 28.939, son sürüm v2.14.3 (29 Ekim 2026).
- **27 Ekim 2026:** Yıldız 28.584 → 28.795, son sürüm v2.14.2 (26 Ekim 2026).

## Ne kazandırır?

- 350'den fazla hazır yetenek paketi
- Mühendislikten pazarlamaya geniş uzmanlık alanı
- 13 farklı kodlama aracıyla uyumlu çalışma

## Kurulum

**Gemini CLI kurulumu**

```
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

**OpenClaw kurulumu**

```
bash <(curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh)
```

## Çalıştırma

**Cursor için yetenekleri dönüştürme**

```
# 1. Convert all skills to all tools (takes ~15 seconds)
./scripts/convert.sh --tool all

# 2. Install into your project (with confirmation)
./scripts/install.sh --tool cursor --target /path/to/project

# Or use --force to skip confirmation:
./scripts/install.sh --tool aider --target . --force

# 3. Verify
find .cursor/rules -name "*.mdc" | wc -l  # Should show 346
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Claude Code veya kullandığın kodlama ajanı için bu kütüphanedeki yetenek paketlerini aktif et. Mühendislik, pazarlama veya C-seviyesi danışmanlık gibi alanlarda uzmanlaşmış betikleri kullanarak iş akışımı standartlaştır ve üretkenliğimi artır. İhtiyacım olan spesifik yetenekleri (örneğin güvenlik denetimi veya ürün geliştirme) projeme entegre et.

Depo: https://github.com/alirezarezvani/claude-skills. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ destekli kodlama araçlarını profesyonel iş akışlarında daha verimli ve uzman bir şekilde kullanmak isteyen yazılımcılar ve teknik ekipler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/alirezarezvani/claude-skills)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-07-05 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [AI Skills](https://trescout.com/dictionary/ai-skills/)
- [CLI](https://trescout.com/dictionary/cli/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/claude-skills/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
