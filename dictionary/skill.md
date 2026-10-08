# Skill nedir, ne demek?

*Sözlük · Yapay Zekâ · Son güncelleme: 22 Eylül 2026*

Skill (Türkçe karşılığıyla **yetenek**), yapay zekâ asistanının dış araçla iş yapmasını sağlayan tanımlı birimdir.

## Tanım ve Kelime Kökeni

Asistanın genel konuşması yetmez; bazen dosya okuması, arama yapması gerekir. Bu özel işlevlerin her biri skill olarak tanımlanır. Kavram, sesli asistan döneminden ajan dönemine taşındı: Alexa becerilerinden bugünkü ajan yeteneklerine.

## Gündelik Hayatta Nasıl Bilinir ve Kullanılır?

**Dosya:** Belge okuma ve özetleme.
**Takvim:** Toplantı ayarlama.
**Arama:** Güncel bilgi çekme.

## Teknik Derinlik ve Mimari

Yetenek üç parçadan yazılır:

**Ad:** Modelin çağıracağı kısa isim.
**Açıklama:** Ne zaman kullanılacağının tarifi. Model seçimi buna bakarak yapar.
**Parametre şeması:** Girdi biçimi.

Örnek tanım:

```
{
  "name": "hava-durumu",
  "description": "Belirtilen şehrin güncel havasını verir",
  "parameters": { "sehir": "string" }
}
```

Akış: Kullanıcı ister, model uygun yeteneği seçer, parametreyi doldurur, araç çalışır, sonuç modele döner. Yazma yetkisi olan yeteneklerde kullanıcı onayı istenir.

## Sık Karıştırılanlar

Genel model yeteneği sanılır. Oysa burada kastedilen, asistanın dış aracı kullanma becerisidir. Model dili anlar, skill işi yapar.

## Farklı Disiplinlerde Kullanımı

**Mutfak:** Şefin elindeki bıçak ve sos teknikleri.
**Matkap:** Uca göre değişen işlev.
**Telefon:** Yüklenen her uygulama.

*Mutfak şefinin elindeki farklı aletler gibidir; şef tektir, her iş için doğru aleti seçer.*

## Sıkça Sorulanlar

**Her modelin yeteneği var mıdır?**

Hayır. Temel modeller metin üretir, yetenek asistana dış araç eklenince kazanılır.

**Yetenekler nasıl geliştirilir?**

API bağlantısı veya kod bloğuyla tanımlanır. Açıklama net yazılır, model doğru seçer.

**Güvenli midir?**

Okuma yetenekleri düşük risklidir. Yazma ve ödeme gibi işlemlerde onay ve kapsam sınırı şarttır.

**Kimler yetenek yazar?**

Geliştiriciler yazar, platformlar mağazada dağıtır. İyi açıklama yazmak işin yarısıdır.

## İlgili terimler

- [AI Agent](https://trescout.com/dictionary/ai-agent/)
- [AI Skill](https://trescout.com/dictionary/ai-skills/)
- [Agent Skills](https://trescout.com/dictionary/agent-skills/)
- [Tools](https://trescout.com/dictionary/tools/)
- [AI Capabilities](https://trescout.com/dictionary/ai-capabilities/)

## İlgili araçlar

- [Anthropic Skills](https://trescout.com/discover/anthropic-skills/)
- [Taste Skill](https://trescout.com/discover/taste-skill/)
- [Archify](https://trescout.com/discover/archify/)
- [Awesome Claude Skills](https://trescout.com/discover/awesome-claude-skills/)
- [Last30days Skill](https://trescout.com/discover/last30days-skill/)
- [I Have Adhd](https://trescout.com/discover/i-have-adhd/)
- [Reverse Skill](https://trescout.com/discover/reverse-skill/)
- [Book to Skill](https://trescout.com/discover/book-to-skill/)

Bu açıklama TreScout için sade dille hazırlandı · yanlış ya da eksik gördüğünüz bir şey olursa [hello@trescout.com](mailto:hello@trescout.com). TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.

---
Kaynak: TreScout Teknoloji Sözlüğü · https://trescout.com/dictionary/skill/
TreScout her gün GitHub, Hacker News ve HuggingFace trendlerini Türkçe özetler.
