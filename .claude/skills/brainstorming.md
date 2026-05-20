---
name: brainstorming
description: Socratic design refinement · belirsiz scope ya da mimari karar varken doğrudan koda atlamadan önce.
trigger: Belirsiz scope · mimari karar · "ne yapmalıyız" sorusu · yeni feature başlangıcı
applies-to:
  - "**/*"
---

# Skill · Brainstorming

## Ne zaman aktif

Kullanıcı net olmayan bir istek sunduysa, mimari karar gerekiyorsa, scope belirsizse. `CLAUDE.md §1 "Kodlamadan Önce Düşün"` prensibinin somut hali. `AGENTS.md §3.a` Plan moment'iyle örtüşür.

## Procedure

Socratic dialogue · sırayla sor (her cevap aldıktan sonra bir sonraki):

### 1. Ne çözüyoruz?

- Problemin tanımı net mi?
- "Şu an X yapıyoruz, sonuç Y, hedef Z" formatında ifade edebiliyor musun?
- Çözüm değil **problem** üzerine konuş

### 2. Kim için?

- Son kullanıcı kim? (TreScout abonesi · landing ziyaretçisi · iç geliştirici)
- Onların bağlamı nedir?
- Bu çözüm onlar için NEDEN değerli?

### 3. Başarı kriteri ne?

- Nasıl ölçeceğiz?
- "X tamamlandı" diyebilmek için ne olmalı?
- Test edilebilir mi? (`CLAUDE.md §4 Hedef Odaklı`)

### 4. Alternatifler ne?

- En az 2 yaklaşım sun
- Her birinin trade-off'larını belirt
- En basit hangisi? (`CLAUDE.md §2 Önce Basitlik`)

### 5. Plan

Kararı verince kısa plan:

```
1. [Adım] → doğrula: [check]
2. [Adım] → doğrula: [check]
```

Sonra koda geç.

## İyi örnek

> **Kullanıcı:** "Hero section'a bir form eklemeliyiz."
>
> **Brainstorming:**
> - Ne çözüyoruz? → "İlk dönüşüm oranı düşük, lead capture eksik"
> - Kim için? → "Landing ziyaretçileri, anonim, ilk kez gelmiş"
> - Başarı kriteri? → "Hafta sonu %5 → %12 dönüşüm"
> - Alternatifler?
>   1. Tally embed (hızlı, marka kısıtlı) ✓ önerilen
>   2. Custom form + Resend (uzun, esnek)
> - Plan: Tally embed kur → spam kontrolü → analytics → A/B test

## Anti-patterns

- ❌ Doğrudan koda atlamak ("hemen yazayım")
- ❌ Tek alternatif sunmak (trade-off görünmez)
- ❌ Başarı kriteri vermeden başlamak ("güzel olsun" çok zayıf)
- ❌ "İhtimal X gerekebilir" diye spekülatif scope eklemek

## Detay

- `CLAUDE.md §1` · "Kodlamadan Önce Düşün · varsayma, sor"
- `AGENTS.md §3.a` · "Plan moment'i · ne yapacağız, niye?"
- Kaynak: obra/superpowers `brainstorming` skill'i
