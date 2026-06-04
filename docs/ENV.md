# Environment Variables

Bu repo Vercel'a deploy edildiğinde gerekli olan environment değişkenleri.

## Production (Vercel · `trescout-landing` project)

| Key | Zorunlu | Açıklama |
|---|---|---|
| `RESEND_API_KEY` | ✅ | Resend API key · "Full access" veya minimum `audiences:write` + `emails:send` scope'lu |
| `RESEND_AUDIENCE_ID` | ✅ | Resend Audience UUID · erken erişim e-postaları buraya kaydedilir |

## Kurulum adımları

### 1. Resend Audience oluştur

1. https://resend.com/audiences → **Create Audience**
2. Name: `TreScout Early Access`
3. Audience oluştuktan sonra ID'yi kopyala (`aud_...` formatında veya UUID)

### 2. Resend API key

1. https://resend.com/api-keys → **Create API Key**
2. Name: `trescout-landing-production`
3. Permission: **Full access** (veya minimum `audiences:write` + `emails:send`)
4. Domain: `send.trescout.com` veya tüm domains
5. Key'i kopyala (`re_...` formatında) · **bir kere gösteriliyor, kaybetme**

### 3. Vercel'a env vars ekle

1. https://vercel.com → `trescout-landing` projesi
2. **Settings → Environment Variables**
3. İki değişkeni ekle:
   - `RESEND_API_KEY` = (Resend'den kopyalanan key)
   - `RESEND_AUDIENCE_ID` = (Audience ID)
4. **Production** + **Preview** environment'larında etkin olduğundan emin ol
5. Save

### 4. Redeploy

Env vars değiştiğinde Vercel otomatik redeploy etmez. Manuel tetikle:
- Vercel Dashboard → Deployments → en son deploy → "Redeploy"
- VEYA yeni commit push'la (her push otomatik deploy eder)

### 5. Test

`trescout.com` aç → hero formuna test e-postası yaz → submit.
- Beklenen: "Aldık. Yayında olduğumuzda size haber vereceğiz." inline success
- `hello@trescout.com` inbox'a Resend'den bildirim e-postası geldi mi
- Resend Dashboard → Audiences → TreScout Early Access · listede yeni contact var mı

## Local development

Vercel CLI ile local'de env vars sync edebilirsin:

```bash
npx vercel link    # repo'yu projeye bağla
npx vercel env pull .env.local    # env vars'ı çek
npx vercel dev    # local server (api/ route'ları dahil)
```

> ⚠️ `.env.local` `.gitignore`'da olmalı · API key sızıntısı olmasın.

## Güvenlik notları

- `RESEND_API_KEY` sadece sunucu tarafında kullanılır (Edge Function). Frontend'e sızmaz.
- Vercel env vars şifrelenmiş saklanır.
- Key sızdığında: Resend Dashboard'dan **revoke** → yeni key oluştur → Vercel'da güncelle → redeploy.
- API key rotation: 6 ayda bir.

---

## GitHub Actions secrets (oto-büyüme CI)

`dict-sync.yml` workflow'u (sözlük + keşif oto-büyüme) Vercel env'lerinden **ayrı** bir kasaya bakar: GitHub Actions secret store.

| Key | Nerede | Açıklama |
|---|---|---|
| `GEMINI_API_KEY` | **Org secret** (`trescout`) | dict-sync + discover-sync (zengin-oto) Gemini'yi çağırır |
| `GITHUB_TOKEN` | otomatik (`github.token`) | README/meta çekme · ekstra kurulum gerekmez |

### Org secret · görünürlük kısıtı (ÖNEMLİ)

- `GEMINI_API_KEY` **org-seviyesi** secret olarak eklendi (trescout → Settings → Secrets and variables → Actions).
- **Mevcut GitHub planında org secret'ları yalnızca PUBLIC repolara scope'lanabiliyor.**
- `trescout/landing` **public** → kapsanıyor ✅ (Action çalışır).
- `app` · `internal` · `brand-kit` · `kit-app` **private** → org public-secret onlara ulaşmaz; her biri kendi repo secret'ını kullanır (`trescout/app`'te `GEMINI_API_KEY` repo secret olarak zaten var, 2026-05-30).

### ⚠️ İleride bak (plan / görünürlük değişiklikleri)

- **landing private olursa** → org public-secret artık kapsamaz → Action `GEMINI_API_KEY`'i bulamaz. Çözüm: landing'e repo-level secret ekle, YA DA GitHub Team/Enterprise'a yüksel (org secret'ları private repolara da açılır).
- **Plan yükseltmesi (Free → Team)** → org secret'ları private repolara da scope'lanabilir → app vb. repo secret'ları org'a taşıyıp tek kaynak yapabilirsin.
- Her durumda: merge sonrası **ilk Action koşusunda** dict-sync adımının geçtiğini doğrula (secret gerçekten erişiliyor mu).

## Secret / env tam haritası (nerede ne var)

| Sır | Kasa | Kullanan |
|---|---|---|
| `RESEND_API_KEY` · `RESEND_AUDIENCE_ID` | Vercel env (runtime) | `api/subscribe` (erken-erişim funnel) |
| `GEMINI_API_KEY` | GitHub **org** secret (public repolar) | landing Action (oto-büyüme) |
| `GEMINI_API_KEY` | `trescout-app/.env.local` (yerel) | script'leri yerelde çalıştırma |
| `GEMINI_API_KEY` · `LANDING_PUSH_TOKEN` | `trescout/app` repo secret | app workflow'ları (rapor üretimi + landing'e push) |

> Üç ayrı kasa karışmasın: Vercel (funnel runtime) · GitHub Actions (CI oto-büyüme) · yerel .env.local (geliştirme). Aynı isimli secret farklı kasalarda ayrı ayrı durur.
