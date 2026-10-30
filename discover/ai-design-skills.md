# Kodlama asistanlarına hazır tasarım kuralları

elayadesign/ai-design-skills, yapay zekâ kodlama araçlarının (Claude Code, Cursor, Codex, Windsurf) okuyabildiği markdown kurallar dosyasından oluşan bir tasarım becerileri koleksiyonu sunuyor. Bu proje, tasarım süreçlerini standartlaştırmak için yapay zekâ destekli araçlara yönelik rehber niteliğinde bir kaynak sağlıyor.

- ★ 12.378
- GitHub Trending · 2026-10-28

## Güncelleme

- **30 Ekim 2026:** Yıldız 11.349 → 12.378.
- **29 Ekim 2026:** Yıldız 9.826 → 11.349.

## Ne kazandırır?

- Yapay zekâ araçlarının sıfırdan uyumlu açılış sayfaları ve görsel sistemler üretmesini sağlar
- Yazı tipi, renk, boşluk ve animasyon gibi tasarım standartlarını tek dosyada toplar
- Kodlama yardımcılarının projeye özel kurallarla daha tutarlı arayüzler yazmasını mümkün kılar

## Kurulum

**Claude Code kural klasörüne ekleme**

```
mkdir -p .claude/skills
git clone https://github.com/elayadesign/ai-design-skills.git /tmp/ai-design-skills
cp -r /tmp/ai-design-skills/skills/<skill-name> .claude/skills/
```

**Yapay zekâlı kod editörü Cursor için kur**

```
mkdir -p .cursor/rules
curl -o .cursor/rules/<skill-name>.md \
  https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/<skill-name>/SKILL.md
```

## Kod bilmiyorsanız

Yapay zekâ ajanınıza (Claude Code · Codex · Antigravity) yapıştırın

Yapay zekâ kodlama aracıma tasarım kurallarını öğretmek istiyorum. Kod editörü Cursor için gerekli kural dosyasını indirmek adına lütfen şu komutları sırasıyla çalıştır: `mkdir -p .cursor/rules` ve ardından `curl -o .cursor/rules/\<skill-name>.md \
https://raw.githubusercontent.com/elayadesign/ai-design-skills/main/skills/\<skill-name>/SKILL.md`. Burada yer alan `\<skill-name>` kısmını indirmek istediğimiz kural olan `landing-page-design` ile değiştirmeyi unutma.

Depo: https://github.com/elayadesign/ai-design-skills. Kurulum ve çalıştırmada bu deponun README dosyasındaki resmî talimatları esas al.

Başlamadan önce hangi işletim sisteminde çalıştığımızı ve gerekli araçların (ör. Python, Node.js, Git, Docker) kurulu olup olmadığını kontrol et; eksik olanları bu sisteme göre adım adım kur.

Çalışmak için yeni ve boş bir klasör oluştur. Bu klasörün dışındaki dosyalarıma dokunma, hiçbir şeyi silme. Her komutu çalıştırmadan önce ne yapacağını bir cümleyle söyle.

Her adımın sonunda ekranda ne görmem gerektiğini söyle. Bir hata oluşursa hata mesajını sana olduğu gibi yapıştıracağım, birlikte düzeltelim.

- **Kimin için:** Yapay zekâ destekli kod editörleriyle estetik ve tutarlı web arayüzleri geliştirmek isteyen ürün sahipleri ile geliştiriciler içindir.
- **Lisans:** MIT

## Bağlantılar

- [GitHub deposu →](https://github.com/elayadesign/ai-design-skills)

TreScout bu aracı geliştirmedi · GitHub trendlerinde keşfedip Türkçe tanıttı. Tanıtım metni deponun kendi belgelerinden yapay zekâ ile hazırlandı. Bu sayfa deponun 2026-10-28 tarihindeki hâlini anlatır: Yıldız sayısı ve yazdığımız metin o güne aittir, depo sonrasında değişmiş olabilir. Güncel durum için depo bağlantısına bakın.

## İlgili sözlük terimleri

- [Skill](https://trescout.com/dictionary/skill/)
- [Markdown](https://trescout.com/dictionary/markdown/)
- [AI Skills](https://trescout.com/dictionary/ai-skills/)
- [Artificial Intelligence](https://trescout.com/dictionary/artificial-intelligence/)

---
Kaynak: TreScout Keşif · https://trescout.com/discover/ai-design-skills/
TreScout her gün GitHub, Hacker News ve Hugging Face'te öne çıkanları Türkçe özetler.
