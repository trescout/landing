# Yapay zekâ kodlama ajanlarına uzmanlık kazandırın

Claude Code ve çeşitli kodlama ajanları için geliştirilen bu kütüphane, mühendislikten pazarlamaya kadar farklı alanlarda 330'dan fazla yetenek paketi (skills) ve 70'in üzerinde özel komut sunuyor. Python tabanlı bu araç seti, yapay zekâ tabanlı iş akışlarını standartlaştırmak ve üretkenliği artırmak amacıyla özelleştirilebilir betikler sağlıyor.

- ★ 20.244
- Python
- GitHub Trending · 2026-07-05

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
bash 

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
find .cursor/rules -name "*.mdc" | wc -l # Should show 346
```

## Kod bilmiyorsanız
🤖 Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın 
Claude Code veya kullandığın kodlama ajanı için bu kütüphanedeki yetenek paketlerini aktif et. Mühendislik, pazarlama veya C-seviyesi danışmanlık gibi alanlarda uzmanlaşmış betikleri kullanarak iş akışımı standartlaştır ve üretkenliğimi artır. İhtiyacım olan spesifik yetenekleri (örneğin güvenlik denetimi veya ürün geliştirme) projeme entegre et.

- **Kimin için:** Yapay zekâ destekli kodlama araçlarını profesyonel iş akışlarında daha verimli ve uzman bir şekilde kullanmak isteyen yazılımcılar ve teknik ekipler içindir. 
- **Lisans:** MIT 

## Bağlantılar
- [GitHub deposu →](https://github.com/alirezarezvani/claude-skills)

## İlgili sözlük terimleri
AI Skills CLI Artificial Intelligence 

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Yıldız ve sayılar keşif tarihindeki değerlerdir.

---
Kaynak: TreScout Keşif · https://trescout.com/discover/claude-skills/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
