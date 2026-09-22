# Agent Skills nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Agent skills (Türkçe karşılığıyla **ajan yetenekleri**), bir ajanın belirli bir görevi tutarlı biçimde yapması için gereken talimatları, araçları ve kaynakları bir araya getiren paketlerdir.

## Tanım ve Kelime Kökeni
Bir skill, ajana hangi işi ne zaman ve hangi sınırlar içinde yapacağını anlatır. Arama, dosya okuma veya kod çalıştırma gibi araçlara erişim sağlayabilir; ancak her skill doğrudan bir araç değildir. İyi tasarlanmış skill, gerekli bağlamı ve doğrulama adımlarını açıkça tanımlar.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Platform:** Hazır yetenek kütüphaneleri.
- **Otomasyon:** Zamanlanmış görevler.
- **Geliştirme:** Depo ve test araçları.

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
- **Çakı:** Bıçak, tornavida ve makas takımı.
- **Alet çantası:** İşe göre seçilen anahtar.
- **Uygulama mağazası:** İhtiyaca göre indirilen program.

## Bir benzetmeyle
Ajanı İsviçre çakısına benzetirseniz, yetenekler bıçak, tornavida ve makas gibi farklı işlevlerdir.

## Sıkça sorulanlar

**Yetenekleri ben mi ekliyorum?**  
Platforma göre değişir. Bazı ortamlarda hazır skill'ler seçilir, bazılarında ekip kendi skill paketlerini tanımlar.

**Her ajanın yeteneği aynı mıdır?**  
Hayır. Amaca göre özelleştirilir, veri analisti ajanla kodcu ajanın seti farklıdır.

**Güvenli midir?**  
Okuma düşük risklidir. Yazma ve ödeme işlemlerinde onay ve kapsam sınırı şarttır.

**Hazır kütüphane var mı?**  
Evet. Platformlar yaygın yetenekleri paketler, özel iş için kendiniz yazarsınız.

## İlgili terimler
- [AI Agent Skill](/dictionary/ai-agent-skill/)
- [AI Skill](/dictionary/ai-skills/)
- [Agentic Skills](/dictionary/agentic-skills/)
- [Agentic Skills Framework](/dictionary/agentic-skills-framework/)

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/agent-skills/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
