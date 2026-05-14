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
const NOTIFY_FROM = 'TreScout · Erken Erişim <hello@send.trescout.com>';

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

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  });
}

function isOriginAllowed(origin) {
  if (!origin) return false;
  if (ALLOWED_ORIGINS.has(origin)) return true;
  // Vercel preview deployments · *.vercel.app subdomain
  try {
    const url = new URL(origin);
    if (url.hostname.endsWith('.vercel.app')) return true;
    // Local dev
    if (url.hostname === 'localhost' || url.hostname === '127.0.0.1') return true;
  } catch {
    return false;
  }
  return false;
}

export default async function handler(req) {
  if (req.method !== 'POST') {
    return jsonResponse({ error: 'Method not allowed' }, 405);
  }

  // CSRF · origin check
  const origin = req.headers.get('origin');
  if (!isOriginAllowed(origin)) {
    console.warn('Blocked origin:', origin);
    return jsonResponse({ error: 'İstek geçersiz' }, 403);
  }

  let body;
  try {
    body = await req.json();
  } catch {
    return jsonResponse({ error: 'Geçersiz istek formatı' }, 400);
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
  const consent = body.consent === true || body.consent === 'true';

  if (!consent) {
    return jsonResponse({ error: 'Aydınlatma Metni onayı gerekli' }, 400);
  }

  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_REGEX.test(email)) {
    return jsonResponse({ error: 'Geçerli bir e-posta adresi girin' }, 400);
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
    return jsonResponse({ error: 'Sunucu konfigürasyonu eksik' }, 500);
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
      return jsonResponse({ error: 'Kayıt yapılamadı, lütfen tekrar deneyin' }, 502);
    }

    // 2. hello@'a bildirim e-postası
    const isDuplicate = audienceRes.status === 409;
    const notifySubject = isDuplicate
      ? `Tekrar kayıt: ${email}`
      : `Yeni erken erişim kaydı: ${email}`;

    await fetch(`${RESEND_API}/emails`, {
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
          `Tarih: ${new Date().toISOString()}`,
          isDuplicate ? 'Not: Bu e-posta listede zaten kayıtlıydı.' : ''
        ].filter(Boolean).join('\n')
      })
    });

    return jsonResponse({ ok: true, duplicate: isDuplicate });
  } catch (err) {
    console.error('Subscribe error:', err);
    return jsonResponse({ error: 'Bağlantı hatası, lütfen tekrar deneyin' }, 502);
  }
}
