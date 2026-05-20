---
name: kvkk-content-review
description: KVKK metni (gizlilik politikası, aydınlatma metni, açık rıza) değişikliği · Türkiye hukuki kontrol + marka voice ile.
trigger: privacy.html, kvkk.md, gizlilik politikası, cookie banner, aydınlatma metni değişikliği
applies-to:
  - "privacy.html"
  - "**/kvkk*"
  - "**/gizlilik*"
  - "**/legal/**"
---

# Skill · KVKK Content Review

## Ne zaman aktif

KVKK (Kişisel Verilerin Korunması Kanunu · 6698 sayılı kanun) kapsamına giren metin değişiyor. Gizlilik politikası, aydınlatma metni, açık rıza beyanı, cookie banner, veri ihlali bildirimi.

## Procedure

### 1. Temel kontrol listesi (KVKK §10 aydınlatma yükümlülüğü)

Metin şunları **açıkça** belirtmeli:

- [ ] **Veri sorumlusu kimliği** · "TreScout / [şirket adı]" + iletişim adresi
- [ ] **Hangi veri toplanıyor** · e-posta, IP, çerez, kullanım verisi, kaynak
- [ ] **Hangi amaçla** · hizmet sunumu, marketing, analiz, yasal yükümlülük
- [ ] **Hukuki sebep** · KVKK §5/2 maddelerinden hangisi (sözleşme, meşru menfaat, açık rıza vb.)
- [ ] **Aktarım** · kimlere, hangi ülkelere (yurt içi/dışı), gerekçesiyle
- [ ] **Saklama süresi** · ne kadar tutulacak, nasıl silinecek
- [ ] **Veri sahibi hakları** · §11 maddesine atıf (erişim, düzeltme, silme, itiraz, vb.)
- [ ] **Başvuru yolu** · iletişim e-postası, başvuru formu link'i

### 2. Açık rıza vs örtülü onay ayrımı

- **Açık rıza** · işaretli kutu **boş**, kullanıcı manuel işaretler. Marketing, profilleme, hassas veri için gerek
- **Örtülü onay** · sözleşme/yasal yükümlülük gereği, açık rıza gerekmez (kayıt-üyelik, ödeme)
- **YASAK:** pre-checked checkbox açık rıza için (GDPR + KVKK her ikisi de yasak sayar)

### 3. Cookie banner uyumu

- [ ] Reddetme seçeneği "Kabul Et"le **aynı görünürlükte**
- [ ] Zorunlu çerezler ayrı kategoride, opt-out edilemez · bunu açıkça belirt
- [ ] 3rd-party çerezler (GA, Vercel Analytics, vb.) ayrı liste
- [ ] "Tümünü kabul et" tek tıkla mümkün ama **"reddet" de aynı şekilde**
- [ ] Banner kapatılana kadar non-essential cookie set EDİLMEMELİ

### 4. Türkçe hukuki dil kontrolü

[`brand-voice-check`](brand-voice-check.md) skill'ini tetikle, ek olarak:

- [ ] "siz" formal, ama hukuki üslup (örn. "tarafınızca", "ilgili kişi")
- [ ] Em dash yok
- [ ] Belirsiz ifade yok ("muhtemelen", "bazen", "genellikle")
- [ ] Kanun referansları doğru numarayla (KVKK §10, §11, §12)
- [ ] Yabancı terim varsa parantez içinde Türkçe karşılığıyla

### 5. Versiyon ve tarih

- [ ] Sayfa altında "Son güncelleme: YYYY-MM-DD" var
- [ ] Önceki sürümler git history'de saklanıyor (asla overwrite-only değil)
- [ ] Önemli değişiklik için kullanıcılara bildirim mekanizması (mail, in-app)

## İyi örnek

> "TreScout, Kişisel Verilerin Korunması Kanunu (6698 sayılı KVKK) kapsamında **veri sorumlusu** sıfatıyla hareket eder. Tarafımızca işlenen kişisel veriler:
> - E-posta adresi (hizmet sunumu · KVKK §5/2-c sözleşme),
> - IP adresi ve oturum bilgisi (güvenlik · §5/2-e meşru menfaat),
> - Tercih çerezleri (deneyim iyileştirme · §5/1 açık rıza).
>
> Veri sahibi olarak §11'de belirtilen haklarınızı `[email]` üzerinden kullanabilirsiniz.
> Son güncelleme: 2026-05-12."

## Anti-patterns

- ❌ "Bazı verilerinizi işliyoruz" gibi belirsiz ifade
- ❌ Pre-checked açık rıza checkbox
- ❌ Cookie banner "Kabul Et" buton'u görünür, "Reddet" gizli/küçük
- ❌ Veri sorumlusu adı/iletişimi eksik
- ❌ Hukuki sebep belirtilmemiş ("topluyoruz" deyip dururuz)
- ❌ Saklama süresi "süresiz" veya hiç belirtilmemiş
- ❌ Türkçesi çevrilmiş GDPR metni hissi veren (Gemini'den geçmemiş)

## Detay

- KVKK · 6698 sayılı kanun · kişisel-verilerin-korunmasi-kanunu
- Madde §5 (işleme şartları), §10 (aydınlatma), §11 (haklar), §12 (güvenlik tedbirleri)
- VERBİS kayıt yükümlülüğü ayrı bir kontrol · veri sorumlusu sicili
- Cross-skill: [`brand-voice-check`](brand-voice-check.md) (Türkçe hukuki dil için)
- TreScout için tipik dosya: `privacy.html`, gelecekte `kvkk.md`
