/**
 * /api/subscribe · TreScout erken erişim form endpoint
 *
 * Akış:
 *   1. POST { email, source } → validate
 *   2. Resend Audience'a contact ekle (lansman maili buradan gönderilecek)
 *   3. hello@trescout.com'a bildirim e-postası
 *   4. JSON { ok: true } döndür
 *
 * Gerekli env vars (Vercel dashboard'da):
 *   - RESEND_API_KEY · Resend'den "Full access" scope'lu API key
 *   - RESEND_AUDIENCE_ID · Resend Audience UUID
 */

export const config = { runtime: 'edge' };

const RESEND_API = 'https://api.resend.com';
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MAX_EMAIL_LENGTH = 254;
const NOTIFY_TO = 'hello@trescout.com';
const NOTIFY_FROM = 'TreScout · Erken Erişim <hello@send.trescout.com>';

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8' }
  });
}

export default async function handler(req) {
  if (req.method !== 'POST') {
    return jsonResponse({ error: 'Method not allowed' }, 405);
  }

  let body;
  try {
    body = await req.json();
  } catch {
    return jsonResponse({ error: 'Geçersiz istek formatı' }, 400);
  }

  const email = (body.email || '').toString().trim().toLowerCase();
  const source = (body.source || 'unknown').toString().slice(0, 32);

  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_REGEX.test(email)) {
    return jsonResponse({ error: 'Geçerli bir e-posta adresi girin' }, 400);
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
