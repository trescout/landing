/**
 * /api/subscribe · TreScout erken erişim form endpoint
 *
 * Akış:
 *   1. CSRF origin check + honeypot · bot/saldırı filtresi
 *   2. POST { email, source, hp } → validate (strict regex + length + disposable check)
 *   3. Resend Audience'a contact ekle (lansman maili buradan gönderilecek)
 *   4. hello@trescout.com'a bildirim e-postası
 *   5. JSON { ok: true } döndür
 *
 * Güvenlik katmanları:
 *   - Origin check (CSRF)
 *   - Honeypot field (bot)
 *   - Strict email validation
 *   - Disposable email domain block
 *   - Cloudflare + Vercel DDoS önünde
 *   - API key Vercel env'de · client'a sızmaz
 *
 * Gerekli env vars (Vercel dashboard'da):
 *   - RESEND_API_KEY · Resend'den "Full access" scope'lu API key
 *   - RESEND_AUDIENCE_ID · Resend Audience UUID
 */

export const config = { runtime: 'edge' };

const RESEND_API = 'https://api.resend.com';
const EMAIL_REGEX = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
const MAX_EMAIL_LENGTH = 254;
const NOTIFY_TO = 'hello@trescout.com';
// trescout.com apex verified · subdomain send.trescout.com Free tier'da
// extra domain gerektiriyor (sadece 1 domain hakkı). Apex'ten gönderiyoruz.
// İleride Pro upgrade olunca send.trescout.com'a taşınabilir.
const NOTIFY_FROM = 'TreScout · Erken Erişim <hello@trescout.com>';

/** Allowed request origins (CSRF) */
const ALLOWED_ORIGINS = new Set([
  'https://trescout.com',
  'https://www.trescout.com',
  'https://trescout-landing.vercel.app',
  // Vercel preview deployments
  // (production check yapılır, preview için origin.endsWith('.vercel.app') kullanılır)
]);

/** Tek seferlik/disposable email domain'leri · spam koruması */
const DISPOSABLE_DOMAINS = new Set([
  'mailinator.com', 'tempmail.com', '10minutemail.com', 'guerrillamail.com',
  'throwaway.email', 'trashmail.com', 'temp-mail.org', 'getairmail.com',
  'sharklasers.com', 'guerrillamailblock.com', 'maildrop.cc', 'mintemail.com',
  'tempail.com', 'tempinbox.com', 'yopmail.com', 'fakeinbox.com',
  'mailcatch.com', 'spamgourmet.com', 'dispostable.com',
]);

/**
 * Kullanıcıya dönen hata metinleri · sayfanın dili neyse o.
 * İstemci `lang` gönderiyor (document.documentElement.lang). Gönderilmezse
 * Türkçe · site Türkçe doğdu, varsayılan o.
 */
const MESAJ = {
  tr: {
    method: 'Method not allowed',
    istek: 'İstek geçersiz',
    limit: 'Çok fazla deneme · birkaç dakika sonra tekrar deneyin',
    format: 'Geçersiz istek formatı',
    onay: 'Aydınlatma Metni onayı gerekli',
    eposta: 'Geçerli bir e-posta adresi girin',
    gecici: 'Lütfen kalıcı bir e-posta adresi kullanın',
    sunucu: 'Sunucu konfigürasyonu eksik',
    kayit: 'Kayıt yapılamadı, lütfen tekrar deneyin',
    baglanti: 'Bağlantı hatası, lütfen tekrar deneyin',
  },
  en: {
    method: 'Method not allowed',
    istek: 'Invalid request',
    limit: 'Too many attempts · try again in a few minutes',
    format: 'Invalid request format',
    onay: 'Please accept the privacy notice to continue',
    eposta: 'Enter a valid email address',
    gecici: 'Please use a permanent email address',
    sunucu: 'Server configuration is missing',
    kayit: 'Could not sign you up, please try again',
    baglanti: 'Connection error, please try again',
  },
};

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  });
}

function isOriginAllowed(origin) {
  if (!origin) return false;
  if (ALLOWED_ORIGINS.has(origin)) return true;
  try {
    const url = new URL(origin);
    // Sadece BU projenin preview deploy'ları · ham *.vercel.app herhangi bir
    // üçüncü taraf Vercel sitesinin CSRF check'ini geçmesine izin verirdi.
    if (
      url.protocol === 'https:' &&
      url.hostname.startsWith('trescout-landing-') &&
      url.hostname.endsWith('.vercel.app')
    ) {
      return true;
    }
    // Local dev · yalnızca production-dışı ortamda
    if (
      process.env.VERCEL_ENV !== 'production' &&
      (url.hostname === 'localhost' || url.hostname === '127.0.0.1')
    ) {
      return true;
    }
  } catch {
    return false;
  }
  return false;
}

/**
 * Best-effort per-IP rate limit · 10 dakikada 5 istek.
 *
 * Form gönderimi insan için seyrek bir işlem; 5/10dk cömert. Amaç tek kaynaktan
 * burst'ü (inbox flood / audience kirletme / Resend kota tüketimi) kesmek.
 *
 * Sınır: edge isolate-bazlı bellek · birden çok isolate/region'a yayılan
 * dağıtık saldırıyı yakalamaz ve isolate geri dönüşümünde sıfırlanır. Honeypot +
 * origin check + Cloudflare üstüne bir KATMAN. Kalıcı/garanti çözüm için Vercel
 * WAF rate-limit kuralı veya Upstash Ratelimit (kalıcı store) — bkz. docs.
 */
const RATE_WINDOW_MS = 10 * 60 * 1000;
const RATE_MAX = 5;
const rateHits = new Map(); // ip → number[] (istek timestamp'leri)

function isRateLimited(ip, now) {
  if (!ip) return false; // IP yoksa limitleyemeyiz · diğer katmanlara bırak
  const cutoff = now - RATE_WINDOW_MS;
  const hits = (rateHits.get(ip) || []).filter((t) => t > cutoff);
  hits.push(now);
  rateHits.set(ip, hits);
  // Map'in sınırsız büyümesini engelle · pencere dışı IP'leri ara sıra temizle
  if (rateHits.size > 5000) {
    for (const [k, v] of rateHits) {
      if (v.every((t) => t <= cutoff)) rateHits.delete(k);
    }
  }
  return hits.length > RATE_MAX;
}

function clientIp(req) {
  const xff = req.headers.get('x-forwarded-for');
  if (xff) return xff.split(',')[0].trim();
  return req.headers.get('x-real-ip') || '';
}

/**
 * Sayfanın dili · Referer yolundan okunur (/en/... → İngilizce).
 * Gövde daha ayrıştırılmadan da hata dönebiliyoruz (yöntem, origin, hız sınırı) ·
 * bu yüzden dili başlıktan alıyoruz, gövdedeki `lang` alanına bağlamıyoruz.
 */
function dilSec(req) {
  const ref = req.headers.get('referer') || '';
  try {
    return new URL(ref).pathname.startsWith('/en/') ? 'en' : 'tr';
  } catch {
    return 'tr';
  }
}

export default async function handler(req) {
  const M = MESAJ[dilSec(req)];

  if (req.method !== 'POST') {
    return jsonResponse({ error: M.method }, 405);
  }

  // CSRF · origin check
  const origin = req.headers.get('origin');
  if (!isOriginAllowed(origin)) {
    console.warn('Blocked origin:', origin);
    return jsonResponse({ error: M.istek }, 403);
  }

  // Rate limit · pahalı Resend çağrılarından önce
  const ip = clientIp(req);
  if (isRateLimited(ip, Date.now())) {
    console.warn('Rate limited:', ip);
    return jsonResponse({ error: M.limit }, 429);
  }

  let body;
  try {
    body = await req.json();
  } catch {
    return jsonResponse({ error: M.format }, 400);
  }

  // Honeypot · bot filtresi · görünmez input, dolu gelirse bot
  const honeypot = (body.hp || body.website || '').toString().trim();
  if (honeypot.length > 0) {
    // Sessizce başarılı dön · bot kayıt olduğunu sanmasın, sistem girmesin
    console.warn('Honeypot triggered:', honeypot.slice(0, 50));
    return jsonResponse({ ok: true });
  }

  const email = (body.email || '').toString().trim().toLowerCase();
  const source = (body.source || 'unknown').toString().slice(0, 32);
  // Kayıt hangi sayfadan geldi · data-source sayfa TİPİNİ veriyor (ör. tüm
  // 488 İngilizce sözlük sayfası 'dictionary-en'), path tek girdiyi veriyor.
  const path = (body.path || '').toString().slice(0, 120).replace(/[^\w\-/.]/g, '');
  const consent = body.consent === true || body.consent === 'true';

  if (!consent) {
    return jsonResponse({ error: M.onay }, 400);
  }

  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_REGEX.test(email)) {
    return jsonResponse({ error: M.eposta }, 400);
  }

  // Disposable email check
  const domain = email.split('@')[1];
  if (DISPOSABLE_DOMAINS.has(domain)) {
    return jsonResponse(
      { error: 'Lütfen kalıcı bir e-posta adresi kullanın' },
      400
    );
  }

  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;

  if (!apiKey || !audienceId) {
    console.error('Missing env vars: RESEND_API_KEY or RESEND_AUDIENCE_ID');
    return jsonResponse({ error: M.sunucu }, 500);
  }

  try {
    // 1. Resend Audience'a kişiyi ekle (idempotent · varsa update eder)
    const audienceRes = await fetch(
      `${RESEND_API}/audiences/${audienceId}/contacts`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, unsubscribed: false })
      }
    );

    if (!audienceRes.ok && audienceRes.status !== 409) {
      // 409 = contact zaten var · sorun değil, devam et
      const errText = await audienceRes.text();
      console.error('Resend audience add failed:', audienceRes.status, errText);
      return jsonResponse({ error: M.kayit }, 502);
    }

    // 2. hello@'a bildirim e-postası
    const isDuplicate = audienceRes.status === 409;
    const notifySubject = isDuplicate
      ? `Tekrar kayıt: ${email}`
      : `Yeni erken erişim kaydı: ${email}`;

    const notifyRes = await fetch(`${RESEND_API}/emails`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from: NOTIFY_FROM,
        to: NOTIFY_TO,
        subject: notifySubject,
        text: [
          `E-posta: ${email}`,
          `Kaynak: ${source}`,
          path ? `Sayfa: https://trescout.com${path}` : '',
          `Tarih: ${new Date().toISOString()}`,
          isDuplicate ? 'Not: Bu e-posta listede zaten kayıtlıydı.' : ''
        ].filter(Boolean).join('\n')
      })
    });

    // Notification başarısız olsa da kullanıcıya 'ok' döneriz · audience'a kayıt
    // zaten oldu. Ama hatayı Vercel logs'a basarız, debug için.
    if (!notifyRes.ok) {
      const errText = await notifyRes.text().catch(() => '');
      console.error(
        'Notification email failed:',
        notifyRes.status,
        notifyRes.statusText,
        errText.slice(0, 500),
      );
    }

    return jsonResponse({ ok: true, duplicate: isDuplicate });
  } catch (err) {
    console.error('Subscribe error:', err);
    return jsonResponse({ error: M.baglanti }, 502);
  }
}
