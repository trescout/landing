# Environment Variables

Bu repo Vercel'a deploy edildiğinde gerekli olan environment değişkenleri.

## Production (Vercel · `trescout-landing` project)

| Key | Zorunlu | Açıklama |
|---|---|---|
| `RESEND_API_KEY` | ✅ | Resend API key · "Full access" veya minimum `audiences:write` + `emails:send` scope'lu |
| `RESEND_AUDIENCE_ID` | ✅ | Resend Audience UUID · erken erişim e-postaları buraya kaydedilir |
| `UPSTASH_REDIS_REST_URL` | ✅ production | Upstash Redis REST URL · dağıtık rate limit için |
| `UPSTASH_REDIS_REST_TOKEN` | ✅ production | Upstash Redis REST token · yalnız Vercel server env’de tutulur |

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

### 4. Upstash rate limit kurulumu

1. https://console.upstash.com/redis → aynı bölgeye bir Redis database oluşturun.
2. REST URL ve REST token değerlerini Vercel `trescout-landing` projesinin **Production** ve gerekiyorsa **Preview** environment’larına ekleyin.
3. `UPSTASH_REDIS_REST_URL` ve `UPSTASH_REDIS_REST_TOKEN` frontend’e, HTML asset’lerine veya GitHub Actions loglarına yazılmamalıdır.
4. Production’da bu iki değişken yoksa endpoint fail-closed davranır ve yeni kayıtları geçici olarak `503` ile durdurur; bu, dağıtık koruma varmış gibi davranıp rate limit’i sessizce atlatmaktan daha güvenlidir.

5. Redeploy

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

- `RESEND_API_KEY`, `UPSTASH_REDIS_REST_URL` ve `UPSTASH_REDIS_REST_TOKEN` sadece sunucu tarafında kullanılır (Edge Function). Frontend'e sızmaz.
- Production’da Upstash yoksa process-memory fallback kullanılmaz; endpoint kayıt kabul etmez.
- Vercel env vars şifrelenmiş saklanır.
- Key sızdığında: Resend Dashboard'dan **revoke** → yeni key oluştur → Vercel'da güncelle → redeploy.
- API key rotation: 6 ayda bir.

---

## GitHub Actions secrets (oto-büyüme CI)

`dict-sync.yml` workflow'u (sözlük + keşif oto-büyüme) Vercel env'lerinden **ayrı** bir kasaya bakar: GitHub Actions secret store.

| Key | Açıklama |
|---|---|
| `GEMINI_API_KEY` | dict-sync + discover-sync (zengin-oto) Gemini'yi çağırır · repo/org secret olarak Actions store'da |
| `GITHUB_TOKEN` | otomatik (`github.token`) · README/meta çekme · ekstra kurulum gerekmez |

> Org secret görünürlük kısıtları, plan/görünürlük değişikliği senaryoları ve
> tüm repolar arası secret-kasa haritası (nerede ne var) `trescout-internal`
> reposunda tutulur. Bu repo public olduğu için altyapı topolojisi burada
> tekrarlanmaz.
