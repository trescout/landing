# Agent Skills nedir, ne demek?

*Sözlük · Yapay Zekâ · Son güncelleme: 22 Eylül 2026*

Agent skills (Türkçe karşılığıyla **ajan yetenekleri**), bir ajanın belirli bir görevi tutarlı biçimde yapması için gereken talimatları, araçları ve kaynakları bir araya getiren paketlerdir.

## Tanım ve Kelime Kökeni

Bir skill, ajana hangi işi ne zaman ve hangi sınırlar içinde yapacağını anlatır. Arama, dosya okuma veya kod çalıştırma gibi araçlara erişim sağlayabilir; ancak her skill doğrudan bir araç değildir. İyi tasarlanmış skill, gerekli bağlamı ve doğrulama adımlarını açıkça tanımlar.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Platform:** Hazır yetenek kütüphaneleri.
**Otomasyon:** Zamanlanmış görevler.
**Geliştirme:** Depo ve test araçları.

## Teknik Derinlik ve Mimari

Biçim platforma göre değişir; sadeleştirilmiş bir skill tanımı şöyledir:

```
{
  "name": "dosya-ozetle",
  "description": "Belirtilen dosyadan kısa bir özet çıkarır",
  "instructions": ["Önce dosyayı oku.", "Hassas veriyi özet içinde maskele."]
}
```

Akış: Görev gelir, ajan açıklamaya göre uygun skill'i seçer, gerekli araçları çağırır ve sonucu doğrular. Yazma, ağ veya ödeme gibi etkili işlemlerde uygulamanın yetki sınırları ve gerektiğinde insan onayı devreye girer. Kural: Az ve net skill, çok ve belirsiz skill'den iyidir.

## Sık Karıştırılanlar

Genel zekâ sanılır. Oysa kastedilen belirli işi yapma becerisidir. Model anlar, yetenek yapar.

## Farklı Disiplinlerde Kullanımı

**Çakı:** Bıçak, tornavida ve makas takımı.
**Alet çantası:** İşe göre seçilen anahtar.
**Uygulama mağazası:** İhtiyaca göre indirilen program.

*Ajanı İsviçre çakısına benzetirseniz, yetenekler bıçak, tornavida ve makas gibi farklı işlevlerdir.*

## Sıkça Sorulanlar

**Yetenekleri ben mi ekliyorum?**

Platforma göre değişir. Bazı ortamlarda hazır skill'ler seçilir, bazılarında ekip kendi skill paketlerini tanımlar.

**Her ajanın yeteneği aynı mıdır?**

Hayır. Amaca göre özelleştirilir, veri analisti ajanla kodcu ajanın seti farklıdır.

**Güvenli midir?**

Okuma düşük risklidir. Yazma ve ödeme işlemlerinde onay ve kapsam sınırı şarttır.

**Hazır kütüphane var mı?**

Evet. Platformlar yaygın yetenekleri paketler, özel iş için kendiniz yazarsınız.

## İlgili terimler

- [AI Agent Skill](https://trescout.com/dictionary/ai-agent-skill/)
- [AI Skill](https://trescout.com/dictionary/ai-skills/)
- [Agentic Skills](https://trescout.com/dictionary/agentic-skills/)
- [Agentic Skills Framework](https://trescout.com/dictionary/agentic-skills-framework/)

## İlgili araçlar

- [Agent Skills](https://trescout.com/discover/agent-skills/)
- [Taste Skill](https://trescout.com/discover/taste-skill/)
- [OpenMontage](https://trescout.com/discover/openmontage/)
- [Scientific Agent Skills](https://trescout.com/discover/scientific-agent-skills/)
- [Awesome Agent Skills](https://trescout.com/discover/awesome-agent-skills/)
- [Agentskills](https://trescout.com/discover/agentskills/)
- [Text to Cad](https://trescout.com/discover/text-to-cad/)
- [Claude Obsidian](https://trescout.com/discover/claude-obsidian/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/agent-skills/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
