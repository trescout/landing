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
 *   - UPSTASH_REDIS_REST_URL · production dağıtık rate limit REST URL
 *   - UPSTASH_REDIS_REST_TOKEN · production dağıtık rate limit REST token
 */

import { createRateLimiter } from './rate-limit.mjs';

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
]);

function configuredPreviewOrigins() {
  const values = [];
  const configured = process.env.TRESCOUT_PREVIEW_ORIGINS || '';
  configured.split(',').forEach(value => values.push(value.trim()));
  // Vercel exposes the exact deployment/branch host to the function. Add only
  // those exact hosts; never trust a hostname prefix or a wildcard domain.
  [process.env.VERCEL_URL, process.env.VERCEL_BRANCH_URL].forEach(host => {
    if (host) values.push(`https://${host.trim()}`);
  });
  return new Set(values.filter(value => /^https:\/\/[^/]+$/.test(value)));
}

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
    method: 'Bu yöntem desteklenmiyor',
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
  fr: {
    method: 'Méthode non autorisée',
    istek: 'Requête invalide',
    limit: 'Trop de tentatives · réessayez dans quelques minutes',
    format: 'Format de requête invalide',
    onay: 'Veuillez accepter la notice de confidentialité pour continuer',
    eposta: 'Saisissez une adresse e-mail valide',
    gecici: 'Veuillez utiliser une adresse e-mail permanente',
    sunucu: 'La configuration du serveur est incomplète',
    kayit: 'Inscription impossible, veuillez réessayer',
    baglanti: 'Erreur de connexion, veuillez réessayer',
  },
  pt: {
    method: 'Método não permitido',
    istek: 'Solicitação inválida',
    limit: 'Muitas tentativas · tente novamente em alguns minutos',
    format: 'Formato de solicitação inválido',
    onay: 'Aceite o aviso de privacidade para continuar',
    eposta: 'Digite um endereço de e-mail válido',
    gecici: 'Use um endereço de e-mail permanente',
    sunucu: 'A configuração do servidor está incompleta',
    kayit: 'Não foi possível fazer sua inscrição; tente novamente',
    baglanti: 'Erro de conexão; tente novamente',
  },
  es: {
    method: 'Método no permitido',
    istek: 'Solicitud no válida',
    limit: 'Demasiados intentos · inténtelo de nuevo en unos minutos',
    format: 'Formato de solicitud no válido',
    onay: 'Acepte el aviso de privacidad para continuar',
    eposta: 'Introduzca una dirección de correo válida',
    gecici: 'Utilice una dirección de correo permanente',
    sunucu: 'Falta la configuración del servidor',
    kayit: 'No se pudo completar el registro; inténtelo de nuevo',
    baglanti: 'Error de conexión; inténtelo de nuevo',
  },
  de: {
    method: 'Methode nicht erlaubt',
    istek: 'Ungültige Anfrage',
    limit: 'Zu viele Versuche · versuchen Sie es in einigen Minuten erneut',
    format: 'Ungültiges Anfrageformat',
    onay: 'Stimmen Sie dem Datenschutzhinweis zu, um fortzufahren',
    eposta: 'Geben Sie eine gültige E-Mail-Adresse ein',
    gecici: 'Verwenden Sie bitte eine dauerhafte E-Mail-Adresse',
    sunucu: 'Die Serverkonfiguration fehlt',
    kayit: 'Die Anmeldung konnte nicht abgeschlossen werden; bitte erneut versuchen',
    baglanti: 'Verbindungsfehler; bitte erneut versuchen',
  },
};
const SUPPORTED_LANGS = new Set(Object.keys(MESAJ));
function errorResponse(messages, code, status) {
  return jsonResponse({ error: messages[code], code }, status);
}

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
    // Preview yalnızca açıkça yapılandırılmış veya Vercel’in bu deployment için
    // verdiği exact origin ile kabul edilir.
    if (process.env.VERCEL_ENV !== 'production' && configuredPreviewOrigins().has(origin)) {
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
 * Per-IP rate limit · 10 dakikada 5 istek.
 *
 * Production’da Upstash Redis REST pipeline kalıcı/dağıtık sayaç olarak kullanılır.
 * Upstash env’leri yoksa yalnız local/preview geliştirmede process-memory fallback
 * çalışır; Vercel production’da endpoint fail-closed davranır. Böylece dağıtık
 * koruma yokken varmış gibi davranıp Resend/Audience çağrılarını açık bırakmayız.
 * Honeypot + origin check + Cloudflare/WAF katmanları ayrıca korunur.
 */
const rateLimiter = createRateLimiter();

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
    const firstSegment = new URL(ref).pathname.split('/').filter(Boolean)[0] || 'tr';
    return SUPPORTED_LANGS.has(firstSegment) ? firstSegment : 'tr';
  } catch {
    return 'tr';
  }
}

export default async function handler(req) {
  const M = MESAJ[dilSec(req)];

  if (req.method !== 'POST') {
    return errorResponse(M, 'method', 405);
  }

  // CSRF · origin check
  const origin = req.headers.get('origin');
  if (!isOriginAllowed(origin)) {
    console.warn('Blocked origin');
    return errorResponse(M, 'istek', 403);
  }

  // Rate limit · pahalı Resend çağrılarından önce
  const ip = clientIp(req);
  const rateLimit = await rateLimiter.check(ip);
  if (rateLimit.unavailable) {
    return errorResponse(M, 'baglanti', 503);
  }
  if (rateLimit.limited) {
    console.warn('Rate limited request');
    return errorResponse(M, 'limit', 429);
  }

  let body;
  try {
    const contentType = (req.headers.get('content-type') || '').toLowerCase();
    if (contentType.includes('application/json')) {
      body = await req.json();
    } else if (contentType.includes('application/x-www-form-urlencoded')) {
      body = Object.fromEntries(new URLSearchParams(await req.text()));
    } else if (contentType.includes('multipart/form-data')) {
      body = Object.fromEntries(await req.formData());
    } else {
      return errorResponse(M, 'format', 400);
    }
  } catch {
    return errorResponse(M, 'format', 400);
  }

  // Honeypot · bot filtresi · görünmez input, dolu gelirse bot
  const honeypot = (body.hp || body.website || '').toString().trim();
  if (honeypot.length > 0) {
    // Sessizce başarılı dön · bot kayıt olduğunu sanmasın, sistem girmesin
    console.warn('Honeypot triggered');
    return jsonResponse({ ok: true });
  }

  const email = (body.email || '').toString().trim().toLowerCase();
  const source = (body.source || 'unknown').toString().slice(0, 32);
  // Kayıt hangi sayfadan geldi · data-source sayfa TİPİNİ veriyor (ör. tüm
  // 488 İngilizce sözlük sayfası 'dictionary-en'), path tek girdiyi veriyor.
  const path = (body.path || '').toString().slice(0, 120).replace(/[^\w\-/.]/g, '');
  const consent = body.consent === true || body.consent === 'true' || body.consent === 'on';

  if (!consent) {
    return errorResponse(M, 'onay', 400);
  }

  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_REGEX.test(email)) {
    return errorResponse(M, 'eposta', 400);
  }

  // Disposable email check
  const domain = email.split('@')[1];
  if (DISPOSABLE_DOMAINS.has(domain)) {
    return jsonResponse(
      { error: M.gecici, code: 'gecici' },
      400
    );
  }

  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;

  if (!apiKey || !audienceId) {
    console.error('Missing env vars: RESEND_API_KEY or RESEND_AUDIENCE_ID');
    return errorResponse(M, 'sunucu', 500);
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
      await audienceRes.text().catch(() => '');
      console.error('Resend audience add failed:', audienceRes.status);
      return errorResponse(M, 'kayit', 502);
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
      await notifyRes.text().catch(() => '');
      console.error('Notification email failed:', notifyRes.status, notifyRes.statusText);
    }

    return jsonResponse({ ok: true, duplicate: isDuplicate });
  } catch (err) {
    console.error('Subscribe error:', err instanceof Error ? err.name : 'unknown');
    return errorResponse(M, 'baglanti', 502);
  }
}
