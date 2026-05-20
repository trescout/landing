---
name: vercel-env-sync
description: Vercel dashboard env vars ile .env.example tutarlılığı · yeni env eklenince/silinince her iki yere yansıt.
trigger: .env.local, .env.example, Vercel env vars değişikliği
applies-to:
  - ".env.example"
  - ".env.local"
  - "lib/utils/env.ts"
  - "vercel.json"
---

# Skill · Vercel Env Sync

## Ne zaman aktif

Yeni env var ekleniyor, mevcut env silinecek, isim değişiyor, veya scope (Production/Preview/Development) güncelleniyor. `AGENTS.md §4.2 Secret yönetimi` kapsamında.

## Procedure

### 1. Üçlü tutarlılık

Her env var için 3 yerde senkron olmalı:

1. **`.env.example`** · repoda · boş değer + yorum (örn. `GEMINI_API_KEY=  # ai.google.dev → Get API key`)
2. **`lib/utils/env.ts`** · Zod schema · type + validation
3. **Vercel dashboard** · gerçek değer · Production/Preview/Development scope

### 2. Yeni env eklerken

```bash
# 1. .env.example'a şablon ekle (commit edilebilir)
echo "NEW_API_KEY=  # neden gerekli, nereden alınır" >> .env.example

# 2. .env.local'a gerçek değeri yaz (commit ETME)
echo "NEW_API_KEY=sk-..." >> .env.local

# 3. lib/utils/env.ts schema'sına ekle
# NEW_API_KEY: z.string().min(1),

# 4. Vercel CLI ile push
vercel env add NEW_API_KEY production
vercel env add NEW_API_KEY preview
vercel env add NEW_API_KEY development
```

### 3. Mevcut env'leri doğrula

```bash
# Vercel'den çek, local ile karşılaştır
vercel env ls
vercel env pull .env.vercel
diff <(grep -oE "^[A-Z_]+=" .env.example | sort) <(grep -oE "^[A-Z_]+=" .env.vercel | sort)
rm .env.vercel   # geçici dosya, sil
```

### 4. Scope farkı kontrolü

| Env scope | Ne zaman aktif |
|---|---|
| **Production** | `main` branch → vercel.com/<project> |
| **Preview** | Tüm PR/branch deploy'ları |
| **Development** | `vercel dev` ile lokal · `.env.local` da fallback |

Genelde aynı değer 3 scope'ta da, ama farklı olabilir (örn. Stripe test key vs live key).

### 5. Secret refleksi

Kontrol et:
- [ ] `.env.local` `.gitignore`'da
- [ ] `.env.vercel` (geçici) commit edilmedi
- [ ] Key'in kendisi commit message'da değil
- [ ] `git log -p .env.example` ile geçmişte gerçek değer sızdırılmadı

```bash
# Geçmiş commitlerde secret tarama
git log --all -p -- .env.example | grep -iE "(sk-|api_key=[^[:space:]#]|password=)" | head
```

### 6. Schema validation

`lib/utils/env.ts`'de zod schema değişimi sonrası:

```bash
# Type check zorunlu
npm run typecheck

# Build start'ta validation çalışır mı kontrol et
npm run build   # env eksikse buradan patlamalı
```

## İyi örnek

```bash
# Resend'den webhook secret ekleniyor
echo "" >> .env.example
echo "# Resend webhook validation (https://resend.com/docs/dashboard/webhooks/introduction)" >> .env.example
echo "RESEND_WEBHOOK_SECRET=" >> .env.example

# lib/utils/env.ts'e ekle:
#   RESEND_WEBHOOK_SECRET: z.string().startsWith('whsec_').optional(),

# Vercel'e push (3 scope)
for scope in production preview development; do
  vercel env add RESEND_WEBHOOK_SECRET $scope
done

# Doğrula
vercel env ls | grep RESEND_WEBHOOK_SECRET   # 3 satır olmalı
```

## Anti-patterns

- ❌ `.env.local` veya gerçek key'i commit etmek (`AGENTS.md §4.2`)
- ❌ `.env.example`'a koymadan yeni env kullanmak (deploy patlar)
- ❌ Sadece Vercel'e ekleyip lib/utils/env.ts'i güncellememek (runtime hata sessiz)
- ❌ Production'da var, Preview'da yok (PR preview patlar)
- ❌ Schema'da `.optional()` koyup, kodda mecburi varmış gibi davranmak
- ❌ Eski env'i silmeden yenisini eklemek (kafa karışıklığı)

## Detay

- `AGENTS.md §4.2` · Secret yönetimi
- `lib/utils/env.ts` · zod schema (mevcut TreScout app pattern)
- Vercel docs · Environment Variables
- Bu skill **landing ve app reposu için** (brand-kit'te Vercel deploy yok)
- Cross-skill: [`code-review-pre`](code-review-pre.md) (PR öncesi secret tarama)
