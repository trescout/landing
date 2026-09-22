# Agent Skills nedir, ne demek?

**Kategori:** Yapay Zekâ  
**Son güncelleme:** 2026-09-22

Agent skills (Türkçe karşılığıyla **ajan yetenekleri**), ajanların iş yapan araç setleridir.

## Tanım ve Kelime Kökeni
Ajan dünyayla yetenekleriyle konuşur: Arama yapar, dosya okur, kod çalıştırır. Yetenek çokluğu değil, doğru yetenek işi bitirir. Kavram sesli asistan becerilerinden ajan dönemine taşındı.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?
- **Platform:** Hazır yetenek kütüphaneleri.
- **Otomasyon:** Zamanlanmış görevler.
- **Geliştirme:** Depo ve test araçları.

## Teknik Derinlik ve Mimari
Yetenek tarifi:

```
{
  "name": "dosya-oku",
  "description": "Belirtilen dosyayı okur",
  "parameters": { "yol": "string" }
}
```

Akış: Görev gelir, ajan açıklamaya bakıp yeteneği seçer, parametreyi doldurur, sonucu değerlendirir. Yazma yetkisi onay ister. Kural: Az ve net yetenek, çok ve muğlak yetenekten iyidir.

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
Genellikle evet. Araçları siz tanımlarsınız veya hazır kütüphaneden seçersiniz.

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
