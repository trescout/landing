---
name: brand-voice-check
description: Tüm Türkçe metinler yayınlanmadan önce marka kuralları kontrolünden geçer. Em dash, siz formal, TreScout casing, kilitli tagline kontrolü.
trigger: Türkçe metin review öncesi, commit öncesi, PR review sırasında
applies-to:
  - "**/*.md"
  - "**/*.tsx"
  - "**/*.jsx"
  - "**/*.html"
  - "**/*.json"
---

# Skill · Brand Voice Check

## Ne zaman aktif

Türkçe metin yazıldıktan sonra, commit veya PR review öncesi son denetim. `gemini-translation` skill'inin son adımı olarak da çağrılır.

## Procedure

Kontrol listesi · her madde geçer olana kadar:

### Voice

- [ ] **"siz" formal Türkçe** her yerde · "sen" yasak
- [ ] **3. kişi anlatımı** · "biz olarak", "ekibimiz" kullanma

### Noktalama (TDK)

- [ ] **Em dash yok** · `—` veya `–` aranmayacak · yerine `,` `.` `:` `;` `·`
- [ ] **", ama" virgülü yok** · Türkçede `ama`'dan önce virgül kullanılmaz
- [ ] **"..." sonrası büyük harf** ile devam
- [ ] **":" sonrası tam cümle gelirse büyük harf**
- [ ] **Tırnak içi tam cümle** → nokta içeride, ifade ise nokta dışarıda

### Marka adı

- [ ] **TreScout** (T+S büyük, Title Case)
- [ ] Yanlış varyantlar: ❌ Trescout, ❌ trescout, ❌ TRESCOUT, ❌ TreSout

### Tagline (kilitli, değiştirme!)

- [ ] Hero: "Teknoloji takibi artık bir iş yükü değil."
- [ ] Mid: "TreScout tarar, özetler, gönderir. Siz sadece okursunuz."
- [ ] Sub: "GitHub, Hacker News, HuggingFace ve daha fazlası. Kendi temponuzda, istediğiniz saatte."

### Pazarlama dolgu yok

- [ ] "Oldukça", "son derece", "önemli ölçüde" gibi anlam boşaltan zarflar yok
- [ ] "Şekillendiren", "ayak izi bırakan", "yepyeni" gibi pazarlama dolgu kelimeleri yok
- [ ] "Gelin birlikte bakalım" tarzı çağrı kalıpları yok
- [ ] Tek kelimelik dramatik açılış yok ("Dönüşüm." gibi)

## Hızlı kontrol komutları

```bash
# Em dash kontrolü (yasak)
grep -rn -E "—|–" path/ && echo "✗ Em dash bulundu, düzelt"

# Yanlış marka adı kontrolü
grep -rn -E "(Trescout|trescout|TRESCOUT|TreSout)" path/ && echo "✗ Yanlış marka adı"

# Tagline değişikliği kontrolü (hero için)
grep -rn "Teknoloji takibi" path/ | grep -v "artık bir iş yükü değil" && echo "✗ Hero tagline değiştirilmiş"
```

## Anti-patterns

- ❌ "TreScout olarak..." cümle başlangıcı (marka adını cümlede zorlama)
- ❌ "...olduğunu gözlemliyoruz / değerli buluyoruz" gibi yorum kalıpları (bilgi ver, yorum yapma)
- ❌ Em dash (Türkçe imlada yok)
- ❌ Tagline'larda kelime değişikliği

## İyi örnek (PR review yorumu)

> "Hero metninde em dash kullanılmış (`teknoloji — değil` → `teknoloji, değil`). Tagline'a `daha fazlası` eklenmiş, kilitli kelime listesinde yok. Düzeltip Gemini'den geçirin."

## Detay

- `AGENTS.md §6` · marka kuralları özeti
- `trescout-brand-kit/docs/BRAND.md` · canonical brand kit (ayrı repo)
- Tagline kilitli · değişiklik için marka kurulu kararı gerekir
